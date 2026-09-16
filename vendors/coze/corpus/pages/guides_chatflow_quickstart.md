> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

随着人工智能技术的不断进步，AI 助手开始越来越受欢迎，它们基于大模型的文本生成能力，用户可以通过自然语言与 AI 助手进行交流。对话式 AI 助手也可以集成到各种社交软件、应用程序中，提供给更多平台的用户使用。

本教程详细指导你如何在扣子编程中基于对话流开发一个移动端 AI 助手，并将其发布到扣子商店。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## AI 助手介绍 {#a659d532}

AI 助手利用大语言模型强大的文本生成能力，在对话过程中扮演助手的角色回答用户问题。AI 助手能够理解和回应用户的指令，提供信息查询、知识问答等多种服务。

## 步骤一：设计 AI 助手功能 {#9ab0dbe5}

在开始开发前，你需要设计 AI 助手的功能及对应的用户界面。

通常情况下，AI 助手的核心功能是通过大语言模型回答用户的问题，且 AI 助手的界面应是类似通讯软件的对话式页面。此场景可以通过一个包含大模型节点的对话流实现。

完成主体功能设计和规划后，就可以开始搭建扣子低代码应用了。

## 步骤二：创建扣子低代码应用 {#8e98f2e8}

首先，你需要创建一个扣子低代码应用。

扣子低代码应用支持使用工作流来完成复杂的业务逻辑编排，也支持使用数据库、知识库、插件等资源实现与本地数据或线上数据的交互。此外，扣子低代码应用支持通过拖拉拽的方式搭建用户界面，并且能够实现与业务逻辑的联动。

参考以下操作，创建扣子低代码应用。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**创建** > **创建应用**。
3. 在**应用模板**页面，单击**创建空白应用**。
4. 输入应用名称，并单击图标旁的 AI 图标使用 AI 自动生成一个图标。然后单击**确认**。
   应用创建成功后，你会直接进入到应用的集成开发环境 (IDE)。
   ![Image=151x153](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9b591cfd29ef488aa2d45ab3f9340372~tplv-goo7wpa0wc-topic.webp)   


## 步骤三：编排业务逻辑 {#480765c6}

创建完扣子低代码应用项目后，你可以开始进行业务逻辑编排了。扣子编程提供了大模型、代码、意图识别、知识库写入与检索等丰富的工作流节点，以满足复杂的业务场景需求。此外，你还可以通过使用变量、插件、知识库等方式与你的本地数据和线上数据进行集成。

本教程中的 AI 助手应用，主要使用大模型实现对话交互，所以只需要创建一个包含大模型节点的对话流即可。

1. 在**业务逻辑**页面，找到**工作流**，然后单击 **+** > **新建对话流**。
   ![Image=624x284](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f42bfbf420124acdab006eef3fc0d836~tplv-goo7wpa0wc-topic.webp)
2. 输入对话流名称和描述，然后单击**确认**。
   扣子编程默认创建一个同名的会话，并为对话流绑定这个会话。对话流运行过程中产生的消息都会记录到这个会话中，大模型会参考会话中记录的历史消息，生成适合当前场景的回复。会话中的消息是用户的个人数据，用户之间的会话消息是相互隔离的，每个用户只能看到本人发起的对话数据。会话管理说明，请参考[管理低代码应用会话](/guides/manage_conversation)。
   ![Image=218x219](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/29bb27a65c1040d696224e7fd27d9a7c~tplv-goo7wpa0wc-topic.webp)
3. 在工作流画布，单击**开始**节点的连接线或画布下方的**添加节点**按钮，然后选择**大模型**节点。
   ![Image=425x252](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b36509978b39488fa6d21dfdfb3a29b8~tplv-goo7wpa0wc-topic.webp)
4. 将开始节点、大模型节点和结束节点按顺序连接起来。
   ![Image=2238x481](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/142f53532ee344379b1649af9f834725~tplv-goo7wpa0wc-topic.webp)
5. 单击**开始节点**进行配置。开始节点用于设定启动对话流需要的信息。
   本场景中，用户需要提供要咨询的问题。这些内容默认通过开始节点的 **USER_INPUT** 参数传入，无需增加其他输入参数。为**USER_INPUT** 参数指定一个默认值，例如“你好”。其他参数维持默认配置即可。
   ![Image=494x339](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ac1cda715a5d409a9ccc3d9d7d86802e~tplv-goo7wpa0wc-topic.webp)
