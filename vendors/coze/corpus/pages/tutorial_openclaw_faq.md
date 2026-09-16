> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

## 了解概念 {#f7beb68c}

### 什么是 OpenClaw，它能做什么？ {#33efbf3a}

[OpenClaw](https://openclaw.ai/)**（原 Moltbot、Clawdbot）** 是一款开源的个人 AI 助理和智能代理系统，可运行在个人电脑或服务器上。和传统的 AI 助理不同，OpenClaw 不是普通的聊天机器人，被授予操作权限之后，它能控制你的终端执行操作，可以“动手工作”，而不是“只出主意”。你可以通过飞书等即时通信工具与它对话交互，让它帮你完成各类任务，例如生成图文、处理邮件、管理日程等。

OpenClaw 的典型使用场景非常广泛，以下是用户最常用的方向：

::::cols
@col 50
**办公自动化**

* 通过飞书让 AI 帮你写文档
* 读飞书多维表格、管理日程
* 创建飞书任务、自动发飞书消息

**联网调研**

* 使用内置联网搜索 Skill
* 自动爬取新闻、调研竞品
* 整理简报并推送到 IM 渠道

**内容创作**

* 生成信息图
* 撰写公众号文章
* 制作演示文稿

@col 50
**文件管理**

* 整理本地/云端文件
* 生成文档摘要
* 批量处理数据

**定时任务**

* 定时新闻推送、周报生成
* 数据监控等自动化流程

**AI 社交**

* 通过 InStreet 让你的 AI 助手
* 在 Agent 社区中发帖、互动、学习
::::

### 在扣子编程部署 OpenClaw 都有哪些优势？ {#5ba337bd}

* **操作简单便捷：**
   * 一键配置：提供隔离的云主机环境、可视化的模型和版本配置，自然语言方式修改配置文件，无需手动开通和切换模型。
   * 一键修复：提供 AI 编程助手，无需下载编程 IDE、无需开放本地文件权限，编程助手可以在隔离的云主机环境中帮你完成部署与配置；支持自然语言对话式修改项目配置、修复问题，初学者也可直接上手。
* **开放的 IM 生态**：
   * 一键打通飞书：一键单击即可创建机器人并完成权限和长连接等配置，无需手动的复杂操作。
   * 生态开放：支持便捷打通企业微信、钉钉等各类 IM 工具，无功能裁剪与限制。
* **丰富的技能和工具：**
   * 技能：内置海量热门技能，支持便捷订阅安装扣子生态的各种公开技能和企业内部技能，增强助手能力。
   * 工具：内置浏览器等常见工具，即使在云主机环境中也可无障碍访问各类网站。
* **提供低成本配置方案**：支持满血版和省流版两大方案，满血版无损体验高性能、省流版通过降低心跳间隔等配置优化来节省 Token 成本，满足不同场景诉求。
* **稳定安全**：隔离的云主机环境，不用担心删掉主力工作设备的本地资源；完善的云端安全防护能力，保障敏感文件和数据的信息安全和存储安全。

### OpenClaw 项目里，扣子 AI 能做什么？ {#85225568}

在 OpenClaw 项目中，扣子 AI 是你的全局助理，通过编辑 OpenClaw 项目的代码文件来控制其配置。

![Image=653x349](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1eb38225a1d3492da89998aedd769d23~tplv-goo7wpa0wc-image.image)

在页面左侧和扣子 AI 对话，你可以：

* 安装各种 OpenClaw 插件和依赖，例如钉钉集成等。
* 修改 OpenClaw 项目的配置信息，例如飞书集成配置、心跳（heartbeat）和记忆（memory）系统等等。
* OpenClaw 项目故障排查，例如对话无响应、网关中断等问题。

遇到 OpenClaw 项目的任何问题，都可以和扣子 AI 对话来尝试解决。

### 扣子编程中的 OpenClaw 能否控制本地电脑？ {#9e629932}

**不支持。** 无论是扣子编程的 OpenClaw 运行在云端网络环境中，与本地电脑网络相互隔离，无法直接跨网络控制本地桌面应用程序。

### 部署完的界面是干什么的？ {#3238ee34}

部署完成后，你看到的这个界面，就是龙虾的总控制台。

你可以在这里**直接跟龙虾对话**、**管理各个平台的连接**、**查看和调整任务**、**管理定时任务**、**管理技能和配置**，还能**查看运行日志、排查问题、更新版本**，所有操作都是可视化操作。

![Image=515x255](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/80bdcd47902a4e0d89e881f32b4cf6bc~tplv-goo7wpa0wc-image.image)

### 龙虾和豆包这些智能体有什么本质区别？ {#34644ac9}

简单来说，豆包是“云端的百科全书”，而龙虾是“你的电子员工”。

* 豆包：像个博学的朋友，擅长回答、创作、思考、聊天，给你思路和内容。
* 龙虾：是一个住在你电脑里、24 小时待命的私人助手。它能记住你的工作习惯，复用过往方法，自主学习迭代，即便你休息，也能默默帮你完成各类重复任务。

### 龙虾能为我做什么？ {#009a6fbe}

规则明确、流程固定、重复又费时间的活可以交给龙虾，例如：

* 文件大管家：文件夹乱糟糟？给它个规则，让它自动分类、改名或清理。
* 简历初筛：100 份简历，让按硬性指标（如学历、年限）先筛一遍，并写好拒信，你只需看剩下的 10 份。
* 工作汇报：把它拉进飞书群，自动抓取聊天记录，按你的要求生成复盘总结。
* 动态监测：盯着某个网页或文件夹，一旦竞品调价了、文件更新了，它立刻去抓取信息并通知你。

### 我完全不懂编程、不会敲代码，能不能玩转龙虾？ {#c572c702}

在扣子编程养虾过程中，遇到任何问题（配置、报错等等），都可以在扣子编程中发起对话，让编程 AI 帮你查看并解决。你用大白话描述问题，它能在后台帮你修代码。

![Image=504x294](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/dcce553220f64feeae600bd26fc77216~tplv-goo7wpa0wc-image.image)

### 如何一键为龙虾开通全部飞书权限？ {#0cad4f8b}

当你在飞书中与龙虾对话时，你只要输入指令`获得全部飞书权限`，即能收到所有权限授权卡片，单击**前往授权**，就能一次性开通所有飞书权限。

**为了隐私安全，更推荐**按需授权，等龙虾干活需要权限时，它会自动找你申请权限。

![Image=516x341](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8836036fd491430a87671662bcca8cde~tplv-goo7wpa0wc-image.image)

### 扣子编程 OpenClaw 运行在哪里？ {#hVndFaK7B}

扣子编程 OpenClaw 项目运行在系统自动分配的**云电脑**中。云电脑是扣子编程为 OpenClaw 项目提供的隔离运行环境，与用户的本地设备相互隔离。OpenClaw 在云电脑中使用浏览器、终端和文件系统等工具完成任务，不会直接操作你的本地电脑，因此不用担心误删或修改本地资源。扣子编程也提供云端安全防护能力，保障敏感文件和数据的信息安全与存储安全。

需要注意的是：

* 扣子编程 OpenClaw 项目的云电脑由系统自动创建，不支持用户手动选择规格，采用默认设备规格，**每天消耗约 800 积分**。更多计费说明，请参考[云设备费用](https://docs.coze.cn/coze_pro_cloud_device_fee)。
* 扣子编程 OpenClaw 项目 OpenClaw 依赖云电脑运行。关闭云电脑后，OpenClaw 项目将不可用，但不会停止计费。

## 使用方法 {#b1d73896}

### 如何修改 OpenClaw 内置的模型？ {#fc9acc86}

* 使用扣子提供的模型：
   在 **OpenClaw 配置**页面，直接使用扣子编程提供的豆包 2.0 等热门模型，无需额外开通其他厂商的模型服务。   


::::cols
@col 50
打开 OpenClaw 配置页面：

![Image=344x254](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e5f0a3e9755245e28881b9ba72bc4858~tplv-goo7wpa0wc-image.image)

@col 50
选择模型：

![Image=315x246](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ef4ad6235b1a4519b94e41dd245ae242~tplv-goo7wpa0wc-image.image)
::::

* 使用方舟或其他模型厂商提供的模型 API：
   将以下内容发送给扣子 AI，注意替换模型名称、base url 和 API key。   


::::cols
@col 50
```Shell
帮我切换成火山方舟 coding plan 的 GLM 4.7 模型，模型详细信息如下：
model name：glm-4.7
Base URL：https://ark.cn-beijing.volces.com/api/coding/v3
API Key：你的API Key
```

@col 50
![Image=210x256](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c89ff08c2cea44fd801cd2386c7945a7~tplv-goo7wpa0wc-image.image)
::::

### 积分消耗太快了怎么办？ {#69cea715}

扣子编程 OpenClaw 的积分消耗通常来源于模型调用，即主要是模型 Token 费用。由于 OpenClaw 的上下文机制，Token 消耗过快一直是 OpenClaw 用户的普遍痛点。以下是经过社区验证的省钱策略：

* **策略一：选择省流版**。扣子编程版提供"满血版"和"省流版"。省流版修改了部分默认配置，例如心跳间隔时间、上下文策略等，Token 消耗更低。此方案更适合新手用户。
   ![Image=264x202](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3e1141711d9e44679ee355eb5aa72ad0~tplv-goo7wpa0wc-image.image)
* **策略二：安装成本优化 Skill**。可以尝试 OpenClaw 社区的 [OpenClaw Token Optimizer](https://clawhub.ai/Asif2BD/openclaw-token-optimizer)，核心逻辑是简单任务自动分配给低价模型，复杂任务才调用高价模型。
   ```Plain Text
   帮我安装一下这个 skill https://clawhub.ai/Asif2BD/openclaw-token-optimizer
   ```
* **策略三**：**使用火山方舟 Coding Plan**。你的 OpenClaw 项目默认使用扣子提供的模型，每次对话都会消耗积分；你可以将模型切换成方舟的 Coding plan，套餐有效期内可以在一定限额下使用各类模型 API。此方案更适合中高频使用 OpenClaw 的开发者用户。切换为 Coding Plan 的方式可参考[切换模型](/tutorial/openclaw#1d491b08)。

### 如何为 OpenClaw 安装技能（Skill）？ {#1e9f666d}

OpenClaw 的技能（Skills）是其核心功能扩展机制，通过安装不同技能，OpenClaw 可完成各种任务。在扣子编程的 OpenClaw 中，你可以通过以下方式安装技能：

::::cols
@col 33
**方式一：URL 方式安装**

将 GitHub 中的 Skill 链接发送给 OpenClaw，它会自动完成安装。例如：

```Plain Text
帮我安装这个 Skill：https://github.com/xxx/xxx-skill
```

@col 33
**方式二：上传 Zip 包**

适用于网络受限场景，例如 OpenClaw 访问 GitHub 可能受限。

1. 在本地电脑上将 Skill 文件下载为 zip 压缩包。
2. 在 OpenClaw 对话框中上传该压缩包。
3. 让 OpenClaw 帮你自行解压安装。

@col 33
**方式三：去扣子生态寻找 Skill**

[Instreet](https://instreet.coze.site/) 和[虾评](https://xiaping.coze.site/)是扣子专为 Agent 打造的社区，你可以在这里找到各种技能。

例如：

```Plain Text
去 Instreet 上看看有没有什么技能适合你。
```

或者：

```Plain Text
安装一下这个技能 https://xiaping.coze.site/skill/731e9e25-2246-49a7-a171-ef5b450a906b
```
::::

### 如何加强记忆？ {#56950f8d}

OpenClaw 通过记忆分层机制，会将对话中的重要内容分别保存为长期记忆（`MEMORY.md`）和每日记忆 （`memory/YYYY-MM-DD.md`），并在每次对话前都加载这些记忆以实现更为拟人的对话效果。扣子也为你的 OpenClaw 项目额外加装了 Embedding 模型，可以帮助 OpenClaw 在回答你的问题时能通过向量检索的方式找到更相关的答案。

如果你仍然发现 OpenClaw 记忆能力不足，可以尝试以下方式增强记忆：

* **强调记录重要信息**：对于 OpenClaw 必须记住的信息，对话时重点强调，OpenClaw 会将你强调过的重点信息记录在长期记忆中。例如：
   ```Plain Text
   我发送"todo：xxx"时自动帮我创建一个飞书待办，一定要记住这个规则。
   ```
* **手动检查记忆**：定期要求 OpenClaw 打印长期记忆和每日记忆给你检查，确保记忆内容正确。如果发现记忆缺失，可以通过对话让 OpenClaw 修改、补齐。例如：
   ```Plain Text
   帮我打印长期记忆和今天的每日记忆文件
   
   请把之前散落在不同会话里的xx相关记忆整理出来，合并成一条，并写入我的 MEMORY.md。
   ```
* **定时总结记忆**：创建一个定时任务，让 OpenClaw 自行总结记忆，可以将概要记录在每日记忆，再提取关键信息记录在长期记忆文件中。例如：
   ```Plain Text
   每天晚上九点，回顾我们当天的所有对话内容，总结后记录在每日记忆里，账密、规则等重要信息记录在我的 MEMORY.md里
   ```   


### 如何取消部署？ {#13f297f9}

OpenClaw 项目默认为部署状态，沙箱环境将持续保活，你可以随时和 OpenClaw AI 助理对话。

如果不再需要和 OpenClaw 个人助手对话，你可以随时在项目页面中取消部署。取消部署不会立即释放沙箱环境，你仍然有可能继续对话一段时间，直到沙箱环境被回收。

在扣子编程中打开 OpenClaw 项目页面，在页面右上角单击红色图标，取消部署 OpenClaw 项目。

![Image=417x347](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e143566de31a44ad8a0d6294b294aa74~tplv-goo7wpa0wc-image.image)

### 如何找到我的 OpenClaw 龙虾项目？ {#ca5ca82e}

* **在飞书找到你的龙虾**：
   在飞书客户端的搜索框中输入龙虾的名字，就可以找到你的龙虾。
* **在扣子编程找到你的龙虾**：
   要在扣子编程找到你的龙虾配置页面，可以参考以下步骤：
   1. 登录[扣子编程](https://code.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   1. 在左侧菜单中单击**项目管理**。
   1. 筛选**项目类型**为**个人助理**。
   1. 在筛选结果中找到你的龙虾，单击进入龙虾配置页面。

::::cols
@col 50
在扣子编程找到龙虾

![Image=332x187](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e634b8f1c51345a8a6d7936c4ce23b84~tplv-goo7wpa0wc-image.image)

@col 50
龙虾配置页面

![Image=340x168](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/919fd157179b4203b68b61934cae978a~tplv-goo7wpa0wc-image.image)
::::

## 飞书相关 {#0e3cb6bd}

### 如何让 OpenClaw 读取飞书文档、多维表格、给我发图片？ {#83d64919}

3 月 5 日之前在扣子编程部署的 OpenClaw 项目，默认使用 OpenClaw 内置的飞书插件，不具备读取飞书文档和多维表格、发送图片的权限。如果你希望使用这些高级能力，可以手动安装**飞书官方**发布的 OpenClaw 飞书插件，操作步骤[安装和更新飞书官方插件](/tutorial/openclaw#96992dac)。

安装成功之后，将飞书文档和多维表格链接发送给你的 OpenClaw 飞书机器人，它就可以读取内容帮你分析。

### 如何切换授权的飞书账号？ {#8c3b1a9c}

扣子编程默认为你已授权的飞书账号下创建机器人应用，如需在其他账号下创建，你可以在 OpenClaw 配置页面取消授权再重新授权。

1. 打开 OpenClaw 配置页面。
   你可以在 OpenClaw 页面右上角单击配置图标，进入 OpenClaw 配置页面。
2. 在渠道配置区域，单击**取消授权**。
3. 单击授权，并根据页面提示登录飞书账号，完成授权。

::::cols
@col 25
> 打开配置页面

![Image=407x300](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e5f0a3e9755245e28881b9ba72bc4858~tplv-goo7wpa0wc-image.image)

@col 25
> 取消授权

![Image=994x886](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/479636d16e9240c098a26f00796fff4a~tplv-goo7wpa0wc-image.image)

@col 25
> 重新授权

![Image=968x897](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c25b708570634a21ab7b5c5ad116e1dc~tplv-goo7wpa0wc-image.image)

@col 25
> 完成授权

![Image=1330x1149](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b0b537b1cd7f4059ba32692b4af0e489~tplv-goo7wpa0wc-image.image)
::::

### 为什么我的飞书机器人和 OpenClaw 的连接总是中断 {#0d48227b}

对于部分企业组织，通常原因是未开启**刷新 user_access_token** 开关。开启方式如下：

1. 登录[飞书开放平台](https://open.larkoffice.com/app?lang=zh-CN)。
2. 在左侧目录树选择**安全配置**，开启**刷新 user_access_token** 开关。
   :::tip 说明
   安全配置页面若无此配置，说明企业默认开启了**刷新 user_access_token** 开关，可跳过此步骤。
   :::   


![Image=402x201](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1a05610ad8d5425ca2984df83748a884~tplv-goo7wpa0wc-image.image)

3. 创建机器人版本并发布。
   1. 单击顶部的**创建版本**按钮。
   2. 单击顶部的创建版本按钮。
      ![Image=640x115](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/98a9c1c27ebb40628d5b1025aeae9f93~tplv-goo7wpa0wc-image.image)
   3. 按需配置应用版本号、默认能力及更新说明等信息。
   4. 详细配置说明可参考[飞书开放平台文档](https://open.larkoffice.com/document/best-practices/intro-to-custom-app-review)。
   5. 单击页面底部的**保存**按钮，创建版本，并根据页面提示发布应用。
      ![Image=508x231](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d9b58a0712934c7499964812a8419d3f~tplv-goo7wpa0wc-image.image)      


### 为什么 OpenClaw 创建的飞书文档，我没有操作权限？ {#2a4b850a}

参考[安装和更新飞书官方插件](/tutorial/openclaw#96992dac)，将你的插件升级到飞书的官方插件，可以解决这个问题。

早期的 OpenClaw 版本默认使用社区版本的飞书插件，OpenClaw 会使用自己的身份创建文档，因此你没有操作权限，OpenClaw 也无法为你授权。目前飞书官方推出的 OpenClaw 插件已解决了此问题，OpenClaw 会默认使用你的身份创建飞书文档、飞书多维表格等，所以你会拥有文档的管理权限。

## 微信相关 {#c5af7890}

### 为什么微信是最新版本，扫码还是报错？ {#a13ae4c6}

可能是因为微信客户端的缓存问题，如果升级微信到最新版本之后仍然报错提示升级版本，可以重启微信，或者清掉后台进程之后重新扫码。

### 微信中搜索不到机器人？ {#f5f36ac4}

由于微信客户端限制，搜索机器人的默认名称 **微信 ClawdBot** 可能搜索不到你的机器人。只能在对话列表中滑动搜索。

建议为机器人设置头像和备注，方便检索。

在机器人对话页面右上角单击设置图标，并在机器人详情页右上角展开隐藏菜单，单击**备注名**区域，根据页面提示输入机器人名称即可。

::::cols
@col 33
![Image=100x216](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/21eac3edf92d4c4ea8d273988d1512c1~tplv-goo7wpa0wc-image.image)

@col 33
![Image=98x212](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/477d8a00c89841b994a7e5946bc8e021~tplv-goo7wpa0wc-image.image)

@col 33
![Image=99x214](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/79e445c91145492eb3baa2f429cf3f9f~tplv-goo7wpa0wc-image.image)
::::

### 为什么电脑、网页等微信客户端看不到 OpenClaw 对话？ {#d7540fac}

由于微信的限制，目前仅微信手机客户端支持连接 OpenClaw。

### 已经配置过渠道，还能添加其他渠道吗？ {#03820834}

可以，同一个 OpenClaw 项目可以绑定多个渠道，每个渠道的 Agent 享有共同的人设和记忆。

例如已经配置过飞书渠道，需要配置微信渠道，可以直接打开 **OpenClaw 配置**页面，找到**微信**区域，并单击**去创建**。详细操作步骤可参考[步骤二：配置微信渠道](/tutorial/openclaw_wechat#6d348026)。

![Image=459x237](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b395aefd4a89483c84383794db8cc81c~tplv-goo7wpa0wc-image.image)

## 故障修复 {#197f10c5}

### 界面一直显示“预览中”怎么办？ {#bf5bddb0}

建议根据以下顺序排查：

1. 右上角首先尝试**重启**。
2. 在左侧扣子 AI 对话区域，发送`“确认网关状态并进行修复”`。此时扣子 AI 会自动检查 OpenClaw 项目状态，并尝试修复。
3. 可能是原因磁盘容量过高导致预览页面卡顿，可以尝试让扣子 AI 帮忙定位和删除部分不必要的文件。

### OpenClaw 不回应飞书消息怎么办？ {#57e2ff5c}

需要判断是 **OpenClaw 服务端**的问题，还是**飞书机器人**的问题。

* 排查 **OpenClaw 服务端**问题：
   * 观察飞书侧发送的消息是否传到了 OpenClaw 项目，如果 OpenClaw 收到了消息，则需要检查扣子编程和飞书渠道之间的连通性。
   * 在左侧扣子 AI 对话区域，发送`“确认网关状态并进行修复”`。此时扣子 AI 会自动检查 OpenClaw 项目状态，并尝试修复。
   * 在扣子编程的 OpenClaw 对话框中发送消息，看是否正常回复。如果 OpenClaw 本身也不回复，可以定位问题在 OpenClaw 服务端。
* 排查**飞书侧**问题：
   * 确认是否已经更新到最新版本官方插件。
   * 检查权限是否已全部申请并通过审核。
   * 检查事件订阅是否已启用长连接并勾选了「接收消息」事件。
   * 确认连接方式选择的是「长连接」模式。
   * 检查飞书应用是否已发布最新版本。

### OpenClaw 对话中断或无响应？ {#87497c22}

可能原因是沙箱连接超时，资源已被回收。你可以重新打开或刷新扣子编程的 OpenClaw 项目页面，系统会自动重连、恢复对话。

扣子编程建议你部署 OpenClaw，以实现沙箱环境持续保活，部署后可以随时和 OpenClaw 对话。

对话提示"401 Unauthorized"或模型调用失败

如果使用阿里云百炼等第三方模型服务，可能会出现类似问题，常见原因及解决方案如下：

<!-- @cols-width: 244,581 -->
| | | \
|**常见原因** |**解决方案** |
|---|---|
|API Key 错误 |检查填写的 API Key 是否正确，注意区分不同服务商的 API Key 格式。 |
|地域不匹配 |如果使用阿里云百炼等第三方模型服务，需确认 API Key 对应的地域与 Base URL 是否匹配。 |
|模型额度耗尽 |登录对应模型服务商控制台，检查免费额度是否用完、账户是否欠费。 |
|Coding Plan 限流 |Coding Plan 存在每 5 小时、每周、每月的请求限额，超出后需等待额度恢复或升级套餐。 |

### 部署 OpenClaw 报错“该工作空间的所有者未开通对应套餐” {#d680e65e}

* **问题现象**：在扣子编程首页单击“立即领取”时，页面报错“该工作空间的所有者未开通对应套餐，请切换至其他工作空间后再进行尝试”。
* **问题原因**：某个工作空间中能否部署 OpenClaw 项目，取决于工作空间所有者的套餐版本。当前所在的**工作空间所有者**未购买个人高阶版、个人旗舰版、企业标准版或企业旗舰版，不具备部署 OpenClaw 的高级权益。
   例如你已经是个人高阶版以上的套餐类型，但试图在个人免费版用户创建的工作空间中部署 OpenClaw，此时无法部署 OpenClaw。
* **解决方案**：
   切换到其他工作空间，并确保工作空间的所有者已购买个人高阶版以上的套餐。   


::::cols
@col 50
**个人版用户切换工作空间：**

在页面左下角单击用户名称，找到个人账号，并选择工作空间。

![Image=281x377](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/377e952586ec42fe96e21f02debb7576~tplv-goo7wpa0wc-image.image)

@col 50
**企业版用户切换到企业空间：**

1. 在页面左下角单击用户名称，找到企业版账号，并选择组织。
   ![Image=225x199](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e61717b9c26f40f18a3a74baf649a95a~tplv-goo7wpa0wc-image.image)
2. 进入组织之后，在页面左上角单击工作空间名称，找到要创建 OpenClaw 项目的工作空间。
   ![Image=178x231](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f7386623d4724fa4aeb65884fd7cbff8~tplv-goo7wpa0wc-image.image)
::::

### 升级 OpenClaw 版本后出现问题 {#518879ff}

扣子编程暂不建议升级 OpenClaw 3.22 版本，已经升级版本的用户可以回滚到 3.13 版本。

![Image=379x84](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/085ac47896424207b0cd35c953d92341~tplv-goo7wpa0wc-image.image)

* **原因**：目前 OpenClaw 官方更新了最新版本 3.23，如果你的使用界面右上角显示了更新提示（Update available: v2026.3.22、v2026.3.23），目前建议暂时不要升级该 3.22 版本或 3.23 版本，该版本和飞书、微信插件有不兼容的情况，建议等后续进一步优化后再升级 OpenClaw 版本。
* **回滚方式**：如果你已经升级到 3.22/3.23 版本，可以通过和扣子编程 AI 对话进行回滚，发送下方指令：
   ```Plain Text
   openclaw update --tag 2026.3.13 --yes
   ```
   ![Image=350x189](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/efd823c1290348ec991fac0a4b65e57d~tplv-goo7wpa0wc-image.image)   


### 安装 Skill 时报"Skill not found"怎么办？ {#ffdbcd41}

常见原因及方案如下：

* **Skill 已改名**：社区 Skill 更新频繁，部分 Skill 可能已更名。例如 `proactive-agent-1-2-4` 已更名为 `proactive-agent`。建议在 ClawHub 官方平台确认最新的 Skill 名称。
* **URL 不可访问**：在扣子编程环境下，某些 GitHub 链接可能因网络限制或API限流无法直接访问。此时可采用「中转源安装」方式，先将文件下载到本地，再上传给 OpenClaw 安装。

### Web UI 页面提示警告符号 {#ebb7ed96}

如果你在 OpenClaw 项目页面打开 OpenClaw 的 WebUI 页面，看到一个警告符号，这是 OpenClaw 的版本过低提示。例如下图：

![Image=473x239](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/dae1a7a40f8f48768c18c437220f2783~tplv-goo7wpa0wc-image.image)

这是因为你安装的 OpenClaw 版本过低，扣子建议你升级到某个稳定的版本，例如 3.13。参考以下步骤升级版本：

1. 登录[扣子编程](https://code.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
2. 在左侧菜单中单击**项目管理**。
3. 筛选**项目类型**为**个人助理**。
4. 在筛选结果中找到你的 OpenClaw 项目。

::::cols
@col 50
在扣子编程找到龙虾

![Image=2780x1564](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/38fa2f5a382045b8a64e7451353305db~tplv-goo7wpa0wc-image.image)

@col 50
打开 OpenClaw 项目页面

![Image=1280x633](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/860a5dc581b24e90877b381a9a38d56a~tplv-goo7wpa0wc-image.image)
::::

5. 和编程 AI 对话，要求升级到 3.13 版本。
   ![Image=662x334](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f7b0f3ec2e764f3ab4028b18b1e1355b~tplv-goo7wpa0wc-image.image)   


### Web UI 页面无响应 {#0118decd}


* **问题现象**：在扣子编程的 OpenClaw 项目中访问 Web UI 时，浏览器报错“页面无响应”。
   ![Image=280x222](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/379470ec666e40afa6557a4d6e596df8~tplv-goo7wpa0wc-image.image)
* **问题原因**：其他渠道的历史消息过多，Web UI 无法一次性加载这些历史消息，导致页面加载超时。
* **解决方案**：
   * 哪个渠道消息量大、堆积多，就优先清理对应渠道的历史会话；若**多个渠道消息均爆满**，所有高负载渠道务必全部清理；
   * 快速清理操作：在飞书等对话内输入 `/new` 新建会话，或者发送“`帮我新建一个会话`”。清空历史消息后，再重新访问 Web UI 即可恢复正常。
      ![Image=597x248](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f455315088e94a3f93749ed1f1f51616~tplv-goo7wpa0wc-image.image)
