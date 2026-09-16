> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 文件

> 上传文件、在会话中绑定文件，并浏览或下载会话文件。

文件接口有两条任务主线：

1. **让已有文件供会话使用**：上传文件，保存返回的 `file_id`，再在创建会话时绑定，或在会话运行期间添加。
2. **获取会话文件**：列出会话文件，再下载所需文件。

上传文件不会自动绑定到会话。
上传文件通过 `/v1/files` 管理，会话文件通过 `/v1/sessions/{session_id}/filesystem` 浏览和下载。

<Warning>
  `/v1/files*` 接口的响应格式由 `kimi-api-version` 请求头决定：携带 `2026-09-01-beta` 时返回 Hosted Agents 格式（上传成功 201、删除成功 204、`FileMetadata` 响应模型）；不带该头时返回开放平台兼容格式（上传 200、删除 200、`FileObject` 模型），其他非空取值返回 400。两套格式的成功码与字段命名均不一致，客户端应按固定一种格式接入，解析逻辑不能混用。建议每个请求都携带 `kimi-api-version: 2026-09-01-beta`：格式固定，且只有该格式下 `file_` 前缀 ID 的文件才能绑定到会话。
</Warning>

## 上传文件并绑定到会话

### 上传文件

向 `POST /v1/files` 发送 `multipart/form-data` 请求。
`file` 部分必填，文件名可以由 `file` 部分提供，也可以通过 `filename` 表单部分指定。
`purpose` 可指定文件的处理方式：`file-extract`、`image`、`video` 或 `batch`。`purpose=batch` 的文件只能由其上传者读取内容或删除，且不能绑定到会话。
单个文件大小上限为 100 MiB，上传后不能更新。
组织总存储配额默认为 10 GiB。达到配额上限后，新的上传会被拒绝；删除不再使用的文件可以释放配额。

调用 `/v1/files*` 接口时携带 `kimi-api-version: 2026-09-01-beta` 请求头，以使用当前 API 版本。
下面的命令把上传响应中的 `id` 保存到 `FILE_ID`，后续请求都使用这个变量。

```bash theme={null}
UPLOAD_RESPONSE=$(curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/files" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --form "file=@report.pdf" \
  --form "purpose=file-extract")
FILE_ID=$(printf '%s' "$UPLOAD_RESPONSE" | jq -r '.id')
```

成功时返回 HTTP 201 和文件对象。
`FILE_ID` 来自上传响应中的 `id`，可用于后续绑定、查看、读取内容和删除操作。

```json theme={null}
{
  "id": "$FILE_ID",
  "filename": "report.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 204800,
  "created_at": "2026-08-26T12:00:00Z",
  "purpose": "file-extract",
  "extract_status": "ready"
}
```

`extract_status` 表示文件的解析状态：`ready` 表示文件可用，`error` 表示解析失败。
解析失败的文件也可以绑定到会话，但会话只能拿到原始文件，没有解析出的文本。

同一作用域内上传同名文件时，服务端会为文件名添加后缀，以避免文件名冲突。

### 创建会话时绑定文件

创建会话时，在请求体的 `resources` 中加入 `type` 为 `file` 的会话资源对象，并使用上一步保存的 `FILE_ID`。
创建会话的完整请求示例请参阅 [会话文档](/docs/hosted-agents/sessions)。

```json theme={null}
{
  "resources": [
    {
      "type": "file",
      "file_id": "$FILE_ID"
    }
  ]
}
```

### 会话运行期间添加文件

会话创建后，可以通过 `POST /v1/sessions/{session_id}/resources` 添加文件资源。
`SESSION_ID` 来自创建会话响应中的 `id`，详见 [会话文档](/docs/hosted-agents/sessions)。
只有文件资源可以在会话创建后添加，凭据库（Vault）和记忆库（Memory Store）必须在创建会话时绑定。

```bash theme={null}
curl --request POST "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/resources" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --header "Content-Type: application/json" \
  --data '{
    "type": "file",
    "file_id": "'"$FILE_ID"'"
  }'
```

请求成功时返回 HTTP 201 和会话资源对象，其中的 `id` 是该绑定关系的 ID。

<Note>
  只有 `file_` 前缀的文件 ID 才能绑定到会话。从旧开放平台同步过来的旧格式 ID（无 `file_` 前缀）不能绑定，绑定时会返回错误。
</Note>

### 管理上传文件

`GET /v1/files` 的读取范围随版本头分层：携带 `2026-09-01-beta` 时列出当前项目的文件；不带版本头时列出整个组织的文件。
列表按上传时间倒序返回，最新上传的文件排在前面。两种格式都支持 `page_size`（1–1000）与 `page_token` 分页，不带参数时返回完整列表；托管智能体格式用响应中的 `next_page_token` 接续下一页（没有下一页时不返回该字段），模型推理 API 兼容格式用 `has_more` 判断是否还有下一页。
要查看某个会话绑定的上传文件，使用 `GET /v1/sessions/{session_id}/filesystem?prefix=upload/` 列出该会话 `upload/` 目录下的文件。

查看 `FILE_ID` 对应的文件元数据：

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/files/$FILE_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