6. 单击**大模型**节点进行配置。大模型节点用于接收用户问题，并生成对应的回复。
   需要添加的设置如下，其他参数维持默认的配置。
   <!-- @cols-width: 126,488,223 -->
   | **参数配置**  | **说明**  | **示例**  |
   | --- | --- | --- |
   | **输入**  | 在输入区域可以看到大模型节点预置了一个默认参数 input，单击设置图标，选择开始节点的 **USER_INPUT** 参数。  | ![Image=1208x422](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d29ad8836e874d4684bfbdafd09c0030~tplv-goo7wpa0wc-topic.webp)  |
   | **开启对话历史**  | 开启对话历史功能后，扣子编程会将会话中已存的近期消息作为对话历史传递给大模型，供大模型生成回复时作为参考，生成更符合语境的回复。  | ![Image=758x306](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8c7dbb7ec0964e799a7ebd709f034a99~tplv-goo7wpa0wc-topic.webp)  |
   | **系统提示词**  | 在**系统提示词**区域，输入以下内容。 | ![Image=712x843](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/72594d7ad1614ed497f0e2efbf8e22cf~tplv-goo7wpa0wc-topic.webp)  | \
   | | | | \
   | | 系统提示词是一组指示模型行为和功能范围的指令，可以包括如何提问、如何提供信息、如何请求特定功能等。系统提示词也用于设定对话的边界，比如告知用户哪些类型的问题或请求是不被接受的。 | | \
   | | | | \
   | | ```Markdown | | \
   | | # 角色 | | \
   | | 你是一个全能的 AI 助手，能够快速准确地回答用户的各种问题，并提供详细的解释和建议。 | | \
   | | | | \
   | | ## 技能：回答问题 | | \
   | | 1. 当用户提出问题时，仔细分析问题的关键信息，使用工具进行搜索以获取准确的答案。 | | \
   | | 2. 以清晰、简洁的语言回答问题，并提供相关的解释和例子。 | | \
   | | | | \
   | | ## 限制: | | \
   | | - 只回答真实、准确的信息，拒绝编造或猜测答案。 | | \
   | | - 回答内容应简洁明了，避免冗长和复杂的表述。 | | \
   | | ```  | |
   | **用户提示词**  | 用户提示词通常是直接的命令，告诉模型要执行的任务或意图。指令越清晰，模型的输出也更贴近你的实际需求。 | ![Image=702x326](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b806ec7fb7b242e2b5ec565621d0b934~tplv-goo7wpa0wc-topic.webp)  | \
   | | | | \
   | | 直接引用输入参数中定义的变量 `{{input}}`，表示使用开始节点的 **USER_INPUT** 参数作为用户提示词。 | | \
   | | | | \
   | | :::tip 说明 | | \
   | | 引用变量成功后，变量应是蓝色字体。如果你没有可用的变量，请检查是否按照教程配置了大模型节点的输入变量。 | | \
   | | ::: | | \
   | | | | \
   | |   | |
7. 选择**结束**节点进行配置。结束节点用于输出对话流的最终结果。
   1. 单击**结束**节点，然后选择**返回文本**。
   2. 选择大模型节点的输出结果作为输出参数。
      ![Image=331x215](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4f9848328a05470cb08bbfa742f516b3~tplv-goo7wpa0wc-topic.webp)
   3. 在**回答内容**文本框中输入`{{output}}`，使用大模型的输出内容作为最终的回复。
      ![Image=330x132](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6b5450633c5a4062b97f373dcd50a2ab~tplv-goo7wpa0wc-topic.webp)
   4. 开启**流式输出**，实现打字机一样的输出效果。
      ![Image=324x124](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/287555ea83374b989c55bfdc721954cc~tplv-goo7wpa0wc-topic.webp)
      至此，你已经完成整个对话流的搭建。
8. 设置 AI 角色信息。
   单击**角色**，在**角色配置**对话框中设置角色信息。
   ![Image=767x514](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4c76af8e21c246b1b405ac055df479da~tplv-goo7wpa0wc-topic.webp)
   重要参数说明如下，详细的参数说明，请参考[AI 对话](/guides/ai_chat_mini_program)。
   <!-- @cols-width: 158,679 -->
   | **配置**  | **说明**  |
   | --- | --- |
   | 角色名称  | 设置 AI 助手的名称，将显示在对话框中，例如 `AI 助手`。  |
   | 角色描述  | 设置 AI 助手的角色描述，帮助用户了解角色的背景和功能。  |
   | 角色头像  | 设置 AI 助手的头像。  |
   | 开场白  | 设置 AI 助手的开场白，可以直接使用以下示例文案。 | \
   | | | \
   | | ```Plain Text | \
   | | 你好！我是你的专属 AI 助手。无论你需要查询信息、提供建议、还是简单的聊天，我都在这里为你服务。 | \
   | | 告诉我你的需求，让我们开始愉快的对话吧！ | \
   | | ```  |
   | 开场白预置问题。  | 为 AI 对话组件预置三个开场白问题，示例如下： | \
   | | | \
   | | * 双子座有什么特点 | \
   | | * 推荐一本好书 | \
   | | * 想去新疆，有什么行程建议吗  |
