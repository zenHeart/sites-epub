> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 联网搜索 Basic

> 通过 /v1/tools/search 接口发起网页搜索，返回结构化搜索结果。

发起一次网页搜索，返回标题、摘要、站点、链接等结构化搜索结果列表，适用于需要自行编排搜索逻辑的 Agent 应用。

<Accordion title="调用示例">
  <CodeGroup>
    ```python python expandable theme={null}
    import os
    import requests

    api_key = os.environ.get("MOONSHOT_API_KEY")
    url = "https://api.moonshot.cn/v1/tools/search"

    response = requests.post(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "text_query": "Kimi K2 模型 发布",
            "limit": 5,
            "timeout_seconds": 10,
        },
    )
    print(response.json())
    ```

    ```bash curl expandable theme={null}
    curl https://api.moonshot.cn/v1/tools/search \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $MOONSHOT_API_KEY" \
      -d '{"text_query": "Kimi K2 模型 发布", "limit": 5, "timeout_seconds": 10}'
    ```

    ```javascript node.js expandable theme={null}
    const apiKey = process.env.MOONSHOT_API_KEY;

    async function main() {
        const response = await fetch("https://api.moonshot.cn/v1/tools/search", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${apiKey}`,
            },
            body: JSON.stringify({
                text_query: "Kimi K2 模型 发布",
                limit: 5,
                timeout_seconds: 10,
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
  | 字段                           | 类型             | 说明                                               |
  | ---------------------------- | -------------- | ------------------------------------------------ |
  | `search_results`             | array\[object] | 搜索结果列表；无结果时为空数组                                  |
  | `search_results[].authority` | string         | 来源权威性等级                                          |
  | `search_results[].date`      | string         | 搜索结果日期                                           |
  | `search_results[].icon`      | string         | 站点图标 URL                                         |
  | `search_results[].mime`      | string         | 内容 MIME 类型                                       |
  | `search_results[].site_name` | string         | 站点名称                                             |
  | `search_results[].snippet`   | string         | 搜索结果摘要                                           |
  | `search_results[].text`      | string         | 网页正文内容；`include_content=true` 时返回，为 false 时为空字符串 |
  | `search_results[].title`     | string         | 搜索结果标题                                           |
  | `search_results[].url`       | string         | 搜索结果链接                                           |

  以上字符串字段在无数据时返回空字符串。

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
              "text": "",
              "title": "API 概述 - Kimi API 开放平台",
              "url": "https://platform.kimi.com/docs/api/overview"
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
  | HTTP 状态码 | error.type               | 典型 message                                         | 说明                                                                                            |
  | -------- | ------------------------ | -------------------------------------------------- | --------------------------------------------------------------------------------------------- |
  | 400      | `invalid_request`        | `invalid request body`                             | 请求体不是合法 JSON                                                                                  |
  | 400      | `invalid_request`        | `text_query is required`                           | 缺少搜索查询文本                                                                                      |
  | 400      | `invalid_request`        | `timeout_seconds must be less than or equal to 60` | `timeout_seconds` 取值范围为 1-60                                                                  |
  | 400      | `invalid_request`        | `limit must be between 1 and 20`                   | `limit` 取值范围为 1-20                                                                            |
  | 401      | -                        | 无错误响应体                                             | API Key 缺失或无效                                                                                 |
  | 403      | -                        | 无错误响应体                                             | 账号未激活或已停用                                                                                     |
  | 408      | `client_canceled`        | `client canceled the request`                      | 客户端在服务端返回前断开连接                                                                                |
  | 429      | `rate_limited`           | `project qps limit exceeded`                       | 触发频率或并发限制；响应头携带 `X-RateLimit-Limit`、`X-RateLimit-Remaining`，触发每秒请求数限制时还携带 `X-RateLimit-Reset` |
  | 429      | `rate_limit_unavailable` | `rate limit store unavailable`                     | 限速服务暂时不可用，请稍后重试                                                                               |
  | 500      | `internal_error`         | 内部错误原文                                             | 服务内部错误，请稍后重试；若持续出现，请携带 `X-Msh-Track-Id` 联系支持团队                                                |
  | 502      | `upstream_failed`        | `upstream service failed`                          | 服务暂时不可用，请稍后重试                                                                                 |
  | 504      | `timeout`                | `request timeout`                                  | 搜索超时；可调大 `timeout_seconds` 或精简查询后重试                                                           |
</Accordion>

<Note>
  计费说明：请求成功（HTTP 200）且 `search_results` 非空时，计费一次；请求失败或未返回结果时不计费。具体价格详见[联网搜索定价](/docs/pricing/websearch)。
</Note>


## OpenAPI

````yaml POST /v1/tools/search
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
  /v1/tools/search:
    post:
      tags:
        - Tools
      summary: 联网搜索 Basic
      description: >-
        发起一次网页搜索，返回标题、摘要、站点、链接等结构化搜索结果。请求成功且返回结果数大于 0
        时计费一次，失败或无结果不计费，详见[联网搜索定价](/pricing/tools)。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ToolsSearchRequest'
      responses:
        '200':
          description: 搜索结果
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
                $ref: '#/components/schemas/ToolsSearchResponse'
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
    ToolsSearchRequest:
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
        include_content:
          type: boolean
          default: false
          description: 是否在结果项 text 中返回网页正文，默认 false。
      required:
        - text_query
    ToolsSearchResponse:
      type: object
      properties:
        search_results:
          type: array
          items:
            $ref: '#/components/schemas/ToolsSearchResult'
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
    ToolsSearchResult:
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
        text:
          type: string
          description: 网页正文内容；include_content=true 时返回，为 false 时为空字符串。
        title:
          type: string
          description: 搜索结果标题。
        url:
          type: string
          description: 搜索结果链接。
      required:
        - authority
        - date
        - icon
        - mime
        - site_name
        - snippet
        - text
        - title
        - url
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Authorization 请求头需要一个 Bearer 令牌。使用 MOONSHOT_API_KEY 作为令牌。这是一个服务端密钥，请在
        [API 密钥页面](https://platform.kimi.com/console/api-keys) 生成。

````