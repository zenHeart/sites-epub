> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 定时运行智能体

> 使用 cron 定时或手动运行智能体，查看运行记录并管理触发器生命周期。

定时运行通过触发器（Trigger）让智能体按计划自动运行，适合定时巡检、周期报告、自动维护等场景。默认的 `new_session` 模式每次触发都会创建一个新会话；`reuse_session` 模式会复用平台为触发器托管的会话（首次触发时自动创建并绑定会话ID，不需要指定会话）。触发器也支持随时手动运行一次。

平台托管的触发器（如梦境的 Dream Policy）不能通过本页的接口修改，其管理方法见 [梦境](/docs/hosted-agents/dreams)。本页介绍你自己创建的触发器。

## 创建定时触发器

调用 `POST /v1/triggers` 创建触发器。以「每个工作日早上 9 点生成一份金融市场晨报」为例：

```bash theme={null}
curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/triggers" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "name": "工作日晨报",
    "agent_id": "agent_your_agent_id",
    "environment_id": "env_your_environment_id",
    "session_mode": "reuse_session",
    "policy": {
      "type": "cron",
      "expression": "0 9 * * 1-5",
      "timezone": "Asia/Shanghai"
    }
  }'
```

必填字段是 `name`、`agent_id`、`environment_id` 和 `policy`。`policy` 的 `expression` 是 cron 表达式，由空格分隔的五个字段组成，依次是分、时、日、月、星期，最小调度单位为 1 分钟——上面示例的 `0 9 * * 1-5` 即「每个工作日 9:00」。未来 5 年内没有命中时间的表达式会在创建或更新时被拒绝。`timezone` 是 IANA 时区名，计划时间按该时区计算，实际触发会比计划时间稍晚，延迟不超过触发间隔的 10%（上限 15 分钟）。

`agent_id` 来自创建智能体响应中的 `id`。`environment_id` 来自创建执行环境响应中的 `id`，指定运行会话使用的执行环境，省略或传空值会被拒绝（400 `invalid_parameter_error`）。省略 `agent_version` 时，每次触发使用该智能体当时的最新版本。创建时会校验智能体、执行环境、凭据库和记忆库引用；引用不存在、跨项目或已归档的会被拒绝。

创建成功返回 201，保存响应中的 `id` 作为 `TRIGGER_ID`（`trig_` 前缀）。触发器创建后即为 `active` 状态，会按计划自动触发。

可选字段说明：

* `session_mode`：`new_session`（默认）或 `reuse_session`，上面的创建示例显式设为了 `reuse_session`。
* `initial_events`：每次触发时投递给会话的初始事件（如任务指令），最多 16 条。平台还会附加一条 `<trigger_fire_context>` 用户消息，包含本次运行的触发器 ID 和运行 ID，计划运行时还包含计划时间。
* `resources`：绑定到运行会话的文件、凭据库或记忆库，最多 16 条。
* `notification`：运行结果通知的 Webhook 配置，见下文「接收运行通知」。

每个项目最多创建 200 个非归档触发器。

## 查看触发器和运行时间

调用 `GET /v1/triggers` 列出触发器，最新的在前。默认不返回已归档的触发器，可用 `status` 按生命周期状态筛选，或用 `policy_type` 按策略类型筛选。列表默认返回 50 条；如果响应包含 `next_page_token`，将其作为下一次请求的 `page_token`，直到该字段为空。

调用 `GET /v1/triggers/{id}` 查看单个触发器：

```bash theme={null}
curl "${API_BASE_URL:-https://api.moonshot.cn}/v1/triggers/$TRIGGER_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

触发器处于 `active` 状态且使用 cron 策略时，响应中包含 `upcoming_runs_at`：按 UTC 给出的未来最多 5 次计划时间。这些时间不包含实际触发时加入的抖动，只是近似值，可用于确认计划是否按预期设置。

## 手动运行一次

调试或临时需要时，调用 `POST /v1/triggers/{id}/run` 立即运行一次，不必等到计划时间。已暂停的触发器也可以手动运行：

```bash theme={null}
curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/triggers/$TRIGGER_ID/run" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "payload": "现在就生成本期晨报"
  }'
