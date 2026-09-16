> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 音色复刻抽卡工具

> <Note> 本案例介绍 Voice ID Lucky Draw：一个把音色复刻从「一次出一个结果」升级为「批量生成 6 个候选并试听筛选」的开箱即用 Web 工具，基于 MiniMax 音色复刻与 T2A 接口构建。 </Note>

<div style={{display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px'}}>
  <div style={{width: '40px', height: '40px', borderRadius: '50%', background: 'linear-gradient(135deg, #6366f1, #8b5cf6)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'white', fontWeight: 'bold'}}>嘉</div>

  <div>
    <div style={{fontWeight: 500}}>嘉川</div>
    <div style={{fontSize: '0.875rem', color: '#9ca3af'}}>2026年5月21日</div>
  </div>
</div>

<a href="https://solution.minimaxi.com/voice-id-lucky-draw/" target="_blank" style={{display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '8px 16px', borderRadius: '8px', border: '1px solid #e5e7eb', textDecoration: 'none', color: 'inherit', marginBottom: '32px'}}>
  <svg height="20" width="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <polyline points="15 3 21 3 21 9" />

    <line x1="10" y1="14" x2="21" y2="3" />

    <path d="M21 14v5a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5" />
  </svg>

  在线试用
</a>

## 工具简介

**Voice ID Lucky Draw** 是一个面向 voice clone 质量调优场景的 Web 工具：用户上传一段长音频，系统自动切分并发起 6 次复刻（3 次 Zero-Shot + 3 次 One-Shot），返回 6 个候选 `voice_id`。用户可以像「抽卡」一样，在统一文案下试听比对每个候选音色，选出满意的一张再激活，**未被激活继续使用的候选不会产生复刻费**。

<img src="https://filecdn.minimax.chat/public/voice-id-lucky-draw-overview.png" alt="Voice ID Lucky Draw 工具界面：API Key 配置、试听文案选择、音频上传" style={{borderRadius: '8px', marginBottom: '24px', maxWidth: '100%'}} />

<Warning>
  **计费说明**：MiniMax 9.9 元的复刻费在**首次使用 `voice_id` 进行语音合成时**收取，因此未继续使用的候选确实不产生复刻费；但工具内 6 段试听音频的合成属于 T2A 调用，会按字符数收取语音合成费用。详见 [按量付费定价 — Voice Cloning](/docs/guides/pricing-paygo)。
</Warning>

***

## 为什么需要「抽卡」

同一段原始声音，在不同的切片、prompt 与复刻策略下，得到的 `voice_id` 可能在**相似度、情绪、稳定性、业务适配度**上各有差异。

传统流程一次只产出一个结果，要试出好音色往往需要反复上传、反复参数调整。Voice ID Lucky Draw 把这些差异**集中生成**出来，让用户在 6 个候选中挑出最满意的一张，显著提高音色复刻一次到位的概率。

<Columns cols={2}>
  <Card title="批量候选" icon="layers">
    一次操作产出 6 个候选 `voice_id`，Zero-Shot 与 One-Shot 策略各 3 次
  </Card>

  <Card title="统一试听" icon="play">
    所有候选用同一段试听文案合成，音色差异可横向对比
  </Card>

  <Card title="切分合规" icon="scissors">
    自动选择说话间隙切片，产出符合接口要求的 `clone_audio` 与 `prompt_audio`
  </Card>

  <Card title="未激活无复刻费" icon="badge-check">
    未继续使用的候选 `voice_id` 不产生 9.9 元复刻费用，降低试错成本
  </Card>
</Columns>

<Note>
  适用于音色复刻效果不稳定、希望一次操作横向比较多候选的场景。
</Note>

***

## 使用方法

<Steps>
  <Step title="填写凭证">
    在页面填写 MiniMax API Key 和 Group ID，信息保存在浏览器 localStorage，刷新后无需重复输入。
  </Step>

  <Step title="选择试听文案">
    系统内置电话客服、有声书旁白、短剧情绪配音、语音助手等场景文案，也可以直接编辑。统一试听文案的作用是保证所有候选 `voice_id` 用同一段文本合成，便于横向比较音色效果。
  </Step>

  <Step title="上传与切分音频">
    上传音频后，后端读取原始文件，进行转码、采样率处理和自动切分。切分逻辑会尽量选择说话间隙，生成两类语料：

    * `clone_audio`：普通复刻原始语料，每条**大于 10 秒**
    * `prompt_audio`：可选参考音频语料，每条**小于 8 秒**
  </Step>

  <Step title="ASR 与文本校对">
    `prompt_audio` 会进入 ASR，自动识别对应文字。因为 prompt\_audio 要求音频和文字一致，页面提供试听和文本编辑能力，用户可以**修正错字、补充标点**，确保 `prompt_text` 与音频内容严格对应。
  </Step>

  <Step title="批量发起复刻">
    完成切分后，系统批量发起复刻，组合 3 次 zero\_shot 和 3 次 one\_shot：

    * **zero\_shot**：主要使用切片语料
    * **one\_shot**：使用原始整段 clone 音频加 prompt 切片语料

    一次操作得到 6 个候选 `voice_id`。
  </Step>

  <Step title="试听筛选与激活">
    每个候选生成后，后端继续调用 T2A 合成接口，用同一段试听文案生成试听音频。前端以卡片形式展示生成状态、`voice_id`、试听播放器、复制按钮和选择激活按钮。用户听完后选中一个 `voice_id`，再进入激活确认和最终合成验证。
  </Step>
</Steps>

***

## 立即体验

<Card title="Voice ID Lucky Draw" icon="external-link" href="https://solution.minimaxi.com/voice-id-lucky-draw/">
  在线试用音色复刻抽卡工具，准备好 MiniMax API Key 与 Group ID 即可开始
</Card>

***

## 总结

Voice ID Lucky Draw 把音色复刻的「一发命中」难题转化为「批量候选 + 试听筛选」流程：

* **批量产出 6 个候选 `voice_id`**（Zero-Shot 3 次 + One-Shot 3 次），最大化挖掘原始音频的潜力
* **统一试听文案**让候选可横向比较
* **未继续使用的候选无复刻费**（试听合成仍按 T2A 字符数计费）降低尝试成本
* **整套流程开箱即用**，无需自己处理音频切分、ASR 与多次接口编排

***

## 相关资源

<Columns cols={3}>
  <Card title="语音复刻 API" icon="mic" href="/docs/guides/speech-voice-clone">
    接口文档与参数说明
  </Card>

  <Card title="T2A 合成 API" icon="volume-2" href="/docs/api-reference/speech-t2a-http">
    用 voice\_id 指定音色合成最终音频
  </Card>

  <Card title="MiniMax 开放平台" icon="globe" href="https://platform.minimaxi.com/user-center/basic-information">
    获取 API Key 与 Group ID
  </Card>
</Columns>