9. 为了保证业务逻辑实现符合预期，需试运行对话流。
   1. 单击**试运行**。
      ![Image=465x180](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8c9dd4516ebb48e68ed7405828d98ab9~tplv-goo7wpa0wc-topic.webp)
   2. 填写对话流入参配置。
      根据页面提示选择一个会话。会话用于存储对话流产生的消息，包括用户的提问和模型的回复。下次执行时，对话流可以从会话中读取到之前存储的消息记录。在本教程中我们在创建对话流的同时创建了一个同名会话，这个同名会话会作为对话流的默认会话。
      单击**保存并开始对话调试**。
      ![Image=680x349](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/787e22e92dca4bf19b0fe548f6bd9d60~tplv-goo7wpa0wc-topic.webp)
   3. 在输入框中输入一段内容，并按回车键发送。
      我们在对话流的开始节点设置了 **USER_INPUT** 参数的默认值“你好”，这个默认值会自动填写在输入框，作为你的输入参考。
      ![Image=170x256](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/962bb80ab43941d4b3d2e1b235cedbd6~tplv-goo7wpa0wc-topic.webp)
   4. 扣子编程会自动运行对话流，并在试运行面板中展示你的输入和对话流执行的返回结果。
      对话流的试运行面板默认为对话式，类似智能体的调试区域，展示每一次试运行此工作流时用户和模型的对话交互过程。
      ![Image=686x361](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cca5f7c7240845e799eede498b03fce1~tplv-goo7wpa0wc-topic.webp)
      在完成业务逻辑搭建并通过试运行后，你就可以开始用户界面搭建了。      


## 步骤四：搭建用户界面 {#0372e6fd}

扣子编程提供了可视化的用户界面搭建能力，你可以通过拖拉拽的方式搭建一个用户界面，无需编写一行代码。

参考以下操作，搭建 AI 助手应用的用户界面。

1. 在应用 IDE，单击页面上方的**用户界面**页签。
2. 选择页面类型。
   扣子低代码应用支持发布为小程序等移动端应用，也可以发布为 Web 页面等网页应用。这里我们选择**小程序和 H5**。
   ![Image=451x269](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/09b19376ea2b45d7b75bf931de810295~tplv-goo7wpa0wc-topic.webp)
3. 搭建页面布局。
   AI 助手应用只有一个简单的对话窗口，所以我们只需要搭建一个页面并添加 AI 对话组件即可。
   1. 在画布中选中页面，并在右侧 Page1 配置面板中关闭导航栏。
      移动端页面默认开启首页底部的导航栏，AI 助手应用只有一个页面，所以需要手动关闭底部的导航栏。
      ![Image=388x249](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/94cd8eda061447aeadda2d81c841b62a~tplv-goo7wpa0wc-topic.webp)
   2. 在**组件**面板中，找到 **AI 组件 > AI对话**组件，然后将 AI 对话组件拖入到画布中。
      ![Image=501x242](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9b658d074a8948868450c751954e0068~tplv-goo7wpa0wc-topic.webp)
4. 设置组件属性。
   1. 在画布中，选中拖入的 **AI对话**组件。组件名称为`Chat1`。
   2. 在 `Chat1` 组件的属性配置面板中，选择步骤三中搭建的对话流。
      ![Image=347x213](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a64e4a9f56f64e6ea5c019251ea02ab5~tplv-goo7wpa0wc-topic.webp)      


配置效果如下：

![Image=424x567](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9c4de6ed7e9d4720b4d112181ff01390~tplv-goo7wpa0wc-topic.webp)

## 步骤五：效果测试 {#49f9aa3e}

完成上述所有配置后，单击**预览**查看整体功能并进行体验。

![Image=277x196](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/60165dadec35445ca438f955bec83792~tplv-goo7wpa0wc-topic.webp)

页面会展示 AI 助手在移动端的页面预览效果，你可以在页面下方的输入框中输入一段文字，并按回车键发送消息。AI 助手会立即回复你的问题。

![Image=203x418](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5a02b798916841b48c0b5f338603a7cd~tplv-goo7wpa0wc-topic.webp)

## 步骤六：发布应用 {#146030ba}

完成应用测试后，你就可以将应用发布到商店、模板、各种社交渠道，或发布成 API 服务与其他应用集成。

本教程中以发布到商店为例。

1. 在应用 IDE 中，单击右上角的**发布**按钮。
2. 在**发布**页面，输入版本号和发布描述。
3. 选择扣子商店，然后选择应用分类。
   ![Image=2796x1348](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cc46ceb547d54d5ca49d0f1af9a81846~tplv-goo7wpa0wc-topic.webp)
4. 单击页面上的**发布**按钮，完成应用发布。
   发布完成后，你就可以在扣子商店上使用这个应用了。   


## 相关文档 {#03709c5f}


* [编排业务逻辑](/guides/build_project_in_projectide)
* [用户界面编辑器概述](/guides/ui_builder_overview)
* [低代码工作流介绍](/guides/workflow)
* [了解项目发布](/guides/publish_overview)
