> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

OAuth 是一种开放授权标准，允许第三方应用程序在用户授权的情况下访问用户存储在服务商的资源，而无需提供用户名和密码。如果服务支持 OAuth 认证，并且你希望在插件中集成该服务，你可以创建一个支持 OAuth 认证的插件。创建成功后，智能体需要通过 OAuth 授权流程来获取访问令牌，以便安全地调用集成到插件中的服务。

本文以扣子编程 API 为例，为你演示如何创建一个支持 OAuth 认证的插件。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 前提条件 {#8f5eedda}

请确保你已经在 API 服务平台创建了 OAuth 应用，并获取了客户端 ID、客户端密钥等信息，详情请参考 API 服务提供商的开发文档。

本示例以在插件中集成扣子编程 API 为例，因此需在扣子编程中创建 OAuth 应用，详情请参考[1 创建 OAuth 应用](/developer_guides/oauth_code#3fba3e8e)。在创建 OAuth 应用时，需注意如下事项：

* 先留空**重定向 URL** 配置。重定向 URL 需包含插件 ID，因此需先完成[步骤一：创建插件](/guides/oauth_plugin#f7bed311)，获取到插件 ID 后，再配置。
* 记录客户端 ID、客户端密钥。

![Image=504x192](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7ca896bb98cc468b9c3912a35b88b117~tplv-goo7wpa0wc-topic.webp)

## 步骤一：创建插件 {#f7bed311}

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 在页面右上角，选择 **+资源** > **插件**。
4. 填写插件基础信息。
   1. 输入插件名称和描述。
   2. 插件工具创建方式选择**基于已有服务创建**。
   3. 插件 URL：输入 API 的服务地址，例如 `https://api.coze.cn`。
   4. 将 API 的 Header 信息配置到 Header 列表中。
   5. 授权方式选择 **OAuth > standard**，然后配置 OAuth 参数。
      <!-- @cols-width: 142,604 -->
      | **配置**  | **说明**  |
      | --- | --- |
      | **client_id**  | 客户端 ID，是应用在授权服务器中的唯一标识符，授权服务器通过客户端 ID 来识别不同的三方应用。 | \
      | | | \
      | | 创建 OAuth 应用时会分配 **client_id**，本示例输入`813924812101982004357116497xxxx.app.coze`。  |
      | **client_secret**  | 客户端密钥，和客户端 ID 配合使用，用于认证应用的身份，确保只有被授权的应用可以请求授权。 | \
      | | | \
      | | 创建 OAuth 应用时会分配 **client_secret**，本示例输入`8jmSA1wi********`。  |
      | **client_url**  | 服务方的 OAuth 页面URL，用于拼接用户登录授权页的URL。 | \
      | | | \
      | | 用户登录插件时，扣子编程会将用户引导至`[client_url]?response_type=code&client_id=[client_id]&scope=[scope]&state=xyz123&redirect_uri=[coze平台的回调安全地址]`。 | \
      | | | \
      | | 参考服务方的授权文档获取 **client_url** ，本示例参考扣子编程开发指南文档，输入`https://www.coze.cn/api/permission/oauth2/authorize`，详情请参考[2 获取访问令牌](/developer_guides/oauth_code#6c13ead3)。  |
      | **scope**  | 允许应用程序请求访问用户数据的范围。 | \
      | | | \
      | | 参考服务方的授权文档输入 **scope。**  |
      | **authorization_url**  | 获取用户 access token 的 URL 地址。 | \
      | | | \
      | | 用户通过`client_url`授权成功后，三方服务会返回用于获取 token 的 code，并跳转至回调地址。此时，服务提供方会通过对应参数向`authorization_url`发起请求，获取用户的access_token。 | \
      | | | \
      | | 参考服务方的授权文档获取 **authorization_url**，本示例参考扣子编程开发指南文档，输入`https://api.coze.cn/api/permission/oauth2/token`，详情请参考[2 获取访问令牌](/developer_guides/oauth_code#6c13ead3)。  |
      | **authorization_content_type**  | 向 OAuth 提供者发送数据的内容类型，目前支持： | \
      | | | \
      | | * （默认）`application/json` | \
      | | * `application/x-www-form-urlencoded`  |
      ![Image=367x453](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c889779628334ce6af31f19c0eb2059d~tplv-goo7wpa0wc-topic.webp)
5. 单击**未授权**，然后单击**确认。**
   ![Image=515x288](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1ef248e69e0a41c4bd59ea29fa47c067~tplv-goo7wpa0wc-topic.webp)
6. 在授权页，单击**授权**即可完成 OAuth 授权。
   ![Image=324x428](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/aebed71f4425467d8a736823753d7e8d~tplv-goo7wpa0wc-topic.webp)   


授权成功后，无论是插件调试还是与智能体对话，每次请求调用插件时，用户授权的 access_token 都会在 header 中传递，具体传递内容为：`"Authorization":"[Bearer] [user's access_token]"`。

## 步骤二：配置 OAuth 应用的重定向 URL {#24582cdd}

创建插件后，你需要获取插件 ID，用于配置 OAuth 应用的重定向 URL。

1. 获取插件 ID。
   在插件详情页面的 URL 中，获取插件 ID。
   ![Image=559x91](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/50007d8c5d874441ac54fccc22978bff~tplv-goo7wpa0wc-topic.webp)
2. 返回[OAuth 应用](https://www.coze.cn/open/oauth/apps?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)页面，单击目标 OAuth 应用对应的**编辑**。
3. 输入重定向 URL，单击**确定**。
   重定向 URL 格式为`https://www.coze.cn/api/plugin_oauth/753316160413368****/authorization_code` ，其中 `753316160413368**** `为插件 ID，需替换为你在步骤 1 中获取到的插件 ID。
   ![Image=481x339](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2a3c301ab4db40a48d81d7b1c514af13~tplv-goo7wpa0wc-topic.webp)   


## 步骤三：创建工具 {#83f0d532}

创建插件后，还需要创建工具，以实现将目标 API 添加到插件中作为工具使用。具体操作，请参考[步骤二：添加工具](/tutorial/build_a_agent_query_plugin#7c97d26d)。

下图以扣子编程的[查看智能体列表](https://www.coze.cn/docs/developer_guides/published_bots_list) API 为例，展示了工具的配置示例。配置完成后，需单击右上角的**试运行**。只有当添加的工具试运行通过后，才能发布插件。

![Image=627x344](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/08753a83316543b389932490735681b5~tplv-goo7wpa0wc-topic.webp)

## 步骤四：发布插件 {#b94606a4}

发布 OAuth 插件。插件发布后，才可以被智能体使用。具体操作，请参考[步骤三：发布插件](/tutorial/build_a_agent_query_plugin#e9051250)。

![Image=631x131](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f3520163f5094d89b53acb2f80ee36c5~tplv-goo7wpa0wc-topic.webp)

## 授权配置 {#20877d71}

你在低代码智能体、工作流中使用 OAuth 插件时，需要完成授权操作，以确保智能体或工作流在调用 OAuth 插件时可以正常运行。详细说明，请参考[为什么插件提示未授权？](/guides/agent_plugin#0edde140)、[如何设置 OAuth 插件的授权模式？](/guides/plugin_node#79ba9ce6)。
