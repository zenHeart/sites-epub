> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

Coze CLI 是扣子面向 AI Agent 和开发者提供的命令行工具。它将扣子编程中的项目开发、资源管理和内容生成能力封装为结构化命令，使 Agent 能够根据用户的自然语言指令，在后台完成从创建到交付的完整任务。

## Coze CLI 是什么 {#a5114b5b}

在扣子编程网页端，用户通常通过页面完成项目创建、AI 对话开发、预览、部署和资源配置。Coze CLI 将这些操作转化为 Agent 和自动化程序可以调用的命令接口。用户不必逐项操作页面，只需说明目标，Agent 就可以选择合适的命令并执行任务。

Coze CLI 的包名为 `@coze/cli`。它既可以由开发者在终端中直接使用，也可以集成到支持命令行工具的 Agent 中。对多数用户而言，推荐的使用方式不是记忆命令，而是直接向 Agent 描述需求，由 Agent 通过 Coze CLI 操作扣子。

Coze CLI 与扣子编程使用相同的账号、组织和工作空间体系。通过 CLI 创建的项目、生成的内容和配置的资源会保存在用户授权的扣子账号下，用户可以继续在扣子编程中查看和管理。

## 为什么需要 Coze CLI {#bcdf2a2a}

传统命令行工具主要用于让开发者更高效地操作软件；Coze CLI 则同时面向开发者和 AI Agent。它将一系列可重复、可标准化的产品操作转化为结构化接口，使 Agent 不仅能够理解需求，还能够实际创建项目、修改应用、配置资源并交付结果。

* 对于 Agent 用户，Coze CLI 减少了在不同页面之间切换和逐项配置的成本。创建应用时，用户可以从一句需求开始，让 Agent 持续完成开发、调试、预览和部署；生成图片、语音或视频时，也可以让 Agent 统一组织生成任务并交付产物。
* 对于开发者和企业团队，Coze CLI 提供了更稳定的自动化入口。项目、代码仓库、数据库、环境变量和工作空间等资源可以通过命令统一管理，并使用结构化输出接入脚本、Agent 或其他自动化流程。

## Coze CLI 能做什么 {#9e2a79ce}

Coze CLI 将扣子编程的核心能力开放给 AI Agent。用户只需说明目标，Agent 就可以在后台完成项目开发、问题修复、资源配置和内容生成，并将可预览、可部署或可下载的结果直接交付给用户。

### **一句话开发应用** {#6fb8a1fc}

无需在页面中逐项创建和配置项目。你可以直接告诉 Agent 想做什么，例如创建一个决策助手、活动报名网站或业务数据看板。Agent 会通过 Coze CLI 创建项目，与编程 AI 持续对话，完成代码生成、功能开发和页面设计，并返回在线预览地址。

预览过程中发现问题时，可以继续通过自然语言提出修改要求。Agent 能读取项目上下文和运行结果，定位并修复问题；验收完成后，还可以继续部署生产版本、配置环境变量和自定义域名。对于已有工程，也可以从 GitHub 仓库或本地 ZIP 文件导入，在原有代码基础上继续开发。

::::cols
@col 33
你的指令：

```Plain Text
使用 Coze CLI，做一个好玩又实用的小东西吧，做个决策助手网站
```

@col 33
对话过程：

<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f35b75b21355440eade33fe79b031620~tplv-goo7wpa0wc-image.image" width="1524px" height="1280px" /></div>

@col 33
你的产物：

<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/78b2398cefb44e2184c5b76705c962be~tplv-goo7wpa0wc-image.image" width="1988px" height="1794px" /></div>
::::

### 让 AI 完成调试和工程协作 {#ae01aba5}

应用开发通常需要多轮修改，而不是一次生成。Coze CLI 支持 Agent 将项目代码、需求文档和错误日志作为上下文发送给编程 AI，并持续跟踪开发任务。遇到部署失败时，Agent 可以查询部署状态和日志，调用 AI 分析失败原因并尝试修复。

对于更完整的工程流程，Agent 还可以管理远程代码仓库、云数据库、模型、工具、Skill 和环境变量。这样，Coze CLI 不仅适合从零生成应用，也可以进入已有项目的日常开发和协作流程。

::::cols
@col 33
你的指令：

```Plain Text
换个风格，换成活泼可爱的
```

@col 33
对话过程：

![Image=1558x1532](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9a2a70b356384442a4053f75d7323891~tplv-goo7wpa0wc-topic.webp)

@col 33
你的产物：

<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/344f18c145a240be8e60b88f7a4550cc~tplv-goo7wpa0wc-image.image" width="2820px" height="1652px" /></div>
::::

在遇到运行错误时，AI 会自动读取 CLI 的后台运行日志，精准定位报错位置、分析执行链路，并自动修复问题。

简单来说，当你在度假时忽然收到线上报错，你甚至不需要打开电脑，随手跟 Agent 说一句就行。它会自己去看报错日志，找出是哪里卡住了，然后自己修改错误、重新测试，直到帮你把整个流程彻彻底底地跑通。

