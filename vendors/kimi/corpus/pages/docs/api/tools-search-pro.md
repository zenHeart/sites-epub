> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 联网搜索 Pro

> 通过 /v1/tools/search_pro 接口发起网页搜索，支持站点与时间范围约束，并返回结构化正文片段。

在联网搜索 Basic 的基础上，支持通过 `sites` 将结果约束在指定站点内（多个站点按 OR 处理，最多 5 个），通过 `time_window` 约束结果的时间范围，并为每个结果返回结构化正文片段（`chunks`），适用于对信息来源和时效有要求的检索场景。

`time_window` 的 `start` 与 `end` 支持 `YYYY`、`YYYY-MM`、`YYYY-MM-DD` 三种格式，均按周期第一天归一化后比较，`start` 不得晚于 `end`。

<Accordion title="调用示例">
  <CodeGroup>
    ```python python expandable theme={null}
    import os
    import requests

    api_key = os.environ.get("MOONSHOT_API_KEY")
    url = "https://api.moonshot.cn/v1/tools/search_pro"

    response = requests.post(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "text_query": "Kimi K2 模型 发布",
            "limit": 5,
            "sites": ["moonshot.cn", "kimi.com"],
            "time_window": {"start": "2026-01", "end": "2026-09"},
        },
    )
    print(response.json())
    ```

    ```bash curl expandable theme={null}
    curl https://api.moonshot.cn/v1/tools/search_pro \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $MOONSHOT_API_KEY" \
      -d '{"text_query": "Kimi K2 模型 发布", "limit": 5, "sites": ["moonshot.cn", "kimi.com"], "time_window": {"start": "2026-01", "end": "2026-09"}}'
    ```

    ```javascript node.js expandable theme={null}
    const apiKey = process.env.MOONSHOT_API_KEY;

    async function main() {
        const response = await fetch("https://api.moonshot.cn/v1/tools/search_pro", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${apiKey}`,
            },
            body: JSON.stringify({
                text_query: "Kimi K2 模型 发布",
                limit: 5,
                sites: ["moonshot.cn", "kimi.com"],
                time_window: { start: "2026-01", end: "2026-09" },
            }),
        });
        const data = await response.json();
        console.log(data);
    }

    main();
    ```
  </CodeGroup>
</Accordion>

<Accordion title="响应字段说明">
  | 字段                                | 类型             | 说明                     |
  | --------------------------------- | -------------- | ---------------------- |
  | `search_results`                  | array\[object] | 搜索结果列表；无结果时为空数组        |
  | `search_results[].authority`      | string         | 来源权威性等级                |
  | `search_results[].date`           | string         | 搜索结果日期                 |
  | `search_results[].icon`           | string         | 站点图标 URL               |
  | `search_results[].mime`           | string         | 内容 MIME 类型             |
  | `search_results[].site_name`      | string         | 站点名称                   |
  | `search_results[].snippet`        | string         | 搜索结果摘要                 |
  | `search_results[].title`          | string         | 搜索结果标题                 |
  | `search_results[].url`            | string         | 搜索结果链接                 |
  | `search_results[].chunks`         | array\[object] | 结构化正文片段，按页面聚合；无正文时为空数组 |
  | `search_results[].chunks[].text`  | string         | 正文片段内容                 |
  | `search_results[].chunks[].score` | number         | 正文片段与查询词的相关性得分         |

  除 `chunks` 外，以上字符串字段在无数据时返回空字符串。

  **响应示例**

  ```json theme={null}
  {
      "search_results": [
          {
              "authority": "S",
              "date": "2026-06-01",
              "icon": "https://platform.kimi.com/favicon.ico",
              "mime": "text/html",
              "site_name": "Kimi API 开放平台",
              "snippet": "Kimi API 开放平台文档入口。",
              "title": "API 概述 - Kimi API 开放平台",
              "url": "https://platform.kimi.com/docs/api/overview",
              "chunks": [
                  {
                      "text": "Kimi API 提供聊天补全、文件、批处理等接口，兼容 OpenAI 与 Anthropic 协议。",
                      "score": 1.23
                  }
              ]
          }
      ]
  }
  ```

  **通用响应头**

  | 响应头              | 说明                                             |
  | ---------------- | ---------------------------------------------- |
  | `X-Msh-Track-Id` | 请求 ID；请求携带同名头时沿用，否则由服务端生成。排查问题时请提供该 ID         |
  | `X-Msh-Chat-Id`  | 会话 ID，固定为 `toolgw-{X-Msh-Track-Id}`；排查问题时请一并提供 |

  以上两个响应头在所有响应（包括错误响应）中均会携带。
</Accordion>

<Accordion title="错误码说明">
  | HTTP 状态码 | error.type               | 典型 message                                                         | 说明                                                                                            |
  | -------- | ------------------------ | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
  | 400      | `invalid_request`        | `invalid request body`                                             | 请求体不是合法 JSON                                                                                  |
  | 400      | `invalid_request`        | `text_query is required`                                           | 缺少搜索查询文本                                                                                      |
  | 400      | `invalid_request`        | `timeout_seconds must be less than or equal to 60`                 | `timeout_seconds` 取值范围为 1-60                                                                  |
  | 400      | `invalid_request`        | `limit must be between 1 and 20`                                   | `limit` 取值范围为 1-20                                                                            |
  | 400      | `invalid_request`        | `sites must contain at most 5 entries`                             | `sites` 最多 5 个站点                                                                              |
  | 400      | `invalid_request`        | `site must not contain whitespace or parentheses`                  | `sites` 单条不能包含空白字符或括号                                                                         |
  | 400      | `invalid_request`        | `time_window.start is invalid, expect YYYY / YYYY-MM / YYYY-MM-DD` | `time_window` 日期格式不合法（`end` 同理）                                                               |
  | 400      | `invalid_request`        | `time_window.start must not be after time_window.end`              | 按周期第一天归一化后，`start` 不得晚于 `end`                                                                 |
  | 401      | -                        | 无错误响应体                                                             | API Key 缺失或无效                                                                                 |
  | 403      | -                        | 无错误响应体                                                             | 账号未激活或已停用                                                                                     |
  | 408      | `client_canceled`        | `client canceled the request`                                      | 客户端在服务端返回前断开连接                                                                                |
  | 429      | `rate_limited`           | `project qps limit exceeded`                                       | 触发频率或并发限制；响应头携带 `X-RateLimit-Limit`、`X-RateLimit-Remaining`，触发每秒请求数限制时还携带 `X-RateLimit-Reset` |
  | 429      | `rate_limit_unavailable` | `rate limit store unavailable`                                     | 限速服务暂时不可用，请稍后重试                                                                               |
  | 500      | `internal_error`         | 内部错误原文                                                             | 服务内部错误，请稍后重试；若持续出现，请携带 `X-Msh-Track-Id` 联系支持团队                                                |
  | 502      | `upstream_failed`        | `upstream service failed`                                          | 服务暂时不可用，请稍后重试                                                                                 |
  | 504      | `timeout`                | `request timeout`                                                  | 搜索超时；可调大 `timeout_seconds` 或精简查询后重试                                                           |
</Accordion>

<Note>
  计费说明：请求成功（HTTP 200）且 `search_results` 非空时，计费一次；请求失败或未返回结果时不计费。具体价格详见[联网搜索定价](/docs/pricing/websearch)。
</Note>


## OpenAPI

````yaml POST /v1/tools/search_pro
openapi: 3.1.0
info:
  title: Moonshot AI API
  version: 1.0.0
  description: Moonshot AI / Kimi 大语言模型服务 API
servers:
  - url: https://api.moonshot.cn
    description: 生产环境
security: []
paths:
  /v1/tools/search_pro:
    post:
      tags:
        - Tools
      summary: 联网搜索 Pro
      description: >-
        在联网搜索 Basic 之上支持站点与时间范围约束，并为每个结果返回结构化正文片段（chunks）。请求成功且返回结果数大于 0
        时计费一次，失败或无结果不计费，详见[联网搜索定价](/pricing/tools)。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ToolsSearchProRequest'
      responses:
        '200':
          description: 搜索结果（含正文片段）
          headers:
            X-Msh-Track-Id:
              description: 请求 ID；请求携带同名头时沿用，否则由服务端生成。排查问题时请提供该 ID。
              schema:
                type: string
            X-Msh-Chat-Id:
              description: 会话 ID，固定为 `toolgw-{X-Msh-Track-Id}`；排查问题时请一并提供。
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolsSearchProResponse'
        '400':
          description: 请求错误 - 参数无效或缺少必填字段
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: 未授权 - API 密钥无效或缺失（直接返回状态码，无错误响应体）
        '403':
          description: 禁止访问 - 账号未激活或已停用（直接返回状态码，无错误响应体）
        '408':
          description: 客户端取消请求
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '429':
          description: 请求过于频繁 - 触发频率或并发限制，或限速服务暂不可用
          headers:
            X-RateLimit-Limit:
              description: 当前触发的限速额度。
              schema:
                type: string
            X-RateLimit-Remaining:
              description: 当前窗口内剩余可用额度。
              schema:
                type: string
            X-RateLimit-Reset:
              description: 限速窗口重置时间（Unix 秒级时间戳；触发每秒请求数限制时返回）。
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: 服务器错误
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '502':
          description: 服务暂时不可用，请稍后重试
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '504':
          description: 请求超时
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - bearerAuth: []
components:
  schemas:
    ToolsSearchProRequest:
      type: object
      properties:
        text_query:
          type: string
          description: 搜索查询文本，不能为空。
        timeout_seconds:
          type: integer
          minimum: 1
          maximum: 60
          description: 搜索超时时间，单位秒，取值范围 1-60。不传则不设置单独超时。
        limit:
          type: integer
          minimum: 1
          maximum: 20
          default: 5
          description: 最多返回结果数，默认 5，取值范围 1-20。
        sites:
          type: array
          items:
            type: string
          maxItems: 5
          description: 站点约束，多个站点按 OR 处理，最多 5 个；单条不能为空，且不能包含空白字符或括号。
        time_window:
          $ref: '#/components/schemas/ToolsSearchTimeWindow'
      required:
        - text_query
    ToolsSearchProResponse:
      type: object
      properties:
        search_results:
          type: array
          items:
            $ref: '#/components/schemas/ToolsSearchProResult'
          description: 搜索结果列表；无结果时为空数组。
      required:
        - search_results
    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            message:
              type: string
              description: 描述错误原因的错误消息
            type:
              type: string
              description: 错误类型
            code:
              type: string
              description: 错误码
          required:
            - message
      required:
        - error
    ToolsSearchTimeWindow:
      type: object
      description: 历史时间窗约束。start 与 end 均按周期第一天归一化后比较，start 不得晚于 end。
      properties:
        start:
          type: string
          description: 起始时间下限，格式 YYYY / YYYY-MM / YYYY-MM-DD。
        end:
          type: string
          description: 结束时间上限，格式 YYYY / YYYY-MM / YYYY-MM-DD。
    ToolsSearchProResult:
      type: object
      properties:
        authority:
          type: string
          description: 来源权威性等级。
        date:
          type: string
          description: 搜索结果日期。
        icon:
          type: string
          description: 站点图标 URL。
        mime:
          type: string
          description: 内容 MIME 类型。
        site_name:
          type: string
          description: 站点名称。
        snippet:
          type: string
          description: 搜索结果摘要。
        title:
          type: string
          description: 搜索结果标题。
        url:
          type: string
          description: 搜索结果链接。
        chunks:
          type: array
          items:
            $ref: '#/components/schemas/ToolsSearchProChunk'
          description: 结构化正文片段，按页面聚合；无正文时为空数组。
      required:
        - authority
        - date
        - icon
        - mime
        - site_name
        - snippet
        - title
        - url
        - chunks
    ToolsSearchProChunk:
      type: object
      properties:
        text:
          type: string
          description: 正文片段内容。
        score:
          type: number
          format: float
          description: 正文片段与查询词的相关性得分。
      required:
        - text
        - score
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Authorization 请求头需要一个 Bearer 令牌。使用 MOONSHOT_API_KEY 作为令牌。这是一个服务端密钥，请在
        [API 密钥页面](https://platform.kimi.com/console/api-keys) 生成。

````