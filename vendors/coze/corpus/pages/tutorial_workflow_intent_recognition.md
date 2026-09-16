> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

意图识别（Intent Recognition）指通过大模型理解和判断用户表达的意图或目的。扣子编程低代码工作流中的意图识别节点可通过内置的大语言模型，对指定内容进行意图识别和分类，并根据分类流转至不同工作流分支处理。
本教程以搭建售后客服对话流为例，通过意图识别节点对用户问题进行归类，并流转至不同知识库查询节点。另外，对于非售前或售后的咨询，统一转交人工处理。
## 效果演示 {#cb3c67e8}
和售后客服对话流进行对话，其效果如下：

::::cols
@col 50
![Image=314x402](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6fc9ab17f6574999832a0d1870814988~tplv-goo7wpa0wc-image.image)


@col 50
![Image=317x270](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fcde74481f8d444eb24cfcf0e9745ee3~tplv-goo7wpa0wc-image.image)

::::

## 低代码工作流设计 {#c0099c4a}

1. 开始节点收集用户问题。
2. 创建一个对话流，在对话流中通过意图识别节点判断用户问题类型，并流转至不同分支处理。
   * 售前咨询类问题，流转至售前知识库节点，知识库召回后输出。
   * 售后类问题，流转至售后知识库节点，其中包含多项售后话术、场景问题，召回知识后输出。
   * 其他类别的问题，统一流转至文本处理分支，输出统一的文案，引导用户转人工处理。
   ![Image=2501x824](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a244db1ea83c44c5ae4dbdd2e41eb243~tplv-goo7wpa0wc-image.image)

## 核心节点配置 {#738a119f}
创建一个对话流，其核心节点配置如下：
<!-- @cols-width: 167,443,220 -->
| | | | \
|**节点名称** |**说明** |**示例** |
|---|---|---|
| | | | \
|意图识别节点 |将用户问题分为售前咨询或售后问题，每个分类提供典型示例作为分类的依据，帮助模型更精准地识别用户意图。其配置如下： |\
| | |\
| |* 模式：选择**完整模式**。完整模式可设置系统提示词，提高意图识别的准确性，但可能会影响节点的运行速度。 |\
| |* 模型：使用默认的豆包模型，你也可以按需选择效果更好的模型。 |\
| |* 输入：开启**会话历史**，默认 3 轮；query 变量值设置为开始节点的输入参数 **USER_INPUT**。 |\
| |* 意图匹配：设置两个分类，即售前咨询和售后问题。 |\
| |* 系统提示词： |\
| | |\
| |```Markdown |\
| |- 售前咨询：咨询类问题，例如对产品规格、性能、功能等方面的咨询。 |\
| |- 售后问题：产品使用相关的问题，例如如何设置xxx、怎么开启xxx、；产品故障相关的问题，例如xxx配置不生效、错误码xxxx、没反应、报错、等等。 |\
| |``` |\
| | |![Image=391x861](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1bba637a05cd4d9b92361c2ddf794e66~tplv-goo7wpa0wc-image.image) |
| | | | \
|知识库节点 |售前和售后问题分别流转到售前知识库和售后知识库处理，并直接输入给结束节点。知识库节点配置如下： |\
| | |\
| |* 输入：沿用默认设置即可，Query 的变量值设置为开始节点的输入参数 USER_INPUT。 |\
| |* 知识库：选择准备好的售前知识库。 |\
| |* 搜索策略等配置：沿用默认配置即可。 |![Image=392x465](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fa96afbd0e8f4a94ba0d54e4e7c4559f~tplv-goo7wpa0wc-image.image) |
| | | | \
|大模型节点 |大模型节点会基于知识库命中的知识，包装一个对外的话术，作为最终回复。其配置如下： |\
| | |\
| |* 输入：设置以下两个输入变量： |\
| |   * input：引用知识库节点的ouput。 |\
| |   * USER_INPUT：引用开始节点的用户输入。 |\
| |* 用户提示词：`用户问题是{{USER_INPUT}}，知识库检索结果是{{input}}，你需要包装一个用户友好的话术，并回复用户`。 |\
| |* 其他选项维持默认设置即可。 |![Image=389x693](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/250d3fbfcfe940469426462eb741f621~tplv-goo7wpa0wc-image.image) |\
| | | |
| | | | \
|文本处理节点 |意图识别的兜底策略，对于未命中任何分类的意图，统一输出一段文案，指导用户提交[工单](https://console.volcengine.com/workorder/create?step=2&SubProductID=P00001396&utm_source=coze&utm_medium=coze_home&utm_term=coze_feedback&utm_campaign=from_coze&utm_content=coze_pro)或联系人工客服。 |\
| |其配置如下： |\
| | |\
| |* 输入：无需设置输入变量。 |\
| |* 输出内容：`非常抱歉，我只能回答售前咨询和售后问题。如果你对产品有任何使用问题或疑问，欢迎向我咨询！` |![Image=710x814](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/80fb211166b44a79b19db3fe5c3a9360~tplv-goo7wpa0wc-image.image) |


