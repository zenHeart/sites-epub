> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 执行环境

> 配置执行环境（云沙箱）的预装依赖、网络访问策略和初始化脚本。

执行环境（Environment）是一份可复用的云沙箱配置。每个会话（Session）创建时都必须通过 `environment_id` 绑定一个执行环境。

<Info>
  每个会话都有独立的沙箱实例，同一执行环境下的会话不共享工作区状态。
</Info>

## 创建执行环境

调用 `POST /v1/environments` 创建执行环境。以下示例通过 pip 和 apt 预装依赖、限制出站访问，并在依赖安装完成后创建工作目录：

```bash theme={null}
curl -sS -X POST "$API_BASE_URL/v1/environments" \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "name": "数据分析环境",
  "description": "用于数据分析任务的执行环境",
  "config": {
    "type": "cloud",
    "packages": {
      "pip": ["polars"],
      "apt": ["graphviz"]
    },
    "networking": {
      "type": "limited",
      "allowed_hosts": ["api.example.com"]
    },
    "setup_script": "mkdir -p /workspace/data"
  }
}
JSON
```

响应会返回环境的 `id` 和当前的 `build_status`。保存 `id`，创建会话时需要通过 `environment_id` 引用它。

## 配置执行环境

目前 `config.type` 仅支持 `"cloud"`。`packages`、`networking` 和 `setup_script` 都是可选配置，可以根据任务需要添加或省略。

### 预装依赖

在 `packages` 中按包管理器声明需要预装的依赖。平台会在智能体启动前安装这些依赖，安装结果可以在使用同一执行环境的会话中复用。

| 包管理器                | 字段               | 示例                                          |
| ------------------- | ---------------- | ------------------------------------------- |
| 系统包（apt-get）        | `packages.apt`   | `"graphviz"`                                |
| Rust（cargo install） | `packages.cargo` | `"ripgrep@14.0.0"`                          |
| Go modules          | `packages.go`    | `"golang.org/x/tools/cmd/goimports@latest"` |
| Node.js（npm）        | `packages.npm`   | `"express@4.18.0"`                          |
| Python（pip）         | `packages.pip`   | `"polars"`                                  |

依赖条目使用对应包管理器的原生版本语法。指定版本号时安装对应版本，未指定时安装最新版。每个包管理器最多可以配置 128 条依赖。

### 网络访问

`networking` 控制沙箱进程的出站网络访问，不影响平台层工具自身的网络访问。省略该配置时使用 `unrestricted` 模式。

| 模式             | 说明                                                |
| -------------- | ------------------------------------------------- |
| `unrestricted` | **默认**。允许访问公网，但仍会拦截通用安全黑名单中的地址                    |
| `limited`      | **推荐用于生产环境**。仅允许访问指定主机，也可以按需允许 MCP server 和公共包注册表 |

在 `limited` 模式下：

* `allowed_hosts` 的条目分为两类：域名条目支持精确主机名和 `*.example.com` 形式的通配符（匹配任意层级子域名，不含根域本身），可以带端口（如 `api.example.com:8443`），不带端口时只放行 80 和 443 端口；IP 和 CIDR 网段条目（如 `1.2.3.4`、`10.0.0.0/8`）按 TCP 直连放行且不限制端口，不得带端口。条目不要包含 URL scheme（如 `https://`）或路径，最多配置 128 条；无效条目会在创建或更新执行环境时被 400 拒绝；
* `allow_mcp_servers` 控制是否额外允许访问智能体配置的 MCP server 端点，默认为 `false`；
* `allow_package_managers` 控制是否额外允许访问 PyPI、npm 等公共包注册表，默认为 `false`。

两种模式都可以配置 `proxy`，把指定的出站流量经自有代理转发。`proxy` 的 `hosts` 列出要走代理的主机；在 `limited` 模式下，`hosts` 中的主机可以直接经代理访问，无需再加入 `allowed_hosts`：

```json theme={null}
{
  "config": {
    "type": "cloud",
    "networking": {
      "type": "limited",
      "proxy": {
        "url": "https://proxy.example.com:8443",
        "auth": {
          "type": "basic",
          "vault_id": "vlt_your_vault_id",
          "credential_id": "vcrd_your_credential_id"
        },
        "hosts": ["api.example.com"]
      }
    }
  }
}
```

| `auth.type`   | 凭据库（Vault）中的凭据内容  | 要求                   |
| ------------- | ----------------- | -------------------- |
| `basic`       | `user:password`   | 使用 HTTP Basic 认证     |
| `client_cert` | 包含证书链和私钥的 PEM 证书包 | 使用 TLS 客户端证书（mTLS）认证 |

