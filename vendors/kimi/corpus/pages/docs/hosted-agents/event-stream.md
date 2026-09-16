> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 事件流

> 订阅会话和线程的 SSE 事件流，读取历史事件，并在断线后继续接收智能体输出。

事件流是应用接收会话执行状态和智能体输出的方式。
应用可以向会话发送用户事件，也可以通过 SSE 实时接收智能体事件和会话事件。

## 事件类型

事件对象使用 `type` 标识事件类型，具体数据放在 `data` 中；没有数据的事件会省略 `data` 字段。

事件主要分为三类：

* **用户事件**：应用发送给会话的输入，例如 `user.message` 和 `user.interrupt`。
* **智能体事件**：智能体产生的输出，例如 `agent.message`、`agent.thinking`、`agent.tool_use` 和 `agent.tool_result`。
* **会话事件**：描述会话状态和执行结果，例如 `session.status`、`session.error`、`session.thread_created` 和 `session.thread_status`。

`agent.delta` 是只在实时事件流中发送的增量事件，历史事件列表中不会包含它。

`agent.tool_result` 事件的 `data.tool_result` 中，`content` 是工具提供给模型的内容（`text`、`image` 或 `video` 类型），该字段始终存在；`structured_content` 是用于界面展示的内容（`text`、`file`、`image` 或 `artifact` 类型）。

事件对象包含以下公共字段：

| 字段                  | 说明                                  |
| ------------------- | ----------------------------------- |
| `id`                | 服务端分配的事件 ID。应用可以用它识别事件，并在重新读取时去重。   |
| `processed_at`      | 事件被处理并写入会话历史的时间。历史事件列表的排序和分页以该字段为准。 |
| `session_thread_id` | 产生事件的线程 ID。协调者级别的事件没有此字段。           |
| `type`              | 事件类型。                               |
| `data`              | 事件数据。没有数据时省略。                       |

例如，完整的 `agent.message` 事件如下：

```json theme={null}
{
  "id": "sevt_example_message",
  "processed_at": "2026-01-01T00:00:00Z",
  "type": "agent.message",
  "data": {
    "content": [
      {"type": "text", "text": "任务已完成。"}
    ]
  }
}
```

注意，SSE 消息和其中的 KHA 事件对象各自有一个 `id`：

* SSE 消息中的 `id` 是恢复游标，断线后用于继续订阅。
* `data` 中 KHA 事件对象的 `id` 是业务事件 ID，用于识别和去重。

## 集成事件

创建会话后，先订阅事件流，再发送第一条消息。
这样可以在消息触发执行前建立连接，避免错过早期状态或输出事件。

创建会话和发送首条消息的完整流程请参阅 [启动会话](/docs/hosted-agents/sessions)。
本页只说明事件流相关的接口和处理方式。

### 订阅实时事件流

以下命令中的 `$SESSION_ID` 来自创建会话响应中的 `id`。
第一次订阅时使用 `cursor=now`，表示只接收建立连接后产生的事件，不补发已有历史。

```bash theme={null}
curl -sS -N "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/events/stream?cursor=now" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Accept: text/event-stream"
```

连接建立后，服务端会先发送一条 `control` SSE 消息，告知当前的恢复游标。
如果会话还没有任何事件，该游标为 `0`。
以 `:` 开头的行是连接保活消息，不包含业务数据，应用可以直接忽略。

一条 SSE 消息由 `id`、`event` 和 `data` 等字段组成：

| 字段      | 说明                                                         |
| ------- | ---------------------------------------------------------- |
| `event` | 消息类型，例如 `agent.message`；控制消息和错误消息分别使用 `control` 和 `error`。 |
| `id`    | SSE 消息的恢复游标。应用应按原值保存；普通消息中的 KHA 事件对象另有自己的 `id`。            |
| `data`  | 消息数据。普通消息中是 KHA 事件对象，控制消息和错误消息中分别是控制信息和错误信息。               |

下面展示连接建立、接收事件、连接保活和流错误时的消息格式：

```text theme={null}
event: control
id: 4096
data: {"cursor":"4096","reason":"tail"}

id: 4128
event: agent.message
data: {"id":"sevt_example_message","type":"agent.message","processed_at":"2026-01-01T00:00:00Z","data":{"content":[{"type":"text","text":"任务已完成。"}]}}

: hb

event: error
data: {"error":{"type":"server_error","message":"stream failed"}}
```

`control` 消息用于告知恢复位置，普通消息携带 KHA 事件对象。
连接保活消息以 `:` 开头，服务端每 30 秒发送一次 `: hb`，不包含业务数据；`event: error` 表示事件流发生错误，服务端发送后会关闭连接。

### 发送输入事件

