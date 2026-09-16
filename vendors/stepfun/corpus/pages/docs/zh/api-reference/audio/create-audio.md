> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 语音合成

调用 TTS 模型将文本合成为语音，返回音频文件。

## 请求地址

`POST https://api.stepfun.com/v1/audio/speech`

<Note>
  Step Plan 场景请使用 `POST https://api.stepfun.com/step_plan/v1/audio/speech`
</Note>

## 请求参数

* `model` `string` ***required***<br />需要使用的模型名称，当前支持 `stepaudio-3-tts`、`stepaudio-2.5-tts`、`step-tts-2` 和 `step-tts-mini`。

  <Note>`step-tts-vivid` 模型名称不再推荐使用，但历史用户请求仍会继续支持。</Note>

* `input` `string` ***required***<br />要生成的文本，最大长度为 1000 个字符。在使用 `stepaudio-2.5-tts`、`stepaudio-3-tts` 时，括号 `()` 内的内容将作为指令处理，默认不发音；如需发音，请勿使用括号包裹。

* `voice` `string` ***required***<br />生成时使用的音色信息，支持[官方音色](/docs/zh/guides/developer/tts#官方音色清单)和开发者自生成音色。

* `response_format` `string` ***optional***<br />返回的音频格式，支持 `wav`、`mp3`、`flac`、`opus`、`pcm`，默认为 `mp3`。

* `speed` `float` ***optional***<br />语速，取值范围为 0.5\~2，默认值 1.0。0.5 表示 0.5 倍速。

* `volume` `float` ***optional***<br />音量，取值范围为 0.1\~2.0，默认值 1.0。0.1 表示缩小至 10% 音量；2.0 表示扩大至 200% 音量。

* `text_normalization` `string` ***optional***<br />文本归一化（Text Normalization）策略，可选值为 `standard` 和 `enhanced`，默认值为 `standard`。缺省（不传该参数）时按 `standard` 处理，与原有行为保持一致。
  * `standard`：标准归一化，适合实时对话等对时延敏感的场景。
  * `enhanced`：增强归一化，对数字、单位、英文、符号等的读法做更充分的处理，适合长文播报、正式播报等更看重合成效果的场景。

* `voice_label` `object` ***optional***<br />音色标签，使用自定义音色时需要传入。language、emotion 和 style 三个字段同一时间只能有一个有值，暂不支持多个组合。
  * `language` `string` ***optional***<br />语言，支持 `粤语`、`四川话`、`日语` 三个选项。
  * `emotion` `string` ***optional***<br />情绪，支持 `高兴`、`生气` 等最多 11 个选项， 不同模型的支持情况可参考[音色标签](/docs/zh/guides/developer/tts#音色标签)
  * `style` `string` ***optional***<br />支持最多17种语速或演绎风格，不同模型的支持情况可参考[音色标签](/docs/zh/guides/developer/tts#音色标签)

<Warning>
  注意：`stepaudio-2.5-tts`、`stepaudio-3-tts` 模型不支持该字段，若传入 `voice_label` 参数会报错。若使用上述模型，请直接使用 `instruction` 字段或文本内的 `()` 提示词控制情绪与风格。其他模型的支持情况可参考[音色标签](/docs/zh/guides/developer/tts#音色标签)。
</Warning>

* `instruction` `string` ***optional***<br />全局自然语言指导，用于设定整段音频的全局情绪基调、角色人设等。仅在使用 `stepaudio-2.5-tts`、`stepaudio-3-tts` 模型时生效；`stepaudio-2.5-tts` 最大支持 200 个字符，`stepaudio-3-tts` 最大支持 500 个字符。

* `sample_rate` `integer` ***optional*** <br />采样率，支持 8000、16000、22050、24000、48000 五个选项。默认值为 24000。采样率越高，音质越好，但文件体积也会更大。其中 48000 为最近几次迭代新增的采样率。

* `pronunciation_map` `object array` ***optional*** <br /> 定义某个文字或符号注音或发音替换规则，在中文文本中，声调用数字表示：一声为1，二声为2，三声为3，四声为4，轻声为5。
  * `tone`  `string`  ***required*** <br /> 具体发音映射规则，以“/”隔开，示例：`["绯闻/fei1闻","扁舟/偏舟","嫉妒/ji2妒"]`

* `stream_format` `string` ***optional*** <br /> 流式返回，默认为返回语音，支持值 `sse` 和 `audio`,默认为 `audio`。当传入 `sse` 时，音频将会以 SSE 的方式返回，数据包格式如下：

  ```text theme={null}
  data: {"type":"speech.audio.delta","audio":"<BASE64 编码的音频片段>"}

  data: {"type":"speech.audio.delta","audio":"<BASE64 编码的音频片段>"}

  data: {"type":"speech.audio.done","audio":""}

  data: [DONE]
  ```

  事件类型说明：

  * `speech.audio.delta`：音频数据分片，`audio` 字段为该分片的 BASE64 编码二进制，拼接所有分片即为完整音频
  * `speech.audio.done`：生成完成，`audio` 为空字符串
  * `speech.audio.error`：生成过程中出错

* `markdown_filter` `bool` ***optional*** <br /> 是否启用 Markdown 过滤。

* `return_url` `bool` ***optional*** <br /> 仅对非流式生效，是否以 URL 而不是二进制流的形式返回，URL 12 小时内有效。

* `timestamp` `bool` ***optional*** <br /> 词级时间戳（字幕）开关，置为 `true` 开启。开启后，服务端会返回每个切句的逐词时间轴（毫秒），可用于字幕高亮、卡拉 OK 式跟读、音画对齐等场景。字幕按两种模式投递：非流式需同时设置 `return_url=true`，字幕随文件 URL 一起返回；流式需设置 `stream_format="sse"`，字幕以 `response.subtitle` 事件随音频帧下发。两种模式的响应结构见[请求响应](#请求响应)。

  <Warning>
    开启 `timestamp` 时，必须满足 `return_url=true` 或 `stream_format="sse"` 之一。否则（如 `stream_format="audio"` 的裸音频流，或非流式但未设置 `return_url`）无法承载字幕，请求返回 HTTP 400：`timestamp requires return_url=true or stream_format=sse`。
  </Warning>

## 请求响应

默认返回合成的音频文件（二进制流）。

开启 `timestamp` 后，服务端会额外返回每个切句的逐词时间戳（字幕），按投递模式分为两种。词级时间戳的 `start_time` / `end_time` 均已累加前序切句时长，可直接用于整段音频定位；服务端会自动按长度对文本切句，较长的文本会被切分为多个切句、每个切句对应一条字幕。

### 非流式 + 文件 URL（`timestamp=true` + `return_url=true`）

响应为 JSON，在 `data` 中新增 `subtitles` 数组，每个切句一条：

```json theme={null}
{
  "created": 1782963404,
  "data": {
    "url": "https://.../xxxx.mp3",
    "subtitles": [
      {
        "text": "今天天气真好，我们出去玩吧！",
        "request_id": "c71567b716871b26176d305aab6a2a7e-0",
        "items": [
          { "text": "今", "start_time": 0, "end_time": 240 },
          { "text": "天", "start_time": 240, "end_time": 400 },
          { "text": "天", "start_time": 400, "end_time": 560 },
          { "text": "气", "start_time": 560, "end_time": 640 },
          { "text": "真", "start_time": 640, "end_time": 880 },
          { "text": "好，", "start_time": 880, "end_time": 1120 },
          { "text": "我", "start_time": 1840, "end_time": 2000 },
          { "text": "们", "start_time": 2000, "end_time": 2080 },
          { "text": "出", "start_time": 2080, "end_time": 2240 },
          { "text": "去", "start_time": 2240, "end_time": 2320 },
          { "text": "玩", "start_time": 2320, "end_time": 2560 },
          { "text": "吧！", "start_time": 2560, "end_time": 2800 }
        ],
        "timestamp": 1782963404434
      },
      {
        "text": "你想去公园还是去看电影呢？",
        "request_id": "c71567b716871b26176d305aab6a2a7e-1",
        "items": [
          { "text": "你", "start_time": 3440, "end_time": 3600 },
          { "text": "想", "start_time": 3600, "end_time": 3760 },
          { "text": "去", "start_time": 3760, "end_time": 3840 },
          { "text": "公", "start_time": 3840, "end_time": 4080 },
          { "text": "园", "start_time": 4080, "end_time": 4480 },
          { "text": "还", "start_time": 4640, "end_time": 4800 },
          { "text": "是", "start_time": 4800, "end_time": 4960 },
          { "text": "去", "start_time": 4960, "end_time": 5040 },
          { "text": "看", "start_time": 5040, "end_time": 5280 },
          { "text": "电", "start_time": 5280, "end_time": 5440 },
          { "text": "影", "start_time": 5440, "end_time": 5680 },
          { "text": "呢？", "start_time": 5680, "end_time": 5920 }
        ],
        "timestamp": 1782963404528
      }
    ]
  }
}
```

* `created` `int`<br />响应生成时间，Unix 时间戳，单位秒。
* `data.url` `string`<br />合成音频文件的下载 URL。
* `data.subtitles` `array`<br />字幕列表，每个切句一条；仅在 `timestamp=true` + `return_url=true` 时返回。

  <Expandable>
    * `text` `string`<br />切句文本。
    * `request_id` `string`<br />切句 ID。
    * `timestamp` `int64`<br />该条字幕的生成时间，单位毫秒。
    * `items` `array`<br />词级时间戳列表（对齐失败时可能为空）。

        <Expandable>
          * `text` `string`<br />分词文本。
          * `start_time` `int64`<br />词起始时间，单位毫秒，已累加前序切句时长。
          * `end_time` `int64`<br />词结束时间，单位毫秒，已累加前序切句时长。
        </Expandable>
  </Expandable>

### 流式 SSE（`timestamp=true` + `stream_format="sse"`）

在 SSE 流中，除音频帧 `speech.audio.delta` 外新增 `response.subtitle` 事件。每个切句对齐完成后下发一条，与音频帧在同一条流中交织下发，且所有字幕事件都会在 `speech.audio.done` 之前下发完毕：

```text theme={null}
data: {"type":"speech.audio.delta","audio":"<BASE64 音频分片>"}

data: {"type":"response.subtitle","event_id":"...","data":{ ... }}

data: {"type":"speech.audio.delta","audio":"<BASE64 音频分片>"}

data: {"type":"speech.audio.done","audio":""}

data: [DONE]
```

其中 `response.subtitle` 事件结构如下，`data` 与非流式 `subtitles[]` 的单个元素一致：

```json theme={null}
{
  "type": "response.subtitle",
  "event_id": "019f20e6858d73b5ad6da2f82af08ea5",
  "data": {
    "text": "今天天气真好，我们出去玩吧！",
    "request_id": "2b00a22c81e3c7f8f2a6378ac040df6f.019f20e6819a7aaab0d03ca8dc725e03",
    "items": [
      { "text": "今", "start_time": 0, "end_time": 160 },
      { "text": "天", "start_time": 160, "end_time": 320 },
      { "text": "天", "start_time": 320, "end_time": 480 },
      { "text": "气", "start_time": 480, "end_time": 560 },
      { "text": "真", "start_time": 560, "end_time": 720 },
      { "text": "好，", "start_time": 720, "end_time": 1120 },
      { "text": "我", "start_time": 1440, "end_time": 1520 },
      { "text": "们", "start_time": 1520, "end_time": 1680 },
      { "text": "出", "start_time": 1680, "end_time": 1760 },
      { "text": "去", "start_time": 1760, "end_time": 1920 },
      { "text": "玩", "start_time": 1920, "end_time": 2080 },
      { "text": "吧！", "start_time": 2080, "end_time": 2320 }
    ],
    "timestamp": 1782963406221
  }
}
```

* `type` `string`<br />事件类型，固定为 `response.subtitle`。
* `event_id` `string`<br />字幕事件 ID。
* `data` `object`<br />字幕内容，结构与非流式 `subtitles[]` 的单个元素一致（`text` / `request_id` / `items[]` / `timestamp`）。

## 示例

<Tabs>
  <Tab title="python">
    ```python theme={null}
    import os
    from pathlib import Path
    from openai import OpenAI

    speech_file_path = Path(__file__).parent / "step-tts.mp3"

    client = OpenAI(
        api_key=os.environ["STEPFUN_API_KEY"],
        base_url="https://api.stepfun.com/v1"
    )
    with client.audio.speech.with_streaming_response.create(
        model="step-tts-mini",
        voice="cixingnansheng",
        input="智能阶跃，十倍每个人的可能.",
        extra_body={
            "volume": 1.0,  # volume 在拓展参数里
            # 文本归一化：standard / enhanced，默认 standard
            "text_normalization": "standard",
            # voice_label 的 language / emotion / style 同一时间只能设其中一个
            "voice_label": {
                "emotion": "高兴"
            },
            "pronunciation_map": {
                "tone": [
                    "阿胶/e1胶",
                    "扁舟/偏舟",
                    "LOL/laugh out loudly"
                ]
            }
        }
    ) as response:
        response.stream_to_file(speech_file_path)
    ```
  </Tab>

  <Tab title="js">
    ```js theme={null}
    import OpenAI from "openai";
    import fs from "fs";
    import path from "path";

    const STEP_API_MODEL = "step-tts-mini";

    const openai = new OpenAI({
        apiKey: process.env.STEPFUN_API_KEY,
        baseURL: "https://api.stepfun.com/v1"
    });

    async function main() {
        const speechFile = path.resolve("./speech.mp3");
        const mp3 = await openai.audio.speech.create({
            model: STEP_API_MODEL,
            voice: "cixingnansheng",
            input: "智能阶跃，十倍每个人的可能.",
            extra_body: {
                volume: 2.0, // volume 在拓展参数里
                // 文本归一化：standard / enhanced，默认 standard
                text_normalization: "standard",
                // voice_label 的 language / emotion / style 同一时间只能设其中一个
                voice_label: {
                    emotion: "高兴"
                },
                pronunciation_map: {
                    tone: [
                        "阿胶/e1胶",
                        "扁舟/偏舟",
                        "LOL/laugh out loudly"
                    ]
                }
            }
        });
        console.log(speechFile);
        const buffer = Buffer.from(await mp3.arrayBuffer());
        await fs.promises.writeFile(speechFile, buffer);
    }

    main();
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl --location 'https://api.stepfun.com/v1/audio/speech' \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer $STEPFUN_API_KEY" \
      --data '{
        "model": "stepaudio-2.5-tts",
        "input": "2025 年第 4 季度营收同比增长 18.6%，约合 12.3 亿元。",
        "voice": "cixingnansheng",
        "text_normalization": "enhanced"
      }' \
      --output "step.mp3"
    ```
  </Tab>

  <Tab title="StepAudio 2.5 TTS (python)">
    ```python theme={null}
    import os
    from pathlib import Path
    from openai import OpenAI

    speech_file_path = Path(__file__).parent / "step-tts.mp3"

    client = OpenAI(
        api_key=os.environ["STEPFUN_API_KEY"],
        base_url="https://api.stepfun.com/v1"
    )
    with client.audio.speech.with_streaming_response.create(
        model="stepaudio-2.5-tts",
        voice="cixingnansheng",
        # 长度需 <=1000 字符；括号 () 内作为指令处理不发音，需发音文本请勿加括号
        input="（冷笑）你以为我们阶跃星辰北京公司的技术是开玩笑的吗！",
        extra_body={
            "volume": 1.0,  # volume 在拓展参数里
            # 文本归一化策略：standard / enhanced，默认 standard；enhanced 适合播报等更看重合成效果的场景
            "text_normalization": "enhanced",
            # 全局情绪指令，最长 200 字符
            "instruction": "语气极其愤怒，压迫感强，语速偏快",
            "pronunciation_map": {
                "tone": [
                    "阿胶/e1胶",
                    "扁舟/偏舟",
                    "LOL/laugh out loudly"
                ]
            }
        }
    ) as response:
        response.stream_to_file(speech_file_path)
    ```
  </Tab>

  <Tab title="字幕 · 非流式 (Python)">
    ```python theme={null}
    import os
    import requests

    url = "https://api.stepfun.com/v1/audio/speech"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['STEPFUN_API_KEY']}"
    }
    payload = {
        "model": "step-tts-mini",
        "input": "今天天气真好。我们出去玩吧。",
        "voice": "cixingnansheng",
        "response_format": "mp3",
        "sample_rate": 24000,
        # 开启字幕；非流式需同时设置 return_url=true，字幕随文件 URL 返回
        "return_url": True,
        "timestamp": True
    }

    result = requests.post(url, headers=headers, json=payload).json()

    # 音频文件下载地址
    print("音频地址:", result["data"]["url"])

    # 逐句、逐词时间戳
    for subtitle in result["data"]["subtitles"]:
        print(f"\n切句: {subtitle['text']}")
        for item in subtitle["items"]:
            print(f"  {item['text']}: {item['start_time']}ms - {item['end_time']}ms")
    ```
  </Tab>

  <Tab title="字幕 · 流式 SSE (Python)">
    ```python theme={null}
    import os
    import json
    import requests

    url = "https://api.stepfun.com/v1/audio/speech"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['STEPFUN_API_KEY']}"
    }
    payload = {
        "model": "step-tts-mini",
        "input": "今天天气真好。我们出去玩吧。",
        "voice": "cixingnansheng",
        "response_format": "mp3",
        "sample_rate": 24000,
        # 开启字幕；流式需设置 stream_format="sse"，字幕以 response.subtitle 事件下发
        "stream_format": "sse",
        "timestamp": True
    }

    resp = requests.post(url, headers=headers, json=payload, stream=True)

    audio_chunks = []
    for line in resp.iter_lines():
        if not line:
            continue
        line = line.decode("utf-8")
        if not line.startswith("data: "):
            continue
        data_str = line[6:]
        if data_str == "[DONE]":
            break
        event = json.loads(data_str)

        if event["type"] == "speech.audio.delta":
            # 音频分片：BASE64，拼接后即完整音频
            audio_chunks.append(event["audio"])
        elif event["type"] == "response.subtitle":
            # 字幕事件：该切句的逐词时间戳
            data = event["data"]
            print(f"字幕: {data['text']}")
            for item in data["items"]:
                print(f"  {item['text']}: {item['start_time']}ms - {item['end_time']}ms")
        elif event["type"] == "speech.audio.done":
            print("音频生成完成")
    ```
  </Tab>
</Tabs>