::::cols
@col 33
你的指令：

```Plain Text
“决策助手”这个项目，抛硬币这里有点问题，图片是正面，文字提示是反面，帮我修复一下
```

@col 33
对话过程：

<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/414211d437794d1aa05168978987fc97~tplv-goo7wpa0wc-image.image" width="1490px" height="790px" /></div>

@col 33
修复结果：

<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c4bd75ee12b64f7f9a86d986f4e2543d~tplv-goo7wpa0wc-image.image" width="2896px" height="1662px" /></div>
::::

### 一站式内容创作 {#65266f45}

Coze CLI 可以调用扣子提供的内容生成能力，完成图片、语音和视频创作。例如，用户可以让 Agent 根据一份产品资料批量生成宣传图片、产品配音和营销短片。Agent 会提交生成任务、跟踪状态，并在任务完成后取得最终产物。

生成结果和本地文件还可以上传为在线可访问资源，便于用户直接预览、下载或继续用于应用开发。整个过程可以在同一次对话中完成，无需用户在多个创作工具和存储服务之间切换。

例如直接对话，就能生成小红书高密度风格信息图、生成视频、音频：

::::cols
@col 42
对话过程：

<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/46c10544fb2b4cb7a364255bd9f50a88~tplv-goo7wpa0wc-image.image" width="1380px" height="874px" /></div>

生成的信息图：

<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7e854d66cb8c40259ba4063a202e76d1~tplv-goo7wpa0wc-image.image" width="1280px" height="450px" /></div>

@col 56
生成的视频：

<Player class="topic-video-player"  class="topic-video-player"  class="topic-video-player"  class="topic-video-player"  class="topic-video-player"  class="topic-video-player"  src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9b5d5a40a8a74dbd831b65adb5e13772~tplv-goo7wpa0wc-image.image"></Player>
::::

### 云端存储产物 {#8f4f2ea9}

之前用过 Openclaw 的朋友可能都遇到过一个痛点：Agent 明明生成了文件，但给出的链接却经常无法打开。这其实是因为文件只存在于 Agent 的虚拟沙盒里，缺乏公共的对象存储能力。

现在通过 扣子编程 CLI 接口，Agent 可以直接把生成的内容上传到云端，可以理解为给 Agent装上了一个“自动同步云盘”，这样你最终收到的，就是一个能直接点击预览、随时下载的公网链接，让文件获取更轻松！

## 核心能力 {#9ba212ca}

