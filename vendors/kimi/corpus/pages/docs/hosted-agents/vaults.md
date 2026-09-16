> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 凭据库

> 保存第三方服务凭据，在创建会话时绑定凭据库，并管理凭据的授权、轮换和归档。

凭据库（Vault）用于保存第三方服务的访问凭据。创建会话时绑定凭据库，平台会在会话运行期间按凭据类型和匹配规则提供凭据。

凭据写入后，API 响应不会返回凭据值。

本页分为两条操作路径：

* **首次接入**：选择凭据类型、创建凭据库、添加凭据，并在创建会话时绑定凭据库。
* **日常维护**：查看凭据、完成 OAuth 授权、轮换凭据值，以及归档或删除资源。

## 首次接入

### 选择凭据类型

根据第三方服务的认证方式选择 `type`：

| 使用场景                 | 凭据类型                   |
| -------------------- | ---------------------- |
| MCP 服务使用 OAuth 2.0   | `mcp_oauth`            |
| MCP 服务使用固定 Bearer 令牌 | `static_bearer`        |
| 程序通过环境变量获取凭据         | `environment_variable` |

`mcp_oauth` 和 `static_bearer` 使用 `mcp_server_url` 匹配 MCP 服务。`environment_variable` 使用 `secret_name` 匹配环境变量名。同一凭据库的活跃凭据中，用于匹配的字段不能重复。每个凭据库最多包含 20 条活跃凭据。

凭据的 `type` 和身份字段创建后不能修改。如需更换认证类型或匹配字段，请先归档旧凭据，再创建新凭据。

对于 `environment_variable`，沙箱中的环境变量是占位符，不是真实密钥。这种类型的凭据适合将凭据放入出站请求，不适合在本地校验真实密钥，或使用真实密钥计算请求签名。

### 创建凭据库

下面的请求创建一个凭据库，用于保存同一用户或同一业务场景的访问凭据：

```bash theme={null}
VAULT_ID=$(curl --silent --show-error --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "display_name": "alice",
    "metadata": {"external_user_id": "usr_abc123"}
  }' | jq -r '.id')
```

成功响应中的 `id` 是凭据库 ID。保存它作为 `VAULT_ID`，后续添加凭据和绑定会话时需要使用。如果当前环境没有 `jq`，请从响应 JSON 中取出 `id` 后设置 `VAULT_ID`。

### 添加凭据

将访问凭据写入刚创建的凭据库。下面的示例添加一个固定 Bearer 凭据：

```bash theme={null}
CREDENTIAL_ID=$(curl --silent --show-error --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/$VAULT_ID/credentials" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "display_name": "MCP access",
    "auth": {
      "type": "static_bearer",
      "mcp_server_url": "https://example.invalid/mcp",
      "token": "your-token"
    }
  }' | jq -r '.id')
```

将 `your-token` 替换为真实凭据值。保存响应中的 `id` 作为 `CREDENTIAL_ID`，后续查看、更新或归档这条凭据时需要使用它。

成功响应包含凭据的 `id` 和非敏感配置，但不会返回 `token`、`access_token`、`refresh_token`、`client_secret` 或 `secret_value` 对应的密钥值。

#### 添加 OAuth 凭据

MCP 服务使用 OAuth 2.0 时，将 `type` 设为 `mcp_oauth`，并提供 `mcp_server_url` 和 `access_token`。需要自动刷新时，再提供 `refresh`，其中 `token_endpoint`、`client_id` 和 `token_endpoint_auth_type` 必须一起正确配置。

#### 添加环境变量凭据

客户端通过环境变量发送凭据时，使用 `secret_name` 和 `secret_value`。可以用 `networking` 限制凭据可以替换到的目标主机，并用 `injection_location` 限制替换位置。省略 `networking` 时默认为 `limited` 加空白名单，凭据不会被替换到任何主机；必须显式配置 `allowed_hosts` 或将 `type` 设为 `unrestricted` 才会发生替换。

