> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 多智能体编排

> 配置智能体之间的任务委派，在同一个会话中运行子线程，并观察多智能体执行状态和事件。

多智能体编排允许一个智能体作为协调智能体（coordinator），在同一个会话（session）中将任务委派给一个或多个子线程（child thread）。
协调智能体接收用户输入并组织工作，子线程使用指定的智能体配置执行子任务并返回结果。

本页的操作主线是：配置可委派的智能体，创建会话，发送任务，观察模型创建的子线程，并读取各线程的状态和事件。

## 什么时候使用多智能体编排

当任务可以拆成边界清晰的子任务，或者不同子任务需要不同的智能体配置时，可以使用多智能体编排。

常见场景包括：

* 并行处理互不依赖的资料或子任务，最后由协调智能体汇总结果。
* 将代码审查、资料检索等工作交给配置了相应工具或技能的智能体。
* 为同一类任务配置多个智能体副本，分别处理不同输入。
* 需要独立查看或审计不同子任务的执行轨迹。

如果任务不需要拆分，直接使用普通智能体和会话即可。
多智能体编排会增加智能体配置、线程管理和事件观察的复杂度，不应为了使用多个智能体而拆分简单任务。

## 协调智能体与子线程

创建会话时，平台会创建一个协调线程（coordinator thread）。
它是会话的默认执行入口，使用会话级接口提交的用户输入由它处理。

协调智能体决定委派后，平台会在同一个会话中创建子线程。
子线程执行协调智能体委派的子任务，并将结果返回给协调智能体。

```text theme={null}
会话
└── 协调线程
    ├── 子线程 A
    ├── 子线程 B
    └── 子线程 C
```

智能体、会话和线程的职责不同：

| 对象                       | 作用                                         |
| ------------------------ | ------------------------------------------ |
| 智能体（Agent）               | 定义模型、系统提示词、工具、MCP 服务、技能、插件（Plugin）和可选的委派配置 |
| 会话（Session）              | 固定本次运行使用的智能体版本，并绑定执行环境和会话资源                |
| 协调线程（coordinator thread） | 创建会话时生成，接收用户输入并管理委派                        |
| 子线程（child thread）        | 协调智能体运行时创建，执行具体子任务并保留独立执行轨迹                |

协调线程和子线程属于同一个会话，但每条线程都有自己的状态、历史事件和实时事件流。
共享执行环境不等于共享完整的模型上下文。

协调智能体可以创建子线程，子线程不能继续创建下一级线程。

## 配置可委派的智能体

在创建或更新协调智能体时，通过 `multiagent.agents` 声明它可以委派的智能体。
`type` 用来区分来源类型：

* `type: "agent"`：引用另一个已经存在的智能体。`id` 填写该智能体的 ID；`version` 可选，省略时平台会在写入时固定它的最新版本。
* `type: "self"`：引用协调智能体自己，让子线程复用协调智能体当前固定的版本和配置，不需要填写 `id`。

```json theme={null}
{
  "multiagent": {
    "agents": [
      { "type": "agent", "id": "agent_researcher" },
      { "type": "agent", "id": "agent_writer", "version": "3" },
      { "type": "self" }
    ]
  }
}
```

`agents` 至少包含 1 个条目，最多包含 20 个条目。
重复引用同一个智能体、显示名重复、引用已归档的智能体，或引用本身配置了 `multiagent` 的智能体，都会在写入时报错。
之后更新被引用的智能体，不会改变已经保存的委派配置。
如果要让协调智能体使用被引用智能体的新版本，需要更新协调智能体，生成新的不可变版本。

### 创建协调智能体

下面演示创建一个协调智能体，并在创建时固定它可以委派的智能体名单。
这个请求不会创建子线程，也不会创建名单中的智能体：`agent_researcher` 需要替换为当前项目中实际存在的智能体 ID。
智能体名单中的 `self` 条目允许它再创建一个复用自身当前版本和配置的子线程。

```bash theme={null}
curl -sS -X POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/agents" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "name": "投研编排者",
    "model": { "id": "kimi-k3" },
    "system": "你负责接收任务，并根据任务选择合适的子线程执行。",
    "multiagent": {
      "agents": [
        { "type": "agent", "id": "agent_researcher" },
        { "type": "self" }
      ]
    }
  }'
```

