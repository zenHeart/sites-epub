> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 启动会话

> 创建会话以运行智能体，绑定所需的执行环境和资源，并发送首条消息启动任务。

会话（Session）是智能体的一次运行实例，对应一项具体任务。
创建会话时，平台会把指定的智能体版本、执行环境版本和会话资源固定下来，并返回一个以 `sesn_` 开头的会话 ID。
后续可以使用该 ID 发送事件、订阅事件和管理会话生命周期。

<Note>
  创建会话前，请先准备好一个 [智能体](/docs/hosted-agents/agents) 和一个处于可用状态的 [执行环境](/docs/hosted-agents/environments)。
</Note>

<Warning>
  **创建会话不等于启动任务。** 创建成功后会话处于 `idle` 状态，不会执行智能体，也不会产生任务事件。
  建议先打开 [事件流](/docs/hosted-agents/event-stream)，再发送第一条 `user.message`；收到该输入后，会话才会进入 `running` 状态。
</Warning>

## 创建前的配置

调用 `POST /v1/sessions` 创建会话。
请求体中只有 `agent_id` 和 `environment_id` 必填：

| 字段                | 类型     | 是否必填 | 说明                                                 |
| ----------------- | ------ | ---- | -------------------------------------------------- |
| `agent_id`        | string | 是    | 要运行的智能体 ID。                                        |
| `environment_id`  | string | 是    | 会话使用的执行环境 ID。环境必须对当前调用方可见、处于活动状态，并且已有可用版本；创建后不能更改。 |
| `agent_version`   | string | 否    | 要使用的智能体精确版本；省略时使用创建时可用的最新版本。                       |
| `title`           | string | 否    | 会话名称，最多 256 个字符；创建后可以更新。                           |
| `metadata`        | object | 否    | 用于检索和标注的自定义键值对，最多 16 对。                            |
| `agent_overrides` | object | 否    | 仅覆盖当前会话的 `mcp_servers` 和 `skills`，分别最多 20 个和 64 个。 |
| `resources`       | array  | 否    | 创建时绑定的文件、凭据库或记忆库资源；每个会话最多绑定 16 个凭据库和 8 个记忆库。       |

`agent_overrides` 用于在当前会话中临时调整冻结的智能体版本，不会修改智能体资源或创建新的智能体版本。
目前只支持 `mcp_servers` 和 `skills` 两个集合字段，不支持覆盖 `model`、`system` 或 `tools`。

每个集合字段都支持三种状态：省略表示继承冻结智能体版本中的集合，显式传入空数组表示清空本会话中的集合，传入有值的数组表示整体替换集合，不会与原集合合并。
该配置只影响当前会话。

`resources` 中的每个对象都通过 `type` 区分资源类型：

* `file`：通过 `file_id` 引用已上传的文件。
* `vault`：通过 `vault_id` 绑定凭据库；绑定关系在创建时确定。
* `memory_store`：通过 `memory_store_id` 绑定记忆库，并通过 `access` 指定 `read_only` 或 `read_write`；绑定关系和访问模式在创建时确定。可选 `instructions` 为本次绑定向模型提供附加指引。

资源是引用关系，不会把文件或凭据内容复制进请求体。
文件、凭据库和记忆库的准备方式分别见 [文件](/docs/hosted-agents/files)、[凭据库](/docs/hosted-agents/vaults) 和 [记忆库](/docs/hosted-agents/memory)。

## 创建会话

下面的请求创建会话并绑定一个已上传文件。
如果不需要绑定资源，可以省略 `resources`；如果需要绑定凭据库或记忆库，请在同一个数组中添加对应的引用。

