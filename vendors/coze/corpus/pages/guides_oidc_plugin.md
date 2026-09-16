> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

OIDC 是一种广泛使用的授权框架，它基于 OAuth 2.0 协议之上，提供了身份验证和授权的功能。本教程介绍扣子编程插件如何与 Google Cloud Platform（GCP）集成，实现安全访问 GCP Cloud Storage Bucket。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 前置条件 {#13c0517b}

你已经创建了一个非公开访问的 Bucket，本教程 Bucket 名称设置为 **coze-plugin-oidc-test**，详情可参考 [Create buckets](https://cloud.google.com/storage/docs/creating-buckets)。

![Image=2555x372](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f162ce1eca0f4554a74faea47fffdda1~tplv-goo7wpa0wc-topic.webp)

## 步骤一：配置工作负载身份联合 {#14ad1be4}

借助 Workload Identity，你的工作负载无需服务账号密钥即可访问 Google Cloud。

1. 登录 [Google Cloud 的 IAM&Admin 控制台](https://console.cloud.google.com/iam-admin/iam)。
2. 在左侧导航栏，单击 **Workload Identity Federation**，然后单击 **GET STARTED**。
3. 创建身份池，使用池来管理外部身份，然后单击 **CONTINUE**。
   * Name：自定义池的名称，本教程输入 **coze-plugin-federation**。
   * Pool ID：输入池的 ID，本教程 ID 与 Name 设置一致。
   * Description：添加池的描述。
   * Enabled Pool：选择启用池。
      ![Image=638x275](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5b7b824b0bb542919123d30a972bd64e~tplv-goo7wpa0wc-topic.webp)
4. 向池添加提供方，提供方可管理和验证身份，然后单击 **CONTINUE**。
   * Select a provider：选择与你的外部身份源匹配的提供商类型，本教程选择 **OpenID Connection（OIDC）**。
   * Provider name：配置提供商名称，本教程输入**coze-cn**。
   * Issuer (URL)：配置颁发者网址，必须以 https:// 开头，本教程输入 [https://api.coze.cn](https://api.coze.cn)。
      ![Image=642x277](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/367dcd5d80fb4cdc9c07ca25acb25711~tplv-goo7wpa0wc-topic.webp)
      在 **Audiences -> Default audience**，复制 URL，在扣子编程插件配置中需要使用该 URL。
      ![Image=648x279](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b00abe5cf9704a0991ad803f0f5b86f8~tplv-goo7wpa0wc-topic.webp)
5. 配置提供方属性，本教程输入 **assertion.sub**。
   ![Image=654x282](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/def337235d1042cd8e4ea42ddae73b29~tplv-goo7wpa0wc-topic.webp)
6. 单击**Save**，在池详细信息页，复制并保存 IAM principal，配置访问控制策略时会使用 IAM principal的值。
   ![Image=657x283](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2044aee745a943efb8a7c90973c74a32~tplv-goo7wpa0wc-topic.webp)   


## 步骤二：配置 OIDC 插件 {#64842551}

OIDC 是一种广泛使用的授权框架，它基于 OAuth 2.0 协议之上，提供了身份验证和授权的功能。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 在页面右上角，选择 **+资源** > **插件**。
4. 配置插件信息并单击**确认**。
   1. 设置基础信息。
      <!-- @cols-width: 231,584 -->
      | **配置项**  | **说明**  |
      | --- | --- |
      | 插件图标  | 单击默认图标后，您可以上传本地图片文件作为新的图标。  |
      | 插件名称  | 自定义插件名称，用于标识当前插件。建议输入清晰易理解的名称，便于大语言模型搜索与使用插件。  |
      | 插件描述  | 插件的描述信息，一般用于记录当前插件的用途。  |
      | 插件工具创建方式  | 本教程选择**基于已有服务创建**。  |
      | 插件 URL  | 插件的访问地址或相关资源的链接，本教程输入 Google Cloud Storage 的默认域名`https://storage.googleapis.com`。 | \
      | | | \
      | | :::tip 说明 | \
      | | 插件 URL 必须为域名格式，暂不支持 IP 格式的 URL 地址。 | \
      | | ::: | \
      | | | \
      | |   |
      | Header 列表  | HTTP 请求头参数列表。您需要根据 API 自身的参数配置要求来填写。  |
   2. 选择授权方式，本教程选择 **Service** > **OAuth 2.0 & OIDC**。
      配置参数说明如下：
      <!-- @cols-width: 144,649 -->
      | **配置项**  | **说明**  |
      | --- | --- |
      | grant_type  | 根据 GrantType 来选择使用的 OAuth Flow，支持的 Flow 包括： | \
      | | | \
      | | * TokenExchange：用于在不同服务之间交换令牌。 | \
      | | * ClientCredential：用于客户端凭据授权流程，适用于没有用户直接参与的情况。 | \
      | | | \
      | | 本教程选择 **TokenExchange**。  |
      | endpoint_url  | 授权服务器的端点 URL，用于发送授权请求和接收响应。配置时需要指定授权服务器的地址，以便客户端可以正确地向服务器发起请求。 | \
      | | | \
      | | 本教程输入 Google Cloud 的 Security Token Service（STS）API 的端点URL：[https://sts.googleapis.com/v1/token](https://sts.googleapis.com/v1/token)。  |
      | audience  | 资源服务器，客户端告诉授权服务器它希望代表用户访问哪个资源服务器。配置时需要指定资源服务器的标识符。 | \
      | | | \
      | | 本教程，输入步骤一中从 **Audiences -> Default audience** 复制的值。 | \
      | | | \
      | | ![Image=300x129](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b00abe5cf9704a0991ad803f0f5b86f8~tplv-goo7wpa0wc-topic.webp)  |
      | scope  | 客户端请求的权限范围。对于 OIDC，通常需要包含`openid`作用域，以请求身份验证，配置时需要根据需要请求的权限范围来设置。 | \
      | | | \
      | | 本教程输入 [https://www.googleapis.com/auth/devstorage.read_only](https://www.googleapis.com/auth/devstorage.read_only)，更多 GCP OAuth 权限点请参考 [Google文档](https://developers.google.com/identity/protocols/oauth2/scopes?hl=zh-cn)。  |
      | client_id  | 客户端在授权服务器注册时获得的唯一标识符，配置时需要使用在授权服务器注册应用时获得的 client_id。 | \
      | | | \
      | | 本教程无需配置 client_id。  |
      ![Image=303x630](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6464ffe89916405d96be05dda5a78119~tplv-goo7wpa0wc-topic.webp)      


## 步骤三：配置插件工具 {#86221134}

参考以下操作，配置插件工具：

1. 在已创建的插件页面，单击**创建工具**。
2. 在**创建工具**页面，配置基本信息，然后单击**确定**。
   * 工具名称：用于标识当前工具。建议输入清晰易理解的名称，便于后续大语言模型搜索与使用工具。
   * 工具描述：工具的描述信息，一般用于记录当前工具的用途。
3. 在**更多信息**区域，单击**编辑**，配置工具路径和请求方法，然后单击**保存**。
   * 工具路径：输入 API 路径。本教程API路径设置为 [https://storage.googleapis.com/storage/v1/b/coze_plugin_oidc](https://storage.googleapis.com/storage/v1/b/coze_plugin_oidc)。
   * 请求方法：参数传入方法，本教程选择 **Get 方法**。
4. 在**配置输入参数**区域，配置工具的输入参数。
   本教程不配置输入参数。
5. 在**配置输出参数**区域，配置工具的输出参数，然后单击**保存**。
   本教程新增一个名称为 **name** 的参数，以获取 Bucket 的 名称。
   ![Image=603x265](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/edc6247ae90c409ab4c80f4128c5ea16~tplv-goo7wpa0wc-topic.webp)   


## 步骤四：配置访问控制策略 {#46e2fffa}

配置 Bucket 访问控制策略，实现步骤一中配置的 Provider 能够访问对应的 Bucket。

1. 登录 [Google Cloud 的 Cloud Storage 控制台](https://console.cloud.google.com/storage/overview;tab=overview?hl=EN&inv=1&invt=AbjvEw&orgonly=true&project=coze-plugin-oidc-test-444309&supportedpurview=project)。
2. 在左侧导航栏，单击 **Buckets**，然后单击 **PERMISSIONS -> GRANT ACCESS。**
3. 添加访问控制权限，然后单击 **SAVE**。
   在 **Add Principals** 填写步骤一中复制的 **IAM principal**，并根据以下规则调整 `SUBJECT_ATTRIBUTE_VALUE` ：
   ```Plain Text
   // account_id: coze 账号 ID，这个账号必须是 workspace owner 的账号 ID
   // workspace_id: 空间 ID
   // plugin_id: 插件 ID
   acct:${account_id}/ws:${workspace_id}/pln:${plugin_id}
   ```
   ![Image=610x304](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d2e4c8db125b4f2a9685491cbd0d1baa~tplv-goo7wpa0wc-topic.webp)   


## 步骤五：调试插件 {#ca1f2511}

完成上述所有配置，在扣子编程插件页面进行试运行，测试能够获取 Bucket 的名称。

1. 在**编辑工具**页面，单击**试运行**。
   ![Image=396x115](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9587b6f77e314a09b1cb49b2303925e4~tplv-goo7wpa0wc-topic.webp)
2. 在**试运行**页面，单击**运行**。
   本教程无需配置输入参数。若在 `Response` 页签中成功返回 Bucket 名称，即表示创建工具成功。
   ![Image=613x415](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/23c09a5b7c8c4ce1bc795fea0d734aae~tplv-goo7wpa0wc-topic.webp)
   ##     {#81e19e9e}   

