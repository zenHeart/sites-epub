> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

如果你想通过钉钉和你的 OpenClaw AI 助理对话，可以在**部署 OpenClaw 部署**之后，创建一个钉钉机器人，通过扣子 AI 配置 OpenClaw 的钉钉渠道。

关于 OpenClaw 的详细说明，可参考[一键部署 OpenClaw 并集成飞书](/tutorial/openclaw)。

## 使用前须知 {#hKqRh5jqx}

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

## 操作步骤 {#f9af6ca9}

### 步骤一：确认已有 OpenClaw 项目 {#90db114f}

:::tip 说明
* **2026 年 6 月 30 日起，​**原扣子编程 OpenClaw 项目不再支持新建，已创建的 OpenClaw 项目不受影响，可继续配置和使用。
* 个人高阶版及以上版本的套餐用户可以通过扣子云端 Agent，新建 OpenClaw Agent。详细说明可参考[云端 Agent](/cozespace_cloud_agent)。
:::

你可以在[扣子编程](https://code.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的**项目开发**页面，查看之前已创建的 OpenClaw 项目。

![Image=338x183](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d64b5e7dcc974f25b33dd22babec3f1a~tplv-goo7wpa0wc-topic.png)

### 步骤二：创建钉钉应用并完成配置 {#6d348026}

1. 创建钉钉应用。
   1. 登录[钉钉开放平台](https://open-dev.dingtalk.com/)，单击**创建**按钮。
      要创建钉钉应用，您的钉钉账号需要有开发者权限。您可以联系您的组织管理员获取钉钉开放平台的开发权限。
   2. 在左侧目录树中选择**企业内部应用** > **钉钉应用**，在页面右上角单击**创建应用**按钮。
      ![Image=464x163](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e516b162ef2c45deac7c5a838c44e3be~tplv-goo7wpa0wc-image.image)
   3. 配置应用名称、图标等信息后，单击**保存**。
2. 为钉钉应用添加权限**。**
   钉钉应用需要申请的权限如下：
   ```Plain Text
   Card.Instance.Write
   Card.Streaming.Write
   qyapi_robot_sendmsg
   ```
   申请权限的操作步骤如下：
   1. 登录[钉钉应用控制台](https://open-dev.dingtalk.com/fe/app)，单击前文创建的应用名称进入其详情页。
   2. 在左侧目录树选择**开发配置 > 权限管理**。
   3. 在搜索框中输入`Card`，勾选**互动卡片实例写权限**与**AI卡片流式更新权限**，单击**批量申请**按钮完成操作。
      ![Image=388x187](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f76c1f6d7018477ca8833fd9a774435e~tplv-goo7wpa0wc-image.image)
   4. 在搜索框中输入`qyapi_robot_sendmsg`，单击**企业内机器人发送消息**权限右侧**操作**列的**立即开通**按钮完成操作。
      ![Image=410x194](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6fbf401eecb448778bdb3b211ec4e7da~tplv-goo7wpa0wc-image.image)
3. 配置钉钉机器人。
   1. 在左侧目录树选择**应用能力 > 添加应用能力**，单击机器人卡片的**添加**按钮。
      ![Image=408x161](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a90a4248a26f4254a2ab23c1fef1b5f1~tplv-goo7wpa0wc-image.image)
   2. 在**机器人配置**页面，打开**机器人配置**开关。
      ![Image=416x240](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/11d458afb56a4a17aef767282a2d970b~tplv-goo7wpa0wc-image.image)
   3. 将**消息接收模式**调整为 **Stream** 模式。
      ![Image=490x118](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/34e37b74863e40bab10ec99d96386e84~tplv-goo7wpa0wc-image.image)
   4. 单击**发布**按钮，保存配置。
4. 发布应用版本。
   1. 在左侧目录树选择**应用发布 > 版本管理与发布**，并单击创建新版本按钮。
   2. 按需配置**应用版本号、可见范围**等信息后，单击**保存**按钮。
   3. 在弹窗中单击**确认发布**按钮，发布应用版本。
      ![Image=586x336](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ec6fa1041020437c919e03e7bf1948b1~tplv-goo7wpa0wc-image.image)
5. 获取应用信息。
   在左侧目录树选择**基础信息 > 凭证与基础信息**，找到并复制 AppKey、AppSecret、App ID 和 CorpId。这些密钥信息将被用于后续的渠道配置。
   ![Image=614x220](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/89466e27b3c34297974157ea0883b774~tplv-goo7wpa0wc-image.image)   


### 步骤三：配置 OpenClaw 钉钉渠道 {#ad707822}

扣子已经为你的 OpenClaw 项目安装了钉钉插件，创建钉钉应用并完成配置后，只要通过对话向扣子 AI 提供密钥信息即可。

1. 登录扣子编程，找到你的 OpenClaw 项目。
2. 在左下角输入框中，输入你的指令，请扣子 AI 安装钉钉插件，并配置相关密钥。

::::cols
@col 66
```Plain Text
请帮我配置钉钉机器人
1. AppKey：<your_appkey>
2. AppSecret：<your_appsecret>
3. App ID：<your_appId>
4. CorpId：<your_CorpId>
```

@col 33
<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fdce4309ebec467a8f5af2908fb4ca91~tplv-goo7wpa0wc-image.image" width="938px" height="1436px" /></div>
::::

### 步骤四：体验效果 {#4bfa2431}

当你的钉钉应用通过企业管理员审核之后，你可以打开钉钉 App，找到 OpenClaw AI 助理，体验对话效果。

::::cols
@col 50
找到 OpenClaw AI 助理：

![Image=2042x1272](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3f19a6b35c0e493c897538f2ad96e372~tplv-goo7wpa0wc-image.image)

@col 50
对话效果：

![Image=1274x1180](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f6a8f7315b674497bc8ebc46030b95e0~tplv-goo7wpa0wc-image.image)
::::

## 常见问题 {#5af2abcb}

* [切换模型](/tutorial/openclaw#1d491b08)
* [OpenClaw 项目里，扣子 AI 能做什么？](/tutorial/openclaw_faq#85225568)
* [如何取消部署？](/tutorial/openclaw_faq#d456c347)
* [OpenClaw 对话中断或无响应？](/tutorial/openclaw_faq#87497c22)
