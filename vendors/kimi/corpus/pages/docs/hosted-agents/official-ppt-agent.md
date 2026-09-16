> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PPT 生成智能体设计

> 拆解官方 PPT 助手的模型、系统提示词、技能与插件配置，以及如何照同样思路自建产出型智能体。

「做 PPT」是托管智能体最高频的使用场景之一。本页将拆解平台官方智能体 **PPT 助手** 的设计思路。读完本页，你可以照同样的思路，用 API 设计出自己的产出型智能体。

官方配置只是起点，设计者应根据业务需求裁剪，真正可以复用的是设计方法。

| 路径       | 适合谁            | 怎么做                                             |
| -------- | -------------- | ----------------------------------------------- |
| 直接用官方智能体 | 想直接使用          | 在控制台选择 **PPT 助手 (official)**，或通过 API 引用它的智能体 ID |
| 照本文思路自建  | 需要定制模板、口径或插件组合 | 参考下文的设计拆解，创建自己的智能体                              |

<Tip>
  在控制台打开 PPT 助手 的详情页可以直接复制它的智能体 ID，也可以调用 `GET /v1/agents` 在列表中找到名为 `PPT助手` 的条目。官方智能体可读不可改，详见 [智能体](/docs/hosted-agents/agents)。
</Tip>

## 场景与目标

典型诉求是：给一份原始材料（或只给一个题目），让智能体产出一份 **结构完整、风格统一、可以在 Office / WPS 里继续编辑** 的 PPTX 文件。官方 PPT 助手 的设计目标有三条：

* **内容有来源**：有原始材料用原始材料，没原始材料就用内置检索自行收集资料，数据类任务直接调用数据插件取数；
* **产出是真文件**：默认产出原生可编辑的 PPTX（文本框、表格、原生图表），而不是图片贴片或网页截图；
* **交付可被程序取回**：文件写到约定目录，客户端按约定取回，不依赖人工进入沙箱查找。

这三条目标就是后面每个配置选择的出发点。

## 设计思路拆解

官方 PPT 助手 的全部能力来自「模型 + 系统提示词 + 技能 + 插件」的组合，加上平台默认加载的内置工具集，没有声明 `tools` 和 `mcp_servers`。下面逐项回答三个问题：官方怎么配的、为什么这样配、你什么时候该换。

### 模型：长上下文和指令遵循优先

官方选择 `kimi-k3`。PPT 任务需要同时处理原始材料全文、技能说明和排版约束，并严格按技能规范生成文件，因此对模型的长上下文处理、指令遵循和结构化生成能力要求较高。

### 系统提示词：四条可复用的约定

官方配置的系统提示词里有四条核心约定。它们不绑定 PPT 场景，自建任何产出型智能体都可以照搬：

1. **技能二维体系**：技能分两类配合使用——方法类技能（Capability）决定怎么做，如深度调研；产物类技能（Artifact）决定产出什么，如 PPT、文档、表格。任务同时命中两类技能时，先按方法类技能调研规划，再按产物类技能的规范产出；两者冲突时，以产物类技能的技术约束为准。
2. **渐进加载**：不预读全部技能说明，任务命中哪个领域才读取哪个 `SKILL.md`，控制上下文成本。挂载多个技能不用担心上下文被一次性占满。
3. **产出物约定**：产出文件一律写入工作区的 `output/` 目录（沙箱内为 `/mnt/agents/output/`），最终回复用相对路径逐一列出（如 `output/industry_analysis.pptx`）。客户端按这个约定列目录、取文件，与 [文件](/docs/hosted-agents/files) 章的会话文件接口对齐。
4. **沟通策略**：回复只讲产出了什么、放在哪里，不汇报中间用了哪些命令和库。

### 技能：产物类技能决定产出物形态

官方当前挂载 PPT 产出物技能 `ha-slides-pptx`，它定义页面结构、排版规范和 PPTX 生成方式，是「产出真 pptx 而不是整页图片」的保证。自建时按需调整：

