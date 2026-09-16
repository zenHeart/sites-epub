> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

你可以将搭建的低代码应用发布到微信公众号（服务号）中。发布后，服务号就可以使用应用回复用户消息，助力运营。

:::notice 注意
如果您之前绑定过微信服务号，则在应用发布页面的原绑定渠道区域会提示**【即将下线】微信公众号（服务号），​**该场景下您需要先解绑原发布渠道，然后参考本文操作重新绑定**微信公众号（服务号）​**渠道进行发布。
:::

## 使用限制 {#6731faa1}

* 一个应用只能发布到一个企业服务号。
* 确保微信服务号**已经完成了认证**。未认证和认证中的服务号无法接收消息。
* 支持在回复服务号时上传图片，但图片大小不能超过 10 MB。

## 前提条件 {#ea5800e8}


* 已经创建了微信服务号。
* 待发布的应用至少包含一个对话流。
* 扣子应用的发布者必须是扣子应用的所有者，协作者或管理员等角色均不支持发布应用。

:::notice 注意
发布应用到微信服务号时，仅发布应用中的指定对话流。
:::

## 步骤一：获取微信服务号的开发者 ID {#ca3362d1}

1. 访问[微信开发者平台](https://developers.weixin.qq.com/platform)并登录你的服务号。
2. 在**我的业务 > 公众号**页面，获取**开发者ID(AppID)**。
   ![Image=600x306](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/83d9a40ca3e84618ad20caa3fc11149e~tplv-goo7wpa0wc-topic.webp)   


## 步骤二：发布应用到微信服务号 {#0dacea28}

以下是将应用发布到微信服务号的详细步骤：

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部空间列表中选择目标工作空间。
3. 在**项目开发**页面，选择目标低代码应用，在应用编排页面右上角，单击**发布**。
4. 在发布页面填写版本信息：
   * **版本号**：必填，必须是一个应用从未设置过的新版本号。
   * **版本描述**：可选，说明该版本更新的内容。
5. 在 **选择发布平台 > 发布到通讯或社交平台** 选项，选择待发布的对话流。当用户在微信服务号发送消息时，将调用该对话流来接收用户消息。
6. 找到**微信服务号**发布渠道，单击**配置**。
7. 在 **AppID** 输入框内，填写微信服务号的开发者 ID，并单击**保存**。
   ![Image=544x407](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cefa0d2b5b8a446699ed475834650e2f~tplv-goo7wpa0wc-topic.webp)
8. 跳转到**公众平台账号授权**页面，使用公众平台绑定的管理员个人微信号扫描二维码。
   ![Image=602x275](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0b1d28b4d5a94bd4bfe8685a395f8f38~tplv-goo7wpa0wc-topic.webp)
9. 在微信移动端，根据页面提示选择服务号并确认授权。
   授权成功的页面提示如下：
   ![Image=203x367](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5d3fe1e9ebc84c38988fdc445ef1891f~tplv-goo7wpa0wc-topic.webp)
10. 返回应用发布页面，选中**微信公众号（服务号）​**发布平台，并设置发布记录后，单击页面右上角的**发布**。
   成功发布后，你可以前往微信服务号与应用对话。
