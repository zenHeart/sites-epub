> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# API 参考

Managed Agents API 的速查页：请求约定、全部端点与错误码。下表说明可点进对应 API 页面，查看字段、示例与 Playground。

## 请求约定

### Base URL 与协议头

```text theme={null}
https://agent-api.bigmodel.cn/api/agent/managed
```

路径以 `/v1` 开头，例如 `POST /v1/agents`。

所有请求携带三个头。Authorization 使用智谱开放平台 API Key：

```bash theme={null}
-H "Authorization: Bearer $ZHIPUAI_API_KEY"
-H "zai-version: 2026-05-26"
-H "zai-beta: managed-agents-2026-05-26"
```

写请求另加 **content-type: application/json**。上传文件或 Skill 时改用表单（`multipart/form-data`），不要发 JSON。

需要把会话里的对话和工具内容加密落库时，创建会话再加 **x-events-encrypted: true**（只能是小写 true / false）。详见 [会话事件数据加密](/cn/managed-agents/events#会话事件数据加密)。

### ID 与时间戳

资源 ID 带类型前缀，例如 **agent\_**、**env\_**、**sess\_**、**sevt\_**（事件）、**file\_**、**sesrsc\_**（会话资源）、**memstore\_**、**vlt\_**（Vault）、**vcrd\_**（凭据）、**skill\_**、**depl\_**、**drun\_**。错误响应中的 **request\_id** 以 **req\_** 开头，联系支持时请附上。时间戳统一为 RFC 3339 UTC 格式。

### 分页

大多数列表接口使用不透明游标：响应含 **next\_page**，把它作为 **page** 参数传入下一次请求；**limit** 控制页大小（各接口默认值不同）。Files 列表例外，使用 **before\_id** / **after\_id** 游标（互斥）。事件列表支持 **order**（asc / desc）。

### metadata

多数资源支持 **metadata**：最多 16 个键值对，键 ≤64 字符、值 ≤512 字符，均为字符串。更新时按键级 patch：传字符串写入、传 null 删除该键、整个 metadata 传 null 清空。

## 端点总表

按资源列出全部接口。名称可点进对应页面看字段、示例与 Playground。

### Agents

概念说明见 [定义 Agent](/cn/managed-agents/agent-setup)。

<div className="api-ref-table">
  | 方法   | 路径                           | 名称                                                              | 说明              |
  | :--- | :--------------------------- | :-------------------------------------------------------------- | :-------------- |
  | POST | /v1/agents                   | [创建 Agent](/api-reference/managed-agents--agent/创建-agent)       | 创建可复用的 Agent 配置 |
  | GET  | /v1/agents                   | [列出 Agent](/api-reference/managed-agents--agent/列出-agent)       | 列出你的 Agent      |
  | GET  | /v1/agents/:agentId          | [获取 Agent](/api-reference/managed-agents--agent/获取-agent)       | 获取当前配置          |
  | POST | /v1/agents/:agentId          | [更新 Agent](/api-reference/managed-agents--agent/更新-agent)       | 更新配置，有变化时生成新版本  |
  | GET  | /v1/agents/:agentId/versions | [列出 Agent 版本](/api-reference/managed-agents--agent/列出-agent-版本) | 列出历史版本          |
  | POST | /v1/agents/:agentId/archive  | [归档 Agent](/api-reference/managed-agents--agent/归档-agent)       | 已有会话继续，不能再开新会话  |
</div>

### Environments

概念说明见 [配置运行环境](/cn/managed-agents/cloud-environment)。

<div className="api-ref-table">
  | 方法     | 路径                                                    | 名称                                                                          | 说明               |
  | :----- | :---------------------------------------------------- | :-------------------------------------------------------------------------- | :--------------- |
  | POST   | /v1/environments                                      | [创建 Environment](/api-reference/managed-agents--environment/创建-environment) | 创建运行环境（软件包、网络策略） |
  | GET    | /v1/environments                                      | [列出 Environment](/api-reference/managed-agents--environment/列出-environment) | 列出运行环境           |
  | GET    | /v1/environments/<wbr />:environmentId                | [获取 Environment](/api-reference/managed-agents--environment/获取-environment) | 获取单个环境           |
  | POST   | /v1/environments/<wbr />:environmentId                | [更新 Environment](/api-reference/managed-agents--environment/更新-environment) | 只影响之后新建的会话       |
  | POST   | /v1/environments/<wbr />:environmentId/<wbr />archive | [归档 Environment](/api-reference/managed-agents--environment/归档-environment) | 已有会话继续，不能再绑新会话   |
  | DELETE | /v1/environments/<wbr />:environmentId                | [删除 Environment](/api-reference/managed-agents--environment/删除-environment) | 删除环境             |
</div>

### Sessions

概念说明见 [创建会话](/cn/managed-agents/create-session)、[管理会话](/cn/managed-agents/session-operations)、[事件与流式输出](/cn/managed-agents/events)。

<div className="api-ref-table">
  | 方法     | 路径                                                                 | 名称                                                                        | 说明                          |
  | :----- | :----------------------------------------------------------------- | :------------------------------------------------------------------------ | :-------------------------- |
  | POST   | /v1/sessions                                                       | [创建 Session](/api-reference/managed-agents--session/创建-session)           | 引用 Agent 与 Environment 创建会话 |
  | GET    | /v1/sessions                                                       | [列出 Session](/api-reference/managed-agents--session/列出-session)           | 按条件列出会话                     |
  | GET    | /v1/sessions/<wbr />:sessionId                                     | [获取 Session](/api-reference/managed-agents--session/获取-session)           | 获取状态、用量与配置快照                |
  | POST   | /v1/sessions/<wbr />:sessionId                                     | [更新 Session](/api-reference/managed-agents--session/更新-session)           | 更新标题或 metadata；idle 时也可换工具  |
  | POST   | /v1/sessions/<wbr />:sessionId/<wbr />archive                      | [归档 Session](/api-reference/managed-agents--session/归档-session)           | 归档后只读                       |
  | DELETE | /v1/sessions/<wbr />:sessionId                                     | [删除 Session](/api-reference/managed-agents--session/删除-session)           | 删除会话                        |
  | POST   | /v1/sessions/<wbr />:sessionId/<wbr />events                       | [发送事件](/api-reference/managed-agents--session/发送事件)                       | 发送用户消息、工具结果或打断              |
  | GET    | /v1/sessions/<wbr />:sessionId/<wbr />events                       | [列出事件](/api-reference/managed-agents--session/列出事件)                       | 分页拉取事件历史                    |
  | GET    | /v1/sessions/<wbr />:sessionId/<wbr />events/<wbr />stream         | [订阅实时事件](/api-reference/managed-agents--session/订阅实时事件)                   | 用 SSE 订阅实时事件                |
  | POST   | /v1/sessions/<wbr />:sessionId/<wbr />resources                    | [新增会话资源](/api-reference/managed-agents--session/新增-session-file-resource) | 会话创建后追加挂载文件等资源              |
  | GET    | /v1/sessions/<wbr />:sessionId/<wbr />resources                    | [列出会话资源](/api-reference/managed-agents--session/列出-session-resource)      | 列出已挂载资源                     |
  | GET    | /v1/sessions/<wbr />:sessionId/<wbr />resources/<wbr />:resourceId | [获取会话资源](/api-reference/managed-agents--session/获取-session-file-resource) | 获取单个挂载资源                    |
  | DELETE | /v1/sessions/<wbr />:sessionId/<wbr />resources/<wbr />:resourceId | [删除会话资源](/api-reference/managed-agents--session/删除-session-file-resource) | 移除挂载资源                      |
</div>

### Files

概念说明见 [文件](/cn/managed-agents/files)。

<div className="api-ref-table">
  | 方法     | 路径                        | 名称                                                           | 说明                  |
  | :----- | :------------------------ | :----------------------------------------------------------- | :------------------ |
  | POST   | /v1/files                 | [上传 File](/api-reference/managed-agents--file/上传-file)       | 上传文件，供会话挂载给 Agent 读 |
  | GET    | /v1/files                 | [列出 File](/api-reference/managed-agents--file/列出-file)       | 列出已上传和会话产出的文件       |
  | GET    | /v1/files/:fileId         | [获取 File](/api-reference/managed-agents--file/获取-file)       | 获取文件元数据             |
  | GET    | /v1/files/:fileId/content | [下载 File 内容](/api-reference/managed-agents--file/下载-file-内容) | 下载文件内容              |
  | DELETE | /v1/files/:fileId         | [删除 File](/api-reference/managed-agents--file/删除-file)       | 删除文件                |
</div>

### Memory Stores

概念说明见 [记忆](/cn/managed-agents/memory-stores)。

<div className="api-ref-table api-ref-table-longpath">
  | 方法     | 路径                                                                                         | 名称                                                                           | 说明                 |
  | :----- | :----------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- | :----------------- |
  | POST   | /v1/memory\_stores                                                                         | [创建 Memory Store](/api-reference/managed-agents--memory/创建-memory-store)     | 创建跨会话的记忆库          |
  | GET    | /v1/memory\_stores                                                                         | [列出 Memory Store](/api-reference/managed-agents--memory/列出-memory-store)     | 列出记忆库              |
  | GET    | /v1/memory\_stores/<wbr />:storeId                                                         | [获取 Memory Store](/api-reference/managed-agents--memory/获取-memory-store)     | 获取记忆库              |
  | POST   | /v1/memory\_stores/<wbr />:storeId                                                         | [更新 Memory Store](/api-reference/managed-agents--memory/更新-memory-store)     | 更新名称、说明或 metadata  |
  | POST   | /v1/memory\_stores/<wbr />:storeId/<wbr />archive                                          | [归档 Memory Store](/api-reference/managed-agents--memory/归档-memory-store)     | 归档后不能再挂到新会话        |
  | DELETE | /v1/memory\_stores/<wbr />:storeId                                                         | [删除 Memory Store](/api-reference/managed-agents--memory/删除-memory-store)     | 删除记忆库及其中全部记忆       |
  | POST   | /v1/memory\_stores/<wbr />:storeId/<wbr />memories                                         | [创建 Memory](/api-reference/managed-agents--memory/创建-memory)                 | 写入一条记忆             |
  | GET    | /v1/memory\_stores/<wbr />:storeId/<wbr />memories                                         | [列出 Memory](/api-reference/managed-agents--memory/列出-memory)                 | 按路径前缀浏览记忆          |
  | GET    | /v1/memory\_stores/<wbr />:storeId/<wbr />memories/<wbr />:memoryId                        | [获取 Memory](/api-reference/managed-agents--memory/获取-memory)                 | 读取一条记忆             |
  | POST   | /v1/memory\_stores/<wbr />:storeId/<wbr />memories/<wbr />:memoryId                        | [更新 Memory](/api-reference/managed-agents--memory/更新-memory)                 | 更新路径或内容            |
  | DELETE | /v1/memory\_stores/<wbr />:storeId/<wbr />memories/<wbr />:memoryId                        | [删除 Memory](/api-reference/managed-agents--memory/删除-memory)                 | 删除一条记忆             |
  | GET    | /v1/memory\_stores/<wbr />:storeId/<wbr />memory\_versions                                 | [列出 Memory Version](/api-reference/managed-agents--memory/列出-memory-version) | 列出记忆的变更记录          |
  | GET    | /v1/memory\_stores/<wbr />:storeId/<wbr />memory\_versions/<wbr />:versionId               | [获取 Memory Version](/api-reference/managed-agents--memory/获取-memory-version) | 获取某次变更             |
  | POST   | /v1/memory\_stores/<wbr />:storeId/<wbr />memory\_versions/<wbr />:versionId/<wbr />redact | [脱敏 Memory Version](/api-reference/managed-agents--memory/脱敏-memory-version) | 抹除该版本中的敏感内容，保留审计轨迹 |
</div>

### Vaults

概念说明见 [凭据管理](/cn/managed-agents/vaults)。

<div className="api-ref-table api-ref-table-longpath">
  | 方法     | 路径                                                                                             | 名称                                                                  | 说明                   |
  | :----- | :--------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ | :------------------- |
  | POST   | /v1/vaults                                                                                     | [创建 Vault](/api-reference/managed-agents--vault/创建-vault)           | 创建凭据集合               |
  | GET    | /v1/vaults                                                                                     | [列出 Vault](/api-reference/managed-agents--vault/列出-vault)           | 列出 Vault             |
  | GET    | /v1/vaults/<wbr />:vaultId                                                                     | [获取 Vault](/api-reference/managed-agents--vault/获取-vault)           | 获取 Vault             |
  | POST   | /v1/vaults/<wbr />:vaultId                                                                     | [更新 Vault](/api-reference/managed-agents--vault/更新-vault)           | 更新展示名或 metadata      |
  | POST   | /v1/vaults/<wbr />:vaultId/<wbr />archive                                                      | [归档 Vault](/api-reference/managed-agents--vault/归档-vault)           | 归档 Vault             |
  | DELETE | /v1/vaults/<wbr />:vaultId                                                                     | [删除 Vault](/api-reference/managed-agents--vault/删除-vault)           | 删除 Vault             |
  | POST   | /v1/vaults/<wbr />:vaultId/<wbr />credentials                                                  | [创建 Credential](/api-reference/managed-agents--vault/创建-credential) | 添加一条凭据               |
  | GET    | /v1/vaults/<wbr />:vaultId/<wbr />credentials                                                  | [列出 Credential](/api-reference/managed-agents--vault/列出-credential) | 列出凭据，不含密钥原文          |
  | GET    | /v1/vaults/<wbr />:vaultId/<wbr />credentials/<wbr />:credentialId                             | [获取 Credential](/api-reference/managed-agents--vault/获取-credential) | 获取凭据元数据              |
  | POST   | /v1/vaults/<wbr />:vaultId/<wbr />credentials/<wbr />:credentialId                             | [更新 Credential](/api-reference/managed-agents--vault/更新-credential) | 轮换 token 等密钥         |
  | POST   | /v1/vaults/<wbr />:vaultId/<wbr />credentials/<wbr />:credentialId/<wbr />mcp\_oauth\_validate | [验证 MCP OAuth](/api-reference/managed-agents--vault/验证-mcp-oauth)   | 探测 MCP OAuth 凭据是否仍有效 |
  | POST   | /v1/vaults/<wbr />:vaultId/<wbr />credentials/<wbr />:credentialId/<wbr />archive              | [归档 Credential](/api-reference/managed-agents--vault/归档-credential) | 归档凭据                 |
  | DELETE | /v1/vaults/<wbr />:vaultId/<wbr />credentials/<wbr />:credentialId                             | [删除 Credential](/api-reference/managed-agents--vault/删除-credential) | 删除凭据                 |
</div>

### Skills

概念说明见 [Skills](/cn/managed-agents/skills)。

<div className="api-ref-table">
  | 方法     | 路径                                            | 名称                                                                        | 说明          |
  | :----- | :-------------------------------------------- | :------------------------------------------------------------------------ | :---------- |
  | POST   | /v1/skills                                    | [创建 Skill](/api-reference/managed-agents--skill/创建-skill)                 | 上传自定义 Skill |
  | GET    | /v1/skills                                    | [列出 Skill](/api-reference/managed-agents--skill/列出-skill)                 | 列出 Skill    |
  | GET    | /v1/skills/:skillId                           | [获取 Skill](/api-reference/managed-agents--skill/获取-skill)                 | 获取 Skill    |
  | DELETE | /v1/skills/:skillId                           | [删除 Skill](/api-reference/managed-agents--skill/删除-skill)                 | 删除 Skill    |
  | POST   | /v1/skills/:skillId/versions                  | [创建 Skill Version](/api-reference/managed-agents--skill/创建-skill-version) | 上传新版本       |
  | GET    | /v1/skills/:skillId/versions                  | [列出 Skill Version](/api-reference/managed-agents--skill/列出-skill-version) | 列出版本        |
  | GET    | /v1/skills/:skillId/versions/:version         | [获取 Skill Version](/api-reference/managed-agents--skill/获取-skill-version) | 获取某个版本      |
  | GET    | /v1/skills/:skillId/versions/:version/content | [下载 Skill ZIP](/api-reference/managed-agents--skill/下载-skill-zip)         | 下载该版本的 ZIP  |
  | DELETE | /v1/skills/:skillId/versions/:version         | [删除 Skill Version](/api-reference/managed-agents--skill/删除-skill-version) | 删除某个版本      |
</div>

### Deployments

概念说明见 [定时任务](/cn/managed-agents/deployments)。

<div className="api-ref-table">
  | 方法   | 路径                                    | 名称                                                                               | 说明             |
  | :--- | :------------------------------------ | :------------------------------------------------------------------------------- | :------------- |
  | POST | /v1/deployments                       | [创建 Deployment](/api-reference/managed-agents--deployment/创建-deployment)         | 创建定时或手动触发的任务   |
  | GET  | /v1/deployments                       | [列出 Deployment](/api-reference/managed-agents--deployment/列出-deployment)         | 列出定时任务         |
  | GET  | /v1/deployments/:deploymentId         | [获取 Deployment](/api-reference/managed-agents--deployment/获取-deployment)         | 获取任务配置         |
  | POST | /v1/deployments/:deploymentId         | [更新 Deployment](/api-reference/managed-agents--deployment/更新-deployment)         | 更新名称、调度或初始事件   |
  | POST | /v1/deployments/:deploymentId/pause   | [暂停 Deployment](/api-reference/managed-agents--deployment/暂停-deployment)         | 暂停定时触发；手动运行仍可用 |
  | POST | /v1/deployments/:deploymentId/unpause | [恢复 Deployment](/api-reference/managed-agents--deployment/恢复-deployment)         | 恢复定时触发         |
  | POST | /v1/deployments/:deploymentId/archive | [归档 Deployment](/api-reference/managed-agents--deployment/归档-deployment)         | 归档后不再触发        |
  | POST | /v1/deployments/:deploymentId/run     | [手动运行 Deployment](/api-reference/managed-agents--deployment/手动运行-deployment)     | 立即触发一次运行       |
  | GET  | /v1/deployment\_runs                  | [列出 Deployment Run](/api-reference/managed-agents--deployment/列出-deployment-run) | 列出运行记录         |
  | GET  | /v1/deployment\_runs/:runId           | [获取 Deployment Run](/api-reference/managed-agents--deployment/获取-deployment-run) | 获取单次运行结果       |
</div>

## 错误处理

错误响应使用统一信封，只包含 HTTP 状态码、**error.type**、**error.message** 与 **request\_id**：

```json theme={null}
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "environment_id: value is required"
  },
  "request_id": "req_xxxxxxxxxxxx"
}
```

<div className="api-error-table">
  | HTTP            | error.type              | 典型场景                                                 |
  | --------------- | ----------------------- | ---------------------------------------------------- |
  | 400 / 422       | invalid\_request\_error | 参数非法、字段不支持、缺少必填字段                                    |
  | 401             | authentication\_error   | 缺少或无法解析凭据                                            |
  | 403             | permission\_error       | 身份可识别但权限不足                                           |
  | 404             | not\_found\_error       | 资源不存在或对调用者不可见                                        |
  | 409             | invalid\_request\_error | 版本冲突、资源状态冲突、唯一键冲突（无独立 conflict 类型，结合状态码与 message 区分） |
  | 413             | request\_too\_large     | 请求体超限                                                |
  | 429             | rate\_limit\_error      | 配额或请求频率超限                                            |
  | 500             | api\_error              | 内部错误                                                 |
  | 504             | timeout\_error          | 请求或上游处理超时                                            |
  | 502 / 503 / 529 | overloaded\_error       | 上游不可用或服务过载                                           |
</div>

建议对 429 与 5xx 做指数退避重试；400 类错误应先修正请求再重试。会话内的异步失败不走 HTTP 错误，而是以 **session.error** 事件送达，见[事件与流式输出](/cn/managed-agents/events)。
