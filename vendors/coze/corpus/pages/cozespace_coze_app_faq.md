> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

## 概念相关 {#565fbe83}

### 扣子 3.0 都有哪些特色能力？ {#e931c7a6}

2026 年 5 月 29日，扣子正式发布了全新的 3.0 版本，带来以下核心特性：

* **多人多 Agent 协作：** 开启全新 Agent 协作方式，一人+多Agent / 多人+多Agent灵活组合，@一下全员就位。多项目独立管理，资产自动沉淀，让团队协作更有序。
* **专业伙伴，开箱即用：​**Coze Agent 持续满配在线，主流模型自由切换，长期记忆+工作台，越用越懂你；从开发到上线，在编程项目中轻松完成；从灵感到成片，在视频项目中尽情创作。
* **你的Agent，你来定义：​**本地 Agent 开放接入，Claude Code、Codex CLl、OpenClaw、Hermes 一键接入，轻松托管；精品行业模版，帮你创建专家 Agent。
* **行业专家，攻克难题：​**为复杂场景而生，自媒体、法律、金融、互联网、医疗健康，轻松加载行业专家技能，解决垂直行业难题。
* **手机电脑跨端同步，任务持续推进：​**桌面端全新上线，可授权 Agent 处理本地文件；App 端同步升级，编程/视频项目手机随时推进；跨端内容同步，用手机遥控处理本地电脑文件。

### 扣子 2.5 都更新了什么？ {#2d33d678}

扣子 2.5 版本中，从被动执行任务的 AI 工具升级为主动规划、决策执行的新一代 AI 助手。

* **保留原本功能**：
   * **核心能力不变**：扣子 2.5 依然支持 AI 创作和 AI Office，无论是长文、绘本、动图、海报、播客、网页、视频，还是 PPT、Word、Excel、图表，扣子仍旧可以陪你拆解复杂问题、直接交付产物。
   * **升级长期计划**：长期计划升级为 Agent 日程，但是别担心，扣子会将已经创建的长期计划拆解为具体日程，持续推进。
   * **更先进的视频创作能力**：从剧本到成片，自动完成分镜拆解、素材匹配、视频合成；支持持续对话创作续集，打造长篇连载；全新的 AI 视频剪辑器，海量素材快速生成。
* **全新的产品形态**：不再只是一个聪明的对话框，而是一个让 AI 伙伴持续生存、协作与进化的广阔世界。
   * **满配的数字员工**：不是只能聊天建议，而是能独立执行、定时运行、后台推进任务的数字员工。
   * **零门槛创作大师**：导演级视频专家，从想法到成片，扣子帮你全流程自动完成。串联剧本、分镜、生成画面、配上音乐的全流程。
   * **养成系专属伙伴**：它有自己的专属邮箱身份，更有一个永不掉线的“心智记忆”。不管你是在微信上随口提的要求，还是在飞书上布置的任务，它都默默记在心里，是你的“养成系”靠谱搭档。
   * **AI 优先的开发基建**：扣子 CLI 是专为 Agent 打造的编程接口，你负责出架构思路，扣子 CLI 负责把代码写完、跑通并自动部署。
   * **Agent 专属的数字世界**：有它的专属邮箱，能在 Agent World 探索更多可能，还能自主学习。AI 伙伴不再是用完即走，而是与你一同成长。

### 和 OpenClaw 有什么区别？ {#571e1b90}


* **开箱即用的满级专家**：无需手动部署，注册即可拥有一个能力满级的专家级助手。视频制作、PPT 生成、海量的预置技能课随时应对各行业的复杂挑战，无需调教直接交付高质量成果。
* **Agent 专属工作台**：扣子拥有自己专属的日程、文件、手机和电脑设备，无需操作用户设备即可自主完成任务。扣子还拥有自己的邮箱地址，以独立身份探索数字世界，与其他 Agent 协作交流，不断成长，记住你也记住自己。
* **更安全稳定的服务**：免运维的云端服务，7×24小时全天稳定在线，企业级的 SLA，更加安全稳定。

## 协作相关 {#6756d7ad}

### 项目和普通对话有什么区别？ {#aa1a79a4}

主要区别如下：

* 每个项目都有独立的上下文，不同主题不会混在同一个主对话里。
* 项目可以邀请人类成员和 Agent 加入协作。
* 项目成员可以通过 @ 成员或 @Agent 的方式推进任务。
* 项目中的消息、文件和 Agent 产物会保留在当前项目中，方便后续继续跟进。
* 多个 Agent 可以分工处理任务，也可以基于已有结果接力推进。

### Agent 可以@人类成员或者@其他 Agent 吗？ {#938f457a}

目前，Agent 可以 @ 人类成员，但暂不支持直接 @ 其他 Agent。

也就是说，Agent 可以在协作中提醒或请求人类成员补充信息、确认结果；但不能主动调度其他 Agent、为其他 Agent 分配任务，或统筹多个 Agent 协同工作。

当前只有人类成员可以 @Agent 并向其派发任务。

### 扣子编程 Agent 和视频 Agent 不能加到项目里吗? {#f8f65221}

暂不支持在普通项目中添加扣子编程 Agent、扣子视频 Agent。但是编程项目支持多人协作，你可以和其他项目成员一起用自然语言在编程项目中开发并部署应用。

## 定制 Agent 相关 {#9113ab53}

### 扣子 Agent、三方精选 Agent 和本地 Agent 有什么区别？ {#435408d4}

三者的核心差异不在于功能多少，而在于**运行位置、协作方式、权限治理和平台化能力**。

* **扣子 Agent**：扣子原生助手，开箱即用，适合大多数日常办公和内容类任务。
* **三方精选 Agent**：运行在扣子云电脑里的专业 Agent，适合长任务、自动化、代码开发和团队协作。
* **本地 Agent**：运行在你自己电脑上的 Agent，适合处理本机文件、本地代码、本地软件和私有环境。

三者可以组合使用——扣子作为统一入口，将不同 Agent 汇聚到同一会话中，统一管理、调用和协作。

### 如何选择扣子 Agent、三方精选 Agent 和本地 Agent ？ {#deeab9fb}

* 如果你想快速拥有一个开箱即用的 AI 助手，选择扣子 Agent。它适合内容创作、办公协作、资料整理、视频制作、日程邮件等通用任务，也适合非技术用户使用。
* 如果你想使用 Claude Code、Codex CLI、OpenClaw、Hermes 等 Agent 框架，但不想自己安装和配置环境，选择三方精选 Agent。它运行在扣子提供的云电脑中，不依赖你的本地电脑在线。
* 如果任务需要访问你电脑里的文件、代码、软件或私有环境，选择本地 Agent。它可以接入你本地已部署的 Agent，并使用本机环境完成相关任务。

### 三方精选 Agent 和本地 Agent 有什么区别？ {#0d84fe5d}

三方精选 Agent 的优势是稳定运行、统一模型调用、权限治理和团队协作。它运行在扣子云电脑中，不依赖你的本地电脑在线，适合长任务、自动化和项目协作。

本地 Agent 的优势是复用你的真实电脑环境。它可以访问你授权的本机文件、代码仓库、终端环境、开发工具、插件、MCP、Hooks 和私有配置，适合处理强依赖本机环境的任务。

### 创建 Agent 之后如何查看 Agent 类型？ {#3bd3c1c1}

各个 Agent 支持的核心能力不同，比如仅 Coze Agent 支持使用自定义模型。所以创建 Agent 之后往往需要查看 Agent 类型。查看方式如下：

找到指定的 Agent，点击它的头像，在详情页中查看 Agent 类型标识。例如下图展示的 Agent 有 **Coze Agent** 的文字标识。

![Image=614x360](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bf5ab92c175348d7a219dee54c26f89d~tplv-goo7wpa0wc-topic.webp)

### 为什么我的 Agent 必须部署在云电脑上？ {#95b5814e}

Claude Code、Codex、OpenClaw、Hermes 等 Agent 框架，本质上是一个持续运行的服务进程，它们需要一台真实的服务器来承载运行环境、维持连接、响应调用，因此创建三方精选 Agent 时，需要选择一台云电脑进行部署。

## 扣子 Agent {#79bdc587}

### **行业模板创建和云端创建的扣子 Agent 有什么区别？** {#7c10b918}

你可以通过两种方式创建扣子 Agent：基于平台内置的行业模板创建、通过三方精选 Agent 创建。

* 基于行业模板创建，适合需要垂直领域专家的场景。你可以直接选择平台预置的行业模板，例如投资理财顾问、调研分析师、科研助理、法务顾问、自媒体运营达人等，快速生成具备专业设定、工作方法和技能的 Agent。
* 通过三方精选 Agent 创建，适合需要专门处理固定任务的场景。你可以根据自己的工作目标创建专属 Agent，例如客户跟进 Agent、学习研究 Agent、内容运营 Agent 或项目整理 Agent 等，让它拥有独立的人设，并围绕同一类任务长期工作。

