> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# StepAudio 3 TTS

> 真人级的说话表现

StepAudio 3 TTS 生成贴近真人的自然语音，在音色、语调、节奏和气口停顿上高度还原真实口语表现。[技术报告](https://arxiv.org/abs/2609.12945)｜[语音体验中心](https://www.stepfun.com/studio/audio?tab=tts)

## 模型信息

| 项目    | 内容                |
| :---- | :---------------- |
| 模型 ID | `stepaudio-3-tts` |
| 输入    | 文本、音频             |
| 输出    | 语音                |
| 计费    | 2.5 元 / 万字符       |
| 音色克隆  | 9.9 元 / 音色        |

## 核心能力

* **真人级的说话表现**：模型在音色基底、语调层次、节奏律动与气口停顿上高度贴合人类原生口语范式，彻底挣脱机器朗读的生硬桎梏与固化韵律模板。模型还原的不只是字面内容，更是人在说话时的最真实状态——笑声、咂嘴、迟疑、结巴、重复与改口等真人级口语表现，还能根据语义脉络自主推演情绪与语气的微妙变化。听到的始终是“一个人在说话”，而不是“一段被合成的语音”。
* **超低时延流式生成**：依托流式生成架构，一边生成一边输出，无需等待整句合成完成即可开始播放，可无缝对接实时对话业务链路，极大压缩交互等待窗口。

适合实时对话、语音助手和高表现力内容生成。

## API 端点

<Columns cols={2}>
  <Card title="非流式合成" href="/docs/zh/api-reference/audio/create-audio">
    `POST /v1/audio/speech`
  </Card>

  <Card title="流式合成" href="/docs/zh/api-reference/audio/ws-audio">
    `WebSocket /v1/realtime/audio`
  </Card>
</Columns>

## 相关资源

<Columns cols={2}>
  <Card title="语音大模型总览" icon="arrow-left" href="/docs/zh/guides/models/audio">
    返回 Audio 3 系列模型总览。
  </Card>

  <Card title="完整定价详情" icon="receipt" href="/docs/zh/guides/pricing/details">
    查看语音、文本、图像等全部模型的计费规则。
  </Card>

  <Card title="音色列表" icon="microphone" href="/docs/zh/guides/developer/tts#支持音色">
    查看官方提供的音色及参数说明。
  </Card>

  <Card title="Demo 与体验中心" icon="play" href="https://www.stepfun.com/studio/audio?tab=tts">
    在线快速体验 StepAudio 3 TTS 的完整能力。
  </Card>
</Columns>
