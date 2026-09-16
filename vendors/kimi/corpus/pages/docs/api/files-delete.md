> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 删除文件

> 删除指定的已上传文件。

删除一个已上传的文件。删除成功后，该文件将不再占用存储空间，也无法继续用于对话或 Batch 等场景。

<Accordion title="调用示例">
  <Tabs>
    <Tab title="python">
      ```python showLineNumbers expandable theme={null}
      import os
      from openai import OpenAI

      client = OpenAI(
          api_key=os.environ.get("MOONSHOT_API_KEY"),
          base_url="https://api.moonshot.cn/v1",
      )

      # 删除指定文件
      delete_result = client.files.delete(file_id="file_xxx")
      print(delete_result)
      ```
    </Tab>

    <Tab title="curl">
      ```bash showLineNumbers theme={null}
      curl -X DELETE https://api.moonshot.cn/v1/files/file_xxx \
        -H "Authorization: Bearer $MOONSHOT_API_KEY"
      ```
    </Tab>

    <Tab title="node.js">
      ```js showLineNumbers expandable theme={null}
      const OpenAI = require("openai");

      const client = new OpenAI({
          apiKey: process.env.MOONSHOT_API_KEY,
          baseURL: "https://api.moonshot.cn/v1",
      });

      async function main() {
          const deleteResult = await client.files.delete({
              file_id: "file_xxx",
          });
          console.log(deleteResult);
      }

      main();
      ```
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="响应字段说明">
  删除文件接口返回一个 JSON 对象，包含以下字段：

  | 字段        | 类型      | 说明           |
  | --------- | ------- | ------------ |
  | `id`      | string  | 已删除文件的标识符    |
  | `object`  | string  | 固定为 `"file"` |
  | `deleted` | boolean | 文件是否删除成功     |

  **响应示例**

  ```json theme={null}
  {
      "id": "file_xxx",
      "object": "file",
      "deleted": true
  }
  ```
</Accordion>

<Note>
  删除操作不可撤销。已上传文件会占用组织总存储配额（默认 10 GiB）；达到配额上限后，新的上传会被拒绝。删除不再使用的文件可以释放配额。
</Note>

<Warning>
  如果文件不存在或已被删除，接口将返回 `404` 错误。请确认 `file_id` 正确无误。
</Warning>


## OpenAPI

````yaml DELETE /v1/files/{file_id}
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
  /v1/files/{file_id}:
    delete:
      tags:
        - Files
      summary: 删除文件
      description: 删除一个已上传的文件。
      parameters:
        - name: file_id
          in: path
          required: true
          description: 文件标识符
          schema:
            type: string
      responses:
        '200':
          description: 删除结果
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileDeleteResponse'
        '401':
          description: 未授权 - API 密钥无效或缺失
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: 文件未找到
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
    FileDeleteResponse:
      type: object
      properties:
        id:
          type: string
          description: 已删除文件的标识符
        object:
          type: string
          example: file
        deleted:
          type: boolean
          description: 文件是否删除成功
      required:
        - id
        - object
        - deleted
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