## 三方精选 **Agent 相关** {#258f80a8}

### **云端 Claude Code、Codex CLI、OpenClaw 、Hermes 与原生版本有什么区别？** {#5d8bb800}

云端版本是将 Claude Code、Codex CLI、OpenClaw、Hermes 框架的 Agent Runtime 部署在扣子云电脑中运行，模型调用接入的是扣子提供的大模型，不使用你自己的 Claude、OpenAI 等账号。

**三方精选 Agent 能做什么：**

* 在云电脑工作区读写文件、搜索代码、运行命令、执行任务。
* 保留各框架的工作方式：Claude Code、Codex CLI 偏代码协作与工程执行；OpenClaw 偏长任务、多渠道接入；Hermes 偏长期记忆和技能沉淀。
* 稳定运行，统一部署、权限和计费限流。
* 可在扣子内直接创建、管理，并加入会话和协作项目。

**相比原生，主要差异：**

* 无法访问你的本机文件、IDE、浏览器、本地 Shell 环境。
* 不继承本机安装的插件、MCP、Hooks 及私有配置。
* 模型列表、上下文长度、限流和计费由扣子统一管理，与直连官方账号有所不同。
* 命令执行、网络访问、文件访问范围受云电脑安全策略约束。

### 我可以通过三方精选 Agent 登录自己的 Claude 账号吗？ {#8efa8f4e}

不可以。扣子提供的是**基于 Claude Code 框架运行的三方精选 Agent**，并不是 Anthropic 官方 Claude Code 应用，不支持登录 Claude 账号或使用 Claude 官方订阅权益，模型调用由扣子统一提供。

如果你希望使用自己的 Claude 账号，可以通过本地 Agent 将你本机已运行的 Claude Code 接入扣子。具体操作，请参考[本地 Agent](/cozespace/local_agent)。

### 三方精选 Claude Code Agent 是否需要我有 Anthropic Claude 账号？ {#0464d761}

不需要。扣子中的云端 Claude Code Agent 是基于 Claude Code 的开源框架构建的，并非 Anthropic 官方产品的入口。你无需注册或登录任何 Claude Anthropic 账号，也不会调用你个人的 Claude 订阅配额。

### 三方精选 **Agent 使用的是 Claude、OpenAI 的模型吗？** {#44a52a1f}

不是，扣子的三方精选 Agent 使用的是扣子平台提供的大模型，并非直接使用你的 Claude 或 OpenAI 账号下的模型。目前，支持 Deepseek-V4-Pro、GLM-5.3、Doubao-Seed-2.1-pro、Kimi K3 等模型，你也可以自定义接入模型。

![Image=327x210](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7a2008a3535349459c21d755b4e44bf5~tplv-goo7wpa0wc-topic.webp)

### **云端 Codex CLI Agent 是否需要 OpenAI 账号或 API Key？** {#4cac12f1}

不需要。扣子中的云端 Codex CLI Agent是基于 **Codex CLI** 的开源框架构建的，并非 OpenAI 官方的 Codex CLI 应用。

你无需注册 OpenAI 账号、配置 OpenAI API Key 或开通 OpenAI 付费服务。

### 三方精选 **Agent 会访问我本地电脑的文件或系统吗？** {#8fa79254}

不会。所有三方精选 Agent 运行在扣子提供的云端服务器中，与你的本地设备完全隔离，不会访问、读取或修改本地文件。

### **创建**三方精选 **Agent 时，我需要在本地安装任何软件或配置环境吗？** {#4ad983ad}

不需要。三方精选 Agent 的运行环境由扣子统一提供和维护，你只需在扣子平台上操作即可，无需本地配置。

## 本地 Agent 相关 {#86f7620d}

### 什么是终端？ {#d3327573}

终端可以简单理解为电脑里一个**可以输入命令并查看结果的窗口**，是你和电脑之间通过命令沟通的桥梁。很多开发工具、自动化工具和本地 Agent，都是在终端里启动和运行。

![Image=342x214](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b3bbf8c2835e42069b66fda21815e616~tplv-goo7wpa0wc-topic.webp)

常见操作系统的打开方式如下：

::::tabs
@tab macOS
* 打开**启动台**，搜索并打开**终端**。
* 按下 `Command + 空格`打开聚焦搜索，输入 `终端` 或 `Terminal`，然后按回车。

@tab Windows
* 在**开始**菜单搜索`终端`**、**`Windows Terminal `或 `命令提示符`，然后打开。
* 按键盘上的 `Win + R` 键，输入 `cmd` 或 `wt`，然后按回车。
::::

### 出现 npm not found、npx not found 错误，怎么处理？ {#bebdc231}

这类错误通常是运行环境中 Node.js 未安装或路径未生效导致的（npm 和 npx 都是 Node.js 自带工具）。npm 和 npx 都是 Node.js 自带的工具，安装并启用 Node.js 后一般即可解决。

你可以按以下步骤排查：

1. 检查 Node.js 是否已安装。
   ```Markdown
   node -v
   npm -v
   npx -v
   ```
   三条命令均返回版本号，说明安装正常，可能是路径问题，重启终端后重试。若提示找不到命令，继续下一步。
2. 检查 nvm 是否可用。
   ```Markdown
   command -v nvm
   ```
   有返回值说明 nvm 已安装，继续下一步。若无返回，需先安装 nvm 或直接安装 Node.js。
3. 通过 nvm 安装并启用 Node.js。
   ```Plain Text
   nvm install --lts
   nvm use --lts
   ```
4. 重新验证。
   ```Markdown
   node -v
   npm -v
   npx -v
   ```
   三条命令均返回版本号，说明 Node.js、npm 和 npx 已可正常使用。   


### 本地 Agent 连接掉线了，怎么处理？ {#eda5f9ac}

在使用本地 Agent 过程中，如果本地 Agent 与扣子的连接断开，请按以下步骤重新连接：

1. 单击 **Agent 设置**图标，单击**重新连接**。
   ![Image=307x253](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/02fdbdddb70a43908b0904504df83348~tplv-goo7wpa0wc-topic.webp)
2. 复制连接地址。
   ![Image=352x247](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/16712a94beb04e208d31099e41437a04~tplv-goo7wpa0wc-topic.webp)
3. 在本地终端执行连接命令。
   ![Image=342x218](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7b65b92268bc430da10929bfec17a7a3~tplv-goo7wpa0wc-topic.webp)
4. 回到扣子页面，单击**我已执行**。
5. 等待系统完成重新连接。

### 本地能接入的 Agent 类型包括哪些？ {#72bd9090}

目前，本地 Agent 支持接入你已经部署在本地电脑上的主流 Agent，包括：

* **Claude Code CLI**：适合本地代码开发、代码修改、项目排查等工程任务。
* **Codex CLI**：适合读取、修改和运行本地代码项目。
* **OpenClaw 及基于 OpenClaw 开源框架的各类 Agent**：适合自动化任务、文件处理、多工具协作等场景。
* **Hermes** ：适合持续任务、长期记忆、经验沉淀和技能生成场景。

### 支持接入本地的 Hermes 吗？ {#18704a6b}

支持，你在本地环境中安装 Hermes Agent 后，可以将其接入到扣子。具体操作，请参考[本地 Agent](/cozespace_local_agent)。

### 接入本地 Agent 有数量限制吗？ {#3af8b8f9}

各个订阅套餐能接入的本地 Agent 数量不一，其他类型的 Agent 暂无数量限制。

<!-- @cols-width: 154,112,112,120,103,100,120,107,100,112,120 -->
| **套餐权益**  | **个人免费版**  | **个人进阶版**  | **个人高阶版**  | **个人旗舰版**  | **个人尊享版**  | **团队高阶版**  | **团队旗舰版**  | **团队尊享版**  | **企业标准版**  | **企业旗舰版**  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 连接本地 Agent 数量  | 1个 | 1个  | 3个  | 10个  | 不限制  | 每个成员3个  | 每个成员10个  | 不限制  | 不限制  | 不限制  | \
| | | | | | | | | | | | \
| | （限时免费）  | | | | | | | | | |

### 为什么我的本地 Agent 没有授权模式选项？ {#hE0HSPiZz}

如果本地 Agent 的对话输入框中没有出现**授权模式**选项，表示该 Agent 可能还未升级到支持授权模式的版本。你可以单击**升级**，并按照页面提示完成升级操作。

升级完成后，你可以在输入框中选择对应的授权模式，用于控制 Agent 在执行文件修改、联网访问等操作时是否需要先向你确认。同时，升级后的版本将在后续更新中支持自动升级。

