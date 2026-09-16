> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 记忆

> 创建可跨会话使用的记忆库，管理其中的文件，并按版本检查和恢复内容。

## 记忆库是什么

记忆库（Memory Store）是项目级的持久化文件集合。创建会话时挂载记忆库后，智能体就可以在会话中读取或更新其中的文件。

记忆库、记忆文件和文件版本分别表示不同的对象：

| 对象                   | 说明                     |
| -------------------- | ---------------------- |
| 记忆库（Memory Store）    | 保存记忆文件的文件集合            |
| 记忆文件（Memory）         | 记忆库中的一份文件              |
| 文件版本（Memory Version） | 该文件一次创建、修改、重命名或删除的历史记录 |

记忆库不提供自动向量检索。会话启动时，平台会向智能体提供根目录 `README.md` 和 `index.md` 的有限内容，每个文件最多 16 KiB。其他文件需要智能体通过文件工具按需读取。

<Warning>
  不要在记忆库中保存 API Key、访问令牌、密码或其他敏感凭据。需要保存凭据时，请使用 [凭据库](/docs/hosted-agents/vaults)。
</Warning>

## 创建并挂载记忆库

完成一次最短使用流程需要三步：创建记忆库、创建记忆文件，然后在创建会话时挂载记忆库。

### 创建记忆库

下面的请求创建一个名为 `project-conventions` 的记忆库：

```bash theme={null}
curl --request POST "https://api.moonshot.cn/v1/memory-stores" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "name": "project-conventions",
    "description": "项目约定与决策记录"
  }'
```

保存响应中的 `id`，作为后续请求的 `MEMORY_STORE_ID`。`name` 必须在项目内唯一，长度为 1 到 64 个字符，并以 Unicode 字母或数字开头；后续字符可以包含 `_` 和 `-`。

### 创建记忆文件

使用记忆库 ID 和文件路径创建文件。`content` 是文件正文的 Base64 编码，解码后的正文最多 20 MiB。示例中，`content` 的值是文件正文「项目约定」的 Base64 编码：

```bash theme={null}
curl --request POST "https://api.moonshot.cn/v1/memory-stores/$MEMORY_STORE_ID/memories" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "path": "project/conventions.md",
    "content": "6aG555uu57qm5a6aCg=="
  }'
```

保存响应中的文件 `id`，作为后续读取、更新和查看版本时使用的 `MEMORY_ID`。省略 `content` 或传入空字符串可以创建空文件，但同一路径不能重复创建。

`path` 必须是规范化的相对路径，最长 900 字节（UTF-8 编码），并使用 `/` 分隔目录。不能使用绝对路径，也不能包含空路径段、`.`、`..`、反斜杠、控制字符或百分号编码。

### 在会话中挂载记忆库

记忆库只能在创建会话时绑定。下面的请求使用前一步得到的 `MEMORY_STORE_ID`，并以读写方式挂载记忆库：

```bash theme={null}
curl --request POST "https://api.moonshot.cn/v1/sessions" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "agent_id": "agent_your_agent_id",
    "environment_id": "env_your_environment_id",
    "resources": [
      {
        "type": "memory_store",
        "memory_store_id": "<上一步得到的 MEMORY_STORE_ID>",
        "access": "read_write",
        "instructions": "参考项目约定，并记录新的重要结论。"
      }
    ]
  }'
```

将 `agent_id` 和 `environment_id` 替换为已有资源的 ID，将 `MEMORY_STORE_ID` 替换为创建记忆库响应中的 `id`。

`access` 可以是 `read_only` 或 `read_write`：

* `read_only` 只允许读取记忆库；
* `read_write` 允许读取和写入记忆库。

记忆库会挂载到会话中的 `/mnt/agents/memories/<store-name>/`。绑定关系、访问模式和 `instructions` 在会话创建后不能修改。

## 管理记忆文件

### 读取文件

使用记忆库 ID 和文件 ID 读取文件。API 响应中的 `content` 是 Base64 编码，保存响应中的 `content_sha256`，更新文件时可以将它原样传回做并发校验：

