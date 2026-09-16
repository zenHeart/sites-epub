> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 梦境

> 为记忆库配置自动整理条件，查看运行记录，并按文件版本核对和恢复变更。

梦境（Dreaming）会在指定条件满足时创建一个普通会话，由配置的智能体读取并修改原记忆库中的文件。
梦境策略由平台管理的触发器执行，结果直接写回原记忆库，不会创建新的记忆库。

<Warning>
  梦境失败时不会自动回滚已经写入的内容。
  梦境可能修改多个文件，恢复时需要逐个文件处理，不能一次性恢复整个记忆库。
</Warning>

## 配置自动梦境

使用已有的记忆库 ID，选中需要更新的记忆库。
配置执行梦境的智能体时，`agent_id` 可以省略，省略后使用平台默认的 Dream Agent。

每次更新都要同时传入完整的 `activity` 和 `schedule` 对象，代表执行梦境的活动条件或定时条件。
两个条件相互独立，任一条件满足都会触发梦境。
两个条件启用任意一个，就必须提供执行环境 ID。

下面的示例请求同时启用活动条件和定时条件。
`MEMORY_STORE_ID`、`ENVIRONMENT_ID` 和可选的 `agent_id` 应替换为已有资源的 ID。

```bash theme={null}
curl --request PATCH "${API_BASE_URL:-https://api.moonshot.cn}/v1/memory-stores/$MEMORY_STORE_ID/dream-policy" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "activity": {
      "enabled": true,
      "min_changed_sessions": 3
    },
    "schedule": {
      "enabled": true,
      "local_time": "03:00",
      "timezone": "Asia/Shanghai"
    },
    "environment_id": "env_your_environment_id"
  }'
```

活动条件会统计绑定该记忆库的会话中，自上次触发梦境（或启用该条件）以来发生变化的会话数量。
会话数量达到 `min_changed_sessions` 后，平台会触发一次梦境。
梦境创建的普通会话不会再次触发该条件。

定时条件表示，梦境每天在指定的本地时间触发一次。
触发时，即使没有新的会话，平台也会创建一次梦境运行，让智能体检查是否需要更新记忆库。
`local_time` 使用 `HH:mm` 格式，`timezone` 使用 IANA 时区名称。

如果只需要其中一个条件，需要将另一个条件的 `enabled` 设置为 `false`，但仍然要传入完整的条件对象。

## 关闭自动梦境

将两个条件的 `enabled` 都设置为 `false`，即可关闭自动梦境。
关闭时不需要提供 `environment_id`。
先将当前策略响应中的 `agent_id` 保存为 `DREAM_AGENT_ID`，这样可以保留当前使用的 Dream Agent。
如果当前使用的是平台默认的 Dream Agent，可以将 `DREAM_AGENT_ID` 设置为 `agent_dream`。

```bash theme={null}
curl --request PATCH "${API_BASE_URL:-https://api.moonshot.cn}/v1/memory-stores/$MEMORY_STORE_ID/dream-policy" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "agent_id": "'"$DREAM_AGENT_ID"'",
    "activity": {
      "enabled": false
    },
    "schedule": {
      "enabled": false
    }
  }'
```

省略 `agent_id` 会选择平台默认的 Dream Agent。

## 查看当前策略

更新后查询 Dream Policy，并保存响应中的 `trigger_id`。

`trigger_id` 标识 Dream Policy 管理的触发器。
触发器（Trigger）是一条按照条件启动智能体会话的规则。
活动条件或定时条件满足时，平台会通过这条触发器创建一次梦境会话。

查询代码：

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/memory-stores/$MEMORY_STORE_ID/dream-policy" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

响应示例：

```json theme={null}
{
  "memory_store_id": "mstr_example_store",
  "agent_id": "agent_dream",
  "activity": {
    "enabled": true,
    "min_changed_sessions": 3
  },
  "schedule": {
    "enabled": false
  },
  "trigger_id": "trig_example_trigger",
  "environment_id": "env_example_environment"
}
```

保存响应中的 `trigger_id`，将它设置为 `TRIGGER_ID`。
后续手动运行梦境和查询运行记录时需要使用这个值。

触发器由 Dream Policy 接口统一管理，不能通过触发器接口更新、暂停、恢复或归档。
需要调整触发条件或关闭自动梦境时，继续使用 Dream Policy 接口。
如果要立即运行一次梦境，可以调用这个触发器的运行接口。

## 手动运行梦境

Dream Policy 没有单独的立即运行接口。
调用触发器的运行接口即可手动触发一次梦境。

```bash theme={null}
curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/triggers/$TRIGGER_ID/run" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{}'
```

响应示例：

```json theme={null}
{
  "id": "trun_example_run",
  "trigger_id": "trig_example_trigger",
  "status": "completed"
}
```

运行接口会同步执行本次触发，响应直接返回终态的运行记录（`completed`、`failed` 或 `skipped`）。
响应中的 `id` 是本次 `TriggerRun` 的 ID。
将它保存为 `TRIGGER_RUN_ID`，用于查询本次运行状态。

## 查看触发记录

`TriggerRun` 是一次运行记录，用于记录梦境的执行状态和关联会话。

使用上一步得到的 `TRIGGER_RUN_ID` 查询本次运行的最新状态。

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/triggers/$TRIGGER_ID/runs/$TRIGGER_RUN_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

