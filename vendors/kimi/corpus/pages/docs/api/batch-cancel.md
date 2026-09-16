> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 取消批处理任务

> 取消一个进行中的批处理任务。

取消一个正在进行的批处理任务。取消后，任务状态将先变为 `cancelling`，最终变为 `cancelled`。仅 `validating`、`in_progress`、`finalizing` 状态的任务可以取消。

<Accordion title="调用示例">
  <CodeGroup>
    ```python Python theme={null}
    import os
    from openai import OpenAI
    from openai.types import Batch

    client = OpenAI(
        api_key=os.environ.get("MOONSHOT_API_KEY"),
        base_url=os.environ.get("MOONSHOT_BASE_URL", "https://api.moonshot.cn/v1"),
    )

    batch: Batch = client.batches.cancel("your_batch_id")
    print(f"状态: {batch.status}")  # cancelling
    ```

    ```bash cURL theme={null}
    curl -X POST ${MOONSHOT_BASE_URL:-https://api.moonshot.cn/v1}/batches/your_batch_id/cancel \
      -H "Authorization: Bearer $MOONSHOT_API_KEY"
    ```

    ```javascript Node.js theme={null}
    const OpenAI = require("openai");

    const client = new OpenAI({
        apiKey: process.env.MOONSHOT_API_KEY,
        baseURL: process.env.MOONSHOT_BASE_URL || "https://api.moonshot.cn/v1",
    });

    async function main() {
        const batch = await client.batches.cancel("your_batch_id");
        console.log(`状态: ${batch.status}`);  // cancelling
    }

    main();
    ```
  </CodeGroup>
</Accordion>

<Accordion title="响应字段说明">
  调用成功后，接口返回一个 `BatchObject` 对象，包含以下字段：

  | 字段                  | 类型              | 说明                                                |
  | ------------------- | --------------- | ------------------------------------------------- |
  | `id`                | string          | 批处理任务的唯一标识符                                       |
  | `object`            | string          | 对象类型，固定为 `batch`                                  |
  | `endpoint`          | string          | 请求端点                                              |
  | `input_file_id`     | string          | 输入文件 ID                                           |
  | `completion_window` | string          | 任务处理时间窗口                                          |
  | `status`            | string          | 当前状态。取消请求成功后通常为 `cancelling`，最终变为 `cancelled`     |
  | `output_file_id`    | string \| null  | 处理成功的结果文件 ID                                      |
  | `error_file_id`     | string \| null  | 处理失败的错误文件 ID                                      |
  | `created_at`        | integer         | 创建时间（Unix 时间戳）                                    |
  | `in_progress_at`    | integer \| null | 开始执行时间（Unix 时间戳）                                  |
  | `expires_at`        | integer \| null | 过期时间（Unix 时间戳）                                    |
  | `finalizing_at`     | integer \| null | 开始准备结果的时间（Unix 时间戳）                               |
  | `completed_at`      | integer \| null | 完成时间（Unix 时间戳）                                    |
  | `failed_at`         | integer \| null | 校验失败时间（Unix 时间戳）                                  |
  | `cancelling_at`     | integer \| null | 发起取消时间（Unix 时间戳）                                  |
  | `cancelled_at`      | integer \| null | 取消完成时间（Unix 时间戳）                                  |
  | `request_counts`    | object          | 请求计数，包含 `completed`（已完成）、`failed`（失败）、`total`（总数） |
  | `metadata`          | object \| null  | 自定义元数据                                            |
</Accordion>

<Warning>
  仅 `validating`、`in_progress`、`finalizing` 状态的任务可以取消。若任务已处于 `completed`、`failed`、`expired` 或 `cancelled` 状态，调用此接口将返回 400 错误。
</Warning>

