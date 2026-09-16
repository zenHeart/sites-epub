> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 迁移到托管智能体

> 从基于模型推理 API 自建的智能体循环，迁移到托管智能体。

如果你已经基于模型推理 API 自建了智能体循环——自己维护消息历史、自己执行工具、自己处理失败重试——本指南说明如何把这套系统迁移到托管智能体，把运行时交给平台，只保留真正属于你的部分。

<Note>
  迁移不要求任何 SDK 兼容层：托管智能体就是一组 HTTP + SSE 接口，用 `curl` 或任意 HTTP 客户端即可调用。以下示例的 API Key 从环境变量 `KIMI_API_KEY` 读取；未设置 `API_BASE_URL` 时，请求地址默认使用 `https://api.moonshot.cn`。
</Note>

## 什么变了

自建 Harness 时，运行时的一切都由你的代码负责。迁移后，这些职责交给平台托管：

| 能力   | 自建 Harness       | 托管智能体                               |
| ---- | ---------------- | ----------------------------------- |
| 会话历史 | 自己拼接、存储并回传消息列表   | 平台以事件形式持久化完整历史，可随时拉取                |
| 工具执行 | 自己解析工具调用、执行并回填结果 | 内置工具由平台在云沙箱中执行；自定义工具（暂未开放）仍由你的客户端执行 |
| 沙箱   | 自己准备运行命令、读写文件的环境 | 平台提供隔离的云沙箱，可按需配置网络与依赖               |
| 失败恢复 | 自己处理崩溃、断线后的状态重建  | 平台故障后自动接管并恢复执行，行为与中断前一致             |
| 超时重试 | 自己实现重试与限流退避      | 平台承担执行层的重试与调度                       |

迁移的本质是：**把「怎么运行」交给平台，把「是什么任务」留在你的配置和代码里**。

## 迁移步骤

<Steps>
  <Step title="把系统提示词、工具定义、技能搬进 Agent 配置">
    把原来代码里的系统提示词、工具 schema 等「怎么干」的内容，收敛为一个持久化的 Agent 配置对象。智能体创建一次即可跨会话按 ID 引用，每次更新生成不可变的新版本。

    ```bash theme={null}
    curl -X POST ${API_BASE_URL:-https://api.moonshot.cn}/v1/agents \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "调研助手",
        "model": {"id": "kimi-k3"},
        "system": "你是一个严谨的调研助手，擅长检索、整理并引用资料。"
      }'
    ```

    原来「循环内硬编码」的内容对应关系：

    * 系统提示词 → 智能体的 `system` 字段；
    * 原来在客户端执行的业务工具 → 先通过 [MCP](/docs/hosted-agents/mcp) 工具接入，或暂时保留在自建流程中；
    * 原来手写的工具函数（搜索、读写文件、跑命令）→ 智能体默认获得云沙箱的内置工具（文件读写、代码执行、搜索等），无需声明，删掉你的实现；
    * 成体系的领域经验（提示词 + 脚本 + 模板）→ 打包为 [技能](/docs/hosted-agents/skills) 挂载。

    智能体字段与版本机制详见 [创建与管理智能体](/docs/hosted-agents/agents)。
  </Step>

  <Step title="删除自建的智能体循环与消息历史存储">
    这是迁移中「删代码」的一步。以下组件可以整体移除：

    * 「调模型 → 解析工具调用 → 执行 → 回填结果 → 再调模型」的主循环；
    * 消息历史的拼接、截断与持久化存储；
    * 崩溃恢复、断线续跑、超时重试的兜底逻辑。

    上下文压缩、历史管理、中断恢复都由平台承担，你不再需要在每次请求时回传完整消息列表。
  </Step>

  <Step title="改为创建会话、订阅事件流、发送事件">
    原来「调用一次模型推理 API」的交互，换成「创建会话 → 订阅事件流 → 发送事件」三步。`AGENT_ID` 为 Step 1 创建响应中的 `id`，`SESSION_ID` 为创建会话响应中的 `id`，`ENVIRONMENT_ID` 为执行环境的 ID：

    ```bash theme={null}
    # 1. 创建会话（创建不等于启动）
    curl -X POST ${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta" \
      -H "Content-Type: application/json" \
      -d "{\"agent_id\": \"$AGENT_ID\", \"environment_id\": \"$ENVIRONMENT_ID\", \"title\": \"我的第一个任务\"}"

    # 2. 先订阅事件流（在另一个终端中执行）
    curl -N ${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/events/stream \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta" \
      -H "Accept: text/event-stream"

    # 3. 发送用户消息，智能体开始工作
    curl -X POST ${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/events \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta" \
      -H "Content-Type: application/json" \
      -d '{"events": [{"type": "user.message", "data": {"content": [{"type": "text", "text": "帮我调研一下行业近况"}]}}]}'
    ```

    <Tip>
      建议先订阅事件流再发送消息，避免漏掉二者之间产生的事件。事件流支持断线续读：重连时携带 `Last-Event-ID` 请求头即可从断点继续，详见 [事件流](/docs/hosted-agents/event-stream)。
    </Tip>

    会话的创建、状态与生命周期详见 [会话](/docs/hosted-agents/sessions)。
  </Step>
</Steps>

## 不用迁移什么

以下能力由平台承担，迁移时不需要在你的系统中重建：

* **会话历史持久化**：事件历史在服务端持久化，可随时完整拉取，无需自建消息存储；
* **断线恢复**：事件流断线后按游标续读；平台故障后执行自动接管并恢复，恢复后行为与中断前一致；
* **超时重试**：执行层的重试、调度与上下文压缩由平台负责，客户端只需处理自身请求的错误码。

<Tip>
  如果你更想继续自建智能体循环、精细控制每一轮模型调用，请使用 [模型推理 API](/docs/api/overview)；托管智能体适合把长程任务的运行时整体托管出去的场景。
</Tip>

## 下一步

<CardGroup cols={3}>
  <Card title="智能体" icon="robot" href="/docs/hosted-agents/agents">
    把系统提示词与工具定义收敛为版本化的 Agent 配置。
  </Card>

  <Card title="会话" icon="message" href="/docs/hosted-agents/sessions">
    创建会话、发送事件，替代自建的智能体循环。
  </Card>

  <Card title="事件流" icon="bolt" href="/docs/hosted-agents/event-stream">
    订阅事件、断线续读与完整事件类型说明。
  </Card>
</CardGroup>