* 换产出物就换产物类技能：做 Word 报告挂文档类技能，做数据表挂表格类技能；
* 需要专门方法论就叠加方法类技能，例如深度调研类技能；
* 一般资料收集可以不挂技能——平台的内置检索工具足以覆盖。

技能按 `skill_id` 引用，`version` 填 `"latest"`，服务端会在写入智能体版本时固定为精确版本，详见 [技能](/docs/hosted-agents/skills)。官方智能体挂载的技能会随官方迭代调整，以 `GET /v1/agents` 返回的当前配置为准。

### 插件：数据能力按行业替换

数据类 PPT 的取数能力来自插件。金融是 PPT 的高频场景，官方挂了金融数据插件——同花顺 iFinD 金融数据库（行情、财报、公告）和天眼查（企业工商、股东高管、司法风险）。自建时按行业替换：做哪个行业的 PPT，就挂哪个行业的数据插件，需要几个挂几个。

插件把 MCP 服务和捆绑技能打包分发，在控制台勾选或在创建请求中声明即可生效，不需要逐项配置。部分数据插件需要授权或访问凭据，凭据不保存在智能体配置里，而是通过 [凭据库](/docs/hosted-agents/vaults) 在运行时注入。插件的引用方式和版本固定规则见 [插件](/docs/hosted-agents/plugins)。

### 工具：默认内置工具集已够用

官方智能体没有声明 `tools`，平台会默认加载内置工具集，云沙箱里的文件读写、命令执行、联网检索等能力开箱即用——这正是它不需要声明 `tools` 和 `mcp_servers` 的原因。只有需要平台之外的能力时才考虑接入 MCP 服务，见 [接入 MCP](/docs/hosted-agents/mcp)。

## 起点模板

下面给出一个可运行的最小起点，按上文的系统提示词和技能、插件搭配写成。它不是官方配置的逐字拷贝；官方当前配置以 `GET /v1/agents` 返回为准。

创建智能体：

```bash theme={null}
curl -X POST ${API_BASE_URL:-https://api.moonshot.cn}/v1/agents \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "我的 PPT 助手",
    "model": {"id": "kimi-k3"},
    "system": "你是一个 PPT 制作助手。\n- 没有原始材料时，先用内置检索收集资料，再制作 PPT。\n- 技能文件按需读取，不要一次性加载全部技能说明。\n- 所有产出文件写到工作区的 output/ 目录，最终回复里用相对路径逐一列出（如 output/report.pptx）。\n- 产出所有元素可编辑的 .pptx 文件，不要用图片贴片。\n- 回复只讲产出了什么、放在哪里，不汇报实现细节。",
    "skills": [
      {"skill_id": "ha-slides-pptx", "version": "latest"}
    ],
    "description": "自建 PPT 助手：官方同款配方，可自定义模板与插件"
  }'
```

创建成功后，从响应中保存 `id` 作为 `AGENT_ID`。之后按需调整的字段：

| 字段        | 调整频率  | 怎么调                                                                        |
| --------- | ----- | -------------------------------------------------------------------------- |
| `system`  | 最常改   | 换公司模板、品牌视觉规范、内容口径；上面四条约定建议保留                                               |
| `skills`  | 按产出物改 | 换产物类技能，或叠加方法类技能                                                            |
| `plugins` | 按行业改  | 加入 `{"plugin_id": "<插件 ID>"}`，插件 ID 用 `GET /v1/plugins` 查询，或在控制台智能体表单中直接勾选 |
| `model`   | 一般不动  | `kimi-k3` 已适配长上下文产出任务                                                      |
| 工具集       | 一般不动  | 默认内置工具集已够用，无需声明                                                            |

## 资源准备

