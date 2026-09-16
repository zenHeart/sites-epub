> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

通过与编程 Agent 对话，你可以快速开发移动应用。无需编写代码、无需搭建开发环境，只需提出明确的开发需求即可从零开始完成应用的代码编写、部署上线。本文档介绍如何使用编程 Agent 开发移动应用。

## 功能概述 {#fe43b1cb}

扣子已将扣子编程平台封装为编程 Agent，提供了一个 AI 编程开发环境，你可以直接与编程 Agent 对话，描述你想要开发的应用的功能、界面、逻辑等需求，编程 Agent 会自动完成应用的开发、测试、迭代和发布。

支持开发各类移动应用，例如工具类应用（如待办清单、健康打卡）、互动类应用（如小游戏、社交聊天）、内容类应用（如资讯阅读、短视频社区）、电商类应用（如商品展示、电商订单管理）等。

:::tip 说明
* 应用开发完成后，可通过 Android 或 iOS 设备扫码预览应用效果。部署应用时，仅支持生成 Android APK 安装包。
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 费用说明 {#901867c0}

开发、测试、部署、线上使用应用时，以下操作将消耗你的扣子积分。

* [编程任务](https://docs.coze.cn/coze_pro/task_fee)：与编程 Agent 的每轮对话。
* [内置集成](https://docs.coze.cn/coze_pro/internal_integrations_fee)：调用大语言模型、联网搜索、图像生成等内置集成服务。
* [服务托管费用](/coze_pro_service_hosting_fee)：部署为线上服务，将产生服务托管费。

## 配额与限制 {#6fe941f3}

开发应用时，存在可创建的项目数量、可回滚版本数、可部署的次数等配额限制，详细说明，请参考[配额与限制](/guides/vibe_coding_limit)。

## 步骤一：创建编程项目 {#38d648e4}

::::tabs
@tab 网页端、桌面端
1. 在扣子左侧导航栏中，单击 + >**新建编程项目**。
2. （可选）团队版或企业版需要选择项目所属的工作空间，然后单击**确认**。
   ![Image=421x244](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9829629728224bdf94a935f1774fa505~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
1. 在扣子 App 顶部，单击 + >**新建编程项目**。
   ![Image=140x273](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4d5e0b014ef94d64867baaefde9dce35~tplv-goo7wpa0wc-topic.webp)
2. （可选）团队版或企业版需要选择项目所属的工作空间，然后单击**确认**。
   ![Image=127x250](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e68c80221f4d4f70a7d24386319e327d~tplv-goo7wpa0wc-topic.webp)
::::

## 步骤二：需求澄清 {#f500d89f}

::::tabs
@tab 网页端、桌面端

1. 创建编程项目并输入你的需求。
   1. 在编程项目中，单击**移动应用**选项卡。
   2. 在文本框输入你的提示词。
      你需要尽可能清晰地描述应用的功能、界面设计、业务逻辑等方面的要求。例如，你可以输入以下提示：
      ```Plain Text
      请帮忙开发一款「极简日常记账App」，具体要求如下：
      1. 实用性要求：
      - 核心用户：20-45岁的普通上班族，核心场景是日常消费后10秒内快速记账、睡前/月末查看收支明细。
      - 核心功能：仅保留“快速记账（选择收支类型+输入金额+备注）”“收支明细查询（按日/月筛选）”“简单统计（月度收支饼图）”，剔除所有冗余功能（如社交分享、广告推送等）。
      2. 易用性要求：
      - 界面设计：首页仅展示“+记账”主按钮（占屏幕下方固定位置）、今日收支概览，无复杂菜单栏。
      - 交互逻辑：记账时默认选中“支出”类型，金额输入支持数字键盘快速录入，备注可选填，点击“完成”即记账成功并给出“已保存”的视觉反馈。
      ```
2. （可选）进阶配置：通过上传附件、选择协作模式、添加技能、选择编程模型，让编程 Agent 生成的结果更精准、更符合你的预期。
   ![Image=517x184](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f2b3a08c081b41eda1acee14488edc9a~tplv-goo7wpa0wc-topic.webp)
   * 上传附件
      酌情上传一些图片或文件，作为附加信息提供给编程 Agent，以便编程 Agent 能更理解你的需求。例如上传一张你想参考的网站截图、想要的风格示例图片等，这些都能帮助编程 Agent 更精准地把握细节要求。
   * 选择协作模式
      默认情况下为 **Agent 模式**，如果你对需求不确定，可以先切换到**问答模式**讨论方案，待方案确认后，再切换到**Agent 模式**，由编程 Agent 根据此前的讨论结论执行开发任务。更多信息，请参考[如何选择协作模式？](https://docs.coze.cn/guides/vibe_coding_faq#3069a332)。
   * 添加技能
      在执行编程任务时，编程 Agent 可以按需加载技能，从而具备相应的专业领域知识和能力。例如，前端设计技能可以有效指导模型如何排版、设计配色和动画效果、处理背景等等，能显著提升模型的 UI 生成能力，减少产物视觉效果的“AI 味”。  更多信息，请参考[在扣子编程中使用技能](/guides/using_skill#3456ebc7)。
   * 选择编程模型
      扣子编程已集成 Doubao、GLM、Kimi、DeepSeek 等主流的编程模型，用于开发应用。为了达到较好的开发效果，系统会自动为你选择适合当前场景的模型，你也可以根据模型的官方介绍自行选择。
3. 单击**运行**图标，开始开发你的项目。
   编程 Agent 会根据你输入的提示词来开始设计应用、创建项目，并自动为项目设置应用名称。

@tab 移动端
1. 创建编程项目并输入你的需求。
   1. 在编程项目中，单击**移动应用**选项卡。
   2. 在文本框输入你的提示词。
      你需要尽可能清晰地描述应用的功能、界面设计、业务逻辑等方面的要求。例如，你可以输入以下提示：
      ```Plain Text
      请帮忙开发一款「极简日常记账App」，具体要求如下：
      1. 实用性要求：
      - 核心用户：20-45岁的普通上班族，核心场景是日常消费后10秒内快速记账、睡前/月末查看收支明细。
      - 核心功能：仅保留“快速记账（选择收支类型+输入金额+备注）”“收支明细查询（按日/月筛选）”“简单统计（月度收支饼图）”，剔除所有冗余功能（如社交分享、广告推送等）。
      2. 易用性要求：
      - 界面设计：首页仅展示“+记账”主按钮（占屏幕下方固定位置）、今日收支概览，无复杂菜单栏。
      - 交互逻辑：记账时默认选中“支出”类型，金额输入支持数字键盘快速录入，备注可选填，点击“完成”即记账成功并给出“已保存”的视觉反馈。
      ```
      ![Image=135x274](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6e6e3bc8073c4fafa23591e73248075d~tplv-goo7wpa0wc-topic.webp)
2. （可选）进阶配置：通过上传附件、选择协作模式、添加技能、选择编程模型，让编程 Agent 生成的结果更精准、更符合你的预期。
   ![Image=140x284](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1262add726c54c3592f393e36b3c3cc0~tplv-goo7wpa0wc-topic.webp)
   * 上传附件和添加技能
      * 酌情上传一些图片或文件，作为附加信息提供给编程 Agent，以便编程 Agent 能更理解你的需求。例如上传一张你想参考的网站截图、想要的风格示例图片等，这些都能帮助编程 Agent 更精准地把握细节要求。
      * 在执行编程任务时，编程 Agent 可以按需加载技能，从而具备相应的专业领域知识和能力。例如，前端设计技能可以有效指导模型如何排版、设计配色和动画效果、处理背景等等，能显著提升模型的 UI 生成能力，减少产物视觉效果的“AI 味”。  更多信息，请参考[在扣子编程中使用技能](/guides/using_skill#3456ebc7)。
   * 选择协作模式
      默认情况下为 **Agent 模式**，如果你对需求不确定，可以先切换到**问答模式**讨论方案，待方案确认后，再切换到**Agent 模式**，由编程 Agent 根据此前的讨论结论执行开发任务。更多信息，请参考[如何选择协作模式？](https://docs.coze.cn/guides/vibe_coding_faq#3069a332)。
   * 选择编程模型
      扣子编程已集成 Doubao、GLM、Kimi、DeepSeek 等主流的编程模型，用于开发应用。为了达到较好的开发效果，系统会自动为你选择适合当前场景的模型，你也可以根据模型的官方介绍自行选择。
3. 单击**运行**图标，开始开发你的项目。
   编程 Agent 会根据你输入的提示词来开始设计应用、创建项目，并自动为项目设置应用名称。
::::

## 步骤三：开发应用 {#28b0040e}

编程 Agent 收到你的需求之后，将立即启动需求分析，并规划开发流程和步骤，逐步生成应用的前后端代码。代码生成完毕后，自动构建并启动服务，以提供一个可视化的界面供你预览。

如果编程 Agent 判断你的应用需要数据库、存储、身份认证、AI 等能力，则会自动添加和配置对应的集成，为你的应用设计数据库表、配置存储系统，实现相关功能。 更多信息，请参考[集成服务概述](/guides/integrations_overview)。

::::tabs
@tab 网页端、桌面端
![Image=418x281](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/10140e791aaa4148bd971a0c0cfaf957~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
![Image=209x419](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/22aaec7587e94da8993e4726bf7ac546~tplv-goo7wpa0wc-topic.webp)
::::

## 步骤四：预览与测试 {#aa63ef44}

初步生成后端代码后，编程 Agent 会自动生成测试用例并完成一轮单元测试。测试通过后编程 Agent 会提供后端代码的预览，同时提醒你对后端开发部分进行验收。

::::tabs
@tab 网页端、桌面端
你可以在右侧**预览页面**查看实际运行效果。 应用预览界面如下：

![Image=346x354](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/21d6c5f0e71749e885e7cfcfbb566ba0~tplv-goo7wpa0wc-topic.webp)



@tab 移动端
你可以在页面中单击**预览**查看实际运行效果。 移动应用预览界面如下：

![Image=126x253](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1b5efd3440e04433b8eb1668895d1bf7~tplv-goo7wpa0wc-topic.webp)
::::

在预览与测试的环节中，你可以通过以下操作测试编程 Agent 为你生成的应用。

<!-- @cols-width: 100,397,239 -->
| | | | \
|**操作** |**说明** |**示例** |
|---|---|---|
|全面测试 |在预览区全面测试你的应用，通常建议关注以下问题： |\
| | |\
| |* **功能是否可用**：验证应用的核心链路是否完整可操作、数据的增删改查是否能成功执行。 |\
| |* **交互是否完善**：检查页面元素是否完整显示、布局是否合理、样式是否符合设计要求、各个按钮是否都能正确触发。 |\
| |* **AI 能力是否正常**：如果你的应用集成了 AI 能力，例如文本生成、图片生成等，验证 AI 模型的输出是否符合预期。 |* 网页端、桌面端 |\
| | |   ![Image=1135x1115](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b2f35eef92894003a40378028a97dcc4~tplv-goo7wpa0wc-topic.webp) |\
| | |* 移动端 |\
| | |   ![Image=89x179](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3f55f496a18d4587989c5cee335fb015~tplv-goo7wpa0wc-topic.webp) |
|修复故障 |通常情况下，编程 Agent 会自动识别并提示你修复故障，你可以根据页面提示，单击一键修复，允许编程 Agent 尝试修复这些问题。 |\
| | |\
| |如果你在体验应用的过程中触发页面报错，但编程 Agent 没有提示你修复，你也可以主动复制报错信息并粘贴到对话中，将其发送给编程 Agent，要求它修复故障。 |* 网页端、桌面端 |\
| | |   ![Image=2140x1149](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/71ee6d7e464041cb9c26b418471d1c09~tplv-goo7wpa0wc-topic.webp) |\
| | |* 移动端 |\
| | |   ![Image=102x200](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/606088f1415144c4961409182ada535b~tplv-goo7wpa0wc-topic.webp) |

## 步骤五：扫码预览应用 {#0b1215b4}

你可以使用 Android 或 iOS 设备进行预览。在[部署移动应用](/guides/deploy_a_mobile_app)后，Android 用户还可以下载生成的 APK 文件，以便将其上架到应用市场。

::::tabs
@tab 网页端、移动端
在**预览**页面，单击右下角二维码的**操作说明**，使用扣子 App 扫码预览您的应用。

![Image=221x243](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3908e335e87f434f8a763b8b9ef8080a~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
在**预览**页面，单击**手机**图标，预览应用。

![Image=142x274](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0e979c4eaea24f9f89f3ac8eb2a4e69a~tplv-goo7wpa0wc-topic.webp)
::::

## 步骤五：部署应用 {#11eedef7}

对于 Android 用户，完成应用的开发与测试之后，你可以将扣子编程搭建的应用部署为 APK 安装包。用户可自行下载安装使用，也可将 APK 安装包提交至 Android 应用市场。详细说明，请参考[部署移动应用](/guides/deploy_a_mobile_app)。

::::tabs
@tab 网页端、移动端
1. 单击页面右上角的**部署**图标，然后单击**开始部署**。
2. 按需配置部署信息。
3. 你可以使用默认配置，快速完成部署，也可以按需配置可见性、数据库、环境变量等配置。
4. 单击**开始部署**。
   ![Image=348x189](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7218072fb1a24ba7bb857a89f3629a50~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
1. 单击页面右上角的 **···** > **部署**，然后单击**开始部署**。
   ![Image=177x355](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4238354a5c2141368b4289c25db47766~tplv-goo7wpa0wc-topic.webp)
2. 按需配置部署信息。
   你可以使用默认配置，快速完成部署，也可以前往扣子网页版进行配置。
   ![Image=191x383](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c67fb8bddd004ae5a025e622639f29ff~tplv-goo7wpa0wc-topic.webp)
3. 单击**部署**。
::::

## 进阶操作 {#4c706bea}

关于开发应用的进阶操作，可以参考以下功能：

* 迭代应用：通过自然语言或直接修改代码，持续优化应用的功能、页面和交互。更多信息，请参考[迭代应用](/guides/vibe_coding_app#ec516e6a)。
* 集成服务：为应用接入 AI 模型、联网搜索、数据库、对象存储、用户登录等能力。更多信息，请参考[集成能力](/guides/vibe_coding_app#d912c5d4)。
* 回滚开发版本：当生成结果不符合预期、修复失败或应用状态异常时，可以在版本历史中将应用恢复到之前的正常版本，再继续迭代。更多信息，请参考[回滚开发版本](/guides/vibe_coding_app#6672685d)。
* 多人协作：邀请同一工作空间下的其他成员加入项目，共同与 Agent 对话、查看开发进度、修改代码和调试应用。更多信息，请参考[多人协作 AI 编程](/cozespace/vibe_coding_collaboration)。
