> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 在 OpenCode 中使用 Kimi 模型

> 安装 OpenCode，通过内置认证接入中国区 Kimi 开放平台，并使用 Kimi K3 及其推理强度档位。

[OpenCode](https://opencode.ai/) 是一款开源的编程 Agent 产品。本文介绍如何通过内置认证将 OpenCode 接入中国区 Kimi 开放平台，并使用具备 1M token 上下文的 `kimi-k3` 模型。

<Note>
  本文内容基于 OpenCode 1.18.3 版本，其界面、配置项和支持能力可能随版本变化。
</Note>

## 准备工作

开始前，请完成以下准备工作。安装和账号相关操作请按照对应的官方指引完成，本文不再展开。

<CardGroup cols={3}>
  <Card title="安装 OpenCode" icon="terminal" href="https://opencode.ai/docs/">
    按照 OpenCode 官方文档完成安装或更新。
  </Card>

  <Card title="创建 API Key" icon="key" href="https://platform.kimi.com/console/api-keys">
    在中国区 Kimi 开放平台创建并妥善保存 API Key。
  </Card>

  <Card title="检查账户设置" icon="gauge" href="/docs/guide/account-and-payments">
    确认账户有可用余额，并检查调用限额、项目预算和组织设置。
  </Card>
</CardGroup>

Kimi K3 需要账户有可用余额；新用户认证赠送的代金券不能用于 Kimi K3。调用限额随用户等级变化，详见 [充值与限速](/docs/pricing/limits) 。如果组织启用了 IP 白名单，请先按照 [组织最佳实践](/docs/guide/org-best-practice) 添加当前网络的出口 IPv4 地址。

## 第一步：配置 API Key

运行 `opencode auth login`，在 Provider 列表中选择 **Moonshot AI (China)**：

```text theme={null}
$ opencode auth login
┌  Add credential
│
◆  Select provider
│  Search: Moon█ (2 matches)
│  ● Moonshot AI (China)
│  ↑/↓ to select • Enter: confirm • Type: to search
└
```

然后粘贴中国区 Kimi 开放平台的 API Key，按 `Enter` 确认：

```text theme={null}
$ opencode auth login
┌  Add credential
│
◇  Select provider
│  Moonshot AI (China)
│
◇  Enter your API key
│  ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪
│
└  Done
```

<Warning>
  不要把 API Key 写入配置文件、截图或 Git 仓库。中国区、国际站使用不同的 API Key，请勿混用。
</Warning>

## 第二步：选择 Kimi K3 模型

运行 `opencode` 启动 OpenCode：

```bash theme={null}
opencode
```

在输入框中执行 `/models` 命令：

<img src="https://mintcdn.com/moonshotcn/-sdCwn5QHf2-xkgA/assets/pics/opencode/models-command.png?fit=max&auto=format&n=-sdCwn5QHf2-xkgA&q=85&s=db4637f3286f6effa52d354c36b447b2" alt="输入 /models 命令" width="1342" height="304" data-path="assets/pics/opencode/models-command.png" />

在 Select model 弹窗中搜索并选择 **Kimi K3**：

<img src="https://mintcdn.com/moonshotcn/-sdCwn5QHf2-xkgA/assets/pics/opencode/select-model.png?fit=max&auto=format&n=-sdCwn5QHf2-xkgA&q=85&s=f60966470659a0a2dafa82e13161a15b" alt="选择 Kimi K3 模型" width="990" height="187" data-path="assets/pics/opencode/select-model.png" />

## 第三步：调节推理强度

在输入框中执行 `/variants` 命令：

<img src="https://mintcdn.com/moonshotcn/-sdCwn5QHf2-xkgA/assets/pics/opencode/variants-command.png?fit=max&auto=format&n=-sdCwn5QHf2-xkgA&q=85&s=6445d82528fd6f7dbb7a9cb18ec1190b" alt="输入 /variants 命令" width="1327" height="305" data-path="assets/pics/opencode/variants-command.png" />

在 Select variant 弹窗中选择 **max**：

<img src="https://mintcdn.com/moonshotcn/-sdCwn5QHf2-xkgA/assets/pics/opencode/select-variant-max.png?fit=max&auto=format&n=-sdCwn5QHf2-xkgA&q=85&s=dc5ca8897a19857fd7398fd1bbf04b8d" alt="选择 max 推理强度" width="1005" height="249" data-path="assets/pics/opencode/select-variant-max.png" />

`kimi-k3` 的推理强度默认 `max`，也支持切换至 `low` / `high`，详见 [模型参数参考](/docs/api/models-overview) 。

完成后，底部状态栏应依次显示 **Kimi K3**、**Moonshot AI (China)** 和 **max**：

<img src="https://mintcdn.com/moonshotcn/-sdCwn5QHf2-xkgA/assets/pics/opencode/final-config.png?fit=max&auto=format&n=-sdCwn5QHf2-xkgA&q=85&s=16e5c8bd8e1fe8f42829437062216e93" alt="最终配置效果" width="1328" height="439" data-path="assets/pics/opencode/final-config.png" />

## 了解更多

* [OpenCode 官方文档](https://opencode.ai/docs)
* [Kimi 开放平台快速开始](/docs/get-api-key)
