> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax × OpenClaw 应用 Demo 集合

> <Note>本系列收录把 OpenClaw 接到真实硬件、外部服务和复杂工作流中的实际 demo。所有 demo 默认以 MiniMax M3 作为底层模型，假设你已完成 [OpenClaw 接入指南](/docs/token-plan/openclaw)中的基础配置。</Note>

<div style={{display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px'}}>
  <div style={{width: '40px', height: '40px', borderRadius: '50%', background: 'linear-gradient(135deg, #6366f1, #8b5cf6)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'white', fontWeight: 'bold'}}>B</div>

  <div>
    <div style={{fontWeight: 500}}>Blue</div>
    <div style={{fontSize: '0.875rem', color: '#9ca3af'}}>2026年5月21日</div>
  </div>
</div>

## Demo 导航

<Columns cols={3}>
  <Card title="01 · OpenClaw 陪伴·多模态生成" icon="sparkles" href="#demo-1">
    在 OpenClaw 对话中调用 MiniMax 多模态模型，生成语音、图像、视频、音乐内容。
  </Card>

  <Card title="02 · 每日 AI 资讯播报" icon="newspaper" href="#demo-2">
    OpenClaw 内置 cron 每天定时抓取多源 AI 资讯，整理成文字日报 + 语音播报，推送到飞书群。
  </Card>

  <Card title="03 · 米家智能家居控制" icon="house" href="#demo-3">
    通过 MCP 协议把米家（Mijia）智能设备接入 OpenClaw，用自然语言开关灯、调节空调。
  </Card>
</Columns>

***

<h2 id="demo-1">
  01：OpenClaw 陪伴——多模态能力
</h2>

通过对接 MiniMax 多模态工具 skill，让 OpenClaw 能在对话中直接为你生成语音、图像、视频、音乐等内容，把“文字助手”升级为更接近真实陪伴的体验。

### 能力一览

* **语音（TTS）**：用 MiniMax 语音模型把任意文本读出来，支持音色定制、声音克隆、多段拼接。
* **图像生成**：一句话生成图片，适合做封面、配图、灵感稿。
* **视频生成**：从文本或参考图生成短视频。
* **音乐创作**：生成完整歌曲或纯音乐片段。

### 视频演示

<video controls src="https://filecdn.minimax.chat/public/openclaw-demo-multimodal.mp4" style={{borderRadius: '8px', marginTop: '12px', maxWidth: '100%'}} />

<Tip>
  在 OpenClaw 中配置 [MiniMax-Multimodal-Toolkit skill](https://clawhub.ai/minimax-ai-dev/minimax-multimodal) 即可快速解锁上述多模态能力。
</Tip>

***

<h2 id="demo-2">
  02：OpenClaw 每日 AI 资讯播报
</h2>

让 OpenClaw 每天清晨自动抓取 GitHub Trending、Hacker News、OpenAI Blog 等多源 AI 资讯，整理成文字日报 + 中文新闻女主播语音播报，定时推送到飞书群。整个流程通过 OpenClaw 内置 cron 加一个内容生成 skill 完成。

### 前置准备

开始前请确认以下三项已就绪：

* **`mmx-cli` 已装并登录**：用于调用 MiniMax 语音模型生成播报音频，配置方法参考 [MiniMax CLI](/docs/token-plan/minimax-cli)。
* **安装 `ffmpeg`**：用于把 mp3 转成飞书 IM 推荐的 opus 格式（libopus 单声道 16 kHz）。macOS 用 `brew install ffmpeg`，Linux 用 `sudo apt install ffmpeg`，Windows 用 `winget install Gyan.FFmpeg` 或从 [FFmpeg 官网](https://ffmpeg.org/download.html) 下载安装。
* **目标接受日报的飞书会话的 chat\_id**：打开你与 OpenClaw 的飞书会话，点击右上角设置，展开会话信息栏后滑动到最下方获取形如 `oc_xxxx` 的会话 id，后面 cron 推送会用到。

### 配置流程

整个 demo 用 3 段提示词完成：让 OpenClaw 创建内容生成 skill、跑端到端验证、注册 cron 定时任务（其中内容设置可按需调整）。

<Steps>
  <Step title="创建 daily-ai-briefing skill">
    在 OpenClaw 对话窗口发送以下提示词，让 Agent 自动写好 SKILL.md 并跑一次端到端验证：

    ```plaintext theme={null}
    请新建 skill: daily-ai-briefing,定位为内容生成 skill —— 抓多源 → 整合 → 写文字日报 → 生成播报语音。

    # 一、内容设置
    - topic: LLM 模型 / AI Agent / 多模态进展 / AI 创业融资
    - sources(5 个):
      - GitHub Trending https://github.com/trending?since=daily
      - Hacker News https://news.ycombinator.com/
      - OpenAI Blog https://openai.com/blog/
      - Anthropic News https://www.anthropic.com/news
      - Google AI Blog https://ai.googleblog.com/
    - 每源 2-3 条,去重后总 8-10 条
    - 日报格式:分 source 分小节,每条「标题 + 一句话中文摘要(≤50 字) + 原文链接」,无 emoji 无装饰

    # 二、语音参数
    - TTS 工具: 使用 mmx-cli 命令行工具; 
    - voice id设置为 "Chinese (Mandarin)_News_Anchor" (MiniMax 中文新闻女主播音色)
    - 播报稿: 300-500 字纯文字,无 link / markdown / emoji,口头播报风格,目标音频 ≤90 秒
    - 输出目录: ~/.openclaw/workspace/minimax-output/

    # 三、超时
    - 每源 curl --max-time 15, 整体 fetch ≤60 秒
    - mmx speech synthesize ≤90 秒
    - 任一 source 失败: 跳过并在末尾"数据来源"行注明, 不阻塞整体

    # 四、WORKFLOW(6 步)
    1. 抓取多源(按 sources 并行 curl)
    2. 去重排序(URL 去重 → 时间排序 → 每源保留 2-3 条)
    3. 生成文字日报 markdown(分 source 分小节)
    4. 生成 300-500 字播报稿(纯文字、口语化)
    5. 用 mmx speech synthesize 命令合成 mp3
    6. ffmpeg -y -i <mp3> -acodec libopus -ac 1 -ar 16000 <对应 .opus> ，转换音频格式 mp3 → opus 

    # 五、OUTPUT 契约 (skill执行完必须返回这两项)
    - text_markdown: 完整文字日报 markdown 字符串
    - audio_path: 生成的 opus 音频文件的绝对路径

    # 六、产出要求
    1. 创建 ~/.openclaw/skills/daily-ai-briefing/SKILL.md,首部含 YAML frontmatter
       (至少 `name: daily-ai-briefing` + 含触发关键词如 "AI 日报" / "daily AI briefing" 的 description),
       含 CONFIG 段(topic / sources / voice,用户可自由 edit)+ 上面的 6 步 WORKFLOW + OUTPUT 契约
    2. 跑一次端到端验证(不调任何外部推送),报告:
       A. 文字日报实际生成了哪 N 条(贴缩略 markdown)
       B. 音频绝对路径 + 大小(KB) + 时长(秒) + 实际用的 voice id
       C. 每 source 状态(成功 / 失败 / 跳过)
    ```

    Agent 会把 SKILL.md 写到 `~/.openclaw/skills/daily-ai-briefing/`，跑完整 workflow，返回文字日报 markdown 和 opus 音频文件的绝对路径。

    <Tip>
      默认的 `Chinese (Mandarin)_News_Anchor` 是 MiniMax 提供的“中文新闻女主播”系统音色，适合资讯播报。想换其他音色，跑 `mmx speech voices` 查看完整可用列表，把心仪的 voice id 填进 SKILL.md 的 CONFIG 段中 VOICE 字段即可。常用替代：

      * `Chinese (Mandarin)_Reliable_Executive` —— 沉稳男声
      * `Chinese (Mandarin)_Warm_Bestie` —— 温暖女声
    </Tip>
  </Step>

  <Step title="验证完整 workflow">
    skill 创建后再跑一次确认稳定性：

    ```plaintext theme={null}
    按 daily-ai-briefing skill 的 WORKFLOW 完成一次内容生成(不调任何外部推送)。
    报告:文字日报实际生成了哪 N 条(贴一份缩略 markdown)、音频文件绝对路径 + 
    大小(KB)+ 时长(秒)+ 实际使用的 voice id、每 source 状态(成功/失败/跳过)。
    ```

    期望看到 `~/.openclaw/workspace/minimax-output/daily-briefing-YYYYMMDD.opus`(90 秒约 200-400 KB)。海外 source（如 Google AI Blog）国内访问可能不稳，workflow 会自动跳过并在末尾“数据来源”行注明，不阻塞整体流程。
  </Step>

  <Step title="注册 cron 定时推送">
    skill 验证通过后，让 OpenClaw 注册 cron（把 `oc_xxxx` 替换为你的 chat\_id）:

    ```plaintext theme={null}
    请创建一个 OpenClaw cron 任务:

    # 一、调度参数
    - name: AI日报
    - cron: 3 9 * * *(每天 09:03)
    - tz: Asia/Shanghai
    - session: isolated(独立会话,不污染主对话历史)
    - timeout-seconds: 900(完整链路实测 100-600 秒,留充足余量)
    - --no-deliver(agent 已在 prompt 内用 message 工具推送,避免重复)

    # 二、触发时执行的 prompt(完整传入 --message)

    执行今日 AI 日报推送,共 3 步。

    Step 1 — 调 daily-ai-briefing skill 生成内容
    按 ~/.openclaw/skills/daily-ai-briefing/SKILL.md 的 WORKFLOW 执行，必须由你自己在当前会话顺序执行skill中的 6 步（不要 sessions
        +_spawn / sessions_yield 派子 agent），拿到 OUTPUT 两项:
      - text_markdown: 文字日报 markdown 字符串
      - audio_path: 生成的 opus 音频文件绝对路径

    Step 2 — 用 message 工具发文字
    参数: action=send, channel=feishu, target=oc_xxxx, message=<text_markdown>
    记返回的 message_id 为 TEXT_MID。

    Step 3 — 用 message 工具发音频
    参数: action=send, channel=feishu, target=oc_xxxx, media=<audio_path 的 opus 绝对路径>
    OpenClaw 内部会自动上传文件、解析 duration、发 audio 类型消息。
    记返回的 message_id 为 AUDIO_MID。

    # 三、最终报告(注册完输出)
    - 文字 message_id: <TEXT_MID>
    - 语音 message_id: <AUDIO_MID>
    - opus 文件大小(KB) + 音频时长(秒)
    - 失败源列表(skill Step 1 跳过的 source)
    - cron job-id(用于后续 `openclaw cron run <job-id>` 立刻验证)
    ```
  </Step>

  <Step title="验证测试">
    可以等到第二天所设定时刻是否收到日报，也可以在会话中要求 openclaw 直接执行一次“每日资讯播报”的cron job进行测试。

    <img src="https://filecdn.minimax.chat/public/openclaw-demo-news-cron.png" alt="OpenClaw cron 任务注册成功" style={{borderRadius: '8px', marginTop: '12px', maxWidth: '100%'}} />

    <Note>
      语音生成大约需要2-3min，故收到文本内容整理完成的提示后，可能需等待一段时间才会收到完整的文字和语音播报内容.
    </Note>
  </Step>
</Steps>

***

<h2 id="demo-3">
  03：用 OpenClaw 接管米家智能家居
</h2>

把家里的米家智能设备（灯、空调、扫地机等）交给 OpenClaw 之后，你可以在飞书中用一句话触发设备动作，例如“把卧室灯调暗一点”、“客厅温度太低，帮我升 2 度”。

<Note>
  **适用范围**：本 demo 适用于所有可通过米家 App 控制的设备。
</Note>

### 整体架构

整体链路是 **自然语言 → OpenClaw → mcporter → miot-mcp → 米家云 → 智能设备**:OpenClaw 把对话意图翻译成 MCP 工具调用，经由 [mcporter](/docs/solutions/openclaw#接入飞书) 转发到 [miot-mcp](https://github.com/javen-yan/miot-mcp)，后者通过米家官方 MIoT 协议下发到具体设备。

### 实现步骤

整个 demo 全程在 OpenClaw 对话窗口完成，无需手动写命令——把下面的提示词依次发给 OpenClaw 即可。

<Steps>
  <Step title="搜索并安装 miot-mcp">
    在 OpenClaw 对话窗口里发送以下提示词，让 Agent 自动完成 MCP 安装与配置：

    ```plaintext theme={null}
    我想把米家设备接入 OpenClaw,请先安装米家 MCP:https://github.com/javen-yan/miot-mcp
    通过 mcporter skill 接入 OpenClaw,并完成 MCP 配置。

    安装完成后,请确认 ~/.openclaw/skills/mcporter/SKILL.md 文件存在。
    ```

    Agent 会自动完成：克隆 miot-mcp 仓库 → 写入 `mcporter.json` → 校验 SKILL 文件可读。
  </Step>

  <Step title="配置米家账号认证">
    miot-mcp 支持两种认证方式，**推荐使用环境变量**，适合远程操控场景。

    <Tabs>
      <Tab title="环境变量（推荐）">
        在 OpenClaw 对话中提供米家账号：

        ```plaintext theme={null}
        对米家 MCP 进行账号认证配置。
        我的米家账号是:189xxxxxxxx,密码是:xxxxxx。
        ```

        Agent 会把账号写入环境变量：

        ```bash theme={null}
        export MIJIA_USERNAME="账号"
        export MIJIA_PASSWORD="密码"
        ```

        <Warning>
          请确认 Agent 写入的配置路径与你的环境一致，避免被覆盖。
        </Warning>
      </Tab>

      <Tab title="扫码登录">
        miot-mcp 也支持扫码登录，会在 OpenClaw 部署端弹出二维码，用米家 App 扫码即可。

        <Note>
          扫码方式不适合远程操控 OpenClaw 的场景，因为二维码弹窗只在本机显示。
        </Note>
      </Tab>
    </Tabs>
  </Step>

  <Step title="验证连接并发现设备">
    用一句话让 OpenClaw 自检，并返回当前账号下的所有米家设备：

    ```plaintext theme={null}
    帮我验证一下米家 MCP 连接是否正常,请给出当前我的米家设备列表。
    ```

    <img src="https://filecdn.minimax.chat/public/openclaw-demo-devices.png" alt="米家设备列表展示效果" style={{borderRadius: '8px', marginTop: '12px', maxWidth: '100%'}} />

    <Note>
      **设备添加方法**：在米家 App 中连接智能设备即可，MCP 会通过米家账号自动获取设备列表。
    </Note>
  </Step>

  <Step title="基本调用测试">
    设备列表确认无误后，直接用自然语言让 OpenClaw 控制具体设备，例如“打开卧室灯”、“把客厅空调调到 24 度”:

    <img src="https://filecdn.minimax.chat/public/openclaw-demo-control.png" alt="OpenClaw 基本调用测试" style={{borderRadius: '8px', marginTop: '12px', maxWidth: '100%'}} />
  </Step>

  <Step title="遇到问题让 Agent 自己排查">
    某个品牌的灯具或空调可能用了非标准的 MIoT 接口，首次调用容易报错。把现象描述给 OpenClaw，让它自己查规范、改参数：

    ```plaintext theme={null}
    我想控制设备(描述你的需求和具体设备,比如:调亮卧室灯、xxx 品牌灯具),但是遇到问题(描述问题现象)。
    请分析可能的原因,搜索官方 MIoT 规范库关于这个设备的正确接口调用参数,并参考 miot-mcp 的文档,修复上述问题。
    ```

    OpenClaw 会调用 web 搜索 + 阅读 miot-mcp 源码，自动修正 `siid`/`piid` 参数，直到设备真正生效。

    <img src="https://filecdn.minimax.chat/public/openclaw-demo-debugging.png" alt="OpenClaw 自动排查设备调试问题" style={{borderRadius: '8px', marginTop: '12px', maxWidth: '100%'}} />
  </Step>
</Steps>

### 进阶：让 OpenClaw 按日程自动开灯

相比传统智能家居的“固定时间开关”,OpenClaw 可以**结合你的真实日程**做个性化触发。下面这段提示词把“日程检查 + 卧室灯定时开”的整个 cron 配置一次性交给 OpenClaw，所有踩过的坑（`device_id` 类型、`--session isolated`、delivery 路径等）都已写死在 prompt 里，直接复制使用即可。

<Accordion title="完整提示词（直接复制到 OpenClaw 对话窗口）">
  ```markdown theme={null}
  帮我设置一个"日程检查 + 卧室灯提醒"的自动化任务,按以下规格用 openclaw cron add 创建主任务,主任务每天触发后由 LLM 创建当日的一次性子任务执行开灯。

  【主任务（cron job）规格】
  - 名称：卧室灯日程检查
  - schedule：每天北京时间 5:30（cron 表达式 30 5 * * *,tz=Asia/Shanghai）
  - session：isolated
  - timeoutSeconds：900（默认 600 经常超时,提到 900 给 LLM + 工具调用更多余量）
  - delivery：{"mode":"announce","channel":"feishu","to":"chat:<我和你 1:1 DM 的 oc_chat_id>"}

  【主任务 message（即每天 5:30 LLM 收到的 prompt）】
  请执行日程检查 + 开灯任务：
  1. date +%Y-%m-%d 拿今日日期
  2. feishu_calendar_event list 查今日上午 (00:00-12:00) 日程
  3. 如果有日程：开灯时间 = 第一个日程开始时间 - 20 分钟。用 openclaw cron add 创建一次性子任务,参数严格如下：
       --name "卧室灯-<今日日期>"
       --at <开灯时间 ISO,+08:00 时区>
       --session isolated   
       --delete-after-run
       --timeout-seconds 120
       --message "请执行开灯：mcporter call mijia.set_property_value --args '{"device_id":"<我的卧室灯 device_id>","siid":2,"piid":1,"value":true}'。
                  ⚠️ 整条命令照抄。--args 后用单引号包裹 JSON,JSON 内字段名/值用普通双引号（不要加反斜杠转义）。
                  执行后必须严格按以下规则写 summary（先看 result 字段值,再决定）：
                  - mcporter 返回 JSON 里 result 是 true ⇒ 写 ✅ 卧室灯已打开
                  - mcporter 返回 JSON 里 result 是 false ⇒ 必须以 ❌ 开头并贴出完整 JSON（命令送达但设备未生效,可能 device_id 错、设备离线、协议拒绝）。严禁写已开灯
                  - mcporter 输出含 Error/error/validation 字样 ⇒ 必须以 ❌ 开头原文贴出错误信息"
       delivery：{"mode":"announce","channel":"feishu","to":"chat:<同主任务的 chat_id>"}
  4. 如果没有日程：发简短确认消息"📅 今天上午暂无日程,不开灯"

  【重要】
  - 不要自己 call 飞书发消息工具！通知由 cron delivery 自动完成,你只需在回复中总结日程情况
  - 子任务的 mcporter 命令必须用 --args JSON 写法,不要写成 device_id=纯数字（int 报错）也不要写成 device_id=string:... （mcporter 不支持该前缀,会把字符串字面传给 mijia 导致 result: false）
  - 子任务一定要 --session isolated；否则带 channel 的 delivery 会被 cron 系统拒
  - 子任务 summary 必须先看 mcporter 返回 JSON 里 result 字段的值再决定 ✅/❌；result: false 时灯实际没开,禁止写"已开灯"
  ```
</Accordion>

<img src="https://filecdn.minimax.chat/public/openclaw-demo-advanced.png" alt="OpenClaw 日程联动开灯效果" style={{borderRadius: '8px', marginTop: '12px', maxWidth: '100%'}} />

<Tip>
  **delivery 路径**：用 `"to":"chat:..."` 以机器人身份发送消息，不要用 `user:<open_id>`——后者要求应用具备 `im:message.send_as_user` 权限。\
  **chat\_id 在哪找**：打开你与 OpenClaw 的飞书会话，点击右上角设置展开会话信息栏后滑动到最下方获取“会话 ID”。
</Tip>

***

## 相关资源

<Columns cols={3}>
  <Card title="OpenClaw 接入指南" icon="book-open" href="/docs/token-plan/openclaw">
    在开始本 demo 前，先完成 OpenClaw 安装和 MiniMax M3 模型配置
  </Card>

  <Card title="MiniMax M3" icon="sparkles" href="https://www.minimaxi.com/models/text/m3">
    驱动本 demo 的底层模型介绍
  </Card>

  <Card title="Token Plan" icon="credit-card" href="https://platform.minimaxi.com/subscribe/token-plan">
    通过 Token Plan 订阅 MiniMax 模型 API
  </Card>
</Columns>
