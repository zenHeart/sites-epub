> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Step Router V1 智能路由开发指南

`step-router-v1` 是阶跃星辰为 [Step Plan](/docs/zh/step-plan/overview) 通道提供的智能路由模型。开发者只需在 `model` 字段填入 `step-router-v1`，系统会根据请求特征自动路由到 `deepseek-v4-pro` 或 `step-3.7-flash` 中更合适的一个：复杂推理交由 `deepseek-v4-pro` 处理，高频执行交由 `step-3.7-flash` 承载。

<Note>
  仅 [Step Plan](/docs/zh/step-plan/overview) 通道（`https://api.stepfun.com/step_plan/v1`）可用。本模型不支持图像识别。
</Note>

## 适用场景

`step-router-v1` 适合以下需要在成本与智能之间自动权衡的场景：

* **复杂度差异大的混合工作流**：同一个 Agent 既要处理格式整理、信息抽取等高频小任务，又要处理架构规划、错误诊断等关键决策，由路由自动分流可省去自行实现分流逻辑的成本。
* **Agent 长链路任务**：多轮对话、含工具调用的请求，系统会在判定为复杂场景时调度 `deepseek-v4-pro` 以保障输出质量。
* **成本敏感但需要高质量决策的场景**：默认由 `step-3.7-flash` 承载多数请求以控制成本，复杂请求自动升级至 `deepseek-v4-pro` 以保留智能产出。

## 调用方式

调用方式与直接调用底层模型完全一致，仅需将 `model` 设为 `step-router-v1`，并将 base\_url 指向 Step Plan 通道。

### 非流式

<Tabs>
  <Tab title="Python (OpenAI SDK)">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_STEP_API_KEY",
        base_url="https://api.stepfun.com/step_plan/v1",
    )

    response = client.chat.completions.create(
        model="step-router-v1",
        messages=[
            {"role": "user", "content": "请帮我把这段需求拆解成开发任务列表"}
        ],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="Python (Anthropic SDK)">
    ```python theme={null}
    from anthropic import Anthropic

    # 注意：Anthropic SDK 会自动拼接 /v1/messages，base_url 不带 /v1
    client = Anthropic(
        api_key="YOUR_STEP_API_KEY",
        base_url="https://api.stepfun.com/step_plan",
    )

    message = client.messages.create(
        model="step-router-v1",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "请帮我把这段需求拆解成开发任务列表"}
        ],
    )

    print(message.content[0].text)
    ```
  </Tab>
</Tabs>

### 流式

```python theme={null}
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_STEP_API_KEY",
    base_url="https://api.stepfun.com/step_plan/v1",
)

stream = client.chat.completions.create(
    model="step-router-v1",
    messages=[{"role": "user", "content": "你好"}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## 字段差异

`step-router-v1` 的请求与响应字段约束整体与直接调用底层模型一致。命中 `deepseek-v4-pro` 时的字段差异（`max_tokens` 上限、不支持的内容类型等），详见 [Chat Completion API](/docs/zh/api-reference/chat/chat-completion-create) 与 [Messages API](/docs/zh/api-reference/chat/messages-create) 中 **Step Plan 通道：DeepSeek 引擎字段差异** 一节。

## 计费机制

按实际命中的引擎计费：命中 `deepseek-v4-pro` 按 `deepseek-v4-pro` 单价收费，命中 `step-3.7-flash` 按 `step-3.7-flash` 单价收费。计费金额最终折算为 Step Plan 总额度消耗，详见 [Step Plan 概览](/docs/zh/step-plan/overview)。

## 相关链接

<Columns cols={2}>
  <Card title="产品介绍" href="/docs/zh/guides/models/step-router">
    `step-router-v1` 的产品定位、底层引擎组成与定价。
  </Card>

  <Card title="接入文档" href="/docs/zh/step-plan/integrations/reasoning-api">
    Step Plan 推理模型接入：base\_url、SDK、字段差异。
  </Card>
</Columns>
