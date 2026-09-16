> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用 Kimi API 的 JSON Mode

> 使用 `response_format` 启用 Kimi API JSON Mode，通过提示词和代码安全获取、解析结构化 JSON 输出。

JSON Mode 让 Kimi 大模型输出合法的、可被正确解析的 JSON 文档。当你需要结构化的输出时——例如总结一篇文章并得到这样的结构化数据——用 `response_format` 参数启用它：

```json theme={null}
{
	"title": "文章标题",
	"author": "文章作者",
	"publish_time": "发布时间",
	"summary": "文章总结"
}
```

## 用 response\_format 启用 JSON Mode

如果只在提示词 prompt 中告诉 Kimi 大模型："请输出 JSON 格式的内容"，Kimi 大模型能理解你的诉求，也会按要求生成 JSON 文档，但生成的内容通常会有一些瑕疵：例如在 JSON 文档之外，Kimi 还会额外输出其他文字内容对 JSON 文档进行解释——

```text theme={null}
以下是你需要的 JSON 文档

{
	"title": "文章标题",
	"author": "文章作者",
	"publish_time": "发布时间",
	"summary": "文章总结"
}
```

——或是输出格式有误、无法被正确解析的 JSON 文档（注意最后一行 `summary` 字段末尾的逗号）：

```text theme={null}
{
	"title": "文章标题",
	"author": "文章作者",
	"publish_time": "发布时间",
	"summary": "文章总结",
}
```

`response_format` 参数用于约束输出格式，默认值为 `{"type": "text"}`，即普通的、没有任何格式约束的文本内容。将 `response_format` 设置为 `{"type": "json_object"}` 即可启用 JSON Mode，Kimi 大模型会按照要求输出一个合法的、可被正确解析的 JSON 文档。

使用 JSON Mode 分三步：

1. 在 system 或 user prompt 中定义输出 JSON 的格式，包括具体的字段名称、字段类型等；**最佳实践是给出具体的输出示例，并解释每个字段的具体含义**；
2. 将 `response_format` 参数设置为 `{"type": "json_object"}`；
3. 解析 Kimi 大模型返回消息中的 `content`，`message.content` 是一个合法的、被序列化成字符串的 JSON Object。

## 完整示例：智能客服的多类型消息回复

设想一个微信智能机器人客服（简称智能客服）：它使用 Kimi 大模型来回答客户提出的问题，不仅能回复文字消息，还能回复图片、链接卡片、语音等类型的消息，并且可以在一次回复中混合多种类型的消息——例如对于客户的产品咨询类问题，既提供文字回复，也提供产品图片，最后附上购买链接（以链接卡片的形式）。

下面的代码演示了如何在这个场景中使用 JSON Mode 让模型按固定结构输出回复，并逐一解析各类消息内容：

<Note>
  本页示例默认使用最新模型 `kimi-k3`。K3 使用请求顶层 `reasoning_effort` 配置推理强度（支持 `"low"` / `"high"` / `"max"`，默认 `"max"`）。换用 `kimi-k2.6` 等其他模型时，只需替换 `model` 字段，但各模型的参数配置存在差异，详见[模型参数参考](/docs/api/models-overview)。
</Note>

