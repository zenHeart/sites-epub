> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 在 OpenClaw 中连接 Kimi

> 使用 OpenClaw 和 Kimi API 构建跨平台 AI 智能体。按照指南安装 OpenClaw 并配置 Kimi API 密钥。

OpenClaw（前身为 Clawdbot 和 Moltbot）是一个开源的自托管 AI 智能体平台，可让您在本地运行 AI 助手。它集成了 WhatsApp、Telegram、Discord、Slack 和 Signal 等消息应用，将大语言模型连接到实际工作流程中。该平台支持多个 LLM 提供商、可扩展的技能，并让您完全掌控自己的数据和 API 密钥。

以下步骤基于 OpenClaw `2026.7.1` 和官方 Moonshot Provider，使用 Kimi K3 完成 Chat Completion 配置。旧版 K2.5 预设已随 `kimi-k2.5` 下线，不再作为本文的配置目标。

<Warning>
  `kimi-k2.5` 已于 2026 年 8 月 31 日全平台下线。新用户请使用官方 Moonshot Provider，并将 `moonshot/kimi-k3` 设置为默认模型。API Key 只在本机向导或终端中输入，不要写入文档、截图、仓库或聊天记录。
</Warning>

## 准备工作

开始前，请完成以下准备工作。安装、源码和账号相关操作请按照对应的官方入口完成，本文只展开 Kimi 在 OpenClaw 中的配置。

<CardGroup cols={3}>
  <Card title="安装 OpenClaw" icon="terminal" href="https://openclaw.ai/">
    按照 OpenClaw 官方入口完成安装或更新。
  </Card>

  <Card title="查看 OpenClaw 源码" icon="code" href="https://github.com/openclaw/openclaw">
    查看官方仓库、版本和变更说明。
  </Card>

  <Card title="创建 Kimi API Key" icon="key" href="https://platform.kimi.com/console/api-keys">
    在中国区 Kimi 开放平台创建并妥善保存 API Key。
  </Card>
</CardGroup>

Kimi K3 需要账户有可用余额；调用限额随用户等级变化，详见 [充值与限速](/docs/pricing/limits) 。如果组织启用了 IP 白名单，请先按照 [组织最佳实践](/docs/guide/org-best-practice) 添加当前网络的出口 IPv4 地址。

## 设置 Kimi K3

确保已完成上方准备工作中的 OpenClaw 安装，并在终端安装或更新官方 Moonshot Provider：

```bash theme={null}
openclaw plugins install @openclaw/moonshot-provider
openclaw gateway restart
```

运行配置向导：

```bash theme={null}
openclaw onboard --auth-choice moonshot-api-key-cn
```

在向导中依次选择：

* **第 1 步：Model.auth provider > 选择 Moonshot**
* **第 2 步：Model AI auth method > 选择 Kimi API key (.cn)**
* **第 3 步：Enter Moonshot API Key (.cn) > 输入中国区 API Key**
* **第 4 步：Default model > 完成向导后设置为 `moonshot/kimi-k3`**

向导里如果暂时看不到 K3，先继续完成认证，再运行：

```bash theme={null}
openclaw models list --provider moonshot
openclaw models set moonshot/kimi-k3
```

如果稳定版 Provider 目录仍没有 K3，升级插件并重启 Gateway：

```bash theme={null}
openclaw plugins update @openclaw/moonshot-provider
openclaw gateway restart
openclaw models list --provider moonshot
```

<Note>
  OpenClaw 旧版向导截图中的 `Moonshot AI (Kimi K2.5)` 和 `moonshot/kimi-k2.5` 是历史预设，本文不再使用。请以文字步骤和下面的 K3 模型选择器截图为准；不要保留旧的默认模型。
</Note>

如果升级后仍没有 K3，可以在 `~/.openclaw/openclaw.json` 的 `models.providers.moonshot.models` 中补充 K3 条目，保留已有模型：

