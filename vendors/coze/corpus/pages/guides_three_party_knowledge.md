> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程支持通过三方知识库连接器插件，接入三方知识库，作为扣子编程低代码智能体、工作流的知识资源。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

:::tip 说明
* **套餐限制**：企业标准版、企业旗舰版
* 仅企业超级管理员、管理员可以创建三方知识库连接器插件。
* 只支持检索三方知识库知识，不支持修改、删除、写入知识等操作。
:::

## 功能概述 {#hFDPz3yZf}

你可以通过三方知识库连接器，将企业自建知识库、本地知识库、内部系统知识库等外部知识资源接入到扣子编程，供低代码智能体和工作流检索使用。

接入前，你需要根据扣子编程提供的连接协议，开发并部署一个可公网访问的连接器服务。该服务负责连接你的外部知识库，并根据扣子编程的调用请求返回知识库列表或知识切片。连接器服务需要实现以下接口：

* `get_list` 用于获取可接入的知识库列表。
* `retrieve` 用于根据用户 Query，从指定知识库中检索并返回匹配的知识切片。

完成连接器服务开发和部署后，你还需要在扣子编程中创建三方知识库连接器插件。扣子编程会通过该插件调用你的连接器服务，检索三方知识库。

## 步骤 1：开发连接器服务 {#hZ2e6CSAN}

在创建连接器插件之前，你需要先开发连接器服务，实现 get_list 和 retrieve 两个接口。连接器服务需要部署在公网可访问的服务器上，并确保扣子编程可以通过你填写的插件 URL 访问到这些接口。两个接口均采用 JSON 格式进行请求和响应，需严格遵循以下协议规范。

::::tabs
@tab get_list
* 请求参数
   <!-- @cols-width: 100,100,100,286 -->
   | **参数**  | **类型**  | **是否必填**  | **说明**  |
   | --- | --- | --- | --- |
   | limit  | integer  | 是  | 每页返回数量，取值范围 1～1000。  |
   | page  | integer  | 是  | 页码，从 1 开始。  |
   | query  | string  | 否  | 搜索关键词，最大长度 100。  |
* 响应参数
   <!-- @cols-width: 146,103,401 -->
   | **参数名**  | **类型**  | **说明**  |
   | --- | --- | --- |
   | data  | array  | 知识库列表。  |
   | data[].id  | string  | 知识库唯一标识，最大长度 255。  |
   | data[].name  | string  | 知识库名称，最大长度 100。  |
   | data[].description  | string  | 知识库描述，最大长度 2000。  |
   | data[].type  | integer  | 知识库类型，可选值。 | \
   | | | | \
   | | | * 0 ：结构化知识库。 | \
   | | | * 1 ：非结构化知识库。  |
   | has_more  | boolean  | 是否还有更多数据。  |
   | total  | integer  | 知识库总数。  |
   | page  | integer  | 当前页码。  |

@tab retrieve
* 请求参数
   <!-- @cols-width: 152,108,100,426 -->
   | **参数**  | **类型**  | **是否必填**  | **说明**  |
   | --- | --- | --- | --- |
   | knowledge_id  | string  | 是  | 目标知识库 ID，对应 `get_list` 接口返回的 `id`。  |
   | query  | string  | 是  | 用户查询内容。  |
   | top_k  | integer  | 是  | 最多返回的知识切片数量，取值范围为 1-20。  |
   | score_threshold  | number  | 是  | 相关度阈值，取值范围为 0～1，默认值为 0.2。 | \
   | | | | | \
   | | | | 仅返回相关度高于该值的切片。  |
   | query_type  | integer  | 否  | 检索方式。 | \
   | | | | | \
   | | | | * 0（默认值）：混合检索。 | \
   | | | | * 1 ：语义检索。 | \
   | | | | * 2：全文检索。  |
   | extra  | object  | 否  | 扩展参数，用于传递额外的检索配置。  |