:::tip 说明
关于 Coze CLI 的命令行及详细参数说明，可参考 [Coze CLI 文档](https://www.npmjs.com/package/@coze/cli)。
:::

当前 Coze CLI 的核心能力可以归纳为六个模块。

<!-- @cols-width: 130,160,494 -->
| 能力模块  | 核心能力  | 能力说明  |
| --- | --- | --- |
| **账号与空间**  | 账号认证  | 登录扣子账号、检查登录状态、退出登录及管理授权凭据。  |
|^^| 资源上下文  | 查看和切换个人版、企业组织及工作空间，确定资源的创建和操作位置。  |
| **AI 编程**  | 项目全生命周期  | 通过自然语言创建、查询、筛选、导入和删除 Web、App、小程序、Agent、工作流、Skill 等项目。  |
|^^| 对话式开发  | 持续发送需求，让 AI 开发、修改和调试项目；支持使用本地文件、需求文档和日志补充上下文。  |
|^^| 任务与版本管理  | 同步或异步执行开发任务，查询和取消任务，并查看对话历史。  |
|^^| 预览与发布  | 获取在线预览、部署生产版本、查询部署历史，并使用 AI 辅助分析和修复部署问题。  |
| **项目资源**  | 运行配置  | 管理环境变量、自定义域名、数据库表同步和发布渠道等运行配置。  |
|^^| AI 能力配置  | 为项目选择模型，启用或停用工具，并挂载、上传或移除 Skill。  |
| **代码与数据**  | 代码仓库  | 完成 Git 平台授权、导入项目、创建和绑定远程仓库，以及推送、拉取和同步状态检查。  |
|^^| 云数据库  | 创建和管理数据库、执行 SQL、生成类型、导出数据，并在必要时执行时间点回滚。  |
| **多模态内容**  | 多媒体生成  | 生成图片、语音和视频，并根据不同任务配置尺寸、音色、时长或参考素材。  |
|^^| 任务与产物交付  | 跟踪生成任务、获取最终结果，并将本地文件上传为在线可访问资源。  |
| **Agent 自动化**  | 结构化调用  | 使用 JSON、事件流和异步任务模式，便于 Agent 与自动化程序稳定调用。  |
|^^| 会话与长任务  | 创建和复用 Session，监听回复、恢复长任务，并处理文件、PPT 和播客等产物。  |
|^^| Agent 协作  | 支持 Agent 之间进行任务委派、状态跟踪和结果回传。  |
|^^| CLI 扩展与维护  | 管理配置和插件，升级 CLI，并将配套 Skill 同步到支持的 AI 工具。  |

不同项目类型、账号版本和组织权限下，可用能力可能存在差异。具体命令及参数以当前安装版本的命令帮助和 npm 包说明为准。

## 如何使用 Coze CLI {#7f3192c5}

### 在扣子中使用 {#50c2dc00}

扣子已集成 Coze CLI。用户可以直接在对话中描述需求，例如创建网站、修改已有项目或生成多媒体内容。扣子会根据任务选择相应能力，无需用户自行安装和执行命令。

::::cols
@col 33
你的指令：

```Plain Text
帮我用 Coze CLI 创建一个网页应用，介绍  Coze CLI  的功能及使用方式 
```

@col 33
对话过程：

![Image=1550x1216](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f1392254331b4b698f21cd906f3656d5~tplv-goo7wpa0wc-topic.webp)

@col 33
预览作品：

<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/17b21c78a4694c2b8f457dff204da649~tplv-goo7wpa0wc-image.image" width="2238px" height="1480px" /></div>
::::

### 在其他 Agent 中使用 {#9caf8063}

如果希望在 TRAE、Claude Code、Codex 等支持命令行工具的 AI Agent 中通过自然语言使用 Coze CLI，需要先安装 CLI：

1. 安装 Coze CLI。
   复制以下信息，并发送给你的 AI Agent，立即完成安装。
   ```Plain Text
   帮我安装 Coze CLI 和相关的技能
   npm install -g @coze/cli --foreground-scripts
   coze self skill install
   ```
2. 安装成功后，重启 Trae 等 Agent 的客户端，使技能生效。
3. 登录你的扣子账号。
   复制以下信息，并发送给你的 AI Agent。Agent 会自动生成授权链接，你需要按照页面提示完成账号授权。
   ```Plain Text
   帮我登录扣子账号 
   coze auth login --oauth
   ```
3. 发起第一个任务。
   复制以下信息，并发送给你的 AI Agent。通过简单对话，快速生成并部署一个网页应用。
   ```Plain Text
   帮我用 Coze CLI 创建一个网页应用，介绍  Coze CLI  的功能及使用方式 
   创建完成后，请将预览链接发给我
   ```   


### 在终端中安装并使用 {#hoyz0IoPg}


1. 在终端中执行以下命令安装 Coze CLI。
   ```Shell
   npm install -g @coze/cli --foreground-scripts
   ```
   ![Image=437x285](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/638940cae35147b9a5c06f5a6e947e2b~tplv-goo7wpa0wc-topic.webp)
2. 执行以下命令安装 Coze CLI 相关的技能。
   安装 CLI 时不会自动安装配套技能。继续执行以下命令，回显信息中会提示你选择需要使用 Coze CLI 的 AI Agent。选择 Agent 并不是为 Coze CLI 分配使用权限，而是为对应 Agent 安装配套 Skill，使其能够识别相关需求，并按照正确流程调用 Coze CLI。除非你明确要求，未安装配套 Skill 的 Agent 通常不会主动调用 Coze CLI。
   1. 执行以下命令，安装技能。
      ```Shell
      coze self skill install
      ```
      如果在脚本或 JSON 模式中执行，需要通过 `--target` 明确指定目标。例如，将 Skill 安装到 Trae：
      ```Bash
      coze self skill install --target trae
      ```
   2. 选择需要安装配套 Skill 的 Agent，支持多选。
      ![Image=369x240](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5ebb207b3a9043b3993d63a06006a5b8~tplv-goo7wpa0wc-topic.webp)
   3. 选择 Agent 并安装技能后，重启终端使技能生效。
3. 登录你的扣子账号。
   执行以下命令，根据回显信息提示完成扣子账号授权。
   ```Plain Text
   coze auth login --oauth
   ```   


## 下一步 {#hBbLXA6cS}

接下来，你可以通过以下教程，在实际任务中使用 Coze CLI。可以按顺序阅读，也可以直接选择与你当前目标对应的教程：

* [Coze CLI：账号登录与授权](/developer_guides_coze_cli_quickstart)
* [Coze CLI：10 分钟开发并上线 Web 应用](/coze-cli-develop-and-deploy-a-web-application)
* [Coze CLI：导入已有项目并通过 AI 持续开发](/coze-cli-import-existing-project)
* [Coze CLI：构建带数据库的 AI 应用](/coze-cli-build-ai-app-with-database)
* [Coze CLI：批量生成营销内容](/coze-cli-batch-generate-marketing-content)
* [Coze CLI：管理企业团队资源](/coze-cli-manage-team-resources)

如需查询完整命令、选项和参数，请参考 [@coze/cli npm 包说明](https://www.npmjs.com/package/@coze/cli)。Coze CLI 仍在持续迭代，实际能力以当前安装版本的 `coze --help` 和对应子命令帮助为准。
