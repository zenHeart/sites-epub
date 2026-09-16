> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 凭据管理

Vault 是凭据的集合：你把 MCP 服务器的 token、OAuth 凭据或环境变量密钥注册进 Vault，创建会话时通过 **vault\_ids** 引用。密钥只写不读——所有 token、secret 在任何响应中都不会回显，Agent 与沙箱也拿不到原始值。

## 创建 Vault

```bash theme={null}
vault=$(curl -sS "$BASE_URL/v1/vaults" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d '{
    "display_name": "Production credentials"
  }')

VAULT_ID=$(jq -r '.id' <<< "$vault")
```

字段：**display\_name**（必填，1–255 字符）、**metadata**（可选，最多 16 个 string 键值）。

## 添加凭据

**POST /v1/vaults/:vaultId/credentials** 创建凭据。**auth** 是按 type 区分的鉴权对象，支持五种类型：

| 类型                        | 用途                         | 身份键（不可变）         |
| ------------------------- | -------------------------- | ---------------- |
| **static\_bearer**        | MCP 服务器的静态 Bearer token    | mcp\_server\_url |
| **mcp\_oauth**            | MCP 服务器的 OAuth（支持自动刷新）     | mcp\_server\_url |
| **bearer**                | 普通 HTTPS origin 的静态 Bearer | host             |
| **oauth**                 | 普通 HTTPS origin 的 OAuth    | host             |
| **environment\_variable** | 以环境变量形式注入沙箱的密钥             | secret\_name     |

```bash theme={null}
curl -sS "$BASE_URL/v1/vaults/$VAULT_ID/credentials" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d '{
    "display_name": "GitHub MCP token",
    "auth": {
      "type": "static_bearer",
      "mcp_server_url": "https://api.githubcopilot.com/mcp/",
      "token": "ghp_xxxxxxxxxxxx"
    }
  }'
```

```bash theme={null}
curl -sS "$BASE_URL/v1/vaults/$VAULT_ID/credentials" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d '{
    "auth": {
      "type": "mcp_oauth",
      "mcp_server_url": "https://mcp.example.com/",
      "access_token": "at_xxxxxxxx",
      "expires_at": "2026-09-01T00:00:00Z",
      "refresh": {
        "token_endpoint": "https://auth.example.com/oauth/token",
        "client_id": "my-client",
        "refresh_token": "rt_xxxxxxxx",
        "token_endpoint_auth": {
          "type": "client_secret_basic",
          "client_secret": "cs_xxxxxxxx"
        }
      }
    }
  }'
```

OAuth 类型的要点：**access\_token** 必填；配置了 **refresh** 后平台会在过期前用 refresh\_token 自动换新。**token\_endpoint\_auth.type** 支持 none / client\_secret\_basic / client\_secret\_post（none 仅创建时接受）。

```bash theme={null}
curl -sS "$BASE_URL/v1/vaults/$VAULT_ID/credentials" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d '{
    "auth": {
      "type": "environment_variable",
      "secret_name": "EXAMPLE_API_KEY",
      "secret_value": "sk-xxxxxxxx",
      "networking": {
        "type": "limited",
        "allowed_hosts": ["api.example.com"]
      }
    }
  }'
```

**environment\_variable** 类型必须声明 **networking** 策略（unrestricted，或 limited + allowed\_hosts，至多 16 项，支持 \*.example.com 通配），限定携带该密钥的出站请求能到达哪些主机。

## 在创建会话时引用

创建会话时传 **vault\_ids**（最多 20 个、不重复，顺序即匹配优先级）。MCP 凭据按 **mcp\_server\_url** 与 Agent 声明的服务器 URL 匹配；无匹配凭据的服务器以未认证方式连接。详见[连接 MCP](/cn/managed-agents/mcp)。

## 验证 MCP OAuth

不必等到会话里才发现凭据失效。**mcp\_oauth\_validate** 会向目标服务器发起 MCP initialize 探测：

```bash theme={null}
curl -sS -X POST "$BASE_URL/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID/mcp_oauth_validate" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26"
```

响应包含：**status**（valid / invalid / unknown 综合结论）、**mcp\_probe**（initialize 探测的 HTTP 摘要，敏感值已脱敏）、**refresh**（刷新尝试结果：succeeded / failed / connect\_error / no\_refresh\_token）、**has\_refresh\_token**（是否配置了 refresh token，不泄露其值）。

## 轮换凭据

**POST /v1/vaults/:vaultId/credentials/:credentialId** 做部分更新：提供的 secret 被替换，省略的 secret 保留。身份字段（**mcp\_server\_url** / **host** / **secret\_name**，以及 refresh 的 token\_endpoint / client\_id / resource）不可变，更新时必须省略——要换目标就新建一条凭据。

```bash theme={null}
curl -sS "$BASE_URL/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d '{
    "auth": {
      "type": "static_bearer",
      "token": "ghp_new_token_xxxx"
    }
  }'
```

**auth.type** 必须与原凭据相同。OAuth 凭据可分别轮换 access\_token、refresh\_token、client\_secret，或用 **refresh: null** 清除刷新配置。

## 凭据生命周期与其他操作

| 接口                                                              | 说明                                  |
| --------------------------------------------------------------- | ----------------------------------- |
| GET /v1/vaults · GET /v1/vaults/:id                             | 列出 / 获取 Vault（include\_archived 可选） |
| POST /v1/vaults/:id                                             | 更新 display\_name / metadata         |
| POST /v1/vaults/:id/archive · DELETE /v1/vaults/:id             | 归档 / 删除 Vault                       |
| GET /v1/vaults/:id/credentials · GET .../credentials/:cid       | 列出 / 获取凭据（仅非敏感字段）                   |
| POST .../credentials/:cid/archive · DELETE .../credentials/:cid | 归档 / 删除凭据                           |

读取接口只返回非敏感字段：凭据的 token / secret / client\_secret 永不回显；OAuth 凭据回显 expires\_at 与不含秘密值的 refresh 配置。

## 安全边界

* 密钥只写不读：创建和轮换时提交的 token / secret 不会出现在任何 API 响应里。
* Agent 与沙箱拿不到凭据原文；MCP 与 HTTPS 出站由平台侧注入，不进入提示词或进程环境。
* **environment\_variable** 类型会按你声明的 **networking** 限制出站主机，见上文。
* 会话创建前可用 **mcp\_oauth\_validate** 探测 MCP OAuth 是否仍有效，不必等到会话里才发现失败。

## 下一步

<CardGroup cols={2}>
  <Card title="连接 MCP" href="/cn/managed-agents/mcp">
    凭据与 MCP 服务器的匹配规则
  </Card>

  <Card title="创建会话" href="/cn/managed-agents/create-session">
    vault\_ids 的使用
  </Card>

  <Card title="本页对应 OpenAPI" href="/cn/managed-agents/api-reference#vaults">
    Vault：凭据创建、轮换、验证 MCP OAuth
  </Card>
</CardGroup>
