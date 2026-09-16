> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 权限策略

> 为托管智能体配置工具权限：禁用不需要的工具，并查看每次工具调用的评估结果。

控制托管智能体的工具行为靠两个字段：`enabled` 决定工具是否暴露给模型，`permission_policy` 决定模型调用工具时如何评估。用它们禁用写文件、执行命令、调用外部服务等可能改变外部状态的工具。

## 两个配置字段

| 字段                  | 决定什么        | 取值与默认                                     |
| ------------------- | ----------- | ----------------------------------------- |
| `enabled`           | 工具是否暴露给模型   | 默认启用；设为 `false` 时禁用，模型看不到也无法调用该工具         |
| `permission_policy` | 模型调用工具时如何评估 | 当前唯一公开取值为 `always_allow`：工具调用直接执行，不需要用户确认 |

两个字段都适用于内置工具集（`agent_toolset`）和 MCP 工具集（`mcp_toolset`），并且都可以在两个层级上设置：

* **工具集级**：在工具声明的 `default_config` 中设置，作为该工具集内所有工具的默认值；
* **单工具级**：在 `configs` 中对某个具体工具设置同名字段，覆盖工具集级默认值。

两个层级都未设置时，工具默认启用，并按 `always_allow` 评估——模型调用该工具时会直接执行。每次工具调用的评估结果都会通过 `agent.tool_use` 事件的 `evaluated_permission` 字段下发给客户端；当前该字段的值只会是 `always_allow`。

<Tip>
  推荐实践：只读、不改变外部状态的工具保持默认放行即可；不希望智能体使用的工具，在工具集级或单工具级设置 `enabled: false` 彻底禁用。
</Tip>

## 配置工具权限

在 [创建智能体](/docs/hosted-agents/agents) 时，通过工具声明携带这两个字段。已有智能体也可以修改这两个配置：[更新智能体](/docs/hosted-agents/agents#更新智能体) 时传入 `tools` 字段即可（`tools` 会整体替换当前工具声明），更新会生成新的智能体版本，无需重建。下面的示例为内置工具集设置默认自动放行，并把其中的写文件工具单独禁用：

```bash theme={null}
curl -X POST ${API_BASE_URL:-https://api.moonshot.cn}/v1/agents \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "代码助手",
    "model": {"id": "kimi-k3"},
    "system": "你是一个严谨的代码助手。",
    "tools": [
      {
        "type": "agent_toolset",
        "name": "default_toolset_20260901",
        "default_config": {
          "permission_policy": "always_allow"
        },
        "configs": [
          {
            "name": "write_file",
            "enabled": false
          }
        ]
      }
    ]
  }'
```

### MCP 工具集

MCP 工具集同样在 `default_config` 和 `configs` 中设置 `enabled` 与 `permission_policy`。`mcp_server_name` 必须引用同一智能体 `mcp_servers` 中已声明的服务；`configs[].name` 使用该 MCP 服务实际提供的工具名。

```json theme={null}
{
  "type": "mcp_toolset",
  "mcp_server_name": "todo",
  "default_config": {
    "permission_policy": "always_allow"
  },
  "configs": [
    {
      "name": "delete_task",
      "enabled": false
    }
  ]
}
```

MCP 服务的声明方式、工具名来源，以及服务清单变化后 `configs` 的生效规则见 [接入 MCP](/docs/hosted-agents/mcp)。

## 下一步

<CardGroup cols={3}>
  <Card title="工具" icon="wrench" href="/docs/hosted-agents/tools">
    了解内置工具集与 MCP 工具的声明方式。
  </Card>

  <Card title="订阅事件流" icon="bolt" href="/docs/hosted-agents/event-stream">
    实时接收工具调用与会话状态事件。
  </Card>
</CardGroup>
