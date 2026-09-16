> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 创建与管理智能体

> 创建、更新、版本管理和归档托管智能体的配置对象。

智能体（Agent）是托管智能体中 **持久化、版本化** 的配置对象：它定义了模型选择、系统提示词、可用工具等「怎么干」的内容。会话（Session）通过 `agent_id` 引用智能体来运行任务，并在创建时冻结当时的智能体版本。

<Info>
  智能体的配置每次更新都会生成一个 **不可变的新版本**，旧版本仍然完整保留。已经创建的会话继续使用创建时冻结的版本，不受后续更新影响——这保证了长任务中断恢复后行为完全一致。
</Info>

## 智能体字段

| 字段                                          | 类型               | 是否必填 | 说明                                                                                                                                                                                      |
| ------------------------------------------- | ---------------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                      | string           | 必填   | 智能体名称，1–256 字符                                                                                                                                                                          |
| `model`                                     | object \| string | 必填   | 模型选择：`"kimi-k3"` 直接给模型 ID 字符串，或 `{"id": "kimi-k3", "reasoning_effort": ..., "provider": ...}` 给结构化配置；`reasoning_effort`（`"low" \| "medium" \| "high"`，是否生效取决于模型）、`provider`（留空使用平台默认）可选 |
| `system`                                    | string           | 可选   | 系统提示词，最长 100,000 字符                                                                                                                                                                     |
| `tools`                                     | array\[object]   | 可选   | 工具声明列表，最多 128 个，内置工具集与 MCP 工具集可自由组合，见下文「工具声明」                                                                                                                                           |
| `mcp_servers`                               | array\[object]   | 可选   | MCP 服务连接信息，最多 20 个，`name` 在同一智能体内必须唯一，见下文「MCP 服务」                                                                                                                                       |
| `skills`                                    | array\[object]   | 可选   | 挂载的技能，见下文「技能引用」                                                                                                                                                                         |
| `plugins`                                   | array\[object]   | 可选   | 挂载的插件（Plugin），每项只需给出 `plugin_id`，版本由服务端在写入时固定，详见 [插件](/docs/hosted-agents/plugins)                                                                                                           |
| `description`                               | string           | 可选   | 描述，最长 2,048 字符                                                                                                                                                                          |
| `metadata`                                  | object           | 可选   | 自定义键值对，最多 16 条                                                                                                                                                                          |
| `multiagent`                                | object           | 可选   | 委派配置，`agents` 声明可委派的智能体名单（1–20 个），写入时固定引用的智能体版本，详见 [多智能体编排](/docs/hosted-agents/multiagent-orchestration)                                                                                    |
| `id`                                        | string           | 输出   | 稳定智能体 ID（`agent_` 前缀），创建后不变                                                                                                                                                             |
| `version`                                   | string           | 输出   | 当前不可变版本号，每次更新都会变化；更新请求可携带它做并发校验                                                                                                                                                         |
| `created_at` / `updated_at` / `archived_at` | string           | 输出   | 创建 / 最近更新 / 归档时间                                                                                                                                                                        |
| `scope`                                     | string           | 输出   | 资源归属范围，`"official"` 表示平台官方智能体                                                                                                                                                           |

### 工具声明

`tools` 数组用来声明智能体可以使用哪些工具。通过 `type` 字段区分类型：

| 类型      | `type` 值          | 说明                                                                                                                                                            |
| ------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 内置工具集   | `"agent_toolset"` | 声明平台内置工具集（文件读写、代码执行、搜索等）。`name` 必填，当前唯一取值为 `"default_toolset_20260901"`；`default_config` 设置整组默认（`enabled`、`permission_policy`、`load_mode`），`configs` 对单个工具做覆盖 |
| MCP 工具集 | `"mcp_toolset"`   | 暴露某个 MCP 服务的工具，`mcp_server_name` 引用同一智能体的 `mcp_servers` 中声明的名称；同样支持 `default_config` 与 `configs`                                                              |

如果不声明任何 `agent_toolset`，默认加载 `default_toolset_20260901` 的全部沙箱工具。显式声明一个或多个 `agent_toolset` 后，只加载声明的 `name`，不再追加默认值。要关闭沙箱工具，请显式声明 `default_toolset_20260901`，并将整个工具集的 `default_config.enabled` 设为 `false`。工具的配置细节见 [工具](/docs/hosted-agents/tools)。

### MCP 服务

`mcp_servers` 只保存连接元信息：`type`（当前仅支持 `"url"`）、`name`、`url`。**访问凭据不保存在智能体配置里**，而是在创建会话时通过凭据库（Vault）注入，详见 [MCP](/docs/hosted-agents/mcp) 与 [凭据库](/docs/hosted-agents/vaults)。

### 技能引用

`skills` 中的每一项包含 `skill_id` 与 `version`。创建或更新时 `version` 可以省略或填 `"latest"`，服务端会在写入新版本前解析为 **精确版本号** 并冻结——此后该智能体版本始终使用同一个技能版本，详见 [技能](/docs/hosted-agents/skills)。

## 官方智能体与自定义智能体

智能体分为两类：

