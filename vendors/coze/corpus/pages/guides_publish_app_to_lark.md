> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

飞书是一站式协同办公平台，为企业提供各种数字化办公解决方案。你可以将搭建的低代码应用发布到飞书中，让飞书中的用户与应用对话。

## 前提条件 {#95adb23d}

* 待发布的应用至少包含一个对话流。
* 扣子应用的发布者必须是扣子应用的所有者，协作者或管理员等角色均不支持发布应用。

:::notice 注意
发布应用到飞书时，仅发布应用中的指定对话流。
:::

## 发布应用到飞书 {#297ad63b}

以下是将低代码应用发布到飞书的详细步骤：

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部空间列表中选择目标工作空间。
3. 在**项目开发**页面，选择目标低代码应用，在应用编排页面右上角，单击**发布**。
4. 在发布页面填写版本信息：
   * **版本号**：必填，必须是一个应用从未设置过的新版本号。
   * **版本描述**：可选，说明该版本更新的内容。
5. 在 **选择发布平台 > 发布到通讯或社交平台** 选项，选择待发布的对话流。当用户在飞书平台发送消息时，将调用该对话流来接收用户消息。
6. 首次发布到飞书时需要进行授权，根据引导完成授权。
   ![Image=408x320](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/999f464b4c52484ea2c637b12a71eaa4~tplv-goo7wpa0wc-topic.webp)
7. 在弹出的页面，单击**授权**。
   ![Image=472x435](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/689d54e3cc124b29ab45da0a91f6274f~tplv-goo7wpa0wc-topic.webp)
8. 完成授权后，返回发布页面，勾选**飞书**渠道，然后单击**发布**。
   发布完成后，可点击在**飞书中打开**链接跳转至飞书应用中，与应用对话。
   :::tip 说明
   如果这是你的飞书租户第一次发布扣子应用，你会收到飞书消息提醒。如果提醒应用审核通过，则你可以直接使用应用。否则你需要等待企业管理员审核完成之后，才可以使用应用。
   :::   


## 在飞书中分享你的应用 {#297d9a13}

:::notice 注意
目前只支持在同一飞书租户内分享应用，不支持跨飞书租户分享应用。
:::

你可以通过以下两种方式分享应用：

* 方式一：分享应用链接。
   1. 打开飞书客户端，单击应用头像，然后再单击分享按钮将应用分享给飞书好友。
   2. 被分享人需要点击链接申请使用权限，待应用开发者通过权限申请后，被分享人即可使用应用。
* 方式二：在开发者后台，修改应用的可见范围。
   1. 登录[飞书开发者后台](https://open.feishu.cn/)。
   2. 单击已发布的应用应用，进入应用详情页。
      ![Image=531x188](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/31672131ef654000ba32ced3757bad73~tplv-goo7wpa0wc-topic.webp)
   3. 在左侧菜单栏，单击**版本管理与发布**，然后再单击**创建版本**。
      ![Image=531x159](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/220948d305d5410e8a2aa21010366548~tplv-goo7wpa0wc-topic.webp)
   4. 输入版本信息和更新版本说明，然后单击可用范围配置下的**编辑**链接，添加可使用该应用的人员。最后单击**保存**。
      ![Image=529x261](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/251a69a1088249e89d2bcdf5c51f3c66~tplv-goo7wpa0wc-topic.webp)
   5. 单击**申请上线发布**完成应用发布。
      发布后，添加的用户就可以在飞书中搜到这个应用，并与其对话。
