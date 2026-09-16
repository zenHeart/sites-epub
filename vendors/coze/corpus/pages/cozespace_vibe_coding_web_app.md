> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

通过与编程 Agent 对话，你可以快速开发网页应用。无需编写代码、无需搭建开发环境，只需提出明确的开发需求即可从零开始完成应用的代码编写、部署上线。本文档介绍如何使用编程 Agent 开发网页应用。

## 功能概述 {#dfca3665}

扣子已将扣子编程平台封装为编程 Agent，提供了一个 AI 编程开发环境。你可以创建一个编程项目，然后在对话区描述应用需求，例如应用功能、页面风格、业务逻辑、用户流程等。编程 Agent 会根据你的描述分析需求，规划开发步骤，并生成应用所需的前端和后端代码。代码生成后，系统会自动构建并启动服务，你可以直接在预览区体验应用效果。

如果应用需要数据库、对象存储、用户登录、AI 生成、联网搜索等能力，编程 Agent 也可以根据需求添加扣子编程的内置集成，并引导你完成必要配置。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 费用说明 {#8d9b70d9}

开发、测试、部署、线上使用应用时，以下操作将消耗你的扣子积分。

* [编程任务](https://docs.coze.cn/coze_pro/task_fee)：与编程 Agent 的每轮对话。
* [内置集成](https://docs.coze.cn/coze_pro/internal_integrations_fee)：调用大语言模型、联网搜索、图像生成等内置集成服务。
* [服务托管费用](/coze_pro_service_hosting_fee)：部署为线上服务，将产生服务托管费。

## 配额与限制 {#hk9m7vftt}

开发网页应用时，存在可创建的项目数量、可回滚版本数、可部署的次数等配额限制，详细说明，请参考[配额与限制](/guides/vibe_coding_limit)。

## 开发应用 {#0ba8c9a0}

参考以下流程，通过编程 Agent 开发网页应用。

## 步骤一：创建编程项目 {#f1fffc2c}

::::tabs
@tab 网页端、桌面端
1. 在扣子左侧导航栏中，单击 + >**新建编程项目**。
2. （可选）团队版或企业版需要选择项目所属的工作空间，然后单击**确认**。
   ![Image=452x262](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9829629728224bdf94a935f1774fa505~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
1. 在扣子 App 顶部，单击 + >**新建编程项目**。
   ![Image=129x251](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4d5e0b014ef94d64867baaefde9dce35~tplv-goo7wpa0wc-topic.webp)
2. （可选）团队版或企业版需要选择项目所属的工作空间，然后单击**确认**。
   ![Image=131x258](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e68c80221f4d4f70a7d24386319e327d~tplv-goo7wpa0wc-topic.webp)
::::

## 步骤二：需求澄清 {#a2fff1be}

::::tabs
@tab 网页端、桌面端
1. 输入你的需求。
   1. 在编程项目中，单击**网页应用**选项卡。
   2. 在文本框输入你的提示词。
      你需要尽可能清晰且详细地描述应用的功能、界面设计、业务逻辑等方面的要求。例如，你可以输入以下提示：
      ```Plain Text
      创建一款能够根据用户输入的热点主题，自动检索并生成对应新闻信息卡片的网页应用。
      1. 支持热点主题输入功能，用户可输入关键词或主题。
      2. 具备新闻检索能力，能自动获取当天与主题相关的10条热点新闻。
      3. 支持图片生成功能，为每条新闻生成1张比例为3:4的4K信息卡片，以图片形式概述新闻内容。
      4. 提供图片管理功能，允许用户查看、整理生成的10张信息卡片，用于发布小红书"每日信息差"主题的新闻图片合集。
      ```
      ![Image=422x273](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/56c40750d1b24042879c57789c04d634~tplv-goo7wpa0wc-topic.webp)
2. （可选）进阶配置：通过上传附件、选择协作模式、添加技能、选择编程模型，让编程 Agent 生成的结果更精准、更符合你的预期。
   ![Image=434x127](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c4d7687f81ce43029a23f92918ba8214~tplv-goo7wpa0wc-topic.webp)
   * 上传附件
      酌情上传一些图片或文件，作为附加信息提供给编程 Agent，以便编程 Agent 能更理解你的需求。例如上传一张你想参考的网站截图、想要的风格示例图片等，这些都能帮助编程 Agent 更精准地把握细节要求。
   * 选择协作模式
      默认情况下为 **Agent 模式**，如果你对需求不确定，可以先切换到**问答模式**讨论方案，待方案确认后，再切换到**Agent 模式**，由编程 Agent 根据此前的讨论结论执行开发任务。更多信息，请参考[如何选择协作模式？](https://docs.coze.cn/guides/vibe_coding_faq#3069a332)。
   * 添加技能
      在执行编程任务时，编程 Agent 可以按需加载技能，从而具备相应的专业领域知识和能力。例如，前端设计技能可以有效指导模型如何排版、设计配色和动画效果、处理背景等等，能显著提升模型的 UI 生成能力，减少产物视觉效果的“AI 味”。 更多信息，请参考[在扣子编程中使用技能](/guides/using_skill#3456ebc7)。
   * 选择编程模型
      扣子编程已集成 Doubao、GLM、Kimi、DeepSeek 等主流的编程模型，用于开发应用。为了达到较好的开发效果，系统会自动为你选择适合当前场景的模型，你也可以根据模型的官方介绍自行选择。
3. 单击**运行**图标，开始开发你的项目。
   编程 Agent 会根据你输入的提示词来开始设计应用、创建项目，并自动为项目设置应用名称。

@tab 移动端
1. 输入你的需求。
   1. 在编程项目中，单击**网页应用**选项卡。
   2. 在文本框输入你的提示词。
      你需要尽可能清晰且详细地描述应用的功能、界面设计、业务逻辑等方面的要求。例如，你可以输入以下提示：
      ```Plain Text
      创建一款能够根据用户输入的热点主题，自动检索并生成对应新闻信息卡片的网页应用。
      1. 支持热点主题输入功能，用户可输入关键词或主题。
      2. 具备新闻检索能力，能自动获取当天与主题相关的10条热点新闻。
      3. 支持图片生成功能，为每条新闻生成1张比例为3:4的4K信息卡片，以图片形式概述新闻内容。
      4. 提供图片管理功能，允许用户查看、整理生成的10张信息卡片，用于发布小红书"每日信息差"主题的新闻图片合集。
      ```
      ![Image=129x252](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cdfee553a1e04d4986b08d7e348527a7~tplv-goo7wpa0wc-topic.webp)
2. （可选）进阶配置：通过上传附件、选择协作模式、添加技能、选择编程模型，让编程 Agent 生成的结果更精准、更符合你的预期。
   ![Image=161x315](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7cd88ae5ae5c4a2db06a8dcf57e7c0f3~tplv-goo7wpa0wc-topic.webp)
   * 上传附件和添加技能
      * 酌情上传一些图片或文件，作为附加信息提供给编程 Agent，以便编程 Agent 能更理解你的需求。例如上传一张你想参考的网站截图、想要的风格示例图片等，这些都能帮助编程 Agent 更精准地把握细节要求。
      * 在执行编程任务时，编程 Agent 可以按需加载技能，从而具备相应的专业领域知识和能力。例如，前端设计技能可以有效指导模型如何排版、设计配色和动画效果、处理背景等等，能显著提升模型的 UI 生成能力，减少产物视觉效果的“AI 味”。 更多信息，请参考[在扣子编程中使用技能](/guides/using_skill#3456ebc7)。
   * 选择协作模式
      默认情况下为 **Agent 模式**，如果你对需求不确定，可以先切换到**问答模式**讨论方案，待方案确认后，再切换到**Agent 模式**，由编程 Agent 根据此前的讨论结论执行开发任务。更多信息，请参考[如何选择协作模式？](https://docs.coze.cn/guides/vibe_coding_faq#3069a332)。
* 选择编程模型
   扣子编程已集成 Doubao、GLM、Kimi、DeepSeek 等主流的编程模型，用于开发应用。为了达到较好的开发效果，系统会自动为你选择适合当前场景的模型，你也可以根据模型的官方介绍自行选择。
3. 单击**运行**图标，开始开发你的项目。
   编程 Agent 会根据你输入的提示词来开始设计应用、创建项目，并自动为项目设置应用名称。
::::

## 步骤三：开发应用 {#9df8a90a}

编程 Agent 收到你的需求之后，将立即启动需求分析，并规划开发流程和步骤，逐步生成应用的前后端代码。代码生成完毕后，自动构建并启动服务，以提供一个可视化的界面供你预览。

如果编程 Agent 判断你的应用需要数据库、存储、身份认证、AI 等能力，则会自动添加和配置对应的集成，为你的应用设计数据库表、配置存储系统，实现相关功能。更多信息，请参考[集成服务概述](/guides/integrations_overview)。

::::tabs
@tab 网页端、桌面端
![Image=456x298](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5fa80b3ac8dd4819b9a2db12cecf3014~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
![Image=160x319](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6ac10233a0d740ff8882fda5f068379c~tplv-goo7wpa0wc-topic.webp)
::::

## 步骤四：预览与测试 {#9243745f}

初步生成后端代码后，编程 Agent 会自动生成测试用例并完成一轮单元测试。测试通过后编程 Agent 会提供后端代码的预览，同时提醒你对后端开发部分进行验收。

::::tabs
@tab 网页端、桌面端
你可以在右侧**预览页面**查看实际运行效果。 网页应用预览界面如下：

![Image=284x237](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6dae10e9227247a7b266b4de1d18fe90~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
你可以在页面中单击**预览**查看实际运行效果。 网页应用预览界面如下：

![Image=165x313](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/de218064b9f3419bad06255ed5947eaa~tplv-goo7wpa0wc-topic.webp)
::::

在预览与测试的环节中，你可以通过以下操作测试编程 Agent 为你生成的应用。

<!-- @cols-width: 100,409,239 -->
| | | | \
|**操作** |**说明** |**示例** |
|---|---|---|
|全面测试 |在预览区全面测试你的应用，通常建议关注以下问题： |\
| | |\
| |* **功能是否可用**：验证应用的核心链路是否完整可操作、数据的增删改查是否能成功执行。 |\
| |* **交互是否完善**：检查页面元素是否完整显示、布局是否合理、样式是否符合设计要求、各个按钮是否都能正确触发。 |\
| |* **AI 能力是否正常**：如果你的应用集成了 AI 能力，例如文本生成、图片生成等，验证 AI 模型的输出是否符合预期。 |* 网页端、桌面端 |\
| | |   ![Image=1447x557](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6bf00d5bdf72462785ede4e2ded1a6ba~tplv-goo7wpa0wc-topic.webp) |\
| | |* 移动端 |\
| | |   ![Image=112x212](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/30c5dff8db4c46de8a8b42a8a8cbc3b7~tplv-goo7wpa0wc-topic.webp) |
|修复故障 |通常情况下，编程 Agent 会自动识别并提示你修复故障，你可以根据页面提示，单击一键修复，允许编程 Agent 尝试修复这些问题。 |\
| | |\
| |如果你在体验应用的过程中触发页面报错，但编程 Agent 没有提示你修复，你也可以主动复制报错信息并粘贴到对话中，将其发送给编程 Agent，要求它修复故障。 |* 网页端、桌面端 |\
| | |   ![Image=1837x674](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/40e9c0258aaa48c18e1de2c01b0c3afe~tplv-goo7wpa0wc-topic.webp) |\
| | |* 移动端 |\
| | |   ![Image=128x252](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e3aed3177e6041f6b73bf3f899c5aeae~tplv-goo7wpa0wc-topic.webp) |

## 步骤五：部署应用 {#c45931d7}

完成应用的开发与测试之后，你可以将应用部署成为一个公开可访问的在线项目，以便服务于真实用户。详细说明，请参考[部署网页应用](/guides/deploy_vibe_web)。

::::tabs
@tab 网页端、桌面端
1. 单击页面右上角的**部署**图标，然后单击**开始部署**。
2. 按需配置部署信息。
   你可以使用默认配置，快速完成部署，也可以按需使用自定义域名，配置可见性、数据库、环境变量等配置。
3. 单击**开始部署**。
   ![Image=384x234](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7b758d2759904b67b3cb0a3e1002dc56~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
1. 单击页面右上角的 **···** > **部署**，然后单击**开始部署**。
   ![Image=125x249](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0c40f46ef7e9489faccdce8a8ac1f4f6~tplv-goo7wpa0wc-topic.webp)
2. 按需配置部署信息。
   你可以使用默认配置，快速完成部署，也可以前往扣子网页版进行配置。
   ![Image=127x254](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ddb6ce545424472a80990b0a6aa40aeb~tplv-goo7wpa0wc-topic.webp)
3. 单击**部署**。
::::

## 进阶操作 {#a6c54d20}

关于开发应用的进阶操作，可以参考以下功能：

* 迭代应用：通过自然语言或直接修改代码，持续优化应用的功能、页面和交互。更多信息，请参考[迭代应用](/guides/vibe_coding_web_app#794facfc)。
* 集成服务：为应用接入 AI 模型、联网搜索、数据库、对象存储、用户登录等能力。更多信息，请参考[集成能力](/guides/vibe_coding_web_app#d912c5d4)。
* 回滚开发版本：当生成结果不符合预期、修复失败或应用状态异常时，可以在版本历史中将应用恢复到之前的正常版本，再继续迭代。更多信息，请参考[回滚开发版本](/guides/vibe_coding_web_app#6672685d)。
* 多人协作：邀请同一工作空间下的其他成员加入项目，共同与 Agent 对话、查看开发进度、修改代码和调试应用。更多信息，请参考[多人协作 AI 编程](/cozespace/vibe_coding_collaboration)。
