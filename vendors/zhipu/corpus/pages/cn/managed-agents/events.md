> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 事件与流式输出

事件（Event）是你的应用与会话之间的唯一通信通道：用户消息、Agent 回复、工具调用与结果、状态变化，全部以事件形式流动，并在服务端持久化为事件历史。本页介绍事件类型、三个事件接口的用法，以及自定义工具、审批、打断等进阶场景。

## 事件类型

### 客户端 → 平台

| 事件                            | 说明                                                                                              |
| ----------------------------- | ----------------------------------------------------------------------------------------------- |
| **user.message**              | 用户消息。content 为内容块数组：text / image（base64，至多 3 张、每张 ≤5 MB）/ document（text 或 file source），至多 20 块。 |
| **user.interrupt**            | 打断 Agent 当前执行；可选 reason 字段（当前不持久化）。                                                             |
| **user.custom\_tool\_result** | 回传自定义工具的执行结果，见下文。                                                                               |
| **user.tool\_confirmation**   | 批准或拒绝一次 always\_ask 工具调用，见[工具权限](/cn/managed-agents/permission-policies)。                       |

### 平台 → 客户端

| 事件                                                            | 说明                                                                                                                               |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **agent.message**                                             | Agent 的文本回复，content 为内容块数组。                                                                                                      |
| **agent.thinking**                                            | Agent 正在思考的进度事件（仅公共字段，不含推理内容）。                                                                                                   |
| **agent.tool\_use** / **agent.tool\_result**                  | 内置工具的调用（name、input、evaluated\_permission）与结果（含 is\_error）。                                                                       |
| **agent.mcp\_tool\_use** / **agent.mcp\_tool\_result**        | MCP 工具的调用与结果，use 额外携带 mcp\_server\_name。                                                                                         |
| **agent.custom\_tool\_use**                                   | Agent 请求你的应用执行一个自定义工具。                                                                                                           |
| **session.status\_running**                                   | 会话进入执行状态。                                                                                                                        |
| **session.status\_idle**                                      | 本轮结束。stop\_reason.type ∈ **end\_turn**（正常完成）/ **requires\_action**（等待你的 resolution，另含 event\_ids）/ **retries\_exhausted**（重试耗尽）。 |
| **session.updated** / **session.deleted**                     | 会话配置被更新 / 会话被删除（随后服务端关闭事件流）。                                                                                                     |
| **session.error**                                             | 错误通知：`error{type, message, retry_status}`；retry\_status ∈ retrying / exhausted / terminal；MCP 相关错误另含 mcp\_server\_name。          |
| **span.model\_request\_start** / **span.model\_request\_end** | 单次模型请求区间；end 事件含 is\_error 与 model\_usage 用量。                                                                                    |

所有服务端事件都有全局唯一 **id** 与 **processed\_at** 时间戳，按处理顺序排列，构成可完整回读的事件历史。

## 集成事件

事件相关的三个接口：

| 接口                                 | 用途                                       |
| ---------------------------------- | ---------------------------------------- |
| POST /v1/sessions/:id/events       | 发送事件（1–10 条一批，整批原子校验，任一非法则零写入）           |
| GET /v1/sessions/:id/events        | 列出历史事件（分页、可按 types 与 processed\_at 时间过滤） |
| GET /v1/sessions/:id/events/stream | SSE 实时流（live-only）                       |

### SSE 实时流

```bash theme={null}
curl -N "$BASE_URL/v1/sessions/$SESSION_ID/events/stream" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26"
```

连接语义：

* **live-only**：流只转发连接建立后的实时事件，不回放历史。
* 服务端每 15 秒发送 **: ping** 注释帧保活，客户端应忽略。
* 收到 **session.deleted** 事件后服务端会主动关闭连接。
* 每个 **data:** 载荷与事件列表接口返回的 Event JSON 结构相同。

断线后不要指望流从断点续推。记下已消费事件的 **id** 与 **processed\_at**，重新打开 SSE，再用列表接口按时间把缺口补上：