创建成功后，响应中的 `id` 是协调智能体的 ID，后续创建会话时需要传入。
响应中的 `multiagent.agents` 展示平台已经固定的智能体版本；`self` 条目在写入时解析为协调智能体自身，因此名单中还会包含一条指向协调智能体自身 ID 和版本的记录。
以下响应只展示本页后续需要理解的字段，具体响应字段以正式 API 契约为准：

```json theme={null}
{
  "id": "agent_coordinator",
  "name": "投研编排者",
  "version": "1",
  "multiagent": {
    "agents": [
      {
        "id": "agent_researcher",
        "version": "3"
      },
      {
        "id": "agent_coordinator",
        "version": "1"
      }
    ]
  }
}
```

保存协调智能体的 `id`，后续创建会话时使用：

```bash theme={null}
export AGENT_ID="agent_coordinator"
```

## 创建并运行会话

### 创建会话

使用上一步创建的协调智能体和一个执行环境创建会话。
`ENVIRONMENT_ID` 应替换为实际执行环境的 ID。

```bash theme={null}
export ENVIRONMENT_ID="env_xxx"

curl -sS -X POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "agent_id": "agent_coordinator",
    "environment_id": "env_xxx",
    "title": "多智能体任务示例"
  }'
```

创建成功后，响应中的 `id` 是后续发送任务和查询线程时使用的会话 ID：

```json theme={null}
{
  "id": "sesn_example",
  "agent_id": "agent_coordinator",
  "environment_id": "env_xxx",
  "status": "idle",
  "title": "多智能体任务示例"
}
```

```bash theme={null}
export SESSION_ID="sesn_example"
```

### 发送任务

通过会话的事件接口发送 `user.message`。
消息内容使用 `content` 数组，每个内容块声明自己的 `type`。

```bash theme={null}
curl -sS -X POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/events" \
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
              "text": "请将任务拆分为资料检索和结果整理两个子任务，并汇总最终结果。"
            }
          ]
        }
      }
    ]
  }'
```

客户端只向会话提交用户消息。
请求成功后，平台会唤醒协调线程。
协调智能体的模型会根据任务和已配置的委派列表决定是否委派、选择哪个智能体，以及创建多少个子线程。当模型调用 `spawn_subagent` 时，平台会在同一个会话中创建子线程并启动执行。

## 同步和异步委派

用户控制委派的方式是配置和指令，而不是填写工具参数。
`spawn_subagent` 是模型在运行时调用的工具，不是客户端直接调用的 REST API。
如果需要客户端精确控制子任务输入和执行顺序，应改为客户端自行编排多个会话调用，而不是使用多智能体委派。

一次委派的工具输入示例如下：

```json theme={null}
{
  "agent_type": "研究分析师",
  "description": "Research deployment history",
  "prompt": "检查最近的部署记录，并返回带证据的总结。",
  "run_in_background": true
}
```

其中：

* `agent_type` 是必填参数，没有默认值，填写委派列表中智能体的名称（显示名），模型调用时必须显式指定；
* `description` 是用于标识任务的短标签；
* `prompt` 是子线程执行任务所需的完整说明；
* `run_in_background: false` 表示同步委派，也是默认行为；
* `run_in_background: true` 表示异步委派。

### 同步委派

同步委派会等待子线程返回报告、进入空闲状态或终止，然后协调智能体继续执行。

当后续步骤必须依赖子线程的结果时，适合使用同步委派。

### 异步委派

异步委派会在子线程创建并开始执行后立即返回。
子线程完成一轮后，会将报告发送回协调智能体，协调智能体可以继续执行其他工作，或等待消息。

异步委派的工具结果是一段文本，包含子线程 ID 和后续处理说明：

```text theme={null}
Subagent "研究分析师" started in background (thread id: sthr_child_example). Its report will be delivered to you automatically when it finishes a turn — no need to poll. Use send_message to give it follow-up work, check_subagent_status to inspect it, and delete_subagent to terminate it and free its slot.
```

以上是模型侧工具结果的示意，具体工具结果以正式运行行为为准。

子线程完成后会保持 `idle`，不会自动删除；协调智能体可以调用 `delete_subagent` 终止它，终止后线程状态变为 `terminated`。
如果后续仍需要该子线程处理相关任务，协调智能体可以通过 `send_message` 复用它继续发送消息；客户端暂不支持直接向子线程发送消息。

