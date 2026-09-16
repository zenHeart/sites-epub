> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Skills

Skill 是基于文件系统的可复用资源，为 Agent 提供领域专长：工作流程、上下文和最佳实践，把一个通用 Agent 变成领域专家。每挂载一个 Skill 都会占用少量会话上下文（用于帮助模型理解何时使用它），Agent 会在任务相关时自动调用。

Skill 有两种来源：

* **平台内置 Skill**（type: **zai**）：平台预置、开箱可用。当前两份：**planning**（拆步骤、跟 todo）、**code-review**（按正确性 / 安全 / 清晰度审代码）。列表会随平台更新，以 **GET /v1/skills?source=zai** 为准。
* **自定义 Skill**（type: **custom**）：你自己编写并上传的技能。

## 创建自定义 Skill

一个自定义 Skill 就是一个目录：根下必须有 **SKILL.md**（frontmatter 中的 **description** 不能为空），加上任意配套文件。通过 multipart 上传整个目录，每个文件 part 的字段名就是它的相对路径，所有文件必须位于同一个顶层目录下：

```bash theme={null}
curl -sS -X POST "$BASE_URL/v1/skills" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -F "display_title=Financial Modeling" \
  -F "financial-modeling/SKILL.md=@financial-modeling/SKILL.md" \
  -F "financial-modeling/templates/dcf.xlsx=@financial-modeling/templates/dcf.xlsx"
```

创建成功返回 201 和 Skill 对象。记下 **id**（skill\_ 前缀）与 **latest\_version**，挂载到 Agent 时需要引用：

```json theme={null}
{
  "id": "skill_xxxxxxxxxxxx",
  "type": "skill",
  "display_title": "Financial Modeling",
  "source": "custom",
  "latest_version": "1759264410641129",
  "created_at": "2026-08-03T08:00:00.000Z",
  "updated_at": "2026-08-03T08:00:00.000Z"
}
```

上传约束：

* 所有文件总量 ≤ 20 MB，文件数 ≤ 200（超出的文件 part 会被静默丢弃，不报错）。
* 根目录必须包含 **SKILL.md**，且 frontmatter 含非空 **description**。
* **display\_title** 是可选的 multipart 文本 part，作为展示名持久化。
* 同一账号下不能重复创建相同目录名的 Skill（返回 409 skill\_directory\_conflict）；每个账号有 Skill 总数配额，超出返回 429。

### 版本管理

Skill 的版本是不可变的。要更新一个 Skill，向 **POST /v1/skills/:id/versions** 重新上传完整目录（约束同创建），生成一个新版本；版本号是服务端生成的 epoch 微秒串。相关接口：

| 接口                                     | 说明                                              |          |
| -------------------------------------- | ----------------------------------------------- | -------- |
| POST /v1/skills                        | 创建 Skill 及其首个版本（multipart 上传）                   |          |
| GET /v1/skills                         | 列出可见 Skill（自己的 + 平台内置），支持 \`?source=custom      | zai\` 过滤 |
| GET /v1/skills/:id                     | 获取 Skill                                        |          |
| DELETE /v1/skills/:id                  | 删除 Skill                                        |          |
| POST /v1/skills/:id/versions           | 上传新版本（multipart）                                |          |
| GET /v1/skills/:id/versions            | 列出版本                                            |          |
| GET /v1/skills/:id/versions/:v         | 获取版本元数据（name / description / directory 从上传内容解析） |          |
| GET /v1/skills/:id/versions/:v/content | 下载该版本的 ZIP 包                                    |          |
| DELETE /v1/skills/:id/versions/:v      | 删除版本                                            |          |

## 把 Skill 挂载到 Agent

创建 Agent 时通过 **skills** 数组挂载，单个 Agent 最多 20 个 Skill。每个条目的字段：

| 字段            | 说明                                        |
| ------------- | ----------------------------------------- |
| **type**      | 必填。**zai**（平台内置）或 **custom**（自己上传）。       |
| **skill\_id** | 必填。Skill 标识；自定义 Skill 用创建时返回的 skill\_ ID。 |
| **version**   | 必填。要固定的版本号（如创建响应中的 latest\_version 值）。    |

```bash theme={null}
agent=$(curl -sS "$BASE_URL/v1/agents" \
  -H "Authorization: Bearer $ZHIPUAI_API_KEY" \
  -H "zai-version: 2026-05-26" \
  -H "zai-beta: managed-agents-2026-05-26" \
  -H "content-type: application/json" \
  -d @- <<'EOF'
{
  "name": "Financial Analyst",
  "model": "glm-5.3",
  "system": "You are a financial analysis agent.",
  "tools": [{"type": "agent_toolset_20260601"}],
  "skills": [
    {"type": "custom", "skill_id": "skill_xxxxxxxxxxxx", "version": "1759264410641129"}
  ]
}
EOF
)
```

<Tip>
  挂载的 Skill 越多，会话沙箱的启动时间越长。只挂载当前任务需要的 Skill。会话运行时，Skill 内容以文件形式挂载在沙箱的 **/mnt/skills** 目录下，Agent 按需读取。
</Tip>

同一账号下自定义 Skill 的目录名不能重复，冲突时返回 **409 skill\_directory\_conflict**。平台内置 Skill 的 **skill\_id** 就是名称（如 `planning`），用 **GET /v1/skills?source=zai** 取 **latest\_version** 后再挂载。

Skill 也可以在创建会话时通过 **agent.skills** 覆盖，只影响该会话，见[创建会话](/cn/managed-agents/create-session)。

## 编写 Skill 的建议

* **SKILL.md 是入口**：frontmatter 写清 name 与 description（模型靠它判断何时使用），正文写工作流程与规范；大块参考资料放在子文件里，让模型按需读取，避免一次性占用上下文。
* **一个 Skill 解决一类任务**：范围过宽的 Skill 会稀释触发信号；按领域拆分成多个 Skill 更有效。
* **附带可执行资产**：模板、脚本、示例文件都可以放进目录，Agent 能在沙箱里直接使用它们。

## 下一步

<CardGroup cols={2}>
  <Card title="定义 Agent" href="/cn/managed-agents/agent-setup">
    skills 数组的完整更新语义
  </Card>

  <Card title="创建会话" href="/cn/managed-agents/create-session">
    按会话覆盖 Skill 配置
  </Card>

  <Card title="本页对应 OpenAPI" href="/cn/managed-agents/api-reference#skills">
    Skill：创建、版本、下载
  </Card>
</CardGroup>
