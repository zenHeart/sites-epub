> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Step Router V1 智能路由

`step-router-v1` 是阶跃星辰为 [Step Plan](/docs/zh/step-plan/overview) 通道提供的智能路由模型。只需在 `model` 字段填入 `step-router-v1`，系统会根据每次请求的特征在 `deepseek-v4-pro` 与 `step-3.7-flash` 之间自动调度：复杂推理与长链路决策交由 `deepseek-v4-pro` 处理，高频与结构化执行交由 `step-3.7-flash` 承载，从而在控制整体成本的同时维持复杂任务的输出质量，开发者无需自行实现分流逻辑。

<Note>
  本模型仅在 [Step Plan](/docs/zh/step-plan/overview) 通道（`https://api.stepfun.com/step_plan/v1`）可用。
</Note>

## 关键信息

<Columns cols={3}>
  <Card title="模型类型">
    双引擎智能路由：deepseek-v4-pro + step-3.7-flash
  </Card>

  <Card title="调度依据">
    按请求特征自动路由，参考消息轮数、输入量、工具数量
  </Card>

  <Card title="可用通道">
    仅 Step Plan 通道；支持 OpenAI 与 Anthropic 协议
  </Card>
</Columns>

## 底层引擎

`step-router-v1` 由以下两个引擎组成，系统按请求特征自动路由到其中之一：

<Columns cols={2}>
  <Card title="deepseek-v4-pro" icon="brain">
    **决策引擎**：1M 上下文、250K 最大输出，面向复杂推理与长链路 Agent 决策，支持 `thinking`、`tools` / `tool_choice` 等字段透传。请求被判定为复杂或高不确定性时路由到此引擎。
  </Card>

  <Card title="step-3.7-flash" icon="bolt">
    **执行引擎**：阶跃星辰旗舰多模态推理模型，198B 总参数 / 11B 激活参数的稀疏 MoE 架构，256K 上下文，原生支持图片与视频理解，支持三档推理强度。承载多数高频与结构化任务，是 `step-router-v1` 的默认执行模型。
  </Card>
</Columns>

## 路由说明

系统根据请求特征（消息轮数、输入 token 量、工具数量等）自动判定复杂度并选择引擎，无需在请求中额外指定。调用方式、字段约束与直接调用底层模型一致，仅 `model` 字段填 `step-router-v1`。

<Info>
  `step-router-v1` 在 Step Plan 通道下的字段差异（`max_tokens` 上限、不支持的内容类型等）详见 [Chat Completion API](/docs/zh/api-reference/chat/chat-completion-create) 与 [Messages API](/docs/zh/api-reference/chat/messages-create) 中 **Step Plan 通道：DeepSeek 引擎字段差异** 一节。
</Info>

## 定价

按实际命中的底层引擎计费：命中 `deepseek-v4-pro` 按 `deepseek-v4-pro` 计费，命中 `step-3.7-flash` 按 `step-3.7-flash` 计费。计费金额最终折算为 [Step Plan](/docs/zh/step-plan/overview) 总额度消耗。

## 开始使用

<Columns cols={3}>
  <Card title="开发指南" icon="rocket" href="/docs/zh/guides/developer/step-router">
    适用场景、流式与非流式调用示例、最佳实践。
  </Card>

  <Card title="Step Plan 推理模型接入" icon="code" href="/docs/zh/step-plan/integrations/reasoning-api">
    base\_url、SDK 示例与 Step Router 切换方式。
  </Card>

  <Card title="Chat Completion API" icon="code" href="/docs/zh/api-reference/chat/chat-completion-create">
    OpenAI 协议端点参数与响应说明。
  </Card>
</Columns>
