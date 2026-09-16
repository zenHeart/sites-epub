> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

OpenClaw 是一款开源的主动型 AI Agent。你可以通过 OpenClaw 将多渠道通信能力与大语言模型深度集成，创建拥有持久记忆与主动执行能力的定制化 AI 助理。

关于 OpenClaw 的详细说明，可参考[什么是 OpenClaw](/tutorial/openclaw#d7ec1b62)。

## 使用前须知 {#hbO2nkqUe}

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

### 步骤一：确认已有 OpenClaw 项目 {#hEm8yMQs8}

:::tip 说明
* **2026 年 6 月 30 日起，​**原扣子编程 OpenClaw 项目不再支持新建，已创建的 OpenClaw 项目不受影响，可继续配置和使用。
* 个人高阶版及以上版本的套餐用户可以通过扣子云端 Agent，新建 OpenClaw Agent。详细说明可参考[云端 Agent](/cozespace_cloud_agent)。
:::

你可以在[扣子编程](https://code.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的**项目开发**页面，查看之前已创建的 OpenClaw 项目。

![Image=338x183](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d64b5e7dcc974f25b33dd22babec3f1a~tplv-goo7wpa0wc-topic.png)

### 步骤二：配置企业微信渠道 {#6d348026}

扣子编程现已支持一键配置企业微信渠道，在 **OpenClaw 配置**页面单击**去配置**按钮，根据页面提示扫描二维码，即可和你的 OpenClaw 助手在企业微信对话。

详细操作步骤如下：

1. 打开 OpenClaw 配置页面。
   你可以在 OpenClaw 页面右上角单击配置图标，进入 **OpenClaw 配置**页面。
   ::::cols
   @col 50
   ![Image=2780x1560](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fd9f74cae1e942ebbed37d3688f3209a~tplv-goo7wpa0wc-topic.png)
   
   @col 50
   ![Image=578x366](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/af65362f91ba42238e24eaed7e73b3b9~tplv-goo7wpa0wc-image.image)
   ::::
2. 在**渠道配置**区域，找到**企业微信**，并单击**去配置**。
   ![Image=583x364](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f2b4ef028acd4b42ae1e71f8fc1f81ef~tplv-goo7wpa0wc-image.image)
3. 使用企业微信 App 扫描二维码。
   ![Image=514x322](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/54a41ca3e5784a548d6b0917434cfbf8~tplv-goo7wpa0wc-image.image)
4. 根据企业微信的页面提示，创建机器人并授权。
   ::::cols
   @col 33
   创建机器人：
   
   ![Image=160x347](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/382f9fec85c64f3a8b59cffe144813d2~tplv-goo7wpa0wc-image.image)
   
   @col 33
   为机器人授权：
   
   ![Image=157x340](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d4687c4672c94b4bb68884cf80175f4c~tplv-goo7wpa0wc-image.image)
   
   @col 33
   创建成功：
   
   ![Image=155x336](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0e74e59233b84513b8ee1c4dccad9c09~tplv-goo7wpa0wc-image.image)
   ::::
5. 等待一切就绪。
   在扣子编程中看到以下页面，表示企业微信渠道已配置完成。你可以去企业微信 APP 中和 OpenClaw 助手对话了。
   ![Image=472x289](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/af3e36d321104e269d1f1e8e2a16c6d9~tplv-goo7wpa0wc-image.image)   


### 步骤三：体验效果 {#dfb84a6c}

当你的企业微信机器人通过企业管理员审核之后，你可以打开企业微信，找到 OpenClaw AI 助理，体验对话效果。

企业微信 OpenClaw 机器人的名称默认为 `XX 的机器人`，你可以直接在企业微信中搜索名称，找到机器人。

::::cols
@col 50
找到 OpenClaw AI 助理：

![Image=174x377](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fabc4976989145b89a014eda00e72822~tplv-goo7wpa0wc-image.image)

@col 50
对话效果：

![Image=170x368](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0dc9e0e228f649d38e229ab99a2351b8~tplv-goo7wpa0wc-image.image)
::::

## 相关操作 {#71d0dde0}

### 修改企业微信机器人名称和头像 {#17ed4340}

企业微信 OpenClaw 机器人的名称默认为 `XX 的机器人`，头像为默认头像。你可以在企业微信的智能机器人应用中修改机器人名称和头像。

1. 搜索智能机器人，并打开应用。
2. 找到你的 OpenClaw 机器人，其名称默认为 `XX 的机器人`。
3. 打开机器人页面，在右上角单击编辑。
4. 修改机器人名称和头像，单击保存即可。

::::cols
@col 25
搜索智能机器人应用：

![Image=146x316](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bfb8fd777e9e45e793e1a18365c65524~tplv-goo7wpa0wc-image.image)

@col 25
打开智能机器人应用：

![Image=147x319](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ad066e561a274d79b62e6fed455d3735~tplv-goo7wpa0wc-image.image)

@col 25
找到机器人，单击编辑：

![Image=147x319](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/047f1fcf56a945a3a7b89bbc01d81994~tplv-goo7wpa0wc-image.image)

@col 25
修改名称和头像：

![Image=144x312](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/086c41235e224c87a07984d3635639ba~tplv-goo7wpa0wc-image.image)
::::

### 更换企业微信账号 {#1b02e718}

如果你想把 OpenClaw 换绑到另一个企业微信账号，需要重新配置一下企业微信渠道，使用新的企业微信账号扫码授权即可。

1. 打开 OpenClaw 配置页面。
   ![Image=466x295](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/af65362f91ba42238e24eaed7e73b3b9~tplv-goo7wpa0wc-image.image)
2. 找到企业微信，展开折叠菜单，单击重新配置。
   ![Image=461x288](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6bfd88d9c8464cabaac20895eae60f4b~tplv-goo7wpa0wc-image.image)
3. 使用新的企业微信账号扫码授权即可。

## 常见问题 {#c5aa9d4d}


* [切换模型](/tutorial/openclaw#1d491b08)
* [OpenClaw 项目里，扣子 AI 能做什么？](/tutorial/openclaw_faq#85225568)
* [如何取消部署？](/tutorial/openclaw_faq#d456c347)
* [OpenClaw 对话中断或无响应？](/tutorial/openclaw_faq#87497c22)
