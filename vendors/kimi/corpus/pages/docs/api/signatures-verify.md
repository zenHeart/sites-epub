> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 校验请求签名

> 校验 Kimi API 返回的请求签名，证明请求确实由 Kimi API 处理且请求的是指定模型，而非被转发到其他服务。

请求签名（Request Signature）用于证明一次请求确实到达了 Kimi API 本身，而不是被中间层转发到了其他服务或替换了模型。持有 nonce、时间戳、模型和签名的任何一方，都可以通过本接口验证 Kimi API 是否在该时间点以指定模型接受了这个请求，例如向用户或第三方证明服务背后调用的是 Kimi 官方 API、核验代理层没有偷换模型，或用于事后审计与争议举证。

调用 [Chat Completions](/docs/api/chat)、[Responses](/docs/api/responses) 或 [Messages](/docs/api/messages) API 时，在请求头 `X-Msh-Request-Nonce` 中携带一个随机 nonce（推荐使用 UUID v4），响应头中就会返回 `Msh-Request-Timestamp`（Kimi API 接受该请求时的 Unix 毫秒时间戳）和 `Msh-Request-Signature`（以 `reqsigv1_` 为前缀的签名 token），流式与非流式均支持。之后将 nonce、timestamp、请求中的 `model` 和 signature 提交到本接口，签名与三者完全一致时返回 `valid: true`，否则返回 `valid: false`。

签名只证明 Kimi API 在该时间点接受了这个 nonce 和请求模型，不证明请求最终成功或响应内容完整。服务端不记录 nonce，重放同一组参数仍会返回 `valid: true`，防重放和有效时间窗口需由调用方自行控制。

<Accordion title="调用示例">
  <CodeGroup>
    ```python python expandable theme={null}
    import os
    import uuid

    import requests
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ["MOONSHOT_API_KEY"],
        base_url="https://api.moonshot.cn/v1",
    )

    nonce: str = str(uuid.uuid4())
    model: str = "kimi-k2.7-code"

    # 1. 携带 X-Msh-Request-Nonce 调用模型接口，并读取响应头
    raw = client.chat.completions.with_raw_response.create(
        model=model,
        messages=[{"role": "user", "content": "你好"}],
        extra_headers={"X-Msh-Request-Nonce": nonce},
    )
    timestamp: int = int(raw.headers["Msh-Request-Timestamp"])
    signature: str = raw.headers["Msh-Request-Signature"]

    # 2. 校验签名
    verify = requests.post(
        "https://api.moonshot.cn/v1/signatures/verify",
        headers={
            "Authorization": f"Bearer {os.environ['MOONSHOT_API_KEY']}",
            "Content-Type": "application/json",
        },
        json={
            "nonce": nonce,
            "timestamp": timestamp,
            "model": model,
            "signature": signature,
        },
    )
    print(verify.json())  # {"valid": true}
    ```

    ```bash curl expandable theme={null}
    NONCE="$(uuidgen)"
    MODEL="kimi-k2.7-code"

    # 1. 携带 X-Msh-Request-Nonce 调用模型接口，并把响应头保存到文件
    curl -sS -D response.headers -o response.json \
      https://api.moonshot.cn/v1/chat/completions \
      -H "Authorization: Bearer $MOONSHOT_API_KEY" \
      -H "Content-Type: application/json" \
      -H "X-Msh-Request-Nonce: $NONCE" \
      -d "{\"model\": \"$MODEL\", \"messages\": [{\"role\": \"user\", \"content\": \"你好\"}]}"

    TIMESTAMP="$(awk -F': ' 'tolower($1)=="msh-request-timestamp" {gsub("\\r", "", $2); print $2}' response.headers)"
    SIGNATURE="$(awk -F': ' 'tolower($1)=="msh-request-signature" {gsub("\\r", "", $2); print $2}' response.headers)"

    # 2. 校验签名
    curl -sS https://api.moonshot.cn/v1/signatures/verify \
      -H "Authorization: Bearer $MOONSHOT_API_KEY" \
      -H "Content-Type: application/json" \
      -d "{\"nonce\": \"$NONCE\", \"timestamp\": $TIMESTAMP, \"model\": \"$MODEL\", \"signature\": \"$SIGNATURE\"}"
    ```

    ```javascript node.js expandable theme={null}
    const { randomUUID } = require("crypto");
    const OpenAI = require("openai");

    const apiKey = process.env.MOONSHOT_API_KEY;
    const client = new OpenAI({
        apiKey,
        baseURL: "https://api.moonshot.cn/v1",
    });

    async function main() {
        const nonce = randomUUID();
        const model = "kimi-k2.7-code";

        // 1. 携带 X-Msh-Request-Nonce 调用模型接口，并读取响应头
        const { response } = await client.chat.completions
            .create(
                { model, messages: [{ role: "user", content: "你好" }] },
                { headers: { "X-Msh-Request-Nonce": nonce } },
            )
            .withResponse();
        const timestamp = Number(response.headers.get("Msh-Request-Timestamp"));
        const signature = response.headers.get("Msh-Request-Signature");

        // 2. 校验签名
        const verify = await fetch("https://api.moonshot.cn/v1/signatures/verify", {
            method: "POST",
            headers: {
                Authorization: `Bearer ${apiKey}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ nonce, timestamp, model, signature }),
        });
        console.log(await verify.json()); // { valid: true }
    }

    main();
    ```
  </CodeGroup>
</Accordion>


## OpenAPI

````yaml POST /v1/signatures/verify
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
  /v1/signatures/verify:
    post:
      tags:
        - Utilities
      summary: 校验请求签名
      description: >-
        校验 Chat Completions、Responses 或 Messages API 响应头中返回的请求签名，用于证明该请求确实由 Kimi
        API 处理且请求的是指定模型，而非被转发到其他服务。提交调用时使用的 nonce、响应头中的 timestamp、请求的 model 以及
        signature，签名与这三个属性完全一致时返回 `valid: true`，否则返回 `valid: false`。
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SignatureVerifyRequest'
      responses:
        '200':
          description: 校验结果
          headers:
            Cache-Control:
              description: 固定为 `no-store`，校验结果不应被缓存。
              schema:
                type: string
                example: no-store
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SignatureVerifyResponse'
        '400':
          description: 请求错误 - 参数无效或缺少必填字段
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
        '429':
          description: 请求过于频繁
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
    SignatureVerifyRequest:
      type: object
      properties:
        nonce:
          type: string
          description: 调用模型接口时通过 `X-Msh-Request-Nonce` 请求头发送的 nonce，需与原值完全一致。
          minLength: 1
          example: 7d929748-0ae6-41c2-ab5d-a186498ad721
        timestamp:
          type: integer
          format: int64
          description: 模型接口响应头 `Msh-Request-Timestamp` 返回的 Unix 毫秒时间戳。
          minimum: 1
          example: 1786338000123
        model:
          type: string
          description: 调用模型接口时请求体中的 `model` 值，需与原值完全一致。
          minLength: 1
          example: kimi-k2.7-code
        signature:
          type: string
          description: 模型接口响应头 `Msh-Request-Signature` 返回的签名 token。
          minLength: 1
          example: reqsigv1_<opaque-token>
      required:
        - nonce
        - timestamp
        - model
        - signature
    SignatureVerifyResponse:
      type: object
      properties:
        valid:
          type: boolean
          description: >-
            签名是否有效。`true` 表示该签名由 Kimi API 签发，且与提交的 nonce、timestamp、model
            完全匹配；否则为 `false`。
          example: true
      required:
        - valid
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