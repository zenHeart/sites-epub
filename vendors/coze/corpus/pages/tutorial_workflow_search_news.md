> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

低代码工作流内可选择丰富的插件节点处理任务。本文介绍如何使用插件节点搭建一个用于搜索新闻的低代码工作流。
## 场景描述 {#2538968d}
大模型的训练数据中不包含最新的知识和数据，所以无法解答对时效性有要求的问题，例如实时新闻、实时天气、实时股票数据等。但是大模型通常具备工具调用（Function calling）的能力，可以调用外部工具拓展能力边界，获取外部的信息和数据。插件商店提供了一系列插件工具供你使用，例如通过新闻搜索插件为大模型提供各个领域的新闻资讯。
本文介绍如何使用搜索插件节点搭建一个用于搜索新闻的低代码工作流。
## 效果示例 {#8b225441}
下图展示了示例工作流添加到智能体之后，智能体带来的用户任务处理能力。用户输入内容后，智能体会调用示例工作流处理任务，并向用户返回处理结果。
![Image=267x364](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/28ffff18540042c782d10ac1758bcf48~tplv-goo7wpa0wc-image.image)
## 低代码工作流设计 {#39766d85}
本文构建的示例工作流节点概览如下图所示，该工作流中添加头条新闻 **getToutiaoNews** 插件节点来实现搜索新闻的能力。
![Image=1340x242](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/75665168a5d6426cb2b1fa4d50bb3598~tplv-goo7wpa0wc-image.image)
## 步骤一：构建低代码工作流 {#b327e97d}
1. 登录[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。


3. 在页面右上角，单击 **+资源** > **工作流**。
   本文示例配置如下：
   * **工作流名称**：输入 `getNews_tasks`
   * **工作流描述**：输入 `搜索新闻`
4. 在工作流的编辑页面的左侧列表内，单击**插件**右侧的 **+** 图标，查找**头条新闻**并选用内置的 **getToutiaoNews** 节点。
   该节点将用于搜索新闻。
   ![Image=616x342](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/707a64687556498a812cf3e54164f2bb~tplv-goo7wpa0wc-image.image)
5. 连接各节点，并依次配置输入输出参数。
   节点连接顺序：**开始 → getToutiaoNews → 结束**。各节点参数配置说明如下表：
   <!-- @cols-width: 149,442,233 -->
   | | | | \
   |**节点** |**配置** |**示例** |
   |---|---|---|
   | | | | \
   |开始 |开始节点预置了输入变量 `input`，**String** 类型。 |![Image=362x203](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5c75c49962634620a87b5f10e5d968b1~tplv-goo7wpa0wc-image.image) |
   | | | | \
   |getToutiaoNews |添加一个插件节点，插件工具选择新闻搜索插件的 getToutiaoNews 工具。通过插件节点运行新闻搜索插件，获取搜索结果。 |\
   | |定义输入变量 **q**，在**参数值**区域引用**开始**节点的 `input` 变量。 |![Image=372x341](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e929074853694a25b18397c2edb39f0d~tplv-goo7wpa0wc-image.image) |
   | | | | \
   |结束 |定义 `output` 输入变量，并在**参数值**区域选择引用 **getToutiaoNews** 节点的 **news** 变量。 |\
   | |工作流绑定智能体之后，智能体收到工作流运行结果，会自行通过模型归纳总结，生成最终的回复内容。 |\
   | | |![Image=369x256](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/59fbb9c24c3646a28cca338d78ce4b56~tplv-goo7wpa0wc-image.image) |

6. 配置完成后，单击页面右上角的**试运行**，测试工作流。
   例如，输入 `科技` 进行测试，待所有节点都运行成功（节点会展示绿色边框）后，查看指定节点的运行结果。
7. 测试工作流无问题后，单击页面右上角的**发布**。
   成功发布后，在工作流列表中可以查看到该工作流。

## 步骤二：在智能体添加工作流并测试 {#544638c4}

1. 在左侧导航栏中单击**项目管理**，然后创建或打开指定智能体。
2. 在智能体编排页面，找到**技能**区域的**工作流**，在右侧单击加号图标。
3. 在对话框左侧单击**团队工作流**，找到自建的 **getNews_tasks** 工作流，并在右侧单击**添加**。
   ![Image=633x341](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fb99d2a5806442acaea39ce150dc0c2e~tplv-goo7wpa0wc-image.image)
4. 在智能体的**人设与回复逻辑**内，声明智能体使用 **getNews_tasks** 工作流处理任务。
   例如设置为`你是一个个人助手小A，调用 {{`**`getNews_tasks`**`}} 实现联网搜索`。
   编写后，你可以单击**优化**，让 AI 帮助你生成结构化的回复逻辑。智能体会分析用户意图，根据系统提示词和工作流的描述信息自行选择执行工作流。
5. 在智能体的右侧**预览与调试**区域，输入内容预览智能体实现的效果。
   例如输入 `科技新闻`。
   ![Image=304x418](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/23279456cf764bf5ae182fb9ca5524c3~tplv-goo7wpa0wc-image.image)