<Tabs>
  <Tab title="python">
    ```python theme={null}
    import os
    import json

    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ["MOONSHOT_API_KEY"], # 运行前请设置 MOONSHOT_API_KEY 环境变量
        base_url="https://api.moonshot.cn/v1",
    )

    system_prompt = """
    你是月之暗面（Kimi）的智能客服，你负责回答用户提出的各种问题。请参考文档内容回复用户的问题，你的回答可以是文字、图片、链接，在一次回复中可以同时包含文字、图片、链接。

    请使用如下 JSON 格式输出你的回复：

    {
        "text": "文字信息",
        "image": "图片地址",
        "url": "链接地址"
    }

    注意，请将文字信息放置在 `text` 字段中，将图片以 `oss://` 开头的链接形式放在 `image` 字段中，将普通链接放置在 `url` 字段中。
    """

    completion = client.chat.completions.create(
        model="kimi-k3",
        messages=[
            {"role": "system",
             "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
            {"role": "system", "content": system_prompt}, # <-- 将附带输出格式的 system prompt 提交给 Kimi
            {"role": "user", "content": "你好，我叫李雷，1+1等于多少？"}
        ],
        response_format={"type": "json_object"}, # <-- 使用 response_format 参数指定输出格式为 json_object
    )

    # 由于我们设置了 JSON Mode，Kimi 大模型返回的 message.content 为序列化后的 JSON Object 字符串，
    # 我们使用 json.loads 解析其内容，将其反序列化为 python 中的字典 dict。
    content = json.loads(completion.choices[0].message.content)

    # 解析文本内容
    if "text" in content:
    	# 为了演示，我们将内容打印出来；
    	# 在真实的业务逻辑中，你可能需要调用发送文本消息的接口将生成的文本发送给用户。
        print("text:", content["text"])

    # 解析图片内容
    if "image" in content:
    	# 为了演示，我们将内容打印出来；
    	# 在真实的业务逻辑中，你可能需要先解析图片地址，下载图片后，调用发送图片消息
    	# 的接口将图片发送给用户。
        print("image:", content["image"])

    # 解析链接
    if "url" in content:
    	# 为了演示，我们将内容打印出来；
    	# 在真实的业务逻辑中，你可能需要调用发送链接卡片的接口，将链接以卡片的形式发送给用户。
        print("url:", content["url"])
    ```
  </Tab>

  <Tab title="node.js">
    ```js theme={null}
    const OpenAI = require("openai")

    const client = new OpenAI({
        apiKey: process.env.MOONSHOT_API_KEY, // 运行前请设置 MOONSHOT_API_KEY 环境变量
        baseURL: "https://api.moonshot.cn/v1",
    })

    system_prompt = `
    你是月之暗面（Kimi）的智能客服，你负责回答用户提出的各种问题。请参考文档内容回复用户的问题，你的回答可以是文字、图片、链接，在一次回复中可以同时包含文字、图片、链接。
    "
    "
    请使用如下 JSON 格式输出你的回复：

    {
        "text": "文字信息",
        "image": "图片地址",
        "url": "链接地址"
    }
    "
    注意，请将文字信息放置在 'text' 字段中，将图片以 oss:// 开头的链接形式放在 'image' 字段中，将普通链接放置在 'url' 字段中。
    `
    async function main() {
        const completion = await client.chat.completions.create({
            model: "kimi-k3",
            messages: [
                {role: "system",
                 content: "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
                {role: "system", content: system_prompt}, // <-- 将附带输出格式的 system prompt 提交给 Kimi
                {role: "user", content: "你好，我叫李雷，1+1等于多少？"}
            ],
            response_format: {type: "json_object"}, // <-- 使用 response_format 参数指定输出格式为 json_object
        })

        // 由于我们设置了 JSON Mode，Kimi 大模型返回的 message.content 为序列化后的 JSON Object 字符串，
        // 我们使用 JSON.parse 解析其内容，将其反序列化为 JavaScript 对象。
        content = JSON.parse(completion.choices[0].message.content)

        // 解析文本内容
        if (content.text) {
            console.log("text:", content.text)
        }
        // 解析图片内容
        if (content.image) {
            console.log("image:", content.image)
        }
        // 解析链接
        if (content.url) {
            console.log("url", content.url)
        }
    }

    main()
    ```
  </Tab>
</Tabs>

## 排查被截断的 JSON 输出

如果正确设置了 `response_format` 参数、也在提示词 prompt 中指定了 JSON 文档的格式，但获取的 JSON 文档不完整或被截断、导致无法正确解析，请检查返回值中的 `finish_reason` 字段是否为 `length`。

较小的 `max_tokens` 值会导致模型输出内容被截断，使用 JSON Mode 时同样适用这个规则。建议在预估输出的 JSON 文档大小后，设置一个合理的 `max_tokens` 值，以便能正确解析 Kimi 大模型返回的 JSON 文档。

关于 Kimi 大模型输出不完整或被截断问题的更详细说明，请参考[常见问题及解决方案](/docs/guide/troubleshooting)。

## 注意事项

* Kimi 大模型只会生成 JSON Object 类型的 JSON 文档，不要引导它生成 JSON Array 或其他类型的 JSON 文档；
* 如果没有正确告知 Kimi 大模型需要输出的 JSON Object 的格式，它会生成不符合预期的结果。
