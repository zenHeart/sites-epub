> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 配置多轮对话参数

> 在无状态的 Kimi API 中维护消息历史、控制上下文长度，并正确构建多轮对话请求。

与 Kimi 智能助手不同，Kimi API 是 **无状态** 的，本身没有记忆功能：多次请求之间，模型不知道你前一次请求的内容，也不会记住任何上下文——上一次你告诉它今年 27 岁，下一次请求它并不知情。要实现多轮对话，需要手动维护每次请求的上下文（Context），把历史消息随下一次请求一起发送，让模型能看到此前聊过的内容。

<Note>
  本页示例默认使用最新模型 `kimi-k3`。K3 使用请求顶层 `reasoning_effort` 配置推理强度（支持 `"low"` / `"high"` / `"max"`，默认 `"max"`）。换用 `kimi-k2.6` 等其他模型时，只需替换 `model` 字段，但各模型的参数配置存在差异，详见[模型参数参考](/docs/api/models-overview)。
</Note>

## 用 messages 列表为模型补上记忆

以下示例改造自上一章节，演示如何通过维护 `messages` 列表让模型拥有记忆：每轮对话把用户的新消息（role=user）和模型的回复（role=assistant）都追加到列表中，再整体随请求发送。实现要点已以注释形式标注在代码中：

<Tabs>
  <Tab title="python">
    ```python theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key = os.environ["MOONSHOT_API_KEY"], # 运行前请设置 MOONSHOT_API_KEY 环境变量
        base_url = "https://api.moonshot.cn/v1",
    )

    # 我们定义一个全局变量 messages，用于记录我们和 Kimi 大模型产生的历史对话消息
    # 在 messages 中，既包含我们向 Kimi 大模型提出的问题（role=user），也包括 Kimi 大模型给我们的回复（role=assistant）
    # 当然，也包括初始的 System Prompt（role=system）
    # messages 中的消息按时间顺序从小到大排列
    messages = [
        {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
    ]

    def chat(input: str) -> str:
        """
        chat 函数支持多轮对话，每次调用 chat 函数与 Kimi 大模型对话时，Kimi 大模型都会"看到"此前已经
        产生的历史对话消息，换句话说，Kimi 大模型拥有了记忆。
        """

        global messages

        # 我们将用户最新的问题构造成一个 message（role=user），并添加到 messages 的尾部
        messages.append({
            "role": "user",
            "content": input,
        })

        # 携带 messages 与 Kimi 大模型对话
        completion = client.chat.completions.create(
            model="kimi-k3",
            messages=messages
        )

        # 通过 API 我们获得了 Kimi 大模型给予我们的回复消息（role=assistant）
        assistant_message = completion.choices[0].message

        # 为了让 Kimi 大模型拥有完整的记忆，我们必须将 Kimi 大模型返回给我们的消息也添加到 messages 中
        messages.append(assistant_message)

        return assistant_message.content

    print(chat("你好，我今年 27 岁。"))
    print(chat("你知道我今年几岁吗？")) # 在这里，Kimi 大模型根据此前的上下文信息，将会知道你今年的年龄是 27 岁
    ```
  </Tab>

  <Tab title="node.js">
    ```js theme={null}
    const OpenAI = require("openai")

    const client = new OpenAI({
      apiKey: process.env.MOONSHOT_API_KEY, // 运行前请设置 MOONSHOT_API_KEY 环境变量
      baseURL: "https://api.moonshot.cn/v1",
    });

    // 我们定义一个全局变量 messages，用于记录我们和 Kimi 大模型产生的历史对话消息
    // 在 messages 中，既包含我们向 Kimi 大模型提出的问题（role=user），也包括 Kimi 大模型给我们的回复（role=assistant）
    // 当然，也包括初始的 System Prompt（role=system）
    // messages 中的消息按时间顺序从小到大排列
    let messages = [
      {
        role: "system",
        content: "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。",
      },
    ];

    async function chat(input) {
      /**
       * chat 函数支持多轮对话，每次调用 chat 函数与 Kimi 大模型对话时，Kimi 大模型都会"看到"此前已经
       * 产生的历史对话消息，换句话说，Kimi 大模型拥有了记忆。
       */

      // 我们将用户最新的问题构造成一个 message（role=user），并添加到 messages 的尾部
      messages.push({
        role: "user",
        content: input,
      });

      // 携带 messages 与 Kimi 大模型对话
      const completion = await client.chat.completions.create({
        model: "kimi-k3",
        messages: messages
      });

      // 通过 API 我们获得了 Kimi 大模型给予我们的回复消息（role=assistant）
      const assistantMessage = completion.choices[0].message;

      // 为了让 Kimi 大模型拥有完整的记忆，我们必须将 Kimi 大模型返回给我们的消息也添加到 messages 中
      messages.push(assistantMessage);

      return assistantMessage.content;
    }

    // 使用示例
    (async () => {
      console.log(await chat("你好，我今年 27 岁。"));
      console.log(await chat("你知道我今年几岁吗？")); // 在这里，Kimi 大模型根据此前的上下文信息，将会知道你今年的年龄是 27 岁
    })();
    ```
  </Tab>