```bash theme={null}
# 1. 重新打开实时流
curl -N "$BASE_URL/v1/sessions/$SESSION_ID/events/stream" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26"

# 2. 按最后一条已消费事件的 processed_at 向后拉历史
curl -sS "$BASE_URL/v1/sessions/$SESSION_ID/events?order=asc&limit=100&created_at[gt]=$LAST_PROCESSED_AT" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26"
```

补历史与新流在时间边界上可能重叠，客户端按事件 **id** 去重。

### 增量预览（event deltas）

默认情况下，**agent.message** 在内容完整后才作为一条事件下发。若想在 UI 上做逐字流式渲染，用 **event\_deltas** 查询参数订阅增量预览：

```bash theme={null}
curl -N "$BASE_URL/v1/sessions/$SESSION_ID/events/stream?event_deltas[]=agent.message" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26"
```

开启后，流上会先出现 **event: event\_start** 帧（`{"type":"event_start","event":{...}}`），随后若干 **event: event\_delta** 帧携带 content\_delta 增量；可订阅 **agent.message** 与 **agent.thinking** 两类。注意：

* 预览帧自身没有 id / processed\_at，**不写入事件历史**；缓冲完成后的完整事件（权威记录）随后照常下发，客户端应以完整事件对齐最终状态。
* **span.model\_request\_end** 会关闭未收敛的预览。
* 本接口的 query 参数白名单只有 event\_deltas（及 beta）；携带其他参数（types、limit 等）返回 400。

### 列出历史事件

```bash theme={null}
curl -sS "$BASE_URL/v1/sessions/$SESSION_ID/events?order=asc&limit=100&types=agent.message,agent.tool_use" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26"
```

参数：**limit**（默认 100）、**order**（默认 asc）、**page**（游标）、**types**（重复参数或逗号分隔，未知类型 400）。时间过滤用 **created\_at\[gt]**、**created\_at\[gte]**、**created\_at\[lt]**、**created\_at\[lte]**（按 **processed\_at** 比较；尚未处理的事件不命中任何边界）。

## 处理自定义工具调用

Agent 调用自定义工具时的完整回路：

1. 平台派发 **agent.custom\_tool\_use** 事件：含本次调用的 **id**、工具 **name**、按 input\_schema 生成的 **input** 参数对象。
2. 会话进入 **idle**，**session.status\_idle** 的 stop\_reason.type 为 **requires\_action**，event\_ids 列出全部等待中的调用。
3. 你的应用执行工具逻辑。
4. 回发 **user.custom\_tool\_result**：**custom\_tool\_use\_id** 必填（对应调用事件的 id）；**content** 可选（至多 20 块，text / image / document）；失败时置 **is\_error: true** 并在 content 中说明错误。省略 content 即空结果，同样合法。
5. 全部等待中的调用被解决后，会话回到 running，Agent 带着结果继续。

```bash theme={null}
curl -sS "$BASE_URL/v1/sessions/$SESSION_ID/events" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d '{
    "events": [
      {
        "type": "user.custom_tool_result",
        "custom_tool_use_id": "sevt_ctool_01J...",
        "content": [
          {"type": "text", "text": "{\"temperature\": 22, \"condition\": \"sunny\"}"}
        ]
      }
    ]
  }'
```

### requires\_action 期间的发送约束

* 会话处于 idle(requires\_action) 时，发送接口只接受 resolution 事件（user.custom\_tool\_result / user.tool\_confirmation）与 user.interrupt；此时发 **user.message** 会整批被拒（400），消息不会排队。
* resolution 匹配错误分三类：目标 ID 未知 / 跨会话 / 类型不匹配返回 404；目标已被解决或取消返回 409；同一批里两条 resolution 指向同一个等待事件，解析阶段直接 400。任一项失败整批拒绝、零写入。

## 打断与引导

