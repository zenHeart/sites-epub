> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 连接 MCP

Managed Agents 支持把 Model Context Protocol（MCP）服务器接入你的 Agent，让 Agent 通过标准化协议访问外部工具、数据源和服务。

MCP 配置分为两步：

1. **创建 Agent 时**声明 Agent 要连接哪些 MCP 服务器（名称 + URL）。
2. **创建会话时**通过引用预先注册的 Vault 为这些服务器提供鉴权凭据（见[凭据管理](/cn/managed-agents/vaults)）。

这种分离让密钥不进入可复用的 Agent 定义，同时允许每个会话使用各自的凭据完成认证。没有匹配凭据时，连接会以未认证方式尝试；创建会话时不预检连通性。失败时会话仍会启动，并发出带 **mcp\_server\_name** 的 **session.error** 事件，见下文「处理连接与鉴权失败」。

## 在 Agent 上声明 MCP 服务器

创建 Agent 时在 **mcp\_servers** 数组中声明服务器。每个服务器需要 **type**、唯一的 **name** 和 **url**；这一步不提供任何鉴权 token。

每个声明的服务器还需要在 **tools** 数组中有一个对应的 **mcp\_toolset** 条目，其 **mcp\_server\_name** 必须与服务器的 **name** 一致。

```bash theme={null}
agent_response=$(curl -sS "$BASE_URL/v1/agents" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d @- <<'EOF'
{
  "name": "GitHub Assistant",
  "model": "glm-5.3",
  "mcp_servers": [
    {
      "type": "url",
      "name": "github",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  ],
  "tools": [
    {"type": "agent_toolset_20260601"},
    {"type": "mcp_toolset", "mcp_server_name": "github"}
  ]
}
EOF
)
AGENT_ID=$(jq -r '.id' <<<"$agent_response")
```

<Tip>
  MCP 工具集的默认权限策略是 **always\_allow**（与内置工具集相同）：MCP 工具调用默认直接执行。如果希望每次 MCP 调用都先经人工确认，为 mcp\_toolset 配置 **always\_ask**，见[工具权限](/cn/managed-agents/permission-policies)。
</Tip>

### mcp\_servers 字段参考

| 字段       | 说明                                                                                 |
| -------- | ---------------------------------------------------------------------------------- |
| **type** | 必填。当前固定为 **"url"**（Streamable HTTP transport）。                                     |
| **name** | 必填。服务器在该 Agent 内的唯一名称。它同时用作 tools 数组中的 **mcp\_server\_name**，并出现在会话事件流的 MCP 工具事件上。 |
| **url**  | 必填。远端 MCP 服务器的公网 HTTPS 地址。                                                         |

约束：一个 Agent 最多声明 20 个 MCP 服务器，名称不得重复；**mcp\_toolset** 的 **mcp\_server\_name** 必须引用已声明的服务器。更新 Agent 时，含 mcp\_toolset 的 **tools** 必须与 **mcp\_servers** 在同一次请求中一起替换，保证引用一致。

## 配置哪些 MCP 工具可用

**mcp\_toolset** 条目支持 **default\_config** 对象和 **configs** 数组，作用于该 MCP 服务器暴露的工具。每个 configs 条目只接受 **name**、**enabled**、**permission\_policy** 三个字段，其中 **name** 是服务器上报的原始工具名。

默认情况下服务器暴露的所有工具都启用。要只启用特定工具，把 **default\_config.enabled** 设为 false 再逐个打开：

```json theme={null}
{
  "type": "mcp_toolset",
  "mcp_server_name": "github",
  "default_config": { "enabled": false },
  "configs": [
    { "name": "get_issue", "enabled": true },
    { "name": "list_issues", "enabled": true },
    { "name": "add_issue_comment", "enabled": true }
  ]
}
```

这种模式适合服务器暴露了很多工具、但 Agent 只需要其中几个的场景，也可以让服务器运营方新增的工具默认保持关闭、待你审查后再启用。

要保持其余工具开启、只禁用个别工具，省略 default\_config、在单个条目上设 **enabled: false**：

```json theme={null}
{
  "type": "mcp_toolset",
  "mcp_server_name": "github",
  "configs": [{ "name": "delete_repository", "enabled": false }]
}
```

## 在创建会话时提供鉴权

启动会话时传入 **vault\_ids**，为 MCP 服务器提供凭据。Vault 是一组凭据的集合，注册一次后按 ID 引用，见[凭据管理](/cn/managed-agents/vaults)。

```bash theme={null}
session_response=$(curl -sS "$BASE_URL/v1/sessions" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "agent": "$AGENT_ID",
  "environment_id": "$ENVIRONMENT_ID",
  "vault_ids": ["$VAULT_ID"]
}
EOF
)
```

凭据按 URL 匹配：Vault 中需要存在一条 **mcp\_server\_url** 指向该服务器的凭据（类型为 **static\_bearer** 或 **mcp\_oauth**）。**vault\_ids** 最多 20 个、不得重复，数组顺序即凭据匹配的优先级。没有匹配凭据时，连接将以未认证方式尝试。

## 处理连接与鉴权失败

创建会话时不校验 MCP 的连通性或凭据。如果某个 MCP 服务器不可达或拒绝了凭据，会话仍会正常启动、正常交互。平台会发出 **session.error** 事件，其中包含出错服务器的 **mcp\_server\_name** 和重试状态 **retry\_status**（取值 **retrying** / **exhausted** / **terminal**）。

你可以自行决定：阻断后续交互、触发凭据轮换、或让会话在缺少该服务器工具的情况下继续。凭据校验也可以在会话之外主动完成：调用 **POST /v1/vaults/:vaultId/credentials/:credentialId/mcp\_oauth\_validate** 会对目标服务器发起 MCP initialize 探测，返回 **valid / invalid / unknown** 结论，见[凭据管理](/cn/managed-agents/vaults)。

## 下一步

<CardGroup cols={2}>
  <Card title="工具权限" href="/cn/managed-agents/permission-policies">
    控制内置与 MCP 工具的执行时机
  </Card>

  <Card title="凭据管理" href="/cn/managed-agents/vaults">
    注册凭据、验证 MCP OAuth、轮换密钥
  </Card>

  <Card title="事件与流式输出" href="/cn/managed-agents/events">
    处理 MCP 工具调用与结果事件
  </Card>

  <Card title="本页对应 OpenAPI" href="/cn/managed-agents/api-reference#agents">
    Agent：mcp\_servers 与 mcp\_toolset
  </Card>
</CardGroup>