* 响应参数
   <!-- @cols-width: 200,100,419 -->
   | **参数**  | **类型**  | **描述**  |
   | --- | --- | --- |
   | items  | array  | 命中的知识切片列表。  |
   | items[].slice  | string  | 命中的知识切片内容。  |
   | items[].score  | number  | 相关度分数，取值范围为 0-1。  |
   | items[].meta  | object  | 知识切片的来源信息。  |
   | items[].meta.slice_source  | string  | 知识切片来源，例如文档名称、网页名称等。  |
   | items[].meta.source_link  | string  | 知识切片来源链接。  |
::::

## 步骤 2：创建连接器插件 {#步骤1：创建连接插件}

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 在页面右上角，选择 **+资源** > **插件**。
4. 配置插件信息。
   1. 设置基础信息。
      <!-- @cols-width: 247,515 -->
      | **配置项**  | **说明**  |
      | --- | --- |
      | 插件图标  | 单击默认图标后，您可以上传本地图片文件作为新的图标。  |
      | 插件名称  | 自定义插件名称，用于标识当前插件。建议输入清晰易理解的名称，便于大语言模型搜索与使用插件。  |
      | 插件描述  | 插件的描述信息，一般用于记录当前插件的用途。  |
      | 插件工具创建方式  | 选择**云侧插件-基于已有服务创建**。  |
      | 私网连接  | 基于已有服务创建云侧插件时，只支持选择**不使用私网连接**。  |
      | 配置为知识库连接器  | 打开**配置为知识库连接器**开关。  |
      | 插件 URL  | 三方知识库对应的 API 接口链接。 | \
      | | | \
      | | :::tip 说明 | \
      | | 插件 URL 必须为域名格式，不支持 IP 格式的 URL 地址。 | \
      | | ::: | \
      | | | \
      | |   |
      | Header 列表  | HTTP 请求头参数列表。您需要根据 API 自身的参数配置要求来填写。  |
   2. 设置授权方式。
      该类型插件，仅支持**Service token / API key**授权方式。
      <!-- @cols-width: 144,649 -->
      | **配置项**  | **说明**  |
      | --- | --- |
      | Service  | 服务认证，支持 **Service token / API key。​**该认证方式是指 API 通过秘钥或令牌校验请求者的身份。配置参数说明如下： | \
      | | | \
      | | * **位置**：选择秘钥或令牌在 API 请求中的位置，即 **Header**（请求头）或是 **Query** （查询参数）内。 | \
      | | * **Parameter name**：密钥或令牌对应的参数名称。 | \
      | | * **Service token / API key**：密钥或令牌的值。后续根据该值进行服务认证。  |
   3. 单击**确认**。
5. 试运行工具。
   创建知识库连接器插件后，系统会自动生成 get_list、retrieve 工具。你需要分别试运行这两个工具，确保能正常运行。
   1. 单击目标工具对应的**运行**图标。
   2. 单击页面右上角的**试运行**。
   3. 设置输入参数，单击**运行**。
      ![Image=274x148](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/598534e6e17d44cdab3b274208bc1f9c~tplv-goo7wpa0wc-topic.webp)
   4. 试运行成功后，单击**连接器校对**，确认校对成功。
6. 返回**工具列表**页面，单击页面右上角的**发布**，发布插件。

## 步骤 3：接入三方知识库 {#步骤2：接入三方知识库}

创建知识库连接器插件后，你可以在扣子编程中接入三方知识库。接入成功后，可以将三方知识库作为扣子编程资源的一种，加入到扣子编程资源库中。关联成功后，开发者便可在扣子编程的低代码智能体、工作流中使用三方知识库。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 在页面右上角，选择**资源**> **知识库。**
4. 单击**创建三方知识库**，选择待关联的三方知识库，然后单击**创建并导入**。
   * 选择三方知识库入口：支持选择**资源库**或**商店**。
   * 关联资源库插件：选择具体的连接器插件，连接知识库。
