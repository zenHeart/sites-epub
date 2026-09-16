> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

本文介绍如何通过导入定义 API 的 JSON 或 YAML 文件来创建插件。创建插件后，必须发布插件才可以被低代码智能体或工作流使用。

:::tip 说明
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
* 个人工作空间中的插件，仅能被个人调用；企业工作空间中插件，能被任意企业成员调用。
* 插件发布了新版本后，使用了这个插件的低代码智能体和工作流会自动使用发布的最新版本。
* 定义 API 的 JSON 或 YAML 文件仅支持 [OpenAPI](https://swagger.io/specification/)、[Swagger](https://swagger.io/docs/specification/2-0/basic-structure/) 或 [Postman Collection](https://learning.postman.com/docs/getting-started/importing-and-exporting/exporting-data/#exporting-data-dumps) 协议，示例请参考[JSON 或 YAML 文件示例](/guides/import#cb985a6c)。
:::

## 操作步骤 {#a0b1f2d2}

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 在页面右上角，选择 **+资源** > **插件**。
   ![Image=504x170](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/013e73be30ef4768a3432e8017d9c325~tplv-goo7wpa0wc-topic.webp)
4. 在右上角单击**导入**。
   ![Image=375x312](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/badc6da36e394800a437d35862bab115~tplv-goo7wpa0wc-topic.webp)
   此外，基于已有服务创建的插件支持在其插件详情页内导入工具，而通过 IDE 方式创建的插件则不支持此功能。你可以在插件详情页的工具列表右上角单击**导入**。
   ![Image=495x108](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0f8ea66882444f9c9f8266a6a988694d~tplv-goo7wpa0wc-topic.webp)
5. 在**导入插件**对话框，选择以下任一导入方式，并单击**下一步**。
   * 方式一：在**本地文件**页签内，通过拖拽或点击的方式，上传保存在本地的 JSON 或 YAML 文件。
   * 方式二：在 **URL 和原始数据页签**内，填写存放 API JSON 或 YAML 文件的 URL 地址。
   * 方式三：在 **URL 和原始数据页签**内，填写 JSON 或 YAML 格式的 API 原始数据。
   :::notice 注意
   如果您需要单次导入多个 API，则需要确保各个 API 有相同的 URL 路径前缀，该路径前缀将会作为插件 URL 来使用。如果单次导入的 API URL 路径前缀不一致，则会导入失败。
   :::
6. 导入后，在**确认插件信息**对话框，补全插件配置信息，并单击**确认**。
   ![Image=296x336](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8c959c252d96467791843bf85953cc3c~tplv-goo7wpa0wc-topic.webp)
   配置项说明：
   <!-- @cols-width: 178,649 -->
   | **配置项**  | **说明**  |
   | --- | --- |
   | 插件图标  | 单击默认图标后，您可以上传本地图片文件作为新的图标。  |
   | 插件名称  | 自定义插件名称，用于标识当前插件。建议输入清晰易理解的名称，便于大语言模型搜索与使用插件。  |
   | 插件描述  | 插件的描述信息，一般用于记录当前插件的用途。  |
   | 插件 URL  | 插件的访问地址或相关资源的链接，不可修改，示例值 `https://www.example.com/api`。如果一次导入了多个 API，则这里的插件 URL 是指各个 API 中相同的 URL 路径前缀。 | \
   | | | \
   | | :::tip 说明 | \
   | | 插件 URL 必须为域名格式，暂不支持 IP 格式的 URL 地址。 | \
   | | ::: | \
   | | | \
   | |   |
   | Header 列表  | HTTP 请求头参数列表。  |
   | 授权方式  | 选择插件内 API 的鉴权方式。目前支持以下三种： | \
   | | | \
   | | * **不需要授权** | \
   | | * **Service**：服务认证，支持 **Service token / API key** 和 **OAuth 2.0 & OIDC**： | \
   | |    * **Service token / API key**：该认证方式是指 API 通过密钥或令牌校验请求者的身份。配置参数说明如下： | \
   | |       * **位置**：选择密钥或令牌在 API 请求中的位置，即 **Header**（请求头）或是 **Query** （查询参数）内。 | \
   | |       * **Parameter name**：秘钥或令牌对应的参数名称。 | \
   | |       * **Service token / API key**：秘钥或令牌的值。后续根据该值进行服务认证。 | \
   | |    * **OAuth 2.0 & OIDC**：OIDC 是一种广泛使用的授权框架，它基于 OAuth 2.0 协议之上，提供了身份验证和授权的功能。配置参数说明如下： | \
   | |       * **grant_type**：根据 GrantType 来选择使用的 OAuth Flow，支持的 Flow 包括： | \
   | |          * TokenExchange：用于在不同服务之间交换令牌。 | \
   | |          * ClientCredential：用于客户端凭据授权流程，适用于没有用户直接参与的情况。 | \
   | |       * **endpoint_url**：授权服务器的端点 URL，用于发送授权请求和接收响应。配置时需要指定授权服务器的地址，以便客户端可以正确地向服务器发起请求。 | \
   | |       * **audience**：资源服务器，客户端告诉授权服务器它希望代表用户访问哪个资源服务器。配置时需要指定资源服务器的标识符。 | \
   | |       * **scope**：客户端请求的权限范围。对于 OIDC，通常需要包含`openid`作用域，以请求身份验证，配置时需要根据需要请求的权限范围来设置。 | \
   | |       * **client_id**：客户端在授权服务器注册时获得的唯一标识符，配置时需要使用在授权服务器注册应用时获得的 client_id。 | \
   | | * **Oauth > standard**：OAuth 是一种常用于用户代理身份验证的标准，它允许第三方应用程序在不共享用户密码的情况下访问用户下的特定资源。 | \
   | |    * **client_id**：注册 OAuth 后获取的唯一标识符。 | \
   | |    * **client_secret**：与 client_id 匹配的密码。 | \
   | |    * **client_url**：验证通过后，模型会重定向到该 url。 | \
   | |    * **scope**：您的应用需要访问的资源范围或级别。 | \
   | |    * **authorization_url**：OAuth 提供商的 URL，用户会重定向到该 URL 进行应用授权。 | \
   | |    * **authorization_content_type**：向 OAuth 提供商发送数据时的内容类型。  |
7. 进入插件详情页，在工具的**启用**列打开启用开关，并在**操作**列单击**调试**按钮。
   :::tip 说明
   导入插件后，插件内的工具默认未启用且未通过调试，因此您需要先启用工具并通过调试。
   :::
   ![Image=508x148](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1c7da116a9d440bcbad4976cb2ba5ff6~tplv-goo7wpa0wc-topic.webp)
8. 在工具的**调试与校验**界面，调试工具，并单击**完成**。
   导入时扣子编程已自动为工具填充了配置项，如果工具内的基本信息、输入参数、输出参数仍有信息未完善，则您需要先完善参数信息（已自动填充的参数配置也支持手动修改），然后再进行调试。调试成功后，在页面右侧会提示**调试通过**。
   ![Image=505x265](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b2b84c60774d46ec8abc636236fd0a90~tplv-goo7wpa0wc-topic.webp)
9. 在插件详情页的右上角，单击**发布**。

## 上架到商店 {#daffdfb5}

你可以将插件上架到扣子插件商店或企业插件商店。不能同时上架扣子插件商店和企业插件商店，仅支持选择其中一个渠道。

* **上架扣子插件商店**
   对于通用功能、不涉及敏感数据且具有广泛适用性的公开插件，你可以将其上架到扣子商店，以便更多扣子用户发现、使用。详情请参考[将插件上架到插件市场](/guides/publish_plugin_to_store)。
* **上架企业插件商店**
   仅企业旗舰版支持。
   对于企业自主开发的涉及核心业务逻辑、数据敏感信息或仅限内部场景使用的插件，你可以将其上架到企业插件商店，供企业成员使用。详情请参考[管理企业插件](/guides/enterprise_plugin_store)。   


## JSON 或 YAML 文件示例 {#cb985a6c}

### OpenAPI 3.0 {#6b8017d3}

```YAML
info:
    description: httpbin apis
    title: Httpbin APIs
    version: v1
openapi: 3.0.1
paths:
    /get:
        get:
            operationId: get
            parameters:
                - description: name
                  in: query
                  name: name
                  schema:
                    type: string
            requestBody:
                content:
                    application/json:
                        schema:
                            type: object
            responses:
                "200":
                    content:
                        application/json:
                            schema:
                                properties:
                                    args:
                                        properties:
                                            name:
                                                type: string
                                        type: object
                                type: object
                    description: new desc
                default:
                    description: ""
            summary: API to get
    /post:
        post:
            operationId: post
            requestBody:
                content:
                    application/json:
                        schema:
                            properties:
                                A:
                                    description: A
                                    type: string
                                B:
                                    description: B
                                    type: integer
                            type: object
            responses:
                "200":
                    content:
                        application/json:
                            schema:
                                properties:
                                    json:
                                        properties:
                                            A:
                                                type: string
                                            B:
                                                type: number
                                        type: object
                                type: object
                    description: new desc
                default:
                    description: ""
            summary: API to get
    /put:
        put:
            operationId: put
            requestBody:
                content:
                    application/json:
                        schema:
                            properties:
                                value:
                                    description: value
                                    type: string
                            type: object
            responses:
                "200":
                    content:
                        application/json:
                            schema:
                                properties:
                                    json:
                                        properties:
                                            value:
                                                type: string
                                        type: object
                                type: object
                    description: new desc
                default:
                    description: ""
            summary: API to put
servers:
    - url: https://httpbin.org
```

### Swagger（OpenAPI 2.0） {#d08ff7c5}

```YAML
swagger: "2.0"
info:
  description: "This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key `special-key` to test the authorization     filters."
  version: "1.0.0"
  title: "Swagger_Petstore_Sample"
  termsOfService: "http://swagger.io/terms/"
  contact:
    email: "apiteam@swagger.io"
  license:
    name: "Apache 2.0"
    url: "http://www.apache.org/licenses/LICENSE-2.0.html"
host: "petstore.swagger.io"
basePath: "/v2"
tags:
- name: "pet"
  description: "Everything about your Pets"
  externalDocs:
    description: "Find out more"
    url: "http://swagger.io"
- name: "store"
  description: "Access to Petstore orders"
- name: "user"
  description: "Operations about user"
  externalDocs:
    description: "Find out more about our store"
    url: "http://swagger.io"
schemes:
- "https"
- "http"
paths:
  /pet:
    post:
      tags:
      - "pet"
      summary: "Add a new pet to the store"
      description: ""
      operationId: "addPet"
      consumes:
      - "application/json"
      - "application/xml"
      produces:
      - "application/xml"
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        description: "Pet object that needs to be added to the store"
        required: true
        schema:
          $ref: "#/definitions/Pet"
      responses:
        "400":
          description: Invalid input
        "422":
          description: Validation exception
      security:
      - petstore_auth:
        - "write:pets"
        - "read:pets"
    put:
      tags:
      - "pet"
      summary: "Update an existing pet"
      description: ""
      operationId: "updatePet"
      consumes:
      - "application/json"
      - "application/xml"
      produces:
      - "application/xml"
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        description: "Pet object that needs to be added to the store"
        required: true
        schema:
          $ref: "#/definitions/Pet"
      responses:
        "400":
          description: "Invalid ID supplied"
        "404":
          description: "Pet not found"
        "422":
          description: "Validation exception"
      security:
      - petstore_auth:
        - "write:pets"
        - "read:pets"
  /pet/findByStatus:
    get:
      tags:
      - "pet"
      summary: "Finds Pets by status"
      description: "Multiple status values can be provided with comma separated strings"
      operationId: "findPetsByStatus"
      produces:
      - "application/xml"
      - "application/json"
      parameters:
      - name: "status"
        in: "query"
        description: "Status values that need to be considered for filter"
        required: true
        type: "array"
        items:
          type: "string"
          enum:
          - "available"
          - "pending"
          - "sold"
          default: "available"
        collectionFormat: "multi"
      responses:
        "400":
          description: "Invalid status value"
      security:
      - petstore_auth:
        - "write:pets"
        - "read:pets"
  /pet/{petId}:
    get:
      tags:
      - "pet"
      summary: "Find pet by ID"
      description: "Returns a single pet"
      operationId: "getPetById"
      produces:
      - "application/xml"
      - "application/json"
      parameters:
      - name: "petId"
        in: "path"
        description: "ID of pet to return"
        required: true
        type: "integer"
        format: "int64"
      responses:
        "200":
          description: "successful operation"
          schema:
            $ref: "#/definitions/Pet"
        "400":
          description: "Invalid ID supplied"
        "404":
          description: "Pet not found"
      security:
      - api_key: []
    post:
      tags:
      - "pet"
      summary: "Updates a pet in the store with form data"
      description: ""
      operationId: "updatePetWithForm"
      consumes:
      - "application/x-www-form-urlencoded"
      produces:
      - "application/xml"
      - "application/json"
      parameters:
      - name: "petId"
        in: "path"
        description: "ID of pet that needs to be updated"
        required: true
        type: "integer"
        format: "int64"
      - name: "name"
        in: "formData"
        description: "Updated name of the pet"
        required: false
        type: "string"
      - name: "status"
        in: "formData"
        description: "Updated status of the pet"
        required: false
        type: "string"
      responses:
        "400":
          description: Invalid input
        "422":
          description: Validation exception
      security:
      - petstore_auth:
        - "write:pets"
        - "read:pets"
    delete:
      tags:
      - "pet"
      summary: "Deletes a pet"
      description: ""
      operationId: "deletePet"
      produces:
      - "application/xml"
      - "application/json"
      parameters:
      - name: "api_key"
        in: "header"
        required: false
        type: "string"
      - name: "petId"
        in: "path"
        description: "Pet id to delete"
        required: true
        type: "integer"
        format: "int64"
      responses:
        "400":
          description: "Invalid ID supplied"
        "404":
          description: "Pet not found"
      security:
      - petstore_auth:
        - "write:pets"
        - "read:pets"
securityDefinitions:
  petstore_auth:
    type: "oauth2"
    authorizationUrl: "http://petstore.swagger.io/oauth/dialog"
    flow: "implicit"
    scopes:
      write:pets: "modify pets in your account"
      read:pets: "read your pets"
  api_key:
    type: "apiKey"
    name: "api_key"
    in: "header"
definitions:
  Order:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      petId:
        type: "integer"
        format: "int64"
      quantity:
        type: "integer"
        format: "int32"
      shipDate:
        type: "string"
        format: "date-time"
      status:
        type: "string"
        description: "Order Status"
        enum:
        - "placed"
        - "approved"
        - "delivered"
      complete:
        type: "boolean"
        default: false
    xml:
      name: "Order"
  Category:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      name:
        type: "string"
    xml:
      name: "Category"
  User:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      username:
        type: "string"
      firstName:
        type: "string"
      lastName:
        type: "string"
      email:
        type: "string"
      password:
        type: "string"
      phone:
        type: "string"
      userStatus:
        type: "integer"
        format: "int32"
        description: "User Status"
    xml:
      name: "User"
  Tag:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      name:
        type: "string"
    xml:
      name: "Tag"
  Pet:
    type: "object"
    required:
    - "name"
    - "photoUrls"
    properties:
      id:
        type: "integer"
        format: "int64"
      category:
        $ref: "#/definitions/Category"
      name:
        type: "string"
        example: "doggie"
      photoUrls:
        type: "array"
        xml:
          name: "photoUrl"
          wrapped: true
        items:
          type: "string"
      tags:
        type: "array"
        xml:
          name: "tag"
          wrapped: true
        items:
          $ref: "#/definitions/Tag"
      status:
        type: "string"
        description: "pet status in the store"
        enum:
        - "available"
        - "pending"
        - "sold"
    xml:
      name: "Pet"
  ApiResponse:
    type: "object"
    properties:
      code:
        type: "integer"
        format: "int32"
      type:
        type: "string"
      message:
        type: "string"
externalDocs:
  description: "Find out more about Swagger"
  url: "http://swagger.io"
```

### Postman Collection {#5078bcc3}

通过 Postman Collection 导出的 json 文件，可以直接导入并创建插件。需要注意的是，request body 和 response body 都只支持 application/json 格式。

```JSON
{
    "info": {
        "_postman_id": "21b585a5-e8b2-41ea-b2d0-6e4f9c703abf",
        "name": "REST API CRUD",
        "description": "# 🚀 This template guides you through CRUD operations (GET, POST, PUT, DELETE), variables, and tests.",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
        "_exporter_id": "32482447"
    },
    "item": [
        {
            "name": "Get data",
            "request": {
                "method": "GET",
                "header": [
                    {
                        "key": "Connection",
                        "value": "Keep-Alive"
                    }
                ],
                "url": {
                    "raw": "{{base_url}}/get?city=beijing&type=park",
                    "host": [
                        "{{base_url}}"
                    ],
                    "path": [
                        "get"
                    ],
                    "query": [
                        {
                            "key": "city",
                            "value": "beijing"
                        },
                        {
                            "key": "type",
                            "value": "park"
                        }
                    ]
                },
                "description": "This is a GET request and it is used to \"get\" data from an endpoint. There is no request body for a GET request."
            },
            "response": []
        },
        {
            "name": "Post data",
            "request": {
                "method": "POST",
                "header": [],
                "body": {
                    "mode": "raw",
                    "raw": "{\"B\": \"b\", \"C\": 1, \"D\": true, \"E\": {\"F\": 2}, \"G\": [\"g\"]}",
                    "options": {
                        "raw": {
                            "language": "json"
                        }
                    }
                },
                "url": {
                    "raw": "{{base_url}}/post?city=beijing&type=park",
                    "host": [
                        "{{base_url}}"
                    ],
                    "path": [
                        "post"
                    ],
                    "query": [
                        {
                            "key": "city",
                            "value": "beijing"
                        },
                        {
                            "key": "type",
                            "value": "park"
                        }
                    ]
                },
                "description": "This is a POST request, submitting JSON data to an API via the request body."
            },
            "response": []
        },
        {
            "name": "Update data",
            "request": {
                "method": "PUT",
                "header": [],
                "body": {
                    "mode": "raw",
                    "raw": "{\"B\": \"b\", \"C\": 1, \"D\": true, \"E\": {\"F\": 2}, \"G\": [\"g\"]}",
                    "options": {
                        "raw": {
                            "language": "json"
                        }
                    }
                },
                "url": {
                    "raw": "{{base_url}}/put?city=beijing&type=park",
                    "host": [
                        "{{base_url}}"
                    ],
                    "path": [
                        "put"
                    ],
                    "query": [
                        {
                            "key": "city",
                            "value": "beijing"
                        },
                        {
                            "key": "type",
                            "value": "park"
                        }
                    ]
                },
                "description": "This is a PUT request and it is used to overwrite an existing piece of data."
            },
            "response": []
        }
    ],
    "variable": [
        {
            "key": "base_url",
            "value": "https://httpbin.org/"
        }
    ]
}
```

## 常见问题 {#966e1304}

### 使用 API 的 YAML 文件导入插件时提示 invalid parameter，如何解决？ {#746370f1}

使用 API 的 YAML 文件导入插件时，如果提示 invalid parameter ，请根据如下步骤排查：

1. 检查 YAML 文件中的参数配置是否正确，不存在参数缺失或格式错误。
   YAML 文件示例，请参考[JSON 或 YAML 文件示例](/guides/import#cb985a6c)。
2. 检查插件参数是否包含手机号等敏感字段。
   如果包含，需移除或修改涉及用户隐私的字段。
