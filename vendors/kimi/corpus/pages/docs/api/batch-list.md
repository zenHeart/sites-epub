> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 列出批处理任务

> 列出当前账户的批处理任务。

列出当前组织下的所有批处理任务，支持分页查询。常用于查看任务列表、检查批量任务状态或进行批量管理。

<Accordion title="调用示例">
  <CodeGroup>
    ```python Python theme={null}
    import os
    from openai import OpenAI
    from openai.pagination import SyncCursorPage
    from openai.types import Batch

    client = OpenAI(
        api_key=os.environ.get("MOONSHOT_API_KEY"),
        base_url=os.environ.get("MOONSHOT_BASE_URL", "https://api.moonshot.cn/v1"),
    )

    batches: SyncCursorPage[Batch] = client.batches.list(limit=10)
    for batch in batches.data:
        print(f"{batch.id} - {batch.status} ({batch.request_counts.completed}/{batch.request_counts.total})")
    ```

    ```bash cURL theme={null}
    curl "${MOONSHOT_BASE_URL:-https://api.moonshot.cn/v1}/batches?limit=10" \
      -H "Authorization: Bearer $MOONSHOT_API_KEY"
    ```

    ```javascript Node.js theme={null}
    const OpenAI = require("openai");

    const client = new OpenAI({
        apiKey: process.env.MOONSHOT_API_KEY,
        baseURL: process.env.MOONSHOT_BASE_URL || "https://api.moonshot.cn/v1",
    });

    async function main() {
        const batches = await client.batches.list({ limit: 10 });
        for (const batch of batches.data) {
            console.log(`${batch.id} - ${batch.status} (${batch.request_counts.completed}/${batch.request_counts.total})`);
        }
    }

    main();
    ```
  </CodeGroup>
</Accordion>

<Accordion title="响应字段说明">
  列出任务接口返回一个分页列表对象，包含以下字段：

  | 字段         | 类型             | 说明                                                                  |
  | ---------- | -------------- | ------------------------------------------------------------------- |
  | `object`   | string         | 对象类型，固定为 `"list"`                                                   |
  | `data`     | array\[object] | 批处理任务列表，每个元素为 `BatchObject` 对象，字段含义与[获取任务详情](/docs/api/batch-retrieve)一致 |
  | `has_more` | boolean        | 是否还有更多数据。为 `true` 时，可通过 `after` 参数传入本页最后一个 `batch.id` 获取下一页         |

  **响应示例**

  ```json theme={null}
  {
      "object": "list",
      "data": [
          {
              "id": "batch_xxx",
              "object": "batch",
              "endpoint": "/v1/chat/completions",
              "input_file_id": "file_xxx",
              "completion_window": "24h",
              "status": "completed",
              "output_file_id": "file_yyy",
              "error_file_id": null,
              "created_at": 1711475054,
              "in_progress_at": 1711475055,
              "expires_at": 1711561454,
              "finalizing_at": 1711475100,
              "completed_at": 1711475110,
              "failed_at": null,
              "cancelling_at": null,
              "cancelled_at": null,
              "request_counts": {
                  "completed": 100,
                  "failed": 0,
                  "total": 100
              },
              "metadata": null
          }
      ],
      "has_more": false
  }
  ```
</Accordion>

<Note>
  完整的调用示例和状态流转说明，请参考 [Batch API 指南](/docs/guide/use-batch-api)。
</Note>

<Warning>
  当 `has_more` 为 `true` 时，需要通过 `after` 参数进行分页查询。将上一页最后一个 `batch.id` 作为 `after` 的值传入，即可获取下一页结果。若省略 `after` 参数，每次查询均返回第一页。
</Warning>


## OpenAPI

````yaml GET /v1/batches
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
  /v1/batches:
    get:
      tags:
        - Batch
      summary: 列出批处理任务
      description: 列出当前组织的批处理任务。
      parameters:
        - name: after
          in: query
          required: false
          description: 分页游标，传入上一页最后一个 batch 的 ID
          schema:
            type: string
        - name: limit
          in: query
          required: false
          description: 每页数量，默认 20
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: 批处理任务列表
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchListResponse'
        '401':
          description: 未授权 - API 密钥无效或缺失
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
    BatchListResponse:
      type: object
      properties:
        object:
          type: string
          example: list
        data:
          type: array
          items:
            $ref: '#/components/schemas/BatchObject'
        has_more:
          type: boolean
          description: 是否还有更多数据
      required:
        - object
        - data
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