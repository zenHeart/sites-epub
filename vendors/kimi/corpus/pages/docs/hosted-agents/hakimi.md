> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 通过 hakimi 创建托管智能体

> 下载 hakimi 技能包并安装到 Kimi Code、Codex、Claude Code 等 agent，用自然语言创建托管智能体、配置执行环境并启动第一个会话。

**hakimi** 是使用托管智能体的第三条路径：创建资源不需要手写 API 请求，也不用在控制台里逐项配置。它由 hakimi skill（技能包）和 hakimi CLI 组成——hakimi skill 引导 agent（AI 编程助手）完成查模型、确认配置、创建资源的流程，hakimi CLI 负责调用托管智能体 API。hakimi 不绑定特定的 agent：Kimi Code、Claude Code、Codex 等支持技能包的工具都可以安装使用。

三条入门路径按需选择：

| 路径                                     | 适合谁                      |
| -------------------------------------- | ------------------------ |
| [快速开始](/docs/hosted-agents/quickstart)（API） | 要把托管智能体集成进自己的系统          |
| [控制台](/docs/hosted-agents/console)          | 不写代码，在网页上完成基础配置和体验       |
| 本页（hakimi）                             | 习惯在终端工作，想用 agent 的自然语言驱动 |

本页会演示利用 hakimi 创建一个金融投研助手。

## 开始前准备

* 已安装一个支持技能包（skill）的 agent，例如 Kimi Code、Claude Code 或 Codex；
* 使用 macOS 或 Linux（hakimi CLI 目前没有 Windows 版本）；
* 已在 [Kimi 开放平台](https://platform.kimi.com/console/api-keys) 创建 API Key。

## 安装 hakimi

下载 hakimi 技能包：

```bash theme={null}
curl -fsSL -o hakimi.zip https://ha-static.moonshot.cn/hakimi/v0.0.5/hakimi.zip
```

把压缩包解压到 agent 的用户级技能目录下的 `hakimi` 文件夹中。压缩包内没有顶层目录，需要先创建这个文件夹。以 Kimi Code 为例：

```bash theme={null}
mkdir -p ~/.kimi-code/skills/hakimi
unzip -q hakimi.zip -d ~/.kimi-code/skills/hakimi
```

使用其他 agent 时，把 `~/.kimi-code/skills` 替换为对应的技能目录：

| agent       | 用户级技能目录               |
| ----------- | --------------------- |
| Kimi Code   | `~/.kimi-code/skills` |
| Claude Code | `~/.claude/skills`    |
| Codex       | `~/.agents/skills`    |

更简单的方式是让 agent 自己装，直接发消息：

```text theme={null}
请下载 https://ha-static.moonshot.cn/hakimi/v0.0.5/hakimi.zip 并安装为你的 skill，目录名为 hakimi。
```

安装完成后新开一个会话，agent 就能识别 hakimi skill。首次使用时，hakimi skill 会引导你安装 hakimi CLI：安装脚本从发布地址下载对应平台的二进制文件、校验 SHA256 后安装到 `~/.local/bin`。装好后可以验证：

```bash theme={null}
hakimi version
```

## 配置 API Key

hakimi CLI 的每次调用都需要显式传入 API Key。在终端中设置环境变量：

```bash theme={null}
export KIMI_API_KEY="你的_API_Key"
```

## 创建金融投研助手

在 agent 中直接描述你要的智能体：

```text theme={null}
请创建一个托管智能体，用于金融投研辅助。它需要能够：
- 分析我提供的财报、公告和研究材料；
- 提取关键指标、风险因素和待核实信息；
- 生成结构化的研究初稿，并明确区分事实、推断和不确定信息。

默认只生成分析结果和研究草稿，不执行交易、不发送外部消息。暂时不绑定插件和 MCP 服务。
```

hakimi skill 接到请求后会按固定流程执行：

1. 根据你的描述生成智能体配置——名称、描述、模型和系统提示词，并在创建前完整展示；
2. 等你明确确认后才创建，创建成功后返回智能体 ID 和版本。

展示配置时重点检查系统提示词。hakimi skill 生成的提示词通常类似这样：

```text theme={null}
你是金融投研助手，根据用户提供的研究材料生成可审核的分析结果。
1. 阅读财报、公告和研究材料，提取经营数据、风险因素和关键假设。
2. 区分原文事实、基于事实的推断和无法确认的信息。
3. 按「分析范围、核心结论、关键数据、主要风险、待核实事项」输出结构化初稿。
4. 不编造数据和结论，不把研究草稿表达为投资建议。
```

如果不满意，直接说明要改的地方（比如「再加一条：引用数据时标明来源」），确认无误后再让它创建。创建成功后，保存返回的智能体 ID 和版本。

## 选择或创建执行环境

智能体配置完成后，hakimi skill 会先列出你现有的执行环境，只推荐状态为 `ready` 的候选环境。你可以选择一个复用；如果没有合适的，它会替你新建一个云沙箱环境，配置项全部使用默认值，无需手动干预。

执行环境的镜像是异步构建的，状态从 `building` 变为 `ready` 后才能创建会话；如果创建会话时收到环境未就绪的错误，稍等片刻用原请求重试即可，不要重复创建环境。环境的网络、依赖等更多配置见 [执行环境](/docs/hosted-agents/environments)。

## 创建会话

环境就绪后，hakimi skill 会展示本次会话的完整配置——智能体、版本、执行环境——确认后创建会话并返回会话 ID。

hakimi 只负责创建资源，不会替你发送消息。会话创建成功后，打开 [控制台](/docs/hosted-agents/console) 找到这个会话，就可以开始对话了。

## 故障排查

**agent 没有使用 hakimi skill**：确认解压后的 `SKILL.md` 在技能目录的 `hakimi` 文件夹里，而不是直接放在技能目录下，然后新开一个会话再试。

**找不到 `hakimi` 命令**：hakimi CLI 还没安装，或 `~/.local/bin` 不在 `PATH` 中。让 hakimi skill 引导你安装，或手动执行 `export PATH="$HOME/.local/bin:$PATH"` 后用 `hakimi version` 验证。

**401 / 403**：API Key 无效或没有托管智能体访问权限。检查环境变量是否设置正确、API Key 是否过期，不要把 API Key 粘贴到对话里排查。

**创建会话时报环境未就绪**：环境镜像还在构建。等状态变为 `ready` 后用原配置重试，不要新建另一个环境。

## 下一步

<CardGroup cols={3}>
  <Card title="快速开始" icon="rocket" href="/docs/hosted-agents/quickstart">
    改用 API 跑通同一条入门链路。
  </Card>

  <Card title="智能体" icon="robot" href="/docs/hosted-agents/agents">
    智能体字段、不可变版本与更新规则。
  </Card>

  <Card title="控制台" icon="display" href="/docs/hosted-agents/console">
    在网页上管理资源和继续会话。
  </Card>
</CardGroup>
