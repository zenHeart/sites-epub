> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

## 什么是 OpenClaw {#d7ec1b62}

[OpenClaw](https://openclaw.ai/)**（原 Moltbot、Clawdbot）** 是一款开源的个人 AI 助理和智能代理系统，可运行在个人电脑或服务器上。和传统的 AI 助理不同，OpenClaw 不是普通的聊天机器人，被授予操作权限之后，它能控制你的终端执行操作，可以“动手工作”，而不是“只出主意”。你可以通过飞书等即时通信工具与它对话交互，让它帮你完成各类任务，例如生成图文、处理邮件、管理日程等。

扣子编程现已支持一键安装 OpenClaw。开发者可以在扣子编程的云主机环境里快速安装部署 OpenClaw，打造一个定制的个人 AI 助理。

相较于其他部署方案，扣子编程部署的 OpenClaw 具备以下**优势**：

* 和**本地运行 OpenClaw** 相比：扣子编程部署 OpenClaw 操作便捷，环境隔离、可保护数据和 API Key 的隐私安全，保障助手全天 24 小时稳定运行。
* 和**云服务器运行 OpenClaw** 相比：扣子编程部署 OpenClaw 是真正的一键部署。无需选购服务器、开通并配置模型；无需终端命令行操作，一键打通飞书等 IM 工具。只需通过自然语言交互，就可以让扣子 AI 为你调整运行配置、添加个性化技能，打造开箱即用的 AI 助手。
* 和 QQ 等 **IM 工具提供的 OpenClaw** 相比：扣子编程提供了安全的云主机环境和配套的 AI 编程助手，可实现高度定制化、更高的能力上限，例如便捷的浏览器工具，可无障碍访问各类网站。生态开放，支持便捷打通各类 IM 工具，无功能裁剪与限制。

::::cols
@col 50
![Image=3810x1640](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/96a8506ea9db44a6992fff36262e5653~tplv-goo7wpa0wc-image.image)

@col 50
![Image=1514x872](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b36199bc74d84f6caafa6cbae91ef4e5~tplv-goo7wpa0wc-image.image)
::::

## 使用前须知 {#htBOm1CoW}

在开始部署前，请花一分钟了解相关的限制、费用和安全建议。

<!-- @cols-width: 160,642 -->
| | | \
|**项目** |**说明** |
|---|---|
|使用限制 |如果取消部署，对话随时可能因环境回收而中断。 |
|安全提醒 |建议企业用户谨慎使用 OpenClaw，它可能存在明文存储凭证等安全风险。扣子编程建议你： |\
| | |\
| |* **定期轮换**所有提供给 OpenClaw 的凭证。 |\
| |* **不要**将任何生产环境的敏感信息交给 OpenClaw 处理。 |\
| |* **谨慎判断**是否要将 OpenClaw 个人助理添加到群聊中，避免其泄露 API Key 等敏感信息。 |
|费用说明 |* 使用 OpenClaw 会消耗你的扣子编程积分（包括对话、大模型调用、图片生成等）。 |\
| |   如需使用第三方模型（如火山方舟 Coding plan 等），需提前准备对应的 API Key，并自行支付模型费用。 |\
| |* OpenClaw 的 Token 消耗较高，你可以选择**省流版**以节省 Token 成本。 |\
| |* 自 **2026 年 7 月 1 日**起，已部署的 OpenClaw 项目会产生云电脑费用，每台云电脑每天消耗约 **800 积分。​**更多信息，请参考[费用说明](/tutorial_openclaw_overview#hszGFhoYK)。 |

## 部署 OpenClaw 飞书助理 {#000351b0}

参考以下流程，在扣子编程中创建你的 OpenClaw AI 助理，并打通飞书渠道。操作完成后，你可以在飞书中和 OpenClaw AI 助理对话。

### 视频教程 {#413988bb}

<Player class="topic-video-player"  class="topic-video-player"  class="topic-video-player"  class="topic-video-player"  class="topic-video-player"  class="topic-video-player"  class="topic-video-player"  class="topic-video-player"  class="topic-video-player"  style="width:730px" src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/43ab6cf5632b497aa817620083cb1376~tplv-goo7wpa0wc-image.image"></Player>

### 步骤一：确认已有 OpenClaw 项目 {#881b9631}

:::tip 说明
* **2026 年 6 月 30 日起，​**原扣子编程 OpenClaw 项目不再支持新建，已创建的 OpenClaw 项目不受影响，可继续配置和使用。
* 个人高阶版及以上版本的套餐用户可以通过扣子云端 Agent，新建 OpenClaw Agent。详细说明可参考[云端 Agent](/cozespace_cloud_agent)。
:::

你可以在[扣子编程](https://code.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的**项目开发**页面，查看之前已创建的 OpenClaw 项目。

![Image=338x183](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d64b5e7dcc974f25b33dd22babec3f1a~tplv-goo7wpa0wc-topic.png)

### 步骤二：配置飞书渠道 {#hfadTYpid}

扣子编程现已支持一键配置飞书渠道，在 OpenClaw 配置页面确认你的飞书机器人名称，单击创建按钮，即可和你的 OpenClaw 助手在飞书对话。

详细操作步骤如下：

1. 打开 OpenClaw 配置页面。
   你可以在 OpenClaw 页面右上角单击配置图标，进入 **OpenClaw 配置**页面。
   ::::cols
   @col 50
   ![Image=2780x1560](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fd9f74cae1e942ebbed37d3688f3209a~tplv-goo7wpa0wc-topic.png)
   
   @col 50
   ![Image=520x325](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f96eb43079794fe6bd9692f6519ee101~tplv-goo7wpa0wc-image.image)
   ::::
2. 在**渠道配置**区域找到**飞书**渠道，单击**去配置**。
   ![Image=343x198](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/16595799a8014ff1bdae470beebdd6bc~tplv-goo7wpa0wc-image.image)
3. （可选）确认飞书机器人的名称，并单击**开始配置**。
   机器人名称默认为 `XX 的助手`，如果你不喜欢这个机器人的名字，可以重新设置。
   ![Image=350x241](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/02c448b755424961869f2fa5c95627a1~tplv-goo7wpa0wc-image.image)
4. 确认飞书账号，并单击**授权**。
   ![Image=362x400](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fe96ee9539214c2f8dcc4d9d385ef648~tplv-goo7wpa0wc-image.image)
5. 等待后台配置完成。
   如果看到以下页面，表示扣子编程仍在后台帮你配置飞书群渠道，请耐心等待。
   ![Image=365x244](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1a8e1ad7155540b99fa8ed2b534b2414~tplv-goo7wpa0wc-image.image)
6. 成功连接到飞书。
   扣子编程会在后台为你创建飞书机器人、开启长连接，并配置相关权限、事件与回调、配对。如果看到以下页面，表示你的 OpenClaw 助手已经成功连接到飞书，可以根据页面提示去飞书和 OpenClaw 助手对话。
   * **去后台管理**：前往飞书开放平台，查看你的飞书机器人应用的相关配置，包括 App ID、权限等信息。
   * **去飞书对话**：前往飞书客户端，和你的 OpenClaw 助手对话。如果你有多个飞书账号，请注意登录上述步骤中完成授权的账号，否则可能跳转对话失败。
      ![Image=616x388](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9be33f7e1e4f48a6bde7278ba4631501~tplv-goo7wpa0wc-image.image)      


### 步骤三：体验效果 {#e2a627ca}

扣子编程为你的 OpenClaw 项目预安装了一系列技能与工具，并开通了相关的飞书权限，无需任何额外配置，直接和 OpenClaw 个人助理对话即可完成以下常见任务。

#### 基础问答 {#ece7417e}

::::cols
@col 50
示例 Query：

```Plain Text
介绍一下你自己
```

@col 49
效果：

![Image=216x234](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fe20e4bf8e644b7eb3c64f908f97d45e~tplv-goo7wpa0wc-image.image)
::::

#### 联网搜索 {#4585466f}

::::cols
@col 50
示例 Query：

```Plain Text
查询一下今天的黄金价格
```

@col 49
效果：

![Image=223x150](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/41b036634abd4b8c8d4f930e11fde678~tplv-goo7wpa0wc-image.image)
::::

#### 生成图片 {#04f19bf0}

::::cols
@col 49
示例 Query：

```Plain Text
帮我生成一个马年春节绘本，卡通风格，包含灯笼、春联等春节常见元素，连续 4 张
```

@col 50
效果：

![Image=242x215](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/eb20cb5004ad4d4181b66e35d7c2f00e~tplv-goo7wpa0wc-image.image)
::::

#### 创建飞书文档 {#6fe5f501}

::::cols
@col 50
示例 Query：

```Plain Text
帮我检索关于 OpenClaw 的新闻，整理成一篇日报之后，写到飞书文档里
```

@col 49
效果：

![Image=232x185](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c756c7de3fb84375921999f95a0ca449~tplv-goo7wpa0wc-image.image)
::::

## 增强 OpenClaw 能力 {#296adb3b}

扣子编程已为 OpenClaw 项目预先安装了联网搜索、图片生成等常用技能（Skills），你也可以将自己开发的技能、扣子技能商店的开源技能、Github 开源社区的热门技能安装到自己的 OpenClaw 项目中，增强其在垂直领域的能力。

关于扣子技能的详细说明，可参考[技能概述](/guides/skill_overview)；关于如何创建一个技能，可参考[开发技能](/guides/vibe_coding_skill)。

参考以下流程，将你已有的技能，导入到 OpenClaw 项目中使用。

1. **获取技能包**：从技能项目的文件树中下载技能的 `.zip` 压缩包。
2. **上传安装**：在扣子编程 OpenClaw 项目的左下角对话框中，**上传** 该压缩包，AI 会自动为你安装。
3. **测试技能**：在预览窗口中用自然语言调用该技能，验证效果。

::::cols
@col 33
获取技能包：

![Image=387x207](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8f3eb2edb2724fc18807c4567c75046a~tplv-goo7wpa0wc-image.image)

@col 33
上传安装：

![Image=353x506](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ebea83c8b1e54b6ca699d53534a1644b~tplv-goo7wpa0wc-image.image)

@col 33
测试技能：

![Image=280x248](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6b622aac71294c98b94a4483fb2b0f80~tplv-goo7wpa0wc-image.image)
::::

## 相关配置 {#f89571a0}

### 飞书快捷指令 {#3ab4cfe9}

你的 OpenClaw 绑定飞书之后，可以通过飞书快捷指令，一键执行 OpenClaw 的部分斜杠命令，灵活管理对话状态。

* **`/new`：开始一个新会话**。此命令会清空当前对话的上下文、开启一段全新对话，不会影响历史对话和记忆，一般在切换新话题的时候。
* **`/restart`：重启 OpenClaw**。此命令会重置 OpenClaw 运行状态，彻底重启服务。常用于助手响应异常、逻辑混乱或功能卡顿时恢复正常。
* **`/stop`：中止当前会话**。此命令立即停止当前正在生成的内容或执行中的任务，保留现有上下文，仅终止本次输出。

![Image=371x341](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/635fcd2d24564f138652ab22b0e1621e~tplv-goo7wpa0wc-image.image)

### 切换模型 {#1d491b08}

扣子编程默认为你的 OpenClaw 项目安装了内置的大模型、图片生成、联网搜索集成，如果你希望 OpenClaw 使用其他模型完成任务，可以通过自然语言对话方式，在页面左侧的输入框中下达你的指令。

* **使用扣子编程内置集成的模型**。
   在 **OpenClaw 配置**页面，直接使用扣子编程提供的豆包 2.0 等热门模型，无需额外开通其他厂商的模型服务。
   1. 在 OpenClaw 页面右上角单击配置图标，进入 OpenClaw 配置页面。
   2. 在**模型选择**框中，选择你想使用的模型。
   3. 单击**确定**。
      ::::cols
      @col 50
      打开 OpenClaw 配置页面：
      
      ![Image=2634x1652](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f2b0b364336441f5b3033345119a704c~tplv-goo7wpa0wc-image.image)
      
      @col 50
      选择模型：
      
      ![Image=366x249](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d10eac94b3194a9e99636666b9a48632~tplv-goo7wpa0wc-image.image)
      ::::
* **使用火山方舟等厂商的模型服务 API**。
   如果内置集成中没有你想使用的模型，或者你已经开通了火山方舟等厂商的模型服务，可以直接使用模型 API。建议提供模型 ID、API Key 和完整的 Base URL，便于扣子 AI 帮你快速、正确配置模型。
   ::::cols
   @col 65
   ```Plain Text
   帮我把模型换成火山方舟的 Doubao 1.8，模型详细信息如下
   模型 ID：ep-20260204215010-*****
   API Key：e9da865c-3050-4ed8-b49d-bc6a********
   Base URL：https://ark.cn-beijing.volces.com/api/v3
   ```
   
   > 你可以在火山方舟控制台的“模型广场”页面找到不同模型的 ID，并在“密钥管理”页面创建和获取 API Key。
   
   @col 34
   ![Image=262x319](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5dc5cca6700b4094afa7a3d826a1fe25~tplv-goo7wpa0wc-image.image)
   ::::
* **使用 Coding Plan**。
   如果你开通了火山方舟 Coding Plan，也可以让扣子 AI 帮你切换成支持 Coding Plan 的模型。注意 Coding Plan 的 Base URL 和普通 API 调用不同，建议在对话中提供完整的 Base URL。
   例如：
   ::::cols
   @col 65
   ```Plain Text
   帮我切换成火山方舟 coding plan 的 GLM 4.7 模型，模型详细信息如下
   model name：glm-4.7
   Base URL：https://ark.cn-beijing.volces.com/api/coding/v3
   API Key：e9da865c-3050-4ed8-b49d-bc6a********
   ```
   
   @col 34
   ![Image=1240x1706](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6b9c20dec78847f2b50ea40c5046db19~tplv-goo7wpa0wc-image.image)
   ::::   


### 安装和更新飞书官方插件 {#96992dac}

:::tip 说明
如果你已安装**飞书官方插件**，希望使用最新的插件版本，可以在**终端**区域执行以下命令查看并更新插件版本。

* 查看当前版本：`npx @larksuite/openclaw-lark-tools info`
* 更新插件版本：`npx -y @larksuite/openclaw-lark-tools update`

你也可以要求你的 OpenClaw 个人助理设置定时任务，帮你定期更新飞书插件版本，例如“每天早上十点帮我更新飞书插件，更新命令是 `npx -y @larksuite/openclaw-lark-tools update`”。
:::

在 3 月 5 日及之前创建的 OpenClaw 项目，默认使用 OpenClaw 内置的飞书插件来配置飞书渠道，如果你希望使用**飞书官方**发布的 OpenClaw 飞书插件，体验更强大的飞书集成能力，可以参考以下步骤更新插件。

关于飞书官方插件的详细说明，可参考 [OpenClaw飞书官方插件使用指南（公开版）](https://bytedance.larkoffice.com/docx/MFK7dDFLFoVlOGxWCv5cTXKmnMh)。

安装插件时，你可以选择创建一个新的机器人，或者使用原有的机器人：

* [使用新建的机器人](/tutorial/openclaw#c2aedb98)：（推荐）使用飞书扫码创建一个新的机器人，此插件将自动帮你完成机器人的创建、事件和回调配置、添加权限等等操作，并自动关联到 OpenClaw 项目。
* [使用 OpenClaw 已关联的机器人](/tutorial/openclaw#b76d1b96)：如果你已经有一个关联过 OpenClaw 的飞书机器人，也可以直接使用。但为了体验飞书官方插件的完整能力，你还需要为机器人手动开启一系列配置。

#### 使用新建的机器人 {#c2aedb98}


1. 在扣子编程的 OpenClaw 项目中，打开**终端**窗口。
   ![Image=499x239](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b2750235b42f42169ea2d43698a970a5~tplv-goo7wpa0wc-image.image)
2. 执行以下命令，安装飞书官方插件。
   安装新插件的同时，扣子编程会自动移除原飞书插件。
   ```Shell
   npx -y @larksuite/openclaw-lark-tools install
   ```
3. 根据页面提示，选择 `Create a new bot`，并敲击回车。
   ![Image=530x222](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0e4690c87d2547f2a91e3fde51587d98~tplv-goo7wpa0wc-image.image)
4. 打开飞书客户端，扫描终端输出的二维码。
   ![Image=534x283](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/843f8528db8f4720aea332059df53b6e~tplv-goo7wpa0wc-image.image)
5. 根据飞书客户端的提示，创建飞书机器人。
6. 在飞书向机器人发送一条消息，验证机器人是否正常工作。

#### 使用 OpenClaw 已关联的机器人 {#b76d1b96}


1. 在扣子编程的 OpenClaw 项目中，打开**终端**窗口。
   ![Image=499x239](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b2750235b42f42169ea2d43698a970a5~tplv-goo7wpa0wc-image.image)
2. 执行以下命令，安装飞书官方插件。
   安装新插件的同时，扣子编程会自动移除原飞书插件。
   ```Shell
   npx -y @larksuite/openclaw-lark-tools install
   ```
3. 根据页面提示，选择 `Use an existing bot linked to OpenClaw (使用 OpenClaw 已关联的机器人)`，并敲击回车。
   看到以下提示，表示已成功安装官方插件。
   ![Image=3110x1069](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/51e5a2f880fa49cd808712a74071d5e3~tplv-goo7wpa0wc-image.image)
4. 完成配对。
   1. 打开飞书客户端，找到你已关联 OpenClaw 的飞书机器人，输入任意一条消息。
   2. 飞书机器人会回复你一条包含配对码的消息，复制配对码。
   3. 回到扣子编程，将配对码发送给扣子 AI。
      扣子 AI 会自动完成机器人配对。
      ::::cols
      @col 49
      获取配对码：
      
      ![Image=1002x454](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bf48bfdc2e704b36bbdb2f31777cd443~tplv-goo7wpa0wc-topic.png)
      
      @col 49
      发送给扣子 AI：
      
      ![Image=235x244](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9b03320e1abb49c7ae1c4d032c7ba53c~tplv-goo7wpa0wc-image.image)
      ::::
5. 在飞书向机器人发送一条消息，验证机器人是否正常工作。
   例如，发送 `/feishu start`，如果机器人回复了飞书 OpenClaw 的插件版本，表示已完成机器人配对。
   ![Image=417x182](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/931816aaa63e407cbc4aeab60c08580b~tplv-goo7wpa0wc-image.image)
6. （可选）为飞书机器人添加权限和配置。
   完成配对后，飞书机器人可以正常对话、回复你的问题，但是但为了体验飞书官方插件的完整能力，你还需要为机器人手动开启一系列配置。
   1. 登录[飞书开放平台](https://open.feishu.cn/app?lang=zh-CN)，找到你的飞书机器人应用。
      ![Image=412x257](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0068aba7b780488f8ec05178a1e4c12d~tplv-goo7wpa0wc-image.image)
   2. 为飞书机器人添加必要的权限。
      1. 在左侧目录树选择**安全配置**，开启**刷新 user_access_token** 开关。
         :::tip 说明
         安全配置页面若无此配置，说明企业默认开启了**刷新 user_access_token** 开关，可跳过此步骤。
         :::
         ![Image=542x271](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d24f492788f64311a2707278e690c335~tplv-goo7wpa0wc-image.image)
      2. 在左侧目录中选择**开发配置** >  **权限管理**，单击**批量导入/导出权限**。
         ![Image=2502x1252](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0e54b9ec1bdf4a98b2edfb544e8f382f~tplv-goo7wpa0wc-topic.png)
      3. 在**导入**页签中，将如下权限替换原有示例，单击**下一步，确认新增权限**。
         :::tip 说明
         建议导入以下完整权限。缺失部分权限会影响你的飞书机器人能力与表现。
         :::
         ```JSON
         {
           "scopes": {
             "tenant": [
               "contact:contact.base:readonly",
               "docx:document:readonly",
               "im:chat:read",
               "im:chat:update",
               "im:message.group_at_msg:readonly",
               "im:message.p2p_msg:readonly",
               "im:message.pins:read",
               "im:message.pins:write_only",
               "im:message.reactions:read",
               "im:message.reactions:write_only",
               "im:message:readonly",
               "im:message:recall",
               "im:message:send_as_bot",
               "im:message:send_multi_users",
               "im:message:send_sys_msg",
               "im:message:update",
               "im:resource",
               "application:application:self_manage",
               "cardkit:card:write",
               "cardkit:card:read"
             ],
             "user": [
               "contact:user.employee_id:readonly",
               "offline_access","base:app:copy",
               "base:field:create",
               "base:field:delete",
               "base:field:read",
               "base:field:update",
               "base:record:create",
               "base:record:delete",
               "base:record:retrieve",
               "base:record:update",
               "base:table:create",
               "base:table:delete",
               "base:table:read",
               "base:table:update",
               "base:view:read",
               "base:view:write_only",
               "base:app:create",
               "base:app:update",
               "base:app:read",
               "sheets:spreadsheet.meta:read",
               "sheets:spreadsheet:read",
               "sheets:spreadsheet:create",
               "sheets:spreadsheet:write_only",
               "docs:document:export",
               "docs:document.media:upload",
               "board:whiteboard:node:create",
               "board:whiteboard:node:read",
               "calendar:calendar:read",
               "calendar:calendar.event:create",
               "calendar:calendar.event:delete",
               "calendar:calendar.event:read",
               "calendar:calendar.event:reply",
               "calendar:calendar.event:update",
               "calendar:calendar.free_busy:read",
               "contact:contact.base:readonly",
               "contact:user.base:readonly",
               "contact:user:search",
               "docs:document.comment:create",
               "docs:document.comment:read",
               "docs:document.comment:update",
               "docs:document.media:download",
               "docs:document:copy",
               "docx:document:create",
               "docx:document:readonly",
               "docx:document:write_only",
               "drive:drive.metadata:readonly",
               "drive:file:download",
               "drive:file:upload",
               "im:chat.members:read",
               "im:chat:read",
               "im:message",
               "im:message.group_msg:get_as_user",
               "im:message.p2p_msg:get_as_user",
               "im:message:readonly",
               "search:docs:read",
               "search:message",
               "space:document:delete",
               "space:document:move",
               "space:document:retrieve",
               "task:comment:read",
               "task:comment:write",
               "task:task:read",
               "task:task:write",
               "task:task:writeonly",
               "task:tasklist:read",
               "task:tasklist:write",
               "wiki:node:copy",
               "wiki:node:create",
               "wiki:node:move",
               "wiki:node:read",
               "wiki:node:retrieve",
               "wiki:space:read",
               "wiki:space:retrieve",
               "wiki:space:write_only"
             ]
           }
         }
         ```
      4. 在弹窗中确认权限无误后，单击**申请开通**按钮，完成操作。
         ![Image=383x206](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/695465d9939740a08d0a6bedc90c95be~tplv-goo7wpa0wc-topic.png)
   7. **为飞书机器人配置事件和回调**。
      飞书官方插件内置了一些技能，便于你更好地和机器人交流，如果未配置相关事件和回调，可能影响部分技能的使用体验和效果。
      1. 在左侧目录树选择**开发配置 > 事件与回调**。
      2. 选择**事件配置**页签，在**已添加事件**区域，单击**添加事件**按钮。
      3. 输入 “action”，选择**消息被reaction**、**消息被取消reaction**两个权限，并单击**添加**。
         ![Image=448x230](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/37be700168d84c39a961390a7490fc33~tplv-goo7wpa0wc-topic.png)
         通过 reaction 权限，你可以在对话中实现以下效果：
         ![Image=398x213](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/834d485071f04f0c871a1a3590737256~tplv-goo7wpa0wc-image.image)
      4. 选择**回调配置**页签，单击订阅方式旁的**编辑**按钮。
7. 选择**使用 长连接 接收回调**，并单击保存按钮。
      ![Image=438x279](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a7c415bf666346d5bcb9e6eafc330665~tplv-goo7wpa0wc-image.image)
   5. 在**已添加事件**区域，单击**添加事件**按钮，选择**卡片回传交互**，并单击**添加**。
      ![Image=512x258](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2192a32346f14620bc06858956a719a2~tplv-goo7wpa0wc-image.image)
7. **新建机器人版本并发布**。
   1. 单击顶部的**创建版本**按钮。
      ![Image=506x152](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8eb97e79560842e98a9a0c36731fbbeb~tplv-goo7wpa0wc-image.image)
   2. 按需配置应用版本号、默认能力及更新说明等信息，并在页面底部的**保存**按钮，创建版本。
   3. 根据页面提示发布应用。
      ![Image=575x262](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5faa7e569bdb44bf979addb4f5b4f120~tplv-goo7wpa0wc-image.image)
      待管理员通过发布审核后，即可正式在飞书中使用全新的飞书官方插件，体验新版效果。
      ![Image=574x176](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/000c4ad0f92740698dae19315ba8c31d~tplv-goo7wpa0wc-image.image)      


## 常见问题 {#094cff1b}


* [如何切换授权的飞书账号？](/tutorial/openclaw_faq#daccf446)
* [OpenClaw 项目里，扣子 AI 能做什么？](/tutorial/openclaw_faq#85225568)
* [如何取消部署？](/tutorial/openclaw_faq#d456c347)
* [OpenClaw 对话中断或无响应？](/tutorial/openclaw_faq#87497c22)
* [为什么我的飞书机器人和 OpenClaw 的连接总是中断](/tutorial/openclaw_faq#5fd89018)
