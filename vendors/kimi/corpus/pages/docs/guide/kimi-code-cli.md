> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 在 Kimi Code CLI 中使用 Kimi API Platform

> 使用 Kimi API Platform API Key 接入、切换和更新 Kimi Code CLI。

[Kimi Code](https://www.kimi.com/code/) 是面向开发者的智能编程服务，Kimi Code CLI 是其运行在终端中的 AI Agent。

Kimi Code CLI 可以直接使用在 [Kimi API Platform](https://platform.kimi.com/) 创建的 API Key。

本文介绍如何：

* 使用 `platform.kimi.com` 的 API Key 完成接入
* 将现有 Kimi Code CLI 切换到 Kimi API Platform
* 更换已经配置的 API Key

<Note>
  本文假设你已经安装 Kimi Code CLI。
</Note>

尚未安装时，请参考 [Kimi Code CLI 官方安装方式](https://www.kimi.com/code/docs/kimi-code-cli/guides/getting-started.html)，或选择系统直接运行：

<Tabs>
  <Tab title="macOS / Linux">
    ```bash theme={null}
    curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
    ```
  </Tab>

  <Tab title="Windows (PowerShell)">
    ```powershell theme={null}
    irm https://code.kimi.com/kimi-code/install.ps1 | iex
    ```

    Windows 用户首次启动前还需要安装 [Git for Windows](https://gitforwindows.org/)。Kimi Code CLI 会使用其中的 Git Bash 作为 Shell 环境。如果 Git Bash 安装在非标准路径，请把 `KIMI_SHELL_PATH` 设为 `bash.exe` 的绝对路径。
  </Tab>
</Tabs>

脚本会自动下载最新版本、校验 checksum，并把 `kimi` 可执行文件放到你的 `PATH` 中。

## 准备 API Key

打开 [Kimi API Platform](https://platform.kimi.com/)，登录后进入 [API Keys](https://platform.kimi.com/console/api-keys) 页面，创建并复制一个 API Key。

<Warning>
  请妥善保管 API Key，不要与他人分享，也不要在截图中展示完整内容。
</Warning>

## 接入 Kimi API Platform

### 1. 启动 Kimi Code CLI

进入需要使用 Kimi Code CLI 的项目目录，然后启动：

```bash theme={null}
kimi
```

进入交互界面后，在输入框中执行：

```text theme={null}
/login
```

Kimi Code CLI 将打开平台选择界面。

<img src="https://mintcdn.com/moonshotcn/IUcWR2acXWBSzV7g/assets/pics/kimi-code-cli/login.png?fit=max&auto=format&n=IUcWR2acXWBSzV7g&q=85&s=009f88c770869147baa6c9a8bd44ced7" alt="在 Kimi Code CLI 中输入 /login" width="1440" height="690" data-path="assets/pics/kimi-code-cli/login.png" />

### 2. 选择 API Key 所属平台

在平台列表中，选择与 API Key 来源一致的选项：

| API Key 来源          | 在 Kimi Code CLI 中选择                           |
| ------------------- | --------------------------------------------- |
| `platform.kimi.com` | `Kimi Platform (API key · platform.kimi.com)` |

使用方向键选择平台，然后按 `Enter` 确认。

<Warning>
  必须选择与 API Key 创建站点一致的平台，否则 API Key 校验将失败。
</Warning>

<img src="https://mintcdn.com/moonshotcn/IUcWR2acXWBSzV7g/assets/pics/kimi-code-cli/select-platform.png?fit=max&auto=format&n=IUcWR2acXWBSzV7g&q=85&s=97e409c286f0bb043cfa8caa9c4ee22f" alt="选择 platform.kimi.com 对应的 Kimi Platform" width="1410" height="346" data-path="assets/pics/kimi-code-cli/select-platform.png" />

### 3. 输入 API Key

根据界面提示粘贴刚刚创建的 API Key，然后按 `Enter`。

Kimi Code CLI 会自动校验 API Key，并读取当前账户可用的模型。

<img src="https://mintcdn.com/moonshotcn/IUcWR2acXWBSzV7g/assets/pics/kimi-code-cli/enter-api-key.png?fit=max&auto=format&n=IUcWR2acXWBSzV7g&q=85&s=27a4f28a8b3b2bf9aa6bee859fc72759" alt="输入 Kimi API Platform API Key" width="1406" height="362" data-path="assets/pics/kimi-code-cli/enter-api-key.png" />

### 4. 选择模型

API Key 校验通过后，界面会显示当前账户可用的模型。选择需要使用的模型并确认。

完成后，Kimi Code CLI 会：

* 切换当前会话使用的模型
* 保存本次平台和模型选择
* 在后续启动时继续使用该配置

看到配置完成提示后，即表示 Kimi API Platform 已成功接入。

<img src="https://mintcdn.com/moonshotcn/IUcWR2acXWBSzV7g/assets/pics/kimi-code-cli/select-model.png?fit=max&auto=format&n=IUcWR2acXWBSzV7g&q=85&s=e274222f8aed5a73e4f3077b92f348e1" alt="选择 Kimi API Platform 模型" width="1436" height="526" data-path="assets/pics/kimi-code-cli/select-model.png" />

### 5. 验证接入结果

执行以下命令查看当前会话状态：

```text theme={null}
/status
```

确认当前模型后，再发送一个简单任务，例如：

```text theme={null}
请查看当前项目，并简要说明目录结构。
```

如果 Kimi Code CLI 能够正常返回结果，即表示接入成功。

<img src="https://mintcdn.com/moonshotcn/IUcWR2acXWBSzV7g/assets/pics/kimi-code-cli/configured.png?fit=max&auto=format&n=IUcWR2acXWBSzV7g&q=85&s=a2ce02f66605e57080a151cc735e3146" alt="Kimi Code CLI 使用 Kimi API Platform 正常回复" width="1444" height="476" data-path="assets/pics/kimi-code-cli/configured.png" />

## 切换到 Kimi API Platform API Key

如果 Kimi Code CLI 已经在使用其他登录方式，无需退出程序，也无需手动修改配置。

在当前会话中重新执行：

```text theme={null}
/login
```

然后依次完成：

1. 选择 `Kimi Platform (API key · platform.kimi.com)`
2. 输入 Kimi API Platform API Key
3. 选择需要使用的模型
4. 等待配置完成提示

完成后，当前会话会直接切换到新选择的 Kimi API Platform 模型，不需要重新启动 Kimi Code CLI。

## 更换 API Key

如果需要更换已经配置的 API Key，再次执行 `/login`，选择 `Kimi Platform (API key · platform.kimi.com)` 并输入新的 API Key 即可。

新配置完成后，Kimi Code CLI 将使用新的 API Key。

## 常见问题

### API Key 校验失败

请依次检查：

* 是否选择了 API Key 实际创建所在的平台
* API Key 是否复制完整，是否包含多余空格
* API Key 是否仍然有效
* 对应的 Kimi API Platform 账户是否可以正常调用 API

如果 API Key 已被撤销或泄露，请在 Kimi API Platform 中创建新的 API Key，然后重新执行 `/login`。

### 无法执行 `/login`

`/login` 需要在 Kimi Code CLI 空闲时执行。如果当前正在生成内容或执行任务，请等待任务结束，或先按 `Esc` 或 `Ctrl-C` 中断，再重新执行 `/login`。

### 没有显示可用模型

请确认 API Key 和所选平台一致，然后重新执行 `/login`。如仍然无法加载，可以先升级 Kimi Code CLI，再检查 Kimi API Platform 账户状态。

## 了解更多

* [Kimi Code CLI 开始使用](https://www.kimi.com/code/docs/kimi-code-cli/guides/getting-started.html)
* [Kimi Code CLI 斜杠命令](https://www.kimi.com/code/docs/kimi-code-cli/reference/slash-commands.html)
* [Kimi Code CLI 平台与模型](https://www.kimi.com/code/docs/kimi-code-cli/configuration/providers.html)
* [Kimi Code CLI 配置文件](https://www.kimi.com/code/docs/kimi-code-cli/configuration/config-files.html)
* [Kimi API Platform 快速开始](/docs/get-api-key)
