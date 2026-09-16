> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 文件

Files API 覆盖两类用法：**输入**（把材料送进会话给 Agent 读）和**产物**（把 Agent 写出来的结果拿回来）。底层都是同一个 File 对象，差别在来源、沙箱路径和能不能被编目下载。

|      | 输入                                      | 产物                                                       |
| ---- | --------------------------------------- | -------------------------------------------------------- |
| 用途   | 给 Agent 读的材料：表格、文档、附件                   | Agent 做完要交给你的文件：报告、图表、导出结果                               |
| 怎么来  | 你 **POST /v1/files** 上传，再挂到会话           | Agent 写入 **/mnt/session/outputs**，平台自动编目                 |
| 沙箱路径 | **/mnt/session/uploads**，对 Agent **只读** | **/mnt/session/outputs**，**读写**                          |
| 怎么取回 | 你本来就持有源文件                               | **GET /v1/files?scope\_id=\$SESSION\_ID** 列出，再下载 content |

写在 **/workspace** 的中间文件不会被编目，会话结束后无法通过 Files API 取回。需要交给调用方的内容，应写到 outputs。

## 输入：上传并挂载

**POST /v1/files**，multipart 形式：

```bash theme={null}
file=$(curl -sS "$BASE_URL/v1/files" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -F "file=@sales_data.csv;type=text/csv")

FILE_ID=$(jq -r '.id' <<< "$file")
```

```json theme={null}
{
  "type": "file",
  "id": "file_xxxxxxxxxxxx",
  "filename": "sales_data.csv",
  "mime_type": "text/csv",
  "size_bytes": 182044,
  "downloadable": true,
  "created_at": "2026-08-28T08:00:00.000Z"
}
```

约束：单文件默认上限 500 MB；文件名 1–255 字符，不得为 . 或 ..，不得含控制字符及小于号、大于号、冒号、双引号、竖线、问号、星号、斜杠、反斜杠；省略 MIME 类型时按 application/octet-stream 处理；组织总配额默认 500 GB。文件类型不限——任何格式都可以上传，是否能被处理取决于沙箱内的工具。

创建会话时通过 **resources** 数组挂载。文件会出现在 **/mnt/session/uploads** 下，对 Agent **只读**：

```bash theme={null}
curl -sS "$BASE_URL/v1/sessions" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "agent": "$AGENT_ID",
  "environment_id": "$ENVIRONMENT_ID",
  "resources": [
    { "type": "file", "file_id": "$FILE_ID", "mount_path": "/data/sales_data.csv" }
  ]
}
EOF
```

挂载路径规则：

* **mount\_path** 可写相对形式（/data/sales\_data.csv）或完整形式（/mnt/session/uploads/data/sales\_data.csv），都归一化到 uploads 目录下。
* 省略或 null 时默认为 `/mnt/session/uploads/<源 File 的 file_id>`。
* 路径会折叠 . 段与多余斜杠、拒绝 .. 越界，结果 ≤1024 UTF-8 字节；多个 File Resource 的路径之间不得重叠。
* 实际生效路径以响应 **resources\[].mount\_path** 的返回值为准。

一个会话最多挂载 500 个 File Resource。挂载时服务端会把源 File 复制为会话范围（scope）的 File，因此响应中的 **file\_id** 可能与你传入的不同。

会话创建后也可以追加挂载：

```bash theme={null}
curl -sS "$BASE_URL/v1/sessions/$SESSION_ID/resources" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d "{
    \"type\": \"file\",
    \"file_id\": \"$FILE_ID\",
    \"mount_path\": \"/data/extra.csv\"
  }"
```

配套接口：**GET /v1/sessions/:id/resources**（列出，limit 1–1000）、**GET .../resources/:resourceId**（详情）、**DELETE .../resources/:resourceId**（卸载）。File Resource 当前不支持更新（POST 返回 400）；已归档会话不可增删资源。

常见输入：表格与原始数据、需要 Agent 阅读的文档、用户上传的附件。系统提示词里写清挂载路径，例如「输入数据在 /mnt/session/uploads/data/sales\_data.csv」。

## 产物：列出并下载

Agent 把要交给你的文件写入 **/mnt/session/outputs**（读写）。平台会把该目录中的文件编目为会话范围的 File，之后即可列出并下载：

```bash theme={null}
curl -sS "$BASE_URL/v1/files?scope_id=$SESSION_ID" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26"
```

```bash theme={null}
curl -sS -L "$BASE_URL/v1/files/$FILE_ID/content" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -o report.xlsx
```

会话范围的 File 在 list/get 响应中带 **scope** 字段（`{"type": "session", "id": "sess_..."}`）；组织级上传的 File 无 scope。列表分页用 **before\_id** / **after\_id** 游标（互斥），limit 默认 20、最大 1000。

<Tip>
  在系统提示词或用户消息里写明产出路径，例如：「把最终报告保存到 /mnt/session/outputs/report.xlsx」。写在 /workspace 的中间文件不会被编目，下载不到。
</Tip>

常见产物：分析报告、导出表格、图表与文档。等到 **session.status\_idle** 再列出 outputs，避免文件还在写入。

## 文件接口一览

| 接口                            | 说明                                    |
| ----------------------------- | ------------------------------------- |
| POST /v1/files                | 上传文件（multipart），用作输入                  |
| GET /v1/files                 | 列出文件；**scope\_id** 过滤某个会话的产物          |
| GET /v1/files/:fileId         | 获取文件元数据                               |
| GET /v1/files/:fileId/content | 下载文件内容                                |
| DELETE /v1/files/:fileId      | 删除文件（返回 `{id, type: "file_deleted"}`） |

## 下一步

<CardGroup cols={2}>
  <Card title="创建会话" href="/cn/managed-agents/create-session">
    resources 数组的完整字段
  </Card>

  <Card title="预装沙箱环境" href="/cn/managed-agents/sandbox-reference">
    uploads / outputs / workspace 目录契约
  </Card>

  <Card title="最佳实践" href="/cn/managed-agents/examples">
    数据分析场景里如何接输入与产物
  </Card>

  <Card title="本页对应 OpenAPI" href="/cn/managed-agents/api-reference#files">
    File：上传、列出、下载
  </Card>
</CardGroup>
