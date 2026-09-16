> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 查询余额

> 查询当前账户的可用余额。

查询您在 Kimi 开放平台上的可用余额、代金券余额和现金余额。当可用余额小于等于 0 时，用户无法调用推理 API。

<Accordion title="调用示例">
  <CodeGroup>
    ```python python expandable theme={null}
    import os
    import requests

    api_key = os.environ.get("MOONSHOT_API_KEY")
    url = "https://api.moonshot.cn/v1/users/me/balance"

    response = requests.get(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
    )
    print(response.json())
    ```

    ```bash curl expandable theme={null}
    curl https://api.moonshot.cn/v1/users/me/balance \
      -H "Authorization: Bearer $MOONSHOT_API_KEY"
    ```

    ```javascript node.js expandable theme={null}
    const apiKey = process.env.MOONSHOT_API_KEY;

    async function main() {
        const response = await fetch("https://api.moonshot.cn/v1/users/me/balance", {
            method: "GET",
            headers: {
                Authorization: `Bearer ${apiKey}`,
            },
        });
        const data = await response.json();
        console.log(data);
    }

    main();
    ```
  </CodeGroup>
</Accordion>

<Accordion title="响应字段说明">
  | 字段                       | 类型      | 说明                                                                       |
  | ------------------------ | ------- | ------------------------------------------------------------------------ |
  | `code`                   | integer | 响应码。0 表示成功。                                                              |
  | `data`                   | object  | 余额数据对象                                                                   |
  | `data.available_balance` | number  | 可用余额（单位：人民币元），包含现金余额和代金券余额。当小于等于 0 时，用户无法调用推理 API                        |
  | `data.voucher_balance`   | number  | 代金券余额（单位：人民币元），不可为负                                                      |
  | `data.cash_balance`      | number  | 现金余额（单位：人民币元），可为负值表示欠费。当为负值时，`available_balance` 等于 `voucher_balance` 的值 |
  | `scode`                  | string  | 状态码                                                                      |
  | `status`                 | boolean | 请求状态                                                                     |

  **响应示例**

  ```json theme={null}
  {
      "code": 0,
      "data": {
          "available_balance": 49.58894,
          "voucher_balance": 46.58893,
          "cash_balance": 3.00001
      },
      "scode": "0x0",
      "status": true
  }
  ```
</Accordion>

<Warning>
  当 `available_balance` 小于等于 0 时，调用推理 API 将返回 `exceeded_current_quota_error` 错误。请及时充值或检查代金券有效期。
</Warning>

<Note>
  `platform.kimi.com`（国内站）与 `platform.kimi.ai`（国际站）申请的 API Key 完全独立，混用会返回 401 错误。请确认调用端点与 Key 所属平台一致。
</Note>


## OpenAPI

````yaml GET /v1/users/me/balance
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
  /v1/users/me/balance:
    get:
      tags:
        - Billing
      summary: 查询余额
      description: 查询您在 Kimi 开放平台上的可用余额、代金券余额和现金余额。
      responses:
        '200':
          description: 余额信息
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BalanceResponse'
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
    BalanceResponse:
      type: object
      properties:
        code:
          type: integer
          description: 响应码。0 表示成功。
        data:
          type: object
          properties:
            available_balance:
              type: number
              format: float
              description: 可用余额（单位：人民币元），包含现金余额和代金券余额。当小于等于 0 时，用户无法调用推理 API
              example: 49.58894
            voucher_balance:
              type: number
              format: float
              description: 代金券余额（单位：人民币元），不可为负
              example: 46.58893
            cash_balance:
              type: number
              format: float
              description: >-
                现金余额（单位：人民币元），可为负值表示欠费。当为负值时，available_balance 等于
                voucher_balance 的值
              example: 3.00001
          required:
            - available_balance
            - voucher_balance
            - cash_balance
        scode:
          type: string
          description: 状态码
          example: '0x0'
        status:
          type: boolean
          description: 请求状态
          example: true
      required:
        - code
        - data
        - scode
        - status
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