* **执行环境**：创建一个通用的云沙箱环境即可，`config` 传 `{"type": "cloud"}` 表示全部使用默认值，详见 [快速开始](/docs/hosted-agents/quickstart)。PPT 生成不需要特殊的依赖或网络配置。
* **原始材料（可选但强烈推荐）**：数据或文字等原始材料先通过 `POST /v1/files` 上传拿到 `file_id`，创建会话时挂载进 `resources`，文件会以只读副本出现在沙箱的 `/mnt/agents/upload/` 下。有原始材料的 PPT 内容质量明显高于一键生成，详见 [文件](/docs/hosted-agents/files)。
* **凭据（可选）**：使用的数据插件需要授权时，提前在凭据库中配置好凭据，运行时自动注入，见 [凭据库](/docs/hosted-agents/vaults)。

## 挂载原始材料调用

[快速开始](/docs/hosted-agents/quickstart) 已经完整走过一遍调用：选智能体、建环境、建会话、订阅事件流、发消息、取文件。这里只补充带原始材料的增量步骤。

先上传原始材料，从响应中保存 `id` 作为 `FILE_ID`。`/v1/files*` 接口通过请求头 `kimi-api-version: 2026-09-01-beta` 选择本文档对应的 API 版本，省略该头时走旧版兼容行为（如上传返回 200 而非 201），请始终携带：

```bash theme={null}
curl ${API_BASE_URL:-https://api.moonshot.cn}/v1/files \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -F "file=@industry_data.xlsx"
```

创建会话时把它挂进 `resources`（没有原始材料就省略 `resources` 字段）：

```bash theme={null}
curl -X POST ${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "'"$AGENT_ID"'",
    "environment_id": "'"$ENVIRONMENT_ID"'",
    "title": "行业分析 PPT",
    "resources": [
      {"type": "file", "file_id": "'"$FILE_ID"'"}
    ]
  }'
```

`AGENT_ID` 是官方 PPT 助手 或自建智能体的 ID，`ENVIRONMENT_ID` 是执行环境 ID。从响应中保存会话 `id` 作为 `SESSION_ID`，然后订阅事件流并下达任务（订阅方式和消息结构见 [快速开始](/docs/hosted-agents/quickstart)）：

```bash theme={null}
curl -X POST ${API_BASE_URL:-https://api.moonshot.cn}/v1/sessions/$SESSION_ID/events \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -H "Content-Type: application/json" \
  -d '{
    "events": [
      {
        "type": "user.message",
        "data": {
          "content": [
            {"type": "text", "text": "基于绑定的行业数据，做一份 12 页的行业分析 PPT：市场格局、产业链、头部公司对比、投资要点，商务简洁风格、深蓝主色，所有元素可编辑的 .pptx。"}
          ]
        }
      }
    ]
  }'
```

会话回到 `idle` 后，智能体交付的成品会登记为 **产物（Artifact）**。先列出该会话的产物，找到生成的 PPTX 并保存它的 `id`：

```bash theme={null}
curl "${API_BASE_URL:-https://api.moonshot.cn}/v1/artifacts?session_id=$SESSION_ID" \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta"
```

再用产物 `id` 下载成品：

```bash theme={null}
curl "${API_BASE_URL:-https://api.moonshot.cn}/v1/artifacts/$ARTIFACT_ID/content" \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "kimi-api-version: 2026-09-01-beta" \
  -o industry_analysis.pptx
```

如果产物列表为空，或需要中间文件，可以浏览会话文件系统：用 `GET /v1/sessions/$SESSION_ID/filesystem` 按 `prefix` 逐层进入子目录，再取文件条目的 `path` 通过 `filesystem/raw` 下载，详见 [文件](/docs/hosted-agents/files)。

<Tip>
  PPT 生成是长任务（含调研时可能跑几分钟到十几分钟）。订阅事件流的连接可能中途断开，用断开前最后一帧 SSE 消息的 `id:` 字段作为 `cursor` 重新订阅即可续读，详见 [事件流](/docs/hosted-agents/event-stream)。
