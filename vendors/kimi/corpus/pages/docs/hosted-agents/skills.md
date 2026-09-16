> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 技能

> 为托管智能体挂载版本化技能包，按需扩展智能体能力。

技能（Skill）是托管智能体中 **基于文件的可复用能力包**：一个 `SKILL.md` 加上若干资源文件（脚本、模板、参考文档等），打包成不可变的版本。把技能挂载到智能体上，模型就能在任务中按照技能说明使用这些能力。

## 什么是技能

每个技能是一个文件包，其中恰好包含一个 `SKILL.md`。`SKILL.md` 的 frontmatter 声明技能的名称与描述，正文是写给模型阅读的使用说明；包内其余文件是技能工作时需要的资源。

```markdown SKILL.md 示例 theme={null}
---
name: pdf-report
description: 读取 PDF 文件并生成结构化摘要报告
---

# PDF 摘要报告

当用户要求分析 PDF 文件时：

1. 运行本目录下的 `extract.py` 提取正文文本；
2. 按「背景 / 要点 / 结论」结构整理摘要；
3. 输出为 Markdown 报告并保存到工作目录。
```

会话运行时，平台会把技能的名称、描述和文件路径注入模型上下文；模型据此决定何时打开 `SKILL.md`，并按说明使用包内资源完成任务。

## 官方技能与自定义技能

技能分为两类，两者使用相同的版本、文件与挂载规则：

|        | 官方技能               | 自定义技能      |
| ------ | ------------------ | ---------- |
| 来源     | 平台官方维护             | 你通过 API 创建 |
| 可见范围   | 已启用的官方技能对所有用户可见    | 仅你的项目成员可见  |
| 归档     | **不允许**（写接口返回 404） | 允许         |
| 被智能体引用 | 可以                 | 项目内成员可以    |

<Note>
  官方技能可读不可改：你可以查看它的 `SKILL.md` 内容并直接引用，但不能更新或归档。如需定制，参照官方技能的内容创建你自己的自定义技能。
</Note>

## 不可变版本与版本冻结

技能与智能体一样采用不可变版本机制，二者配合使用：

* **创建即不可变**：创建技能时生成第一个不可变版本，自定义技能创建后不能再修改内容。
* **智能体冻结精确版本引用**：创建或更新智能体时，技能引用的 `version` 可以省略或填 `"latest"`，服务端会在写入新版本前解析并冻结为 **精确版本引用**。
* **会话冻结智能体版本**：会话在创建时冻结当时的智能体版本，因此一次会话运行期间技能文件不会变化，中断恢复后也继续使用同一版本。
* **修订等于换新**：需要修订技能时，归档旧技能并创建新技能（新技能有新的 ID 和版本线），再更新智能体的引用以生成新的智能体版本。已有的智能体版本和会话继续使用当时冻结的版本，不受影响。

## 挂载到云沙箱

会话启动时，平台把智能体冻结的每个技能版本以 **只读** 方式挂载到云沙箱的固定路径：

```text theme={null}
/mnt/agents/skills/<技能名>/
```

* 每个技能挂载为独立目录，挂载目录名即技能的名称（`SKILL.md` 中声明的 `name`）；
* 文件 **按需读取**，首次访问时才加载，不会一次性全部下载；
* 挂载只读，会话中的任何进程都不能修改技能文件；
* 同一智能体不能重复引用同一个技能；两个技能的名称相同时会占用同一挂载路径，创建或更新智能体会被拒绝。

## 接口一览

| 操作              | 方法与路径                                            |
| --------------- | ------------------------------------------------ |
| 列出技能            | `GET /v1/skills`                                 |
| 获取技能            | `GET /v1/skills/{id}`                            |
| 列出版本历史          | `GET /v1/skills/{id}/versions`                   |
| 获取版本 `SKILL.md` | `GET /v1/skills/{id}/versions/{version}/content` |
| 创建技能            | `POST /v1/skills`                                |
| 归档技能            | `POST /v1/skills/{id}/archive`                   |
| 删除技能            | `DELETE /v1/skills/{id}`                         |

<Note>
  归档和删除只作用于自定义技能，对官方技能调用会返回 404。两者是同一个归档操作的两种写法：返回 204 且无响应体，已归档的技能不能被新的智能体版本引用，已有的精确版本引用继续可用。
</Note>

以下示例从环境变量 `KIMI_API_KEY` 读取 API Key。请求地址默认使用 `https://api.moonshot.cn`。

## 创建自定义技能

创建技能时必须通过 `multipart/form-data` 提交一个必填的 **`file`** part：包含 `SKILL.md` 和资源文件的 `.zip` 或 `.skill` 二进制包。包内必须恰好包含一个 `SKILL.md`，缺失或出现第二个都会导致创建失败（400）。

平台会解析 `SKILL.md` frontmatter 中的 `name` 和 `description`，作为该版本面向模型的元信息。创建成功后返回 `{"skill": Skill, "version": SkillVersion}`，请保存 `skill.id` 用于在智能体中引用。

```bash theme={null}
curl -X POST ${API_BASE_URL:-https://api.moonshot.cn}/v1/skills \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -F "file=@pdf-report.skill"
```

## 修订自定义技能

自定义技能创建后不可修改。需要修订时：归档旧技能，用修订后的技能包创建新技能，再在智能体中更新引用以生成新的智能体版本；已有的智能体版本和会话不受影响。官方技能始终只读，不在本流程中。

## 在智能体中引用技能

创建或更新智能体时，在 `skills` 数组中声明技能引用，`version` 可省略或填 `"latest"`：

```json theme={null}
{
  "skills": [
    { "skill_id": "skill_01h455vb4pex5vsknk084sn02q", "version": "latest" },
    { "skill_id": "skill_01h455vb4pex5vsknk084sn02r", "version": "1" }
  ]
}
```

第一个条目引用上文创建的技能；第二个条目来自另一个已创建的技能，演示把版本固定为 `"1"` 的写法。

以下情况会导致创建或更新智能体被拒绝：

* 引用的技能不可见、已被归档，或指定版本不存在；
* 同一智能体中重复引用同一个 `skill_id`；
* 两个技能的名称相同（挂载路径冲突）。

技能状态只有 `active` 与 `archived` 两种；技能之后被归档（`archived`）时，已建立的精确版本引用不受影响。

## 归档技能

不再维护的自定义技能可以归档。归档后 **新的智能体版本不能再引用它**，但已有的精确版本引用继续可用。

```bash theme={null}
curl -X POST ${API_BASE_URL:-https://api.moonshot.cn}/v1/skills/skill_01h455vb4pex5vsknk084sn02q/archive \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta"
```

## 限制

| 项目            | 上限      |
| ------------- | ------- |
| 上传包大小（`file`） | 64 MiB  |
| 解压后总大小        | 128 MiB |
| 包内文件数         | 256 个   |

## 下一步

<CardGroup cols={3}>
  <Card title="智能体" icon="robot" href="/docs/hosted-agents/agents">
    在智能体配置中引用技能并冻结版本。
  </Card>

  <Card title="会话" icon="message" href="/docs/hosted-agents/sessions">
    用挂载好技能的智能体启动一次任务。
  </Card>

  <Card title="云沙箱参考" icon="box" href="/docs/hosted-agents/sandbox-reference">
    了解沙箱文件系统与挂载路径布局。
  </Card>

  <Card title="工具" icon="wrench" href="/docs/hosted-agents/tools">
    了解内置工具集的配置方式。
  </Card>
</CardGroup>
