> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速开始

> 预构建、可配置的托管智能体运行平台，适合 Agent 长程任务与异步工作。

Kimi 托管智能体（Beta 版）正式开启测试，在模型推理 API 之上封装 Kimi Durable Harness，**企业无需自建 Harness，就能获得一个 7x24 小时全托管的环境，保证 Agent 高质量、可持续地执行长程任务**。

<Note>
  Beta 版当前仅针对国内企业认证用户开放，扫描下方二维码，联系销售获取测试支持。
</Note>

<Accordion title="联系销售（飞书扫码）">
  <img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/hosted-agents/qrcode-sales.jpg?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=3d3822aef348de9757914ec06f2861af" alt="联系销售飞书二维码" width="232" data-path="assets/pics/hosted-agents/qrcode-sales.jpg" />
</Accordion>

## 托管智能体产品架构

<img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/hosted-agents/kha-arch.jpeg?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=f9696e25a22bc40227039830f34dcfb9" alt="托管智能体产品架构" width="2880" height="1620" data-path="assets/pics/hosted-agents/kha-arch.jpeg" />

> 托管智能体在设计上是有状态的：会话可长时间运行，暂停后可顺利恢复，并在服务器端存储对话历史、沙箱状态和输出。因此，托管智能体目前不符合「零数据保留」的覆盖条件。

## 何时使用 Kimi 托管智能体

Kimi 开放平台目前提供以下两种产品：

|         | 模型推理 API                    | 托管智能体                              |
| ------- | --------------------------- | ---------------------------------- |
| **是什么** | 直接调用模型推理，查看 [模型列表](/docs/models) | 运行在 Kimi 开放平台基础设施上的预构建、可配置的智能体托管服务 |
| **适合**  | 自定义 Harness，精细控制            | 长时间运行或异步的任务，无需自建沙箱和会话基础设施          |

您可以通过模型推理 API 自建 Harness 系统， 也可以直接体验 Kimi 托管智能体「开箱即用」的 Harness 能力：

| 能力   | 自建 Harness       | **Kimi 托管智能体**          |
| ---- | ---------------- | ----------------------- |
| 会话历史 | 自己拼接、存储并回传消息列表   | 平台以事件形式持久化完整历史，可随时拉取    |
| 工具执行 | 自己解析工具调用、执行并回填结果 | 内置工具由平台在云沙箱中执行          |
| 沙箱   | 自己准备运行命令、读写文件的环境 | 平台提供隔离的云沙箱，可按需配置网络与依赖   |
| 失败恢复 | 自己处理崩溃、断线后的状态重建  | 平台故障后自动接管并恢复执行，行为与中断前一致 |
| 超时重试 | 自己实现重试与限流退避      | 平台承担执行层的重试与调度           |

## 三种使用托管智能体的方式

| 方式                   | 使用文档                             | 使用场景                                                                                 |
| -------------------- | -------------------------------- | ------------------------------------------------------------------------------------ |
| API (推荐)             | [本页面](/docs/hosted-agents/quickstart) | **有完备的功能接口**，可以把托管智能体集成进自己的系统                                                        |
| 控制台                  | [控制台](/docs/hosted-agents/console)    | 在网页上完成 **基础的功能体验**                                                                   |
| hakimi (skill & CLI) | [hakimi](/docs/hosted-agents/hakimi)  | 在终端上用 Kimi Code 或其他类似工具，**用自然语言初始化托管智能体**，初始化之后，详细配置与调用需要参考 [API 文档](/docs/api-reference) |

## 核心概念