* **running 期间**：可以继续发送 user.message 与 user.interrupt。追加的消息排队到下一个循环边界生效，用于中途引导；interrupt 则要求 Agent 停下当前工作。
* **idle(requires\_action) 期间**：发送 user.interrupt 会取消整组等待中的自定义工具调用与审批请求；取消不产生逐条回执，以事件流中的下一条生命周期事件为准。
* **恢复空闲会话**：对处于 idle(end\_turn) 的会话直接发送新的 user.message 即可继续，沙箱状态与对话历史都在。

## 会话事件数据加密

创建会话时加上 **x-events-encrypted: true**，业务内容型事件会按你在开放平台登记的密钥加密后再落库。开关只在创建时生效，之后不能改，也不会出现在 Session 响应里。

启用前先到开放平台用户中心提交日志加密密钥：[https://bigmodel.cn/usercenter/safety-mgmt/logkeys](https://bigmodel.cn/usercenter/safety-mgmt/logkeys) 。创建时平台会先探测密钥：没有可用密钥或加密服务不可达，会返回 400，且不会创建会话。

```bash theme={null}
curl -sS "$BASE_URL/v1/sessions" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "x-events-encrypted: true" \
  -H "content-type: application/json" \
  -d "{\"agent\": \"$AGENT_ID\", \"environment_id\": \"$ENVIRONMENT_ID\"}"
```

取值必须是精确小写的 **true** 或 **false**（省略等于 false）。**True** / **1** / **yes** 都会 400。

### 加密范围

| 分类       | 事件类型                                                                                                  | 落库          |
| -------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| 用户内容     | user.message、user.tool\_result、user.custom\_tool\_result、user.tool\_confirmation、user.define\_outcome | payload 加密  |
| Agent 内容 | agent.message、agent.tool\_use / tool\_result、custom / MCP 工具的 use 与 result、thread 消息                  | payload 加密  |
| 系统与评测    | system.message、session.updated、span.outcome\_evaluation\_end                                          | payload 加密  |
| 控制与遥测    | user.interrupt、session 状态、thread 状态、模型请求 span、session.error、session.usage、agent.thinking              | 保持明文，供调度与排障 |

同一会话可以同时有明文控制事件和加密业务事件。Agent 执行时平台会临时解密必要内容——这是降低落库暴露面的静态加密，不是平台自己也解不开的端到端零知识。

### 列表与流里长什么样

加密事件不会回明文 content，而是给一个独立信封。GET /v1/sessions/:id/events 与 SSE 都走同一套形状：

```json theme={null}
{
  "id": "sevt_xxxxxxxxxxxx",
  "type": "user.message",
  "processed_at": "2026-08-05T08:06:00.000Z",
  "encrypted": {
    "version": "v1",
    "salt": "base64-salt",
    "data": "base64-ciphertext"
  }
}
```

用你持有的客户密钥，按 version + salt 解密 data，即可还原原来的 payload。控制类事件仍然是普通 JSON，没有 encrypted 字段。

## 跟踪用量

两个粒度：**span.model\_request\_end** 事件携带该次模型请求的 **model\_usage**；Session 对象的 **usage** 字段累计整个会话的 input\_tokens / output\_tokens / cache\_read\_input\_tokens，随 GET /v1/sessions/:id 返回。

## 调试建议

* UI 状态机以 **session.status\_\*** 事件为权威依据；不要仅凭一条 evaluated\_permission: "ask" 的工具事件就渲染审批 UI，等待 idle(requires\_action) 的 event\_ids 确认。
* 排查问题时优先回读事件历史（order=asc），完整的事件序列几乎总能还原现场。
* 长连接注意处理 15 秒 ping 帧与网络中断重连；重连后先补齐缺口再继续消费流。

## 下一步

<CardGroup cols={2}>
  <Card title="工具权限" href="/cn/managed-agents/permission-policies">
    工具审批的完整流程
  </Card>

  <Card title="管理会话" href="/cn/managed-agents/session-operations">
    状态机与运维操作
  </Card>

  <Card title="本页对应 OpenAPI" href="/cn/managed-agents/api-reference#sessions">
    Session：发送事件、列出事件、订阅实时事件
  </Card>
</CardGroup>
