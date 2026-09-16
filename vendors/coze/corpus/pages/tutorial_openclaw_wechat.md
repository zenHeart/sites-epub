> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

如果你想通过微信和你的 OpenClaw AI 助理对话，可以在**部署 OpenClaw 部署**之后，创建一个微信机器人，通过扣子 AI 配置 OpenClaw 的微信渠道。

关于 OpenClaw 的详细说明，可参考[一键部署 OpenClaw 并集成飞书](/tutorial/openclaw)。

## 使用前须知 {#hwpoZq1vl}

在开始部署前，请花一分钟了解相关的限制、费用和安全建议。

<!-- @cols-width: 160,642 -->
| | | \
|**项目** |**说明** |
|---|---|
|使用限制 |如果取消部署，对话随时可能因环境回收而中断。 |
|微信限制 |* **个人专用**：**微信ClawBot**是你与自己拥有的 OpenClaw 之间的私密消息通道，其他用户无法添加你的**微信ClawBot**。 |\
| |* **不支持群聊**：目前，微信ClawBot不能被加入微信群，仅支持个人单点使用。 |\
| |* **不支持自动化操作**：**微信ClawBot**仅作为消息通道，不会自动化操作你的微信。 |
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

### 步骤一：确认已有 OpenClaw 项目 {#hPBIfGrxy}

:::tip 说明
* **2026 年 6 月 30 日起，​**原扣子编程 OpenClaw 项目不再支持新建，已创建的 OpenClaw 项目不受影响，可继续配置和使用。
* 个人高阶版及以上版本的套餐用户可以通过扣子云端 Agent，新建 OpenClaw Agent。详细说明可参考[云端 Agent](/cozespace_cloud_agent)。
:::

你可以在[扣子编程](https://code.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的**项目开发**页面，查看之前已创建的 OpenClaw 项目。

![Image=338x183](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d64b5e7dcc974f25b33dd22babec3f1a~tplv-goo7wpa0wc-topic.png)

### 步骤二：配置微信渠道 {#90db114f}

1. 在**项目开发**页面找到 OpenClaw 项目，然后在 **OpenClaw 配置**页面找到**微信渠道**，单击**去创建**。
   * 如果是刚刚部署的 OpenClaw 项目，页面会自动弹出 **OpenClaw 配置**页面。
   * 如果之前已经部署 OpenClaw 并配置了其他渠道，可以在 OpenClaw 项目页面右上角单击配置按钮，打开 **OpenClaw 配置**页面。
   ::::cols
   @col 50
   ![Image=2780x1560](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fd9f74cae1e942ebbed37d3688f3209a~tplv-goo7wpa0wc-topic.png)
   
   @col 50
   ```Plain Text
     ![Image=641x331](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ce4f8ec5c56845988438a9dbdf5644a1~tplv-goo7wpa0wc-image.image)
   ```
   ::::
2. 打开微信客户端，扫描屏幕显示的二维码。
   :::tip 说明
   * 微信客户端版本要求为 8.0.70 及以上，如果版本号不符合要求，扫码时会提示更新版本。更新版本后需要重启微信、再扫码。
   * 首次配置微信渠道时，生成二维码预计耗时 3~4 分钟左右，请耐心等待。
   * 二维码有效期为 5 分钟，如果微信扫码时提示二维码已过期，请手动刷新二维码后再试。
   :::
3. 根据微信客户端提示，单击**连接**。
4. 后台会自动完成渠道连接，并自动打开一个名为**微信 ClawBot** 的对话页面。
   ::::cols
   @col 49
   ![Image=190x411](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/834f333f73084ed2928b96bcde508451~tplv-goo7wpa0wc-image.image)
   
   @col 49
   ![Image=185x401](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a182b0e9a66c4fe38c0c1676d33b750b~tplv-goo7wpa0wc-image.image)
   ::::
5. 输入任意一条消息，测试微信机器人是否能正常回复。
   如果机器人及时回复消息，表示微信渠道已配置成功。为了方便后续快速打开机器人对话页面，建议你置顶对话。   


::::cols
@col 33
测试回复：

![Image=180x389](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4a79a7bf27d6434086246793bdce5515~tplv-goo7wpa0wc-image.image)

@col 33
打开设置页面：

![Image=177x383](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/21eac3edf92d4c4ea8d273988d1512c1~tplv-goo7wpa0wc-image.image)

@col 33
置顶对话：

![Image=178x385](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/183965bb22754d1296457c6cf88c2784~tplv-goo7wpa0wc-image.image)
::::

6. （可选）设置机器人的备注名称。
   由于微信客户端限制，搜索机器人的默认名称 **微信 ClawdBot** 可能搜索不到你的机器人。建议为机器人设置头像和备注，方便检索。
   在机器人对话页面右上角单击设置图标，并在机器人详情页右上角展开隐藏菜单，单击**备注名**区域，根据页面提示输入机器人名称即可。
   ::::cols
   @col 33
   ![Image=162x351](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/21eac3edf92d4c4ea8d273988d1512c1~tplv-goo7wpa0wc-image.image)
   
   @col 33
   ![Image=165x357](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/477d8a00c89841b994a7e5946bc8e021~tplv-goo7wpa0wc-image.image)
   
   @col 33
   ![Image=164x355](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/79e445c91145492eb3baa2f429cf3f9f~tplv-goo7wpa0wc-image.image)
   ::::   


### 步骤三：体验效果 {#4bfa2431}

打开微信客户端，在对话列表中找到你的 OpenClaw 助理，体验对话效果。

对话列表中，有 AI 标识的就是你的 OpenClaw 助理。

::::cols
@col 50
找到 OpenClaw AI 助理：

![Image=198x428](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/00a1f64a53184edfacab933baaa91509~tplv-goo7wpa0wc-image.image)

@col 50
对话效果：

![Image=199x431](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0fa84babf71d4110b032d3c6a75626e5~tplv-goo7wpa0wc-image.image)
::::

## 常见问题 {#b2b8b524}

* [已经配置过渠道，还能添加其他渠道吗？](/tutorial/openclaw_faq#03820834)
* [为什么微信是最新版本，扫码还是报错？](/tutorial/openclaw_faq#a13ae4c6)
* [微信中搜索不到机器人？](/tutorial/openclaw_faq#f5f36ac4)
* [为什么电脑、网页等微信客户端看不到 OpenClaw 对话？](/tutorial/openclaw_faq#d7540fac)
