> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

你可以将搭建的低代码智能体发布到微信客服机器人中，增强微信客服的能力。

:::tip 说明
* 支持在回复微信客服时上传图片，但图片大小不能超过 10 MB。
* 确保已经完成了企业认证。
:::

# 前提条件 {#3ba9983c}

1. 已开通了[微信客服](https://kf.weixin.qq.com/)。
2. 已搭建了智能体。

# 步骤一：获取微信客服配置信息 {#b13f0e92}


1. 登录[微信客服](https://kf.weixin.qq.com/)平台。
2. 单击**企业信息**，然后复制企业 ID。
   ![Image=470x194](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d5298c9044534fa887eeadf1a5c2dc77~tplv-goo7wpa0wc-topic.webp)
3. 单击**开发配置**，然后再单击**开始使用**。
   ![Image=462x236](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2bccbd00fe9c42158e1fb2f8466ff652~tplv-goo7wpa0wc-topic.webp)
4. 单击**随机获取**按钮分别生成并保存 Token 和 EncodingAESKey。
   :::notice 注意
   复制 Token 和 EncodingAESKey 后，先不要关闭该页面。
   :::
   ![Image=395x266](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1552811acb57416e924a62af75975973~tplv-goo7wpa0wc-topic.webp)   


# 步骤二：在扣子中配置微信客服信息 {#aa9c3158}


1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部空间列表中选择目标工作空间。
3. 在**项目开发**页面，选择低代码智能体。在页面右上角，单击**发布**。
5. 找到微信客服渠道，然后单击 **配置**。
6. 输入步骤一中复制的企业 ID，然后单击**下一步**。
7. 输入步骤一中复制的 Token 和 EncodingAESKey，然后单击**下一步**。
   ![Image=322x222](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/aff3f593418f4ef183bfe338079d8b23~tplv-goo7wpa0wc-topic.webp)
8. 复制 webhook 地址。
   :::notice 注意
   复制 webhook 地址后，先不要关闭该配置窗口。
   :::
   ![Image=296x293](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/45ccd8a142344632b8acf959eb192efd~tplv-goo7wpa0wc-topic.webp)   


# 步骤三：配置回调地址 {#60012c87}


1. 回到步骤一中的开始企业接入页面，输入上一步中复制的 webhook 地址。单击**完成**。
   :::tip 说明
   * 确保粘贴回调地址时没有引入空格，空格会导致校验失败。
   * 未完成企业认证时，回调地址校验失败。
   :::
   ![Image=394x288](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/eda97458988f40ec9c9754b7f4ccc69c~tplv-goo7wpa0wc-topic.webp)
2. 在**开发配置**页面，复制 secret。
   ![Image=358x181](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6463d145b0c54876b5044b6838be17f1~tplv-goo7wpa0wc-topic.webp)
3. 单击**客服账号**，复制账号。
   ![Image=359x106](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f96a5f90b613486a8697aa1101a03e1e~tplv-goo7wpa0wc-topic.webp)   


# 步骤四：发布智能体 {#476a5c7e}


1. 回到扣子平台的微信客服渠道配置页面，输入复制的 secret 和客服名称。
   ![Image=279x272](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8d0dbb7bab1e4667b57302e69eb3c17b~tplv-goo7wpa0wc-topic.webp)
2. 单击**保存**。
3. 在**发布记录**中输入发布信息，然后勾选**微信客服**渠道，再单击**发布**。
4. 发布完成后，单击**立即对话**登录微信客服，体验智能体效果。

# 下架智能体 {#605f8653}

如果不再需要在该渠道中展示智能体，你可以选择将其下架。下架的操作步骤请参见[下架智能体](/guides/manage_published_project#21bbc41b)。

# 常见问题 {#978ef7fe}

## 收不到机器人回复消息 {#1034a5ff}

可尝试通过以下方法解决：

* **查看微信客服的启用状态**
   1. 登录[企业微信管理后台](https://work.weixin.qq.com/wework_admin/frame#apps)，在**应用管理**页面，点击**微信客服**。
      ![Image=399x124](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/98502d02bb414f81b47c7c59a5754bc6~tplv-goo7wpa0wc-topic.webp)
   2. 确保**没有启用**微信客服功能。如果已经开启了微信客服功能，需要关闭。
      :::tip 说明
      关闭后，该应用在工作台入口将被隐藏，员工不可使用。请谨慎评估。
      :::

   ![Image=463x99](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/802964dc72124daf9868a2dd7b9fc30b~tplv-goo7wpa0wc-topic.webp)
* **检查近期是否有登录企业微信应用。**
   确保企业至少有一个成员通过**手机号验证/微信授权**登录过企业微信应用。   


## 页面提示回调地址校验失败 {#9d2c7091}

以下原因可能导致回调地址校验失败：

* 未完成企业认证：
   企业认证中、未发起企业认证流程等状态下，配置回调地址时会触发页面提示“回调地址校验失败”。你也可以先发布到微信订阅号，待企业认证通过后再发布到微信客服中使用。发布到微信订阅号的方式可参考[发布到微信订阅号](/guides/wechat_subscription)。
* 回调地址中存在空格：
   请检查回调地址是否正确、是否存在多余的空格等不可见字符。   


## 如何让微信中直接显示图片？ {#502e6c92}

由于微信平台本身的限制。当一条消息中同时包含文字和图片时，系统会自动将图片以 URL 形式发送，而不是直接显示图片。

如果需要在微信中直接显示图片，而不是图片链接，你需要确保智能体在输出图片时不输出任何其他文字内容。

## 如何下架已发布到微信客服的智能体？ {#c8d81d96}

如需下架发布到微信客服的智能体，需在微信客服后台完成下架操作，直接在扣子侧删除智能体并不能完成下架操作。请前往[企业微信管理后台](https://work.weixin.qq.com/wework_admin/frame#apps)手动解除智能体的接入状态。

## 发布微信客服提示审核不通过怎么办？ {#737aad90}

将智能体发布到微信公众号或微信客服等渠道时，需要经过微信平台的审核。如果审核未通过，请您耐心等待审核结果。根据[扣子平台内容发布标准和规范](/guides/content_principles)检查并修改智能体配置，确保内容符合微信平台的要求，然后重新提交审核。

如果确认内容没有问题，但审核仍未通过，你可以在微信客服平台单击回复消息下方的**转人工**按钮，联系微信客服团队，并提供以下信息以便协助排查问题：

* 智能体编辑页面的 URL 地址。
* 微信客服平台上的企业 ID（以  ww  开头的字符）。
