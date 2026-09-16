> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 列出文件

> 列出当前账户已上传的文件。

<Accordion title="调用示例">
  ```python theme={null}
  file_list = client.files.list()

  for file in file_list.data:
      print(file) # 查看每个文件的信息
  ```
</Accordion>


## OpenAPI

````yaml GET /v1/files
openapi: 3.1.0
info:
  title: Kimi 托管智能体
  version: 2026-09-01-beta
  description: >-
    Kimi 托管智能体的公共 REST API。


    ## 认证


    每个操作都使用 `Authorization: Bearer sk-...` 认证。不要在其他请求头中发送 API 凭据。


    ## 资源标识符


    资源 ID 是不透明字符串。其格式不属于本契约，可能随平台演进变化：客户端应将 ID 作为完整值使用，不要解析其结构，也不要根据其形态做任何推断。


    ## 核心概念


    **智能体（Agent）**是版本化的智能体配置。**会话（Session）**是绑定到冻结智能体版本的一次进行中的对话。会话运行在一个协调者**线程**上，线程可以把工作委托给子线程。线程的每个轮次都会向会话事件流发送事件。

    **凭据库（Vault）**持有项目级凭据，秘密值为只写。**环境（Environment）**描述会话运行所在的云沙箱。**记忆库（Memory
    Store）**是项目级文件存储，挂载进会话。**梦境（Dream）**是平台对一个记忆库执行的记忆维护。

    **触发器（Trigger）**按计划或手动启动会话，每次执行记录为一次
    **TriggerRun**。**产物（Artifact）**是会话交付的可下载文件。**插件（Plugin）**为智能体打包 MCP 服务器与技能。

    **协调者**是会话的主线程，用户输入先到达它。模型提供方操作中的 `provider binding` 指调用方为该提供方配置的接入。


    ## 版本控制


    `kimi-api-version` 请求头选择本次请求使用的 API 版本（`YYYY-MM-DD`，与每个规范修订版的 `info.version`
    对应）。除 `/v1/files*` 外，所有端点都必须携带该请求头：发送 `kimi-api-version: 2026-09-01-beta`
    即可使用本文档所述版本。在 `/v1/files*` 之外未携带请求头，或取值未知时，请求将被拒绝并返回 400
    `invalid_request_error`。在 `/v1/files*` 上该请求头可选，缺省时选择兼容行为：上传与删除返回 200（而非
    201/204），文件记录使用 `status`、`status_details` 字段（而非
    `extract_status`），且上传的文件不能挂载到会话。


    **破坏性变更只会随新的带日期版本发布。** 破坏性变更包括：


    - 删除或重命名端点、字段或枚举值

    - 改变字段的类型或含义

    - 新增必填请求字段或收窄可接受的输入

    - 改变默认行为

    - 删除错误类型或改变其含义


    非破坏性变更（可随时发布；客户端必须容忍）：新端点、新的可选请求字段、新的响应字段或响应头、响应侧枚举中的新值（包括错误类型词汇表）、新的错误类型，以及文档或消息措辞更新。


    带 `-beta` 后缀的版本是预览版：行为仍可能调整、不承诺完全兼容，但调用方可见的变更会在 ChangeLog
    与发布说明中通知。稳定版在其后继版本发布后仍然可用。退役会提前在发布说明中公告，但不承诺固定窗口。版本进入退役状态后，其响应会携带
    `Deprecation: true` 和 `Sunset: <RFC3339 date>` 响应头。Sunset
    日期之后，该退役值会被视为未知值而拒绝。


    ## 幂等


    创建操作（创建资源或触发运行的 `POST` 端点）接受可选的 `Idempotency-Key` 请求头（最长 255 个字符；UUID
    是不错的选择）。第一个请求的响应会保存 24
    小时，作用域限定在你的项目和该端点：用相同的键和相同的请求体重试，会原样重放该响应（状态码和响应体）而不会重新执行。用不同的请求体复用同一个键，或在第一个请求仍在处理中时复用，返回
    409 `conflict_error`。校验失败（400）和服务器错误（5xx）从不会被保存，因此重试这些请求总是安全的。键在 24
    小时后过期，之后被视为新键。


    ## 错误


    所有非 2xx 响应共用一个错误响应 JSON 格式：`{"error": {type, message, request_id,
    param?}}`。每个响应（无论成功还是错误）都携带 `Msh-Request-Id` 响应头，其值与错误体中的 `request_id` 一致。


    `error.type` 是一个包含 10 个值的封闭词汇表——每个值对应一种客户端恢复策略，且各自固定映射到一个 HTTP 状态码：


    | 错误类型 | 状态码 | 含义 → 恢复方式 |

    | --- | --- | --- |

    | `invalid_parameter_error` | 400 | 某个字段未通过校验。`param` 指出该字段——修复字段后重试 |

    | `invalid_request_error` | 400 | 请求本身格式错误（无法解析的请求体、错误的方法、请求体过大、未知的 API
    版本）——修复请求 |

    | `failed_precondition_error` | 400 | 资源当前状态不允许该操作——先改变状态（消息中说明了方法） |

    | `authentication_error` | 401 | 凭据缺失或被拒绝——重新认证 |

    | `permission_denied_error` | 403 | 已认证但无权限——不要重试，检查凭据所属项目与权限 |

    | `resource_not_found_error` | 404 | 资源不存在或不可见——检查 id |

    | `conflict_error` | 409 | 唯一键冲突或并发修改——重命名，或重新加载后重试 |

    | `rate_limit_reached_error` | 429 | 瞬时速率限制——在 `Retry-After` 之后重试 |

    | `exceeded_current_quota_error` | 429 | 配额或预算耗尽——配额或预算增加后再重试 |

    | `server_error` | 500 | 平台内部故障，包括暂时不可用——通用消息。退避（1s → 2s → 4s）后重试 |


    可定位到字段的失败始终是带 `param` 的 `invalid_parameter_error`。无法归咎于单一字段的失败是不带 `param` 的
    `invalid_request_error`。只有 `rate_limit_reached_error` 携带 `Retry-After`。


    嵌入资源内部的错误字段（例如 `TriggerRun.error`）复用同一错误响应 JSON，但其 `type` 是领域专属的分类（例如
    `fire_failed`），不属于上述 10 个值——仅用于展示。客户端必须容忍未知值。


    ## 会话执行错误


    `session_error` 事件报告已创建会话期间发生的失败。它不是 HTTP 错误响应。其 `error_type` 使用独立于 HTTP
    `error.type` 的封闭词表：


    | `error_type` | 含义 → 恢复方式 |

    | --- | --- |

    | `internal_error` | 未归类的平台内部错误——联系支持并提供 request_id |

    | `model_error` | 模型服务出错——按 message 处理或稍后重试 |

    | `model_unavailable` | 当前 Session 的模型路由不可用——重新创建 Session |

    | `rate_limited` | 模型请求被限流——稍后重试 |

    | `engine_overloaded` | 模型引擎暂时过载——稍后重试 |

    | `quota_exceeded` | 模型配额耗尽或账户欠费——充值后发送新消息继续 |

    | `context_length_exceeded` | 对话超出模型上下文窗口——缩短输入或新建 Session |

    | `invalid_request` | 请求被模型拒绝——按 message 修改请求 |

    | `timeout` | 模型请求超时——稍后重试 |

    | `max_steps` | 本轮达到步数上限——发送新消息继续 |

    | `mcp_connection_failed` | MCP 连接或 transport 失败——稍后重试 |

    | `mcp_authentication_failed` | MCP server 拒绝鉴权——到 vault 页面重新连接 |


    这些值标识执行过程中失败的环节，其 message 会给出下一步操作。客户端必须将该事件与 HTTP `error.type` 分开处理。


    ## 分页


    列表操作接受 `page_size`（1–1000，默认 50）和不透明的 `page_token`，返回 `{items,
    next_page_token}`。`next_page_token` 缺失表示已到最后一页。


    ## 速率限制与大小上限


    请求可能受到速率限制。被限流的请求返回 429 `rate_limit_reached_error`，`Retry-After`
    的值是需要等待的秒数。`exceeded_current_quota_error`
    仅表示配额或预算耗尽，不携带该响应头。请求体按路由类别设有上限。超限返回 400 `invalid_request_error`，没有 413：


    | 路由 | 请求体上限 |

    | --- | --- |

    | JSON 端点（下列除外） | 4 MiB |

    | 记忆写入路由 | 28 MiB |

    | `POST /v1/files` | 每个文件 100 MiB |

    | `POST /v1/skills` | 每个 Skill 包 64 MiB |


    ## 事件流（SSE）


    Session 和线程事件流（`GET .../events/stream`）将事件封装为：`event:` = 事件类型，`id:` =
    恢复游标，`data:` = 完整的事件 JSON，并每 30 秒发送一个 `: hb` 心跳。流建立之前发生的失败返回标准错误响应
    JSON。流中途发生的失败以一个携带相同错误响应 JSON 的终止帧 `event: error` 到达，随后流关闭。重连时，以最后收到的帧 `id`
    作为 `cursor`（或使用 `Last-Event-ID` 头）。不可用的游标返回 `invalid_parameter_error` 且
    `param=cursor`：修正它，或从保留的起点重新订阅。如果消息提示游标已过期（其位置已被回收），丢弃已有的部分预览，打开
    `cursor=now` 流并等待控制帧，通过 `GET .../events` 补齐数据，然后继续实时流。


    ## ChangeLog


    本节汇总当前 API 版本发布后的调用方可见变更。


    ### 2026-09-07


    - 资源 ID 字段不再声明 `pattern` 格式约束。ID 历来是不透明字符串（见「资源标识符」一节），而已声明的 pattern
    并未覆盖平台实际签发的全部格式。此前按这些 pattern 校验 ID 的客户端应移除该校验。

    - `GET /v1/environments` 新增 `official_only` 查询参数，用于仅列出平台提供的官方环境。默认值为 false。

    - `SessionErrorPayload` 新增可选的 `mcp_server_name` 字段：`mcp_connection_failed` 与
    `mcp_authentication_failed` 携带受影响 MCP server 的声明名，客户端可直接链接到对应凭据，无需解析
    message。其他错误类型及本次变更前写入的事件不含该字段。

    - `SessionErrorType` 为即将落地的 MCP runtime 错误分类预留 `mcp_connection_failed` 与
    `mcp_authentication_failed` 两个值。会话现在在 MCP server
    初始连接或工具调用阶段失败时发出这两个值（不可达，或明确 401
    经凭据刷新与一次重试仍未恢复）。平台侧刷新失败（网络、锁、DB、回写）只记服务端日志，不发出。

    - 错误响应现在一致遵循文档约定的 `error.type` 与 `error.param` 规则。JSON 类型或校验失败的字段返回
    `invalid_parameter_error`，`param` 携带从请求根开始的完整点路径（如
    `config.networking.type`、`tools.mcp_server_name`）；union 字段的误用（缺失或未知
    discriminator、携带其他 variant 的负载）指向 union 字段自身的路径（如
    `model`、`items.auth`）；请求级错误仍是不带 `param` 的
    `invalid_request_error`。此前部分字段级错误被误报为 `invalid_request_error` 或使用不完整路径。缺少必填
    `data` 字段的 `user.message` 事件与低于契约下限的 `activity.min_changed_sessions`
    现在会被拒绝，不再被接受。


    ### 2026-09-06


    - `listTriggers` 新增 `agent_id` 查询参数，按所属 Agent 筛选触发器。


    ### 2026-09-05


    - `listMemoryStores` 与 `listMemories` 的返回顺序由按创建时间升序改为最新在前。


    - `GET /v1/agents` 新增 `official_only` 查询参数，用于仅列出平台提供的官方智能体。默认值为 false。


    ### 2026-09-04


    - `kimi-api-version` 请求头现在以可选 header 参数的形式在每个操作上显式声明。`/v1/files*`
    之外未携带该请求头将被拒绝并返回 400 `invalid_request_error`；在 `/v1/files*`
    上缺省时选择兼容格式。请求行为不变。

    - 事件流响应现在声明其 `Cache-Control: no-cache` 与 `X-Accel-Buffering: no`
    响应头。这两个响应头一直都会发送，本次仅新增契约声明。

    - 共享 429 响应现在声明 `Retry-After` 响应头，仅当 `error.type` 为
    `rate_limit_reached_error` 时携带。该响应头一直都会发送，本次仅新增契约声明。


    ### 2026-09-03


    - 将 `batch` 用途的文件绑定到会话，现在返回 400 `failed_precondition_error`，而不是 404
    `resource_not_found_error`。`batch` 文件本来就不支持绑定，本次仅变更错误类型。

    - `EnvironmentProxy` 新增可选的 `route_all`：设置后全部出站主机默认经环境代理转发，`hosts`
    可为空名单。平台内部接口仍绕过代理；`limited` 下白名单不再生效，可达性由该代理自行决定。
