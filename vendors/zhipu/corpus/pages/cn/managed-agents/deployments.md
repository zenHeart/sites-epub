> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 定时任务

Deployment 把 Agent 变成一个可以按计划自动运行的任务：绑定 cron 调度与初始指令，每次触发时平台自动创建一个新会话执行。适合日报生成、数据巡检、定期同步这类无人值守的工作。没有 cron 的 Deployment 也可以只用于手动触发（manual-only）。

## 创建 Deployment

```bash theme={null}
deployment=$(curl -sS "$BASE_URL/v1/deployments" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "name": "Daily report",
  "agent": "$AGENT_ID",
  "environment_id": "$ENVIRONMENT_ID",
  "schedule": {
    "type": "cron",
    "expression": "0 9 * * 1-5",
    "timezone": "Asia/Shanghai"
  },
  "initial_events": [
    {
      "type": "user.message",
      "content": [
        { "type": "text", "text": "生成昨日销售日报，保存到 /mnt/session/outputs/report.md" }
      ]
    }
  ]
}
EOF
)

DEPLOYMENT_ID=$(jq -r '.id' <<< "$deployment")
```

### 字段说明

| 字段                     | 必填 | 说明                                                                                                                                            |
| ---------------------- | -- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| name                   | 是  | 非空名称                                                                                                                                          |
| agent                  | 是  | Agent ID 字符串（跟随最新版本），或对象形态固定版本 / 带 override：`{"type": "agent", "id": "...", "version": 3}`                                                    |
| environment\_id        | 是  | 运行环境；须为自有且未归档的 Environment。Deployment 只保存引用，每次触发按环境当前配置固化进新会话；环境被归档或删除后，下一次触发失败                                                               |
| schedule               | 否  | `{"type": "cron", "expression", "timezone"}`；省略则为 manual-only。expression 为 5 段 cron 且须存在未来触发点，相邻触发默认间隔 ≥5 分钟；timezone 当前仅支持 Asia/Shanghai（默认） |
| initial\_events        | 是  | 非空的 user.message 列表，内容块支持 text / image（不支持 document）。每次触发都以这组事件启动新会话                                                                          |
| resources              | 否  | 与会话相同：file ≤500 个 + memory\_store ≤8 个                                                                                                        |
| vault\_ids             | 否  | MCP / 环境变量凭据引用                                                                                                                                |
| description / metadata | 否  | 用途说明与自定义元数据（≤16 个 string 键值）                                                                                                                  |

响应中的 **agent.version** 是创建时固定（pin）下来的真实版本号，**next\_run\_at** 是下一次触发时间（manual-only 为 null）。

<Tip>
  部署触发时通常没有客户端在线。自定义工具和 **always\_ask** 不会被接口拒绝，但没人回结果或批准时，会话会停在 **requires\_action**。无人值守的定时任务应只用内置工具和 **always\_allow** 的 MCP，凭据走 **vault\_ids**。
</Tip>

## 记忆让定时任务有连续性

每次触发都是全新会话，默认不共享任何状态。挂载 read\_write 的 Memory Store 后，Agent 可以记住上次运行处理到哪里：

```json theme={null}
{
  "resources": [
    {
      "type": "memory_store",
      "memory_store_id": "memstore_xxxxxxxx",
      "access": "read_write",
      "instructions": "运行结束时把本次处理的截止位置写入 /state/checkpoint.md"
    }
  ]
}
```

## 查看运行记录

每次触发（定时或手动）产生一条 DeploymentRun，记录触发上下文与创建的会话：

```bash theme={null}
curl -sS "$BASE_URL/v1/deployment_runs?deployment_id=$DEPLOYMENT_ID" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26"
```

Run 的关键字段：**trigger\_context**（type 为 schedule 或 manual，schedule 触发含 scheduled\_at）、**session\_id**（该次运行创建的会话，可据此拉事件与产出文件）、**error**（异步失败摘要，成功为 null）、**agent**（本次运行实际使用的 Agent 版本）。列表支持 **deployment\_id**、**has\_error**、**trigger\_type**、**created\_at\[gte]** / **created\_at\[lte]** 过滤，limit 默认 50。单条详情用 **GET /v1/deployment\_runs/:runId**。

拿到 **session\_id** 后，用 **GET /v1/sessions/:id/events** 查看执行过程，用 `GET /v1/files?scope_id=<session_id>` 下载产出。

## 手动触发

```bash theme={null}
curl -sS -X POST "$BASE_URL/v1/deployments/$DEPLOYMENT_ID/run" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26"
```

手动运行直接插入一条 run，不影响 **next\_run\_at**；暂停期间也允许手动触发。适合调试 initial\_events 与验证产出，无需等到下一个调度点。

## 暂停、恢复与归档

| 操作                               | 语义                                                          |
| -------------------------------- | ----------------------------------------------------------- |
| POST /v1/deployments/:id/pause   | 停止后续定时触发；手动 run 仍允许                                         |
| POST /v1/deployments/:id/unpause | 以当前时间为锚重算 next\_run\_at；暂停期间漏掉的触发不会补跑                       |
| POST /v1/deployments/:id         | 更新 name / schedule / initial\_events 等；改 schedule 同样以当下为锚重算 |
| POST /v1/deployments/:id/archive | 终态且幂等；归档后不再触发、不可手动 run（409），历史 run 仍可查询                     |

列表 **GET /v1/deployments** 支持 **agent\_id**、**status**（active / paused）、**created\_at\[gte]** / **created\_at\[lte]**、**include\_archived** 过滤。

## 下一步

<CardGroup cols={2}>
  <Card title="记忆" href="/cn/managed-agents/memory-stores">
    让跨运行状态可持久
  </Card>

  <Card title="事件与流式输出" href="/cn/managed-agents/events">
    分析每次运行的执行过程
  </Card>

  <Card title="文件" href="/cn/managed-agents/files">
    下载运行产出
  </Card>

  <Card title="本页对应 OpenAPI" href="/cn/managed-agents/api-reference#deployments">
    Deployment 与 Deployment Run
  </Card>
</CardGroup>
