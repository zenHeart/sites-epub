> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

以好书解析场景为例，演示如何将长文本消息拆分为多条消息，减少用户等待回复的时间。
## 场景说明 {#f3abde6f}
在内容生成和内容处理场景中，工作流最终输出的内容较长，即使开启了结束节点的流式输出，用户也需要等待一段时间才能获得完整的输出文本，在一定程度上会影响用户体验。
扣子编程的低代码工作流提供了输出节点，可以在工作流执行过程中阶段性输出文本消息。我们可以使用文本处理节点将消息拆分为两部分，一部分通过输出节点输出，一部分通过结束节点输出，同时开启流式输出。此方案适用于文章生成、剧本写作、文档优化等最终输出大量文本的场景，减少用户等待时间，提升用户体验。
## 效果演示 {#93a9ae4f}
以好书解析场景为例，智能体将一条长文本消息拆分为了两条消息输出：
![Image=585x302](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/99c79661e5cc4723a2069ddfbd9aec51~tplv-goo7wpa0wc-image.image)
## 低代码工作流设计 {#dbeb0a67}
大模型节点生成书籍的介绍，并指定输出为两个段落，通过文本处理节点将两个段落拆开，一段通过输出节点输出，一段通过结束节点输出。
![Image=2840x1159](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e1103be31a104ff9b63b739ac1537bfa~tplv-goo7wpa0wc-image.image)
## 核心节点配置 {#01a6d857}
工作流核心节点的配置详情如下：
<!-- @cols-width: 221,394,191 -->
| | | | \
|**节点类型** |**配置说明** |**示例** |
|---|---|---|
| | | | \
|大模型节点 |引用开始节点的变量，获取用户需要查询的书籍名称。 |\
| |用户提示词中需要指定输出格式，例如指定输出为两个段落。 |![Image=400x668](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b07df505d3ec44bbb65bc9abaa37f36c~tplv-goo7wpa0wc-image.image) |\
| | | |
| | | | \
|文本处理节点 |使用字符串分隔模式，通过换行符将大模型节点的输出内容转为数组格式，每个段落是数组的一个元素。 |![Image=400x456](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5eaafb71d12f4a80a4428c4b7bcacbba~tplv-goo7wpa0wc-image.image) |
| | | | \
|输出节点 |引用文本处理节点的输出，注意这里只引用数组的第一个元素，也就是书籍简介的第一个段落。 |![Image=400x397](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/241d72d708d045f480ed081c14fd0fbd~tplv-goo7wpa0wc-image.image) |
| | | | \
|结束节点 |引用文本处理节点的输出，这里只引用第二个段落即可。 |![Image=400x444](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a2b0d0764eec40fcbf86bbee8b214546~tplv-goo7wpa0wc-image.image) |