| 概念                  | 说明                                                |
| ------------------- | ------------------------------------------------- |
| **智能体（Agent）**      | 模型、system prompt、工具、MCP 服务器、技能与插件                 |
| **技能（Skill）**       | 智能体能力的定义，可按需挂载到智能体配置中，扩展其领域知识或优化其工作流，除官方模板外也支持自定义 |
| **插件（Plugin）**      | 官方打包上架的能力组合（如金融数据插件），可直接加入智能体配置，暂时不支持自定义          |
| **会话（Session）**     | 执行环境中的一次智能体运行实例，执行具体任务并产生输出                       |
| **环境（Environment）** | 会话运行的云沙箱配置：预装依赖、网络访问策略、初始化脚本                      |
| **凭据库（Vault）**      | 集中保存第三方服务凭据，创建会话时绑定使用                             |

这些概念在控制台中都有对应的管理页面，详见 [在控制台中使用](/docs/hosted-agents/console)。

## 注意事项

1. 开始使用前，你需要：
   * 注册 [Kimi 开放平台账号](https://platform.kimi.com/console)，并申请「企业认证」，企业组织 IP 白名单配置、项目成员管理及限额配置请参照 [组织管理最佳实践](/docs/guide/org-best-practice)。
     <img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/hosted-agents/org-verification.png?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=601a7074e0ea77e502aef442877f7bc8" alt="申请企业认证" width="2966" height="1528" data-path="assets/pics/hosted-agents/org-verification.png" />
   * 企业认证通过后，在 [组织管理 - API 管理](https://platform.kimi.com/console/api-keys) 页面创建 API Key

2. 托管智能体是有状态的服务：会话历史、沙箱状态与产出文件持久化在服务端。你可以通过 API 删除已归档的会话（归档后状态为 `terminated`，需先调用归档接口），以及单独删除上传的文件。

3. 托管智能体产品定价见 [托管智能体定价](/docs/pricing/hosted-agents)，常见错误与处理方式见 [常见问题](/docs/hosted-agents/faq)。

## 通过 API 创建托管智能体

<Steps>
  <Step title="获取 API Key 并设置环境变量">
    在 [Kimi 开放平台](https://platform.kimi.com/console/api-keys) 创建 API Key，然后在终端中设置 API 地址和 API Key：

    ```bash theme={null}
    export API_BASE_URL="https://api.moonshot.cn"
    export KIMI_API_KEY="你的_KIMI_API_KEY"
    ```

    后续所有 API 请求都使用 `Authorization: Bearer $KIMI_API_KEY` 进行认证，并携带 `kimi-api-version: 2026-09-01-beta` 请求头选择本文档对应的 API 版本。请妥善保管你的 API Key，不要硬编码在代码中。

    <Note>
      示例统一从环境变量读取 `API_BASE_URL`、`KIMI_API_KEY`，以及后续步骤保存的 `AGENT_ID`、`ENVIRONMENT_ID`、`SESSION_ID`。
    </Note>
  </Step>

  <Step title="查看并选择智能体">
    列出当前可用的智能体：

    ```bash theme={null}
    curl -sS "$API_BASE_URL/v1/agents" \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta"
    ```

    响应包含每个智能体的完整定义，内容较长。如果已安装 `jq`，可以只列出名称和 `id`，让输出更清爽：

    ```bash theme={null}
    curl -sS "$API_BASE_URL/v1/agents" \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta" \
      | jq -r '.items[] | "name: \(.name)\tid: \(.id)"'
    ```

    列表中包含名为 `PPT助手` 的平台官方智能体，它已配置金融插件和 PPT 技能。保存它的 `id`：

    ```bash theme={null}
    export AGENT_ID="agent_..."
    ```
  </Step>

  <Step title="创建执行环境">
    列出现有的执行环境：

    ```bash theme={null}
    curl -sS "$API_BASE_URL/v1/environments" \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta"
    ```

    如果列表不为空，从中挑一个执行环境，保存它的 `id`，然后直接跳到下一步「创建会话」：

    ```bash theme={null}
    export ENVIRONMENT_ID="env_..."
    ```

    如果列表为空，创建一个用于制作 PPT 的执行环境。`config` 为必填字段，`{"type": "cloud"}` 表示创建一个云端执行环境，其余配置项全部使用默认值：

    ```bash theme={null}
    curl -sS -X POST "$API_BASE_URL/v1/environments" \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta" \
      -H "Content-Type: application/json" \
      -d @- <<'JSON'
    {
      "name": "PPT 制作环境",
      "description": "用于生成和保存 PPT 文件",
      "config": {
        "type": "cloud"
      }
    }
    JSON
    ```

    从响应中保存环境 ID（`id` 字段）：

    ```bash theme={null}
    export ENVIRONMENT_ID="env_..."
    ```

    <Tip>
      执行环境的云沙箱镜像在创建后需要一点时间异步构建，通常很快就能就绪。如果接下来创建会话时因环境尚未就绪而报错，说明镜像还没准备好，稍等片刻后重试即可。
    </Tip>
  </Step>

  <Step title="创建会话">
    关联前面保存的智能体和执行环境，创建会话：

    ```bash theme={null}
    curl -sS -X POST "$API_BASE_URL/v1/sessions" \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta" \
      -H "Content-Type: application/json" \
      -d @- <<JSON
    {
      "agent_id": "$AGENT_ID",
      "environment_id": "$ENVIRONMENT_ID",
      "title": "生成金融市场分析 PPT"
    }
    JSON
    ```

    从响应中保存会话 ID（`id` 字段）：

    ```bash theme={null}
    export SESSION_ID="sesn_..."
    ```
  </Step>

  <Step title="订阅事件流">
    为了实时接收智能体的输出，在发送消息之前，先在另一个终端中订阅该会话的 SSE 事件流：

    ```bash theme={null}
    curl -sS -N "$API_BASE_URL/v1/sessions/$SESSION_ID/events/stream" \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta" \
      -H "Accept: text/event-stream"
    ```

    流中的每个事件帧包含 `id`、`event` 和 `data` 三行：

    * `id`：恢复游标（不是事件 ID）。断线重连时把它作为 `cursor` 查询参数或 `Last-Event-ID` 请求头回传，即可从断点之后继续接收。
    * `event`：事件类型，与事件 JSON 中的 `type` 字段一致。
    * `data`：单行完整的事件 JSON，包含事件 ID（`id` 字段，`sevt_` 前缀）、`processed_at`、`type` 和 `data` 负载。

    发送消息后，你会在事件流中看到类似如下的事件帧：

    ```text theme={null}
    id: 101
    event: session.status
    data: {"id":"sevt_01h455vb4pex5vsknk084sn02q","processed_at":"2026-09-01T08:00:01Z","type":"session.status","data":{"status":"running"}}

    id: 102
    event: agent.thinking
    data: {"id":"sevt_01h455vb4pex5vsknk084sn02r","processed_at":"2026-09-01T08:00:03Z","type":"agent.thinking","data":{"content":[{"type":"thinking","thinking":"我需要先搜索近两天的金融行业行情数据……"}]}}

    id: 103
    event: agent.tool_use
    data: {"id":"sevt_01h455vb4pex5vsknk084sn02s","processed_at":"2026-09-01T08:00:05Z","type":"agent.tool_use","data":{"tool_use":{"id":"call_1","name":"web_search","input":{"query":"近两天 金融行业 股票 行情"}},"evaluated_permission":"always_allow"}}

    id: 104
    event: agent.message
    data: {"id":"sevt_01h455vb4pex5vsknk084sn02t","processed_at":"2026-09-01T08:00:20Z","type":"agent.message","data":{"content":[{"type":"text","text":"PPT 已生成，保存在 output/ 目录下。"}]}}
    ```

    <Note>
      以上事件帧仅为示意，展示事件流的大致形态。完整事件类型说明见 [事件流](/docs/hosted-agents/event-stream)。
    </Note>
  </Step>

  <Step title="发送消息">
    回到原来的终端，向会话发送消息，下达本次任务：

    ```bash theme={null}
    curl -sS -X POST "$API_BASE_URL/v1/sessions/$SESSION_ID/events" \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta" \
      -H "Content-Type: application/json" \
      -d @- <<'JSON'
    {
      "events": [
        {
          "type": "user.message",
          "data": {
            "content": [
              {
                "type": "text",
                "text": "你是一个金融行业股票研究员，请汇总近两天的金融行业股票情况，生成一个用于晨会报告的 PPT。"
              }
            ]
          }
        }
      ]
    }
    JSON
    ```

    发送后，订阅事件流的终端会持续收到智能体的执行事件，说明智能体已经开始工作了。
  </Step>

  <Step title="等待执行完成并下载产物">
    当事件流中出现 `session.status` 事件、且事件 `data` 中的 `status` 为 `"idle"` 时，本轮执行完成。

    <Tip>
      事件流支持断线续读：连接断开后重新订阅时，在请求头中携带 `Last-Event-ID`（值为断开前收到的最后一帧的 `id`），即可从断点之后继续接收事件，不会漏掉中间的输出。断线重连与错误码处理详见错误处理。
    </Tip>

    智能体生成的 PPT 会通过内置的 `save_artifact` 工具登记为 **产物（Artifact）**。列出该会话的产物，找到 `.pptx` 文件并保存它的 `id`：

    ```bash theme={null}
    curl -sS "$API_BASE_URL/v1/artifacts?session_id=$SESSION_ID" \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta"
    ```

    下载该产物：

    ```bash theme={null}
    export ARTIFACT_ID="arti_..."
    curl -sS -o output.pptx "$API_BASE_URL/v1/artifacts/$ARTIFACT_ID/content" \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta"
    ```

    下载完成后，在本地打开 `output.pptx` 查看生成的 PPT。
  </Step>

  <Step title="（可选）查看会话中的全部文件">
    产物只包含智能体明确交付的文件。如果需要中间文件，或产物列表为空，可以直接浏览会话文件系统。接口不会递归列出子目录，每次只返回一层的文件和目录，进入子目录时用 `prefix` 指定目录路径：

    ```bash theme={null}
    curl -sS "$API_BASE_URL/v1/sessions/$SESSION_ID/filesystem" \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta"
    curl -sS "$API_BASE_URL/v1/sessions/$SESSION_ID/filesystem?prefix=output" \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta"
    ```

    用文件条目的 `path` 字段替换 `<PATH>`，下载该文件：

    ```bash theme={null}
    curl -sS -o <本地文件名> "$API_BASE_URL/v1/sessions/$SESSION_ID/filesystem/raw?path=<PATH>" \
      -H "Authorization: Bearer $KIMI_API_KEY" \
      -H "kimi-api-version: 2026-09-01-beta"
    ```
  </Step>
</Steps>

## 下一步

<CardGroup cols={3}>
  <Card title="托管智能体定价" icon="tag" href="/docs/pricing/hosted-agents">
    了解插件计费与模型 Tokens 计费的详细说明。
  </Card>

  <Card title="创建与管理智能体" icon="robot" href="/docs/hosted-agents/agents">
    配置模型、system prompt、工具、MCP 服务器、技能与插件。
  </Card>

  <Card title="事件流" icon="bolt" href="/docs/hosted-agents/event-stream">
    查看完整的事件类型与订阅、断线续读机制。
  </Card>

  <Card title="技能" icon="wand-magic-sparkles" href="/docs/hosted-agents/skills">
    为智能体挂载技能，扩展领域知识与工作流能力。
  </Card>

  <Card title="插件" icon="plug" href="/docs/hosted-agents/plugins">
    接入金融等官方插件，让智能体直接调用专业数据源。
  </Card>

  <Card title="记忆" icon="brain" href="/docs/hosted-agents/memory">
    跨会话持久化记忆，让智能体记住偏好与历史上下文。
  </Card>

  <Card title="常见问题" icon="circle-question" href="/docs/hosted-agents/faq">
    常见错误码、排查思路与处理方式汇总。
  </Card>
</CardGroup>
