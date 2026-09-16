> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 工具

Managed Agents 提供一组内置工具，Agent 在会话中可以自主使用它们。你通过 Agent 配置中的 **tools** 数组控制哪些工具可用。

平台同时支持自定义工具（custom tools）：由你的应用在平台之外执行，把结果返回给 Agent，Agent 据此继续任务。要让 Agent 使用来自 MCP 服务器的工具，请改用[连接 MCP](/cn/managed-agents/mcp)。

<Tip>
  创建 Agent 时省略 **tools** 字段等价于空数组——内置工具**不会**被自动启用。要让 Agent 具备沙箱操作能力，必须显式加入 **agent\_toolset\_20260601** 工具集。
</Tip>

## 可用工具

内置工具集（agent\_toolset\_20260601）当前包含以下工具。把工具集加入 Agent 配置后，下表工具默认全部启用。**configs** 数组中的每个条目通过 **name** 字段识别：

| 工具    | Name      | 说明                    |
| ----- | --------- | --------------------- |
| Bash  | **bash**  | 在 shell 会话中执行 bash 命令 |
| Read  | **read**  | 读取沙箱文件系统中的文件          |
| Write | **write** | 向沙箱文件系统写入文件           |
| Edit  | **edit**  | 对文件执行字符串替换编辑          |
| Grep  | **grep**  | 使用正则表达式做文本检索          |
| Find  | **find**  | 按名称模式查找文件             |
| Ls    | **ls**    | 列出目录内容                |

<Note>
  **Web Search**（**web\_search**）与 **Web Fetch**（**web\_fetch**）近期即将支持，当前工具集还不包含；上线后将单独计费。
</Note>

## 配置工具集

创建 Agent 时用 **agent\_toolset\_20260601** 启用完整工具集，用 **configs** 数组关闭特定工具或覆盖其设置。每个 config 条目还可以设置 **permission\_policy**，控制该工具的调用是自动放行还是需要确认，见[工具权限](/cn/managed-agents/permission-policies)。

```bash theme={null}
agent=$(curl -sS "$BASE_URL/v1/agents" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d @- <<'EOF'
{
  "name": "Coding Assistant",
  "model": "glm-5.3",
  "tools": [
    {
      "type": "agent_toolset_20260601",
      "configs": [
        {"name": "bash", "permission_policy": {"type": "always_ask"}}
      ]
    }
  ]
}
EOF
)
```

### 关闭特定工具

在工具集对象的 **configs** 数组里把对应条目的 **enabled** 设为 false：

```json theme={null}
{
  "type": "agent_toolset_20260601",
  "configs": [
    { "name": "write", "enabled": false },
    { "name": "edit", "enabled": false }
  ]
}
```

### 只启用特定工具

**default\_config** 对象为集合内所有工具设定基线，逐工具的 **configs** 条目覆盖它。要从「全部关闭」出发只开需要的工具，把 **default\_config.enabled** 设为 false：

```json theme={null}
{
  "type": "agent_toolset_20260601",
  "default_config": { "enabled": false },
  "configs": [
    { "name": "bash", "enabled": true },
    { "name": "read", "enabled": true },
    { "name": "write", "enabled": true }
  ]
}
```

省略或传 null 的字段按继承规则回退：**configs\[].enabled** 继承 **default\_config.enabled**（默认 true），**configs\[].permission\_policy** 继承 **default\_config.permission\_policy**（默认 always\_allow）。单个 Agent 最多声明 128 个工具条目。

会话处于 **idle** 时，也可以整体替换 **agent.tools**（运行中需先 **user.interrupt**，否则 409 session\_not\_idle），见[管理会话](/cn/managed-agents/session-operations)。

## 自定义工具

除内置工具外，你还可以定义自定义工具。每个自定义工具定义了一份契约：你声明有哪些操作可用、返回什么，模型决定何时以及如何调用。模型自己不会执行任何东西——它发出一个结构化请求，你的代码执行操作，把结果送回对话。

自定义工具的调用与结果通过会话事件流完成：平台派发 **agent.custom\_tool\_use** 事件，你的应用执行后回发 **user.custom\_tool\_result** 事件。完整交互流程见[事件与流式输出](/cn/managed-agents/events)。

```bash theme={null}
agent=$(curl -sS "$BASE_URL/v1/agents" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d @- <<'EOF'
{
  "name": "Weather Agent",
  "model": "glm-5.3",
  "tools": [
    {
      "type": "agent_toolset_20260601"
    },
    {
      "type": "custom",
      "name": "get_weather",
      "description": "Get current weather for a location",
      "input_schema": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "City name"}
        },
        "required": ["location"]
      }
    }
  ]
}
EOF
)
```

自定义工具的字段约束：

| 字段                | 约束                                                                   |
| ----------------- | -------------------------------------------------------------------- |
| **name**          | 1–128 字符，仅允许字母、数字、下划线和连字符；不得以 **mcp\_\_** 开头；同一 Agent 内不得重名          |
| **description**   | 1–4096 字符                                                            |
| **input\_schema** | JSON Schema，要求 **type: "object"** 且包含 **properties**，可选 **required** |

<Tip>
  自定义工具依赖客户端实时在线响应。创建定时任务时接口不会拒绝带自定义工具的 Agent，但触发后没人回结果，会话会停在 **requires\_action**。无人值守的 cron 请只用内置工具。详见[定时任务](/cn/managed-agents/deployments)。
</Tip>

### 自定义工具的最佳实践

* **写极其详细的描述。** 这是影响工具调用效果的最重要因素。描述应说明工具做什么、什么时候用（以及什么时候不用）、每个参数的含义与影响、重要的注意事项与限制。每个工具至少三四句话，复杂工具更多。
* **把相关操作合并为更少的工具。** 与其为每个动作单独建工具（create\_pr、review\_pr、merge\_pr），不如合成一个带 action 参数的工具。更少而更强的工具能降低模型选择时的歧义。
* **工具名使用有意义的命名空间。** 当工具横跨多个服务或资源时，用资源名做前缀（例如 db\_query、storage\_read），随着工具增多仍能保持选择无歧义。
* **让工具响应只返回高信号信息。** 返回语义化、稳定的标识符（如 slug 或 UUID）而非内部引用，只包含模型决定下一步所需的字段。臃肿的响应浪费上下文，也让模型更难提取关键信息。

## 下一步

<CardGroup cols={2}>
  <Card title="连接 MCP" href="/cn/managed-agents/mcp">
    接入 MCP 服务器，获得外部工具与数据源
  </Card>

  <Card title="工具权限" href="/cn/managed-agents/permission-policies">
    控制内置与 MCP 工具的执行时机
  </Card>

  <Card title="事件与流式输出" href="/cn/managed-agents/events">
    发送事件、处理自定义工具调用
  </Card>

  <Card title="本页对应 OpenAPI" href="/cn/managed-agents/api-reference#agents">
    Agent：创建与更新时的 tools 字段
  </Card>
</CardGroup>