|         | 官方智能体              | 自定义智能体         |
| ------- | ------------------ | -------------- |
| 来源      | 平台预置并维护            | 你通过 API 或控制台创建 |
| `scope` | `"official"`       | 你的项目           |
| 读取      | 所有用户可见             | 仅你的项目可见        |
| 修改 / 归档 | **不允许**（API 只读）    | 允许             |
| 创建会话    | 可以直接引用其 `agent_id` | 可以             |

<Note>
  官方智能体可读不可改：你可以查看它的完整配置、直接用它创建会话，但更新和归档请求会被拒绝。如需调整，参照官方智能体的配置创建你自己的自定义智能体。
</Note>

## 接口一览

| 操作     | 方法与路径                          |
| ------ | ------------------------------ |
| 创建智能体  | `POST /v1/agents`              |
| 列出智能体  | `GET /v1/agents`               |
| 获取智能体  | `GET /v1/agents/{id}`          |
| 更新智能体  | `PATCH /v1/agents/{id}`        |
| 归档智能体  | `POST /v1/agents/{id}/archive` |
| 列出版本历史 | `GET /v1/agents/{id}/versions` |

列出智能体时可传 `exclude_multiagent=true`，只返回未配置 `multiagent` 的智能体；配置委派名单时可以用它过滤掉本身已配置委派的智能体。

以下示例从环境变量 `KIMI_API_KEY` 读取 API Key；未设置 `API_BASE_URL` 时，请求地址默认使用 `https://api.moonshot.cn`。

## 创建智能体

创建一个最小可用的智能体只需要 `name` 和 `model`；通常还会填写系统提示词 `system`。创建成功后返回完整智能体对象，包含 `id` 与第一个 `version`，请保存 `id` 用于后续创建会话。

```bash theme={null}
curl -X POST ${API_BASE_URL:-https://api.moonshot.cn}/v1/agents \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "调研助手",
    "model": {"id": "kimi-k3"},
    "system": "你是一个严谨的调研助手，擅长检索、整理并引用资料。",
    "description": "面向深度调研任务的托管智能体"
  }'
```

## 更新智能体

更新采用 **不可变版本机制**：`PATCH` 不会原地修改配置，而是基于当前配置生成一个全新的不可变版本，旧版本完整保留在版本历史中。

两个要点：

1. **可选的 `version` 并发控制**：请求体可携带读取智能体时返回的当前 `version`；若智能体在此期间被修改，服务端返回 `409`，重新读取最新 `version` 后重试。不携带 `version` 则不做并发校验。
2. **出现的字段即被修改**：只替换请求体中出现的字段，未出现的字段保持原值，`null` 视为缺席。数组字段（`tools`、`mcp_servers`、`skills` 等）与 `metadata` 是 **整体替换**——传空数组或空对象即可清空该字段。

下面的示例只更新系统提示词，其余配置不变：

```bash theme={null}
curl -X PATCH ${API_BASE_URL:-https://api.moonshot.cn}/v1/agents/agent_xxx \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -H "Content-Type: application/json" \
  -d '{
    "version": "1",
    "system": "你是一个严谨的调研助手，所有结论都必须附带来源引用。"
  }'
```

<Tip>
  更新智能体不影响已经创建的会话——会话在创建时冻结了当时的智能体版本，中断恢复也会继续使用该版本。只有新建会话才会使用更新后的版本。
</Tip>

## 查看版本历史

每次更新都会留下一个不可变版本。通过版本历史接口可以回看任意历史版本的完整配置，接口分页返回，响应中的 `next_page_token` 用于翻页（没有更多时该字段缺席）。

```bash theme={null}
curl "${API_BASE_URL:-https://api.moonshot.cn}/v1/agents/agent_xxx/versions?page_size=10" \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta"
```

## 归档智能体

不再使用的智能体可以归档。归档后：

* 智能体变为 **只读**，不能再更新；
* **不能再用于创建新会话**；
* 已创建的会话不受影响，可继续运行与恢复。

归档成功返回 `204`，无响应体，无需解析响应 JSON。

```bash theme={null}
curl -X POST ${API_BASE_URL:-https://api.moonshot.cn}/v1/agents/agent_xxx/archive \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta"
```

<Warning>
  归档操作不可逆。请确认之后不再需要用它创建新会话，再执行归档。
</Warning>

## 下一步

<CardGroup cols={3}>
  <Card title="工具" icon="wrench" href="/docs/hosted-agents/tools">
    了解内置工具集的配置方式。
  </Card>

  <Card title="MCP" icon="plug" href="/docs/hosted-agents/mcp">
    为智能体接入 MCP 服务并注入访问凭据。
  </Card>

  <Card title="技能" icon="book" href="/docs/hosted-agents/skills">
    为智能体挂载版本化的技能包。
  </Card>

  <Card title="会话" icon="message" href="/docs/hosted-agents/sessions">
    用创建好的智能体启动一次任务。
  </Card>

  <Card title="凭据库" icon="key" href="/docs/hosted-agents/vaults">
    管理 MCP 等外部服务的访问凭据。
  </Card>
</CardGroup>
