> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

对于智能体应用市场、手机厂商等业务逻辑较为复杂的场景，渠道侧通常支持渠道用户管理自己在扣子编程中搭建的智能体，例如支持用户在渠道中查看自己的智能体列表、查看智能体的基础信息、将智能体开放给其他渠道用户使用等。这些行为通常由渠道侧调用扣子编程 OpenAPI 实现，但需要打通渠道侧的账号体系，将智能体开发者在扣子编程的 ID 与其在渠道中的 ID 关联。

在这种场景下，渠道入驻时应接收扣子编程的消息回调，并在渠道侧服务端配置 OAuth 鉴权流程，允许扣子编程获取开发者在渠道中的用户 ID。开发者将智能体发布到渠道中时，扣子编程会同时发送一条包含开发者扣子编程 ID 和渠道用户 ID 的消息回调到渠道指定的回调地址。渠道服务端根据这条消息回调可以识别出指定渠道用户对应的智能体 ID，在渠道平台中维护这种绑定关系、以渠道用户身份管理智能体、提供智能体对话服务。

该方案适用于渠道侧开发者多人共建、协同开发的场景，渠道侧的用户需要以自己的身份而不是渠道平台侧的身份维护自己的智能体。

## 对接流程 {#0237f550}

![Image=600x221](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6bdfe0025543482eb264db07c2036cab~tplv-goo7wpa0wc-topic.webp)

## 步骤一：渠道管理员配置 JWT 授权流程 {#6441d758}

创建一个渠道类型的 OAuth 应用，并在渠道侧实现 JWT 的授权流程、具备获取 OAuth Access Token 的能力。

创建 OAuth 应用并实现 JWT 授权的流程可参考[OAuth JWT 授权（渠道场景）](/developer_guides/oauth_jwt_channel)。

## 步骤二：渠道管理员添加发布渠道 {#debea935}

渠道管理员应在扣子编程中添加一个发布渠道。发布渠道是智能体发布到的目标平台，完成渠道入驻的所有配置之后，平台用户可以在平台中和智能体对话。添加发布渠道的本质是在扣子中填写平台相关的配置及权限。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面左下角单击用户头像，并选择**账号设置**。
3. 在**设置**页面的左侧导航栏选择**发布渠道** 。
   ::::tabs
   @tab 企业版
   在**企业自定义渠道管理**页面单击**添加平台。**
   
   ![Image=500x252](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/58dcf7f11f9d492ea30b7e33bb6c748b~tplv-goo7wpa0wc-topic.webp)
   
   @tab 个人版
   在**我的渠道管理**页面单击**添加平台**。
   
   ![Image=500x255](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2e08f8be67f44b0582c25b29e8de78ce~tplv-goo7wpa0wc-topic.webp)
   ::::
4. 填写目标渠道的配置。
   <!-- @cols-width: 157,547 -->
   | **配置**  | **说明**  |
   | --- | --- |
   | 图标  | 自定义渠道提供一个默认图标，单击渠道图标可更换一个图标。  |
   | 平台名称  | 自定义渠道的名称，将显示在智能体的发布页面。  |
   | 描述  | 渠道的描述信息，在智能体的发布页面中 hover 展示。  |
   | 绑定 OAuth 应用  | 为自定义渠道绑定一个 OAuth 应用。 | \
   | | | \
   | | 自定义渠道通过扣子 OpenAPI 接入扣子并使用智能体，调用 OpenAPI 时通过 OAuth 鉴权方式获取 OAuth Access Token。为渠道绑定 OAuth 应用后，这个 OAuth 应用生成的 OAuth Access Token 将拥有所有发布到此渠道的智能体的操作权限。具体的操作权限可参考此 OAuth 应用中选择的权限列表。  |   


::::cols
@col 50
```Plain Text
  配置示例：
  ![Image=300x324](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/81b92fa825f042edaa108488c2a554a2~tplv-goo7wpa0wc-image.image)
```

@col 50
配置效果：

