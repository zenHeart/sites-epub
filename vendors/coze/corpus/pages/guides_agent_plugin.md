> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

插件是一个工具集，一个插件内可以包含一个或多个工具（API）。

目前，扣子编程集成了类型丰富的插件，包括资讯阅读、旅游出行、效率办公、图片理解等 API 及多模态模型。使用这些插件，可以帮助你拓展低代码智能体能力边界。例如，在你的低代码智能体内添加新闻搜索插件，那么该智能体将拥有搜索新闻资讯的能力。

关于插件的详细介绍，请参考[插件介绍](/guides/plugin)。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 添加插件 {#ce046cb5}

插件可以直接在智能体内使用，拓展智能体的能力边界。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**创建** > **创建智能体**。
3. 根据页面提示，创建一个新智能体。
4. 在智能体编排页面的**技能** > **插件**区域，添加插件。
   支持通过以下方式添加插件：
   * **直接添加插件**：单击+图标，从工作空间或插件商店中挑选已发布的插件。如果没有合适的插件，也可以根据页面提示创建一个新的插件。
   * **自动添加插件**：单击自动添加图标，大模型会根据人设与回复逻辑，自动从商店中选择合适的插件添加到智能体中。
   :::tip 说明
   使用大语言模型自动添加插件后，建议调试智能体，检查被添加的插件是否可以正常使用。
   :::
5. 在**添加插件**页面，展开目标插件查看工具，然后单击**添加**。
   单击**资源库工具**，可查看资源库中可用的插件工具。
6. 在智能体的**人设与回复逻辑**区域，定义何时使用插件，然后在**预览与调试**区域测试插件功能是否符合预期。
   ![Image=447x294](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2888ec585ae34c3c92f60eb7f2e7797d~tplv-goo7wpa0wc-topic.webp)   


## 参数配置 {#95b4b08d}

在智能体中添加插件后，可以通过参数配置灵活设置参数的默认值及可见性。参数的默认值可有效避免大模型运行时因插件参数值缺失而导致的报错。同时，针对一些值较为稳定的参数，设置其默认值且隐藏其可见性可减少大模型的无效判断，从而提高插件调用效率。

### 使用场景 {#1306f310}

**场景 1：避免调用报错**

当用户与智能体交互时，如果未输入某些必要信息，而这些信息对于智能体中的大模型调用插件至关重要，那么在没有参数默认值时，大模型可能无法正常工作。例如在调用天气插件查询天气时，如果用户与智能体对话时未输入具体地域且对应的插件参数无默认值，那么智能体可能无法回答问题。如果为该参数设置了默认值（如杭州），即使用户未输入具体地域，大模型也会按照默认值进行调用，并返回答案，从而有效避免因参数值缺失导致的错误。

::::cols
@col 50
**未设置默认值**

* 参数配置
   ![Image=954x297](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fec40f2a48b34c0291f97311b3c8158a~tplv-goo7wpa0wc-topic.webp)
* 智能体问答
   大模型未能正常回复问题。
   ![Image=351x156](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1772da0973c04e55a029e62d835e24b0~tplv-goo7wpa0wc-topic.webp)

@col 50
**设置默认值**

* 参数配置
   ![Image=937x274](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/337bd97f353d496683a091cbe2f38da3~tplv-goo7wpa0wc-topic.webp)
* 智能体问答
   大模型使用默认值回复问题。
   ![Image=871x407](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5116b52d2d464e34b26c8f251e408001~tplv-goo7wpa0wc-topic.webp)
::::

**场景 2：参数值稳定**

某些插件参数值较为稳定，不需要动态传入参数值，则建议为参数设置默认值，并关闭**开启**开关（参数对模型不可见），减少智能体中的大模型调用插件时的流程，提高调用效率。例如在调用头条搜索插件时，如果只希望每次返回三条信息，不需要模型进行动态判断，则可以设置插件 `count` 参数的默认值为 3，且关闭**开启**开关（参数对模型不可见）。如果设置 `count` 参数默认值为 3，但打开**开启**开关（参数对模型可见），则大模型仍会根据自身的逻辑判断返回的信息数量。

::::cols
@col 50
* 参数配置
   ![Image=883x445](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d6a6294148064cb8b242ce37e7cb43ba~tplv-goo7wpa0wc-topic.webp)
* 智能体问答
   根据默认值，返回 3 条信息。
   ![Image=857x561](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/212880ff1c4b442c9398839e9f6a6fb1~tplv-goo7wpa0wc-topic.webp)

@col 50
* 参数配置
   ![Image=869x419](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ff5c23c8e56e40688d60969fe1b8abd7~tplv-goo7wpa0wc-topic.webp)
* 智能体问答
   虽然设置了默认值，但大模型仍自行判断了返回的信息数量，仅返回 2 条信息。
   ![Image=859x572](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f3a33e46be444d8fb26667e821acd5c3~tplv-goo7wpa0wc-topic.webp)
::::

### 操作步骤 {#77a0a13e}

1. 在指定插件右侧，单击**编辑参数**图标。
   ![Image=555x108](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1aa040644999476e9cdf6e172d50e64b~tplv-goo7wpa0wc-topic.webp)
2. 修改参数配置。
   * 默认值：设置参数的默认值。你可以输入固定值，或引用变量值，例如启用系统变量，并引用系统变量值。变量说明，请参考[变量](/guides/variable)。
   * 开启：打开开关，表示参数对大模型可见，大模型可以读取该参数；关闭开关，表示隐藏参数，大模型无法读取该参数。
      * 如果设置了参数默认值且打开**开启**开关，那么调用插件时，大模型会以该默认值为基础，但仍会根据自身的逻辑判断是否使用其他值。
      * 如果设置了参数默认值且关闭**开启**开关，那么调用插件时，大模型只会使用这个默认值。
         ![Image=602x148](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1679e4d6516a4674a9aa8bcdb42037c2~tplv-goo7wpa0wc-topic.webp)         


## 绑定卡片数据 {#5949a4cb}

添加到智能体的插件支持绑定消息卡片。绑定成功后，智能体以消息卡片的形式发送消息。

:::notice 注意
目前，消息卡片仅在豆包客户端、飞书客户端内生效。
:::

1. 在指定插件右侧，单击**绑定卡片数据**图标。
   ![Image=427x225](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1cef3267ba1d40b78cc980f492ad5191~tplv-goo7wpa0wc-topic.webp)
2. 在智能体**回复卡片配置**对话框，选择扣子编程提供的**官方卡片**，或创建自定义卡片。
   ![Image=428x223](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/59ac7083816a4b23b78acc8d1062476e~tplv-goo7wpa0wc-topic.webp)
3. 配置消息卡片后，卡片图标将会显示绿点。
   ![Image=449x122](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/839a26448b2746fab953ccf4975c2ae3~tplv-goo7wpa0wc-topic.webp)
4. 发布智能体，使配置生效。

## 删除插件 {#a563ec88}

你可以为智能体删除一个不需要的插件。

在指定插件的右侧，单击**移除**图标，即可删除添加到智能体中的插件。

![Image=475x312](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d6441fe82f4248888f53d8260cccd9d3~tplv-goo7wpa0wc-topic.webp)

## 常见问题 {#fd2c60cc}

### 智能体无法正常调用插件如何解决？ {#30b852da}

当智能体无法正常调用插件时，请参考如下步骤排查：

5. 确认大模型是否支持调用插件。
   在智能体中，大模型通过 Functioncall 能力调用插件或工作流，即你需判断所需的大模型是否支持 Functioncall 能力。
6. 确认提示词是否合理，是否明确表达了调用插件的意图及时机。
7. 对话里可正常提取插件的必选参数。

### 为什么豆包·角色扮演·Pro模型无法调用插件？ {#90e83529}

大模型通过 Functioncall 能力调用插件或工作流，而豆包·角色扮演·Pro模型暂不支持 Functioncall 能力。你可以使用豆包·工具调用模型，同时在提示词中明确描述插件调用场景。

### 为什么插件提示未授权？ {#0edde140}

OAuth 插件执行时需要通过 OAuth 方式获取用户授权，才能访问对应账号下的资源。在智能体或工作流节点中添加 OAuth 插件之后，智能体或工作流页面会提示**未授权**，你需要单击**未授权**，并根据页面提示完成授权，否则在当前页面调试智能体或试运行工作流时，插件会执行中断，引导你完成授权后才会继续执行。

对于绑定了 OAuth 插件的智能体，每个用户调用插件时都需要使用各自的账号授权。工作流中的 OAuth 插件节点支持设置共享授权模式，智能体或工作流发布后，用户使用插件时默认使用开发者账号进行授权，无需用户手动授权。

![Image=480x271](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c348d308a3424000b3d8be39d171a08f~tplv-goo7wpa0wc-topic.webp)

### 为什么无法添加扣子编程插件商店中的插件？ {#2ef6fdab}

如果在**添加插件**页面仅显示资源库工具和企业插件，未显示扣子编程插件商店中的插件，是因为企业超级管理员或管理员设置了**仅允许使用企业商店中的插件**，限制了对扣子编程插件商店的访问权限。

如需使用扣子编程插件商店中的相关插件，可联系企业超级管理员或管理员将对应插件添加至企业插件商店中，具体请参见[添加扣子插件商店中的插件](/guides/enterprise_plugin_store#73149c80)。

![Image=500x121](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7fba84eb42e74aa9bc524933a2b6e362~tplv-goo7wpa0wc-topic.webp)