```

`payload` 是可选的文本，不传时只执行触发器原有配置，会包裹在 `<untrusted_trigger_payload>` 标签中作为用户消息投递给本次运行的会话。

手动运行是同步的：请求等待运行结束后，返回 201 和终态运行记录（`completed`、`failed` 或 `skipped`）。同一触发器已有另一个手动运行进行时，请求会返回 400 `failed_precondition_error`。在 `reuse_session` 模式下，如果计划运行或其他运行占用托管会话，本次运行会记录为 `skipped`，并在 `error.type` 中标记 `overlap_in_flight`。

注意 `completed` 的含义：它只表示本次运行的会话已创建、初始事件已被接受，不代表智能体已经完成任务。要确认任务结果，请用运行记录中的 `session_id` 查询会话状态或订阅事件流，见 [会话](/docs/hosted-agents/sessions) 和 [事件流](/docs/hosted-agents/event-stream)。

## 查看运行记录

调用 `GET /v1/triggers/{id}/runs` 列出运行记录，最新的在前；传入 `has_error=true` 时只列出失败的运行。列表默认返回 50 条；如果响应包含 `next_page_token`，将其作为下一次请求的 `page_token` 获取下一页：

```bash theme={null}
curl "${API_BASE_URL:-https://api.moonshot.cn}/v1/triggers/$TRIGGER_ID/runs" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

每条运行记录的 `status` 含义如下：

* `running`：运行记录已创建，会话正在启动（`pending` 状态目前不会出现）。
* `completed`：会话已创建且初始事件已被接受（不代表任务成功）。
* `failed`：运行失败，失败原因见记录中的 `error`。
* `skipped`：触发时触发器不在活跃状态，或 `reuse_session` 模式下上一次运行尚未结束。

`context` 区分运行来源：`schedule` 表示计划触发（含计划时间 `scheduled_at`），`manual` 表示手动运行（含操作者 `actor`）。`session_id` 是本次运行创建的会话，用它查询任务进展。

每个触发器最多保留最新 500 条运行记录，90 天前的记录会被删除。

失败运行记录中的 `error` 使用触发器领域的错误类型（如 `agent_not_found`、`environment_missing`、`environment_not_found`、`environment_archived`、`session_terminated`、`fire_failed`、`overlap_in_flight`），仅供展示和排查，不属于标准错误码体系。词表还覆盖智能体、凭据库、记忆库等目标资源的缺失与归档错误（如 `agent_archived`、`vault_not_found`、`memory_store_archived`），完整列表见 [API 参考](/docs/api-reference)。其中 `environment_missing` 表示触发器没有配置执行环境（未配置执行环境的存量触发器会在下次触发时以该错误失败并自动暂停），`environment_not_found` 表示配置的执行环境已被删除；`session_terminated` 表示 `reuse_session` 的托管会话已被停止，平台不会自动重建，触发器会随之自动暂停——需要继续使用时，先把 `session_mode` 切到 `new_session` 再切回 `reuse_session` 以释放旧绑定，恢复触发器后首次触发会新建托管会话。不可恢复的目标资源错误会自动暂停触发器；可恢复的 `fire_failed` 会保持活跃，在下一次计划时间重试。

## 暂停与恢复

临时停用计划运行时，调用 `POST /v1/triggers/{id}/pause` 暂停触发器：

```bash theme={null}
curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/triggers/$TRIGGER_ID/pause" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

暂停后不再按计划触发，返回 `204`。已经在运行的会话不受影响，手动运行仍然可用。重复暂停是空操作。发生不可恢复的运行错误时，平台也会自动暂停触发器，此时查看触发器，响应中的 `paused_reason.type` 为 `error`，并带有错误详情。

调用 `POST /v1/triggers/{id}/unpause` 恢复：

```bash theme={null}
curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/triggers/$TRIGGER_ID/unpause" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

恢复后计划从现在开始重新计算，暂停期间错过的运行不会补跑，返回 `204`。

## 更新触发器配置

调用 `PATCH /v1/triggers/{id}` 更新配置。该接口采用部分更新：只修改请求体中出现的字段，省略的字段保持不变。下面的示例把计划时间改为工作日 8 点半，并清空文件、凭据库或记忆库等资源以及初始事件：

```bash theme={null}
curl --request PATCH "${API_BASE_URL:-https://api.moonshot.cn}/v1/triggers/$TRIGGER_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "resources": [],
    "initial_events": [],
    "policy": {
      "type": "cron",
      "expression": "30 8 * * 1-5",
      "timezone": "Asia/Shanghai"
    }
  }'
```

