> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 工具

> 查看托管智能体的内置工具清单、使用限制与按需加载方式。

工具是智能体与外部世界交互的手段。托管智能体中的工具分两类：

| 类型                     | 执行方    | 说明                                                    |
| ---------------------- | ------ | ----------------------------------------------------- |
| 内置工具集                  | 平台     | 平台提供的文件、代码、搜索等开箱即用的工具，默认加载 `default_toolset_20260901` |
| MCP 工具集（`mcp_toolset`） | MCP 服务 | 来自你在智能体上声明的 MCP 服务，见 [接入 MCP](/docs/hosted-agents/mcp)     |

内置工具集由平台默认提供。在智能体上声明 MCP 服务后其工具即对模型可用；`mcp_toolset` 声明位于 `tools` 字段，用于调整这些工具的配置。本页介绍内置工具集，以及工具集共用的加载模式配置。

## 内置工具集

未显式声明 `agent_toolset` 时，智能体默认加载 `default_toolset_20260901` 的全部沙箱工具。按类别划分如下：

| 类别 | 工具                                               | 用途                            |
| -- | ------------------------------------------------ | ----------------------------- |
| 文件 | `read_file`                                      | 读取沙箱中的文件，支持文本、图片、视频与二进制       |
| 文件 | `write_file`                                     | 写入或创建文件                       |
| 文件 | `edit_file`                                      | 按字符串匹配对文本文件做局部编辑              |
| 代码 | `shell`                                          | 在云沙箱中执行 Shell 命令              |
| 代码 | `ipython`                                        | 在云沙箱的 IPython 内核中执行 Python 代码 |
| 待办 | `todo_read` / `todo_write`                       | 读写智能体的任务清单，用于长任务的计划与进度跟踪      |
| 搜索 | `web_search`                                     | 联网搜索                          |
| 搜索 | `web_open_url`                                   | 打开指定 URL 并读取网页内容              |
| 搜索 | `search_image_by_text` / `search_image_by_image` | 以文搜图、以图搜图                     |
| 交付 | `save_artifact`                                  | 将指定产物以不可变版本交付，便于后续下载和引用       |

<Note>
  要调整内置工具集的配置（包括按工具覆盖 `enabled`、`permission_policy`、`result_hint`、`load_mode`），需显式声明 `agent_toolset`；未声明时使用默认配置，无法单独调整。关闭沙箱工具时，也需显式声明工具集，并将 `default_config.enabled` 设为 `false`。
</Note>

### 工具集配置

`agent_toolset` 的 `name` 目前使用 `default_toolset_20260901`。未显式声明 `agent_toolset` 时，默认加载该工具集的全部沙箱工具；显式声明后只加载声明的工具集，不会追加默认值。

`default_config` 作用于工具集中的所有工具，`configs` 可按工具名覆盖这些默认值。权限相关字段与 [权限策略](/docs/hosted-agents/permissions) 一致：`enabled` 控制工具是否暴露给模型，`permission_policy` 当前唯一公开取值为 `always_allow`；未设置时工具默认启用并按 `always_allow` 评估。禁用工具请使用 `enabled: false`。

下面的示例关闭整个内置沙箱工具集：

```json theme={null}
{
  "type": "agent_toolset",
  "name": "default_toolset_20260901",
  "default_config": {
    "enabled": false
  }
}
```

MCP 工具集使用 `mcp_toolset`，通过 `mcp_server_name` 指向智能体中声明的 MCP 服务。它同样支持 `default_config` 和 `configs`，其中 `configs` 只能覆盖 MCP 服务实际提供的工具。内置沙箱工具不在这里配置，仍由 `agent_toolset` 的 `default_config` 和 `configs` 管理。

### 限制与安全边界

内置工具对读写规模与执行时长设有上限，超限的调用会返回带原因说明的错误结果，模型通常会据此调整策略（例如分段读取），而不会中断会话：

