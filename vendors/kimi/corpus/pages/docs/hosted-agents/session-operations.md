> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 会话管理

> 查看和更新会话，取消当前轮次，并管理会话生命周期。

会话用于运行智能体。创建会话后，通过事件接口发送 `user.message` 来提交输入。创建会话的方法请参阅 [启动会话](/docs/hosted-agents/sessions)。

## 查看会话状态

`status` 表示会话当前状态，公开值包括 `idle`、`running` 和 `terminated`。

| 状态           | 含义              |
| ------------ | --------------- |
| `idle`       | 等待输入，或当前轮次已经结束。 |
| `running`    | 正在执行当前轮次。       |
| `terminated` | 会话已终止，不能继续使用。   |

通常，创建会话后为 `idle`。发送输入后，会话进入 `running`，当前轮次结束后回到 `idle`。取消当前轮次后，会话也会回到 `idle`。归档后，会话进入 `terminated`。

使用下面的命令查询会话当前状态。将 `$SESSION_ID` 替换为创建会话响应中的 `id`。创建会话的完整示例请参阅 [启动会话](/docs/hosted-agents/sessions)。

```bash theme={null}
curl --silent --show-error --fail-with-body "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

状态变化也可通过事件流中的 `session.status` 事件观察。会话回到 `idle` 时，该事件可能包含 `data.stop_reason`，表示当前轮次的停止原因，详见[事件流](/docs/hosted-agents/event-stream)。

## 列出会话

调用 `GET /v1/sessions` 获取当前可见会话。响应中的 `items` 包含当前页的会话；存在下一页时，还会返回 `next_page_token`，用于获取下一页。

| 参数                 | 类型                                                            | 说明                                                        |
| ------------------ | ------------------------------------------------------------- | --------------------------------------------------------- |
| `page_size`        | integer                                                       | 每页数量。                                                     |
| `page_token`       | string                                                        | 使用上一页响应中的 `next_page_token` 继续翻页。                         |
| `order`            | `created_at`、`created_at_desc`、`updated_at`、`updated_at_desc` | 会话排序方式；未提供时使用 `updated_at_desc`。                          |
| `agent_id`         | string                                                        | 只列出某个智能体的会话。                                              |
| `agent_version`    | string                                                        | 只列出固定到某个智能体版本的会话，通常与 `agent_id` 一起使用。                     |
| `statuses`         | array\[string]                                                | 只列出指定生命周期状态的会话（`idle`、`running`、`terminated`）；未提供时包含所有状态。 |
| `include_archived` | boolean                                                       | 传入 `true` 时列表同时包含已归档的会话；默认不列出。                            |

```bash theme={null}
curl --silent --show-error --fail-with-body "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions?page_size=20&order=updated_at_desc" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

## 获取会话

调用 `GET /v1/sessions/{id}` 获取会话详情。

```bash theme={null}
curl --silent --show-error --fail-with-body "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

响应中的 `agent` 是创建时确定的智能体版本快照，`resources` 是绑定到该会话的资源引用（含创建后追加的文件）。

## 更新标题

调用 `PATCH /v1/sessions/{id}` 更新会话标题。请求体中未出现的字段保持不变。

```bash theme={null}
curl --silent --show-error --fail-with-body --request PATCH "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "title": "新的会话标题"
  }'
```

## 覆盖会话中的智能体配置

你可以通过更新会话的 `agent_overrides`，为当前会话后续轮次临时覆盖冻结的智能体版本中的 MCP 服务和技能配置。

此操作不会修改智能体本身，也不会生成新的智能体版本。

`agent_overrides` 只支持 `mcp_servers` 和 `skills`。`mcp_servers` 最多包含 20 个服务，`skills` 最多包含 64 个技能。两个集合字段都按整体替换处理，不会与原集合合并：

* 字段缺省时，保留该集合现有的覆盖配置。
* 传入空数组时，清除该集合的覆盖，回退到冻结的智能体版本对应集合。
* 传入有值的数组时，整体替换该集合的覆盖。

下面示例清除 `mcp_servers` 覆盖。示例不会修改 `skills`，因为请求体中没有包含该字段。

```bash theme={null}
curl --silent --show-error --fail-with-body --request PATCH "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "agent_overrides": {
      "mcp_servers": []
    }
  }'
```

更新 `agent_overrides` 不要求会话处于 `idle` 状态。当前轮次继续使用旧配置，后续轮次使用更新后的配置。

## 取消当前轮次

向 `POST /v1/sessions/{id}/events` 发送 `user.interrupt` 事件停止当前轮次，`user.interrupt` 必须是请求中唯一的事件。只有 `running` 状态的会话才能取消；对 `idle` 或已终止会话调用会返回 400 `failed_precondition_error`。请求成功后返回 `202`；`user.interrupt` 不进入队列，响应中没有 `event_id`。

取消成功后，会话回到 `idle`，仍可发送新的输入。

```bash theme={null}
curl --silent --show-error --fail-with-body --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/events" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "events": [
      { "type": "user.interrupt" }
    ]
  }'
```

## 归档会话

调用 `POST /v1/sessions/{id}/archive` 将会话置为 `terminated`。运行中的会话不能归档，请先取消当前轮次或等待轮次结束。归档不可逆，归档后仍可读取事件和下载文件；如需删除会话，请在删除前下载仍需保留的内容。归档后的会话为只读状态，不能继续发送输入。

归档接口返回 `204`。

```bash theme={null}
curl --silent --show-error --fail-with-body --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/archive" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

## 删除会话

只有已终止的会话才能删除。请先归档会话，再调用 `DELETE /v1/sessions/{id}` 永久删除。删除不可逆，删除后不能再查询会话、事件或会话资源。

```bash theme={null}
curl --silent --show-error --fail-with-body --request DELETE "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

删除接口返回 `204`。
