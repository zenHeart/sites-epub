> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 最佳实践

下面两个配法覆盖最常见的接入方式：把 Agent **嵌进你的产品**（客服），以及让 Agent **处理文件**（数据分析）。它们不是官方模板，按自己的业务改字段即可。

## 客服 Agent

适合接待用户、查询订单或工单、在你的业务系统里执行操作。会话是多轮对话；真正碰数据的是你的后端，通过自定义工具完成。

| 要点   | 建议                                                                         |
| ---- | -------------------------------------------------------------------------- |
| 模型   | **glm-5.3-flash**，客服更在意首字延迟                                                |
| 内置工具 | 默认关掉 bash / write / edit，避免在沙箱里执行无关命令；需要读用户附件时只开 **read** / **ls**         |
| 业务能力 | **custom** 工具接订单、工单、退款等接口                                                  |
| 敏感操作 | 权限策略不作用于自定义工具。收到 **agent.custom\_tool\_use** 后，由你的应用决定是否执行，需要时先在 UI 里让用户确认 |
| 记忆   | 按客户挂载 Memory Store，记下偏好与未解决问题                                              |
| 附件   | 截图可用消息里的 image；较大文件走 [文件输入](/cn/managed-agents/files)                      |

```json theme={null}
{
  "name": "Customer Support",
  "model": "glm-5.3-flash",
  "system": "你是客服助手。先弄清用户问题，再用工具查询，不要编造订单或政策。退款、改密等写操作必须走对应工具，不要口头承诺已办理。",
  "tools": [
    {
      "type": "agent_toolset_20260601",
      "default_config": { "enabled": false },
      "configs": [
        { "name": "read", "enabled": true },
        { "name": "ls", "enabled": true }
      ]
    },
    {
      "type": "custom",
      "name": "lookup_order",
      "description": "按订单号查询状态、商品、物流与支付信息。用户提供订单号或要求查单时使用。不要用它处理退款。",
      "input_schema": {
        "type": "object",
        "properties": {
          "order_id": { "type": "string", "description": "订单号" }
        },
        "required": ["order_id"]
      }
    },
    {
      "type": "custom",
      "name": "create_ticket",
      "description": "在工单系统创建一条客服工单。当工具查不到答案、或用户要求转人工时使用。",
      "input_schema": {
        "type": "object",
        "properties": {
          "summary": { "type": "string" },
          "priority": { "type": "string", "enum": ["low", "normal", "high"] }
        },
        "required": ["summary"]
      }
    },
    {
      "type": "custom",
      "name": "process_refund",
      "description": "发起退款。仅在用户明确要求退款、且已查到可退订单时使用。调用后由业务系统决定是否真正执行。",
      "input_schema": {
        "type": "object",
        "properties": {
          "order_id": { "type": "string" },
          "amount_cents": { "type": "integer" },
          "reason": { "type": "string" }
        },
        "required": ["order_id", "reason"]
      }
    }
  ]
}
```

创建会话时挂上该客户的 Memory Store，**instructions** 写清记什么、不记什么。自定义工具的事件闭环见[事件与流式输出](/cn/managed-agents/events#处理自定义工具调用)。

<Tip>
  客服需要客户端在线回传工具结果，不适合做成 [定时任务](/cn/managed-agents/deployments)。如果工单系统是 MCP，可为不可逆工具单独设 **always\_ask**，见[工具权限](/cn/managed-agents/permission-policies)。
</Tip>

## 数据分析 Agent

适合用户上传表格或导出文件，让 Agent 在沙箱里计算、出图、再把结果文件拿回来。沙箱已预装 pandas、openpyxl 等，一般不必再配 packages。

| 要点   | 建议                                        |
| ---- | ----------------------------------------- |
| 模型   | **glm-5.3**，复杂表更稳                         |
| 内置工具 | 启用完整 **agent\_toolset\_20260601**         |
| 输入   | 上传 File，挂到会话；提示词写明路径                      |
| 产物   | 要求写入 **/mnt/session/outputs**，idle 后按会话下载 |
| 定时   | 无自定义工具时，可改成 Deployment 做日报                |

```json theme={null}
{
  "name": "Data Analyst",
  "model": "glm-5.3",
  "system": "你是数据分析助手。只根据会话里挂载的输入文件计算，不要编造数据。中间过程可以写在 /workspace。最终表格、图表或报告必须保存到 /mnt/session/outputs/，并在回复里说明文件名。",
  "tools": [
    { "type": "agent_toolset_20260601" }
  ]
}
```

创建会话时挂上输入文件，例如：

```json theme={null}
{
  "agent": "agent_xxxxxxxxxxxx",
  "environment_id": "env_xxxxxxxxxxxx",
  "resources": [
    {
      "type": "file",
      "file_id": "file_xxxxxxxxxxxx",
      "mount_path": "/data/sales.csv"
    }
  ]
}
```

用户消息写清任务，例如：「分析 /mnt/session/uploads/data/sales.csv，按月汇总销售额，把图表和 Excel 存到 /mnt/session/outputs/。」本轮 **session.status\_idle** 之后，用 `GET /v1/files?scope_id=$SESSION_ID` 取回产物。路径约定见[文件](/cn/managed-agents/files)。

需要每天自动跑时，把同一套 Agent / Environment 配进 Deployment，**initial\_events** 写清任务，凭据走 **vault\_ids**。无人值守时不要加自定义工具或 **always\_ask**，否则会话会停着等你回结果。

## 下一步

<CardGroup cols={2}>
  <Card title="定义 Agent" href="/cn/managed-agents/agent-setup">
    字段与版本
  </Card>

  <Card title="工具" href="/cn/managed-agents/tools">
    内置工具集与自定义工具
  </Card>

  <Card title="文件" href="/cn/managed-agents/files">
    输入与产物
  </Card>

  <Card title="常见问题" href="/cn/managed-agents/faq">
    默认工具、重连、归档
  </Card>
</CardGroup>