需要注意的是，Codex CLI 和 Claude Code 框架支持在对话框中选择**授权模式**，OpenClaw 不支持。

::::cols
@col 50
![Image=297x338](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bbb07682e0ce475a8f03bbeef821815e~tplv-goo7wpa0wc-topic.webp)

@col 50
![Image=365x268](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/399e8ef6f7a641d584f01e4686307362~tplv-goo7wpa0wc-topic.webp)
::::

## 编程项目相关 {#a228794f}

### 扣子和扣子编程的编程能力完全一致吗？ {#1a57ff27}

不完全一致。

* 扣子（coze.cn）中的 AI 编程能力基于扣子编程提供，但它是对扣子编程部分能力的封装，主要面向在对话中快速创建、修改、预览和部署编程项目。目前支持的产物类型包括网页、App、小程序和从扣子编程导入的项目。
* 扣子编程（code.coze.cn）主站提供更完整的开发工作台和项目管理能力，适合进行更深入的开发、配置和管理。例如，如果你需要使用更完整的项目配置、集成管理，或开发智能体、工作流等更复杂的 AI 产物，建议前往扣子编程完成。

简单来说：

* 想在对话中快速创建网页、App、小程序项目，或者修改已有的扣子编程项目，可以使用扣子中的 AI 编程。
* 想进行更专业、完整的项目开发和配置管理，建议使用扣子编程。

### 如何删除编程项目？ {#d2f9bb51}

你可以通过如下方式删除编程项目。

:::notice 注意
删除后，项目全部内容将被清空，扣子编程侧的项目会同步删除且无法恢复，请谨慎操作。
:::

::::tabs
@tab 网页端、桌面端
在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)对话列表中，单击目标 Agent 对应的 **···** > **删除对话**。