## 智能体之间发送消息

KHA 中的消息都经过协调线程中转。
协调线程可以向指定子线程发送消息，也可以向所有子线程广播；子线程只能把结果或问题发回协调线程。
子线程之间不能直接通信，也不能跨会话发送消息。

```text theme={null}
                协调线程
               /   |    \
        子线程 A  子线程 B  子线程 C
```

### 发送消息：`send_message`

协调智能体可以向指定子线程发送消息，也可以向所有子线程广播：

```json theme={null}
{
  "agent_id": "sthr_child_example",
  "content": "请补充检查 2026 年第二季度的部署记录。"
}
```

广播时，将 `agent_id` 设置为 `all`：

```json theme={null}
{
  "agent_id": "all",
  "content": "请在报告中明确列出尚未验证的事实。"
}
```

### 等待消息：`wait_for_message`

协调智能体或支持消息协作的异步子线程可以使用 `wait_for_message` 等待消息：

```json theme={null}
{
  "timeout": 300
}
```

收到子线程报告后，工具结果文本会包含消息数量、来源线程和正文：

```text theme={null}
<subagent_message from="sthr_child_example">检查完成，未发现新的部署错误。</subagent_message>
```

以上是模型侧消息结果的示意。
客户端可以从 `agent.thread_message_received` 事件的 payload 中读取来源线程（`from_session_thread_id`）和来源智能体显示名（`from_agent_name`）。
如果需要查看子线程的完整执行过程，应读取线程历史事件，而不是依赖 `wait_for_message` 的返回内容。

## 共享资源与上下文隔离

智能体、会话和线程分别管理不同范围的配置：

| 范围   | 内容                       |
| ---- | ------------------------ |
| 智能体级 | 模型、系统提示词、工具、MCP 服务、技能和插件 |
| 会话级  | 固定的智能体版本、执行环境和会话资源       |
| 线程级  | 线程状态、历史事件和实时事件流          |

子线程使用被选中智能体的固定版本及其配置。
会话绑定的文件、凭据库和记忆库等资源通过会话配置管理，具体绑定方式参阅 [启动会话](/docs/hosted-agents/sessions)。

会话级智能体配置覆盖 `agent_overrides` 只影响当前会话，不修改智能体资源或委派列表中的其他智能体。
会话级覆盖配置只作用于协调线程，不会传递给子线程；子线程始终使用委派配置中固定的智能体版本。

## 观察线程和事件

发送任务后，可以先通过会话级事件流观察协调线程的整体进展。
要查看子线程的详细活动，需要先列出会话中的线程，再使用返回的 `id` 查询对应线程。

### 列出会话中的线程

```bash theme={null}
curl -sS \
  "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/threads" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

线程列表按协调线程在前、子线程按创建顺序返回：

```json theme={null}
{
  "items": [
    {
      "id": "sthr_coordinator",
      "session_id": "sesn_example",
      "status": "idle"
    },
    {
      "id": "sthr_researcher",
      "session_id": "sesn_example",
      "parent_thread_id": "sthr_coordinator",
      "status": "idle"
    }
  ],
  "next_page_token": "next-page-token"
}
```

列表响应中的 `id` 是后续查询线程的来源。
协调线程没有 `parent_thread_id`，子线程通过该字段指向父线程。
如果响应包含 `next_page_token`，继续请求下一页，不要假定当前页面包含所有线程。

### 查看线程详情

将 `$THREAD_ID` 设置为线程列表中目标线程的 `id`：

```bash theme={null}
export THREAD_ID="sthr_researcher"

curl -sS \
  "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/threads/$THREAD_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

响应中的 `status` 可以帮助你判断线程是否仍在运行：

```json theme={null}
{
  "id": "sthr_researcher",
  "session_id": "sesn_example",
  "parent_thread_id": "sthr_coordinator",
  "status": "idle",
  "created_at": "2026-08-29T04:00:01Z",
  "updated_at": "2026-08-29T04:01:40Z"
}
```

### 读取线程历史事件