```bash theme={null}
curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/$VAULT_ID/credentials" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "display_name": "Example API key",
    "auth": {
      "type": "environment_variable",
      "secret_name": "EXAMPLE_API_KEY",
      "secret_value": "your-token",
      "networking": {"type": "limited", "allowed_hosts": ["api.example.com"]},
      "injection_location": {"header": true}
    }
  }'
```

创建时完全省略 `injection_location`，请求头和请求体都启用替换。提供该对象但省略其中一个字段时，省略的字段为 `false`，例如只提供 `{"header": true}` 时不会替换请求体。至少要启用一个位置。

`networking.allowed_hosts` 只控制凭据可以替换到哪些目标主机，不能代替执行环境的网络策略。只有目标主机和执行环境都允许请求时，凭据替换才可用。

#### 批量添加凭据

需要一次写入多条凭据时，使用批量创建接口，在 `items` 中传入 1 到 20 条凭据，每条的字段与单条创建相同：

```bash theme={null}
curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/$VAULT_ID/credentials/batch" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "items": [
      {
        "display_name": "MCP access",
        "auth": {
          "type": "static_bearer",
          "mcp_server_url": "https://example.invalid/mcp",
          "token": "your-token"
        }
      },
      {
        "display_name": "MCP access 2",
        "auth": {
          "type": "static_bearer",
          "mcp_server_url": "https://example.invalid/mcp-2",
          "token": "your-token-2"
        }
      }
    ]
  }'
```

批量创建是原子操作：任何一条校验失败，所有凭据都不会创建。`items` 中用于匹配的字段（如 `mcp_server_url`）不能重复，否则返回 400；这批凭据同样计入凭据库 20 条活跃凭据的上限。成功响应的 `items` 按请求顺序返回创建的凭据，同样不返回凭据值。

### 完成 OAuth 授权

也可以通过浏览器授权添加 `mcp_oauth` 凭据，无需手动填写 `access_token`；授权成功会自动创建凭据。同一 MCP 服务已有活跃凭据时发起授权会返回 409，需先归档旧凭据。创建授权会话后，将返回的 `authorize_url` 交给用户打开。

```bash theme={null}
OAUTH_SESSION_ID=$(curl --silent --show-error --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/$VAULT_ID/oauth-sessions" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "mcp_server_url": "https://example.invalid/mcp",
    "display_name": "MCP access"
  }' | jq -r '.oauth_session_id')
```

请从响应中取出 `authorize_url`，交给用户在浏览器中打开，并保存响应中的 `oauth_session_id` 作为 `OAUTH_SESSION_ID`。不提供 `client` 时，平台会自动注册 OAuth 客户端；使用已有客户端时，可以提供 `client_id` 以及授权服务器要求的其他 `client` 字段。

用户完成浏览器授权后，轮询授权会话状态：

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/$VAULT_ID/oauth-sessions/$OAUTH_SESSION_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

状态为 `pending` 时继续轮询，状态为 `authorized` 时响应包含新凭据的 `credential_id`，请将它保存为 `CREDENTIAL_ID`。状态为 `failed` 时响应包含 `error`，应根据原因重新发起授权。平台没有立即完成授权的接口，必须通过轮询获取结果。

### 预检凭据覆盖情况

凭据预检接口用于确认一组 MCP 服务 URL 在凭据库中的活跃凭据覆盖情况。例如，在发起 OAuth 授权前预检，可以提前发现同一服务已有活跃凭据，避免授权请求返回 409：

```bash theme={null}
curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/credentials/check" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "mcp_server_urls": ["https://example.invalid/mcp"],
    "vault_ids": ["替换为要检查的凭据库 ID"]
  }'
```

`mcp_server_urls` 传入 1 到 50 个不重复的 MCP 服务 URL；`vault_ids` 可选，最多 16 个凭据库 ID，省略时搜索调用方可见的所有凭据库。响应中的 `coverage` 按请求顺序给出每个 URL 的覆盖结果：`mcp_server_url` 是请求中的原始 URL，`matching_vault_ids` 是含有该 URL 活跃凭据的凭据库 ID 列表，空数组表示没有覆盖。匹配前每个 URL 会先规范化，无法规范化的 URL 不匹配任何凭据。只有 `mcp_oauth` 和 `static_bearer` 凭据计入覆盖，`environment_variable` 凭据不会出现在结果中。

