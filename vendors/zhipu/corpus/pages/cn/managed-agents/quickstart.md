> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速入门

本指南将带你完成：创建一个 Agent、配置运行环境、启动会话、流式接收响应，并下载产出文件。全程只需要 curl 和一个智谱开放平台 API Key，大约 5 分钟。

## 核心概念

| 概念              | 说明                                           |
| --------------- | -------------------------------------------- |
| **Agent**       | 模型、系统提示词、工具、MCP 服务器和 Skills 的组合定义            |
| **Environment** | 会话运行环境的声明式配置：软件包与网络策略                        |
| **Session**     | 在环境中运行的一个 Agent 实例，执行任务并产出结果                 |
| **Events**      | 你的应用与 Agent 之间交换的消息（用户输入、Agent 回复、工具调用、状态更新） |

## 前置条件

* 一个智谱开放平台账号
* 一个智谱开放平台 API Key

## 配置鉴权

Managed Agents 是标准的 HTTP + SSE 接口，任何语言都可以直接调用。先把智谱开放平台 API Key 和基础地址设置为环境变量：

```bash theme={null}
export ZHIPUAI_API_KEY="your-api-key-here"
export BASE_URL="https://agent-api.bigmodel.cn/api/agent/managed"
```

<Tip>
  所有 Managed Agents 请求都需要携带版本头 **zai-version: 2026-05-26** 和 Beta 头 **zai-beta: managed-agents-2026-05-26**。
</Tip>

## 创建你的第一个会话

<Steps>
  <Step title="创建 Agent">
    创建一个 Agent，定义模型、系统提示词和可用工具：

    ```bash theme={null}
    agent=$(
      curl -sS "$BASE_URL/v1/agents" \
        -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
        -H "zai-version: 2026-05-26" \
        -H "zai-beta: managed-agents-2026-05-26" \
        -H "content-type: application/json" \
        -d @- <<'EOF'
    {
      "name": "Coding Assistant",
      "model": "glm-5.3",
      "system": "You are a helpful coding assistant. Write clean, well-documented code.",
      "tools": [
        {"type": "agent_toolset_20260601"}
      ]
    }
    EOF
    )

    AGENT_ID=$(jq -er '.id' <<<"$agent")
    echo "Agent ID: $AGENT_ID"
    ```

    **agent\_toolset\_20260601** 这个工具类型会启用全套内置 Agent 工具（bash、文件操作等）。完整列表与逐项配置见 [工具](/cn/managed-agents/tools)。

    记下返回的 **agent.id**，后面每次创建会话都要引用它。

    <Tip>
      省略 **tools** 不会自动启用内置工具。上面的示例已显式加入 **agent\_toolset\_20260601**。
    </Tip>
  </Step>

  <Step title="创建 Environment">
    Environment 定义 Agent 运行所在的沙箱：

    ```bash theme={null}
    environment=$(
      curl -sS "$BASE_URL/v1/environments" \
        -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
        -H "zai-version: 2026-05-26" \
        -H "zai-beta: managed-agents-2026-05-26" \
        -H "content-type: application/json" \
        -d @- <<'EOF'
    {
      "name": "quickstart-env",
      "config": {
        "type": "cloud",
        "networking": {"type": "unrestricted"}
      }
    }
    EOF
    )

    ENVIRONMENT_ID=$(jq -er '.id' <<<"$environment")
    echo "Environment ID: $ENVIRONMENT_ID"
    ```

    记下返回的 **environment.id**。你可以在多个会话中复用同一个 Environment；需要预装软件包或收紧网络策略时，见 [配置运行环境](/cn/managed-agents/cloud-environment)。
  </Step>

  <Step title="启动 Session">
    创建一个会话，引用上面的 Agent 和 Environment：

    ```bash theme={null}
    session=$(
      curl -sS "$BASE_URL/v1/sessions" \
        -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
        -H "zai-version: 2026-05-26" \
        -H "zai-beta: managed-agents-2026-05-26" \
        -H "content-type: application/json" \
        -d @- <<EOF
    {
      "agent": "$AGENT_ID",
      "environment_id": "$ENVIRONMENT_ID",
      "title": "Quickstart session"
    }
    EOF
    )

    SESSION_ID=$(jq -er '.id' <<<"$session")
    echo "Session ID: $SESSION_ID"
    ```
  </Step>

  <Step title="订阅事件并发送消息">
    先订阅 SSE，再发消息。流只推送连接建立之后的事件，发消息前未打开流会错过实时进展。

    打开一个 SSE 流订阅实时事件（保持这个终端不退出）：

    ```bash theme={null}
    curl -N "$BASE_URL/v1/sessions/$SESSION_ID/events/stream" \
      -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
      -H "zai-version: 2026-05-26" \
      -H "zai-beta: managed-agents-2026-05-26"
    ```

    然后在另一个终端发送用户消息事件：

    ```bash theme={null}
    curl -sS "$BASE_URL/v1/sessions/$SESSION_ID/events" \
      -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
      -H "zai-version: 2026-05-26" \
      -H "zai-beta: managed-agents-2026-05-26" \
      -H "content-type: application/json" \
      -d @- <<'EOF'
    {
      "events": [
        {
          "type": "user.message",
          "content": [
            {
              "type": "text",
              "text": "Create a Python script that generates the first 20 Fibonacci numbers and saves them to /mnt/session/outputs/fibonacci.txt"
            }
          ]
        }
      ]
    }
    EOF
    ```

    Agent 会编写一个 Python 脚本、在沙箱里运行它、并把结果写到产出目录。终端 1 里会依次收到类似这些事件：

    ```text theme={null}
    event: agent.message
    data: {"type":"agent.message","content":[{"type":"text","text":"I'll create a Python script ..."}], ...}

    event: agent.tool_use
    data: {"type":"agent.tool_use","name":"write", ...}

    event: agent.tool_use
    data: {"type":"agent.tool_use","name":"bash", ...}

    event: session.status_idle
    data: {"type":"session.status_idle", ...}
    ```

    在你的应用代码里，通常只需要处理三类事件：**agent.message**（拼接文本展示给用户）、**agent.tool\_use**（展示 Agent 正在做什么）、**session.status\_idle**（本轮工作完成）。完整事件类型见 [事件与流式输出](/cn/managed-agents/events)。
  </Step>

  <Step title="下载产出文件">
    **session.status\_idle** 表示本轮结束。Agent 写入 **/mnt/session/outputs** 的文件会被编目，可用 Files API 列出并下载：

    ```bash theme={null}
    files=$(curl -sS "$BASE_URL/v1/files?scope_id=$SESSION_ID" \
      -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
      -H "zai-version: 2026-05-26" \
      -H "zai-beta: managed-agents-2026-05-26")

    FILE_ID=$(jq -er '.data[0].id' <<<"$files")
    echo "Output file: $FILE_ID"
    ```

    ```bash theme={null}
    curl -sS -L "$BASE_URL/v1/files/$FILE_ID/content" \
      -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
      -H "zai-version: 2026-05-26" \
      -H "zai-beta: managed-agents-2026-05-26" \
      -o fibonacci.txt
    ```

    输入材料与产出文件的路径约定见 [文件](/cn/managed-agents/files)。
  </Step>
