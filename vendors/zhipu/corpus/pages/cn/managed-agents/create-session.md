> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 创建会话

Session 是一次实际运行的载体：它把一个 Agent 放进一个 Environment，维护对话历史与沙箱状态，通过事件与你的应用交互。会话是长生命周期、有状态的——可以持续数小时、跨多轮交互，随时恢复。

## 创建一个会话

最小请求只需要 **agent** 和 **environment\_id** 两个字段：

```bash theme={null}
session=$(curl -sS "$BASE_URL/v1/sessions" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "agent": "$AGENT_ID",
  "environment_id": "$ENVIRONMENT_ID",
  "title": "Data analysis session"
}
EOF
)

SESSION_ID=$(jq -r '.id' <<< "$session")
```

<Tip>
  会话事件加密：创建时加 **x-events-encrypted: true**，对话和工具 I/O 按客户密钥加密落库。开关创建后不能改。完整说明见 [会话事件数据加密](/cn/managed-agents/events#会话事件数据加密)。
</Tip>

请求字段：

| 字段                  | 说明                                                                                                                                                  |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **agent**           | 必填。Agent ID 字符串（等价于固定最新版本），或对象形态用于钉版本 / 覆盖配置，见下文。                                                                                                   |
| **environment\_id** | 必填。运行环境 ID（env\_ 前缀），必须引用你自己的、未归档的 Environment。创建时环境配置被固化为会话快照。                                                                                     |
| **title**           | 可选。标题，最大 256 字符。                                                                                                                                    |
| **metadata**        | 可选。最多 16 个 string 键值（key ≤64、value ≤512 字符）。                                                                                                        |
| **initial\_events** | 可选。最多 50 条初始 user.message 事件，见下文。                                                                                                                   |
| **resources**       | 可选。挂载 Memory Store 与 File Resource，合计最多 508 项（file ≤500 + memory\_store ≤8），见[文件](/cn/managed-agents/files)与[记忆](/cn/managed-agents/memory-stores)。 |
| **vault\_ids**      | 可选。最多 20 个不重复的 active Vault ID，顺序即凭据匹配优先级，见[凭据管理](/cn/managed-agents/vaults)。                                                                       |

响应是完整的 Session 对象。**agent** 字段回显解析后的配置快照（钉住的版本 ⊕ 会话级覆盖），**status** 初始为 **idle**：

```json theme={null}
{
  "id": "sess_xxxxxxxxxxxx",
  "type": "session",
  "agent": {
    "id": "agent_xxxxxxxxxxxx",
    "type": "agent",
    "name": "Coding Assistant",
    "model": { "id": "glm-5.3", "effort": "max", "speed": "standard" },
    "tools": [ ... ],
    "version": 3
  },
  "environment_id": "env_xxxxxxxxxxxx",
  "status": "idle",
  "title": "Data analysis session",
  "metadata": {},
  "resources": [],
  "vault_ids": [],
  "budget": null,
  "usage": {
    "input_tokens": 0,
    "output_tokens": 0,
    "cache_read_input_tokens": 0
  },
  "archived_at": null,
  "created_at": "2026-08-28T08:00:00.000Z",
  "updated_at": "2026-08-28T08:00:00.000Z"
}
```

<Note>
  响应中的 **budget** 字段当前恒为 **null**：平台暂不支持会话级消费上限，用量请通过 **usage** 字段与账单侧监控。
</Note>

## 用初始事件预置会话

创建时通过 **initial\_events** 预置最多 50 条 **user.message**，适合把既有对话上下文或任务说明一次性带入。会话不会因初始事件立即开始执行——它们只是进入事件历史，Agent 会在你发送第一条常规消息（或订阅事件流触发执行）后带着这些上下文工作：

```bash theme={null}
curl -sS "$BASE_URL/v1/sessions" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "agent": "$AGENT_ID",
  "environment_id": "$ENVIRONMENT_ID",
  "initial_events": [
    {
      "type": "user.message",
      "content": [
        {"type": "text", "text": "项目背景：我们在分析 2026 年 Q2 的销售数据。"}
      ]
    }
  ]
}
EOF
```

内容块约束：每条事件非空且至多 20 个内容块，类型为 **text** 或 **image**（初始事件不支持 document）；每条至多 3 张图片，每张 ≤5 MB。

## 为会话覆盖 Agent 配置

**agent** 的对象形态可以钉住特定版本，或在不改动 Agent 的前提下为单个会话覆盖配置：

```json theme={null}
{
  "agent": { "type": "agent", "id": "agent_xxxxxxxxxxxx", "version": 3 },
  "environment_id": "env_xxxxxxxxxxxx"
}
```

```json theme={null}
{
  "agent": {
    "type": "agent_with_overrides",
    "id": "agent_xxxxxxxxxxxx",
    "system": "You are a code reviewer. Only review, never modify files.",
    "tools": [
      {
        "type": "agent_toolset_20260601",
        "default_config": { "enabled": false },
        "configs": [
          { "name": "read", "enabled": true },
          { "name": "grep", "enabled": true }
        ]
      }
    ]
  },
  "environment_id": "env_xxxxxxxxxxxx"
}
```

覆盖语义：

* 可覆盖 **model**、**system**、**tools**、**mcp\_servers**、**skills**；每个字段都是**整体替换**（非深合并）。
* 覆盖只作用于本会话，Agent 本身不变；会话创建后覆盖即冻结。
* 覆盖含 **mcp\_toolset** 时须与 **agent.mcp\_servers** 一起提供，保证引用一致。
* 钉不存在的 **version** 返回 400，并在错误信息中提示当前最新版本。

## 通过 Vault 提供 MCP 鉴权

如果 Agent 声明了需要鉴权的 MCP 服务器，创建会话时传 **vault\_ids** 引用凭据集合。凭据按服务器 URL 匹配，详见[连接 MCP](/cn/managed-agents/mcp)与[凭据管理](/cn/managed-agents/vaults)。

## 启动会话

会话创建后处于 **idle** 状态，尚未供给沙箱。先打开事件流，再发消息——SSE 只转发连接建立后的实时事件，发完再订流会错过本轮进展。

典型的启动顺序：

1. 打开 SSE 事件流：**GET /v1/sessions/:id/events/stream**（保持连接）。
2. 发送第一条 **user.message** 事件：**POST /v1/sessions/:id/events**。
3. 会话进入 **running**：平台按环境快照供给沙箱、挂载资源与 Skill、启动 Agent 循环。
4. Agent 完成本轮工作后回到 **idle**（事件 **session.status\_idle**），等待你的下一条消息。

发送消息与处理事件的完整说明见[事件与流式输出](/cn/managed-agents/events)。

## 下一步

<CardGroup cols={2}>
  <Card title="管理会话" href="/cn/managed-agents/session-operations">
    查询、更新、归档与删除会话
  </Card>

  <Card title="事件与流式输出" href="/cn/managed-agents/events">
    事件类型、SSE、打断与引导
  </Card>

  <Card title="文件" href="/cn/managed-agents/files">
    向会话挂载输入文件
  </Card>

  <Card title="记忆" href="/cn/managed-agents/memory-stores">
    跨会话保留长期记忆
  </Card>

  <Card title="本页对应 OpenAPI" href="/cn/managed-agents/api-reference#sessions">
    Session：创建、列出、更新、事件
  </Card>
</CardGroup>
