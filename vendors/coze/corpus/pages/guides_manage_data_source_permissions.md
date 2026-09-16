> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

从飞书、Notion 、微信公众号等渠道导入知识库文件时，需要数据源侧的授权，例如飞书账号授权扣子编程读取本账号的公开文档。授权后可以随时取消授权，也可以添加其他账号的授权。

## 添加授权 {#54d9a837}

参考以下操作，为知识库添加数据源侧的授权。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在左下角，单击头像，然后单击**账户设置**。
   ![Image=134x279](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fa22984bb50b4be28b315d7b5fe159fa~tplv-goo7wpa0wc-topic.webp)
3. 在**数据源**页面，找到需要授权的数据源，并单击其右侧的**授权**。
   ![Image=626x225](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/206be79595a44cc9bdec85e2eed98427~tplv-goo7wpa0wc-topic.webp)
   * 飞书授权：确认授权的飞书账号无误后，单击**授权**。
   * Notion 授权：单击**选择页面**，勾选允许扣子编程访问的页面，然后单击**允许访问**。
4. 授权后，即可在数据源中查看刚刚添加的账号。
   ![Image=624x246](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/46a590a0841341778c8bf6071c9a40f1~tplv-goo7wpa0wc-topic.webp)
   在知识库中添加内容时，也可以切换账号，选择另一个账号中的文档。
   ![Image=418x226](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/40be7d7c92ee4f24a8de3a8eaa28870b~tplv-goo7wpa0wc-topic.webp)   


## 移除授权 {#0943897b}

如果你不需要将飞书或 Notion 平台的文件导入到知识库，你可以移除相应的授权。

参考以下操作，移除授权：

1. 在**数据源**页面，将鼠标悬浮至需要移除授权的账号区域，然后单击其右侧的移除图标。
   ![Image=536x210](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/be065c1bf47140f9bfb3682ed0552e8b~tplv-goo7wpa0wc-topic.webp)
2. 在弹出的对话框中，单击**确认**。
   * 移除飞书账号：移除后，与该账号关联的文档将无法更新内容。
   * 移除 workspace：移除后，从该 workspace 导入和创建的 Units 的定期更新将被暂停，如要恢复，需要重新绑定更新同步到 workspace。
      你也可以勾选**同时删除已添加的文件和向量块**，然后单击**确认**，系统会删除该账号下已经导入到知识库的文件。
      ![Image=407x220](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a88aa64a6d6943258a2bc5821da94e45~tplv-goo7wpa0wc-topic.webp)