<Note>
  **常见错误说明**

  * **400 请求错误**：任务状态不允许取消，或请求参数无效。请确认任务状态后再发起取消。
  * **401 未授权**：API Key 无效或缺失。请检查 `Authorization: Bearer <key>` 是否正确。
  * **404 未找到**：指定的 `batch_id` 不存在。请确认 ID 拼写正确且该任务属于当前组织。
  * **500 服务器错误**：服务端内部错误，请稍后重试；若持续出现，请附带 `request_id` 联系支持团队。

  详见 [常见错误码说明](/docs/api/errors)。
</Note>

完整的调用示例和状态流转说明，请参考 [Batch API 指南](/docs/guide/use-batch-api)。


## OpenAPI

````yaml POST /v1/batches/{batch_id}/cancel
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
  /v1/batches/{batch_id}/cancel:
    post:
      tags:
        - Batch
      summary: 取消批处理任务
      description: >-
        取消一个正在进行的批处理任务。取消后，任务状态将先变为 cancelling，最终变为 cancelled。仅
        validating、in_progress、finalizing 状态的任务可以取消。
      parameters:
        - name: batch_id
          in: path
          required: true
          description: 批处理任务的 ID
          schema:
            type: string
      responses:
        '200':
          description: 已取消的批处理任务
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchObject'
        '400':
          description: 请求错误 - 任务状态不允许取消
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: 未授权 - API 密钥无效或缺失
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: 批处理任务未找到
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
      security:
        - bearerAuth: []
components:
  schemas:
    BatchObject:
      type: object
      properties:
        id:
          type: string
          description: 批处理任务的唯一标识符
        object:
          type: string
          description: 对象类型，固定为 batch
          example: batch
        endpoint:
          type: string
          description: 请求端点
        input_file_id:
          type: string
          description: 输入文件 ID
        completion_window:
          type: string
          description: 任务处理时间窗口
        status:
          type: string
          description: >-
            当前状态：validating（校验中）、failed（校验失败）、in_progress（执行中）、finalizing（准备结果中）、completed（已完成）、expired（已过期）、cancelling（取消中）、cancelled（已取消）
          enum:
            - validating
            - failed
            - in_progress
            - finalizing
            - completed
            - expired
            - cancelling
            - cancelled
        output_file_id:
          type:
            - string
            - 'null'
          description: 处理成功的结果文件 ID
        error_file_id:
          type:
            - string
            - 'null'
          description: 处理失败的错误文件 ID
        created_at:
          type: integer
          description: 创建时间（Unix 时间戳）
        in_progress_at:
          type:
            - integer
            - 'null'
          description: 开始执行时间（Unix 时间戳）
        expires_at:
          type:
            - integer
            - 'null'
          description: 过期时间（Unix 时间戳）
        finalizing_at:
          type:
            - integer
            - 'null'
          description: 开始准备结果的时间（Unix 时间戳）
        completed_at:
          type:
            - integer
            - 'null'
          description: 完成时间（Unix 时间戳）
        failed_at:
          type:
            - integer
            - 'null'
          description: 校验失败时间（Unix 时间戳）
        cancelling_at:
          type:
            - integer
            - 'null'
          description: 发起取消时间（Unix 时间戳）
        cancelled_at:
          type:
            - integer
            - 'null'
          description: 取消完成时间（Unix 时间戳）
        request_counts:
          $ref: '#/components/schemas/BatchRequestCounts'
        metadata:
          type:
            - object
            - 'null'
          description: 自定义元数据
          additionalProperties:
            type: string
      required:
        - id
        - object
        - endpoint
        - input_file_id
        - completion_window
        - status
        - created_at
        - request_counts
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
    BatchRequestCounts:
      type: object
      properties:
        completed:
          type: integer
          description: 已完成的请求数量
        failed:
          type: integer
          description: 失败的请求数量
        total:
          type: integer
          description: 总请求数量
      required:
        - completed
        - failed
        - total
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Authorization 请求头需要一个 Bearer 令牌。使用 MOONSHOT_API_KEY 作为令牌。这是一个服务端密钥，请在
        [API 密钥页面](https://platform.kimi.com/console/api-keys) 生成。

````