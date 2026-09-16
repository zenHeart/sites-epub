> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 一键安装向导

想在 Claude Code、Codex 或 OpenCode 里使用 MiniMax，不必先弄清每个工具把配置放在哪里。运行一键安装向导，选择你常用的工具和服务区域，向导会验证 API Key、补齐缺少的兼容工具，再把 MiniMax M3 配好。

目前支持以下 AI 编程工具：

* **Claude Code**
* **Codex CLI**
* **OpenCode**
* **Grok CLI**
* **Hermes Agent**
* **Pi**

## 开始之前

请确认已经准备好：

* Node.js 18 或更高版本，并且终端可以运行 `npx`
* 可用的 MiniMax API Key
* 可以访问 npm、MiniMax 服务和工具官方安装源的网络

<Accordion title="如何安装 Node.js">
  访问 [Node.js 官网](https://nodejs.org/zh-cn/download)，下载并安装当前的 LTS 版本。

  安装完成后，重新打开终端并运行：

  ```bash theme={null}
  node --version
  npx --version
  ```

  两条命令都能显示版本号，即表示安装成功。
</Accordion>

## 把 MiniMax 带进你的编程工具

<Steps>
  <Step title="准备 API Key">
    * [获取 Token Plan 订阅 Key](https://platform.minimax.cn/user-center/payment/token-plan)
    * [获取按量计费 API Key](https://platform.minimax.cn/user-center/basic-information/interface-key)

    <Note>
      Token Plan Key（`sk-cp-...`）和按量计费 API Key（`sk-api-...`）使用不同额度。向导支持两种 Key，并会询问 Key 类型。
    </Note>
  </Step>

  <Step title="让向导接手配置">
    ```bash theme={null}
    npx -y mmx-cli@latest agent setup
    ```

    先选择要使用的工具。如果选中的工具未在 `PATH` 中检测到，向导会显示第二个多选列表，让你决定安装哪些工具。随后选择服务区域和 API Key 类型，再粘贴 Key。

    确认后，向导会先验证 Key，再显示并执行官方软件包或安装脚本。安装完成后，它会先检查工具，再写入 MiniMax 配置。安装失败时，你可以选择跳过安装并继续配置。
  </Step>

  <Step title="回到熟悉的工作流">
    配置成功后，启动所选工具，例如 `claude`、`codex` 或 `opencode`。MiniMax M3 已经成为默认模型。
  </Step>
</Steps>

自动安装支持 macOS、Linux 和 Windows。除 Pi 外，当前仅支持 arm64 和 x64 架构。

<Accordion title="查看安装来源与命令">
  <Tabs sync={false}>
    <Tab title="macOS / Linux">
      **Claude Code**

      ```bash theme={null}
      curl -fsSL https://claude.ai/install.sh | bash
      ```

      **Codex CLI**

      ```bash theme={null}
      npm install -g @openai/codex
      ```

      **Grok CLI**

      ```bash theme={null}
      curl -fsSL https://x.ai/cli/install.sh | bash
      ```

      **OpenCode**

      ```bash theme={null}
      npm install -g opencode-ai
      ```

      **Pi**

      ```bash theme={null}
      npm install -g --ignore-scripts --engine-strict @earendil-works/pi-coding-agent
      ```

      Hermes Agent 使用[官方安装脚本](https://hermes-agent.nousresearch.com/install.sh)的非交互核心 CLI 阶段，不运行 `setup`、`gateway` 等可选流程。
    </Tab>

    <Tab title="Windows">
      **Claude Code**

      ```powershell theme={null}
      irm https://claude.ai/install.ps1 | iex
      ```

      **Codex CLI**

      ```powershell theme={null}
      npm install -g @openai/codex
      ```

      **Grok CLI**

      ```powershell theme={null}
      irm https://x.ai/cli/install.ps1 | iex
      ```

      **OpenCode**

      ```powershell theme={null}
      npm install -g opencode-ai
      ```

      **Pi**

      ```powershell theme={null}
      npm install -g --ignore-scripts --engine-strict @earendil-works/pi-coding-agent
      ```

      Hermes Agent 使用[官方 PowerShell 安装脚本](https://hermes-agent.nousresearch.com/install.ps1)的非交互核心 CLI 阶段，并跳过 Computer Use 和其他可选流程。
    </Tab>
  </Tabs>
</Accordion>

## 让脚本也能完成配置

在上面的 npx 命令后传入选项，就会进入非交互模式。非交互模式只写配置，不安装工具。此时必须指定工具、API Key 和服务区域：

```bash theme={null}
npx -y mmx-cli@latest agent setup \
  --agent claude-code \
  --agent codex \
  --api-key "$MINIMAX_API_KEY" \
  --region cn
```

一次配置全部受支持的工具：

```bash theme={null}
npx -y mmx-cli@latest agent setup \
  --all \
  --api-key "$MINIMAX_API_KEY" \
  --region cn
```

先预览将要修改的文件：

```bash theme={null}
npx -y mmx-cli@latest agent setup \
  --agent codex \
  --api-key "$MINIMAX_API_KEY" \
  --region cn \
  --dry-run
```

`--dry-run` 不会联网、安装工具或写入文件。

| 选项                    | 说明                    |
| --------------------- | --------------------- |
| `--agent <name>`      | 选择一个工具，可重复使用          |
| `--all`               | 选择全部受支持的工具            |
| `--api-key <key>`     | MiniMax API Key       |
| `--region cn\|global` | 国内或海外服务区域             |
| `--model <model>`     | 默认模型，默认为 `MiniMax-M3` |
| `--dry-run`           | 只预览，不验证 Key、不写入文件     |
| `--output json`       | 输出适合脚本处理的 JSON        |

可选模型包括 `MiniMax-M3`、`MiniMax-M2.7` 和 `MiniMax-M2.7-highspeed`。

## 看看向导改了哪些文件

<Accordion title="查看各工具的配置文件">
  | 工具           | 配置文件                                                     |
  | ------------ | -------------------------------------------------------- |
  | Claude Code  | `~/.claude/settings.json`                                |
  | Codex        | `~/.codex/config.toml`、`~/.codex/mmx-model-catalog.json` |
  | Grok CLI     | `~/.grok/config.toml`                                    |
  | OpenCode     | `~/.config/opencode/opencode.json` 或 `opencode.jsonc`    |
  | Hermes Agent | `~/.hermes/config.yaml`、`~/.hermes/.env`                 |
  | Pi           | `~/.pi/agent/models.json`、`~/.pi/agent/settings.json`    |
</Accordion>

写入配置时，向导会：

* 保留文件中与 MiniMax 无关的设置
* 修改已有文件前创建带时间戳的 `.bak` 备份
* 将配置文件设为仅当前用户可读写（Windows 除外）
* 任一步骤失败时恢复本次已经修改的文件

<Info>
  配置会更新选中工具的 MiniMax Provider，并将默认模型设为你选择的模型。已有的其他 Provider 和无关设置会保留。
</Info>

## 遇到问题，先看这里

<AccordionGroup>
  <Accordion title="找不到 agent setup 命令">
    请确认已经安装 Node.js 18 或更高版本，然后重新运行 `npx -y mmx-cli@latest agent setup`。如果使用的是本地 `mmx` 命令，版本过旧时也可以改用这条 npx 命令。
  </Accordion>

  <Accordion title="工具显示 not detected on PATH">
    向导没有在当前终端的 `PATH` 中找到工具。交互式流程会继续检查安装条件，并询问是否安装符合条件的工具。
  </Accordion>

  <Accordion title="没有出现安装选项">
    工具已经安装、当前调用是非交互模式，或当前环境不满足自动安装要求时，都不会出现安装多选列表。向导会列出缺少的命令或不支持的系统架构；Pi 还要求 Node.js 22.19 或更高版本。
  </Accordion>

  <Accordion title="安装失败">
    向导会显示实际执行的命令和错误信息。Codex、OpenCode 或 Pi 遇到 npm 权限错误时，可参考 [npm 官方说明](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally)。你也可以跳过安装，继续写入配置。
  </Accordion>

  <Accordion title="配置后仍然连接到其他服务">
    检查当前终端是否设置了会覆盖配置文件的环境变量。例如 Claude Code 的 `ANTHROPIC_AUTH_TOKEN`、`ANTHROPIC_BASE_URL`，以及 Grok CLI 的 `OPENAI_API_KEY`、`OPENAI_BASE_URL`。
  </Accordion>

  <Accordion title="Codex 已经使用自定义模型目录">
    如果 `~/.codex/config.toml` 已将 `model_catalog_json` 指向自定义文件，一键配置向导会停止且不修改文件。你可以保留现有目录并按 [Codex 手动配置](/docs/token-plan/codex) 操作，或移除该设置后重试。
  </Accordion>
</AccordionGroup>