</Tabs>

要点回顾：

* Kimi API 本身没有上下文记忆功能，需要通过 `messages` 参数手动把"之前聊了什么"告知模型；
* `messages` 中既要存用户提出的问题（role=user），也要存模型的回复（role=assistant）。

## 截断历史消息，控制上下文长度

随着 `chat` 调用次数增多，`messages` 列表不断增长，每次请求消耗的 Tokens 也随之增加，最终列表中的消息会超出模型支持的上下文窗口。建议用某种策略把 `messages` 控制在可控范围内，例如每次只保留最新的 20 条消息作为本次请求的上下文。

以下示例演示如何用 `make_messages` 函数控制每次请求的消息数量（默认保留最新 20 条），注意它如何保证截断后 System Messages 仍然留在列表中：

<Tabs>
  <Tab title="python">
    ```python theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key = os.environ["MOONSHOT_API_KEY"], # 运行前请设置 MOONSHOT_API_KEY 环境变量
        base_url = "https://api.moonshot.cn/v1",
    )

    # 我们将 System Messages 单独放置在一个列表中，这是因为每次请求都应该携带 System Messages
    system_messages = [
    	{"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
    ]

    # 我们定义一个全局变量 messages，用于记录我们和 Kimi 大模型产生的历史对话消息
    # 在 messages 中，既包含我们向 Kimi 大模型提出的问题（role=user），也包括 Kimi 大模型给我们的回复（role=assistant）
    # messages 中的消息按时间顺序从小到大排列
    messages = []


    def make_messages(input: str, n: int = 20) -> list[dict]:
    	"""
    	使用 make_messaegs 控制每次请求的消息数量，使其保持在一个合理的范围内，例如默认值是 20。在构建消息列表
    	的过程中，我们会先添加 System Prompt，这是因为无论如何对消息进行截断，System Prompt 都是必不可少
    	的内容，再获取 messages —— 即历史记录中，最新的 n 条消息作为请求使用的消息，在大部分场景中，这样
    	能保证请求的消息所占用的 Tokens 数量不超过模型上下文窗口。
    	"""
    	global messages

    	# 首先，我们将用户最新的问题构造成一个 message（role=user），并添加到 messages 的尾部
    	messages.append({
    		"role": "user",
    		"content": input,
    	})

    	# new_messages 是我们下一次请求使用的消息列表，现在让我们来构建它
    	new_messages = []

    	# 每次请求都需要携带 System Messages，因此我们需要先把 system_messages 添加到消息列表中；
    	# 注意，即使对消息进行截断，也应该注意保证 System Messages 仍然在 messages 列表中。
    	new_messages.extend(system_messages)

    	# 在这里，当历史消息超过 n 条时，我们仅保留最新的 n 条消息
    	if len(messages) > n:
    		messages = messages[-n:]

    	new_messages.extend(messages)
    	return new_messages


    def chat(input: str) -> str:
    	"""
    	chat 函数支持多轮对话，每次调用 chat 函数与 Kimi 大模型对话时，Kimi 大模型都会"看到"此前已经
    	产生的历史对话消息，换句话说，Kimi 大模型拥有了记忆。
    	"""

    	# 携带 messages 与 Kimi 大模型对话
    	completion = client.chat.completions.create(
            model="kimi-k3",
            messages=make_messages(input)
        )

    	# 通过 API 我们获得了 Kimi 大模型给予我们的回复消息（role=assistant）
    	assistant_message = completion.choices[0].message

    	# 为了让 Kimi 大模型拥有完整的记忆，我们必须将 Kimi 大模型返回给我们的消息也添加到 messages 中
    	messages.append(assistant_message)

    	return assistant_message.content

    print(chat("你好，我今年 27 岁。"))
    print(chat("你知道我今年几岁吗？")) # 在这里，Kimi 大模型根据此前的上下文信息，将会知道你今年的年龄是 27 岁
    ```
  </Tab>

  <Tab title="node.js">
    ```js theme={null}
    const OpenAI = require("openai")

    const client = new OpenAI({
      apiKey: process.env.MOONSHOT_API_KEY, // 运行前请设置 MOONSHOT_API_KEY 环境变量
      baseURL: "https://api.moonshot.cn/v1",
    });

    // 我们将 System Messages 单独放置在一个列表中，这是因为每次请求都应该携带 System Messages
    const systemMessages = [
      {
        role: "system",
        content: "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。",
      },
    ];

    // 我们定义一个全局变量 messages，用于记录我们和 Kimi 大模型产生的历史对话消息
    // 在 messages 中，既包含我们向 Kimi 大模型提出的问题（role=user），也包括 Kimi 大模型给我们的回复（role=assistant）
    // messages 中的消息按时间顺序从小到大排列
    let messages = [];

    async function makeMessages(input, n = 20) {
      /**
       * 使用 make_messages 控制每次请求的消息数量，使其保持在一个合理的范围内，例如默认值是 20。在构建消息列表
       * 的过程中，我们会先添加 System Prompt，这是因为无论如何对消息进行截断，System Prompt 都是必不可少的
       * 内容，再获取 messages —— 即历史记录中，最新的 n 条消息作为请求使用的消息，在大部分场景中，这样
       * 能保证请求的消息所占用的 Tokens 数量不超过模型上下文窗口。
       */
      // 首先，我们将用户最新的问题构造成一个 message（role=user），并添加到 messages 的尾部
      messages.push({
        role: "user",
        content: input,
      });

      // newMessages 是我们下一次请求使用的消息列表，现在让我们来构建它
      let newMessages = [];

      // 每次请求都需要携带 System Messages，因此我们需要先把 systemMessages 添加到消息列表中；
      // 注意，即使对消息进行截断，也应该注意保证 System Messages 仍然在 messages 列表中。
      newMessages = systemMessages.concat(newMessages);

      // 在这里，当历史消息超过 n 条时，我们仅保留最新的 n 条消息
      if (messages.length > n) {
        messages = messages.slice(-n);
      }

      newMessages = newMessages.concat(messages);
      return newMessages;
    }

    async function chat(input) {
      /**
       * chat 函数支持多轮对话，每次调用 chat 函数与 Kimi 大模型对话时，Kimi 大模型都会"看到"此前已经
       * 产生的历史对话消息，换句话说，Kimi 大模型拥有了记忆。
       */

      // 携带 messages 与 Kimi 大模型对话
      const completion = await client.chat.completions.create({
        model: "kimi-k3",
        messages: await makeMessages(input)
      });

      // 通过 API 我们获得了 Kimi 大模型给予我们的回复消息（role=assistant）
      const assistantMessage = completion.choices[0].message;

      // 为了让 Kimi 大模型拥有完整的记忆，我们必须将 Kimi 大模型返回给我们的消息也添加到 messages 中
      messages.push(assistantMessage);

      return assistantMessage.content;
    }

    (async () => {
      console.log(await chat("你好，我今年 27 岁。"));
      console.log(await chat("你知道我今年几岁吗？")); // 在这里，Kimi 大模型根据此前的上下文信息，将会知道你今年的年龄是 27 岁
    })();
    ```
  </Tab>
</Tabs>

## 生产环境还需要考虑什么

上述代码示例仅覆盖最简单的调用场景，实际业务中可能还需要处理更多场景和边界：

* 并发场景下可能需要额外的读写锁；
* 多用户场景需要为每个用户单独维护 `messages` 列表；
* 对 `messages` 列表进行持久化；
* 用更精确的方式计算 `messages` 列表中需要保留多少条消息；
* 对被遗弃的消息做一次总结，生成一条新消息加入 `messages` 列表；
* ……
