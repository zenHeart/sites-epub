> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

企业旗舰版支持企业插件商店，你可以将外部插件或企业开发的自定义插件添加至企业插件商店，以便企业成员使用，还可以设置是否仅允许使用企业插件商店中的插件。

:::tip 说明
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
* **套餐限制**：仅企业旗舰版支持企业插件商店。
:::

## 功能简介 {#31193f23}

企业插件商店是企业专属的插件管理与分发中心。通过企业插件商店，企业可以集中管控插件来源，确保企业成员使用的插件安全合规，其核心优势包括：

* **内部插件分发，保护企业敏感信息**
   对于企业自主开发的自定义插件，如涉及核心业务逻辑、数据敏感信息或仅限内部场景使用的工具，无需上架至扣子插件商店，可直接通过企业插件商店进行内部分发。既能避免内部资源外泄，保护企业知识产权与数据隐私，又能让企业成员便捷使用内部服务，提升协作效率。
* **外部插件管控**
   企业可从扣子插件商店中筛选所需的外部插件，添加至企业插件商店。确保所有外部插件均经过安全合规校验，避免未经管控的外部插件可能导致的数据泄露风险。   


## 管理企业插件商店中的插件 {#ba1fe942}

### 上架自定义插件 {#48000d35}

插件所有者可以将资源库中已发布的自定义插件上架到企业插件商店，以便企业成员使用该插件。

:::tip 说明
* **操作权限**：仅插件所有者可以上架企业插件。
* 同一自定义插件不可同时上架至扣子插件商店和企业插件商店。
:::

在[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)左侧导航栏单击**企业插件**，在右上角单击**上架插件**，选择对应的工作空间和已发布的自定义插件。

![Image=600x347](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3eef17ff1c1748afa5818bd8abc2885b~tplv-goo7wpa0wc-topic.webp)

### 添加扣子插件商店中的插件 {#73149c80}

当企业开启**仅允许使用企业商店中的插件**开关后，为确保企业成员能够安全、合规地使用外部插件，企业超级管理员和管理员可以将扣子插件商店中的插件添加到企业插件商店中，以便企业成员在低代码智能体或工作流中添加该外部插件。

:::tip 说明
**操作权限**：企业超级管理员和管理员。
:::

在[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)左侧导航栏选择**插件商店**，单击目标插件，在插件详情页面右上角选择… > **添加到企业商店**。

![Image=600x212](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b36636551a4d42b49b60bb19d405feab~tplv-goo7wpa0wc-topic.webp)

### 将插件从企业插件商店下架 {#811e460d}

若企业插件商店中的插件存在问题，不希望被继续使用，你可以将其从企业插件商店下架，避免企业成员添加该插件。

:::tip 说明
* **操作权限**：
   * 企业超级管理员和管理员可下架企业插件商店中所有插件。
   * 插件所有者可下架本人的插件。
* **操作影响**：下架后，企业成员无法看到该插件。对于已添加该插件的智能体或工作流，其已发布版本不受影响，可继续使用。
:::

1. 在[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)左侧导航栏单击**企业插件**，在企业插件商店页面，单击右上角的**管理**。
2. 选择目标插件，单击**下架所选插件**。
   ![Image=500x308](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/341e06a933be4677bb2ecf6d647c9907~tplv-goo7wpa0wc-topic.webp)   


## 设置仅允许使用企业商店中的插件 {#948a18f1}

扣子编程默认允许使用扣子插件商店中的插件。为保障企业数据安全，防范外部插件可能带来的数据泄露风险，企业可根据需要配置仅允许使用企业插件商店中的插件，严格管理企业的插件来源，确保企业成员只能使用已添加至企业插件商店中的插件。

:::tip 说明
**操作权限**：企业超级管理员和管理员。
:::

1. 企业超级管理员或管理员登录[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
2. 在左下角单击个人头像，选择**企业账号**> **企业管理**。
   ![Image=272x263](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0eb73c4ced114017846afa1763ddf185~tplv-goo7wpa0wc-topic.webp)
3. 在左侧导航栏中，单击**企业成员管理**，然后在顶部选择**成员权限**。
4. 根据需求开启或关闭**仅允许使用企业商店中的插件**。
   * **开启开关**：仅允许使用企业商店中的插件。
      开启后，企业成员将仅可使用企业插件商店内的插件。对于已使用扣子插件商店中插件的智能体或工作流，其线上已发布的版本将不受影响，可继续正常使用。
   * **关闭开关**：允许使用扣子插件商店中的插件。
      ![Image=636x330](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/360100bc2f014b779c7768683df3d5b1~tplv-goo7wpa0wc-topic.webp)      


##  {#2032309d}

