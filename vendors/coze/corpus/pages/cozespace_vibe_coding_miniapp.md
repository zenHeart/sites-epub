> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

通过与编程 Agent 对话，你可以快速开发微信小程序。无需编写代码、无需搭建开发环境，只需提出明确的开发需求即可从零开始完成小程序的代码编写、部署上线。本文档介绍如何使用编程 Agent 开发小程序。

## 功能概述 {#cc6e9870}

扣子已将扣子编程平台封装为编程 Agent，提供了一个 AI 编程开发环境，你可以直接与编程 Agent 对话，描述你想要开发的小程序的功能、界面、逻辑等需求，编程 Agent 会自动完成小程序的开发、测试、迭代和发布。

:::tip 说明
* 目前仅支持开发微信小程序。
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 费用说明 {#9d02870b}

开发、测试、部署、线上使用小程序时，以下操作将消耗你的扣子积分。

* [编程任务](https://docs.coze.cn/coze_pro/task_fee)：与编程 Agent 的每轮对话。
* [内置集成](https://docs.coze.cn/coze_pro/internal_integrations_fee)：调用大语言模型、联网搜索、图像生成等内置集成服务。
* [服务托管费用](/coze_pro_service_hosting_fee)：部署为线上服务，将产生服务托管费。

## 配额与限制 {#ad0cce03}

开发小程序时，存在可创建的项目数量、可回滚版本数、可部署的次数等配额限制，详细说明，请参考[配额与限制](/guides/vibe_coding_limit)。

## 准备工作 {#9a105646}

在开始开发之前，你需要在微信公众平台完成小程序的注册和基础配置。

* **注册小程序**：前往 [微信公众平台](https://mp.weixin.qq.com/)，按照官方[小程序注册指引](https://developers.weixin.qq.com/miniprogram/introduction/#%E5%B0%8F%E7%A8%8B%E5%BA%8F%E6%B3%A8%E5%86%8C)完成小程序账号的注册。
* **获取 AppID**：在[微信公众平台](https://mp.weixin.qq.com/)左侧导航栏单击**管理** > **开发管理**，在**开发设置**页签的**开发者 ID** 区域找到并复制 AppID。这是小程序的唯一标识，后续步骤将会用到。

![Image=469x265](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ed2a74df4fc94d76ad33d19afdff3e2d~tplv-goo7wpa0wc-topic.webp)

## 步骤一：创建编程项目 {#8802f400}

::::tabs
@tab 网页端、桌面端
1. 在扣子左侧导航栏中，单击 + >**新建编程项目**。
2. （可选）团队版或企业版需要选择项目所属的工作空间，然后单击**确认**。
   ![Image=452x262](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9829629728224bdf94a935f1774fa505~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
1. 在扣子 App 顶部，单击 + >**新建编程项目**。
   ![Image=174x339](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4d5e0b014ef94d64867baaefde9dce35~tplv-goo7wpa0wc-topic.webp)
2. （可选）团队版或企业版需要选择项目所属的工作空间，然后单击**确认**。
   ![Image=155x306](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e68c80221f4d4f70a7d24386319e327d~tplv-goo7wpa0wc-topic.webp)
::::

## 步骤二：需求澄清 {#1c67bc6b}

::::tabs
@tab 网页端、桌面端
1. 创建编程项目并输入你的需求。
   1. 在编程项目中，单击**小程序**选项卡。
   2. 在文本框输入你的提示词。
      你需要尽可能清晰且详细地描述小程序的功能、界面设计、业务逻辑等方面的要求。例如，你可以输入以下提示：
   ```Plain Text
   帮我制作一个小程序，用于学习普通话情景对话
   1. 模型随机生成并展示 3 个不同主题，例如买菜、问路、面试等，用户进入页面时，选择一个主题，模型根据主题生成一段对话数据，并展示给用户
   2. 类似聊天气泡的布局展示对话，每个汉字上方标注拼音，点击气泡可以朗读语句，整体有个录音按钮，用户可以跟读并录音，跟读完听回放
   ```
   ![Image=404x263](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/606022bba5024fedb91c79819612193d~tplv-goo7wpa0wc-topic.webp)
2. （可选）进阶配置：通过上传附件、选择协作模式、添加技能、选择编程模型，让编程 Agent 生成的结果更精准、更符合你的预期。
   ![Image=370x98](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6529022d281e4328b69e7e29c4462798~tplv-goo7wpa0wc-topic.webp)
   * 上传附件
      酌情上传一些图片或文件，作为附加信息提供给编程 Agent，以便编程 Agent 能更理解你的需求。例如上传一张你想参考的网站截图、想要的风格示例图片等，这些都能帮助编程 Agent 更精准地把握细节要求。
   * 选择协作模式
      默认情况下为 **Agent 模式**，如果你对需求不确定，可以先切换到**问答模式**讨论方案，待方案确认后，再切换到**Agent 模式**，由编程 Agent 根据此前的讨论结论执行开发任务。更多信息，请参考[如何选择协作模式？](https://docs.coze.cn/guides/vibe_coding_faq#3069a332)。
   * 添加技能
      在执行编程任务时，编程 Agent 可以按需加载技能，从而具备相应的专业领域知识和能力。例如，前端设计技能可以有效指导模型如何排版、设计配色和动画效果、处理背景等等，能显著提升模型的 UI 生成能力，减少产物视觉效果的“AI 味”。 
   * 选择编程模型
      扣子编程已集成 Doubao、GLM、Kimi、DeepSeek 等主流的编程模型，用于开发应用。为了达到较好的开发效果，系统会自动为你选择适合当前场景的模型，你也可以根据模型的官方介绍自行选择
3. 单击**运行**图标，开始开发你的项目。
   编程 Agent 会根据你输入的提示词来开始设计小程序、创建项目，并自动为项目设置小程序名称。

@tab 移动端
1. 创建编程项目并输入你的需求。
   1. 在编程项目中，单击**小程序**选项卡。
   2. 在文本框输入你的提示词。
      你需要尽可能清晰且详细地描述小程序的功能、界面设计、业务逻辑等方面的要求。例如，你可以输入以下提示：
      ```Plain Text
      帮我制作一个小程序，用于学习普通话情景对话
      1. 模型随机生成并展示 3 个不同主题，例如买菜、问路、面试等，用户进入页面时，选择一个主题，模型根据主题生成一段对话数据，并展示给用户
      2. 类似聊天气泡的布局展示对话，每个汉字上方标注拼音，点击气泡可以朗读语句，整体有个录音按钮，用户可以跟读并录音，跟读完听回放
      ```
      ![Image=140x268](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/850add0d72fa4a3ea990a62741003239~tplv-goo7wpa0wc-topic.webp)
2. （可选）进阶配置：通过上传附件、选择协作模式、添加技能、选择编程模型，让编程 Agent 生成的结果更精准、更符合你的预期。
   ![Image=162x310](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6fac1a7d3b844694a4ed8f183681ccf8~tplv-goo7wpa0wc-topic.webp)
   * 上传附件和添加技能
      * 酌情上传一些图片或文件，作为附加信息提供给编程 Agent，以便编程 Agent 能更理解你的需求。例如上传一张你想参考的网站截图、想要的风格示例图片等，这些都能帮助编程 Agent 更精准地把握细节要求。
      * 在执行编程任务时，编程 Agent 可以按需加载技能，从而具备相应的专业领域知识和能力。例如，前端设计技能可以有效指导模型如何排版、设计配色和动画效果、处理背景等等，能显著提升模型的 UI 生成能力，减少产物视觉效果的“AI 味”。 更多信息，请参考[在扣子编程中使用技能](/guides/using_skill#3456ebc7)。
   * 选择协作模式
      默认情况下为 **Agent 模式**，如果你对需求不确定，可以先切换到**问答模式**讨论方案，待方案确认后，再切换到**Agent 模式**，由编程 Agent 根据此前的讨论结论执行开发任务。更多信息，请参考[如何选择协作模式？](https://docs.coze.cn/guides/vibe_coding_faq#3069a332)。
   * 选择编程模型
      扣子编程已集成 Doubao、GLM、Kimi、DeepSeek 等主流的编程模型，用于开发应用。为了达到较好的开发效果，系统会自动为你选择适合当前场景的模型，你也可以根据模型的官方介绍自行选择。
3. 单击**运行**图标，开始开发你的项目。
   编程 Agent 会根据你输入的提示词来开始设计小程序、创建项目，并自动为项目设置小程序名称。
::::

## 步骤三：开发应用 {#a71a4f5b}

编程 Agent 收到你的需求之后，将立即启动需求分析，并规划开发流程和步骤，逐步生成小程序的前后端代码。代码生成完毕后，自动构建并启动服务，以提供一个可视化的界面供你预览。

如果编程 Agent 判断你的小程序需要数据库、存储、身份认证、AI 等能力，则会自动添加和配置对应的集成，为你的小程序设计数据库表、配置存储系统，实现相关功能。

::::tabs
@tab 网页端、桌面端
![Image=372x250](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f298c50c971f4eab95cf92095c8d9624~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
![Image=132x270](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/41575ac41b7048fd9a7152ebfd385af3~tplv-goo7wpa0wc-topic.webp)
::::

## 步骤四：预览与测试 {#92599173}

初步生成后端代码后，编程 Agent 会自动生成测试用例并完成一轮单元测试。测试通过后编程 Agent 会提供后端代码的预览，同时提醒你对后端开发部分进行验收。

:::tip 说明
录音等部分功能仅在小程序真机调试时可用，建议配置 AppID 之后通过微信扫码预览真机效果。
:::

::::tabs
@tab 网页端、桌面端
你可以在右侧**预览页面**查看实际运行效果。 应用预览界面如下：

![Image=454x471](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a037d78ce4f04cd7a16c9e39af548046~tplv-goo7wpa0wc-topic.webp)



@tab 移动端
你可以在页面中单击**预览**查看实际运行效果。 网页应用预览界面如下：

![Image=174x348](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/738d77986dcc4144b784176d8ba434bb~tplv-goo7wpa0wc-topic.webp)


::::

### 绑定微信小程序 {#80271445}

为了体验小程序在手机上的效果，建议参考以下流程真机调试小程序。

::::tabs
@tab 网页端、桌面端
1. 在编程项目页面右下角单击 **AppID 设置**。
   ![Image=297x310](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/dae75434446e457db462200dda41a933~tplv-goo7wpa0wc-topic.webp)
2. 在弹出页面中填写 AppID，并单击**绑定**。
   **AppID** 是你在[准备工作 ](/cozespace/vibe_coding_miniapp#9a105646)中获取的 AppID。
   ![Image=270x572](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ce83548c687240e49ff2ab1c2448be5b~tplv-goo7wpa0wc-topic.webp)
3. 完成公众平台账号授权。
   单击**绑定**后，系统默认打开授权页面，使用小程序的管理员微信号扫描授权二维码，并根据页面提示完成授权。

@tab 移动端
1. 在**预览**页面的右上角，单击**二维码**图标。
   ![Image=204x394](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ac3e5b17310348e9bace46f701374d7c~tplv-goo7wpa0wc-topic.webp)
2. 复制链接，前往扣子 Web 端打开项目，进行预览。
   即参考【网页端、桌面端】的操作步骤。
::::

<!-- @cols-width: 206,208,207,207 -->
| | | | | \
|1. 管理员扫描二维码 |2. 选择账号 |3. 授权确认 |4. 授权成功 |
|---|---|---|---|
|![Image=557x651](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/789901bad26444d9b6228d1a9a3a39c0~tplv-goo7wpa0wc-topic.webp) |![Image=1292x2798](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/aa214c68ea224ec587a16a792b279384~tplv-goo7wpa0wc-topic.webp) |![Image=1292x2798](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/42168118fa4648e486f17959d1d4e841~tplv-goo7wpa0wc-topic.webp) |![Image=1292x2798](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/54b38c59860a4642a3a274c2e81b181f~tplv-goo7wpa0wc-topic.webp) |

### 真机调试小程序 {#755a6210}

成功绑定小程序之后，就可以使用管理员微信号扫描页面右侧的二维码，在手机上调试小程序。

::::tabs
@tab 网页端、移动端
使用管理员微信号，在**预览**页面右下角扫描二维码，即可在手机上预览你的小程序。

![Image=278x235](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c54a53d3f4974175b1419164416cf30b~tplv-goo7wpa0wc-topic.webp)



@tab 移动端
单击**二维码**图标，然后扫码预览。

![Image=163x293](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/987d4d64c6fd443fa5e3ce669fa9c7ba~tplv-goo7wpa0wc-topic.webp)
::::

### 测试项目 {#c9e239ce}

在预览与测试的环节中，你可以通过以下操作测试编程 Agent 为你生成的小程序。

<!-- @cols-width: 112,402,239 -->
| | | | \
|**操作** |**说明** |**示例** |
|---|---|---|
|全面测试 |全面测试你的小程序，通常建议关注以下问题： |\
| | |\
| |* **功能是否可用**：验证小程序的核心链路是否完整可操作、数据的增删改查是否能成功执行。 |\
| |* **交互是否完善**：检查页面元素是否完整显示、布局是否合理、样式是否符合设计要求、各个按钮是否都能正确触发。 |\
| |* **AI 能力是否正常**：如果你的小程序集成了 AI 能力，例如文本生成、图片生成等，验证 AI 模型的输出是否符合预期。 |![Image=105x227](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/624f4de2813c48238a3cbb754475ad0a~tplv-goo7wpa0wc-topic.webp) |
|修复故障 |如果页面报错，编程 Agent 会自动识别并提示你修复故障，你可以根据页面提示，单击**一键修复**，允许编程 Agent 尝试修复这些问题。 |\
| | |\
| |如果你在体验小程序的过程中触发页面报错，或者页面交互、生成结果不符合你的预期，你也可以主动复制报错信息、描述预期的结果，并粘贴到左侧输入框中，要求编程 Agent 修复故障。 |* 网页端 |\
| | |   ![Image=167x133](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/aac8c1bc42d94d3283739af6d7b7ceee~tplv-goo7wpa0wc-topic.webp) |\
| | |* 手机端 |\
| | | |\
| | |![Image=154x301](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f16dd7c5c2cc420daa2be34d8c171f41~tplv-goo7wpa0wc-topic.webp) |

## 步骤五：部署应用 {#68c47592}

完成小程序的开发与测试之后，你需要在微信开放平台完成**小程序的配置和备案**，然后在页面右上角单击**部署**，将扣子编程搭建的小程序部署成为一个公开可访问的微信小程序，将你的创意和原型，转化为服务于真实用户的产品。详细操作步骤可参考[部署小程序](https://docs.coze.cn/guides/deploy_vibe_miniapp)。

::::tabs
@tab 网页端、移动端
1. 单击页面右上角的**部署**图标，然后单击**开始部署**。
2. 按需配置部署信息。
3. 你可以使用默认配置，快速完成部署，也可以按需配置可见性、数据库、环境变量等配置。
4. 单击**开始部署**。
   ![Image=492x310](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c5d2e1037a964f9db39107a7ad55c85b~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
1. 单击页面右上角的 **···** > **部署**，然后单击**开始部署**。
   ![Image=166x334](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6cbd2911b72a4df396e5a3a6ee9708ed~tplv-goo7wpa0wc-topic.webp)
2. 按需配置部署信息。
   你可以使用默认配置，快速完成部署，也可以前往扣子网页版进行配置。
   ![Image=136x273](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/35960d000dd049a0b3845ced2bf8ad8b~tplv-goo7wpa0wc-topic.webp)
3. 单击**部署**。
::::

## 进阶操作 {#8a458db1}

关于开发应用的进阶操作，可以参考以下功能：

* 迭代应用：通过自然语言或直接修改代码，持续优化应用的功能、页面和交互。更多信息，请参考[迭代小程序](/guides/vibe_coding_miniapp#794facfc)。
* 集成服务：为应用接入 AI 模型、联网搜索、数据库、对象存储、用户登录等能力。更多信息，请参考[集成能力](/guides/vibe_coding_miniapp#d912c5d4)。
* 回滚开发版本：当生成结果不符合预期、修复失败或应用状态异常时，可以在版本历史中将应用恢复到之前的正常版本，再继续迭代。更多信息，请参考[回滚开发版本](/guides/vibe_coding_miniapp#6672685d)。
* 多人协作：邀请同一工作空间下的其他成员加入项目，共同与 Agent 对话、查看开发进度、修改代码和调试应用。更多信息，请参考[多人协作 AI 编程](/cozespace/vibe_coding_collaboration)。