响应示例：

```json theme={null}
{
  "id": "trun_example_run",
  "trigger_id": "trig_example_trigger",
  "status": "completed",
  "session_id": "sesn_example_session"
}
```

运行状态包括 `running`、`completed`、`failed` 和 `skipped`。
其中，`running` 表示会话正在启动，`failed` 表示运行失败（详见 `error`），`skipped` 表示触发时触发器不在活跃状态。
`completed` 只表示平台已经创建会话，并且接受了会话的初始事件，不表示梦境已经完成记忆整理。
需要继续查看 `session_id` 对应的会话事件和记忆库版本，确认梦境的实际执行结果。

如果运行记录还没有 `session_id`，说明本次运行还没有创建或关联会话，此时不能查询对应会话。

如果需要查看历史运行记录，可以列出该触发器的所有 TriggerRun：

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/triggers/$TRIGGER_ID/runs?page_size=20" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

## 查看关联会话

获取运行记录中的 `session_id` 后，使用该值查询本次运行创建的会话。

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

`SESSION_ID` 应替换为 TriggerRun 响应中的 `session_id`。
查看会话事件可以了解梦境的执行过程：

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/events?page_size=20" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

如果需要持续接收执行过程中的状态和输出，请参阅 [事件流](/docs/hosted-agents/event-stream)。

## 检查记忆库的修改

梦境可能修改记忆库中的多个文件。
先列出文件，选择需要检查的文件 ID：

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/memory-stores/$MEMORY_STORE_ID/memories" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

将上一步文件列表中目标文件的 `id` 保存为 `MEMORY_ID`，查询该文件的版本列表。版本按时间从新到旧排列：

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/memory-stores/$MEMORY_STORE_ID/memories/$MEMORY_ID/versions?order=desc" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

梦境创建的普通会话使用 `source: "session"`，`source_id` 是本次梦境会话的 ID。
`source` 为 `api` 表示通过 API 直接写入；通过 API 恢复文件产生的版本也是 `api`。
先将 `TriggerRun` 响应中的 `session_id` 保存后，在版本列表中筛选 `source` 为 `session` 且 `source_id` 等于该会话 ID 的版本，就能定位本次梦境产生的所有变更。
再结合 `operation`、`path` 和 `created_at`，判断本次运行对该文件执行了创建、修改、重命名还是删除（重命名通过比较相邻版本的 `path` 判断）。

需要读取正文时，选择 `operation` 不是 `"deleted"` 且没有 `redacted_at` 的版本，将它的 `id` 保存为 `VERSION_ID`：

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/memory-stores/$MEMORY_STORE_ID/memories/$MEMORY_ID/versions/$VERSION_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

返回的 `content` 是 Base64 编码。
`operation` 为 `"deleted"` 的版本只是删除标记，没有正文；已经 `redacted_at` 的版本正文已被清除。恢复被删除的文件时，应使用该文件删除前最近一个可读版本，而不是删除标记本身。
梦境失败时可能已经留下部分文件变更，因此需要逐个检查受影响的文件。

## 恢复文件

恢复文件就是把某个历史版本的正文写回当前文件。
上一节已经取得历史版本响应中的 `content`，将它保存为 `HISTORICAL_CONTENT`。

恢复前，重新读取当前文件，取得最新的 `content_sha256`：

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/memory-stores/$MEMORY_STORE_ID/memories/$MEMORY_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

将当前文件响应中的 `content_sha256` 保存为 `CONTENT_SHA256`。
这里只需要保存 `content_sha256`，当前文件响应中的 `content` 不用于本次恢复。
`CONTENT_SHA256` 必须直接使用接口返回的值，不能自行填写或修改。

然后，将历史版本的正文写回当前文件：

```bash theme={null}
curl --request PATCH "${API_BASE_URL:-https://api.moonshot.cn}/v1/memory-stores/$MEMORY_STORE_ID/memories/$MEMORY_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "content": "'"$HISTORICAL_CONTENT"'",
    "content_sha256": "'"$CONTENT_SHA256"'"
  }'
```

更新成功后，平台会返回更新后的文件；内容发生变化时，会为这次恢复生成一个新的文件版本，写入与当前内容相同的内容则不生成新版本。
后续再次更新该文件时，应使用响应中的新 `content_sha256`。

如果当前文件在读取后已经被其他操作修改，旧的 `content_sha256` 与当前值不匹配，更新会返回 `409`，平台不会覆盖新的内容。
此时应重新读取当前文件，取得新的 `content_sha256`，再决定是否继续恢复。

恢复多个文件时，需要为每个文件分别读取最新的 `content_sha256` 并执行更新。
恢复多个文件时，平台会分别更新每个文件。如果某个文件更新失败，之前已经恢复成功的文件不会自动撤销，因此需要逐个确认恢复结果。

## 相关资源

<CardGroup cols={3}>
  <Card title="记忆库" icon="database" href="/docs/hosted-agents/memory">
    创建记忆库、绑定会话并管理记忆版本。
  </Card>

  <Card title="会话" icon="message" href="/docs/hosted-agents/sessions">
    了解会话的创建方式和记忆库绑定配置。
  </Card>

  <Card title="智能体" icon="robot" href="/docs/hosted-agents/agents">
    配置执行梦境的智能体。
  </Card>
</CardGroup>
