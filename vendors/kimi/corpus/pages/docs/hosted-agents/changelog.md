> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 更新日志

> 托管智能体 API 的调用方可见变更记录：新增能力、行为变更与契约声明更新。

本页汇总托管智能体 API 当前版本发布后的调用方可见变更，与 OpenAPI 规范中的 ChangeLog 保持一致。

**破坏性变更只会随新的带日期版本发布。** 以下条目均为当前版本内的非破坏性变更，客户端应能容忍新端点、新的可选请求字段、新的响应字段与响应头、响应侧枚举新值。

## 2026-09-07

* 资源 ID 字段不再声明 `pattern` 格式约束。ID 历来是不透明字符串，已声明的 pattern 并未覆盖平台实际签发的全部格式。此前按这些 pattern 校验 ID 的客户端应移除该校验。
* `GET /v1/environments` 新增 `official_only` 查询参数，用于仅列出平台提供的官方环境。默认值为 false。
* `SessionErrorPayload` 新增可选的 `mcp_server_name` 字段：`mcp_connection_failed` 与 `mcp_authentication_failed` 携带受影响 MCP server 的声明名，客户端可直接链接到对应凭据，无需解析 message。其他错误类型及本次变更前写入的事件不含该字段。
* `SessionErrorType` 为即将落地的 MCP runtime 错误分类预留 `mcp_connection_failed` 与 `mcp_authentication_failed` 两个值。会话现在在 MCP server 初始连接或工具调用阶段失败时发出这两个值（不可达，或明确 401 经凭据刷新与一次重试仍未恢复）。平台侧刷新失败（网络、锁、DB、回写）只记服务端日志，不发出。
* 错误响应现在一致遵循文档约定的 `error.type` 与 `error.param` 规则。JSON 类型或校验失败的字段返回 `invalid_parameter_error`，`param` 携带从请求根开始的完整点路径（如 `config.networking.type`、`tools.mcp_server_name`）；union 字段的误用（缺失或未知 discriminator、携带其他 variant 的负载）指向 union 字段自身的路径（如 `model`、`items.auth`）；请求级错误仍是不带 `param` 的 `invalid_request_error`。此前部分字段级错误被误报为 `invalid_request_error` 或使用不完整路径。缺少必填 `data` 字段的 `user.message` 事件与低于契约下限的 `activity.min_changed_sessions` 现在会被拒绝，不再被接受。

## 2026-09-06

* `listTriggers` 新增 `agent_id` 查询参数，按所属 Agent 筛选触发器。

## 2026-09-05

* `listMemoryStores` 与 `listMemories` 的返回顺序由按创建时间升序改为最新在前。
* `GET /v1/agents` 新增 `official_only` 查询参数，用于仅列出平台提供的官方智能体。默认值为 false。

## 2026-09-04

* `kimi-api-version` 请求头现在以可选 header 参数的形式在每个操作上显式声明。`/v1/files*` 之外未携带该请求头将被拒绝并返回 400 `invalid_request_error`；在 `/v1/files*` 上缺省时选择兼容格式。请求行为不变。
* 事件流响应现在声明其 `Cache-Control: no-cache` 与 `X-Accel-Buffering: no` 响应头。这两个响应头一直都会发送，本次仅新增契约声明。
* 共享 429 响应现在声明 `Retry-After` 响应头，仅当 `error.type` 为 `rate_limit_reached_error` 时携带。该响应头一直都会发送，本次仅新增契约声明。

## 2026-09-03

* 将 `batch` 用途的文件绑定到会话，现在返回 400 `failed_precondition_error`，而不是 404 `resource_not_found_error`。`batch` 文件本来就不支持绑定，本次仅变更错误类型。
* `EnvironmentProxy` 新增可选的 `route_all`：设置后全部出站主机默认经环境代理转发，`hosts` 可为空名单。平台内部接口仍绕过代理；`limited` 下白名单不再生效，可达性由该代理自行决定。
