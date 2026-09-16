> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Token Count

计算 token 数，支持 Chat Completion 接口与 Messages 接口两种格式。

## 计算 Chat Completion Token 数

### 请求地址

`POST https://api.stepfun.com/v1/token/count`

### 请求参数

* `model` `string` ***required***<br />需要使用的模型名称
* `messages` `object array` ***required***<br />迄今为止用户输入或模型生成的不同类别消息列表

  <Expandable>
    * 系统消息 `object`
        <Expandable>
          * `role` `string`<br />系统类别名称，总是为 `system`
          * `content` `string`<br />系统消息的文本内容
        </Expandable>
    * 用户消息 `object`
        <Expandable>
          * `role` `string`<br />用户类别名称，总是 `user`
          * `content` `string or object array`<br />用户消息内容，类型为 `multipart` 消息列表或者普通文本消息字符串
                <Expandable>
                  * `普通文本消息` `string`<br />直接传入字符串作为消息内容
                  * `multipart` 消息列表 `object array`<br />结构化的图文混合消息
                          <Expandable>
                            * 文本消息 `object`
                                      <Expandable>
                                        * `type` `string`<br />总为 `text`
                                        * `text` `string`<br />消息文本内容
                                      </Expandable>
                            * 图片消息 `object`
                                      <Expandable>
                                        * `type` `string`<br />总为 `image_url`
                                        * `image_url` `object`
                                                    <Expandable>
                                                      * `url` `string`<br />图片地址或 base64编码的图片
                                                        <p>图片地址仅支持 http 和 https 协议</p>
                                                        <p>base64格式举例：`data:image/jpeg;base64,${base64_string}`，请更换图片格式(jpeg)及对应的 base64编码后字符串</p>
                                                        <p>本接口支持的图片格式：jpg/jpeg、png、webp、静态 gif</p>
                                                    </Expandable>
                                      </Expandable>
                          </Expandable>
                </Expandable>
        </Expandable>
    * 聊天助手消息 `object`
        <Expandable>
          * `role` `string`<br />聊天助手类别名称，总是为 `assistant`
          * `content` `string | null`<br />聊天助手消息的文本内容
        </Expandable>
  </Expandable>

### 请求响应

* `data` `object`<br />计算 token 返回数据
  <Expandable>
    * `total_tokens` `int`<br />输入 token 数
  </Expandable>

### 示例

<Tabs>
  <Tab title="文字聊天">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/token/count \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "model": "step-3.7-flash",
        "messages": [
          {
            "role": "system",
            "content": "你是由阶跃星辰提供的AI聊天助手，你擅长中文，英文，以及多种其他语言的对话。在保证用户数据安全的前提下，你能对用户的问题和请求，作出快速和精准的回答。同时，你的回答和建议应该拒绝黄赌毒，暴力恐怖主义的内容。"
          },
          {
            "role": "user",
            "content": "你好，请介绍一下阶跃星辰的人工智能！"
          }
        ]
      }'
    ```

    ```json filename="返回" theme={null}
    {
      "data": {
        "total_tokens": 85
      }
    }
    ```
  </Tab>

  <Tab title="图文混合">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/token/count \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "model": "step-3.7-flash",
        "messages": [
          {
            "role": "system",
            "content": "你是由阶跃星辰提供的AI聊天助手，你除了擅长中文，英文，以及多种其他语言的对话以外，还能够根据用户提供的图片，对内容进行精准的内容文本描述。在保证用户数据安全的前提下，你能对用户的问题和请求，作出快速和精准的回答。同时，你的回答和建议应该拒绝黄赌毒，暴力恐怖主义的内容"
          },
          {
            "role": "user",
            "content": [
              {
                "type": "text",
                "text": "用优雅的语言描述这张图片"
              },
              {
                "type": "image_url",
                "image_url": {
                  "url": "https://www.stepfun.com/assets/section-1-CTe4nZiO.webp"
                }
              }
            ]
          }
        ]
      }'
    ```

    ```json filename="返回" theme={null}
    {
      "data": {
        "total_tokens": 497
      }
    }
    ```
  </Tab>

  <Tab title="Base64编码图片">
    ```bash theme={null}
    # 加载图片到内存，仅演示。按需改成读文件等
    image_base64="data:image/webp;base64,"$(curl -s "https://www.stepfun.com/assets/section-1-CTe4nZiO.webp" | base64)

    curl https://api.stepfun.com/v1/token/count \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d "{
        \"model\": \"step-3.7-flash\",
        \"messages\": [
          {
            \"role\": \"system\",
            \"content\": \"你是由阶跃星辰提供的AI聊天助手，你除了擅长中文，英文，以及多种其他语言的对话以外，还能够根据用户提供的图片，对内容进行精准的内容文本描述。在保证用户数据安全的前提下，你能对用户的问题和请求，作出快速和精准的回答。同时，你的回答和建议应该拒绝黄赌毒，暴力恐怖主义的内容\"
          },
          {
            \"role\": \"user\",
            \"content\": [
              {
                \"type\": \"text\",
                \"text\": \"用优雅的语言描述这张图片\"
              },
              {
                \"type\": \"image_url\",
                \"image_url\": {
                  \"url\": \"${image_base64}\"
                }
              }
            ]
          }
        ]
      }"
    ```

    ```json filename="返回" theme={null}
    {
      "data": {
        "total_tokens": 497
      }
    }
    ```
  </Tab>
</Tabs>

***

## 估算 Message Token 数

估算 Messages API 输入 token 数量，不生成模型回复。

### 请求地址

`POST https://api.stepfun.com/v1/messages/count_tokens`

<Note>
  使用 Anthropic SDK 时，base\_url 应设为 `https://api.stepfun.com`，SDK 会自动拼接 `/v1/messages/count_tokens`，无需手动带 `/v1`。
</Note>

<Note>
  Step Plan 场景请求地址为 `POST https://api.stepfun.com/step_plan/v1/messages/count_tokens`，对应 SDK base\_url 为 `https://api.stepfun.com/step_plan`。
</Note>

### 请求参数

请求体结构与[创建 Message](/docs/zh/api-reference/chat/messages-create) 相同，通常至少需要提供：

* `model` `string` ***required***<br />模型名称
* `messages` `object array` ***required***<br />对话消息列表

也可按需携带 `system`、`tools` 等上下文字段。`max_tokens` 在该接口中可不传。

### 请求响应

`Content-Type: application/json`

```json theme={null}
{
  "input_tokens": 12
}
```

* `input_tokens` `int`<br />估算的输入 token 数量

### 示例

<Tabs>
  <Tab title="python">
    ```python theme={null}
    from anthropic import Anthropic

    client = Anthropic(api_key="YOUR_STEP_API_KEY", base_url="https://api.stepfun.com")

    response = client.messages.count_tokens(
        model="step-3.5-flash",
        messages=[
            {
                "role": "user",
                "content": "统计这句话需要多少输入 token？"
            }
        ],
    )

    print(response.input_tokens)
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/messages/count_tokens \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "model": "step-3.5-flash",
        "messages": [
          {
            "role": "user",
            "content": "统计这句话需要多少输入 token？"
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "input_tokens": 12
}
```