### 创建会话时绑定凭据库

凭据库只能在创建会话时绑定，不能通过会话资源接口追加。`agent_id` 和 `environment_id` 应替换为已经创建并且有权访问的智能体，以及已构建就绪的执行环境的 ID。

```bash theme={null}
curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "agent_id": "替换为已有智能体 ID",
    "environment_id": "替换为已有环境 ID",
    "resources": [{"type": "vault", "vault_id": "<上一步得到的 VAULT_ID>"}],
    "title": "alice 的每日摘要"
  }'
```

创建成功后，会话的 `resources` 中包含 `type` 为 `vault` 的绑定。一个会话最多绑定 16 个凭据库。如果多个凭据库有同一个 MCP 服务的活跃凭据，平台按 `resources` 中凭据库的顺序使用第一个匹配项。

## 日常维护

### 查看凭据库和凭据

查看凭据库及其中的凭据，确认当前名称、匹配字段和归档状态。凭据列表默认不包含已归档凭据，传入 `include_archived=true` 时，列表会同时包含已归档凭据。列表结果使用 `page_size` 和不透明的 `page_token` 分页：将响应中的 `next_page_token` 作为下一页请求的 `page_token`；该字段省略时表示没有更多结果。

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/$VAULT_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/$VAULT_ID/credentials" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

查看单个凭据：

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

成功响应返回资源记录和非敏感配置，不返回凭据值。

### 更新凭据库

更新凭据库时只能修改 `display_name` 或 `metadata`：

```bash theme={null}
curl --request PATCH "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/$VAULT_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{"display_name": "Alice credentials"}'
```

### 轮换凭据值

轮换凭据值时，只需提交需要更新的字段。凭据的类型和身份匹配字段不能修改，例如 `type`、`mcp_server_url`、`secret_name`、`token_endpoint` 和 `client_id`。请求中的 `type` 必须与现有凭据一致。

下面的请求轮换一个静态 Bearer 凭据的令牌。`mcp_server_url` 是该凭据已有的值，不能改成其他地址：

```bash theme={null}
curl --request PATCH "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "auth": {
      "type": "static_bearer",
      "mcp_server_url": "https://example.invalid/mcp",
      "token": "your-new-token"
    }
  }'
```

成功响应返回更新后的非敏感配置，但不会返回新的凭据值。

### 归档或删除

归档和删除是两种不同的操作：

* **归档**：保留资源记录，清除其中的密钥值。归档后的凭据或凭据库不能用于新会话。
* **删除**：永久删除资源记录。

根据要处理的资源选择对应接口。删除仅适用于已归档的凭据库或凭据；要永久删除，需先归档再删除。

| 资源  | 归档接口                                                             | 删除接口                                                       |
| --- | ---------------------------------------------------------------- | ---------------------------------------------------------- |
| 凭据  | `POST /v1/vaults/{vault_id}/credentials/{credential_id}/archive` | `DELETE /v1/vaults/{vault_id}/credentials/{credential_id}` |
| 凭据库 | `POST /v1/vaults/{vault_id}/archive`                             | `DELETE /v1/vaults/{vault_id}`                             |

归档凭据库时，其中的活跃凭据也会被归档并清除密钥值。删除凭据库时，其中的凭据记录也会一并删除，不需要再单独删除。

归档一条凭据，保留凭据记录：

```bash theme={null}
curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID/archive" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

永久删除一个凭据库及其中的凭据记录。先归档凭据库：

```bash theme={null}
curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/$VAULT_ID/archive" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

归档完成后再删除：

```bash theme={null}
curl --request DELETE "${API_BASE_URL:-https://api.moonshot.cn}/v1/vaults/$VAULT_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

## 安全边界

凭据值只接受写入，不会出现在创建、查询、列表或更新响应中。不要在客户端日志、提示词或其他会进入模型上下文的内容中记录凭据值。

MCP 凭据按 `mcp_server_url` 匹配，环境变量凭据按 `secret_name` 匹配。对于 `environment_variable`，只有目标主机和执行环境的网络策略都允许请求时，平台才会替换占位符。