```json theme={null}
{
  "models": {
    "mode": "merge",
    "providers": {
      "moonshot": {
        "baseUrl": "https://api.moonshot.cn/v1",
        "api": "openai-completions",
        "models": [{
          "id": "kimi-k3",
          "name": "Kimi K3",
          "reasoning": true,
          "input": ["text", "image", "video"],
          "contextWindow": 1048576,
          "maxTokens": 8192,
          "thinkingLevelMap": {
            "off": null,
            "minimal": "max",
            "low": "max",
            "medium": "max",
            "high": "max",
            "xhigh": "max",
            "max": "max"
          },
          "compat": {
            "maxTokensField": "max_tokens",
            "supportsUsageInStreaming": false,
            "requiresStringContent": true,
            "supportsReasoningEffort": true,
            "supportedReasoningEfforts": ["minimal", "low", "medium", "high", "xhigh", "max"]
          }
        }]
      }
    }
  }
}
```

如果需要让图片和视频输入也走 K3，请在同一个配置中加入：

```json theme={null}
{
  "agents": {
    "defaults": {
      "imageModel": "moonshot/kimi-k3"
    }
  },
  "tools": {
    "media": {
      "image": { "models": [{ "type": "provider", "provider": "moonshot", "model": "kimi-k3", "capabilities": ["image"] }] },
      "video": { "models": [{ "type": "provider", "provider": "moonshot", "model": "kimi-k3", "capabilities": ["video"] }] }
    }
  }
}
```

K3 的服务端思考参数固定为 `max`。`contextWindow` 保持 1M；`maxTokens` 使用 8192 作为 OpenClaw 单次回复上限，避免把 1M 输入窗口误当成单次输出上限。`maxTokensField: "max_tokens"`、`supportsUsageInStreaming: false` 和 `requiresStringContent: true` 是 K3 兼容性配置，不能删除：K3 对 `max_completion_tokens`、流式 usage 和纯文本数组 content 的兼容性不同。

<img src="https://mintcdn.com/moonshotcn/aRk2WwauT7qVH_Kj/assets/pics/openclaw/openclaw-chat-model-cn.png?fit=max&auto=format&n=aRk2WwauT7qVH_Kj&q=85&s=8b585d157e644da584bccb40d820342a" alt="控制台中的 Moonshot / Kimi K3 选择" width="1280" height="720" data-path="assets/pics/openclaw/openclaw-chat-model-cn.png" />

## 第四步：开始使用

安装完成后，打开安装向导或 Gateway 输出的 Control UI 地址进入聊天界面，底部模型应显示 `kimi-k3 · moonshot`。

进入聊天页后即可发送消息。模型选择器截图见第三步：

<img src="https://mintcdn.com/moonshotcn/aRk2WwauT7qVH_Kj/assets/pics/openclaw/openclaw-chat-cn-dashboard.png?fit=max&auto=format&n=aRk2WwauT7qVH_Kj&q=85&s=7db71ef97e3f8a4db8f1bf889401b8e2" alt="K3 聊天页" width="1280" height="720" data-path="assets/pics/openclaw/openclaw-chat-cn-dashboard.png" />

## 常见问题

### 401 / Invalid Authentication

* 确认使用的是 Kimi 开放平台 API Key，而不是 Kimi Code Key。
* 中国区使用 `moonshot-api-key-cn`；国际站使用国际版认证选项。
* 如果环境变量中已有旧的 Key，重新运行向导并重新输入中国区 Key。

### 找不到 Moonshot 认证选项

确认官方插件已安装并重启 Gateway：

```bash theme={null}
openclaw plugins install @openclaw/moonshot-provider
openclaw gateway restart
```

### K3 不在模型列表

升级 OpenClaw 和 Moonshot Provider；仍缺失时补充第三步的 K3 条目，然后重新执行 `openclaw models set moonshot/kimi-k3`。

更多 Kimi API 问题排查方法请参阅 [问题排查](/docs/guide/troubleshooting) 页面。