```bash theme={null}
curl "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions" \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "agent_your_agent_id",
    "environment_id": "env_your_environment_id",
    "agent_version": "version_you_want_to_pin",
    "title": "代码仓库调研任务",
    "metadata": {
      "project": "backend-migration"
    },
    "agent_overrides": {
      "mcp_servers": [
        {
          "type": "url",
          "name": "project-tools",
          "url": "https://mcp.example.com/mcp"
        }
      ],
      "skills": [
        {
          "skill_id": "skill_your_skill_id",
          "version": "your_skill_version"
        }
      ]
    },
    "resources": [
      {
        "type": "file",
        "file_id": "file_your_file_id"
      }
    ]
  }'
```

创建成功后，接口返回会话对象。
此时 `status` 为 `idle`，表示会话已经创建但尚未启动：

```json theme={null}
{
  "id": "sesn_your_session_id",
  "agent_id": "agent_your_agent_id",
  "environment_id": "env_your_environment_id",
  "status": "idle",
  "title": "代码仓库调研任务",
  "metadata": {
    "project": "backend-migration"
  },
  "resources": [
    {
      "type": "file",
      "id": "sres_your_resource_id",
      "file_id": "file_your_file_id"
    }
  ],
  "created_at": "2026-01-01T00:00:00Z",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

## 创建时冻结版本

创建会话时，平台会为会话选择并固定以下配置：

* **智能体版本**：省略 `agent_version` 时，固定创建时可用的最新版本；指定该字段时，固定指定的版本。
  之后更新智能体不会改变这个会话使用的版本。
* **执行环境版本**：请求传入的是 `environment_id`，平台在创建时为该环境选择并固定符合条件的可用版本。
  `environment_id` 绑定后不能更改；如果环境不可见、已归档或没有可用版本，创建请求会被拒绝。
* **会话资源**：创建时绑定的凭据库和记忆库不能再追加或替换。
  文件可以在创建后通过会话资源接口追加或移除，具体操作见 [文件](/docs/hosted-agents/files)。

<Tip>
  想让新任务使用更新后的智能体或执行环境配置时，请创建新会话。
  已创建的会话继续使用其冻结的版本。
</Tip>

## 启动任务

创建会话后按以下顺序启动任务：

<Steps>
  <Step title="订阅事件流">
    调用 `GET /v1/sessions/{session_id}/events/stream` 建立 SSE 连接，以便接收启动后的状态和输出事件。
  </Step>

  <Step title="发送首条消息">
    调用 `POST /v1/sessions/{session_id}/events`，发送一个 `user.message` 事件。
    该请求才会把任务加入会话输入队列并触发执行。
  </Step>

  <Step title="处理事件">
    订阅 `session.status`、`agent.message` 等事件，直到本轮执行结束。
    事件格式和断线续读方式见 [事件流](/docs/hosted-agents/event-stream)。
  </Step>
</Steps>

下面的示例需要在两个终端中运行。先在终端 1 订阅事件流，再在终端 2 发送首条消息；将示例中的 `sesn_your_session_id` 替换为创建会话后返回的会话 ID。

**终端 1：订阅事件流**

```bash theme={null}
curl -sS -N --request GET \
  "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/sesn_your_session_id/events/stream?cursor=now" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Accept: text/event-stream"
```

**终端 2：发送首条消息**

```bash theme={null}
curl --request POST \
  "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/sesn_your_session_id/events" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "events": [
      {
        "type": "user.message",
        "data": {
          "content": [
            {
              "type": "text",
              "text": "请分析这份数据并给出结论。"
            }
          ]
        }
      }
    ]
  }'
```

发送消息后，事件会持续输出到终端 1。收到 `session.status` 和 `agent.message` 等事件后，可以观察任务状态和智能体输出。事件流的断线恢复和事件处理方式见 [事件流](/docs/hosted-agents/event-stream)。

## 下一步

<CardGroup cols={3}>
  <Card title="订阅事件流" icon="bolt" href="/docs/hosted-agents/event-stream">
    建立 SSE 连接、发送消息并处理实时事件。
  </Card>

  <Card title="会话操作" icon="sliders" href="/docs/hosted-agents/session-operations">
    查询会话、更新标题、取消执行、归档或删除会话。
  </Card>
</CardGroup>
