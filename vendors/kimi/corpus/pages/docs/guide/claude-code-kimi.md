> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 在 Claude Code 中使用 Kimi

> 介绍如何将 Kimi API 接入 Claude Code，并完成模型选择与配置验证。

> 本文介绍如何在 [Claude Code](https://claude.com/product/claude-code) 中接入 Kimi 的 Anthropic 兼容端点（[Messages API](/docs/api/messages)）。Claude Code 的界面与配置项可能随版本变化，请以实际版本为准。

## 安装 Claude Code

已安装的用户可跳过。执行以下命令安装：

```shell theme={null}
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
```

<Accordion title="安装 Node.js 与初始化配置">
  macOS 和 Linux：

  ```shell theme={null}
  # 安装 nodejs
  curl -fsSL https://fnm.vercel.app/install | bash

  # 新开一个终端，让 fnm 生效
  fnm install 24.3.0
  fnm default 24.3.0
  fnm use 24.3.0
  ```

  Windows（PowerShell）：

  ```powershell theme={null}
  # 右键按 Windows 按钮，点击「终端」，然后依次执行
  winget install OpenJS.NodeJS
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

  # 关闭终端窗口，新开一个终端窗口
  ```

  安装 Node.js 后，执行一次初始化配置：

  ```shell theme={null}
  node --eval "
      const fs = require('fs');
      const path = require('path');
      const os = require('os');
      const homeDir = os.homedir();
      const filePath = path.join(homeDir, '.claude.json');
      if (fs.existsSync(filePath)) {
          const content = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
          fs.writeFileSync(filePath, JSON.stringify({ ...content, hasCompletedOnboarding: true }, null, 2), 'utf-8');
      } else {
          fs.writeFileSync(filePath, JSON.stringify({ hasCompletedOnboarding: true }, null, 2), 'utf-8');
      }"
  ```
</Accordion>

<Accordion title="非首次安装：注意清理历史配置和环境变量">
  如果您之前通过第三方工具或手动修改过 `~/.claude/settings.json`，里面残留的旧配置会 **覆盖** 终端里 export 的同名环境变量，导致新配置不生效或模型请求被静默改写。建议先执行以下脚本清理：

  ```shell theme={null}
  node --eval "
      const fs = require('fs');
      const path = require('path');
      const os = require('os');
      const settingsPath = path.join(os.homedir(), '.claude', 'settings.json');
      if (fs.existsSync(settingsPath)) {
          const content = JSON.parse(fs.readFileSync(settingsPath, 'utf-8'));
          if (content && typeof content === 'object' && content.env && typeof content.env === 'object') {
              for (const key of [
                  'ANTHROPIC_BASE_URL',
                  'ANTHROPIC_API_KEY',
                  'ANTHROPIC_AUTH_TOKEN',
                  'ANTHROPIC_MODEL',
                  'ANTHROPIC_SMALL_FAST_MODEL',
                  'CLAUDE_CODE_SUBAGENT_MODEL',
                  'ANTHROPIC_DEFAULT_OPUS_MODEL',
                  'ANTHROPIC_DEFAULT_OPUS_MODEL_NAME',
                  'ANTHROPIC_DEFAULT_SONNET_MODEL',
                  'ANTHROPIC_DEFAULT_SONNET_MODEL_NAME',
                  'ANTHROPIC_DEFAULT_HAIKU_MODEL',
                  'ANTHROPIC_DEFAULT_HAIKU_MODEL_NAME',
                  'ANTHROPIC_DEFAULT_FABLE_MODEL',
                  'ANTHROPIC_DEFAULT_FABLE_MODEL_NAME',
                  'ENABLE_TOOL_SEARCH',
                  'CLAUDE_CODE_AUTO_COMPACT_WINDOW',
                  'CLAUDE_CODE_EFFORT_LEVEL',
              ]) {
                  delete content.env[key];
              }
              fs.writeFileSync(settingsPath, JSON.stringify(content, null, 2), 'utf-8');
          }
      }"
  ```

  该脚本仅删除 `env` 中的端点、密钥与模型相关变量，不影响 `settings.json` 中的其他配置（如权限、主题等）。

  另外，请检查 `~/.zshrc`、`~/.bashrc` 等 shell 配置文件中是否残留旧的 `ANTHROPIC_*` export（Windows 用户请检查用户环境变量），如有请一并删除，否则同样会干扰新配置。
</Accordion>

## 获取 Kimi API Key

访问 [Kimi 开放平台](https://platform.kimi.com/console/api-keys) 创建 API Key，替换下文中的 `YOUR_MOONSHOT_API_KEY`。

## 配置环境变量

将以下变量写入 `~/.claude/settings.json` 的 `env` 字段，保存后重启 Claude Code 即可生效。本示例将 HAIKU 档配置为 `kimi-k2.7-code`，其余档位均为 `kimi-k3[1m]`。

```json theme={null}
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.moonshot.cn/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "YOUR_MOONSHOT_API_KEY",
    "ANTHROPIC_MODEL": "kimi-k3[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "kimi-k3[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "kimi-k3[1m]",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "kimi-k2.7-code",
    "ANTHROPIC_DEFAULT_FABLE_MODEL": "kimi-k3[1m]",
    "CLAUDE_CODE_SUBAGENT_MODEL": "kimi-k3[1m]",
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000",
    "CLAUDE_CODE_EFFORT_LEVEL": "max"
  }
}
```

注意：`settings.json` 的 `env` 会 **覆盖** 终端里 export 的同名变量；该文件包含明文 API Key，请勿提交到 git 仓库。

### 配置项说明

Claude Code 内部会按场景使用不同档位的模型（主对话、后台摘要、子 Agent 等），只配置部分变量会让对应场景静默失败：

| 变量                                                                                                                                    | 作用           | 不配置的后果                   |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------------ |
| `ANTHROPIC_BASE_URL`                                                                                                                  | Kimi 端点地址    | 请求发往 Anthropic 官方端点，鉴权失败 |
| `ANTHROPIC_AUTH_TOKEN`                                                                                                                | Kimi API Key | 返回 401 鉴权错误              |
| `ANTHROPIC_MODEL`                                                                                                                     | 主对话模型        | 报模型不存在错误                 |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` / `ANTHROPIC_DEFAULT_SONNET_MODEL` / `ANTHROPIC_DEFAULT_HAIKU_MODEL` / `ANTHROPIC_DEFAULT_FABLE_MODEL` | 各任务档位使用的模型   | 对应档位的任务失败                |
| `CLAUDE_CODE_SUBAGENT_MODEL`                                                                                                          | 子 Agent 模型   | 子任务失败或效果明显变差             |
| `CLAUDE_CODE_AUTO_COMPACT_WINDOW`                                                                                                     | 触发自动压缩的上下文窗口 | 过小会过早压缩丢失上下文，过大报上下文超限错误  |
| `CLAUDE_CODE_EFFORT_LEVEL`                                                                                                            | 推理强度         | 建议设为 `max`，调低可能影响复杂任务质量  |

## 模型与思考行为

三个模型在 Claude Code 中的行为差异：

| 模型               | 思考模式      | 使用要点                                                                    |
| ---------------- | --------- | ----------------------------------------------------------------------- |
| `kimi-k3`（默认）    | 默认开启，可关闭  | 开箱即用，无需额外配置                                                             |
| `kimi-k2.7-code` | 强制开启，不可关闭 | 必须在 Claude Code 中开启 Thinking（macOS `Option+T`，Windows/Linux `Alt+T`）后使用 |
| `kimi-k2.6`      | 可选，可关闭    | 适合对延迟敏感的简单任务                                                            |

未开启思考时，`kimi-k2.7-code` 的请求会被拒绝并返回 `400 invalid thinking: only type=enabled is allowed for this model`。

## 确认配置是否生效

配置完成后，可以先用 curl 验证端点和 API Key 是否可用：

```shell theme={null}
curl https://api.moonshot.cn/anthropic/v1/messages \
  --header "Authorization: Bearer YOUR_MOONSHOT_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{"model": "kimi-k3", "max_tokens": 1, "messages": [{"role": "user", "content": "hi"}]}'
```

返回正常的 JSON 响应即说明端点与凭据均可用；返回 401 说明 API Key 无效或与平台不匹配。确认无误后启动 Claude Code，输入 `/status` 确认配置状态：

* Base URL 应显示为 `https://api.moonshot.cn/anthropic`
* Model 应显示为 `kimi-k3[1m]`

<img src="https://mintcdn.com/moonshotcn/YB8GjRk9GuxCN-3-/assets/pics/cline/status.png?fit=max&auto=format&n=YB8GjRk9GuxCN-3-&q=85&s=8d3442db47d48a1b531f49789e9a761f" alt="status" width="1140" height="260" data-path="assets/pics/cline/status.png" />

Claude Code 的 `/model` 菜单会显示已配置的模型。

<img src="https://mintcdn.com/moonshotcn/YB8GjRk9GuxCN-3-/assets/pics/cline/model-menu.png?fit=max&auto=format&n=YB8GjRk9GuxCN-3-&q=85&s=debffa8a1d58333e1bd71b2d808e3a89" alt="model-menu" width="1140" height="308" data-path="assets/pics/cline/model-menu.png" />

最后随意发送一条消息（例如 `你好`），能正常收到回复即说明端到端配置成功：

<img src="https://mintcdn.com/moonshotcn/YB8GjRk9GuxCN-3-/assets/pics/cline/chat-verify.png?fit=max&auto=format&n=YB8GjRk9GuxCN-3-&q=85&s=1bfac7192461f790e614af67740f1d3b" alt="chat-verify" width="1140" height="401" data-path="assets/pics/cline/chat-verify.png" />

## 常见问题

<AccordionGroup>
  <Accordion title="返回 401 鉴权错误">
    * 检查 `ANTHROPIC_AUTH_TOKEN` 是否为有效的 Kimi API Key，并确认 `YOUR_MOONSHOT_API_KEY` 已替换为你的 Key；
    * 确认 `ANTHROPIC_BASE_URL` 与创建 API Key 的平台一致，即在上文「获取 Kimi API Key」链接对应的平台创建 Key 并使用本页给出的端点；
    * 如果您之前配置过 `ANTHROPIC_API_KEY`，请将其删除，避免与 `ANTHROPIC_AUTH_TOKEN` 同时存在导致冲突。
  </Accordion>

  <Accordion title="提示模型不存在（model not found）">
    检查各模型变量的值是否拼写正确（`kimi-k3[1m]`），注意不要有多余的空格或引号。
  </Accordion>

  <Accordion title="后台任务或子 Agent 报错">
    通常是 `ANTHROPIC_DEFAULT_HAIKU_MODEL`、`ANTHROPIC_DEFAULT_FABLE_MODEL` 或 `CLAUDE_CODE_SUBAGENT_MODEL` 未配置，对应场景请求了 Kimi 端点无法识别的模型名，请对照「配置项说明」补齐。
  </Accordion>

  <Accordion title="修改配置后不生效">
    * 检查 `~/.claude/settings.json` 的 `env` 中是否有残留旧配置，可执行上文折叠块中的清理脚本；
    * 检查 `~/.zshrc`、`~/.bashrc` 等 shell 配置文件中是否有旧的 `ANTHROPIC_*` export 残留；
    * 修改 `settings.json` 后需重启 Claude Code 才会生效。
  </Accordion>

  <Accordion title="之前通过 /login 登录过 Claude 账号">
    `ANTHROPIC_AUTH_TOKEN` 设置后会优先于已保存的登录态生效，一般无需处理。可在会话中输入 `/status` 确认当前生效的凭据来源；如需清除已保存的登录，可执行 `/logout`。
  </Accordion>
</AccordionGroup>
