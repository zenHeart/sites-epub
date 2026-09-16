> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

MCP 工具是基于模型上下文协议（Model Context Protocol，MCP）的一种工具实现，它允许服务器向客户端暴露可执行的功能。通过 MCP 工具，大语言模型（LLM）可以按需自动执行计算、操作外部系统，甚至与真实世界交互。扣子应用现已支持发布为 MCP 工具，可作为扣子空间的扩展能力，帮助用户在扣子空间内实现更丰富的功能，为扣子空间增加垂直领域的私有知识、数据、工具等等。

## 什么是 MCP {#3024ff26}

MCP 是一种开放协议，它规范了应用程序向大语言模型提供上下文的方式。你可以将 MCP 理解为扣子空间的插件系统，它允许你通过标准化的接口，将扣子空间的 AI Agent 与各种外部工具、数据源相连接。通过 MCP 扩展，大语言模型（LLM）可以按需自动执行计算、操作外部系统，甚至与真实世界交互。关于 MCP 的更多信息，请参考 [MCP 官方文档](https://modelcontextprotocol.io/introduction)。

MCP 可以帮助你在大语言模型的基础上构建智能体和复杂的工作流。大语言模型常常需要与数据和工具进行集成，而 MCP 提供了：

* 一系列不断增加的预构建集成，让大模型可以直接接入这些集成。
* 能够在不同的大语言模型提供商和供应商之间灵活切换。
* 在你的基础设施内保障数据安全的最佳实践方法。

## MCP 扩展库 {#1e571834}

扣子提供了一系列官方 MCP 扩展供你使用，常见的官方 MCP 扩展详细说明可参考[官方 MCP 扩展](/guides/publish_to_space#27e21e3a)。

如果你的任务还需要添加私有知识、数据，或者集成一系列定义好的流程节点，你也可以在扣子编程中搭建扣子应用，并将其发布为 MCP 扩展，为扣子空间增加垂直领域的私有知识、数据、工具等等。扣子编程为你提供了简单易用但能力上限极高的 AI 应用开发脚手架，在这里你可以快速开发、调试各种流程工具，并快速发布到包括扣子空间扩展库在内的丰富渠道。

:::tip 说明
扣子空间调用扣子应用对应的自定义 MCP 扩展完成任务时，会产生模型 Token 等资源用量，扣子编程会根据每次调用的实际 Token 数量从扣子账号中扣减对应的积分。你可以在积分的**消费历史**中查看明细。
:::

### 官方 MCP 扩展 {#27e21e3a}

:::tip 说明
在使用过程中，可能需要你进行环境变量配置、授权等操作。
:::

扣子空间集成了丰富的 MCP 扩展，为你提供了全面的功能支持。对于通用的 MCP 扩展，扣子空间已直接将其内置到主 Agent 中，在 Agent 执行任务过程中，会自动选择并调用合适的 MCP 扩展，无需你额外配置。此外，扣子空间还提供了一系列个性化的 MCP 扩展，这些扩展已上传至扩展库。

扩展库中常用的 MCP 扩展如下所示。

![Image=372x417](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8a892a974d804ae5a3b35012a5ac5aff~tplv-goo7wpa0wc-topic.webp)

<!-- @cols-width: 172,550 -->
| **MCP 扩展**  | **说明**  |
| --- | --- |
| 高德地图  | 高德地图官方 MCP 扩展，支持查询地点、搜索周边、规划不同交通工具的路线、经纬度与位置的转换等功能。  |
| 飞书云文档  | 支持在你的飞书文档空间中进行检索、创建、编辑飞书文档等操作。  |
| 飞书多维表格  | 支持在你的飞书文档空间中进行检索、创建、编辑飞书多维表格等操作。  |
| 飞书电子表格  | 支持在你的飞书文档空间中进行检索、创建、编辑飞书电子表格等操作。  |
| 水滴信用  | 支持全国企业信用信息查询，包括企业工商数据、股权结构、司法行政风险等信息。  |
| 飞常准  | 支持查询全球航班状态、航班号、预计出发/降落时间等信息。  |
| 音乐生成  | 支持生成不同风格的高质量歌曲，支持男/女声等不同音色。  |
| 墨迹天气  | 天气查询工具，可提供省、市、区县的未来 40 天的天气情况，包括温度、湿度、日夜风向等信息。  |
| 图像工具  | 支持生成高质量图片以及编辑已有图像。  |
| 语音合成  | 支持将文本转化成不同音色的人声音频。  |
| Notion  | 支持 Notion 文档和数据表的创建、读取、编辑、更新、搜索、查询等操作。  |
| Github  | 支持搜索 Github 仓库、文件、代码、用户，并支持查询 issue。申请 Personal Access Token，请参考 [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/github)。  |
| MySQL  | 支持连接并执行 MySQL 查询请求。  |
| Clickhouse  | 支持对 ClickHouse 数据库的列取、数据表操作和只读 Query 执行功能，详情请参考[mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse)。  |

### 自定义 MCP 扩展 {#8bbba115}

#### 为什么需要自定义 MCP 扩展 {#1b7340ab}

* 对于某些要求严格根据流程执行的任务，Agent 不一定每次都按照固定的流程执行，而自定义的 MCP 扩展可以约束 Agent 按照固定的步骤稳定执行任务。例如，在数据分析场景，通用 Agent 通常会通过写 Python 代码来处理数据，每次执行的代码可能都不同，但如果你开发了一个数据分析的扣子应用，则可以稳定地使用你预设的逻辑和分析方法处理数据。
* 通用 Agent 常常缺少解决任务必须的私有数据和知识，此时你可以通过自定义扩展为 Agent 提供这些内容。例如通过自定义扩展让 Agent 通过你已搭建的达人数据库帮你筛选最合适的推品达人。
* 自定义扩展也可以为扣子空间通用 Agent 赋予一些垂直领域的能力，比如根据房型设计装修图、搭建 3D 模型、发送消息等等。

## 发布应用为 MCP 工具 {#2aee24f5}

### 注意事项 {#336a6088}

将应用发布为 MCP 工具，应注意：

<!-- @cols-width: 148,655 -->
| **限制**  | **说明**  |
| --- | --- |
| 工作流  | * 输出节点不生效，发布后只会返回结束节点的最终输出 | \
| | * 暂不支持以下工作流发布为 MCP 工具： | \
| |    * 对话流 | \
| |    * 包含创建会话等会话管理类节点的工作流 | \
| |    * 包含端插件节点、问答节点、输入节点等中断节点的工作流  |
| 权限  | 扣子应用的发布者必须是应用的所有者。发布后仅应用所有者本人可在扣子空间中使用  |
| 费用  | 如果扣子空间在执行任务时，自动调用了此 MCP 工具，扣子编程会根据实际产生的模型 Token 等资源用量，自动扣减对应的扣子积分。扣子编程的收费标准可参考[计费概述](/coze_pro/billing_overview)。  |
| 名称与图标  | MCP 工具名称和图标默认为扣子应用的名称和图标。  |

### 操作步骤 {#e03e0b2e}

以下是发布到商店的详细步骤：

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部空间列表中选择目标工作空间。
3. 在**项目开发**页面，选择你要发布的低代码应用，进入应用的编排页面。
4. 在页面右上角，单击**发布**，进入发布页面。
5. 在发布页面填写版本信息：
   * **版本号**：必填，必须是一个应用从未设置过的新版本号。
   * **版本描述**：可选，说明该版本更新的内容。
6. 填写扩展配置。
   1. 在**选择发布平台 > MCP 服务**选项，找到**扣子空间扩展库**，并单击**配置**。
      ![Image=400x193](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d2eeefddf4354c7583a7adffd6f3e287~tplv-goo7wpa0wc-topic.webp)
   2. 选择要发布为 MCP 工具的工作流，并单击**确认**。
      ![Image=349x208](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/33ebbeed32d64f95ba613a1081845572~tplv-goo7wpa0wc-topic.webp)
7. 确认已选择**扣子空间扩展库**，并单击**发布**。
   ![Image=400x216](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bed18950bef44dac875ceb9f750bdda7~tplv-goo7wpa0wc-topic.webp)
8. 确认发布成功。
   ![Image=297x244](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fbeb007000a84ab18d4fd7cb1a8e6bde~tplv-goo7wpa0wc-topic.webp)   


## 在扣子空间使用 MCP 工具 {#86159f3b}

将应用中的指定工作流发布为 MCP 工具之后，你就可以在扣子空间中开启 MCP 工具扩展，并创建任务。MCP 工具默认是模型控制，即大模型会按需自动调用 MCP 工具完成任务，例如进行简单的计算、复杂的 API 交互，或查看私有知识与数据。

### 添加 MCP 工具 {#0204dec8}

在扣子空间中创建任务之前，单击扩展并添加你的自定义 MCP 工具即可。

::::cols
@col 50
点击**扩展**：

![Image=425x155](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d23c2c6c83d84864b9e399c93f8600fe~tplv-goo7wpa0wc-topic.webp)

@col 50
**添加扩展**：

![Image=3144x1677](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2c55f7b383dd487898daa4fc5565d453~tplv-goo7wpa0wc-topic.webp)
::::

### 调用 MCP 工具 {#837e2ec3}

任务执行过程中，扣子空间会自动调用工具完成任务，你可以通过 Agent 的思考过程来判断是否已调用工具。例如 MCP 工具的功能为解析抖音视频，其中工作流名为 `douyin_video_parse`，当创建一个需要解析抖音视频的任务时，可以看到 Agent 调用了 `douyin_video_parse` 来解析视频。

![Image=603x322](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/057e485e489342a6b25636e38d4d69f6~tplv-goo7wpa0wc-topic.webp)

### 查看 MCP 工具的调用记录 {#4875a35f}

将扣子应用发布为 MCP 工具之后，你可以在**发布管理**页面查看此 MCP 工具在扣子空间中的调用记录。

![Image=601x301](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6083683ad37d4232a6c67ceb5bfae18e~tplv-goo7wpa0wc-topic.webp)

扣子空间调用扣子应用对应的 MCP 工具完成任务时，会产生模型 Token 等资源用量，扣子编程会根据每次调用的实际 Token 数量从扣子账号中扣减对应的积分。你可以在积分的消费历史中查看明细。

![Image=587x312](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a6ba66c7e4b646c3bae38a0785ceaf36~tplv-goo7wpa0wc-topic.webp)

## 下架应用 {#921f1a7d}

如果不再需要在扣子空间中展示该 MCP 工具，你可以选择将其下架。下架的操作步骤请参见[下架应用](/guides/manage_published_project#0d68edf9)。
