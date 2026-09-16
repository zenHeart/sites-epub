> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 列出模型

> 列出当前可用的模型及其 ID。

列出当前可用的所有模型，包含模型 ID、上下文长度及能力标识等信息。建议在调用对话补全前查询本接口，以确认目标模型是否可用及具备对应能力。

<Accordion title="调用示例">
  <CodeGroup>
    ```python python expandable theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("MOONSHOT_API_KEY"),
        base_url="https://api.moonshot.cn/v1",
    )

    models = client.models.list()
    print(models.data)
    ```

    ```bash curl expandable theme={null}
    curl https://api.moonshot.cn/v1/models \
        -H "Authorization: Bearer $MOONSHOT_API_KEY"
    ```

    ```javascript node.js expandable theme={null}
    const OpenAI = require("openai");

    const client = new OpenAI({
        apiKey: process.env.MOONSHOT_API_KEY,
        baseURL: "https://api.moonshot.cn/v1",
    });

    async function main() {
        const models = await client.models.list();
        console.log(models.data);
    }

    main();
    ```
  </CodeGroup>
</Accordion>

<Accordion title="响应字段说明">
  响应为一个对象，包含以下字段：

  | 字段       | 类型             | 说明                |
  | -------- | -------------- | ----------------- |
  | `object` | string         | 对象类型，固定为 `"list"` |
  | `data`   | array\[object] | 模型列表，每个元素为一个模型对象  |

  `data` 数组中每个模型对象的字段说明：

  | 字段                   | 类型      | 说明                      |
  | -------------------- | ------- | ----------------------- |
  | `id`                 | string  | 模型 ID，例如 `kimi-k3`      |
  | `object`             | string  | 对象类型，固定为 `"model"`      |
  | `created`            | integer | 模型创建时的 Unix 时间戳         |
  | `owned_by`           | string  | 模型所有者标识，例如 `"moonshot"` |
  | `context_length`     | integer | 模型支持的最大上下文长度（tokens）    |
  | `supports_image_in`  | boolean | 是否支持图片输入                |
  | `supports_video_in`  | boolean | 是否支持视频输入                |
  | `supports_reasoning` | boolean | 是否支持深度思考                |
</Accordion>

<Note>
  模型列表及能力标识可能随平台更新而变化。若调用对话补全时收到 `resource_not_found_error`（404），说明模型不存在或当前账号无权限访问，请检查 `model` 参数拼写及账号 tier。
</Note>

<Warning>
  本接口需要有效的 API Key 进行认证。若收到 401 错误，请检查 `Authorization` 请求头是否为 `Bearer <MOONSHOT_API_KEY>`，并确认 API Key 与调用端点所属平台一致（`platform.kimi.com` 与 `platform.kimi.ai` 的 Key 不可混用）。
</Warning>


## OpenAPI

````yaml GET /v1/models
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
  /v1/models:
    get:
      tags:
        - Models
      summary: 列出模型
      description: 列出当前可用的所有模型。
      responses:
        '200':
          description: 模型列表
          content:
            application/json:
              schema:
                type: object
                properties:
                  object:
                    type: string
                    example: list
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: 模型 ID
                          example: kimi-k3
                        object:
                          type: string
                          example: model
                        created:
                          type: integer
                          description: 创建时间戳
                        owned_by:
                          type: string
                          example: moonshot
                        context_length:
                          type: integer
                          description: 最大上下文长度（tokens）
                        supports_image_in:
                          type: boolean
                          description: 是否支持图片输入
                        supports_video_in:
                          type: boolean
                          description: 是否支持视频输入
                        supports_reasoning:
                          type: boolean
                          description: 是否支持深度思考
        '401':
          description: 未授权 - API 密钥无效或缺失
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - bearerAuth: []
components:
  schemas:
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