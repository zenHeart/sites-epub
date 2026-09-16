> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 常见问题

> 托管智能体常见问题：资源概念与区别、版本与并发、会话运行与故障、文件与记忆库、控制台能力边界。

<AccordionGroup>
  <Accordion title="官方智能体（Agent）和自定义智能体有什么区别？">
    官方智能体由平台预置并维护，所有用户可读、可直接引用其 `agent_id` 创建会话（Session），但不能更新或归档。自定义智能体由你通过 API 或控制台创建，仅你的项目可见，允许更新和归档。需要定制时，参照官方智能体的配置创建自己的自定义智能体，详见 [智能体](/docs/hosted-agents/agents)。
  </Accordion>

  <Accordion title="技能和插件有什么区别？">
    技能（Skill）是基于文件的可复用能力包：一个 `SKILL.md` 加上若干资源文件，告诉模型怎么做某类任务。插件（Plugin）是官方插件目录分发的打包单元，一个插件可以包含远程 MCP 服务和捆绑技能，引用后一次性获得打包好的工具连接与技能。详见 [技能](/docs/hosted-agents/skills) 与 [插件](/docs/hosted-agents/plugins)。
  </Accordion>

  <Accordion title="记忆库（Memory Store）和会话文件有什么区别？">
    记忆库是项目级的持久化文件集合，可以挂载到不同会话中反复读写，并保留版本历史；会话文件随会话产生，用于一次任务的输入与产出。需要跨会话沉淀的资料放记忆库，详见 [记忆库](/docs/hosted-agents/memory)；任务产出文件的取回见 [文件](/docs/hosted-agents/files)。
  </Accordion>

  <Accordion title="更新智能体后，进行中的会话会受影响吗？">
    不会。会话在创建时冻结当时的智能体版本，中断恢复也继续使用该版本；更新智能体只影响之后新建的会话。
  </Accordion>

  <Accordion title="更新智能体时返回 409 是什么意思？">
    更新请求携带的 `version` 与智能体当前版本不一致，说明它在你读取后被其他操作修改过。重新调用 `GET /v1/agents/{id}` 取得最新 `version`，确认配置后重试。不携带 `version` 则不做并发校验，详见 [智能体](/docs/hosted-agents/agents)。
  </Accordion>

  <Accordion title="平台升级插件后，智能体为什么还在用旧版本？">
    这是版本固定规则：引用插件时，平台会把引用固定为当时的采用版本并写进智能体的不可变版本，之后插件升级不影响已保存的智能体版本。要让智能体用上新版本，需要对智能体做一次更新，生成新的智能体版本，详见 [插件](/docs/hosted-agents/plugins)。
  </Accordion>

  <Accordion title="事件流断开后需要重新执行任务吗？">
    不需要。重新订阅时携带断开前最后一帧的 `id:` 值（恢复游标，不是事件 ID）作为 `cursor`（或使用 `Last-Event-ID` 请求头），就能从断点继续读取，任务本身在服务端继续运行，详见 [事件流](/docs/hosted-agents/event-stream)。
  </Accordion>

  <Accordion title="创建会话时报环境未就绪怎么办？">
    执行环境（Environment）的沙箱镜像在创建后需要异步构建。收到环境未就绪的错误时，等环境状态变为 `ready` 后用原请求重试，不要重复创建新环境，详见 [执行环境](/docs/hosted-agents/environments)。
  </Accordion>

  <Accordion title="取消、归档和删除会话有什么区别？">
    取消（向 `POST /v1/sessions/{id}/events` 发送 `user.interrupt` 事件）只停止当前轮次，会话回到 `idle`，仍可继续发送输入；归档（`POST /v1/sessions/{id}/archive`）把会话置为只读的终止状态，不能再发送输入，且不可逆；删除（`DELETE /v1/sessions/{id}`）永久移除会话，只有已归档的会话才能删除。详见 [会话操作](/docs/hosted-agents/session-operations)。
  </Accordion>

  <Accordion title="智能体产出的文件怎么取回？">
    先调用 `GET /v1/sessions/{session_id}/filesystem` 列出会话文件（可用 `prefix` 逐层查看目录），再用文件条目的 `path` 通过 `GET /v1/sessions/{session_id}/filesystem/raw` 下载，详见 [文件](/docs/hosted-agents/files)。
  </Accordion>

  <Accordion title="上传文件有什么限制？">
    上传限制以 [文件](/docs/hosted-agents/files) 页为准。上传后先确认 `extract_status` 为 `ready`，再把文件引用到会话。
  </Accordion>

  <Accordion title="为什么在控制台里找不到记忆库？">
    当前控制台没有记忆库入口，不能在其中创建或管理记忆库，但记忆库已提供公开 API：可以通过 API 创建和管理记忆库、管理记忆文件，并在创建会话时以 `read_only` 或 `read_write` 方式绑定，详见 [记忆库](/docs/hosted-agents/memory)。
  </Accordion>
</AccordionGroup>