![Image=469x355](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b152ad15ff1f4c4499c1cb1efec5bc48~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
1. 在扣子 App 中，单击目标 Agent。
2. 单击 Agent 名称。
3. 在项目详情中，单击··· > **删除项目**。
   ![Image=352x357](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e66f85bfe8fa4b3d854ffcd13fb3127a~tplv-goo7wpa0wc-topic.webp)
::::

## 视频相关 {#c92bcf63}

### 我之前创建的视频项目在哪里？ {#729f2f04}

扣子已于 2026 年 5 月 29 日 全新改版，在扣子 3.0 中，新创建的视频项目已改造为会话流的形式。所有在此之前创建的视频项目仍会保留，你可以在**对话**列表 > **历史视频项目**中找到它们。

::::cols
@col 50
历史视频项目入口：

![Image=378x201](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/36e4ffcec2374906833d0394c3e9138a~tplv-goo7wpa0wc-topic.webp)

@col 50
历史视频项目列表：

![Image=371x197](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/23d6eb0d031b4010b4768467d9229128~tplv-goo7wpa0wc-topic.webp)
::::

### 视频项目不能多人协作吗？ {#863da196}

正在紧锣密鼓准备中，敬请期待。

## 对话相关 {#5339e7ea}

### 如何新建话题？ {#bd195257}

在扣子中，默认只有一个主对话。现在你可以通过“创建项目”开启新的独立工作空间。创建项目时，需要选择一个 Agent。每个项目都会基于所选 Agent 创建一条独立的 Session，也就是一段独立的上下文和对话任务。不同项目之间互不干扰，各自保存自己的对话历史、对话任务、文件和日程。

此外，项目中还支持多人多 Agent 协作，你可以邀请其他用户和 Agent 加入项目，组建团队来一起工作。详细说明可参考[项目与协作](/cozespace/collaboration)。

创建项目的方式如下：

::::tabs
@tab 网页端、桌面端
1. 登录扣子。
2. 在对话列表区域单击 +，并选择**新建项目**。
3. 填写项目名称，并选择要加入到项目中的 Agent。
4. 单击**创建项目**。
   ![Image=314x257](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e42fd6f313ce45c5a6b72d9fd2388bb0~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
1. 打开并登录扣子 App。
2. 在对话列表区域单击 +，并选择**新建项目**。
3. 选择要加入到项目中的 Agent。
4. 选择**完成**。
   ![Image=299x581](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fc74d0a59ae24195a04624bf998c1fd5~tplv-goo7wpa0wc-topic.webp)
::::

### 什么是已归档对话？ {#9bc6689e}

在扣子 2.5 升级之前，你和扣子的每一次不同主题的对话都是独立的，其中包含不同的对话记录和上下，是你和旧版扣子之间已经完成的所有对话记录的集合。这些对话现已被归档。

在全新的扣子中，你可以在通过以下方式找到这些对话。

::::tabs
@tab 网页端、桌面端
在扣子主页左上角单击**对话** > **已归档对话**。

![Image=397x249](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c5782aaef553411280cc3117abb04d97~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
在扣子 App 首页，选择“历史对话”，即可找到所有已归档的对话。

![Image=260x480](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/64043a50a6034a98ac62d642c356da10~tplv-goo7wpa0wc-topic.webp)
::::

### 各个平台的对话是打通的吗？ {#63eaa79d}

是的，扣子支持网页端、桌面端和移动端多端使用。同一账号登录后，项目、对话、文件和设置会自动同步，你可以在不同设备之间自然接力任务。即使不在电脑旁，也可以在手机上继续推进任务，或遥控处理个人电脑里的文件。

### 各个渠道的对话是打通的吗？ {#aec67a98}

各个渠道对话不是打通的，但记忆打通。例如你无法在飞书看到和扣子在微信的具体对话记录，但是飞书的扣子也会记得你在微信叮嘱过它的事情。

### 可以把对话分享给其他人吗？ {#46f002ef}

可以。把你和扣子对话的精彩瞬间分享给你的社交好友，让其他 Agent 一起学习、进化。

1. 登录 coze.cn。
2. 在对话中找到扣子的精彩回复，并单击分享图标。
3. 选择你想分享的对话内容，选择是否允许访问对话中的文件，并单击**复制分享链接**。
4. 将分享链接发送给你的好友，或者分享到社交平台。

::::cols
@col 33
分享对话

![Image=2430x1634](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4ab3ccadf8ae4ab98f4dcbc36378e6b9~tplv-goo7wpa0wc-topic.webp)

@col 33
分享设置

![Image=2476x1640](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/98f0f60e6dae496aa3843ce7018a7139~tplv-goo7wpa0wc-topic.webp)

@col 33
查看分享链接

![Image=1846x1644](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/11518d077cb645f8b348dd56e15500ef~tplv-goo7wpa0wc-topic.webp)
::::

### 如何删除扣子的对话记录、聊天记录？ {#098567da}

出于隐私保护和数据安全的要求，暂不支持删除你和扣子的聊天记录、对话内容。

### 可以重置扣子，或者清空对话吗？ {#d4638233}

暂不支持。但是你可以创建一个新的扣子 Agent，为它赋予全新的身份和记忆，和扣子重新认识一下。

### 扣子对话能保证隐私安全吗？ {#48c236c5}

扣子采用以下措施来保证你的数据安全和信息安全。

* 数据加密：传输和存储采用加密技术
* 权限控制：对话内容仅你可见，即使是企业中的其他成员也无法访问。
* 企业版：提供更严格的数据隔离和权限管理，关于企业版的安全特性，可参考[扣子官网](https://www.coze.cn/overview/enterprise/trust&safety?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。

使用扣子之前，请先阅读[扣子隐私政策](/guides/privacy)、[扣子用户协议](/guides/terms-of-service)。

### 哪些 Agent 支持自定义模型？ {#df1b7efd}

目前仅 Coze Agent 支持自定义模型，包括你默认拥有的 Agent，以及你通过以下方式创建的 Agent：

* 新建 Agent > 选择职业模板。
* 新建 Agent > 三方精选 Agent > Coze Agent。

你可以在 Agent 详情页中看到 Coze Agent 的标识。

![Image=614x360](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bf5ab92c175348d7a219dee54c26f89d~tplv-goo7wpa0wc-topic.webp)

### 不支持@收藏夹文档了吗？ {#fff747bd}

扣子 3.0 改版后，已不再支持通过 @ 或 / 在对话中引用收藏夹中的文档或收藏夹标签。

目前，你无法在对话中使用收藏夹标签，也无法引用收藏夹中的文档。

### **深度截图和普通截图有什么区别？** {#hq4eNwgK8}

普通截图只记录屏幕上可见的画面。深度截图除了截取窗口画面，还会尝试获取应用提供给系统的可读取文本，其中可能包含当前屏幕上没有显示的内容。截取结果会直接添加到扣子对话，无需手动保存和上传。

### **如何修改深度截图快捷键？** {#hwS5lsiBq}

进入**系统设置 > 快捷键 > 深度截图**，选择**自定义**并按下新的快捷键。你也可以选择**恢复默认**。

### **按下深度截图快捷键没有反应？** {#hN7qPXe62}

* 确认**系统设置 > 客户端设置**中的深度截图开关已打开。
* 确认按下的快捷键与设置中显示的一致，且没有被其他应用占用。
* 在 macOS 上，确认已开启屏幕录制和辅助功能权限。
* 如果刚刚完成授权，请按照系统提示重启扣子后重试。

如果仍然无法使用，可以尝试更换快捷键。

## 邮箱相关 {#72e8246f}

### 可以修改扣子 Agent 邮箱地址/邮箱名称/邮箱前缀吗？ {#b64d1589}

一旦设定邮箱地址之后，暂不支持修改。但是你可以为扣子 Agent 重新注册一个邮箱账号，让它改为使用新邮箱。需要注意的是，更换邮箱之后，之前的邮件等通信记录将不可见，请谨慎操作。

发送以下指令让扣子 Agent 更换一个邮箱账号。

```Plain Text
请为你自己重新注册一个邮箱账号，前缀是xxxx。
```

### 可以注销扣子邮箱吗？ {#d69ee318}

暂不支持注销邮箱。如果你对扣子 Agent 的邮箱账号不满意，可以通过指令让它更换一个邮箱账号，例如：

```Plain Text
请为你自己重新注册一个邮箱账号，前缀是xxxx。
```

### 扣子 Agent 只有一个邮箱吗？ {#bd2dc6ec}

是的，扣子 Agent 同时只能使用一个邮箱账号，如果注册了新邮箱账号，将同时弃用旧的。更换邮箱账号之前，可以让你的 Agent 保留自己的邮箱通讯录，逐个通知 Agent 朋友这个换号消息。

## 记忆相关 {#80d5076a}

### “记不住”、“失忆”怎么办？ {#abb7a3a2}

**问题现象**：你之前用过`记住：...`或在对话里说过的重要信息，这次问起时，扣子表示“不知道”、“未找到相关记录”。

**可能原因：​**信息在首次描述时太模糊，模型难以抽取出可复用的“事实”。

**解决方式**：

* 把它当成一个第一次上手的新同事，尽可能描述清晰、完整，以便扣子提炼重点。
* 提醒扣子尝试查询记忆或者搜索，比如“你看看你的记忆”、“搜索历史话题回忆”。

### 回忆信息错误、记忆信息太乱怎么办？ {#18334890}

**现象**：回答里用错了人名/时间/指标，或者给出的结论与你的记忆不一致，看起来像是“幻觉”。

**可能原因：**

* 同一件事情在不同时间被反复记忆，记忆里关于某个项目、某个人的信息较多，无法提取出最新的进展和状态。
* 记忆、知识包和对话上下文的信息发生冲突，模型选择了过时或不正确的一条。
* 某条暂时性的对话内容被当成长期事实使用。

**解决方式：**

让扣子重新整理自己的记忆文件，提取出所有关于指定主题的信息，整合为一条。参考以下对话：

```Plain Text
帮我整理一下关于3月份新品推广项目的所有记忆，把过时的信息（比如之前提到的2月底截止日期）标注出来，再把不同会话里提到的推广渠道、预算、进度等相似信息整合统一，只保留最新的状态和关键信息，更新到 MEMORY.md。
```

确认无误后再说：

```Plain Text
请以后一律按照最新记忆回答，不要再使用旧版本。
```

### 如何指定或更改记忆的写入位置？ {#800b69ea}

**如果**你希望精确控制某条记忆写入哪一类档案，比如把一次群聊结论沉淀到主对话的长期记忆里，而不是随便写在某个会话下。可以参考以下方式实现：

**解法：**

* **在话术中直接点名文件**：
   ```Plain Text
   更新到 MEMORY.md：将今天群聊中确认的xx整理成一条正式记忆，供后续所有相关方案引用。
   ```
* **帮你调整历史记忆的位置**：
   ```Plain Text
   请把之前散落在不同会话里的xx相关记忆整理出来，合并成一条，并写入我主对话下的 MEMORY.md。    
   ```
* **确认写入结果**：改动完成后，可以让扣子复述它刚刚写入了哪一份文件、采用了什么结构，便于你在记忆中心快速核对。哪怕第一次写错了位置，也可以通过一两句纠偏话术让它重新整理。

### 如何修改记忆文件？ {#6762c316}

暂不支持手动编辑 `Memory.md` 等记忆文件，如需修改，你可以直接和扣子对话，请它帮你补充记忆、修正记忆。例如扣子原本不知道你喜欢的颜色，所以 `Memory.md`  中没有相关记录，你可以告诉扣子，然后就能在 `Memory.md` 中看到了，扣子也会在后续的对话中记住这一点。

::::cols
@col 33
告诉扣子你的喜好：

![Image=1586x732](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d1826c5be05845bfa40e674a322e0752~tplv-goo7wpa0wc-topic.webp)

@col 33
检查记忆文件：

![Image=237x125](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b55d08ccb74547ebbe1989fa3b419fe3~tplv-goo7wpa0wc-topic.webp)

@col 33
后续对话中展现记忆：

![Image=137x124](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ed922578770c45df976a4716302e56ee~tplv-goo7wpa0wc-topic.webp)
::::

### 如何查看记忆文件？ {#9522e63a}

注意，仅**扣子 Agent** 和**云端 OpenClaw Agent** 支持在线查看记忆文件。

查看方式如下：

::::tabs
@tab 网页端、桌面端
打开扣子，找到你的扣子 Agent 或三方精选 Agent，点击右上角的文件图标，在**记忆**页签查看记忆文件的内容。

![Image=326x208](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3685835ff7ca4ba789a991de926d0a2c~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
打开扣子，找到你的扣子 Agent 或云端 Agent，在右上角的折叠菜单中选择文件，并在**记忆**页签查看记忆文件的内容。

![Image=142x277](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f692f2a7b95c46b1944e883a911d3e00~tplv-goo7wpa0wc-topic.webp)
::::

### Agent 在项目里的记忆和主对话的记忆是相通的吗？ {#778e3b08}

是的。

同一个 Agent 的主对话和项目对话会共用同一份长期记忆。也就是说，用户在项目里与 Agent 对话时，如果产生了可沉淀的偏好、身份信息、重要事实或长期上下文，这些内容会进入该 Agent 的记忆文件，后续在主对话或其他项目中也可以被该 Agent 参考。

需要注意的是，**项目不会单独生成一份“项目记忆文件”**。因此你在查看 Agent 记忆文件时，可能只看到主对话、渠道等入口，而看不到按项目拆分的记忆文件。这是正常现象，并不代表项目里的记忆没有生效。

## 渠道相关 {#55d66151}

### 如何换绑飞书账号？ {#2bb42527}

扣子默认为你已授权的飞书账号创建机器人应用，如需在其他账号下创建，你可以在[扣子配置](https://www.coze.cn/configure?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)页面取消授权再重新授权。

::::tabs
@tab 网页端
1. 打开扣子的[配置页面](https://www.coze.cn/configure?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
2. 在渠道连接区域找到飞书渠道，单击**︙**> **关闭渠道**，取消当前授权。
   ![Image=312x119](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d2e9298393fe40438a08e397d6ce857c~tplv-goo7wpa0wc-topic.webp)
3. 重新选择**添加渠道**>**飞书**，根据页面提示进行授权。
   在飞书授权过程中，单击**使用其他账号**，需要换绑的飞书账号重新授权。
   ![Image=217x250](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ed677336b8794b4b9ce057458a95d8a6~tplv-goo7wpa0wc-topic.webp)

@tab 手机端
1. 登录扣子 App。
2. 在左侧导航栏，单击**渠道**，然后单击飞书对应的**取消授权**。
3. 使用目标飞书账号重新登录飞书 App。
4. 返回扣子 App，单击飞书对应的**去授权，​**根据页面提示，完成授权。
::::

### 如何换绑微信账号？ {#cb9dd8b6}

如果你已经为扣子绑定了微信渠道，暂不支持直接换绑，但你可以关闭微信渠道，重新绑定时选择另一个微信账号。

::::tabs
@tab 网页端
> 换绑前，请先在手机微信上登录要绑定的微信账号。

1. 打开扣子的[配置页面](https://www.coze.cn/configure?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
2. 在渠道连接区域，找到微信渠道，并单击**︙**> **关闭渠道**。
   ![Image=358x200](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/620bc08407244eef8d0fe027018cfec8~tplv-goo7wpa0wc-topic.webp)
3. 重新选择**添加渠道**>**微信**。
   ![Image=392x150](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/37bd1ba979cb4ca38ec4568e8bde76cb~tplv-goo7wpa0wc-topic.webp)
4. 根据页面提示，使用微信客户端扫码并完成授权。
5. 在手机微信客户端上找到 ClawdBot，发送消息即可对话。

@tab 手机端
> 换绑前，请先在手机微信上登录要绑定的微信账号。

1. 登录扣子 App。
2. 在左侧导航栏，单击**渠道**。
   ![Image=153x331](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8210f4854b174fcd8ab54d7d16145387~tplv-goo7wpa0wc-topic.webp)
3. 找到微信渠道，选择**取消授权**，并确认。
4. 取消成功后，再选择**去授权**，并保存二维码到相册。
   ![Image=155x336](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5a4e9572d2064444b384ce191d0aeed2~tplv-goo7wpa0wc-topic.webp)
5. 打开微信 App，登录要换绑的新账号，并扫描相册中保存的二维码图片。
6. 根据页面提示，完成授权。
::::

### 如何修改飞书机器人的名称和头像？ {#db1788d7}

1. 登录[飞书开放平台](https://open.feishu.cn/app?lang=zh-CN)，找到你的飞书机器人应用。
   ![Image=364x144](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1b431213def84641a380c876a49b8309~tplv-goo7wpa0wc-topic.webp)
2. 为飞书机器人修改名称和头像。
   1. 单击目标应用。
   2. 按以下图示修改名称和头像。
      ![Image=309x256](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/53772fb48dfd4eab85ee25f6ab4de203~tplv-goo7wpa0wc-topic.webp)
3. 新建机器人版本并发布。
   1. 单击顶部的**创建版本**按钮。
   2. 按需配置应用版本号、默认能力及更新说明等信息，并在页面底部的**保存**按钮，创建版本。
   3. 根据页面提示发布应用。
      ![Image=349x159](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/82ae639e15cb450e89a9e45f58dcb997~tplv-goo7wpa0wc-topic.webp)      


待管理员通过发布审核后，即可正式在飞书中使用全新的飞书官方插件，体验新版效果。

![Image=468x150](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/483471033cb24dabb9e5de656ae560eb~tplv-goo7wpa0wc-topic.webp)

## 日程相关 {#f18edaf8}

### 我之前创建的长期计划在哪里？ {#1138a7ca}

扣子**长期计划**已升级为**日程**，不限制任务数量，新版本中也取消了长期计划的创建入口。如果你之前创建了长期计划，可以通过以下方式继续推进：

* **自动升级**：首次和新版扣子对话时，扣子会引导你完成初始化流程，例如给扣子取个名字、介绍你自己等等，同时扣子也会主动帮你整理历史的长期计划列表，并询问你是否需要重启长期计划。跟随扣子的引导，确认需要重启的范围即可。
* **对话重启**：如果你直接跳过了初始化流程，也可以主动给扣子下发指令，要求重启长期计划，例如“**`帮我重启长期计划`**”。扣子接到任务后也会调用长期计划迁移技能，引导你选择要重启的计划范围。
   ![Image=297x198](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/950990f071be49338f549f6c5f1c08a4~tplv-goo7wpa0wc-topic.webp)
* **批量重启**：如果你需要迁移的长期计划数量较多，建议使用一键批量重启。在扣子左侧导航栏中找到**长期计划重启**，并单击**批量重启**即可，扣子会引导你选择重启的计划范围。
   ![Image=284x277](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d09f162f8b0549d49389d5c2c7cd7225~tplv-goo7wpa0wc-topic.webp)   


确认迁移后，扣子会根据以下流程规划新日程：

1. **确认历史文件的目标迁移路径**。扣子不会删除长期计划中已生成的文件，只是复制一份到新版扣子的文件目录下。
2. **帮你规划新的日程**。扣子会仔细阅读你的长期计划，并规划出新的日程，以持续推进。
3. **请你确认日程规划**。扣子会向你介绍后续的日程规划，待你确认后才生效执行。

> 如果你在迁移长期计划时遇到任何问题，可随时[提交反馈](https://bytedance.larkoffice.com/share/base/form/shrcnYfaV5LyPOfiS3TmvqyfMFb)。

### 新版扣子如何创建长期计划？ {#14260368}

扣子**长期计划**已升级为**日程**，不限制任务数量。你可以随时和扣子对话，它会把你的目标拆为具体的日程计划，并以持续推进。

例如创建一个 3 个月雅思 7 分的学习计划：

::::cols
@col 50
制定日程

![Image=405x277](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/257561a3fc64410eaeab5e7e272c73f3~tplv-goo7wpa0wc-topic.webp)

@col 50
查看日程

![Image=413x243](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/10697c5f9ca44c478d7e981c098ec3b7~tplv-goo7wpa0wc-topic.webp)
::::

## 设备相关 {#b4539b80}

### 云设备都有哪些规格，如何选择？ {#1ebfb9a3}

* 云手机：目前提供以下规格。具体可选范围以你的套餐权益和页面展示为准。
   <!-- @cols-width: 155,100,390 -->
   | **设备规格**  | **系统盘**  | **适用场景**  |
   | --- | --- | --- |
   | 2 vCPU / 6 GiB  | 45GB  | 适合浏览单个 App、查找信息、整理少量内容等轻量任务。  |
   | 4 vCPU / 12 GiB  | 91GB  | 适合在多个 App 间切换，执行信息收集、内容整理等中等强度任务。  |
   | 8 vCPU / 24 GiB  | 182GB  | 适合运行较重的 App，或执行长时间、高频率的批量操作任务。  |
* 云电脑：目前提供以下规格。具体可选范围以你的套餐权益和页面展示为准。
   <!-- @cols-width: 153,100,400 -->
   | **设备规格**  | **系统盘**  | **适用场景**  |
   | --- | --- | --- |
   | 2 vCPU / 4 GiB  | 40GB  | 适合单个 Agent 执行轻量任务，例如浏览网页、填写简单表单、运行小脚本。  |
   | 4 vCPU / 8 GiB  | 60GB  | 适合常驻任务和多工具协作，例如网页自动化、文件处理、轻量数据分析。  |
   | 8 vCPU / 16 GiB  | 80GB  | 适合多个 Agent 并行运行，或执行持续时间较长的脚本和自动化任务。  |
   | 16 vCPU / 32 GiB  | 100GB  | 适合高并发、长时间运行和较大规模数据处理，例如批量分析文件或运行较重脚本。  |
   | 32 vCPU / 64 GiB  | 120GB  | 适合超大规模并行任务和重度数据处理，例如大量文件批处理、复杂计算或高负载自动化任务。  |
* **如何选择规格**：
   * 如果只是处理轻量任务，例如查看网页、整理少量信息、执行简单脚本，通常选择较低规格即可。
   * 如果任务需要多个 Agent 并行、长时间运行、多工具协作，或处理较大的数据和文件，建议选择更高规格。
   * 添加云设备之后，支持扩容的套餐可以在设备详情页对云设备进行扩容。扩容后设备性能会提升，费用也会相应变化。
   * 目前暂不支持缩容，或更换到更低的设备规格。具体可调整范围以页面展示为准。

### 云电脑是个人独享的吗？ {#87739169}

是的，云电脑是分配给你的独享资源，即使你没有访问云电脑，也不会有其他用户访问它。

### 云设备能保证信息安全吗？ {#9bb4a3c9}

扣子和云设备之间采用加密传输，保证你的数据传输安全和信息安全。但是扣子建议你关注以下规则，以免泄露个人信息：

* 禁止在云设备上安装任何不明来源的第三方软件，包括但不限于浏览器等，以免病毒感染。
* 建议不要将你的私人手机号、银行卡账号密码、社交账号及密码发送给 Agent，推荐为 Agent 注册专用账号。

### 使用云手机登录软件，会被封号吗？ {#3106706e}

存在封号风险。

请明示知悉：第三方产品或服务可能对云手机、虚拟环境或自动化操作设有安全风控机制。云手机及相关服务无法保证精准识别所有重要操作。若因以下行为导致账号封禁、财产损失、数据泄露或第三方服务纠纷，平台不承担任何赔偿责任：

1. 授权云手机自动执行任务并触发第三方风控。
2. 未审慎进行人工确认，或发现操作错误后未及时终止任务。
3. 通过技术手段绕过云手机或第三方产品的安全机制。

因此，建议你使用各类手机应用之前，为扣子注册专属的应用账号，以便扣子自行探索网络世界。如果直接在云手机登录你的私人账号，因自动化规律操作，极易被其他平台判定为机器人行为，导致封号。

### 浏览器为什么总是间歇性黑屏？ {#c11c7cd6}

这是因为云端的浏览器是**无头模式**（headless）运行的，没有图形界面，只有命令行。你看到的偶尔黑屏，是因为它会可视化渲染后截屏拍照，黑屏表示一次快照。

### 云手机可以扫码登录或者人脸识别吗？ {#0e465a92}

暂不支持。由于是虚拟设备，云手机没有摄像头等物理硬件，因此无法进行二维码扫描或人脸识别。请更换其他登录方式。

### 为什么安装 App 时提示“此用户无权限安装此应用”？ {#d3b3354d}

原因是扣子云手机暂不支持安装此 App。云手机目前支持通过设备自带的应用商店下载并安装大部分热门、常用的手机 App，如抖音、今日头条、微博、QQ 等，暂不支持安装UC 浏览器等浏览器工具、云代理、VPN 等工具。

### 云手机和云电脑可以安装代理软件、VPN 吗？ {#e1066325}

安全起见，云手机和云电脑暂不支持安装代理软件或 VPN。

### 云设备支持访问海外网站吗？ {#a8195fd7}

暂不支持。

### 云设备能换个系统吗？ {#80d78f8f}

云电脑和云手机暂不支持更换操作系统。

### 云设备怎么没有声音？ {#8e9ebf0c}

云手机和云电脑是云端操作环境，没有音频播放设备，暂时也未配置音频通道，所以播放音频和视频是没有声音的。

## 技能相关 {#38f65ff9}

### 什么是技能包和数据集？ {#34aad4f3}

* **技能包**是面向行业场景的扣子官方严选技能组合，扣子将多个技能打包成一套可一键安装、统一展示、统一使用的行业解决方案，帮助你的 Agent 快速具备特定行业场景下的专业能力
* **数据集**是带有数据查询或数据 API 能力的特殊技能，帮助 Agent 获取和使用特定数据。

### 我开发的技能可以上架到技能商店吗？ {#e50ea448}

可以，具体上架流程可参考[上架技能](/cozespace/publish_skill)。上架技能之前，请先参考[技能商店新手指南](/cozespace/skill_store_onboarding_guide)、[技能审核自查指南](/cozespace/skills_audit_self_check)了解商店技能的要求。

## 云盘相关 {#754ce152}

### 如何删除文件？ {#6b98aef6}

你可以通过与 Agent 对话删除文件，也可以在云盘中手动删除。

::::cols
@col 33
Agent 删除——删除指定文件

在与 Agent 对话中，引用目标文件，然后输入**删除文件**。

![Image=340x169](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/caadeae7fdcb4eef9bb6fd7a876bbf21~tplv-goo7wpa0wc-topic.webp)

@col 33
Agent 删除——批量删除文件

在与 Agent 对话中，描述你的需求，让 Agent 自行整理并批量删除文件。参考示例如下：

> 整理下自己的工作文件，删除 3 个月内没访问的文件

![Image=326x313](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3dc8e942e7cf4ae09b160e6607fa2efa~tplv-goo7wpa0wc-topic.webp)

@col 33
手动删除

在**云盘**页面的目标文件夹中，找到要删除的文件，单击**删除**。

如果有多个文件要删，可以先勾选它们，再批量删除。

![Image=1707x396](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3804519b19a84933a2498b9b8c4ea92e~tplv-goo7wpa0wc-topic.webp)
::::

### **升级到云盘后，我原来的文件去哪了？** {#hzefvfgmy}

升级到云盘后，历史 Agent 或项目中的文件会自动整理到云盘中。系统会为历史 Agent 或项目生成对应文件夹，你可以在云盘中继续查看、管理和复用这些文件。

Agent 的记忆文件，例如 `SOUL.md`、`USER.md`、`MEMORY.md` 等，不会迁入云盘，仍保留在 Agent 设置中。

### **云盘和原来的文件，有什么区别？** {#hymyRnbT8}

原来，项目和 Agent 的工作目录由系统自动生成，文件保存在各自的工作目录中，不支持复用。

现在，创建 Agent 或项目时，你可以选择某个云盘文件夹作为工作目录。被选为工作目录后，Agent 可以读取和使用该文件夹内的文件。这样，同一批资料可以被多个项目或 Agent 复用，无需重复上传。

云盘支持桌面端本地同步。开启后，你可以像使用本地文件夹一样编辑云盘文件，修改内容会同步到云盘。

### **云盘提示"空间不足"怎么办？** {#hWuIBnXBM}

你可以通过以下方式释放或增加云盘空间：

* **清理文件**：删除不再需要的文件。删除后的文件会先进入垃圾箱，垃圾箱中的文件仍会占用云盘空间。清空垃圾箱后，空间才会真正释放。
* **升级容量**：升级订阅套餐，或购买云盘扩容包（部分套餐支持）。

### **删除云盘文件后，还能找回吗？** {#hRLsbhuR8}

可以，但有时间限制。删除后的文件会先进入垃圾箱，并保留 30 天。在此期间，你可以随时恢复。

超过 30 天后，文件会被自动清理。如果你手动清空垃圾箱，文件也会被彻底删除，无法恢复。请谨慎操作。

### **哪些文件会占用云盘空间？** {#hmqWStjAM}

以下文件保存在工作目录中，占用云盘空间：

* 你和项目协作者上传的素材：在 Agent 对话和项目中上传的图片、文档、表格、音视频等文件。
* 扣子生成的产物：扣子根据你的要求生成的文件，例如日报、周报、统计报表、分析结果、PPT、图片、视频等。

其他如下文件，不进入云盘，也不占用云盘配额：

* Agent 记忆文件（SOUL.md、USER.md、MEMORY.md 等）
* 编程项目文件（独立存储）
* 视频项目文件（独立存储）

### **飞书群成员能看到我的云盘吗？** {#hJ32M5Maa}

看不到。飞书群成员无法直接浏览你的云盘，也不能查看完整工作目录。

他们只能收到 Agent 在飞书对话中主动发出的具体文件。此时，文件会以附件形式发送到飞书群中。

### **Agent 能访问我的所有云盘文件吗？** {#hoXm9cpGs}

不能。Agent 能访问哪些文件，取决于它当前所在的场景和权限。

* 单聊时：Agent 可以读写自己的工作目录，也可以只读它参与的项目工作目录。
* 项目中：Agent 默认读写当前项目的工作目录，也可以读写 Agent 私有的工作目录。
   如果 Agent 需要访问或编辑其他项目的文件，需要获得对应项目 Owner 授权。   


### **本地同步会同步整个云盘吗？** {#hZFRwxp03}

开启云盘本地同步时，你可以手动选择目标云盘文件夹。如果不选择，则会默认同步整个云盘。

### 云盘**本地同步**到我电脑的哪个位置？ {#haSkFga41}

开启云盘本地同步后，文件会自动同步到你电脑本地的固定目录，不支持修改。

* macOS：`/Users/你的用户名/Coze/Drive`
* Windows：`%USERPROFILE%\Coze\Drive`

## 本地工作目录相关 {#huazBsHLY}

### 云盘文件夹和本地目录作为工作目录有什么区别？ {#hjLBswMKy}

创建项目时，你可以选择云盘文件夹或本地目录作为项目工作目录。

* **选择云盘文件夹**：项目资料、文件和生成产物会保存在扣子云盘中，适合大多数场景，也方便在不同设备上使用。项目还可以添加成员，适合和团队一起围绕某个话题、目标或任务持续协作。更多信息，请参考[项目与协作](/cozespace_collaboration)。
* **选择本地目录**：将你电脑上的某个文件夹会作为项目工作目录。项目里的 Agent 可以在你授权后围绕该目录读取、处理和保存文件，适合已有本地文件、不方便搬迁或希望产物直接保存在本地目录的场景。选择本地目录作为工作目录的项目只支持添加项目 Owner、三方精选 Agent 和本地 Agent，不支持添加团队成员。

### 本地连接断开了，如何处理？ {#hpBzD2wDU}

当桌面端和本地设备断开时，你可以在桌面端的**项目设置**页面中，单击**重新连接**。连接恢复后，Agent 就可以继续访问和操作本地目录中的文件。

![Image=376x277](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/63f3cc6375ef4ba897c11442669506da~tplv-goo7wpa0wc-topic.webp)

### 项目本地目录和本地设备有什么区别？ {#hBVQoa4BM}

二者都可以让 Agent 在你授权后处理电脑上的本地文件，但适用场景不同。

* **本地设备**：更适合在 Agent 单聊中读写本地文件。开启**允许 Coze 访问本地文件**权限后，Agent 可以在当前 Agent 单聊中处理你授权的文件或目录。更多信息，请参考[本地设备](/cozespace_local_device)。
* **在项目中选择本地目录**：从项目中使用，更适合围绕一个固定文件夹持续工作。创建项目时选择本地目录后，该目录会作为项目工作目录。项目里的 Agent 可以在你授权后围绕这个目录读取、处理和保存文件，相关对话、文件操作和生成产物也会沉淀在项目中。
   安装桌面端后，系统会在你的电脑上配置一个后台服务（bridge），用来保持本地电脑和扣子之间的连接。   


### 为什么我创建本地工作目录失败，提示环境依赖有缺失？ {#hCvKzheiQ}

使用本地目录创建项目时，扣子桌面端需要使用电脑上的 Node.js 环境建立本地连接。如果未安装 Node.js、Node.js 版本过低，或相关组件因网络问题下载失败，就可能出现该提示。

你可以按以下步骤检查 Node.js 是否已正确安装。完成后，重启桌面端并重新创建项目。

::::tabs
@tab macOS
1. 检查 Node.js 是否已安装。
   ```Markdown
   node -v
   npm -v
   npx -v
   ```
   三条命令均返回版本号，说明安装正常，可能是路径问题，重启终端后重试。若提示找不到命令，继续下一步。
   ![Image=306x105](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3c146e26061347ea8205414d2b374969~tplv-goo7wpa0wc-topic.webp)
2. 通过 nvm 安装 Node.js。
   1. 安装 nvm。
      ```Markdown
      curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
      ```
   2. 检查 nvm 是否可用。
      ```Markdown
      command -v nvm
      ```
      有返回值说明 nvm 已正确安装，继续下一步。
      ![Image=317x58](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/07ce4fa41e904be1ac6ba42ad0d87b10~tplv-goo7wpa0wc-topic.webp)
   3. 安装并启用 Node.js。
      ```Plain Text
      nvm install --lts
      nvm use --lts
      ```
4. 重新验证。
   ```Markdown
   node -v
   npm -v
   npx -v
   ```
   三条命令均返回版本号，说明 Node.js、npm 和 npx 已可正常使用。然后重启桌面端，继续创建项目。

@tab Windows
1. 检查 Node.js 是否已安装。
   ```Markdown
   node -v
   npm -v
   npx -v
   ```
   三条命令均返回版本号，说明安装正常，可能是路径问题，重启终端后重试。若提示找不到命令，继续下一步。
2. 通过 nvm 安装 Node.js。
   1. 安装 nvm-windows。
      ```Markdown
      winget install CoreyButler.NVMforWindows
      ```
      安装完成后，关闭当前 PowerShell 窗口，然后重新打开 PowerShell。
   2. 检查 nvm 是否可用。
      ```Markdown
      nvm version
      ```
      如果返回版本号，说明 nvm 已正确安装，继续下一步。
   3. 安装并启用 Node.js。
      先查看可安装的版本：
      ```Plain Text
      nvm list available
      ```
      从列表中选择最新的 LTS 版本，例如 `22.18.0`，然后执行：
      ```Plain Text
      nvm install 22.18.0
      nvm use 22.18.0
      ```
      示例中的 `22.18.0` 替换为列表中实际显示的最新 LTS 版本。
3. 重新验证。
   ```Markdown
   node -v
   npm -v
   npx -v
   ```
   三条命令均返回版本号，说明 Node.js、npm 和 npx 已可正常使用。然后重启桌面端，继续创建项目。
::::

## 平台相关 {#8f40f5e1}

### 如何下载扣子 App？ {#e35d5358}

扣子 App 支持 Android、iOS 系统下载。

你可以在 Android 应用市场或 Apple Store 下载扣子 App，也可以通过扣子官网，直接扫码下载。

![Image=168x411](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a55ac0a66fa44e5d87faa7b2ecd286c1~tplv-goo7wpa0wc-topic.webp)

### 移动端支持扣子编程吗？ {#29260928}

支持，移动端扣子 App 现已支持通过以下方式使用扣子编程的 AI 编程能力：

* 编程项目：在扣子一键创建编程项目，和其他项目成员一起开发和部署网页应用、移动应用或小程序。关于编程项目能做什么，可参考[AI 编程概述](/cozespace/w7dfyn5j)。
* Coze CLI：扣子预安装了 Coze CLI，即使在手机上也可以让扣子通过 CLI 来调用扣子编程的 AI 编程能力，例如创建并部署网页应用等。关于 Coze CLI 能做什么，可参考[Coze CLI 介绍](/developer_guides/coze_cli)。

### 移动端不能查看或者创建智能体吗？ {#3a727b79}

即将支持。扣子预安装了 Coze CLI，即使在手机上也可以让扣子通过 CLI 创建并部署网页应用。Coze CLI 未来将陆续支持扣子编程的所有 AI 编程能力，包括创建智能体、查看智能体等等。目前的 Coze CLI 能做什么，可参考[Coze CLI 介绍](/developer_guides/coze_cli)。

### 移动端和网页端数据互通吗？ {#513cddc2}

互通。使用同一个扣子账号登录后，你在网页端、移动端和桌面端看到的设备、Agent 和任务信息会保持同步。

例如，你可以在网页端创建云设备，在移动端查看设备状态；也可以在移动端向 Agent 下达任务，让在线的桌面端继续处理本地电脑上的文件。

需要注意的是，本地设备能力依赖扣子桌面端。如果要通过移动端或网页端操作本地电脑，请确保对应电脑处于唤醒状态，并已打开扣子桌面端应用程序。

### 桌面端支持哪些快捷键？ {#hegaD2te2}

启动扣子桌面端后，使用以下快捷键即可快速**唤醒**或**收起**应用：

* macOS：`Cmd` + `Shift` + `Space（空格）`
* WIndows：`Ctrl` + `Shift` + `Space（空格）`

要自定义或重置快捷键，可打开**设置>快捷键**。

![Image=429x156](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0cd9a7d597d446ff93a56852bf548d06~tplv-goo7wpa0wc-topic.webp)

## 套餐相关 {#36978bd9}

### 如何购买或升级订阅套餐？ {#f2ff0982}

你可以在网页端或者手机端购买或升级订阅套餐。

::::tabs
@tab 网页端
访问[扣子订阅套餐购买页](https://code.coze.cn/subscription-paywall?dist_channel=33336&dist_code=wd)，根据你的业务需求选择套餐，并完成支付。

![Image=370x213](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/02d83afea5ba4a6295269c32d009209e~tplv-goo7wpa0wc-topic.webp)

@tab 手机端
1. 登录扣子 App。
2. 在左下角单击**积分**卡片。
3. 在套餐卡片区域，根据页面提示完成购买。
   ![Image=114x224](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/94a900d4a20b4ba287ebcb990eab7f49~tplv-goo7wpa0wc-topic.webp)
::::

### 扣子 App 支持哪些支付渠道？ {#04534ef3}

目前，扣子 iOS App 支持 Apple Pay 支付；扣子 Android App 支持支付宝、抖音支付。

### 为什么在扣子 App 内无法升级或取消订阅？ {#d769894a}

在扣子 App 内无法升级或取消订阅的原因是不同支付渠道（Apple Pay、支付宝、抖音支付）之间的订阅管理不互通，订阅关系会被你首次发起订阅的支付渠道锁定。例如你在 Android 端通过支付宝订阅套餐后，如果在扣子 iOS App 端取消订阅，系统会提示前往原订阅渠道完成取消操作。

### 已经购买套餐，为什么还是有水印？ {#e061c88c}

会员生成图片是支持无水印的，你可以这样开启：

* APP：右上角设置-通用设置-开启“保存时无 AI 生成水印”
* 网页端：左下角头像-设置-通用设置-开启“保存时无 AI 生成水印”

根据国家法律法规要求，目前需要由用户来手动开启这个设置，平台无法代用户开启，感谢您的理解与支持。

### 和其他个人版相比，个人尊享版有什么高级权益？ {#9350283f}

个人尊享版是个人版最高档，主要优势包括：

* **积分最多**：99.9 万积分/月。
* **本地 Agent 不限量**：高于旗舰版的 10 个。
* **项目协作人数最多**：每个项目最多 50 人。
* **新模型优先内测**：个人版中仅尊享版支持。
* **视频排队优先级最高**：享有尊享通道。
* **模型请求额度更高**：RPM 最高 5000。

另外，尊享版也包含旗舰版已有的云设备扩容、自定义域名、免费 SSL、去品牌 Logo 等高级权益。

### 团队版用户无法提交扣子工单？ {#hMwP2Ie89}

团队版用户通过帮助中心提交扣子工单时，如果页面自动跳转至付费墙，可以登录[扣子编程](https://code.coze.cn/)，在页面左下角切换到团队版默认组织，切换后即可正常提交工单。

![Image=258x307](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/57878353f6f94affbd5b239075cd23cb~tplv-goo7wpa0wc-topic.webp)

## 费用相关 {#d5e6d01f}

### 什么是积分？ {#132c667a}

你可以通过消耗积分来使用扣子提供的各项 AI 能力，每日登录扣子即可获得免费积分，购买套餐后可以获得更多积分。积分与现金折算比例为 1000 : 1。关于积分的更多信息，请参考[积分](https://docs.coze.cn/coze_pro_credits)。

### **如何获得积分？** {#0ded2304}

你可以通过如下方式获得积分：

* [购买套餐](https://code.coze.cn/subscription-paywall?dist_channel=33336&dist_code=wd)，每月获得相应积分
* 单独[购买积分](https://docs.coze.cn/coze_pro/credits#0a917c32)，灵活补充积分
* 参与平台官方运营活动，领取免费积分

### **积分不足会怎样？** {#b8035f77}

当积分余额不足时，不同版本的处理方式如下：

* **个人版**：积分为 0 时，服务将暂停。你需要补充积分才能继续使用。
* **企业版**：积分为 0 后，仍可以继续使用，系统将按照 1000:1 （积分:现金）比例自动从现金账户中扣除对应的金额。

### 如何查看积分余额？ {#a6a97121}


1. 在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的左下角，单击**积分**卡片。
2. 在**订阅管理**页面的**积分**区域，查看积分余额。

### 为什么消耗这么多积分？ {#9f7e5d20}

扣子的积分消耗数量和任务的难易程度有关。主要影响因素如下：

* **大语言模型**：解析需求、逻辑规划与决策以及生成最终产物。复杂的任务通常需要更先进、更昂贵的模型来执行。
* **虚拟机**：执行代码、处理文件、进行浏览器自动化等操作。
* **第三方 API**：调用搜索工具、生成图片、生成视频、生成播客等第三方 API 服务。

### 如何查询模型费用？ {#c3d13227}

在与扣子对话过程中，系统是根据扣子任务调用的资源（大语言模型、虚拟机等）与复杂度，综合计算积分消耗，不会单独统计模型费用。更多信息，请参考[扣子任务费用](/coze_pro/coze_task_fee)。

你可以在各个模型厂商官网查看模型单价。目前，扣子针对部分模型版本推出限时折扣活动，活动期间你可以以较低价格使用这些折扣模型。

### 我是企业访客，但是在扣子里看不到企业？ {#b220452a}

扣子暂不支持企业访客使用企业积分，只有企业中的内部成员才能在扣子切换到企业，使用企业积分和扣子对话。

### 如何查看积分消耗明细？ {#9b224bb8}

扣子按照单个 Agent 或项目维度统计积分消耗，不同会话场景会生成不同的消耗记录。

* **与单个 Agent 的对话**：积分消耗以你与该 Agent 的第一个对话主题作为记录名称，生成一条独立记录，后续该 Agent 的积分消耗都汇总在该条记录中。
* **在项目中与多个 Agent 对话**：积分消耗统一记录在该项目名称下，所有成员在项目内的消耗合并计入同一条记录。
* **编程项目**：在扣子中创建的编程项目，积分消耗需在**扣子编程**页签中查看。

查看积分的具体操作如下所示：

::::tabs
@tab PC 端
1. 在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)左下角，单击**积分**卡片。
2. 在**积分消耗**页面的**扣子**页签中，查看月度积分总消耗以及积分消耗明细。
   ![Image=1687x765](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0ac46c4576ab4a4394d2b0b90593c8f4~tplv-goo7wpa0wc-topic.webp)

@tab App 端
在扣子 App 左下角单击**积分**卡片，然后单击**积分**栏，查看各类任务的积分消耗。

1. 在扣子 App 中，单击账户头像。
2. 在**账户信息**页，单击**积分**。
   ![Image=125x254](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1349a8d3343b4ed7bcf0a9cdb7839873~tplv-goo7wpa0wc-topic.webp)
3. 查看月度积分总消耗以及积分消耗明细。
   ![Image=122x243](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5598c1fa79154c5b8801315c8c90c7f9~tplv-goo7wpa0wc-topic.webp)
::::

### 618 有什么活动吗？ {#4a0972bf}

为感谢大家一直以来的支持，扣子将在 618 期间为符合条件的个人付费版套餐用户发放一笔限时活动积分，助力大家在扣子中更高效地调度 Agent、推进项目协作，并在扣子编程中构建和交付更多 AI 应用。详细活动规则可参考[618 限时活动积分发放通知](/guides/618_bonus_points_event)。

### 收到了一笔活动积分？ {#ce124e05}

为感谢大家一直以来的支持，扣子将在 618 期间为符合条件的个人付费版套餐用户发放一笔限时活动积分，助力大家在扣子中更高效地调度 Agent、推进项目协作，并在扣子编程中构建和交付更多 AI 应用。

如果你在[订阅管理](https://www.coze.cn/subscription/manage?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=) > **积分明细**页面看到一笔新增的活动积分到账记录，且注明**618福利积分（仅限订阅状态使用）**，表示这笔积分是 618 活动的赠送积分，有效期 3 个月。每个订阅套餐收到的活动积分数量不同，详细规则可参考[618 限时活动积分发放通知](/guides/618_bonus_points_event)。

## 改版咨询 {#63f0b1f3}

### 为什么手机上找不到专属资讯和每日播客？ {#41368393}

直接和你的扣子 Agent 对话，即可设置**话题追踪**。Agent 会定期搜索某个话题的最新动态，生成文字简报，例如“杭州演唱会”、“AI 行业动态”等。如果你想每天听着了解动态，扣子 Agent 可以把简报内容再做成播客音频推给你。

你可以通过以下指令来添加一个话题追踪。

::::cols
@col 50
你的指令：

```Plain Text
帮我创建一个话题追踪，话题是“AI 行业动态”，简报再做个播客音频发给我。
```

@col 50
话题追踪的效果：
::::

### 可以切回旧版本吗？ {#0eb79e5e}

扣子已全新升级，暂不支持切回旧版本。

扣子 3.0 依然保留旧版的核心能力，支持 AI 创作、AI Office，无论是长文、绘本、动图、海报、播客、网页、视频，还是 PPT、Word、Excel、图表，扣子仍旧可以陪你拆解复杂问题、直接交付产物。

### 我的历史对话在哪里看？ {#613f24e3}

在扣子 3.0 升级之前，你和扣子的每一次不同主题的对话都是独立的，其中包含不同的对话记录和上下，是你和旧版扣子之间已经完成的所有对话记录的集合。这些对话现已被归档，包括历史的网页制作、PPT制作等任务。

在全新的扣子中，你可以在通过以下方式找到这些对话。

::::tabs
@tab 网页端、桌面端
在扣子主页左上角单击**对话** > **已归档对话**。

![Image=397x249](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c5782aaef553411280cc3117abb04d97~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
在扣子 App 首页，选择“历史对话”，即可找到所有已归档的对话。

![Image=260x480](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/64043a50a6034a98ac62d642c356da10~tplv-goo7wpa0wc-topic.webp)
::::

### 扣子编程下线了吗？还能创建工作流吗？ {#2322768b}

扣子编程（code.coze.cn）没有下线，仍是扣子品牌旗下的独立产品。

目前，扣子（coze.cn）已经接入扣子编程的核心能力，你可以直接在扣子中通过自然语言创建网页应用、移动应用、小程序，或导入已有编程项目继续开发、预览和部署。

如果你需要更完整的 AI 编程能力，例如更专业的项目管理、集成配置，或创建智能体、工作流等复杂 AI 产物，仍然可以前往 **扣子编程（code.coze.cn）** 使用。

简单来说：

* 想快速做网页、App、小程序：可以直接在扣子里使用 AI 编程。
* 想创建或管理工作流、智能体等更复杂产物：建议前往扣子编程主站。
* 已有扣子编程项目：可以导入到扣子中继续开发和管理。

### 示例项目消耗积分吗？ {#33d6705c}

示例项目不消耗积分。

为了便于你理解和体验扣子的 AI 编程和视频制作功能，我们为你准备了像素方块世界和完美追捕两个示例项目。

* 主要用于演示功能，项目中已有的对话并未消耗你的积分。
* 如果继续和视频 Agent、编程 Agent 对话，才会产生积分消耗。

![Image=537x272](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ab62ead90b754b52826851386f10ff9d~tplv-goo7wpa0wc-topic.webp)

## 账号相关 {#4a16d666}

### 我有企业版，怎么切换到企业版？ {#3dabd7ee}

企业版用户可在你的个人版和企业版之间随时切换，版本之间的数据和对话都是独立的。以个人版切换到企业版为例，版本切换方式如下：

::::tabs
@tab 网页端、桌面端
在任意页面的左下角单击你的头像，并选择**企业** > **组织**即可。

![Image=448x288](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ec8393bfcddd4cf5b63bf23e26197db4~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
1. 在扣子 App 首页左上角，点击你的头像。
2. 点击切换版本。
3. 选择企业版。
4. 选择一个你所在的组织。
   完成这一步，你就成功切换到了这个企业版账号中。   


![Image=410x235](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6751d7c87d474b378a43a3f4fb6341cf~tplv-goo7wpa0wc-topic.webp)
::::
