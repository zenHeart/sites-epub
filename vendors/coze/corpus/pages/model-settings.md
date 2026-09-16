> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

## 切换模型 {#hcgQgyNEt}

模型就像是扣子的大脑，扣子的回答质量、响应速度、对复杂任务的处理能力很大程度上取决于你为它配置的模型。不同模型单价不同、也各有所长，你可以换几个模型对比一下效果和成本，从而选择最合适的模型。

目前扣子提供以下模型模式供你选择：

* 自动（默认）：后台自动调度，根据任务复杂程度、各个模型负载来灵活匹配合适的模型。
* 指定模型：提供业界先进的模型版本。关于模型费用，请参考[扣子任务费用](https://docs.coze.cn/coze_pro_coze_task_fee)。
   * 大语言模型：Deepseek-V4-Pro、GLM-5.3、Doubao-Seed-2.1-pro、Kimi K3 等模型。
   * 多模态模型：Seedream 5.0 Pro、Seedream 5.0 Lite、Seedream4.5、Seedance2.5 等模型。

你可以为 Agent 指定一个**大语言模型**和一个**多模态模型**。

:::notice 注意
* 各个模型的 Token 单价不同，单价更高的模型，每次对话消耗的积分越多。你可以在各个模型厂商官网查看模型单价。
* 扣子会针对部分模型版本推出限时折扣活动，活动期间你可以以较低价格使用这些折扣模型。
:::

::::tabs
@tab 桌面端、网页端
1. 在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的对话列表中，单击目标 Agent。
2. 在 Agent 对话输入框中，单击**模型**下拉列表，选择其他模型。
   ![Image=249x193](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f3f1b73ad5554754bbd2332bf1a24a97~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
1. 在扣子 App 中，单击目标 Agent。
2. 在 Agent 对话输入框中，单击**模型**下拉列表，选择其他模型。
::::

## **接入自定义模型** {#hkxptvfmL}

:::tip 说明
* **套餐限制**：仅个人进阶版及以上版本支持添加自定义模型。
* **Agent 类型**：Coze Agent、云端 Agent、以及编程项目支持切换为自定义模型，其他类型 Agent 均不支持。
* **企业用户权限**：企业成员均可添加自定义模型，添加后默认仅本人可用。**企业组织的超级管理员和管理员**可以在**模型管理**页面开启**成员可用**，将模型分享给企业组织内的其他成员。
* **平台限制**：仅限网页端和桌面端操作，移动端暂不支持添加和管理自定义模型。
:::

扣子官方提供了 Doubao、GLM、Kimi 等大模型供你选择。除此之外，你也可以添加自定义模型、接入自己的模型 API，例如你自行部署的模型、第三方在线模型等。成功接入后，你的 Coze Agent 就可以使用自己的模型服务，使用自定义模型的 Agent 也不会再收取扣子对话费用，而是消耗你自己的 Token 费用。

<!-- @cols-width: 175,500 -->
| **接入方式**  | **适用场景**  |
| --- | --- |
| 服务商接入  | 使用扣子已适配的第三方模型服务商。 | \
| | | \
| | 当前支持以下服务商： | \
| | | \
| | * 火山引擎方舟 | \
| | * Kimi | \
| | * DeepSeek | \
| | * 智谱 GLM | \
| | * MiniMax | \
| | * 智谱GLM (Coding Plan)  |
| 自定义接入  | 使用用户自己的模型服务，或兼容 OpenAI 协议的第三方模型服务。 | \
| | | \
| | 支持的协议类型： | \
| | | \
| | * Chat API | \
| | * Responses API | \
| | * Anthropic Messages  |

具体的操作步骤如下：

::::tabs
@tab 服务商接入
1. 在[模型管理](https://www.coze.cn/model-management?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)页面右上角单击 **+ 接入模型**。
2. 在**服务商接入**页签中填写以下配置：
   * **服务商**：选择需要接入的模型服务商。
   * **API Key**：调用服务商模型接口所需的鉴权凭证。以火山方舟为例，API Key 获取方式可参考[火山方舟官方文档](https://www.volcengine.com/docs/82379/1399008?lang=zh#da0e9d90)。
   * **选择模型**：选择需要添加到扣子中的模型。每次只能添加一款模型。
   * **图片理解**：开启后，该模型可用于图片理解场景，需模型本身支持该能力。关闭后，图片理解场景将自动调用扣子提供的识图工具。
      ![Image=371x221](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9b13bb44b0a54b369b6b8d5eace3d38e~tplv-goo7wpa0wc-topic.webp)
3. 单击**添加**。
   成功添加自定义模型后，就可以将 Agent 模型设置为你的自定义模型了。
   ![Image=340x260](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/292d419446d04663ace7ed8ad3e1f8d9~tplv-goo7wpa0wc-topic.webp)

@tab 自定义接入
1. 进入**添加自定义模型**页面。
   找到要切换模型的扣子 Agent 或云端 Agent，在对话框右下角展开模型列表，并选择 **+ 添加自定义模型**。
2. 在自定义接入页签中填写以下配置：
   * **模型展示名称**：模型在扣子内展示的名称，便于用户识别和选择。
   * **模型 ID**：模型唯一标识，例如 `doubao-seed-2-0-lite-260428`，调用接口时会作为模型标识传入。
   * **模型协议**：选择模型服务兼容的 OpenAI 协议类型，支持 Chat API、Responses API 和 Anthropic Messages。
   * **API URL**：填写模型服务的 Base URL。选择不同协议后，系统会自动拼接对应接口路径。
   * **API Key**：调用模型服务所需的鉴权凭证。
   * **图片理解**：开启后，该模型可用于图片输入场景，需模型本身支持图片理解。
   * **最大输入长度**：模型单次支持的最大输入 token 数，可手动填写，也可选择 32K、64K、128K、256K。
   * **最大回复长度**：模型单次回复支持的最大输出 token 数，可手动填写，也可选择 16K、32K、64K、128K。
      ![Image=262x432](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e0d54d2260334870841db5ade97bba21~tplv-goo7wpa0wc-topic.webp)
3. 单击**添加**。
   成功添加自定义模型后，就可以将 Agent 模型设置为你的自定义模型了。
   ![Image=489x273](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1a85870f71914819bf928283f5f42652~tplv-goo7wpa0wc-topic.webp)
::::
