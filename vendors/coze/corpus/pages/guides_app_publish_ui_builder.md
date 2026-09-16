> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子 Web SDK 是一个功能强大的 JavaScript 库。开发者发布低代码应用后，扣子会将低代码应用中的用户界面和工作流打包发布到 Web SDK，方便开发者将其无缝嵌入到各类业务系统中，快速实现界面集成，适用于需要将应用界面嵌入到内部系统或第三方平台等场景。本文介绍如何将已开发的低代码应用发布到 Web SDK。

## 前提条件 {#208f2039}

* 待发布的应用至少包含一个对话流，且已配置用户界面。
* 用户界面仅支持网页端，不支持小程序端。小程序端界面不支持发布为 Web SDK。
* 在发布前已[创建个人令牌](https://www.coze.cn/open/oauth/pats?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)，或实现了 OAuth 鉴权逻辑。详细说明可参考[鉴权方式概述](/developer_guides/authentication)。
* 发布者必须拥有发布权限，即发布者必须是应用的所有者或协作者。详细说明可参考[多人协作开发低代码应用](/guides/collaborate_app)。

## 将应用发布到 Web SDK {#f41e373a}

以下是将低代码应用发布为 Web SDK 的详细步骤：

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部空间列表中选择目标工作空间。
3. 在**项目开发**页面，选择目标低代码应用。
4. 在应用编排页面的右上角，单击**发布**，在发布页面填写版本信息：
   * **版本号**：必填，版本号用于区分不同发布版本，确保应用更新的可追溯性。
   * **版本描述**：可选，说明该版本更新的内容，以便快速了解版本变更内容。
5. 在**选择发布平台** > **API 或 SDK** 区域，选择 **Web SDK** ，单击**发布**。
   ![Image=600x451](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8fbd7d0d8a874f0986e62ba253d94d6f~tplv-goo7wpa0wc-topic.webp)
   发布完成后，你可以应用编排页面的**版本记录**中查看指定版本的发布结果。请注意应用审核需要一定的时间，请耐心等待。
   ![Image=500x268](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/faaf483622ea4cb598f597748d624da5~tplv-goo7wpa0wc-topic.webp)   


## 使用 Web SDK {#d6604bac}

你可以在[扣子 Playground 的 UI Builder](https://www.coze.cn/open/playground/uibuilder?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=) 页面体验 Web SDK 的使用效果。安装和使用 Web SDK 的详细方法请参见[Web SDK（低代码）](/developer_guides/ui_builder_web_sdk)。

## 撤销发布 Web SDK {#99da5cdb}

如果不再需要通过 Web SDK 方式使用扣子应用，可以在发布页面撤销发布到 Web SDK。撤销后，调用 Web SDK 时会收到错误提示。

撤销发布的详细操作步骤如下：

1. 在应用编排页面右上角单击**发布**，进入应用发布页面。
2. 在**选择发布平台** > **API 或 SDK** 区域，单击 **Web SDK** 卡片中的**撤销发布**。在弹出的对话框中，单击**撤销发布**。
   ![Image=500x310](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e84559f90d374f9c8cf5280ace9cd0a9~tplv-goo7wpa0wc-topic.webp)
   撤销发布操作立即生效。撤销后，发布历史中显示的历史版本发布状态不会变更，但是应用会与 Web SDK 解绑。你将无法通过调用 Web SDK 的方式与应用交互。