```bash theme={null}
curl --request GET "https://api.moonshot.cn/v1/memory-stores/$MEMORY_STORE_ID/memories/$MEMORY_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

### 更新文件

把新正文编码为 Base64 后更新文件。请求中的 `content_sha256` 应使用读取当前文件时得到的值，平台会用它检查文件在读取后是否被修改：

```bash theme={null}
curl --request PATCH "https://api.moonshot.cn/v1/memory-stores/$MEMORY_STORE_ID/memories/$MEMORY_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "content": "5pu05paw5ZCO55qE6aG555uu57qm5a6aCg==",
    "content_sha256": "<读取当前文件响应中的 content_sha256>"
  }'
```

如果文件已被其他来源修改，使用旧 `content_sha256` 更新会返回 `409`，平台不会覆盖新内容。通过会话挂载路径和文件工具写入时，不经过 API 的 `content_sha256` 并发校验，并发写入可能互相覆盖。每次成功的文件变更都会生成一个新版本。

### 删除文件

删除只移除当前文件，历史版本仍然保留：

```bash theme={null}
curl --request DELETE "https://api.moonshot.cn/v1/memory-stores/$MEMORY_STORE_ID/memories/$MEMORY_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

删除后，原 `memory_id` 的版本列表和历史版本内容仍可查询，但不能再对这个 `memory_id` 使用 `PATCH`。

## 查看版本和恢复

### 查看文件版本

创建、修改、重命名和删除都会生成版本，版本的 `operation` 字段分别对应 `created`、`modified`、`renamed` 和 `deleted`。先查询文件的版本列表，再选择要读取的版本：

```bash theme={null}
curl --request GET "https://api.moonshot.cn/v1/memory-stores/$MEMORY_STORE_ID/memories/$MEMORY_ID/versions?order=desc" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

选择包含正文的版本，读取该版本的 `content`。`operation` 为 `deleted` 的版本不返回 `content`，不能用于恢复：

```bash theme={null}
curl --request GET "https://api.moonshot.cn/v1/memory-stores/$MEMORY_STORE_ID/memories/$MEMORY_ID/versions/<version_id>" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

版本还记录写入来源：`source` 为 `api` 表示通过 API 写入，为 `session` 表示由会话写入；`source_id` 是产生该版本的会话 ID。要找出某次会话产生的变更，筛选 `source` 为 `session` 且 `source_id` 等于该会话 ID 的版本。

历史版本的 `content` 也是 Base64 编码。恢复文件时，将历史版本的 `content` 作为新的文件正文写回，并同时传入当前文件的 `content_sha256`：

```bash theme={null}
curl --request PATCH "https://api.moonshot.cn/v1/memory-stores/$MEMORY_STORE_ID/memories/$MEMORY_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "content": "<历史版本响应中的 content>",
    "content_sha256": "<当前文件响应中的 content_sha256>"
  }'
```

恢复会为该文件生成一个新版本。恢复多个文件时，需要逐个文件读取当前 `content_sha256` 并写回历史正文，不是整个记忆库的原子操作。

### 恢复已删除的文件

删除版本不包含正文。要恢复已删除的文件，请读取删除前某个包含正文的版本，再使用该版本的 `content` 和原路径重新创建文件：

```bash theme={null}
curl --request POST "https://api.moonshot.cn/v1/memory-stores/$MEMORY_STORE_ID/memories" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "path": "project/conventions.md",
    "content": "<删除前历史版本响应中的 content>"
  }'
```

重新创建会生成新的 `memory_id`，版本记录从新的 `created` 版本重新开始；删除前的版本历史仍保留在原 `memory_id` 下，可继续查询。恢复前应确认历史版本中的 `content` 未被清除。

## 相关资源

<CardGroup cols={2}>
  <Card title="梦境" icon="cloud-moon" href="/docs/hosted-agents/dreams">按策略整理记忆库，并通过版本记录检查和恢复变更。</Card>
  <Card title="会话" icon="message" href="/docs/hosted-agents/sessions">了解会话创建以及资源绑定方式。</Card>
  <Card title="沙箱规格" icon="box" href="/docs/hosted-agents/sandbox-reference">查看记忆库挂载路径和沙箱边界。</Card>
  <Card title="凭据库" icon="key" href="/docs/hosted-agents/vaults">管理会话使用的凭据。</Card>
</CardGroup>