![Image=400x141](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/dc067e53542a4ed9b3bdb03e8a126b09~tplv-goo7wpa0wc-topic.webp)
::::

5. 单击**确认**。

## 步骤三：渠道管理员配置渠道授权 {#144eb84a}

在本方案中，扣子编程服务端需要获取扣子用户在渠道中的身份信息，即扣子开发者在渠道中的用户 ID。所以渠道服务端应作为 OAuth Server，在扣子编程请求授权时，为其授予获取用户身份信息的权限。授权后，每次智能体开发者发布智能体到此渠道时，扣子编程会同步发送一条携带渠道用户 ID 的回调信息到渠道指定的回调地址。

授权流程如下：

![Image=420x377](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/517b4a6fb86b43c4b09c461fe636ea0b~tplv-goo7wpa0wc-topic.webp)

授权步骤如下：

1. 实现 OAuth Server 授权服务。
   渠道端应具备 OAuth Server 的能力，面向扣子服务端提供 OAuth 授权服务。在扣子编程服务端请求授权时，为其授予获取用户身份信息的权限。
   授权流程应为标准的 OAuth2.0 授权码（code）授权流程。
   1. 扣子编程向跳转地址发送一条格式固定的授权请求。
      跳转地址也就是渠道侧提供的 OAuth2.0 授权地址。跳转地址的协议可参考[跳转地址](/dev_how_to_guides/configure_custom_channel2#4108c744)。智能体开发者首次发布到这个渠道前，需要完成授权，允许扣子编程以用户身份获取自己的用户 ID。开发者单击授权时，智能体发布页面将会跳转至这个地址。
   2. 在用户单击授权后，渠道侧将授权页重定向到扣子的 REDIRECT_URI，并向扣子编程服务端返回 code。
      此重定向请求的参数协议可参考[跳转到扣子 Coze REDIRECT_URI](/dev_how_to_guides/configure_custom_channel2#f22a228a)。
   3. 扣子编程服务端调用渠道侧 API 获取 token，根据 code 请求获取 access_token。
      扣子编程服务端向渠道侧[获取 token](/dev_how_to_guides/configure_custom_channel2#0a99a55e)接口发送获取 access_token 的请求，请求中携带 code 参数。
   4. 渠道侧鉴权后，提供 access_token。
      渠道侧完成 OAuth 鉴权，生成 access_token，并在获取 token 接口 Response 中返回给扣子编程服务端。扣子编程服务端拿到这个 access_token 后，就可以调用渠道侧的 API [获取用户信息](/dev_how_to_guides/configure_custom_channel2#a9e30ad7)，从接口响应中获取用户信息。
2. 配置渠道授权。
   在渠道侧实现这一套 OAuth Server 授权服务后，渠道管理员应在扣子编程中配置渠道鉴权，将 OAuth 授权流程中的相关接口地址上传到扣子编程。后续触发授权时，扣子编程会根据授权码（code）授权流程向渠道侧申请授权。配置渠道授权的操作流程如下：
   1. 登录扣子编程。
   2. 在页面左下角单击用户头像，并选择**账号设置**。
   3. 在**发布渠道** > **企业自定义渠道管理**页签中找到步骤二中添加的平台。
   4. 在平台对应的 OAuth 一列中单击配置图标。
      ![Image=500x270](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2d384967ddc447289d0fe147616ec4e9~tplv-goo7wpa0wc-topic.webp)
   5. 填写配置。
      <!-- @cols-width: 157,667 -->
      | **配置**  | **说明**  |
      | --- | --- |
      | OAuth 跳转地址  | 自定义渠道提供的 OAuth2.0 授权地址。 | \
      | | | \
      | | 智能体开发者首次发布到这个渠道前，需要完成授权，允许扣子编程以用户身份获取自己的用户 ID。开发者单击授权时，发布页面将会跳转至这个地址。  |
      | 获取 Token 地址  | 自定义渠道提供的获取 Token API 的请求 URL 地址。扣子编程服务端获取授权码之后，会调用此 API，使用授权码换取 access_token。  |
      | 获取用户信息地址  | 自定义渠道提供的获取用户信息 API 的请求 URL 地址。扣子编程服务端获取 access_token 之后，会调用此 API 获取智能体开发者在渠道中的用户 ID。  |
      | 客户端 ID  | 渠道提供给扣子编程的 OAuth 应用客户端 ID。渠道侧应具备 OAuth Server 的能力，渠道管理员在渠道侧为扣子创建一个 OAuth 应用，并提供客户端 ID。  |
      | 客户端密钥  | 渠道提供给扣子编程的 OAuth 应用客户端密钥。渠道侧应具备 OAuth Server 的能力，渠道管理员在渠道侧为扣子编程创建一个 OAuth 应用，并提供客户端密钥。  |
      配置示例如下：
      ![Image=242x283](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/687746447d54486a9ef9e709dc35a769~tplv-goo7wpa0wc-topic.webp)
   6. 单击**确认**。

## 步骤四：开发者完成授权并发布智能体 {#5840ff81}

开发者搭建智能体之后，可以随时将智能体发布到指定的渠道中。首次发布前需要配置渠道授权，即授予扣子编程获取开发者的渠道用户 ID 的权限。授权后，智能体发布到渠道时，扣子编程会同时向渠道发送一条回调消息，其中包含智能体开发者的渠道用户 ID，渠道可以根据这个回调消息获取智能体 ID 和渠道用户 ID 之间的对应关系。

开发者在发布页面找到自定义渠道，并单击**授权**。

![Image=500x167](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/65cc6930702443c399941d16627b0c67~tplv-goo7wpa0wc-topic.webp)

在弹出页面中完成授权后，回到发布页面，选中自定义渠道，并单击**发布**。

![Image=599x308](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8e38a5401d124d1ba0f68d41bf9ba52f~tplv-goo7wpa0wc-topic.webp)

## 步骤五：渠道服务端处理消息回调 {#6014cc16}

渠道管理员订阅渠道回调，具体请参见[订阅渠道回调](/dev_how_to_guides/add_callback#72098317)。

当有智能体发布到此渠道时，扣子服务端会发送一条 `application/json` 格式的 POST 请求。渠道侧收到消息回调后，应校验签名、从回调消息中提取信息，在渠道侧进行业务处理后，返回处理结果给扣子服务端。

目前支持的回调事件类型、渠道侧的处理方式及回调事件的详细定义可参考[接收并处理回调](/dev_how_to_guides/receive_handle_callbacks)。

![Image=454x416](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5884a6e3346e4a6cba5bbea3beafd63a~tplv-goo7wpa0wc-topic.webp)

## 步骤六：渠道服务端调用扣子 API {#6d46e9f6}

自定义渠道通过服务端调用扣子 OpenAPI 来使用智能体，例如查看智能体详情、和智能体对话等。您的自建网站等渠道中可以定义通过 OpenAPI 与智能体对话的相关业务流程，将智能体提供给渠道用户使用。

渠道服务端调用扣子 OpenAPI 前，必须通过渠道类型的 OAuth 应用授权，且通过此应用生成 JWT 类型的 OAuth Access Token，而开发者应用程序则可以使用 PAT 等多种类型的 OAuth Access Token。默认情况下，为渠道绑定 OAuth 应用后，这个 Oauth 应用生成的 OAuth Access Token 将拥有所有发布到此渠道的智能体的操作权限。具体的操作权限可参考此 OAuth 应用中选择的权限列表。如果渠道侧希望限制 OAuth Access Token 的操作权限，可以在申请的 OAuth Access Token 时，通过 scope 参数指定令牌的操作权限，例如此令牌只能和智能体 A 对话，不能执行其他操作。详细说明可参考[通过 JWT 获取 Oauth Access Token](/developer_guides/oauth_jwt#a458f4b1)。

![Image=491x483](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6025d8c853e348b585cb96a7abbee161~tplv-goo7wpa0wc-topic.webp)

## 附录：OAuth 参数协议 {#10357080}

对于自行入驻扣子编程的第三方渠道，扣子编程根据标准的 OAuth2.0 授权码授权方式，提供统一的 OAuth 2.0 参数协议。渠道侧应参考以下 API 的定义，在渠道服务端实现 OAuth2.0 Server 能力。

### 跳转地址 {#4108c744}

自定义渠道提供的 OAuth2.0 授权地址。

开发者首次发布到这个渠道前，需要完成授权，允许扣子以用户身份获取自己的用户 ID。开发者单击授权时，扣子编程服务端会向此地址发送请求，请求 Query 中包含 client_id 等信息，发布页面将会跳转至这个地址。渠道侧应在此地址中展示具体的授权内容，你可以参考飞书渠道的授权页面样式。

![Image=268x269](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c4c9f50674884d4ab2c15db1bfd54eac~tplv-goo7wpa0wc-topic.webp)

此接口请求方式为 GET，不限制请求的 Header 和 Body。接口请求 URL 格式及示例如下：

```Bash
# 格式：
<AUTH_URL>?                    # 渠道侧提供的 OAuth2 授权地址
   client_id=817****&           # 渠道侧提供给 coze 的客户端 id
   redirect_uri=https://www.coze.cn/auth/callback&  # 授权完成后, 跳转到 coze 的 REDIRECT_URI 地址
   response_type=code&         # 固定为 code
   state=1294848                 # 由 coze 生成, 跳转到 coze 的 REDIRECT_URI 地址的时候应该透传
    
# 扣子发送的请求示例：
https://www.newplatform.cn/api/permission/oauth2/authorize?client_id=8173420653665306615182245269****&redirect_uri=https://www.coze.cn/auth/callback&response_type=code&state=1294848
```

:::tip 说明
配置渠道授权时，仅填写 \<AUTH_URL> 部分即可，无需填写 Query 参数部分。
:::

请求 Query 参数如下：

<!-- @cols-width: 129,100,100,500 -->
| **字段**  | **类型**  | **是否必选**  | **说明**  |
| --- | --- | --- | --- |
| client_id  | String  | 必选  | 客户端 ID。渠道侧应具备 OAuth Server 的能力，渠道管理员在渠道侧为扣子创建一个 OAuth 应用，并提供客户端 ID。  |
| redirect_uri  | String  | 必选  | 重定向 URL。固定为 `https://www.coze.cn/auth/callback`。 | \
| | | | | \
| | | | 用户授权后，授权页面自动跳转到此地址。  |
| response_type  | String  | 必选  | 响应类型，固定为 code。  |
| state  | String  | 可选  | 由扣子编程生成的状态码。通常情况下，state 是一串随机字符串或哈希值。扣子编程在发起授权请求时将其附加到请求 URL 中，终端用户完成授权时，扣子编程会验证返回的 state 值是否与原始值匹配。如果不匹配或 state 参数丢失，扣子编程会拒绝这次授权请求。  |

### 跳转到扣子REDIRECT_URI {#f22a228a}

在用户单击授权后，渠道侧应生成一个授权码（code），将授权页重定向到扣子编程的 REDIRECT_URI，并向扣子编程服务端返回 code。

此 API 由扣子编程提供，渠道侧应确保正确发送 API 请求，在请求 Query 中传递 code 和 state。

此接口请求方式为 GET，不限制请求的 Header 和 Body。接口请求 URL 格式及示例如下：

```Python
# 格式：
https://www.coze.cn/auth/callback?
   code=1294848&  # 渠道侧生成的授权码, 只能使用一次
   state=STATE       # 扣子在发起授权请求时指定的 state 参数, 渠道侧需要透传
    
 # 渠道侧发送的请求示例：
 https://www.coze.cn/auth/callback?code=1294848&state=STATE 
```

请求 Query 参数如下：

<!-- @cols-width: 129,100,100,500 -->
| **字段**  | **类型**  | **是否必选**  | **说明**  |
| --- | --- | --- | --- |
| code  | String  | 必选  | 渠道侧生成的授权码，只能使用一次。有效期应在 5 分钟以上。  |
| state  | String  | 必选  | 由扣子编程生成的状态码。渠道侧应透传 跳转地址 API 中获取的 state 参数值。  |

### 获取 token {#0a99a55e}

此 API 由渠道侧提供。扣子服务端获取授权码之后，会调用此 API，使用授权码换取 access_token。

此接口请求方式为 POST，不限制请求的 Body。接口请求 URL 格式及示例如下：

```JSON
curl --location --request POST <TOKEN_URL> \                  // 渠道侧提供的API
--header 'Content-Type: application/json' \  
--data-raw '{
    "client_id":"aaaaa",                // 渠道侧为扣子指定的客户端 ID
    "client_secret":"bbbbb",            // 渠道侧为扣子指定的客户端秘钥
    "code":"xxxx",                     // 渠道侧返回给扣子的 code
    "redirect_uri":"https://www.coze.cn/auth/callback", // 可选。重定向 URL。固定为 https://www.coze.cn/auth/callback。
    "grant_type":"authorization_code"  // 固定为 authorization_code
}'
```

请求 Header 参数如下：

<!-- @cols-width: 129,255,436 -->
| **字段**  | **取值**  | **说明**  |
| --- | --- | --- |
| Content-Type  | application/json  | 表示请求格式为 JSON。  |

请求 Query 参数如下：

<!-- @cols-width: 129,100,100,500 -->
| **字段**  | **类型**  | **是否必选**  | **说明**  |
| --- | --- | --- | --- |
| client_id  | String  | 必选  | 客户端 ID。渠道侧应具备 OAuth Server 的能力，渠道管理员在渠道侧为扣子创建一个 OAuth 应用，并提供客户端 ID。  |
| client_secret  | String  | 必选  | 客户端密钥。渠道侧应具备 OAuth Server 的能力，渠道管理员在渠道侧为扣子创建一个 OAuth 应用，并提供客户端密钥。  |
| grant_type  | String  | 必选  | 授权类型，固定为 authorization_code。  |
| redirect_uri  | String  | 可选  | 重定向 URL。固定为 `https://www.coze.cn/auth/callback`。  |
| code  | String  | 必选  | 渠道侧返回的授权码 code。  |

响应参数如下：

<!-- @cols-width: 199,139,500 -->
| **字段**  | **类型**  | **说明**  |
| --- | --- | --- |
| access_token  | String  | 访问令牌。有效期应为 3 分钟以上。  |
| token_type  | String  | 访问令牌的类型，固定为 Bearer。  |

响应示例如下：

```JSON
// http_code=200时，表示请求成功
{
  "access_token": "111",
  "token_type": "Bearer"
}

// http_code 为其他值时，表示请求失败
{
  "code": 123,
  "message": "error message"
}
```

### 获取用户信息 {#a9e30ad7}

此 API 由渠道侧提供。扣子服务端获取访问令牌之后，会调用此 API 查看渠道用户 ID。

此接口请求方式为 GET，不限制请求的 Query、Body。接口请求 URL 格式及示例如下：

```Python
curl <AUTH_USER_URL>
   -H 'Authorization: Bearer <user_access_token>'
```

响应参数如下：

<!-- @cols-width: 199,139,500 -->
| **字段**  | **类型**  | **说明**  |
| --- | --- | --- |
| name  | String  | 当前智能体开发者的渠道用户名称。  |
| id  | String  | 当前智能体开发者的渠道用户 ID。  |

响应示例如下：

```JSON
// http_code=200时，表示请求成功
{
  "name": "zhangsan",
  "id": "user_id"
}

// http_code 为其他值时，表示请求失败
{
  "code": 123,
  "message": "error message"
}
```
