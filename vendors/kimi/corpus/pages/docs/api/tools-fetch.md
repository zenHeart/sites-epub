> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 网页抓取

> 通过 /v1/tools/fetch 接口抓取指定 URL 的网页内容，返回页面标题与 Markdown 格式正文。

抓取指定 URL 的网页内容，返回页面标题与 Markdown 格式正文，适用于网页阅读、资料整理等内容提取场景。

<Warning>
  仅支持 `http` 和 `https` 协议的 URL。触发安全风控的 URL 会返回 403 `security_risk` 错误；页面无可提取正文时返回 404 `markdown_not_found` 错误。
</Warning>

<Accordion title="调用示例">
  <CodeGroup>
    ```python python expandable theme={null}
    import os
    import requests

    api_key = os.environ.get("MOONSHOT_API_KEY")
    url = "https://api.moonshot.cn/v1/tools/fetch"

    response = requests.post(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        json={"url": "https://platform.kimi.com/docs/api/overview"},
    )
    print(response.json())
    ```

    ```bash curl expandable theme={null}
    curl https://api.moonshot.cn/v1/tools/fetch \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $MOONSHOT_API_KEY" \
      -d '{"url": "https://platform.kimi.com/docs/api/overview"}'
    ```

    ```javascript node.js expandable theme={null}
    const apiKey = process.env.MOONSHOT_API_KEY;

    async function main() {
        const response = await fetch("https://api.moonshot.cn/v1/tools/fetch", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${apiKey}`,
            },
            body: JSON.stringify({
                url: "https://platform.kimi.com/docs/api/overview",
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
  | 字段         | 类型     | 说明                                                                |
  | ---------- | ------ | ----------------------------------------------------------------- |
  | `url`      | string | 抓取 URL                                                            |
  | `markdown` | string | 抓取结果的 Markdown 内容；文本与图片按在页面中出现的顺序拼接，图片以占位符形式嵌入（格式见下方示例），各段之间以空行分隔 |
  | `title`    | string | 页面标题                                                              |

  **响应示例**

  ```json theme={null}
  {
      "url": "https://platform.kimi.com/docs/api/overview",
      "markdown": "# API 概述\n\nKimi API 开放平台文档入口。",
      "title": "API 概述 - Kimi API 开放平台"
  }
  ```

  **markdown 内容形态示例**

  ```text theme={null}
  # API 概述

  Kimi API 开放平台文档入口。

  ![image1](https://platform.kimi.com/assets/logo/dark.svg)

  更多正文内容……
  ```

  **通用响应头**

  | 响应头              | 说明                                             |
  | ---------------- | ---------------------------------------------- |
  | `X-Msh-Track-Id` | 请求 ID；请求携带同名头时沿用，否则由服务端生成。排查问题时请提供该 ID         |
  | `X-Msh-Chat-Id`  | 会话 ID，固定为 `toolgw-{X-Msh-Track-Id}`；排查问题时请一并提供 |

  以上两个响应头在所有响应（包括错误响应）中均会携带。
</Accordion>

<Accordion title="错误码说明">
  | HTTP 状态码 | error.type               | 典型 message                                                                                                | 说明                                                                                            |
  | -------- | ------------------------ | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
  | 400      | `invalid_request`        | `invalid request body`                                                                                    | 请求体不是合法 JSON                                                                                  |
  | 400      | `invalid_url`            | `The provided URL is invalid: only http and https are supported`                                          | URL 为空或协议非 http/https                                                                         |
  | 400      | `invalid_url`            | `The provided URL is invalid: missing host`                                                               | URL 缺少主机名                                                                                     |
  | 401      | -                        | 无错误响应体                                                                                                    | API Key 缺失或无效                                                                                 |
  | 403      | -                        | 无错误响应体                                                                                                    | 账号未激活或已停用                                                                                     |
  | 403      | `security_risk`          | `We consider the current URL poses a security risk and are unable to provide fetch service at this time.` | URL 触发安全风控，请更换 URL                                                                            |
  | 404      | `markdown_not_found`     | `No text/markdown content found for the current URL.`                                                     | 页面无可提取的正文内容                                                                                   |
  | 408      | `client_canceled`        | `client canceled the request`                                                                             | 客户端在服务端返回前断开连接                                                                                |
  | 429      | `rate_limited`           | `project concurrency limit exceeded`                                                                      | 触发频率或并发限制；响应头携带 `X-RateLimit-Limit`、`X-RateLimit-Remaining`，触发每秒请求数限制时还携带 `X-RateLimit-Reset` |
  | 429      | `rate_limit_unavailable` | `rate limit store unavailable`                                                                            | 限速服务暂时不可用，请稍后重试                                                                               |
  | 500      | `internal_error`         | 内部错误原文                                                                                                    | 服务内部错误，请稍后重试；若持续出现，请携带 `X-Msh-Track-Id` 联系支持团队                                                |
  | 502      | `upstream_failed`        | `upstream service failed`                                                                                 | 服务暂时不可用，请稍后重试                                                                                 |
  | 504      | `timeout`                | `request timeout`                                                                                         | 抓取超时，请稍后重试                                                                                    |
</Accordion>

<Note>
  计费说明：请求成功（HTTP 200）且返回的 `markdown` 非空白时，计费一次；请求失败或页面无正文内容时不计费。具体价格详见[联网搜索定价](/docs/pricing/websearch)。
</Note>


## OpenAPI

````yaml POST /v1/tools/fetch
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
  /v1/tools/fetch:
    post:
      tags:
        - Tools
      summary: 网页抓取
      description: >-
        抓取指定 URL 的网页内容，返回页面标题与 Markdown 格式正文（文本与图片按序拼接）。仅支持 http 和 https
        协议。请求成功且抓取到正文内容时计费一次，失败或无内容不计费，详见[联网搜索定价](/pricing/tools)。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ToolsFetchRequest'
      responses:
        '200':
          description: 抓取结果
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
                $ref: '#/components/schemas/ToolsFetchResponse'
        '400':
          description: 请求错误 - 参数无效或 URL 不合法
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: 未授权 - API 密钥无效或缺失（直接返回状态码，无错误响应体）
        '403':
          description: 禁止访问 - 账号未激活或已停用（无错误响应体），或 URL 触发安全风控（返回 security_risk 错误）
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: 未找到可提取的正文内容（markdown_not_found）
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
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
    ToolsFetchRequest:
      type: object
      properties:
        url:
          type: string
          format: uri
          description: 要抓取的网页 URL，仅支持 http 和 https 协议。
      required:
        - url
    ToolsFetchResponse:
      type: object
      properties:
        url:
          type: string
          description: 抓取 URL。
        markdown:
          type: string
          description: 抓取结果的 Markdown 内容；文本与图片按在页面中出现的顺序拼接，图片以 `![imageN](url)` 形式占位。
        title:
          type: string
          description: 页面标题。
      required:
        - url
        - markdown
        - title
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Authorization 请求头需要一个 Bearer 令牌。使用 MOONSHOT_API_KEY 作为令牌。这是一个服务端密钥，请在
        [API 密钥页面](https://platform.kimi.com/console/api-keys) 生成。

````