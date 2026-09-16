> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 定义 Agent

Agent 是一份可复用、带版本的配置，定义了 Agent 的角色与能力。它把模型、系统提示词、工具、MCP 服务器和 Skills 打包在一起，决定模型在会话中的行为方式。

Agent 创建一次即可作为可复用资源存在，每次创建会话时通过 ID 引用。Agent 是版本化的，便于在大量会话之间统一管理。

<Tip>
  所有 Managed Agents 请求都需要携带 **zai-version: 2026-05-26** 与 **zai-beta: managed-agents-2026-05-26** 请求头。
</Tip>

## Agent 配置字段

| 字段               | 说明                                                                                                                                                                   |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **name**         | 必填。人类可读的 Agent 名称，1–256 字符。                                                                                                                                          |
| **model**        | 必填。驱动 Agent 的 GLM 模型。当前仅支持 **glm-5.3** 与 **glm-5.3-flash**。接受模型 ID 字符串，或对象形态如 **`{"id": "glm-5.3", "effort": "max"}`**；对象形态还可携带 **speed**（当前仅 standard）。见下文「设置推理强度」。 |
| **system**       | 系统提示词，定义 Agent 的行为与人设。系统提示词与用户消息不同：前者定义「你是谁、怎么做事」，后者描述「这次要做什么」。                                                                                                      |
| **tools**        | Agent 可用的工具。可组合内置工具集（agent\_toolset\_20260601）、MCP 工具集（mcp\_toolset）与自定义工具（custom）。省略该字段不会自动启用内置工具，创建时请显式加入 **agent\_toolset\_20260601**。                            |
| **mcp\_servers** | 提供标准化第三方能力的 MCP 服务器声明。                                                                                                                                               |
| **skills**       | 为 Agent 提供领域知识的 Skills，按需渐进加载。                                                                                                                                       |
| **description**  | Agent 用途说明。                                                                                                                                                          |
| **metadata**     | 任意键值对，供你自己做标记与追踪。                                                                                                                                                    |

你也可以在创建单个会话时临时覆盖 **model**、**system**、**tools**、**mcp\_servers**、**skills**，而不改动 Agent 本身，见[创建会话](/cn/managed-agents/create-session)的配置覆盖章节。

## 创建 Agent

下面的示例定义了一个使用 glm-5.3、可访问全套内置工具的编码 Agent：

```bash theme={null}
agent=$(curl -sS "$BASE_URL/v1/agents" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d '{
    "name": "Coding Assistant",
    "model": "glm-5.3",
    "system": "You are a helpful coding agent.",
    "tools": [{"type": "agent_toolset_20260601"}]
  }')

AGENT_ID=$(jq -r '.id' <<< "$agent")
AGENT_VERSION=$(jq -r '.version' <<< "$agent")
```

响应会回显你的配置，并补充 **id**、**type**、**version**、**created\_at**、**updated\_at**、**archived\_at** 字段；你省略的 model 子字段（如 effort）会以默认值补全。**version** 从 1 开始，每次更新导致配置变化时递增：

```json theme={null}
{
  "id": "agent_xxxxxxxxxxxx",
  "type": "agent",
  "name": "Coding Assistant",
  "model": {
    "id": "glm-5.3",
    "effort": "max",
    "speed": "standard"
  },
  "system": "You are a helpful coding agent.",
  "description": null,
  "tools": [
    {
      "type": "agent_toolset_20260601",
      "default_config": {
        "enabled": true,
        "permission_policy": { "type": "always_allow" }
      }
    }
  ],
  "skills": [],
  "mcp_servers": [],
  "metadata": {},
  "version": 1,
  "created_at": "2026-08-20T08:24:10.412Z",
  "updated_at": "2026-08-20T08:24:10.412Z",
  "archived_at": null
}
```

工具集上的 **default\_config** 显示了它的默认权限策略 **always\_allow**；不做任何配置时即按此执行。权限策略详见[工具权限](/cn/managed-agents/permission-policies)。