更新请求中的配置字段会替换当前值；`resources` 和 `initial_events` 使用空数组清空。`agent_version` 传空字符串表示在触发时刻选择最新版本。`notification` 只有在请求中出现时才会替换当前配置：传入空对象 `{}` 可解除通知，省略该字段则保留现有配置。切换 `session_mode` 离开 `reuse_session` 时，会释放原托管会话的绑定。暂停、恢复和归档不能通过更新完成，请使用对应的操作接口。

## 归档触发器

不再需要的触发器可以归档：

```bash theme={null}
curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/triggers/$TRIGGER_ID/archive" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

归档返回 `204`。归档后触发器永远不再触发，并释放 `reuse_session` 的会话绑定；已有的运行记录仍然保留，可以继续查询。归档不可逆，请确认不再需要该计划后再执行。

## 接收运行通知

需要把运行结果推送到自己的系统时，在创建或更新触发器时配置 `notification`。更新接口只需提交要变更的字段：

```bash theme={null}
curl --request PATCH "${API_BASE_URL:-https://api.moonshot.cn}/v1/triggers/$TRIGGER_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "notification": {
      "url": "https://example.com/webhooks/trigger-runs",
      "secret_vault": {
        "vault_id": "vlt_your_vault_id"
      }
    }
  }'
```

`url` 是接收通知的 HTTPS 端点。`secret_vault` 指向一个凭据库，其中需要有一条名为 `webhook_secret` 的 `environment_variable` 类型凭据，用于给通知签名；凭据值在投递时才读取，配置时只校验凭据库引用，不校验这条凭据是否存在。`url` 和 `secret_vault` 必须同时设置，只设置一个会被拒绝（400 `invalid_parameter_error`）。更新时传入空对象 `{}` 可解除通知配置，省略 `notification` 则保留当前配置。

配置后，平台会针对每次 **计划触发** 的运行向该 URL 发送 HTTPS POST 通知（手动运行和被跳过的运行不发送）。通知事件有三种：`trigger_run.started`（运行开始）、`trigger_run.succeeded`（运行完成）、`trigger_run.failed`（运行失败）。一次运行会收到两类通知：开始时投递 `trigger_run.started`，结束时投递 `trigger_run.succeeded` 或 `trigger_run.failed`。通知按至少一次策略投递，同一事件可能因重投而重复到达，接收方应按 `Webhook-Id` 去重（见下文投递策略）。

通知正文是一个精简的 JSON 信封，只携带事件类型和资源 ID，运行的详细状态由接收方通过运行记录接口查询：

```json theme={null}
{
  "type": "event",
  "id": "whe_01j3z7k8m2n4p6q8r0s2t4v6x8",
  "created_at": "2026-09-02T01:00:00Z",
  "data": {
    "type": "trigger_run.succeeded",
    "id": "trun_01j3z7k8m2n4p6q8r0s2t4v6x9",
    "scope_ref": "project:your_project_id"
  }
}
```

其中 `id` 是本次投递的 ID，与 `Webhook-Id` 请求头相同；重投时正文逐字节不变。

每个投递都带有 `Webhook-Id`、`Webhook-Timestamp` 和 `Webhook-Signature: v1,<base64>` 三个请求头。签名是对 `"<Webhook-Id>.<Webhook-Timestamp>.<请求体原文>"` 计算 HMAC-SHA256 后再做 Base64 编码的结果，密钥就是 `webhook_secret` 凭据的值，接收方应按相同方式计算并比对，确认通知来自平台。

平台按至少一次投递策略尝试发送，每个事件最多尝试 3 次（含首次），失败时使用带抖动的指数退避（基准间隔为 5 秒、10 秒）。收到 2xx 响应即视为成功；投递次数耗尽后该通知会被丢弃。接收方应按 `Webhook-Id` 去重。

## 下一步

<CardGroup cols={3}>
  <Card title="梦境" icon="cloud-moon" href="/docs/hosted-agents/dreams">
    平台托管的记忆维护触发器（Dream Policy）的配置方法。
  </Card>

  <Card title="多智能体编排" icon="sitemap" href="/docs/hosted-agents/multiagent-orchestration">
    让多个智能体协作完成复杂任务。
  </Card>

  <Card title="事件流" icon="bolt" href="/docs/hosted-agents/event-stream">
    订阅运行会话的实时事件，跟踪任务进展。
  </Card>
</CardGroup>
