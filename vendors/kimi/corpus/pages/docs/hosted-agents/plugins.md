> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 插件

> 在智能体中引用官方插件：浏览插件目录、理解版本固定规则，并在控制台或 API 中完成配置。

插件（Plugin）是托管智能体中 **可复用的能力分发单元**：一个插件由一份清单（manifest）加上可选的捆绑技能（Skill）和可选的远程 MCP 服务组成。把插件挂载到智能体上，就能一次性获得它打包好的工具连接与技能，而不必逐项自行配置。

平台维护一个 **官方插件目录**，目录中的插件由平台统一上架、维护和更新，对所有项目可见。插件是平台级官方资源：你可以浏览、引用，但不能通过 API 修改。

<Note>
  插件使用会单独收费，不同插件的定价说明见 [托管智能体定价](/docs/pricing/hosted-agents)。
</Note>

<Note>
  **插件与 MCP 的关系**：插件中声明的远程 MCP 服务会在运行时展开为普通的 MCP 服务，与智能体自行配置的 `mcp_servers` 走同一条接入链路——包括按凭据库（Vault）注入访问凭据、工具开关过滤等，二者能力一致、互不冲突。详见 [MCP](/docs/hosted-agents/mcp)。
</Note>

## 官方插件目录

插件目录中只展示 **已上架** 的插件。每个插件包含：

| 组成部分          | 说明                          |
| ------------- | --------------------------- |
| 清单（manifest）  | 插件的名称、描述、图标、关键词等元信息         |
| 远程 MCP 服务（可选） | 插件打包的一个或多个 MCP 服务连接，运行时自动接入 |
| 捆绑技能（可选）      | 随插件分发的技能（Skill），运行时自动挂载到云沙箱 |

通过 API 可以列出当前已上架的插件。以下示例中的 API Key 从环境变量 `KIMI_API_KEY` 读取，API 地址从环境变量 `API_BASE_URL` 读取（示例值 `https://api.moonshot.cn`）：

```bash theme={null}
curl ${API_BASE_URL:-https://api.moonshot.cn}/v1/plugins \
  --header "Authorization: Bearer $KIMI_API_KEY" \
  --header "kimi-api-version: 2026-09-01-beta"
```

<Note>
  列表响应是分页结构：插件在 `items` 中返回，响应中的 `next_page_token` 用于翻页。
</Note>

## 在智能体中使用插件

### 官方智能体：开箱即用

平台提供的 **官方智能体**（如 PPT 助手）已经配置好所需插件，无需任何配置——直接用官方智能体创建会话，插件中的 MCP 服务与技能就会在运行时自动生效。在控制台中选择官方智能体创建会话即可开始使用，见 [控制台](/docs/hosted-agents/console)；PPT 助手的配置说明见 [官方 PPT 智能体](/docs/hosted-agents/official-ppt-agent)。

### 自定义智能体：按 ID 引用

自定义智能体通过插件 ID 引用已上架的插件。插件引用（`PluginRef`）**只需给出 `plugin_id`**：平台会在写入智能体版本时，把引用解析为当时的采用版本（见下文「版本固定规则」），冻结结果可见于响应中 `plugins` 列表里对应引用的 `version` 字段。版本由服务端固定，请求中显式指定 `version` 会被拒绝。在控制台的“智能体”页表单中可以直接勾选插件；通过 API 创建或更新智能体时，在插件引用列表中填入插件 ID 即可。

<Tip>
  部分插件打包的远程 MCP 服务需要授权（OAuth）或访问凭据才能使用。这类凭据不保存在智能体配置里，而是通过凭据库（Vault）在运行时注入，配置方式见 [凭据库](/docs/hosted-agents/vaults) 与 [MCP](/docs/hosted-agents/mcp)。
</Tip>

## 版本固定规则

插件的版本由平台与智能体两级固定，开发者一般无需关心版本号：

<Steps>
  <Step title="平台侧采用版本">
    平台为每个插件维护一个「当前采用版本」，由平台统一升级或回退。目录中的插件作者发布的是不可变版本，平台决定何时采用新版本。
  </Step>

  <Step title="智能体版本冻结">
    每次提交智能体新版本时，若请求包含插件引用，平台把每个引用解析为当时的采用版本并冻结进该智能体版本；未包含插件引用的更新沿用上一版本冻结的引用。
  </Step>

  <Step title="会话内不变">
    会话在创建时绑定当时的智能体版本，因此一次会话从开始到结束（包括中断恢复）使用的插件版本始终不变，行为可复现。
  </Step>
</Steps>

平台升级某个插件的采用版本后，**已有智能体不会自动跟着升级**。让智能体用上新版本插件的唯一方式是：对智能体做一次更新并重新提交插件引用（生成新的不可变版本），新版本会冻结当时的最新采用版本。

## 上架与下架

上架状态同时控制「能否引用」和「会话能否生效」：

| 场景       | 行为                                     |
| -------- | -------------------------------------- |
| 引用未上架的插件 | 创建或更新智能体时被拒绝                           |
| 下架后的新建会话 | 跳过该插件（不接入其 MCP 服务、不挂载其技能），跳过不会导致会话创建失败 |
| 下架后的既有会话 | 从下一次唤醒起不再接入该插件；若插件重新上架，下一次唤醒恢复接入       |
| 已有智能体版本  | 版本中冻结的插件引用保持原样，不受上架状态变化影响              |

上架状态不随会话保存，平台在每次唤醒时按当时的上架状态重新判断——这与智能体版本中冻结的插件引用不是同一层行为。

## 在控制台中操作

控制台的 **“插件”** 页是插件目录的浏览入口：

* 浏览全部已上架插件，查看每个插件的名称、描述与其包含的 MCP 服务、技能；
* 为自定义智能体配置插件在 **“智能体”** 页的表单中完成（勾选即可）。

## 下一步

<CardGroup cols={3}>
  <Card title="智能体" icon="robot" href="/docs/hosted-agents/agents">
    创建与更新智能体，为智能体引用插件。
  </Card>

  <Card title="MCP" icon="plug" href="/docs/hosted-agents/mcp">
    了解 MCP 服务的接入与凭据注入。
  </Card>

  <Card title="技能" icon="book" href="/docs/hosted-agents/skills">
    了解技能（Skill）的版本化与挂载方式。
  </Card>

  <Card title="凭据库" icon="key" href="/docs/hosted-agents/vaults">
    管理插件与 MCP 服务所需的访问凭据。
  </Card>

  <Card title="控制台" icon="display" href="/docs/hosted-agents/console">
    不写代码，在控制台中浏览插件目录。
  </Card>
</CardGroup>
