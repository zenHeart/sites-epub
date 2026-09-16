> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 接入 MCP

> 在智能体上声明 MCP 服务，通过凭据库注入访问凭据，让托管智能体调用第三方 MCP 工具。

MCP（Model Context Protocol）是连接第三方能力的标准协议。托管智能体原生支持接入远程 MCP 服务：你在智能体上声明服务地址，平台在会话运行时自动建立连接、拉取工具清单并暴露给模型——工具的发现、调用与结果回流全部由平台完成，你不需要编写任何 MCP 客户端代码。

接入分为两步，职责清晰分离：

* **在智能体上声明连接**：`mcp_servers` 只保存服务的名称与地址，不含任何凭据；
* **创建会话时注入凭据**：访问凭据保存在 [凭据库（Vault）](/docs/hosted-agents/vaults) 中，创建会话时按凭据库 ID 绑定，平台按服务地址自动匹配并注入。

<Info>
  这样的分离让同一份智能体配置可以服务多个最终用户：每个用户有自己的凭据库和凭据，智能体定义保持通用。
</Info>

以下示例中的 API Key 从环境变量 `KIMI_API_KEY` 读取，API 地址从环境变量 `API_BASE_URL` 读取（示例值 `https://api.moonshot.cn`）。

## 声明 MCP 服务

在创建或更新智能体时，通过 `mcp_servers` 字段声明 MCP 服务：

| 字段     | 类型     | 说明                                                                 |
| ------ | ------ | ------------------------------------------------------------------ |
| `type` | string | 服务类型，当前仅支持 `"url"`（远程服务，streamable HTTP 传输）                        |
| `name` | string | 服务名称，在同一智能体内必须唯一；需要单独配置工具时，供 `mcp_toolset` 通过 `mcp_server_name` 引用 |
| `url`  | string | MCP 服务的端点地址，也是凭据库中凭据的匹配键                                           |

数量限制为每个智能体最多 20 个 MCP 服务。**声明即暴露**：连接成功后，该 MCP 服务提供的全部工具默认就会对模型可用，不需要额外声明 `mcp_toolset`。只有需要单独配置工具时，才在 `tools` 中使用 `mcp_toolset`，通过 `mcp_server_name` 引用同名的服务，并配置 `default_config` 或 `configs`。

```bash theme={null}
curl -X POST ${API_BASE_URL:-https://api.moonshot.cn}/v1/agents \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "项目助手",
    "model": {"id": "kimi-k3"},
    "system": "你是一个项目管理助手，帮用户跟踪任务进展。",
    "mcp_servers": [
      {
        "type": "url",
        "name": "todo",
        "url": "https://mcp.example.com/mcp"
      }
    ]
  }'
```

<Note>
  `url` 是凭据匹配的键，请以规范的服务端点形式填写，不要携带 query 参数、片段（fragment）或用户信息——这类地址无法与凭据库中的凭据匹配，平台会在创建时拒绝写入。
</Note>

### 按工具配置开关与权限

需要精细控制时，可以在 `tools` 中用 `mcp_toolset` 引用某个已声明的服务，按工具覆盖配置；不需要覆盖时省略即可（默认全量暴露）：

```json theme={null}
{
  "tools": [
    {
      "type": "mcp_toolset",
      "mcp_server_name": "todo",
      "default_config": {"enabled": true},
      "configs": [
        {"name": "delete_task", "enabled": false}
      ]
    }
  ]
}
```

| 配置项                           | 说明                                              |
| ----------------------------- | ----------------------------------------------- |
| `mcp_server_name`             | 必填，引用同一智能体 `mcp_servers` 中声明的服务名称               |
| `default_config.enabled`      | 该服务全部工具的默认开关，未设置时默认启用                           |
| `configs[].name`              | MCP 服务提供的原始工具名                                  |
| `configs[].enabled`           | 按工具覆盖开关；被禁用的工具不会进入模型上下文                         |
| `configs[].permission_policy` | 按工具设置权限策略，详见 [权限策略](/docs/hosted-agents/permissions) |

`configs` 引用了服务已不提供的工具名不会报错，该条配置被静默忽略——服务端的工具清单可能随版本变化，智能体配置不应因此失效。

<Tip>
  权限策略当前唯一公开取值为 `always_allow`，`always_ask` 暂未开放。对可能改变外部状态的工具（删除、发送、支付等），建议用 `enabled: false` 禁用，详见 [权限策略](/docs/hosted-agents/permissions)。
</Tip>

## 通过凭据库注入凭据

`mcp_servers` 中不放任何凭据。访问凭据保存在凭据库中，创建会话时在 `resources` 里绑定，不同凭据类型按各自的匹配条件处理：

* **`environment_variable` 凭据**：用于允许的出站请求占位符替换，不作为 MCP 服务的连接凭据。真实凭据不会写入文件系统或环境变量；
* **MCP 凭据**：`mcp_oauth` 和 `static_bearer` 按 MCP 服务地址（`url`）匹配。匹配成功后，连接携带相应的认证信息；没有匹配凭据时，平台会以匿名方式连接，不会自动补充认证信息；
* **多个凭据库命中同一服务地址**：按 `resources` 中的绑定顺序，第一个匹配的凭据库生效。

