> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程支持为低代码项目接入自定义模型。本文将介绍如何在低代码项目中配置并使用自定义模型。

:::tip 说明
* **套餐限制**：企业旗舰版。
* **角色限制**：组织超级管理员和管理员。
* **访问控制**：在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 功能简介 {#b3c7dc41}

为满足企业对模型的专业化与个性化需求，对于**低代码项目**，扣子编程在提供官方模型及火山方舟模型的基础上，支持**接入自定义模型**。企业可将自部署或第三方在线模型集成至扣子编程，进一步拓展扣子编程可用的模型范围。组织管理员配置自定义模型的 API Key 和 API URL 等相关参数后，给指定工作空间授权，工作空间成员在智能体编排或工作流大模型节点中，能像使用扣子模型一样便捷地使用自定义模型。

**自定义模型**优势包括：

* **提升特定领域的准确性**：借助自定义模型对特定领域的深度适配，可大幅提升智能体在金融、法律、医疗等垂直场景的专业性与准确性。这不仅能构建企业独特的技术壁垒，更能实现核心业务推理逻辑的自主可控，保障 AI 应用的安全可靠。
* **灵活的鉴权方式**：支持 Authorization 和 Header 两种鉴权方式。
   * **Authorization**：通过 `Authorization` 请求头字段传递 API Key。
   * **Header**：通过自定义请求头字段传递身份鉴权信息，即需要自定义 Header Key 和 Header Value。
* **密钥安全托管**：调用模型所需的鉴权密钥支持明文存储或通过火山引擎 KMS 加密存储。KMS 加密存储能够有效杜绝密钥泄露风险，确保模型调用过程中的身份认证安全。
* **标准化接入协议**：模型 API 协议与 OpenAI Chat Completions 或 Responses API 完全兼容，降低了模型的适配和迁移成本。
* **动态参数配置**：支持通过 JSON Schema 定义模型参数，扣子编程可动态生成配置界面，方便开发者在编排智能体时对模型进行精细化调整。

## 费用说明 {#b542891e}

接入自定义模型时，如果选择火山引擎 KMS 加密存储鉴权密钥（API Key 或 Header Value），则 KMS 产品会收取**凭据托管费**和 **API 调用费**，这些费用自动从你的火山引擎余额中扣款，不支持使用扣子积分抵扣，具体收费标准可参考[凭据管理计费说明](https://www.volcengine.com/docs/6476/1356306)。

## 使用限制 {#324506c6}

* **账号状态**：火山引擎账号欠费后，KMS 凭据无法使用，使用自定义模型的智能体将无法正常使用，应及时充值。
* **模型响应要求**：扣子编程请求自定义模型时，使用流式传输 (`ChatRequest.stream=true` )，自定义模型 API 需支持并返回流式响应。

## 管理员接入自定义模型 {#86c4dab9}

### 准备工作 {#9d00f018}

* 已获取模型 API URL。
* 采用 Authorization 鉴权方式时，需先获取自定义模型的 API Key。
* 采用火山 KMS 加密存储鉴权密钥时，需将密钥托管至火山引擎 KMS 凭据中，具体请参考[使用火山引擎 KMS 管理鉴权密钥](/guides/deploy_custom_model#4ea43dc9)。
   :::tip 说明
   建议由企业超级管理员对应的火山引擎主账号创建 KMS 凭据。其他企业成员账号需具备 KMS 产品的 KMSFullAccess 权限，具体操作，请参考[为成员设置火山引擎 IAM 权限（企业版）](/guides/set_pro_subusers)。
   :::   


### 步骤一：在扣子编程接入自定义模型 {#1fa51d21}


1. 在[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)左下角单击个人头像，选择企业账号，然后单击对应组织的**设置**图标。
   ![Image=292x279](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/578f48daeef44d77a9883395c7af08f3~tplv-goo7wpa0wc-topic.webp)
2. 在**企业组织管理**页面，选择**模型接入** > **自定义模型**页签。
3. 在页面中单击**接入模型**，在弹出的对话框中设置相关参数，参数说明如下表所示。
   <!-- @cols-width: 164,633 -->
   | **参数**  | **说明**  |
   | --- | --- |
   | 模型 icon  | 单击图标，上传自定义模型的 icon 图片，方便团队成员识别和选择。 | \
   | | | \
   | | 若未配置，扣子编程将使用默认图标。  |
   | 模型展示名称  | 自定义模型在扣子编程中展示的名称，方便团队成员识别和选择。例如：`Kimi-K2-adapt`。  |
   | 模型唯一标识  | 模型的唯一 ID。扣子编程在发起 API 请求访问模型时，会将其填入 `ChatRequest` 的 `model` 字段，请正确填写，以确保请求能够准确指向目标模型。 | \
   | | | \
   | | * 方舟模型：请填写模型的 **Endpoint ID**。 | \
   | | * 其他自定义模型：请填写该模型自身的 **模型 ID**，例如：`Kimi-K2-25071`。  |
   | 模型描述  | 对模型的详细说明，描述其能力、适用场景和特点。  |
   | 模型 API URL  | 自定义模型的 API 调用地址。扣子编程在发起请求时，会自动在该地址后拼接`/chat/completions`，因此填入的 URL 无需包含这部分内容。示例：`https://example.com/api/v1`。  |
   | API 协议  | 扣子编程调用自定义模型 API 时，采用的 API 协议，固定为 OpenAI Chat/completion API 协议。  |
   | 鉴权方式  | 设置扣子编程调用自定义模型 API 时的鉴权方式。 | \
   | | | \
   | | * **Authorization**：通过 `Authorization` 请求头字段传递 API Key。 | \
   | | * **Header**：通过自定义请求头字段传递身份鉴权信息，即需要在此处的 **Header Key** 中自定义一个请求头字段，例如 `X-API-Key`，并在**鉴权密钥**中设置 **Header Value**。  |
   | 鉴权密钥  | 设置鉴权方式后，需要选择鉴权密钥（API Key 或 Header Value）的存储方式以及输入具体的鉴权密钥。密钥存储方式包括火山 KMS 加密存储、明文存储。 | \
   | | | \
   | | * 火山 KMS 加密存储：需要先将鉴权密钥托管在火山引擎 KMS 密钥管理系统中，然后在此处的 **Secret Name** 中填入你在 KMS 中创建的**凭据名称**。例如：`CozeSecret`。在火山引擎托管 API Key 的具体方法请参考[使用火山引擎 KMS 管理鉴权密钥](/guides/deploy_custom_model#4ea43dc9)。 | \
   | | * 明文存储：以明文形式存储模型的 API Key 或自定义的 Header Value。 | \
   | |    * 采用 **Authorization** 鉴权方式时，需在此处的 **API Key** 中填入自定义模型的 API Key。 | \
   | |    * 采用 **Header** 鉴权方式时，需在此处的 **Header Value** 中填入自定义的 Header Value。 | \
   | |       明文存储的密钥在安全性上相对较低，存在一定的泄露风险。  |
   | 模型能力  | 选择自定义模型支持的能力，扣子编程将根据你选择的模型能力，在模型标签中展示对应的能力标签，方便用户选择。包括工具调用、图片理解、视频理解、音频理解、续写、深度思考。  |
   | 模型上下文长度  | 根据模型的实际能力，填写模型能够处理的上下文最大长度，单位：token。  |
   | 自定义参数 schema  | 自定义模型支持的配置项，以便开发者在智能体编排页面或工作流大模型节点的**模型设置**中，调整这些参数。 | \
   | | | \
   | | 采用 **JSON Schema** 格式进行定义，样例和各字段的说明请参考[JSON Schema 字段说明](/guides/deploy_custom_model#34e1be46)。  |   


### 步骤二：管理员配置模型的可用空间 {#4a0fb892}

接入自定义模型后，你需要指定哪些工作空间可以使用该模型，默认所有工作空间都不能使用该模型。

1. 在**企业组织管理** > **模型接入** > **自定义模型**页面的模型列表中找到需要停运的模型。
2. 单击该模型右侧的 **…** 按钮，选择**修改可用空间**。
3. 单击对应工作空间右侧的开关，开启这个自定义模型。
   ![Image=448x260](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/85737a4303e84e06af229e684d3e1344~tplv-goo7wpa0wc-topic.webp)   


## 企业成员使用自定义模型 {#35bdf482}

在智能体的编排页面，开发者可以在模型列表的**自定义模型**区域，选择管理员已成功接入的自定义模型。

![Image=573x279](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/162be1750c824c9db98a8a77344d5d74~tplv-goo7wpa0wc-topic.webp)

## 相关操作 {#79f7f0fa}

### 停运模型 {#5604d81e}

如果不再需要某个自定义模型，管理员可以按照以下步骤进行停运。

:::notice 注意
停运模型后，所有正在使用此模型的智能体和工作流将无法正常工作。在停运模型之前，请务必确认所有使用此模型的智能体和工作流已切换至其他可用模型。
:::

1. 在**企业组织管理** > **模型接入** > **自定义模型**页面的模型列表中，找到需要停运的模型。
2. 在需停运模型的**操作**列，选择···> **停运模型**。
   ![Image=531x136](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f5e03d6297e2460ba98fc51952cdb846~tplv-goo7wpa0wc-topic.webp)
3. 在弹出的确认对话框中，单击**停运**。

### 使用火山引擎 KMS 管理鉴权密钥 {#4ea43dc9}

采用火山 KMS 加密存储模型的鉴权密钥时，企业超级管理员需要先将模型的鉴权密钥（API Key 或 Header Value）托管在火山引擎 KMS 密钥管理系统中，通过 KMS 凭据实现安全存储。扣子编程调用自定义模型 API 时将使用此凭据进行身份认证。通过 KMS 凭据管理既能防止未授权访问，又避免密钥明文存储导致信息泄露。

1. 登录火山引擎 [KMS控制台](https://console.volcengine.com/kms/region:kms+cn-beijing/primary)开通 KMS 凭据管理服务，单击**新建凭据**，具体步骤请参考[凭据管理快速入门](https://www.volcengine.com/docs/6476/1356301)。
   ![Image=600x357](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3a1bcba1e15f4afbac4ce4dc0438116b~tplv-goo7wpa0wc-topic.webp)
2. 在新建凭据页面配置相关参数，单击**创建**，关键参数说明如下表所示。
   <!-- @cols-width: 100,100,500 -->
   | **分类**  | **参数**  | **说明**  |
   | --- | --- | --- |
   | 基础信息  | 凭据类型  | 在本场景中选择**通用凭据**。  |
   |^^| 凭据名称  | 自定义的凭据名称。例如：`CozeSecret`。  |
   |^^| 加密主密钥  | 加密主密钥为用来对保管的 Secret 数据进行加密的密钥，本场景中选择**系统默认密钥**。  |
   |^^| 项目  | 选择该凭据资源所属的项目，保持默认值即可。  |
   | 凭据值配置  | 凭据值  | 本场景中选择**纯文本**，然后在文本中输入如下内容。 | \
   | | | | \
   | | | * 采用 **Authorization** 鉴权方式时，输入自定义模型的 API Key。 | \
   | | | * 采用 **Header** 鉴权方式时，输入自定义的 Header Value。  |   


### JSON Schema 字段说明 {#34e1be46}

在 JSON Schema 中明确自定义模型可配置的参数，包括参数名称、类型、默认值、可选范围等，以便扣子编程前端能动态生成模型配置界面，扣子编程服务端能够校验用户提交的参数值是否正常，确保符合模型要求。

下方的 JSON 示例是一个数组（Array），其中每个配置项都是一个对象（Object）。每个对象都定义了一个可供开发者在 UI 界面上配置的模型参数。你需要依据模型实际支持的功能进行设置，例如模型生成内容的多样性、随机性、最大回复长度等。

字段说明：

<!-- @cols-width: 138,120,100,504 -->
| **字段**  | **类型**  | **是否必选**  | **说明**  |
| --- | --- | --- | --- |
| `name`  | string  | 必选  | 参数的唯一标识符，对应 API 请求中的字段名。例如：`max_tokens`。  |
| `type`  | integer  | 必选  | 参数类型，枚举值如下： | \
| | | | | \
| | | | * 1：Float | \
| | | | * 2：Integer | \
| | | | * 3：Boolean | \
| | | | * 4：String  |
| `is_required`  | boolean  | 必选  | 标识该参数是否为必选项。 | \
| | | | | \
| | | | * `true`表示必选。 | \
| | | | * `false`表示可选。  |
| `default_value`  | object  | 必选  | 参数的默认值配置。该对象可以包含一个或多个键值对。 | \
| | | | | \
| | | | 示例：`{ "default": "1" }`。  |
| `min` / `max`  | string  | 可选  | * 当 `type`为 1（Float）和 2（Integer）时，需要设置参数的最小值和最大值。 | \
| | | | * 当 `type`为其他类型时，该字段为空。  |
| `precision`  | integer  | 必选  | 当 `type`为 1 （Float）时，定义数值的小数位数精度。例如，`precision: 1` 表示允许一位小数。非数值类型，通常为 0。  |
| `options`  | array  | 可选  | 定义下拉菜单中的所有枚举值。例如 `[ "enabled", "disabled", "auto" ]`。  |
| `auto_fix`  | boolean  | 必选  | 当用户输入的值超出取值范围时，是否自动修正。 | \
| | | | | \
| | | | * `true`：自动修正为最接近的边界值。例如，若`max`为 100 而用户输入120，扣子编程会将其自动修正为 100。 | \
| | | | * `false`：超出取值范围时不会自动修正。  |

:::tip 说明
自定义模型可配置的参数仅支持以下示例代码中的参数，暂不支持其他参数。
:::

示例代码：

::::tabs
@tab Chat API
```JSON
[
  // 定义"temperature"配置项，用于控制模型输出的随机性和创造性
  {
    "auto_fix": false,    // 超出取值范围时是否自动修正：false表示不自动修正
    "default_value": {
      "default": "1"    // 默认场景下的初始值为1
    },
    "is_required": false,
    "max": "2",
    "min": "0",
    "name": "temperature",
    "options": [],     // 下拉选项：type=1（Float）无需配置，为空数组
    "precision": 2,  // 数值精度：保留2位小数（如0.80、1.25）
    "type": 1  // UI控件类型：1表示Float
  },
  // 定义"top_p"配置项，用于控制模型输出的随机性（与temperature配合使用）
  {
    "auto_fix": false,
    "default_value": {
      "default": "0.7"
    },
    "is_required": false,
    "max": "1",
    "min": "0",
    "name": "top_p",
    "options": [],
    "precision": 2,
    "type": 1
  },
  // 定义"frequency_penalty"配置项，用于降低模型重复使用相同词汇的倾向
  {
    "auto_fix": false,
    "default_value": {
      "default": "0"
    },
    "is_required": false,
    "max": "2",
    "min": "-2",
    "name": "frequency_penalty",  // 如果自定义模型的实际参数为presence_penalty，你也可以将该参数替换为presence_penalty
    "options": [],
    "precision": 2,
    "type": 1
  },
  // 定义"max_tokens"配置项，用于限制单次请求中模型生成的最大内容长度
  {
    "auto_fix": false,
    "default_value": {
      "default": "4096"
    },
    "is_required": false,
    "max": "16384",
    "min": "0",
    "name": "max_tokens",
    "options": [],
    "precision": 0,
    "type": 2  // UI控件类型：2表示Integer
  },
  // 定义"sp_current_time"配置项，用于配置是否在每次请求时向模型注入当前时间信息
  {
    "auto_fix": false,
    "default_value": {
      "default": "false"
    },
    "is_required": false,
    "max": "",   // 布尔值参数无需配置
    "min": "",     // 布尔值参数无需配置
    "name": "sp_current_time",
    "options": [],  // 布尔值参数无需配置
    "precision": 0,   // 无需精度配置，固定为0
    "type": 3  // UI控件类型：3表示 Boolean
  },
  // 定义"sp_anti_leak"配置项，用于配置是否启用系统提示词防泄漏功能
  {
    "auto_fix": false,
    "default_value": {
      "default": "false"
    },
    "is_required": false,
    "max": "",
    "min": "",
    "name": "sp_anti_leak",
    "options": [],
    "precision": 0,
    "type": 3
  },
  // 用于配置"thinking_type"（深度思考模式）配置项，仅当模型支持深度思考时需配置
  {
    "auto_fix": false,
    "default_value": {
      "default": "auto"
    },
    "is_required": false,
    "max": "",    // 枚举值参数无需配置
    "min": "",    // 枚举值参数无需配置
    "name": "thinking_type",
    "options": [    // 下拉选项列表：枚举所有可选值
      "enabled",
      "disabled",
      "auto"
    ],
    "precision": 0,   // 无需精度配置，固定为0
    "type": 4     // UI控件类型：4 String
  },
  // 定义"reasoning_effort"配置项，用于控制模型的深度思考程度。仅部分模型支持，详情请参考 。并且"thinking_type"为 disabled 时，reasoning_effort 需为 minimal。
  {
    "auto_fix": false,
    "default_value": {
      "default": "medium"
    },
    "is_required": false,
    "max": "",
    "min": "",
    "name": "reasoning_effort",
    "options": [
      "minimal",
      "low",
      "medium",
      "high"
    ],
    "precision": 0,
    "type": 4
  },
  // 定义"max_completion_tokens"配置项，用于限制模型思维链推理和回答的最大长度（单位：token）
  {
    "auto_fix": false,
    "default_value": {
      "default": "0"
    },
    "is_required": false,
    "max": "16384",
    "min": "0",
    "name": "max_completion_tokens",
    "options": [],
    "precision": 0,
    "type": 2
  }
]
```



@tab Responses API
与 Chat API 相比，Responses API 新增了以下字段：

* `caching_type`
* `store`
* `caching_expire_time`

```JSON
[
  // 定义"sp_current_time"配置项，用于配置是否在每次请求时向模型注入当前时间信息
  {
    "auto_fix": false,    // 超出取值范围时是否自动修正：false表示不自动修正
    "default_value": {
      "default": "false"    // 默认场景下的初始值为false
    },
    "is_required": false,
    "max": "",   // 布尔值参数无需配置
    "min": "",     // 布尔值参数无需配置
    "name": "sp_current_time",
    "options": [],  // 布尔值参数无需配置
    "precision": 0,   // 无需精度配置，固定为0
    "type": 3  // UI控件类型：3表示Boolean
  },
  // 定义"sp_anti_leak"配置项，用于配置是否启用系统提示词防泄漏功能
  {
    "auto_fix": false,
    "default_value": {
      "default": "false"    // 默认场景下的初始值为false
    },
    "is_required": false,
    "max": "",   // 布尔值参数无需配置
    "min": "",     // 布尔值参数无需配置
    "name": "sp_anti_leak",
    "options": [],  // 布尔值参数无需配置
    "precision": 0,   // 无需精度配置，固定为0
    "type": 3  // UI控件类型：3表示Boolean
  },
  // 定义"temperature"配置项，用于控制模型输出的随机性和创造性
  {
    "auto_fix": false,    // 超出取值范围时是否自动修正：false表示不自动修正
    "default_value": {
      "default": "1"    // 默认场景下的初始值为1
    },
    "is_required": false,
    "max": "2",
    "min": "0",
    "name": "temperature",
    "options": [],     // 下拉选项：type=1（Float）无需配置，为空数组
    "precision": 2,  // 数值精度：保留2位小数（如0.80、1.25）
    "type": 1  // UI控件类型：1表示Float
  },
  // 定义"top_p"配置项，用于控制模型输出的随机性（与temperature配合使用）
  {
    "auto_fix": false,
    "default_value": {
      "default": "0.7"    // 默认场景下的初始值为0.7
    },
    "is_required": false,
    "max": "1",
    "min": "0",
    "name": "top_p",
    "options": [],     // 下拉选项：type=1（Float）无需配置，为空数组
    "precision": 2,  // 数值精度：保留2位小数（如0.60、0.95）
    "type": 1  // UI控件类型：1表示Float
  },
  // 用于配置"thinking_type"（深度思考模式）配置项，仅当模型支持深度思考时需配置
  {
    "auto_fix": false,
    "default_value": {
      "default": "auto"    // 默认场景下的初始值为auto
    },
    "is_required": false,
    "max": "",    // 枚举值参数无需配置
    "min": "",    // 枚举值参数无需配置
    "name": "thinking_type",
    "options": [    // 下拉选项列表：枚举所有可选值
      "enabled",
      "disabled",
      "auto"
    ],
    "precision": 0,   // 无需精度配置，固定为0
    "type": 4     // UI控件类型：4表示String
  },
  // 定义"reasoning_effort"配置项，用于控制模型的深度思考程度。仅部分模型支持，详情请参考模型服务。并且"thinking_type"为 disabled 时，reasoning_effort 需为 minimal。
  {
    "auto_fix": false,
    "default_value": {
      "default": "medium"
    },
    "is_required": false,
    "max": "",
    "min": "",
    "name": "reasoning_effort",
    "options": [
      "minimal",
      "low",
      "medium",
      "high"
    ],
    "precision": 0,
    "type": 4
  },
  // 定义"max_output_tokens"配置项，用于限制单次请求中模型生成的最大输出内容长度（单位：token）
  {
    "auto_fix": false,
    "default_value": {
      "default": "4096"    // 默认场景下的初始值为4096
    },
    "is_required": false,
    "max": "16384",
    "min": "0",
    "name": "max_output_tokens",
    "options": [],     // 整数参数无需配置下拉选项，为空数组
    "precision": 0,   // 无需精度配置，固定为0（整数无小数位）
    "type": 2  // UI控件类型：2表示Integer
  },
  // 定义"caching_type"配置项，用于配置缓存功能的启用状态
  {
    "auto_fix": false,
    "default_value": {
      "default": "disabled"    // 默认场景下的初始值为disabled
    },
    "is_required": false,
    "max": "",    // 枚举值参数无需配置
    "min": "",    // 枚举值参数无需配置
    "name": "caching_type",
    "options": [    // 下拉选项列表：枚举所有可选值
      "enabled",
      "disabled"
    ],
    "precision": 0,   // 无需精度配置，固定为0
    "type": 4     // UI控件类型：4表示String
  },
  // 定义"store"配置项，用于配置是否启用数据存储功能
  {
    "auto_fix": false,
    "default_value": {
      "default": "true"    // 默认场景下的初始值为true
    },
    "is_required": false,
    "max": "",   // 布尔值参数无需配置
    "min": "",     // 布尔值参数无需配置
    "name": "store",
    "options": [],  // 布尔值参数无需配置
    "precision": 0,   // 无需精度配置，固定为0
    "type": 3  // UI控件类型：3表示Boolean
  },
  // 定义"caching_expire_time"配置项，用于配置缓存数据的过期时间（单位：秒）
  {
    "auto_fix": false,
    "default_value": {
      "default": "259200"    // 默认场景下的初始值为259200（3天）
    },
    "is_required": false,
    "max": "259200",
    "min": "0",
    "name": "caching_expire_time",
    "options": [],     // 整数参数无需配置下拉选项，为空数组
    "precision": 0,   // 无需精度配置，固定为0（整数无小数位）
    "type": 2  // UI控件类型：2表示Integer
  }
]
```


::::
