> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程提供了代码解析器，支持解析 API 配置文件来创建插件。创建插件后，必须发布插件才可以被低代码智能体使用。

:::tip 说明
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
* 个人工作空间中的插件，仅能被个人调用；企业工作空间中插件，能被任意企业成员调用。
* 插件发布了新版本后，使用了这个插件的低代码智能体会自动使用发布的最新版本。
:::

## 操作步骤 {#3bb2b444}

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 在页面右上角，选择 **+资源** > **插件**。
   ![Image=504x170](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/013e73be30ef4768a3432e8017d9c325~tplv-goo7wpa0wc-topic.webp)
4. 在页面右上角单击代码图标。
   ![Image=458x209](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/845b3b548450462aa02fef225fc41c38~tplv-goo7wpa0wc-topic.webp)
5. 完成以下配置，然后单击**确认**。
   1. 在左侧面板中以 JSON 格式填入插件的配置信息。
   2. 在右侧面板中以 YAML 格式填入 API 的配置信息。
6. 在插件页面，进入插件详情页查看已创建的 API 工具。单击已创建的 API 进行调试。
   ![Image=452x118](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/227592c2e508429d8c251be5db29fd90~tplv-goo7wpa0wc-topic.webp)
7. 检查 API 配置，在**调试与校验**页面，单击编辑工具，输入请求参数，然后单击**运行**查看 API 是否可以成功调用。
8. 如果 API 调用成功，单击**完成**。如果 API 调用失败，根据错误信息修改 API 配置，直至 API 调试成功。
   ![Image=469x248](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4fa0f7d08f284c9397f749ec25013608~tplv-goo7wpa0wc-topic.webp)
9. 在插件详情页的右上角，单击**发布**。

## 上架到商店 {#900d35b8}

你可以将插件上架到扣子插件商店或企业插件商店。不能同时上架扣子插件商店和企业插件商店，仅支持选择其中一个渠道。

* **上架扣子插件商店**
   对于通用功能、不涉及敏感数据且具有广泛适用性的公开插件，你可以将其上架到扣子商店，以便更多扣子用户发现、使用。详情请参考[将插件上架到插件市场](/guides/publish_plugin_to_store)。
* **上架企业插件商店**
   仅企业旗舰版支持。
   对于企业自主开发的涉及核心业务逻辑、数据敏感信息或仅限内部场景使用的插件，你可以将其上架到企业插件商店，供企业成员使用。详情请参考[管理企业插件](/guides/enterprise_plugin_store)。
