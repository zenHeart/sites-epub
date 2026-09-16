> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax CLI 

> [mmx-cli](https://github.com/MiniMax-AI/cli)：一句话，帮你的 Agent 助手用上 MiniMax

对于 Token Plan 用户，无需编写代码，即可在 OpenClaw、Claude Code 等 AI 助手中直接调用 MiniMax 的文本、图像、视频、语音、视觉理解和网络搜索能力。实际可用能力以当前套餐和 CLI 版本为准。

如果仍想通过 API 直接调用，作为开发者自行集成，另外详见 [API 文档](/docs/api-reference/api-overview)。

### 安装和配置 CLI

<Tabs>
  <Tab title="通过Agent安装">
    请将以下提示词复制给你的AI Agent（OpenClaw、Claude Code、Cursor、MaxClaw、AutoClaw、KimiClaw、TRAE、OpenCode等）, 它会引导你完成安装、登录与 SKILL 接入（请将 sk-xxxxx 替换为你的实际密钥）：

    ```text theme={null}
    请帮我接入 MiniMax CLI（https://github.com/MiniMax-AI/cli），按以下三步完成安装与配置：

    1. 全局安装 CLI：执行 `npm install -g mmx-cli`，完成后用 `mmx --version` 验证
    2. 登录并配置 API Key：执行 `mmx auth login --api-key sk-xxxxx`；
    3. 安装官方 SKILL：执行 `npx skills add MiniMax-AI/cli -y -g`

    完成后请执行 `mmx quota` 查看我的 Token Plan 余额，确认整体配置生效。
    ```
  </Tab>

  <Tab title="手动安装">
    <Steps>
      <Step title="安装 MMX-CLI">
        在终端运行以下命令完成全局安装：

        ```bash theme={null}
        npm install -g mmx-cli
        ```
      </Step>

      <Step title="登录 API Key">
        使用 API Key 完成鉴权（请将 `sk-xxxxx` 替换为你的 Key）：

        ```bash theme={null}
        mmx auth login --api-key sk-xxxxx
        ```

        最新版 mmx-cli 会根据 Key 自动检测服务区域，通常无需手动配置 region。

        <Note>
          服务区域根据所使用的 API 服务是在国内平台（`cn`，[MiniMax 国内版订阅](https://platform.minimaxi.com/subscribe/token-plan)）还是在海外平台（`global`，[MiniMax 国际版订阅](https://platform.minimax.io/subscribe/token-plan)）上购买所决定。
        </Note>

        <Warning>
          若登录后调用接口报 401，大概率是 region 未自动匹配成功。可手动指定：

          ```bash theme={null}
          mmx config set --key region --value cn       # 国内 API 服务
          mmx config set --key region --value global   # 海外 API 服务
          ```

          执行 `mmx auth status` 确认当前 region 与所购买服务来源平台一致。
        </Warning>
      </Step>

      <Step title="安装 SKILL（可选，推荐 Agent 用户）">
        若你要在 Claude Code、OpenClaw、Cursor 等 AI Agent 中调用 mmx，建议加装官方 SKILL.md，Agent 调用时决策更准、无需临时翻 `--help`：

        ```bash theme={null}
        npx skills add MiniMax-AI/cli -y -g
        ```

        <Tip>
          SKILL 会自动 symlink 到 `~/.claude/skills/`、`~/.openclaw/skills/` 等目录，各 Agent 下次启动即可识别。**仅在终端直接使用 mmx 命令的用户可以跳过此步。**
        </Tip>
      </Step>
    </Steps>
  </Tab>
</Tabs>

### 调用 CLI

<Tabs>
  <Tab title="通过Agent调用">
    **语言 · 四言诗**

    输入（Agent指令）： `帮我用minimax生成一首关于AI的4言诗`

    输出： 算力无垠，星火相连；<br />智能如海，梦随光年

    ***

    **视频 · [Hailuo 2.3](https://minimaxi.com/news/minimax-hailuo-23)**

    输入（Agent指令）： `生成一段视频：夕阳下，一只猫坐在窗边望向远方`

    输出：

    <video src="https://filecdn.minimax.chat/public/84768d5d-354f-408f-b63f-56c5cee3e969.mp4" controls={true} style={{width: '50%', borderRadius: '8px'}} />

    ***

    **语音 · [Speech 2.8](https://www.minimaxi.com/news/minimax-speech-28)**

    输入（Agent指令）： `用温柔女声音朗读：欢迎使用 MiniMax Token Plan, 订阅 Token Plan 后，让你的 Agent 生成视频、语音和图片。`

    输出：

    <video src="https://filecdn.minimax.chat/public/bc984f52-ab54-4c4e-b410-713ff4cdbfdc.mp3" controls={true} className="audio-container" style={{width: '50%'}} />

    ***

    **图片 · Image 01**

    输入（Agent指令）： `生成一张赛博朋克风格的城市夜景图，16:9 比例`

    输出：

    <img src="https://filecdn.minimax.chat/public/94db816d-016e-4fc5-8913-b1a6a4935aad.jpeg" style={{width: '50%', borderRadius: '8px'}} />

    未指定输出参数时，图片保存到当前工作目录；可通过 `--out` 指定单张图片路径，或通过 `--out-dir` 指定批量输出目录。
  </Tab>

  <Tab title="手动调用">
    **语言 · 四言诗**

    输入（命令行指令）： `mmx text chat --message "帮我生成一首关于AI的4言诗"`

    输出： 算力无垠，星火相连；<br />智能如海，梦随光年

    ***

    **视频 · [Hailuo 2.3](https://minimaxi.com/news/minimax-hailuo-23)**

    输入（命令行指令）： `mmx video generate --prompt "夕阳下，一只猫坐在窗边望向远方"`

    输出：

    <video src="https://filecdn.minimax.chat/public/84768d5d-354f-408f-b63f-56c5cee3e969.mp4" controls={true} style={{width: '50%', borderRadius: '8px'}} />

    ***

    **语音 · [Speech 2.8](https://www.minimaxi.com/news/minimax-speech-28)**

    输入（命令行指令）： `mmx speech synthesize --text "欢迎使用 MiniMax Token Plan, 订阅 Token Plan 后，让你的 Agent 生成视频、语音和图片" --out voiceover.mp3`

    输出：

    <video src="https://filecdn.minimax.chat/public/bc984f52-ab54-4c4e-b410-713ff4cdbfdc.mp3" controls={true} className="audio-container" style={{width: '50%'}} />

    ***

    **图片 · Image 01**

    输入（命令行指令）： `mmx image "赛博朋克风格的城市夜景，16:9"`

    输出：

    <img src="https://filecdn.minimax.chat/public/94db816d-016e-4fc5-8913-b1a6a4935aad.jpeg" style={{width: '50%', borderRadius: '8px'}} />
  </Tab>
</Tabs>

### CLI 面板

<Note>
  <div>
    <p>在命令行输入 `mmx`，即可打开CLI面板，快速了解 MMX-CLI 的主要功能和用量信息</p>

    <img src="https://filecdn.minimax.chat/public/agent-tool/mmx-cli/20260903-211352.png" style={{borderRadius: '8px', marginTop: '12px', maxWidth: '100%'}} alt="MMX-CLI 中文面板示意图" />

    <ul style={{marginTop: '12px'}}>
      <li><strong>resources：</strong> 当前可用的调用资源类型</li>
      <li><strong>flags：</strong> 支持在命令后加的参数/选项</li>
      <li><strong>用量信息：</strong> 剩余额度与视频配额概览</li>
      <li><strong>帮助入口：</strong> 使用方法说明</li>
    </ul>
  </div>
</Note>

***

## 能力概览

MMX-CLI 在终端内提供统一的命令入口，覆盖文本、图像、视频、语音、视觉理解与网络检索等能力：

| 能力     | 基本命令                    | 说明                      |
| ------ | ----------------------- | ----------------------- |
| **语言** | `mmx text chat`         | 多轮对话、流式输出、系统提示词、JSON 输出 |
| **图像** | `mmx image generate`    | 文生图，支持宽高比与批量生成          |
| **视频** | `mmx video generate`    | 异步视频生成，支持任务查询与下载        |
| **语音** | `mmx speech synthesize` | 文字转语音（TTS），支持多音色与流式输出   |
| **视觉** | `mmx vision describe`   | 图像理解，支持本地文件、URL、文件 ID   |
| **搜索** | `mmx search query`      | 内置网络检索                  |

<Accordion title="更多运维命令">
  | 命令                                   | 用途                    | 典型示例                                     |
  | ------------------------------------ | --------------------- | ---------------------------------------- |
  | `mmx auth status / refresh / logout` | 查看登录身份 / 刷新凭据 / 登出    | `mmx auth status`                        |
  | `mmx config show / set`              | 查看与修改配置（region、默认模型等） | `mmx config set --key region --value cn` |
  | `mmx agent setup`                    | 为 AI 编程工具配置 MiniMax   | `mmx agent setup`                        |
  | `mmx quota`                          | 查看 Token Plan 用量与剩余额度 | `mmx quota`                              |
  | `mmx update`                         | 显示当前版本和升级提示           | `mmx update`                             |
</Accordion>

***

### 用量覆盖范围

Token Plan 额度和用量进度条规则请见：[Token Plan 订阅定价](/docs/guides/pricing-token-plan)

***

## 常见问题

### API Key 在哪里申请？

* 国际版：[platform.minimax.io 订阅 Token Plan](https://platform.minimax.io/subscribe/token-plan)
* 国内版：[platform.minimaxi.com 订阅 Token Plan](https://platform.minimaxi.com/subscribe/token-plan)

### 登录后仍报 401 怎么办？

通常 `mmx auth login` 会根据 API Key 自动检测服务区域（若购买的是国内套餐，在进行 mmx auth login 配置时尽量不要开VPN）。若仍报 401，大概率是 region 未自动匹配成功，可手动指定：

```bash theme={null}
mmx config set --key region --value cn       # 国内 API Key
mmx config set --key region --value global   # 海外 API Key
```

执行 `mmx auth status` 确认当前 region 与 Key 来源平台一致。

***