```bash theme={null}
curl -sS \
  "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/threads/$THREAD_ID/events" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

可以从历史事件中查看线程的状态变化和消息协作：

```json theme={null}
{
  "items": [
    {
      "id": "sevt_status",
      "processed_at": "2026-08-29T04:00:05Z",
      "type": "session.thread_status",
      "session_thread_id": "sthr_researcher",
      "data": {
        "status": "running"
      }
    },
    {
      "id": "sevt_message_received",
      "processed_at": "2026-08-29T04:01:40Z",
      "type": "agent.thread_message_received",
      "session_thread_id": "sthr_researcher",
      "data": {
        "content": [
          {
            "type": "text",
            "text": "检查最近的部署记录，并返回带证据的总结。"
          }
        ],
        "from_session_thread_id": "sthr_coordinator"
      }
    }
  ],
  "next_page_token": "next-page-token"
}
```

线程创建事件 `session.thread_created` 只写入协调线程的历史，需要通过会话级事件流（协调线程）观察，不会出现在子线程自己的历史事件中。
以上响应只展示与多智能体编排相关的事件字段。
完整事件类型、字段和分页规则见 [事件流](/docs/hosted-agents/event-stream)。

### 订阅线程实时事件

```bash theme={null}
curl -sS -N \
  "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/threads/$THREAD_ID/events/stream" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Accept: text/event-stream"
```

线程实时事件可能包含状态变化：

```text theme={null}
id: 4096
event: session.thread_status
data: {"id":"sevt_status","processed_at":"2026-08-29T04:00:05Z","session_thread_id":"sthr_researcher","type":"session.thread_status","data":{"status":"running"}}
```

以上事件帧仅用于说明观察方式，实际事件字段和顺序以正式运行行为为准。
帧中的 `id:` 行是恢复游标（数值），断线后可用它从断点继续订阅，详见[事件流](/docs/hosted-agents/event-stream)。
事件中的 `session_thread_id` 用于判断事件属于哪条线程。
线程游标只对对应线程的事件流有效，不能用于其他线程或会话。

### 归档子线程

子线程完成并处于 `idle` 状态后，可以归档它：

```bash theme={null}
curl -sS -X POST \
  "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/threads/$THREAD_ID/archive" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

成功时接口返回 `204 No Content`。
归档不会删除线程的历史事件。

## 一次委派的事件链

一次异步委派通常可以按以下顺序观察：

```text theme={null}
1. 协调线程接收 user.message
2. 协调智能体调用 spawn_subagent
3. session.thread_created
4. 协调线程的任务消息写入 agent.thread_message_sent
5. 子线程进入 running
6. 子线程完成进入 idle，报告投递到协调线程信箱
7. 协调智能体收到 agent.thread_message_received
8. 协调智能体汇总结果
9. 协调线程进入 idle
```

实际事件顺序会受到同步或异步委派、任务执行过程和错误处理的影响。
本流程用于说明观察重点，不代表每次运行都会产生完全相同的事件序列。

## 最佳实践

### 为子线程设置清晰的任务边界

在 `prompt` 中明确输入、输出、成功条件和需要保留的证据。
例如：

```text theme={null}
任务：检查最近 30 天的部署记录。
输出：已确认的事实、对应证据、未解决的问题、建议的下一步。
```

### 只配置实际需要的智能体

委派列表中只加入协调智能体确实需要委派的智能体。
智能体数量过多会增加模型的选择空间和配置维护成本。

### 约定报告格式

可以要求子线程按固定格式返回：

```markdown theme={null}
## 结论

## 证据

## 未解决问题

## 建议
```

这样可以减少协调智能体汇总结果时的格式差异和无关内容。

### 使用线程级事件流审计

不要只查看协调智能体的最终结果。
需要调试或审计时，列出会话中的线程，并独立读取目标子线程的历史事件和实时事件。

## 下一步

<CardGroup cols={4}>
  <Card title="智能体" icon="robot" href="/docs/hosted-agents/agents">
    配置智能体、工具和多智能体委派能力。
  </Card>

  <Card title="会话" icon="message" href="/docs/hosted-agents/sessions">
    创建会话并发送任务输入。
  </Card>

  <Card title="事件流" icon="bolt" href="/docs/hosted-agents/event-stream">
    读取历史事件、订阅 SSE 并处理断线续读。
  </Card>

  <Card title="金融投研智能体" icon="users" href="/docs/hosted-agents/official-investment-research-agent">
    查看官方投研多智能体团队的完整设计。
  </Card>
</CardGroup>