</Tip>

## 运行与观察

事件流是观察任务进展的窗口。一次典型的 PPT 任务里值得关注的信号：

* **`session.status`**：`idle` → `running` 表示任务启动；回到 `idle` 表示本轮完成，可以去取文件了。
* **`agent.thinking`**：能看到智能体的任务拆解——先读原始材料还是先调研、大纲怎么分章、每页放什么。大纲方向不对时，这是最早可以介入纠正的时机（取消会话后重发更明确的需求）。
* **`agent.tool_use` / `agent.tool_result`**：数据类任务里可以看到它调用了哪些数据插件或检索工具、查了什么口径的数据。数据不对时，问题通常出在这一步的数据源选择。
* **`agent.message`**：最终回复会按产出物约定列出 `output/` 下的相对路径。客户端可以解析这份清单，但取成品时建议直接查产物接口（`GET /v1/artifacts?session_id=...`），更稳定。
* **`session.error`**：任务失败时出现，携带错误类型与信息。

## 写清任务描述

PPT 助手的产出质量主要取决于任务描述。以下四条原则按重要性排序。

### 1. 有原始材料就先提供

数据或文字等原始材料先上传、创建会话时挂载进 `resources`，再下达任务。有原始材料的 PPT 内容质量明显高于一键生成。

* 推荐：上传财报 Excel 后说「基于绑定的数据做季度经营分析 PPT」；
* 也可以：不给原始材料只给题目，智能体会用内置检索自行收集资料——覆盖面好，但耗时更长，内容口径不如原始材料贴合。

### 2. 约束只说三件事：页数、风格、受众

其余排版细节交给 PPT 技能的默认规范。约束给得越多，越容易互相打架。

> 示例：「做一份 12 页的新能源行业分析 PPT，商务简洁风格、深蓝主色，给投委会看。」

### 3. 数据类 PPT，直接点名数据源

挂载了数据插件的智能体，任务里写明数据来源即可，不用自己准备数据。

> 示例：「用金融数据插件拉取某公司最近四个季度的财报数据，做一份基本面分析 PPT。」

### 4. 要可编辑，就明确说「可编辑的 .pptx」

> 示例：「所有元素可编辑的 .pptx，不要图片贴片。」

PPT 技能默认产出原生可编辑的 PPTX 元素（文本框、表格、原生图表），但显式说一句能避免个别任务退化成整页图片。

后续在同一会话中要求修改 PPT 时，新版本文件仍会写入 `output/` 目录，重新列目录取回即可。

## 进阶方向

* **批量生产**：多份 PPT 任务各建一个会话并发跑，互不干扰。会话间彼此隔离，产出按会话分别取回。
* **嵌入自有系统**：审批、预览 UI 放在自己的业务看板里，智能体只负责产出 PPTX 文件——你的系统订阅事件流、按 `output/` 约定取文件，最终用户无需感知智能体的存在。
* **自建变体**：从上面的起点模板出发，按字段表裁剪——换系统提示词固定公司模板与口径，换 `skills` 改变产出物形态，换 `plugins` 匹配所在行业的数据源。
* **发布前人工确认**：金融、品宣等对外场景，把人工审核放在自己的系统里——智能体只负责产出 PPTX 文件，你的系统订阅事件流、取回文件后先送人工审核，确认无误再对外发布。

## 下一步

<CardGroup cols={3}>
  <Card title="快速开始" icon="rocket" href="/docs/hosted-agents/quickstart">
    从零走通一次官方 PPT 助手的完整调用。
  </Card>

  <Card title="事件流" icon="bolt" href="/docs/hosted-agents/event-stream">
    订阅、断线续读与增量事件对账。
  </Card>

  <Card title="文件" icon="folder" href="/docs/hosted-agents/files">
    上传原始材料、挂载会话与取回产出文件。
  </Card>
</CardGroup>