| 限制项                        | 默认值                  |
| -------------------------- | -------------------- |
| `read_file` 单文件读取上限        | 100 MiB              |
| `read_file` 输出截断           | 最多 1000 行、100,000 字符 |
| `edit_file` 单文件大小上限        | 100 MiB              |
| `shell` 输出截断               | 10,000 字符            |
| `ipython` 输出截断             | 10,000 字符（滚动截断）      |
| `shell` / `ipython` 单次执行超时 | 4 分钟                 |
| `web_search` / 图片搜索超时      | 30 秒                 |
| `web_search` 结果长度          | 10,240 token         |
| 单次工具调用总超时                  | 5 分钟                 |

<Tip>
  文件类工具的 `file_path` 必须使用沙箱绝对路径。`edit_file` 仅支持 UTF-8 文本文件；非 UTF-8 内容会返回“不是文本文件”的错误结果。
</Tip>

文件读写和进程执行都发生在会话使用的云沙箱中，不同沙箱实例之间相互隔离。
实例本地文件可能在实例回收后丢失；挂载到会话的工作区、会话文件和 [记忆库](/docs/hosted-agents/memory) 可以跨实例保存，但采用异步写回，实例退出前尚未完成同步的最新写入仍可能丢失。
需要长期保留的关键产物，应使用 `save_artifact` 工具显式交付为不可变版本。
实例重建后，平台会自动把后续工具调用落到新实例上，客户端不需要额外处理。

### 沙箱网络与凭据

沙箱进程的出站网络由环境的网络策略控制，平台级工具不受该环境网络策略直接控制。环境可以额外配置代理，把指定的出站流量经自有代理转发；代理不等同于凭据注入。

| 网络访问类型         | 说明                              |
| -------------- | ------------------------------- |
| `limited`      | 仅允许访问配置的主机，以及按配置允许的包管理器和 MCP 服务 |
| `unrestricted` | 允许访问公网，但云厂商元数据地址等特殊端点仍会被平台拦截    |

凭据注入只覆盖经平台出口代理的 HTTP/HTTPS 流量（端口 `80`/`443`）；其他端口是否可访问由网络策略决定。凭据库（Vault）中的凭据不会注入所有出站请求，而是根据凭据类型和匹配规则注入或替换：MCP 凭据按 MCP 服务地址匹配；`environment_variable` 凭据按凭据自身的主机白名单和注入位置配置，在匹配的出站请求中替换占位符。

## 按需动态加载

工具集变大时（尤其是插件携带的 MCP 工具），把全部工具 schema 内联进每轮模型请求会显著占用上下文。工具集支持两种 schema 加载模式，通过 `load_mode` 配置：

| 取值          | 说明                                               |
| ----------- | ------------------------------------------------ |
| `eager`     | 工具 schema 全量内联进每轮请求。内置工具集默认使用此模式                 |
| `on_demand` | 模型先只看到工具名，选定后才把 schema 加载进上下文。插件的 MCP 工具集默认使用此模式 |

按需加载的工作方式：

1. 平台向模型播报按需工具的名字清单，但不提供参数 schema；
2. 模型通过 `select_tools` 元工具按名字加载需要的工具，schema 随即进入上下文；
3. 之后模型即可像普通工具一样调用它。

`load_mode` 同样支持两级配置：`default_config.load_mode` 作用于整个工具集，`configs` 中的 `load_mode` 按工具覆盖。不支持的模型会自动回退为全量内联，行为与未配置时一致，你无需为此调整代码。

<Note>
  `select_tools` 的加载动作会以普通的 `agent.tool_use` 事件出现在事件流中，客户端无需特殊处理。模型或提供方不支持按需加载时静默回退，不产生错误。
</Note>

## 下一步

<CardGroup cols={3}>
  <Card title="接入 MCP" icon="plug" href="/docs/hosted-agents/mcp">
    通过 MCP 服务为智能体接入外部工具与数据。
  </Card>

  <Card title="权限策略" icon="shield" href="/docs/hosted-agents/permissions">
    了解 enabled 与 permission\_policy 的当前行为。
  </Card>

  <Card title="事件流" icon="bolt" href="/docs/hosted-agents/event-stream">
    订阅工具调用与结果事件，掌握每一步执行。
  </Card>
</CardGroup>