带刷新配置的 `mcp_oauth` 凭据在 access token 过期时由平台自动刷新，无需你介入（OAuth Connect 落成的凭据在提供方发放刷新令牌时自带刷新配置）。

```bash theme={null}
curl -X POST ${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "agent_your_agent_id",
    "environment_id": "env_your_environment_id",
    "resources": [
      { "type": "vault", "vault_id": "vlt_your_vault_id" }
    ],
    "title": "整理本周任务"
  }'
```

`agent_id` 用上一步创建智能体响应中的 `id`；`environment_id`、`vault_id` 分别来自执行环境和凭据库的创建响应。

凭据库的绑定在创建会话时确定，创建后不能追加。凭据的轮换、归档对会话自动生效——平台在每次连接建立时重新解析凭据，最迟在下一次连接时拿到新值，无需重建会话。

凭据的创建与管理详见 [凭据库](/docs/hosted-agents/vaults)；`resources` 绑定机制详见 [会话](/docs/hosted-agents/sessions)。

## MCP OAuth Connect 授权

如果 MCP 服务使用 OAuth 2.0 授权，你不需要让最终用户手动复制 token。平台提供 **MCP OAuth Connect** 授权流：平台带着最终用户走完标准的 OAuth 授权码流程，授权完成后 token 自动落成凭据库凭据，你全程不经手任何凭据明文。

授权入口有两处：

<CardGroup cols={2}>
  <Card title="控制台 Connect" icon="display" href="/docs/hosted-agents/console">
    在凭据库页面或插件页面点击 Connect，按弹窗引导完成授权，token 自动入库。
  </Card>

  <Card title="授权会话 API" icon="code" href="/docs/hosted-agents/vaults">
    通过 `POST /v1/vaults/{vault_id}/oauth-sessions` 发起授权、引导用户打开授权页、轮询授权结果，适合嵌入你自己的产品界面。
  </Card>
</CardGroup>

授权完成后落成的凭据与手动创建的 `mcp_oauth` 凭据完全等价：同样的按地址匹配注入规则，同样由平台托管刷新。同一凭据库、同一服务地址已有活跃凭据时再次发起会返回 409，归档旧凭据后即可重新授权。

完整的 API 流程与字段说明见 [凭据库](/docs/hosted-agents/vaults) 的「MCP OAuth Connect 授权」一节。

## 运行时行为与注意事项

### 连接生命周期

MCP 连接跟随会话的执行节奏：会话每次被唤醒执行任务时，平台对每个声明的服务建立连接、拉取最新工具清单，执行结束后关闭。这意味着：

* 凭据轮换、工具清单变化最迟在下一次唤醒时生效；
* 每次唤醒建立连接会引入少量建连延迟，引用多个 MCP 服务时各服务的连接并行建立。

### 连接失败与降级

单个 MCP 服务不可用 **不会导致会话失败**，平台按服务粒度降级：

| 故障                | 行为                                         |
| ----------------- | ------------------------------------------ |
| 服务连不上、初始化超时、鉴权被拒绝 | 跳过该服务的全部工具，本轮模型看不到它们，会话与其他工具不受影响；下一次唤醒自动重连 |
| 工具调用过程中连接中断或超时    | 失败作为工具错误结果返回给模型，模型可以重试或调整策略；会话不中断          |
| 凭据库中无匹配凭据         | 匿名连接（合法配置，不报错误）                            |

<Warning>
  降级是静默的：服务不可用时，模型在本轮执行中会认为智能体不具备对应能力。对关键业务依赖的 MCP 服务，建议在你的应用侧关注会话运行结果是否符合预期。
</Warning>

### 网络放行

会话所在 [执行环境](/docs/hosted-agents/environments) 若配置了 `limited` 网络策略，需要打开 `allow_mcp_servers` 开关（或将服务域名加入 `allowed_hosts`），MCP 连接才能到达对应的服务端点。

## 下一步

<CardGroup cols={3}>
  <Card title="凭据库" icon="key" href="/docs/hosted-agents/vaults">
    创建凭据、走 OAuth Connect 授权流、轮换与归档。
  </Card>

  <Card title="权限策略" icon="shield" href="/docs/hosted-agents/permissions">
    按工具配置权限策略，管控高风险 MCP 工具的执行方式。
  </Card>

  <Card title="插件" icon="puzzle-piece" href="/docs/hosted-agents/plugins">
    通过插件一键接入平台收录的 MCP 服务与技能组合。
  </Card>

  <Card title="工具" icon="wrench" href="/docs/hosted-agents/tools">
    了解内置工具集与 MCP 工具的组合方式。
  </Card>

  <Card title="执行环境" icon="server" href="/docs/hosted-agents/environments">
    配置网络策略，放行 MCP 服务端点。
  </Card>

  <Card title="会话" icon="message" href="/docs/hosted-agents/sessions">
    创建会话并在 resources 中绑定凭据库。
  </Card>
</CardGroup>
