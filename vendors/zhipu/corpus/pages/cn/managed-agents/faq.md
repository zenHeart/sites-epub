> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 常见问题

**Q：创建 Agent 时不写 tools，会自带沙箱工具吗？**

**A：** 不会。省略 **tools** 等价于空数组，内置工具不会自动启用。需要 bash、读文件等能力时，请显式加入 **agent\_toolset\_20260601**。详见[工具](/cn/managed-agents/tools)。

***

**Q：glm-5.3 和 glm-5.3-flash 怎么选？**

**A：** 要更强推理、处理复杂场景、能多想一会儿，用 **glm-5.3**。更在意首响速度，或需要读图，用 **glm-5.3-flash**。两款都支持 low / high / max，可在创建 Agent 时用 `{"id": "...", "effort": "..."}` 指定。详见[定义 Agent](/cn/managed-agents/agent-setup#设置推理强度)。

***

**Q：能用 Coding Plan 套餐额度跑 Managed Agents 吗？**

**A：** 不能。目前暂不支持 Coding Plan。模型用量一律按开放平台 **API 按量计费**，使用标准 API Key，按 [模型价格](https://bigmodel.cn/pricing) 从 API 余额扣费，不会消耗 Coding Plan 套餐额度。分项说明见[概述 · 计费](/cn/managed-agents/overview#计费)。

***

**Q：怎么判断这一轮做完了？**

**A：** 看 **session.status\_idle**。会话没有单独的「本轮 completed」状态：Agent 做完一轮就会回到 **idle**。再看这条事件的 **stop\_reason.type**：**end\_turn** 表示正常结束，可以发下一条 **user.message**；**requires\_action** 表示在等你回工具结果或批准，还没做完。

***

**Q：会话停在 idle 或 requires\_action，下一步做什么？**

**A：** 先看 **session.status\_idle** 的 **stop\_reason**：

* **end\_turn**：本轮已结束。再发 **user.message** 即可继续。
* **requires\_action**：在等你处理 **event\_ids** 里列出的调用。自定义工具回 **user.custom\_tool\_result**，审批回 **user.tool\_confirmation**。此时发 **user.message** 会被拒绝（400）。

详见[事件与流式输出](/cn/managed-agents/events)。

***

**Q：怎么打断正在跑的 Agent？中途追加消息会怎样？**

**A：** 发送 **user.interrupt** 会打断当前这一轮。Agent 正在跑（**running**）时，也可以继续发 **user.message**，消息会排到下一轮边界再生效，用来中途引导。若停在 **requires\_action**，发 interrupt 会取消整组等待中的工具调用和审批。详见[事件与流式输出](/cn/managed-agents/events)。

***

**Q：改了 Agent 或 Environment，已经在跑的会话会跟着变吗？**

**A：** 不会。创建会话时会钉住当时的 Agent 配置（含会话级覆盖）和环境快照，之后改 Agent 或 Environment 只影响之后新建的会话。定时任务每次触发会按环境**当时**的配置开一条新会话。要在某个已有会话里换工具，须等它 **idle**，再更新该会话的 **agent.tools**。

***

**Q：Web Search / Web Fetch 现在能用吗？**

**A：** 还不能。当前工具集还不包含这两项，上线后将单独计费。

***

**Q：更新 Agent 返回 409 是什么意思？**

**A：** 请求里带了 **version**，但服务器上的当前版本已经变了——通常是别人（或另一次请求）刚更新过。先 GET 最新 Agent，用返回的 version 再更新；CI 这类声明式同步可以省略 version，后写覆盖。

***

**Q：归档和删除有什么区别？**

**A：** 归档把资源变成只读：Agent / Environment 归档后不能再开新会话，已有会话继续；会话归档后只读。删除会拿掉资源本身。归档会话再删除是允许的；running 中的会话要先 **user.interrupt**。各资源细节见对应指南页。

***

**Q：环境未归档是什么意思？创建会话失败？**

**A：** 创建会话必须引用你自己的、未归档 Environment。归档或删除后的环境不能再绑新会话；仍挂在该环境上的会话，在下一次需要使用环境时可能被终止。

***

**Q：SSE 断线后怎么续？会从上次的位置接着推吗？**

**A：** 不会。流是 live-only，只推连接建立之后的事件。记下已消费事件的 **id** 与 **processed\_at**，重新打开流，再用 **GET /v1/sessions/:id/events** 按时间补缺口，并按 id 去重。示例见[事件与流式输出](/cn/managed-agents/events#sse-实时流)。

***

**Q：定时任务能用自定义工具 / always\_ask 吗？**

**A：** 可以创建。但触发后没有人在线回工具结果或批准，会话会停在 **requires\_action**，直到你通过事件接口补上。无人值守的 cron 请只用内置工具和 **always\_allow** 的 MCP，凭据走 **vault\_ids**。

***

**Q：MCP 连不上，会话还会启动吗？**

**A：** 会。创建会话不预检 MCP。服务器不可达或凭据被拒时，会话照常交互，同时发 **session.error**（含 **mcp\_server\_name** 与 **retry\_status**）。可以事先调用 **mcp\_oauth\_validate**。详见[连接 MCP](/cn/managed-agents/mcp)。

***

**Q：有控制台吗？**

**A：** 目前以 API 开放内测，控制台等更多功能近期即将推出。现在请走 API。进展与问题反馈见概述页的[反馈与交流](/cn/managed-agents/overview#反馈与交流)。

***

**Q：怎么看一次对话消耗了多少 tokens？**

**A：** 看 **span.model\_request\_end** 里的 **model\_usage**（单次模型请求），以及 Session 对象的 **usage**（整段会话累计）。这些用量按开放平台 API 按量计费入账，不走 Coding Plan。

***

**Q：Agent 生成的文件在哪里下载？**

**A：** 让 Agent 写到 **/mnt/session/outputs**，再用 `GET /v1/files?scope_id=$SESSION_ID` 列出并下载。写在 /workspace 的中间文件不会被编目。见[文件](/cn/managed-agents/files)。
