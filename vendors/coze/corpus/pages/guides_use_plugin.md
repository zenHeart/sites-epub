> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

插件可以直接在低代码智能体内使用，拓展智能体的能力边界。插件也可以作为节点添加到工作流，执行一个操作。

:::tip 说明
* 仅扣子付费套餐用户可使用三方付费插件。
* 添加了三方付费插件的低代码智能体或应用（工作流），不支持发布到飞书多维表格、掘金、豆包及部分公共渠道。
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 为低代码智能体绑定插件 {#a6f33b3b}

可以将插件添加到低代码智能体内，扩展智能体的能力。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**项目开发**。
3. 单击指定的低代码智能体。
4. 在智能体编排页面的**技能** > **插件**区域，添加插件。
   支持通过以下方式添加插件：
   * **直接添加插件**。单击+图标，从工作空间或插件商店中挑选已发布的插件。如果没有合适的插件，也可以根据页面提示创建一个新的插件。
   * **自动添加插件**。单击自动添加图标，大模型会根据人设与回复逻辑，自动从商店中选择合适的插件添加到智能体中。
   :::tip 说明
   使用大语言模型自动添加插件后，建议调试智能体，检查被添加的插件是否可以正常使用。
   :::
5. 在**添加插件**页面，搜索并展开目标插件，单击目标工具对应的**添加**。
   支持从插件商店中添加扣子编程官方插件或三方插件，也支持从当前工作空间的资源库中添加已发布的自定义插件。
   首次添加某个三方付费插件时，系统将弹出插件开通提示框。确认开通后，才能使用该三方付费插件。
   ![Image=388x202](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8538b99daf0c4a84b221386a373776f1~tplv-goo7wpa0wc-topic.webp)
6. 在智能体的**人设与回复逻辑**区域，定义何时使用插件，然后在**预览与调试**区域测试插件功能是否符合预期。
   ![Image=427x305](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fa26b8b67af0431ebccd9e4c00607bb8~tplv-goo7wpa0wc-topic.webp)   


## 为低代码工作流添加插件节点 {#2acbb7f6}


1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 单击指定的低代码工作流。
4. 在工作流的编排页面中，选择**添加节点** > **插件**。
   ![Image=304x323](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5dd1bf3541d149b8aa106038a064acae~tplv-goo7wpa0wc-topic.webp)
5. 搜索并展开目标插件，单击目标工具对应的**添加**。
   支持从插件商店中添加扣子编程官方插件或三方插件，也支持从当前工作空间的资源库中添加已发布的自定义插件。
   首次添加某个三方付费插件时，系统将弹出插件开通提示框。确认开通后，才能使用该三方付费插件。
   ![Image=388x202](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8538b99daf0c4a84b221386a373776f1~tplv-goo7wpa0wc-topic.webp)
6. 在工作流的画布内，连接插件节点，并配置插件的输入参数来源。
   ![Image=636x192](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/16f33cbc17f748cdb1da85db1dd6b1be~tplv-goo7wpa0wc-topic.webp)   


## 在对话中使用插件 {#b3f96710}

对于工作流中绑定的插件节点，你在配置工作流时已设置了插件的输入参数来源，当对话触发工作流运行时，扣子编程会根据工作流的配置逻辑自动调用插件节点，完成工作流。对于直接绑定智能体的插件，智能体会根据对话内容自动判断何时调用插件回答用户的问题，并从用户 Query 中提取插件的输入参数，如果 Query 中未包含所有的必选参数，智能体会追问用户直到获得所有的必选参数。

![Image=527x290](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b54a0004cd414b5ea0547f75d975a4e0~tplv-goo7wpa0wc-topic.webp)

为了提高插件调用时机的准确性，建议在**人设与回复逻辑**区域明确定义插件的使用场景，从而减少因模型回复随机性导致的插件调用不符合预期的情况。

![Image=790x349](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1d1a32eca3a04f0b9abf12591161fee0~tplv-goo7wpa0wc-topic.webp)

## 扩容插件 QPS {#fd75b39b}

针对已开通且支持扩容的三方付费插件及部分官方插件，扣子编程提供付费扩容服务。你可以根据业务需求，在**扩容管理**页面，找到目标插件申请扩容。

* 官方插件：根据页面提示填写并发数量，即可完成扩容。
* 三方付费插件：根据页面提示添加并发数量后，需等待插件开发者审核通过，才能完成扩容。

详细说明，请参考[资源扩容费用](/coze_pro/resource_expansion_fee)。
