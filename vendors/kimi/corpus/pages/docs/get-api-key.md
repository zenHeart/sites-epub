> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速开始

> 从创建 API Key 到完成第一次 Kimi API 调用。

Kimi API 提供了与 Kimi 大模型交互的能力，兼容 OpenAI 与 Anthropic API 格式。只需准备 API Key、选择模型，并配置 `base_url`，即可通过 HTTP API、OpenAI SDK 或 Anthropic SDK 发起调用。

<Info>
  [Kimi K3 模型](/docs/guide/kimi-k3-quickstart) 已正式发布。它是 Kimi 迄今能力最强的模型，支持 1M token 上下文与视觉理解，适合 [Claude Code](guide/claude-code-kimi) 等编程 Agent 场景，以及知识工作与深度推理场景。加入 [Kimi 开发者交流群](/docs/api/join-the-community) ，let's build on Kimi!
</Info>

## 开始使用

<Steps>
  <Step title="获取 API Key">
    访问 [Kimi API 开放平台](https://platform.kimi.com/) ，登录后进入 [API Keys](https://platform.kimi.com/console/api-keys) 页面创建并复制 API Key。

    请妥善保管你的 API Key，不要泄露给他人，也不要直接硬编码在代码中。建议使用环境变量保存：

    ```bash theme={null}
    export MOONSHOT_API_KEY="你的_KIMI_API_KEY"
    ```

    <CardGroup cols={2}>
      <Card title="Kimi API 开放平台" icon="link" href="https://platform.kimi.com/">
        登录开放平台，进入控制台、开发工作台和用户中心。
      </Card>

      <Card title="API Keys" icon="key" href="https://platform.kimi.com/console/api-keys">
        创建、复制和管理用于 API 调用的密钥。
      </Card>
    </CardGroup>
  </Step>

  <Step title="选择模型">
    作为快速开始入口，建议优先从 Kimi K3 开始；也可以根据场景选择 Kimi K2.7 Code 或 Kimi K2.6。

    <CardGroup cols={3}>
      <Card title="Kimi K3" icon="rocket" href="/docs/guide/kimi-k3-quickstart">
        Kimi K3 是面向长程编程与端到端知识工作的旗舰模型——2.8 万亿参数、1M token 上下文，综合智能达到领先水平。
      </Card>

      <Card title="Kimi K2.7 Code" icon="code" href="/docs/guide/kimi-k2-7-code-quickstart">
        面向代码场景的 Coding 模型，支持 256K 上下文窗口、文本/图片/视频输入和思考模式。如需更高输出速度，可选择 `kimi-k2.7-code-highspeed`。
      </Card>

      <Card title="Kimi K2.6" icon="brain" href="/docs/guide/kimi-k2-6-quickstart">
        综合能力强，支持 256K 上下文窗口、文本/图片/视频输入、思考与非思考模式，适合通用对话、Agent 任务、视觉理解和复杂推理。
      </Card>
    </CardGroup>

    <Tip>
      不确定如何选择时，默认从 `kimi-k3` 开始。如果你主要做代码生成、代码修改或编程 Agent 且追求更高输出速度，可以选择 `kimi-k2.7-code-highspeed`。
    </Tip>
  </Step>

  <Step title="选择调用方式">
    Kimi API 兼容 OpenAI 与 Anthropic API 格式，你可以根据项目技术栈选择最合适的接入方式。

    <CardGroup cols={2}>
      <Card title="Chat Completions API" icon="globe" href="/docs/api/chat">
        OpenAI 兼容格式，支持 OpenAI SDK 与任意语言 HTTP 接入。
      </Card>

      <Card title="Responses API" icon="bolt" href="/docs/api/responses">
        OpenAI 兼容格式，生成文本/JSON 输出或调用函数工具。
      </Card>

      <Card title="Messages API" icon="comment" href="/docs/api/messages">
        Anthropic 兼容格式，适合 Anthropic SDK、Claude Code 等工具接入。
      </Card>

      <Card title="开发工作台" icon="terminal" href="https://platform.kimi.com/playground">
        无需写代码，快速测试提示词、模型效果和业务样例。
      </Card>
    </CardGroup>
  </Step>

  <Step title="发起第一次调用">
    下面以 Kimi K3 模型为例。示例中的 `MOONSHOT_API_KEY` 需要替换为你在平台上创建的 API Key，或提前设置为同名环境变量。

    <Note>
      本页示例默认使用最新模型 `kimi-k3`。K3 使用请求顶层 `reasoning_effort` 配置推理强度（支持 `"low"` / `"high"` / `"max"`，默认 `"max"`）。换用 `kimi-k2.6` 等其他模型时，只需替换 `model` 字段，但各模型的参数配置存在差异，详见[模型参数参考](/docs/api/models-overview)。
    </Note>

    <Tip>
      如果你希望使用编程场景的高速模型，可将示例中的 `kimi-k3` 替换为 `kimi-k2.7-code-highspeed`；如果要调用 Kimi K2.6，则替换为 `kimi-k2.6`。
    </Tip>

    <Tabs>
      <Tab title="python">
        ```python theme={null}
        import os
        from openai import OpenAI

        client = OpenAI(
            api_key=os.environ["MOONSHOT_API_KEY"],
            base_url="https://api.moonshot.cn/v1",
        )

        completion = client.chat.completions.create(
            model="kimi-k3",
            messages=[
                {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
                {"role": "user", "content": "你好，我叫李雷，1+1等于多少？"}
            ]
        )

        print(completion.choices[0].message.content)
        ```
      </Tab>

      <Tab title="curl">
        ```bash theme={null}
        curl https://api.moonshot.cn/v1/chat/completions \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer $MOONSHOT_API_KEY" \
            -d '{
                "model": "kimi-k3",
                "messages": [
                    {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
                    {"role": "user", "content": "你好，我叫李雷，1+1等于多少？"}
                ]
           }'
        ```
      </Tab>

      <Tab title="node.js">
        ```js theme={null}
        const OpenAI = require("openai");

        const client = new OpenAI({
          apiKey: process.env.MOONSHOT_API_KEY,
          baseURL: "https://api.moonshot.cn/v1",
        });

        async function main() {
          const completion = await client.chat.completions.create({
            model: "kimi-k3",
            messages: [
              {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
              {"role": "user", "content": "你好，我叫李雷，1+1等于多少？"}
            ]
          });

          console.log(completion.choices[0].message.content);
        }

        main();
        ```
      </Tab>
    </Tabs>

    运行上述代码前，请准备：

    1. Python 3.8 及以上版本，或 Node.js 18 及以上版本。
    2. OpenAI SDK 1.0.0 及以上版本。Kimi API 兼容 OpenAI API 格式，你可以直接使用 Python 或 Node.js OpenAI SDK 进行调用。
       ```text theme={null}
       pip install --upgrade 'openai>=1.0' # Python
       npm install openai@latest # Node.js
       ```
    3. API Key。你需要从 Kimi 开放平台中 [创建一个 API Key](https://platform.kimi.com/console/api-keys) ，将其传入 `OpenAI Client` 以便平台正确识别你的身份。

    如果成功运行上述代码，且没有任何报错，你将看到类似如下的内容输出：

    ```text theme={null}
    你好，李雷！1+1 等于 2。这是一个基本的数学加法问题。如果你有其他问题或需要帮助，请随时告诉我。
    ```

    *注：由于 Kimi 大模型的不确定性，实际的回复内容可能并不与上述内容完全一致。*
  </Step>
</Steps>

## 探索更多功能

<CardGroup cols={3}>
  <Card title="流式输出" icon="bolt" href="/docs/api/chat">
    启用 `stream`，让回复边生成边返回，适合聊天、代码生成和长文本输出场景。
  </Card>

  <Card title="多轮对话" icon="comments" href="/docs/guide/engage-in-multi-turn-conversations-using-kimi-api">
    通过维护 `messages` 列表实现上下文记忆，让模型记住对话历史。
  </Card>

  <Card title="多模态输入" icon="image" href="/docs/guide/use-kimi-vision-model">
    Kimi K3、Kimi K2.7 Code 和 Kimi K2.6 均支持文本、图片与视频输入。
  </Card>

  <Card title="工具调用" icon="wrench" href="/docs/guide/use-kimi-api-to-complete-tool-calls">
    让模型调用外部函数或 API，实现 Agent 任务、联网搜索和复杂工作流。
  </Card>

  <Card title="JSON Mode" icon="code" href="/docs/guide/use-json-mode-feature-of-kimi-api">
    强制模型输出合法 JSON，方便结构化数据提取和下游系统对接。
  </Card>

  <Card title="思考模型" icon="brain" href="/docs/guide/use-thinking-models">
    使用思考能力处理复杂推理、多步工具调用和 Agent 任务。
  </Card>
</CardGroup>

### 流式输出

```json theme={null}
{
  "model": "kimi-k3",
  "messages": [
    {
      "role": "user",
      "content": "请解释什么是递归，并给出一个 Python 示例。"
    }
  ],
  "stream": true
}
```

### 多模态输入

```json theme={null}
{
  "model": "kimi-k3",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": "data:image/png;base64,..."
          }
        },
        {
          "type": "text",
          "text": "请描述这张图片。"
        }
      ]
    }
  ]
}
```

<Warning>
  对于较大的视频或需要多次引用的图片、视频，建议使用文件上传方式。图片建议不超过 4K 分辨率，视频建议不超过 1080p。
</Warning>

## 相关资源

<CardGroup cols={2}>
  <Card title="Kimi K3 模型" icon="rocket" href="/docs/guide/kimi-k3-quickstart">
    查看 Kimi K3 的模型能力、调用示例和最佳实践。
  </Card>

  <Card title="Kimi K2.7 Code 模型" icon="code" href="/docs/guide/kimi-k2-7-code-quickstart">
    查看 Kimi K2.7 Code 的模型能力、调用示例和最佳实践。
  </Card>

  <Card title="Kimi K2.6 模型" icon="brain" href="/docs/guide/kimi-k2-6-quickstart">
    查看 Kimi K2.6 的模型能力、图片/视频理解示例和工具调用说明。
  </Card>

  <Card title="加入 Kimi 开发者反馈群" icon="comments" href="/docs/api/join-the-community">
    提供建议、问题反馈、分享案例: Let's Build with Kimi !
  </Card>

  <Card title="模型列表" icon="list" href="/docs/models">
    查看当前可用模型名称和模型说明。
  </Card>
</CardGroup>
