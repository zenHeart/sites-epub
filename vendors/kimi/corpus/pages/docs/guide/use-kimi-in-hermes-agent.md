> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 在 Hermes Agent 中使用 Kimi K3

> 安装 Hermes Agent，接入中国区 Kimi 开放平台，并启用 Kimi K3 的文本、图片和视频理解能力。

[Hermes Agent](https://github.com/nousresearch/hermes-agent) 是 Nous Research 开源的 AI Agent，支持持久化记忆、工具调用，以及 CLI、Telegram、Discord、Slack 和 WhatsApp 等多种交互方式。

本文介绍如何将 Hermes Agent 接入中国区 Kimi 开放平台，并使用具备 1M token 上下文和原生视觉理解能力的 `kimi-k3`。Hermes 配置中的 API Base URL 为 `https://api.moonshot.cn/v1`；实际 Chat Completions 请求地址为 `https://api.moonshot.cn/v1/chat/completions`。

<Note>
  本文截图基于 Hermes Agent v0.18.2。后续版本的菜单文字可能变化，但应继续使用中国区 Kimi 开放平台 API Key、`kimi-k3` 和 `https://api.moonshot.cn/v1`。
</Note>

## 准备工作

开始前，请完成以下准备工作。安装和账号相关操作请按照对应的官方指引完成，本文不再展开。

<CardGroup cols={3}>
  <Card title="安装 Hermes Agent" icon="terminal" href="https://hermes-agent.nousresearch.com/docs/getting-started/installation">
    按照 Hermes Agent 官方安装文档完成安装或更新。
  </Card>

  <Card title="创建 API Key" icon="key" href="https://platform.kimi.com/console/api-keys">
    在中国区 Kimi 开放平台创建并妥善保存 API Key。
  </Card>

  <Card title="检查账户设置" icon="gauge" href="/docs/guide/account-and-payments">
    确认账户有可用余额，并检查调用限额、项目预算和组织设置。
  </Card>
</CardGroup>

Kimi K3 需要充值后使用；新用户认证赠送的代金券不能用于 Kimi K3。调用限额随用户等级变化，详见 [充值与限速](/docs/pricing/limits) 。如果组织启用了 IP 白名单，请先按照 [组织最佳实践](/docs/guide/org-best-practice) 添加当前网络的出口 IPv4 地址。

## 第一步：选择中国区 Kimi Provider 和 K3

运行模型配置向导：

```bash theme={null}
hermes model
```

在一级菜单选择 **Kimi / Moonshot**。

<img src="https://mintcdn.com/moonshotcn/aRk2WwauT7qVH_Kj/assets/pics/hermes-k3/provider-menu.png?fit=max&auto=format&n=aRk2WwauT7qVH_Kj&q=85&s=e61e546542c6344b4a84698dcb744a2b" alt="选择 Kimi / Moonshot" width="1720" height="998" data-path="assets/pics/hermes-k3/provider-menu.png" />

在二级菜单选择 **Kimi / Moonshot (China)**，然后在掩码输入框中粘贴中国区 Kimi API Key。Hermes 会把它保存到本机的私密环境配置中，对应变量为 `KIMI_CN_API_KEY`。

<img src="https://mintcdn.com/moonshotcn/aRk2WwauT7qVH_Kj/assets/pics/hermes-k3/provider-region.png?fit=max&auto=format&n=aRk2WwauT7qVH_Kj&q=85&s=7203ef27a8e53a4c1fb869c99e1e9b5b" alt="选择中国区 Kimi Provider" width="1020" height="322" data-path="assets/pics/hermes-k3/provider-region.png" />

提示确认 Base URL 时，保留下列默认值并按 Enter：

```text theme={null}
Base URL [https://api.moonshot.cn/v1]:
```

选择默认模型时，如果列表中没有 `kimi-k3`，请选择 **Enter custom model name**，再输入 `kimi-k3`。不要添加 `moonshot/` 等前缀。

<img src="https://mintcdn.com/moonshotcn/aRk2WwauT7qVH_Kj/assets/pics/hermes-k3/custom-model.png?fit=max&auto=format&n=aRk2WwauT7qVH_Kj&q=85&s=138e42e8ab68420a3bb6aa18f30ce50e" alt="选择手动输入模型名称" width="908" height="372" data-path="assets/pics/hermes-k3/custom-model.png" />

<Warning>
  不要把 API Key 写入 `config.yaml`、命令参数、截图或 Git 仓库。中国区、国际站和 Kimi Coding Plan 使用不同的 API Key，请勿混用。
</Warning>

## 第二步：写入 K3 完整配置

运行：

```bash theme={null}
hermes config edit
```

把下面的 `kimi-k3-cn` 条目追加到现有 `custom_providers` 列表，并把其余字段合并到对应的顶层区域。如果已有同名顶层区域，请修改其中的字段，不要重复创建；如果已有其他自定义 Provider，请保留它们。

```yaml theme={null}
custom_providers:
  - name: kimi-k3-cn
    base_url: https://api.moonshot.cn/v1
    key_env: KIMI_CN_API_KEY
    api_mode: chat_completions
    model: kimi-k3
    extra_body:
      reasoning_effort: max
    models:
      kimi-k3:
        context_length: 1048576
        supports_vision: true

model:
  provider: custom:kimi-k3-cn
  default: kimi-k3
  context_length: 1048576
  supports_vision: true

agent:
  reasoning_effort: max

auxiliary:
  vision:
    provider: main
    model: kimi-k3
    extra_body:
      reasoning_effort: max
```

这组配置明确启用 Kimi K3 当前支持的最高推理强度、1M token 上下文和原生图片理解，同时让视频分析复用同一个 K3 主 Provider。其中 `reasoning_effort` 是 Chat Completions 请求的顶层字段，支持 `low` / `high` / `max`，默认 `max`；示例使用 `max`，详见 [模型参数参考](/docs/api/models-overview) 。

<Note>
  `base_url` 只填写 `https://api.moonshot.cn/v1`。Hermes 使用 OpenAI 兼容客户端时会自动追加 `/chat/completions`，不要把完整请求地址写入 `base_url`。
</Note>

## 第三步：启用并使用官方视频工具

运行：

```bash theme={null}
hermes tools enable video
```

启用后，Hermes 可以调用官方 `video_analyze` 工具。对于本地视频，该工具会读取完整文件，将其编码为 `data:video/...;base64,...`，再以一个 `video_url` 内容块发送给 `kimi-k3`；这条链路不会先在本地使用 FFmpeg 抽帧。

Hermes v0.18.2 支持 MP4、WebM、MOV、AVI、MKV 和 MPEG 等常见格式，Base64 视频载荷上限约为 50 MB。该限制来自 Hermes 客户端视频工具的硬编码上限，并非 Kimi API 限制。较大的视频请先裁剪或压缩。

这个命令只需执行一次。以后分析视频时，无需再次配置，也无需使用 `/video` 命令；请在 Hermes 对话中提供视频的绝对路径，并明确要求调用 `video_analyze`：

```text theme={null}
请调用 video_analyze 分析 /视频的绝对路径/demo.mp4，概括视频内容，并列出三个能从画面中确认的细节。
```

也可以提供可直接访问的 HTTP 或 HTTPS 视频 URL。

## 第四步：启动 Hermes 并使用 K3

开启新会话，让新的 Provider、上下文和工具配置全部生效：

```bash theme={null}
hermes
```

状态栏应显示 `kimi-k3` 和 `1M` 上下文。

<img src="https://mintcdn.com/moonshotcn/aRk2WwauT7qVH_Kj/assets/pics/hermes-k3/chat.png?fit=max&auto=format&n=aRk2WwauT7qVH_Kj&q=85&s=e6047994b3705b9f0838f3d781be779a" alt="在 Hermes 中使用 Kimi K3" width="1000" height="321" data-path="assets/pics/hermes-k3/chat.png" />

### 使用图片

使用本地图片绝对路径：

```text theme={null}
/image /图片的绝对路径/example.png
```

也可以把图片复制到剪贴板后使用 `/paste`，再输入问题。图片会作为原生视觉内容发送给 `kimi-k3`。

## 常见问题

### 模型列表里没有 `kimi-k3`

重新运行 `hermes model`，选择 **Kimi / Moonshot > Kimi / Moonshot (China)**，然后选择 **Enter custom model name** 并输入 `kimi-k3`。

### Hermes 连接到了错误的 Endpoint

中国区配置向导中的默认值应为 `Base URL [https://api.moonshot.cn/v1]:`。请确认使用的是在 `https://platform.kimi.com/console/api-keys` 创建的中国区 API Key，然后重新运行 `hermes model`。

### API Key 无效或请求被拒绝

确认使用的是中国区 Kimi 开放平台创建的 API Key，并重新运行 `hermes model` 输入。如果组织启用了 IP 白名单，还需确认当前出口 IPv4 地址已被允许。

### 出现 429 错误

降低并发并稍后重试，同时检查账户余额和当前用户等级的调用限额。具体规则以 [充值与限速](/docs/pricing/limits) 页面为准。

### 视频工具没有被调用

确认已经运行 `hermes tools enable video`，并在请求中明确写出“请调用 `video_analyze`”。本地文件必须使用绝对路径，且编码后的载荷不能超过约 50 MB。

更多 Kimi API 问题排查方法请参阅 [问题排查](/docs/guide/troubleshooting) 页面。