servers:
  - url: https://api.moonshot.cn
    description: 生产环境
    variables: {}
security:
  - BearerAuth: []
tags:
  - name: 智能体
    description: 管理智能体配置及其版本。
  - name: 会话
    description: 管理会话、线程、资源、消息和事件。
  - name: 文件
    description: 上传、浏览、下载和删除用户文件。
  - name: 产物
    description: 查看已交付的产物，下载指定版本。
  - name: 技能
    description: 管理 Skill 包及不可变版本。
  - name: 环境
    description: 管理执行环境及其配置。
  - name: 凭据库
    description: 管理凭据库、凭据和 OAuth 会话。
  - name: 插件
    description: 列出并查看可用插件。
  - name: 记忆库
    description: 管理记忆库、文件、版本和梦境策略。
  - name: 触发器
    description: 创建、管理和运行 Trigger。
paths:
  /v1/files:
    get:
      tags:
        - 文件
      summary: 列出文件
      description: >-
        列出已上传的文件。不带 `kimi-api-version` 请求头的请求列出整个组织的文件列表；`2026-09-01-beta`
        请求列出项目下的文件。不带 `page_size` 时返回完整列表。通过 `POST /v1/sessions/{id}/resources`
        将文件挂载到会话。
      operationId: listFiles
      parameters:
        - $ref: '#/components/parameters/APIVersionHeader'
        - name: page_size
          in: query
          required: false
          schema:
            type: integer
            format: int32
            minimum: 1
            maximum: 1000
          explode: false
        - name: page_token
          in: query
          required: false
          schema:
            type: string
          explode: false
      responses:
        '200':
          description: 调用方可见的全部已上传文件。
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileMetadataList'
              example:
                items:
                  - id: file_01h455vb4pex5vsknk084sn02q
                    filename: report.txt
                    mime_type: text/plain
                    size_bytes: 14
                    created_at: '2026-08-26T12:00:00Z'
                    purpose: file-extract
                    extract_status: ready
        '401':
          description: 凭据缺失或被拒绝。
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UnauthorizedErrorResponse'
        '429':
          description: 已达速率限制或配额耗尽。
          headers:
            Retry-After:
              required: false
              description: >-
                重试前需要等待的秒数。仅当 `error.type` 为 `rate_limit_reached_error`
                时携带；配额错误不携带该响应头。
              schema:
                type: integer
                format: int32
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequestsErrorResponse'
        default:
          description: 意外的错误响应。
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/APIError'
components:
  parameters:
    APIVersionHeader:
      name: kimi-api-version
      in: header
      required: false
      description: >-
        本次请求使用的 API 版本，格式为 `YYYY-MM-DD`。发送 `2026-09-01-beta`
        即使用本文档所述版本。`/v1/files*` 之外必传：未携带请求头将被拒绝并返回 400 `invalid_request_error`；在
        `/v1/files*` 上缺省时选择兼容行为。所有端点对未知取值均返回 400 `invalid_request_error`。
      schema:
        $ref: '#/components/schemas/APIVersion'
  schemas:
    FileMetadataList:
      type: object
      required:
        - items
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/FileMetadata'
          description: 调用方可见的文件，最新在前。
        next_page_token:
          type: string
          description: 下一页的分页令牌。列表耗尽时缺省。
      description: 调用方可见的已上传文件列表。不带 `page_size` 时端点返回完整列表。
    UnauthorizedErrorResponse:
      type: object
      required:
        - error
      properties:
        error:
          $ref: '#/components/schemas/ErrorObject'
    TooManyRequestsErrorResponse:
      type: object
      required:
        - error
      properties:
        error:
          $ref: '#/components/schemas/ErrorObject'
    APIError:
      type: object
      required:
        - error
      properties:
        error:
          $ref: '#/components/schemas/ErrorObject'
          description: 错误详情。
    APIVersion:
      type: string
      enum:
        - 2026-09-01-beta
      description: 平台当前支持的 API 版本。新的日期版本发布时加入；版本在公告的 Sunset 日期后移除。
    FileMetadata:
      type: object
      required:
        - id
        - filename
        - mime_type
        - size_bytes
        - created_at
        - extract_status
      properties:
        id:
          type: string
          description: 文件 ID。
        filename:
          type: string
          description: 原始文件名（可能带有服务器分配的去重后缀）。
        mime_type:
          type: string
          description: 上传时检测到的 MIME 类型。
        size_bytes:
          type: integer
          format: int64
          description: 文件大小（字节）。
        created_at:
          type: string
          format: date-time
          description: 上传时间戳。
        purpose:
          $ref: '#/components/schemas/FilePurpose'
          description: 处理用途。
        extract_status:
          $ref: '#/components/schemas/FileStatus'
          description: 当前处理状态。
      description: 上传到调用方项目的文件元数据。
    ErrorObject:
      type: object
      required:
        - type
        - message
      properties:
        type:
          $ref: '#/components/schemas/ErrorType'
          description: 来自注册词汇表的机器可读错误类型。
        message:
          type: string
          description: 人类可读的错误消息。
        param:
          type: string
          description: 适用时，为与错误相关的请求参数或请求体字段。在 `invalid_parameter_error` 上始终存在。
        request_id:
          type: string
          description: >-
            服务端分配的请求标识符，用于支持查询。在错误响应上始终存在（与 `Msh-Request-Id`
            头一致），在嵌入资源内部的错误详情中缺省。
      description: 所有 API 版本共用的机器可读错误详情。
    FilePurpose:
      type: string
      enum:
        - file-extract
        - image
        - video
        - batch
      description: >-
        上传文件的处理用途。默认为 `file-extract`。


        - `file-extract`：文档（包括表格和公式）会解析为供模型使用的 Markdown。内容端点返回一个携带解析出的 Markdown
        的 JSON 对象，而非原始上传内容。图片和视频由媒体解析处理，因此其内容端点不可用。

        - `image`/`video`：跳过文档解析。只有检测为图片或视频的文件才会进行媒体处理。图片不做 OCR，内容端点不可用。

        -
        `batch`：上传文件作为批处理输入。内容端点返回上传的文件；文件在上传时经解析规范化，返回的字节可能与原文件不同。只有上传者本人可以读取或删除。该文件不能挂载到会话。
    FileStatus:
      type: string
      enum:
        - ready
        - error
      description: |-
        文件的处理状态。

        - `ready`：文件可按指定用途使用。图片或视频解析失败不会改变此状态。
        - `error`：文档解析失败。文件仍可见、可删除，也可以挂载到新的会话。
    ErrorType:
      type: string
      enum:
        - invalid_parameter_error
        - invalid_request_error
        - failed_precondition_error
        - authentication_error
        - permission_denied_error
        - resource_not_found_error
        - conflict_error
        - rate_limit_reached_error
        - exceeded_current_quota_error
        - server_error
      description: >-
        已注册的机器可读错误类型，每种客户端恢复策略对应一个。该集合对客户端封闭，可穷尽处理，但响应侧保持开放：客户端必须容忍未来新增的取值（新增取值不属于破坏性变更）。
  securitySchemes:
    BearerAuth:
      type: http
      scheme: Bearer

````