</Steps>

## 背后发生了什么

当你发送一个用户事件时，Managed Agents 会：

1. **供给沙箱**：按你的 Environment 配置构建并启动运行环境。
2. **运行 Agent 循环**：模型根据你的消息自主决定使用哪些工具。
3. **执行工具**：文件写入、bash 命令等都在沙箱内执行。
4. **流式推送事件**：Agent 工作过程中你实时收到进展更新。
5. **进入空闲**：Agent 完成本轮工作后发出 **session.status\_idle** 事件，等待你的下一条消息。
6. **取回产出**：写在 **/mnt/session/outputs** 的文件可按会话列出并下载。

会话是有状态的：沙箱文件系统和对话历史都会保留。你可以在同一个会话里继续发送消息，Agent 会带着完整上下文继续工作。

## 下一步

<CardGroup cols={2}>
  <Card title="定义 Agent" href="/cn/managed-agents/agent-setup">
    创建可复用、带版本的 Agent
  </Card>

  <Card title="配置运行环境" href="/cn/managed-agents/cloud-environment">
    自定义软件包与网络策略
  </Card>

  <Card title="工具" href="/cn/managed-agents/tools">
    为 Agent 启用或限制特定工具
  </Card>

  <Card title="事件与流式输出" href="/cn/managed-agents/events">
    处理事件、在执行途中引导 Agent
  </Card>

  <Card title="最佳实践" href="/cn/managed-agents/examples">
    客服、数据分析等常见配法
  </Card>

  <Card title="定时任务" href="/cn/managed-agents/deployments">
    按 cron 计划周期性运行 Agent
  </Card>
</CardGroup>
