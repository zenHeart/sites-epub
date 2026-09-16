> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# API 概述

> 查看 Kimi API 的服务地址、认证方式、请求格式、兼容性和主要接口入口。

## 服务地址

```
https://api.moonshot.cn
```

不同兼容协议的 `base_url` 不同，见下方「协议兼容性」。

## 协议兼容性

Kimi API 兼容三种 API 格式，您可以直接复用对应的官方 SDK 和工具：

| 兼容 API                  | base\_url                           | 接口                               | 可用 SDK / 工具                                                      |
| ----------------------- | ----------------------------------- | -------------------------------- | ---------------------------------------------------------------- |
| OpenAI Chat Completions | `https://api.moonshot.cn/v1`        | [`/chat/completions`](/docs/api/chat) | OpenAI 官方 SDK（Python / Node.js），以及 LangChain、Dify、Coze 等第三方工具和框架 |
| OpenAI Responses        | `https://api.moonshot.cn/v1`        | [`/responses`](/docs/api/responses)   | OpenAI 官方 SDK（Python / Node.js）                                  |
| Anthropic Messages      | `https://api.moonshot.cn/anthropic` | [`/messages`](/docs/api/messages)     | Anthropic 官方 SDK、Claude Code 等工具                                 |

如果您的项目原本在使用 OpenAI 或 Anthropic 的官方 API，只需将 `base_url` 和 API Key 替换为 Kimi 的配置即可迁移，无需修改其他代码。

<Note>
  使用 OpenAI 兼容接口时，部分参数为 Kimi 专有扩展：`thinking` 参数需要通过 SDK 的 `extra_body` 传递；`partial` 是写在 messages 中 assistant 消息上的字段（`"partial": true`），不是顶层请求参数。详见[工具调用](/docs/api/tool-use)和 [Partial Mode](/docs/api/partial)。
</Note>

## 认证

所有 API 请求需要在 HTTP 头中携带 API Key：

```
Authorization: Bearer $MOONSHOT_API_KEY
```

API Key 可在 [Kimi 开放平台控制台](https://platform.kimi.com/console/api-keys) 创建和管理。

<Warning>
  API Key 是敏感信息，请妥善保管。不要在客户端代码、公开仓库或日志中暴露。建议通过环境变量管理。
</Warning>

使用官方 SDK 时，在初始化时传入 API Key 和对应协议的 `base_url`。

OpenAI 兼容接口：

<CodeGroup>
  ```python Python theme={null}
  import os

  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ["MOONSHOT_API_KEY"],
      base_url="https://api.moonshot.cn/v1",
  )
  ```

  ```javascript Node.js theme={null}
  const OpenAI = require("openai");

  const client = new OpenAI({
      apiKey: process.env.MOONSHOT_API_KEY,
      baseURL: "https://api.moonshot.cn/v1",
  });
  ```
</CodeGroup>

Anthropic 兼容接口：

<CodeGroup>
  ```python Python theme={null}
  import os

  from anthropic import Anthropic

  client = Anthropic(
      api_key=os.environ["MOONSHOT_API_KEY"],
      base_url="https://api.moonshot.cn/anthropic",
  )
  ```

  ```javascript Node.js theme={null}
  const Anthropic = require("@anthropic-ai/sdk");

  const client = new Anthropic({
      apiKey: process.env.MOONSHOT_API_KEY,
      baseURL: "https://api.moonshot.cn/anthropic",
  });
  ```
</CodeGroup>

## 错误处理

请求失败时返回包含 `error.type` 和 `error.message` 的 JSON 错误响应，完整的错误类型、错误消息和排障建议请参阅[错误说明](/docs/api/errors)。

## API 端点一览

| 端点                                    | 方法     | 协议        | 说明                                |
| ------------------------------------- | ------ | --------- | --------------------------------- |
| `/v1/chat/completions`                | POST   | OpenAI    | [创建对话补全](/docs/api/chat)               |
| `/v1/responses`                       | POST   | OpenAI    | [Responses API](/docs/api/responses)   |
| `/anthropic/v1/messages`              | POST   | Anthropic | [Messages API](/docs/api/messages)     |
| `/v1/models`                          | GET    | OpenAI    | [列出模型](/docs/api/list-models)          |
| `/v1/tokenizers/estimate-token-count` | POST   | OpenAI    | [计算 Token](/docs/api/estimate)         |
| `/v1/users/me/balance`                | GET    | OpenAI    | [查询余额](/docs/api/balance)              |
| `/v1/tools/search`                    | POST   | Kimi      | [联网搜索 Basic](/docs/api/tools-search)   |
| `/v1/tools/search_pro`                | POST   | Kimi      | [联网搜索 Pro](/docs/api/tools-search-pro) |
| `/v1/tools/fetch`                     | POST   | Kimi      | [网页抓取](/docs/api/tools-fetch)          |
| `/v1/files`                           | POST   | OpenAI    | [上传文件](/docs/api/files-upload)         |
| `/v1/files`                           | GET    | OpenAI    | [列出文件](/docs/api/files-list)           |
| `/v1/files/{file_id}`                 | GET    | OpenAI    | [获取文件信息](/docs/api/files-retrieve)     |
| `/v1/files/{file_id}`                 | DELETE | OpenAI    | [删除文件](/docs/api/files-delete)         |
| `/v1/files/{file_id}/content`         | GET    | OpenAI    | [获取文件内容](/docs/api/files-content)      |
| `/v1/batches`                         | POST   | OpenAI    | [创建批处理任务](/docs/api/batch-create)      |
| `/v1/batches`                         | GET    | OpenAI    | [列出批处理任务](/docs/api/batch-list)        |
| `/v1/batches/{batch_id}`              | GET    | OpenAI    | [获取批处理任务详情](/docs/api/batch-retrieve)  |
| `/v1/batches/{batch_id}/cancel`       | POST   | OpenAI    | [取消批处理任务](/docs/api/batch-cancel)      |

## 下一步

<CardGroup cols={2}>
  <Card title="快速开始" icon="rocket" href="/docs/api/quickstart">
    发送第一个 API 请求
  </Card>

  <Card title="Responses API" icon="code" href="/docs/api/responses">
    OpenAI Responses 兼容接口
  </Card>

  <Card title="Messages API" icon="message" href="/docs/api/messages">
    Anthropic Messages 兼容接口
  </Card>

  <Card title="模型列表" icon="list" href="/docs/api/list-models">
    查看当前可用模型
  </Card>
</CardGroup>