读取 `FILE_ID` 对应文件的内容。
该接口按 `purpose` 返回内容：`file-extract` 文件返回一个 JSON 对象，解析出的 Markdown 在 `content` 字段中；`batch` 文件返回上传的文件内容，文件在上传时会被解析和规范化，返回的字节可能与原始上传不同。
`image`、`video` 文件和解析失败的文件没有解析内容，请求会返回 400 `failed_precondition_error`。

下面的命令读取 `FILE_ID` 的内容，用 `jq` 把响应 `content` 字段中的 Markdown 写入 `report.md`：

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/files/$FILE_ID/content" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" | jq -r '.content' > report.md
```

删除 `FILE_ID` 对应的上传文件，成功时返回 HTTP 204：

```bash theme={null}
curl --request DELETE "${API_BASE_URL:-https://api.moonshot.cn}/v1/files/$FILE_ID" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

这些命令中的 `FILE_ID` 都来自上传响应。

## 两种响应格式对照

`/v1/files*` 的两种响应格式同时存在：不带 `kimi-api-version` 请求头时按模型推理 API 兼容格式响应，携带 `2026-09-01-beta` 时按托管智能体格式响应。从旧开放平台同步过来的文件与新上传的文件在同一个列表中返回。

| 维度        | 模型推理 API 兼容格式                                              | 托管智能体格式                             |
| --------- | ---------------------------------------------------------- | ----------------------------------- |
| 触发方式      | 不带 `kimi-api-version` 请求头                                  | `kimi-api-version: 2026-09-01-beta` |
| 列表读取范围    | 整个组织                                                       | 调用方项目                               |
| 列表响应结构    | `{object, data, first_id, last_id, has_more}`              | `{items, next_page_token}`          |
| 文件模型      | FileObject                                                 | FileMetadata                        |
| 上传成功码     | 200                                                        | 201                                 |
| 删除成功码     | 200                                                        | 204                                 |
| 分页        | `page_size` / `page_token`，不带参数返回完整列表，`has_more` 判断是否还有下一页 | 同左，用 `next_page_token` 接续下一页        |
| 可绑定会话的 ID | 仅 `file_` 前缀 ID                                            | 同左                                  |

两种格式的文件模型字段对照：

| 模型推理 API（FileObject）        | 托管智能体（FileMetadata）                 | 说明                                               |
| --------------------------- | ----------------------------------- | ------------------------------------------------ |
| `id`                        | `id`                                | 文件 ID，旧平台同步 ID 与 `file_` 前缀 ID 共存                |
| `object`（恒为 `file`）         | —                                   | 托管智能体格式无此字段                                      |
| `bytes`                     | `size_bytes`                        | 文件大小（字节）                                         |
| `created_at`（Unix 秒）        | `created_at`（RFC3339）               | 时间表示不同，解析时注意                                     |
| `filename`                  | `filename`                          | 文件名，项目内重名自动追加序号                                  |
| `file_type`                 | `mime_type`                         | MIME 类型                                          |
| `purpose`                   | `purpose`                           | 用途（`file-extract` / `image` / `video` / `batch`） |
| `status`（`ready` / `error`） | `extract_status`（`ready` / `error`） | 解析状态                                             |
| `status_details`            | —                                   | 失败详情，托管智能体格式不透出                                  |

## 获取会话文件

### 列出会话文件

会话运行期间产生或保存的文件保存在会话下，通过 `GET /v1/sessions/{session_id}/filesystem` 列出。
接口按目录逐层返回内容：省略 `prefix` 时返回根目录，传入目录前缀时返回该目录下的一层文件和目录。

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/filesystem?prefix=output" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

列出会话文件时，接口返回 `SessionFSNode` 条目。

| 字段              | 类型      | 说明                             |
| --------------- | ------- | ------------------------------ |
| `name`          | string  | 文件或目录名，如 `report.txt`、`output` |
| `path`          | string  | 相对会话文件根目录的路径，下载时使用             |
| `is_dir`        | boolean | 是否为目录                          |
| `size_bytes`    | integer | 文件大小，单位为字节，目录为 0               |
| `last_modified` | string  | 最后修改时间，可选                      |

<Note>
  响应一次返回所请求目录的全部直接子项，不分页。
  会话绑定的上传文件位于 `upload/` 目录下，传入 `prefix=upload/` 即可列出。
</Note>

### 下载会话文件

使用列表返回条目的 `path` 调用 `GET /v1/sessions/{session_id}/filesystem/raw` 下载文件。

```bash theme={null}
curl --request GET "${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/filesystem/raw?path=output/report.pptx" \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta" \
  --output report.pptx
```

会话文件不保证完全持久化：智能体结束后仍在运行的后台进程写出的文件可能丢失或不完整，文件列表也可能滞后于最近的写入。需要持久保存、带版本管理的产出时，应通过 `save_artifact` 交付为产物，产物由独立的产物接口管理。

## 下一步

<CardGroup cols={3}>
  <Card title="会话" icon="message" href="/docs/hosted-agents/sessions">
    了解会话的生命周期、创建方式与消息收发。
  </Card>
</CardGroup>
