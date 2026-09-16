> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 在 Codex 中使用 Kimi K3

> 通过 Kimi Responses API 将 Codex 直连 Kimi K3：配置 API Key、编辑 `~/.codex/config.toml`，并分别在桌面端与 CLI 中验证连接。

Kimi 开放平台原生支持 Codex 使用的 [Responses API](/docs/api/responses)，因此 Codex 可以直接使用 `kimi-k3` 模型，无需协议转换或本地代理。

<Note>
  Codex CLI 目前支持文本和图片输入，但尚未提供原生视频输入通道，无法将视频文件直接作为多模态输入提交给模型。这是 Codex CLI 输入层的限制，并非 Kimi K3 模型的能力限制——Kimi K3 API 原生支持视频输入，按 [视觉输入](/docs/guide/use-kimi-vision-model) 直接调用 `kimi-k3` 即可进行完整的视频理解，无需手动抽帧。
</Note>

## 准备工作

开始前，请完成以下准备工作。安装和账号相关操作请按照对应的官方指引完成，本文不再展开。

<CardGroup cols={2}>
  <Card title="安装 Codex CLI" icon="terminal" href="https://developers.openai.com/codex/cli">
    按照 Codex 官方文档完成安装，并至少启动一次 Codex CLI。
  </Card>

  <Card title="创建 API Key" icon="key" href="https://platform.kimi.com/console/api-keys">
    在 Kimi 开放平台创建并保存 API Key。
  </Card>
</CardGroup>

## 第一步：配置 API Key

Codex 通过环境变量读取 API Key，请不要把 Key 写进 `config.toml`。为避免 Key 被记入命令历史，请按以下方式输入：

<Tabs>
  <Tab title="macOS / Linux">
    ```bash theme={null}
    echo "请粘贴你的 Kimi API Key，然后按 Enter（输入内容不会显示）："
    read -s KIMI_API_KEY
    export KIMI_API_KEY
    ```

    该方式只对当前终端会话生效；如需长期保存，可将 `export` 命令写入 `~/.zshrc`（文件为明文，请注意权限）。
  </Tab>

  <Tab title="Windows (PowerShell)">
    ```powershell theme={null}
    $env:KIMI_API_KEY="YOUR_KIMI_API_KEY"
    ```

    如需长期保存，请在 **设置 > 系统 > 关于 > 高级系统设置 > 环境变量** 中添加 `KIMI_API_KEY`。
  </Tab>
</Tabs>

## 第二步：将 Kimi 添加为模型供应商

打开 `~/.codex/config.toml`（Windows 上为 `%USERPROFILE%\.codex\config.toml`），添加以下配置。如果 `model` 或 `model_provider` 已存在，请替换其值：

```toml theme={null}
model = "kimi-k3"
model_provider = "kimi"
model_context_window = 1048576

[model_providers.kimi]
name = "Kimi"
base_url = "https://api.moonshot.cn/v1"
env_key = "KIMI_API_KEY"
wire_api = "responses"
```

| 配置项                              | 类型        | 作用                                                    |
| -------------------------------- | --------- | ----------------------------------------------------- |
| `wire_api = "responses"`         | `string`  | 通过原生 Responses API 与 Kimi 通信，这是实现直连的关键配置              |
| `env_key = "KIMI_API_KEY"`       | `string`  | Codex 读取 API Key 的环境变量名                               |
| `model_context_window = 1048576` | `integer` | 与 `kimi-k3` 的 1M 上下文窗口对齐；不配置时 Codex 会使用默认模型元数据，可能影响表现 |

## 在 Codex Desktop（桌面端）中使用

完成前面的 API Key 和供应商配置后，退出并重新启动 Desktop，使其重新读取 `~/.codex/config.toml`。

启动 Desktop 后，打开模型选择器并选择 `kimi-k3`。此时界面可能会显示 **自定义**，但实际请求仍然使用你配置的 `kimi-k3`。

<img src="https://mintcdn.com/moonshotcn/-QDiBAqEH852pCbj/assets/pics/codex-kimi/desktop-custom-provider.png?fit=max&auto=format&n=-QDiBAqEH852pCbj&q=85&s=19159aaf52d892908cefd1a30de3aaba" alt="Desktop 模型状态区显示「自定义」" width="1140" height="498" data-path="assets/pics/codex-kimi/desktop-custom-provider.png" />