### 设置推理强度

要设置模型的推理强度（effort），把 **model** 写成对象形态，例如 **`{"id": "glm-5.3", "effort": "max"}`**。各模型支持的档位与默认值不同：

| 模型            | 可用档位             | 默认档位 |
| :------------ | :--------------- | :--- |
| glm-5.3       | low / high / max | max  |
| glm-5.3-flash | low / high / max | high |

当前仅支持以上两款模型。缺省或显式传 **null** 时取该模型的默认档位。**speed** 字段当前所有模型仅支持 **standard**。

## 更新 Agent

更新会在配置发生变化时生成一个新版本。**version** 可选：带上当前版本号时，如果这期间别人已经改过这个 Agent，接口返回 409，避免你覆盖刚发生的改动；不带则直接按你提交的内容覆盖。已归档的 Agent 拒绝更新。

```bash theme={null}
updated_agent=$(curl -sS "$BASE_URL/v1/agents/$AGENT_ID" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d "{
    \"version\": $AGENT_VERSION,
    \"system\": \"You are a helpful coding agent. Always write tests.\"
  }")

echo "New version: $(jq -r '.version' <<< "$updated_agent")"
```

上面的示例携带了创建响应中的 **version**，因此只有在此后没有其他调用者改过这个 Agent 时更新才会生效。要无条件更新，省略 **version** 即可。交互式调用建议携带 version；声明式同步循环（例如 CI 把仓库里的 Agent 定义同步到平台）适合省略。

### 更新语义

* **省略的字段保持不变。** 只需要提交你想改的字段。
* **标量字段**（model、system、name、description）整体替换为新值。**system** 和 **description** 可传 null 清空；**name** 和 **model** 必填、不可清空。
* **数组字段**（tools、mcp\_servers、skills）整体替换为新数组，传 null 或空数组可全部清空。注意：tools 中包含 **mcp\_toolset** 时，必须与 **mcp\_servers** 在同一次请求中一起替换，保证引用一致。
* **metadata** 按键级合并：提交的键新增或覆盖，未提交的键保留，把某个键设为 null 可删除它。
* **无变化检测**：如果更新结果与当前版本完全一致，不会生成新版本，直接返回现有版本。

## Agent 生命周期

| 操作       | 行为                                   |
| -------- | ------------------------------------ |
| **更新**   | 配置变化时生成新版本                           |
| **列出版本** | 返回完整版本历史，每个条目都是该版本的完整 Agent 配置快照     |
| **归档**   | Agent 变为只读：新会话不能再引用它，已有会话继续运行。归档操作幂等 |

### 列出版本

```bash theme={null}
curl -sS "$BASE_URL/v1/agents/$AGENT_ID/versions" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  | jq -r '.data[] | "Version \(.version): \(.updated_at)"'
```

结果分页返回，翻页使用响应中的 **page** 游标。每个条目的时间戳是版本级的（各版本有自己的 created\_at / updated\_at），**archived\_at** 保持 Agent 级。

### 归档 Agent

```bash theme={null}
curl -sS -X POST "$BASE_URL/v1/agents/$AGENT_ID/archive" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26"
```

归档后响应中的 **archived\_at** 会填充时间戳。重复归档同一个 Agent 是幂等的，返回相同结果。

## 下一步

<CardGroup cols={2}>
  <Card title="工具" href="/cn/managed-agents/tools">
    配置内置工具集与自定义工具
  </Card>

  <Card title="连接 MCP" href="/cn/managed-agents/mcp">
    声明 MCP 服务器扩展能力
  </Card>

  <Card title="工具权限" href="/cn/managed-agents/permission-policies">
    控制工具执行前是否需要确认
  </Card>

  <Card title="创建会话" href="/cn/managed-agents/create-session">
    引用 Agent 启动会话，或按会话覆盖配置
  </Card>

  <Card title="本页对应 OpenAPI" href="/cn/managed-agents/api-reference#agents">
    Agent：创建、列出、更新、归档
  </Card>
</CardGroup>
