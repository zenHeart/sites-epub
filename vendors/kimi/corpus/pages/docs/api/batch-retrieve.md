> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取批处理任务详情

> 获取指定批处理任务的详情与进度。

获取指定批处理任务的当前状态、进度统计和详细元数据。通常用于创建任务后轮询任务是否完成。

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

    batch: Batch = client.batches.retrieve("your_batch_id")
    print(f"状态: {batch.status}")
    print(f"进度: {batch.request_counts.completed}/{batch.request_counts.total}")
    ```

    ```bash cURL theme={null}
    curl ${MOONSHOT_BASE_URL:-https://api.moonshot.cn/v1}/batches/your_batch_id \
      -H "Authorization: Bearer $MOONSHOT_API_KEY"
    ```

    ```javascript Node.js theme={null}
    const OpenAI = require("openai");

    const client = new OpenAI({
        apiKey: process.env.MOONSHOT_API_KEY,
        baseURL: process.env.MOONSHOT_BASE_URL || "https://api.moonshot.cn/v1",
    });

    async function main() {
        const batch = await client.batches.retrieve("your_batch_id");
        console.log(`状态: ${batch.status}`);
        console.log(`进度: ${batch.request_counts.completed}/${batch.request_counts.total}`);
    }

    main();
    ```
  </CodeGroup>
</Accordion>

<Accordion title="响应字段说明">
  | 字段                  | 类型              | 说明                                                                                                                                              |
  | ------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
  | `id`                | string          | 批处理任务的唯一标识符                                                                                                                                     |
  | `object`            | string          | 对象类型，固定为 `batch`                                                                                                                                |
  | `endpoint`          | string          | 请求端点                                                                                                                                            |
  | `input_file_id`     | string          | 输入文件 ID                                                                                                                                         |
  | `completion_window` | string          | 任务处理时间窗口                                                                                                                                        |
  | `status`            | string          | 当前状态：`validating`（校验中）、`failed`（校验失败）、`in_progress`（执行中）、`finalizing`（准备结果中）、`completed`（已完成）、`expired`（已过期）、`cancelling`（取消中）、`cancelled`（已取消） |
  | `output_file_id`    | string \| null  | 处理成功的结果文件 ID                                                                                                                                    |
  | `error_file_id`     | string \| null  | 处理失败的错误文件 ID                                                                                                                                    |
  | `created_at`        | integer         | 创建时间（Unix 时间戳）                                                                                                                                  |
  | `in_progress_at`    | integer \| null | 开始执行时间（Unix 时间戳）                                                                                                                                |
  | `expires_at`        | integer \| null | 过期时间（Unix 时间戳）                                                                                                                                  |
  | `finalizing_at`     | integer \| null | 开始准备结果的时间（Unix 时间戳）                                                                                                                             |
  | `completed_at`      | integer \| null | 完成时间（Unix 时间戳）                                                                                                                                  |
  | `failed_at`         | integer \| null | 校验失败时间（Unix 时间戳）                                                                                                                                |
  | `cancelling_at`     | integer \| null | 发起取消时间（Unix 时间戳）                                                                                                                                |
  | `cancelled_at`      | integer \| null | 取消完成时间（Unix 时间戳）                                                                                                                                |
  | `request_counts`    | object          | 请求数量统计，包含 `completed`（已完成）、`failed`（失败）、`total`（总数）                                                                                             |
  | `metadata`          | object \| null  | 自定义元数据                                                                                                                                          |
</Accordion>

<Note>
  完整的调用示例和轮询脚本请参考 [Batch API 指南](/docs/guide/use-batch-api)。
</Note>

<Warning>
  当 `status` 为 `completed` 时，`output_file_id` 包含结果文件 ID；当 `status` 为 `failed` 时，建议查看 `error_file_id` 获取错误详情。如果指定的 `batch_id` 不存在，接口将返回 `404` 错误（`resource_not_found_error`）。
</Warning>


## OpenAPI

````yaml GET /v1/batches/{batch_id}
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
  /v1/batches/{batch_id}:
    get:
      tags:
        - Batch
      summary: 获取批处理任务详情
      description: 获取指定批处理任务的状态和详细信息。
      parameters:
        - name: batch_id
          in: path
          required: true
          description: 批处理任务的 ID
          schema:
            type: string
      responses:
        '200':
          description: 批处理任务详情
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchObject'
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