发送一个简单请求：

```text theme={null}
你是谁
```

能正常收到回复，说明基本连接已经建立。接着发送一个会触发 Codex Agent 能力的任务：

```text theme={null}
检查这个仓库并总结它的结构。
```

如果 Desktop 能在工具结果返回后继续生成最终回答，说明模型调用与工具调用均已正常工作：

<img src="https://mintcdn.com/moonshotcn/-QDiBAqEH852pCbj/assets/pics/codex-kimi/desktop-kimi-agent.png?fit=max&auto=format&n=-QDiBAqEH852pCbj&q=85&s=d5ea0248143aeafe61a3463b0662a18b" alt="Desktop 中 Kimi 完成仓库检查并返回结构总结" width="1140" height="996" data-path="assets/pics/codex-kimi/desktop-kimi-agent.png" />

## 在 Codex CLI 中使用

Codex CLI 与 Desktop 共用同一份用户级配置，前面的配置对它同样生效。进入需要使用的项目目录，启动 Codex（如果 Codex CLI 已经在运行，请先退出当前会话，以便重新加载配置）：

```bash theme={null}
cd /path/to/your/project
codex
```

启动后，先确认 Codex CLI 显示的当前模型为 `kimi-k3`：

<img src="https://mintcdn.com/moonshotcn/-QDiBAqEH852pCbj/assets/pics/codex-kimi/verify-codex-cli.png?fit=max&auto=format&n=-QDiBAqEH852pCbj&q=85&s=13fd13cb3a6ca0da2a631c3ad53a26ee" alt="在 Codex CLI 中确认当前模型为 kimi-k3" width="1140" height="291" data-path="assets/pics/codex-kimi/verify-codex-cli.png" />

发送一个简单请求（例如 `你好`），能正常收到回复即说明 Codex 已成功连接 Kimi Responses API。

在底层，Codex 会将请求发送到 `POST https://api.moonshot.cn/v1/responses`。请求与响应的协议细节请参阅 [Responses API 参考](/docs/api/responses)。

## 常见问题

<AccordionGroup>
  <Accordion title="401 Unauthorized">
    API Key 无效，或 Key 与 base\_url 分属不同平台——在 [platform.kimi.com](https://platform.kimi.com) 创建的 Key 只能用于 `https://api.moonshot.cn/v1`。同时确认 `KIMI_API_KEY` 已配置在启动 Codex 或 Desktop 的环境中；对于 CLI，可以在启动 Codex 的终端中执行 `test -n "$KIMI_API_KEY" && echo set || echo missing` 检查。
  </Accordion>

  <Accordion title="400 web_search.search_context_size is not supported">
    请求中包含了暂不受支持的 `search_context_size` 参数，移除即可。Codex 默认发送的请求不包含该参数，内置的 web\_search 工具开箱即用。
  </Accordion>

  <Accordion title="404 /v1/responses">
    base\_url 填写有误——请确认其值恰好为 `https://api.moonshot.cn/v1`（带 /v1 后缀）。如果之前通过 CC Switch 等本地路由接入，还要确认 base\_url 不再指向 `http://127.0.0.1:...` 之类的本地地址。
  </Accordion>

  <Accordion title="429 Rate Limit">
    触发了速率或并发限制。各档位的配额请参阅 [速率限制](/docs/pricing/limits)。
  </Accordion>

  <Accordion title="警告 Model metadata for kimi-k3 not found">
    kimi-k3 不在 Codex 内置的模型目录中，该警告属于预期现象，不影响使用；第二步的 `model_context_window = 1048576` 已确保上下文窗口按 1M 计算。
  </Accordion>

  <Accordion title="配置修改不生效">
    Codex 只在启动时读取 config.toml，请退出后重新启动；同时确认修改的是 `~/.codex/config.toml` 本身，且没有被 `-c` 参数或 profile 覆盖。如果之前通过 CC Switch 接入，还需在其 **设置 > 路由** 中关闭 Codex，否则它会持续改写 config.toml，覆盖新配置。
  </Accordion>

  <Accordion title="其他 HTTP 错误">
    各状态码的含义请参阅 [错误码](/docs/api/errors)。
  </Accordion>
</AccordionGroup>