代理不需要认证时可以省略 `auth` 字段。生产环境中代理 URL 必须使用 HTTPS（不论认证方式）；`client_cert` 在任何环境都强制 HTTPS。

`proxy.ca` 是可选字段，用于提供 PEM 格式的 CA 证书包。代理凭据通过 `vault_id` 和 `credential_id` 引用，凭据明文不会保存在执行环境配置中。引用的凭据必须是凭据库中 active 的 `environment_variable` 类型凭据，其他类型会被 400 拒绝。创建和管理凭据的方法见 [凭据库](/docs/hosted-agents/vaults)。

<Warning>
  生产环境建议显式使用 `limited` 模式，并按照最小权限原则只配置智能体实际需要访问的主机。省略 `networking` 会使用 `unrestricted` 模式。
</Warning>

### 初始化脚本

`setup_script` 适合用于创建目录、生成配置文件等一次性准备工作。

| 约束   | 值                                    |
| ---- | ------------------------------------ |
| 最大长度 | 65536 字符                             |
| 解释器  | `bash -c`，执行前自动添加 `set -eo pipefail` |
| 执行时机 | 构建的最后一步，在所有预装依赖安装完成后执行               |
| 失败行为 | 脚本以非零状态退出时，本次构建失败                    |

## 在会话中使用

创建会话时传入 `environment_id` 即可使用执行环境。绑定后不能更换执行环境，完整请求示例见 [会话](/docs/hosted-agents/sessions)。

执行环境必须对当前调用方可见、未归档，并且至少有一个 `ready` 版本，才能用于创建新会话。

## 等待执行环境构建完成

创建或替换环境配置后，平台会异步构建新版本。要让新建会话使用刚提交的配置，请通过环境 ID 查询构建状态，等待 `build_status` 变为 `ready`：

```bash theme={null}
curl -sS "$API_BASE_URL/v1/environments/$ENVIRONMENT_ID" \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta"
```

`build_status` 表示最新配置版本的构建状态：

| 状态         | 含义            |
| ---------- | ------------- |
| `building` | 正在构建          |
| `ready`    | 构建完成，可以用于新建会话 |
| `failed`   | 构建失败          |

如果最新版本的状态仍为 `building` 或已变为 `failed`，新建会话会使用最近一个 `ready` 的历史版本。只有执行环境不存在任何 `ready` 版本时，创建会话才会失败。

创建会话时会绑定到当时最新的 `ready` 版本，并在整个生命周期中使用该版本。此后更新执行环境不会影响已有会话。

## 更新执行环境

调用 `PATCH /v1/environments/{id}` 可以修改请求体中出现的字段。替换 `config` 时，请提交希望保留的完整 `config`。以下示例保留原有配置，并额外安装 DuckDB：

```bash theme={null}
curl -sS -X PATCH "$API_BASE_URL/v1/environments/$ENVIRONMENT_ID" \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "config": {
    "type": "cloud",
    "packages": {
      "pip": ["polars", "duckdb"],
      "apt": ["graphviz"]
    },
    "networking": {
      "type": "limited",
      "allowed_hosts": ["api.example.com"]
    },
    "setup_script": "mkdir -p /workspace/data"
  }
}
JSON
```

平台会将新配置保存为新版本并异步构建。新版本不会影响已有会话；更新执行环境时也不能修改 `config.type`。

## 管理执行环境

列出当前可见的执行环境：

```bash theme={null}
curl -sS "$API_BASE_URL/v1/environments?page_size=20" \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta"
```

列表默认不返回已归档的环境，需要时可传 `include_archived=true`。

归档不再用于创建新会话的执行环境：

```bash theme={null}
curl -sS -X POST "$API_BASE_URL/v1/environments/$ENVIRONMENT_ID/archive" \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta"
```

归档不可撤销。归档后的环境不能用于创建新会话，但已有会话不受影响。成功归档返回 `204`。

删除不再需要的执行环境。只能删除已归档的执行环境，未归档时删除请求会失败：

```bash theme={null}
curl -sS -X DELETE "$API_BASE_URL/v1/environments/$ENVIRONMENT_ID" \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta"
```

如果仍有未终止的会话引用该环境，删除请求也会失败。成功删除返回 `204`。

## 相关资源

<CardGroup cols={2}>
  <Card title="沙箱规格参考" icon="box" href="/docs/hosted-agents/sandbox-reference">
    查看云沙箱预装的操作系统、运行时与工具，以及文件系统和网络边界。
  </Card>

  <Card title="会话" icon="message" href="/docs/hosted-agents/sessions">
    了解如何创建会话并绑定执行环境。
  </Card>
</CardGroup>