建立 SSE 连接后，向同一个会话发送 `POST /v1/sessions/{session_id}/events`，提交 `user.message` 或 `user.interrupt`。
请求成功后返回 202，响应中的 `event_id` 是已接受排队输入的事件 ID（部署提供输入队列时返回），可用于查询待处理队列或撤回；后续状态和输出会通过 SSE 连接返回。
发送首条 `user.message` 的完整 cURL 命令请参阅 [启动会话](/docs/hosted-agents/sessions#启动任务)。

## 判断任务状态

收到 `session.status` 且 `data.status` 为 `idle` 时，表示当前轮次已经结束。
`idle` 不表示会话资源已经结束；应用仍然可以向同一会话发送新的用户事件。

`session.error` 表示会话执行过程中发生错误，其中的 `data.error_type` 是机器可读的错误类别，`data.message` 是错误说明。

这类会话执行错误与 SSE 消息中的 `event: error` 不同：前者是会话运行失败，后者是事件流本身发生错误，服务端发送后会关闭连接。

## 读取历史并继续接收实时事件

历史事件通过 `GET /v1/sessions/{session_id}/events` 分页读取。
响应中的 `items` 按 `processed_at` 排序，默认 `order=asc`，最旧的事件在前；传入 `order=desc` 时最新的事件在前，`page_token` 继续向更早的事件翻页。响应可能包含 `next_page_token` 和 `stream_cursor`。
`items` 不包含 `agent.delta`。

```bash theme={null}
curl -sS "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/events?page_size=20" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

如果响应包含 `next_page_token`，将它直接作为下一次请求的 `page_token`，继续读取下一页：

```bash theme={null}
curl -sS "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/events?page_size=20&page_token=$NEXT_PAGE_TOKEN" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

`$NEXT_PAGE_TOKEN` 必须替换为上一次响应中的 `next_page_token`。
读取到需要的位置后，使用该页响应中的 `stream_cursor` 订阅后续实时事件，不要把 `next_page_token` 作为实时流的 `cursor`。

由于 `stream_cursor` 对应的是该页末尾的恢复位置，继续订阅时可能再次收到该页末尾已经读取过的事件。
应用应按 KHA 事件对象的 `id` 去重。

## 断线恢复

游标是不透明字符串，应用只需保存并原样回传，不要解析或拼接。
网络断开后，将最近收到的 SSE 消息 `id` 作为 `cursor` 查询参数，或放入 `Last-Event-ID` 请求头重新订阅。
这里的 SSE 消息 `id` 是消息层的恢复游标，不是 KHA 事件对象的 `id`。

下面的 `$SSE_CURSOR` 必须替换为应用保存的最近一条 SSE 消息 `id`：

```bash theme={null}
curl -sS -N "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/events/stream?cursor=$SSE_CURSOR" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Accept: text/event-stream"
```

也可以使用 `Last-Event-ID` 请求头传回同一个游标：

```bash theme={null}
curl -sS -N "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/events/stream" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Accept: text/event-stream" \
  --header "Last-Event-ID: $SSE_CURSOR"
```

如果同时提供 `cursor` 查询参数和 `Last-Event-ID` 请求头，服务端优先使用 `cursor` 查询参数。
如果游标无效，接口会返回错误；此时重新读取历史，并使用新的 `stream_cursor` 继续订阅实时事件。

## 处理事件增量

`agent.delta` 只出现在实时事件流中，不会出现在历史事件列表中。
如果应用只需要任务完成后的最终结果，可以忽略它，直接处理完整的 `agent.message`、`agent.thinking` 和 `agent.tool_use` 事件。

如果应用需要在智能体生成过程中实时显示输出，请按 `data.kind` 处理增量：

| `data.kind` | 应用的处理方式                                                                                                |
| ----------- | ------------------------------------------------------------------------------------------------------ |
| `text`      | 将 `data.delta` 依次追加到当前显示的文本末尾。                                                                         |
| `thinking`  | 将 `data.delta` 依次追加到当前显示的思考内容末尾。                                                                       |
| `tool_use`  | 按 `data.tool_use_id` 关联同一次工具调用，将 `data.input_delta` 依次追加到工具输入中。首个增量携带 `name`；工具由 MCP 服务器提供时还会携带 `mcp`。 |

例如，应用先后收到以下两个文本增量：

```json theme={null}
{
  "type": "agent.delta",
  "data": {
    "kind": "text",
    "delta": "正在"
  }
}
```

```json theme={null}
{
  "type": "agent.delta",
  "data": {
    "kind": "text",
    "delta": "分析"
  }
}
```

应用将两个事件中的 `data.delta` 依次追加，实时输出就会从“正在”更新为“正在分析”。

工具输入增量示例如下：

```json theme={null}
{
  "type": "agent.delta",
  "data": {
    "kind": "tool_use",
    "tool_use_id": "toolu_example_call",
    "name": "search",
    "input_delta": "{\"query\":\""
  }
}
```

同一次工具调用的增量都使用相同的 `tool_use_id`。
`input_delta` 是工具输入 JSON 的片段，单个片段通常不是完整的 JSON，应用应拼接完整输入后再解析。

增量只用于实时显示，不是最终结果。
收到完整的 `agent.message`、`agent.thinking` 或 `agent.tool_use` 后，应用应使用完整事件内容替换此前累积的增量内容。

## 查看线程事件

多智能体会话中的每条线程都有自己的历史事件和实时事件流。
会话级接口返回协调线程的事件；要查看子线程，请使用线程级接口。
子线程的 `thread_id` 通常来自事件中的 `session_thread_id`，也可以从会话的线程列表中获取。
多智能体配置和线程关系请参阅 [多智能体编排](/docs/hosted-agents/multiagent-orchestration)。

### 读取线程历史

```bash theme={null}
curl -sS "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/threads/$THREAD_ID/events?page_size=20" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

### 订阅线程实时事件

```bash theme={null}
curl -sS -N "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/threads/$THREAD_ID/events/stream?cursor=now" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Accept: text/event-stream"
```

将 `$SESSION_ID` 和 `$THREAD_ID` 替换为实际的会话 ID 和线程 ID。
线程历史和实时流的处理方式与会话级事件相同，但线程游标只对对应线程的事件流有效，不能用于其他线程或会话。
