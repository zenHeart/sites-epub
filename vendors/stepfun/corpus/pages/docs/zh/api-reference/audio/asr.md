> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 音频文件识别

将音频文件中的人声内容异步识别为文本，适合较长音频的离线转写。当前支持中英文识别（暂不支持中文方言及其他语种），支持分句与字 / 词级时间戳、双声道分轨、说话人识别（Speaker Diarization），暂不支持热词。推荐使用模型 `stepaudio-2.5-asr`。

<Info>
  如需实时流式识别，请参考 [流式语音识别（双向流式）](/docs/zh/api-reference/audio/asr-stream) 或 [语音识别（流式返回文本）](/docs/zh/api-reference/audio/asr-sse)。
</Info>

## 提交任务

创建一个新的语音识别任务。

请求地址：`POST https://api.stepfun.com/v1/audio/asr/file/submit`

### 请求头

* `Authorization` `string` ***required***<br />认证令牌，格式为 `Bearer $STEPFUN_API_KEY`。
* `Content-Type` `string` ***required***<br />固定为 `application/json`。
* `X-Trace-Id` `string` ***optional***<br />调用方自定义 Trace ID；不传则由服务端生成。
* `X-Request-Id` `string` ***optional***<br />调用方自定义 Request ID；不传则由服务端生成。

### 请求参数

* `audio` `object` ***required***<br />音频配置。`format` 必填；`pcm` 格式需额外填写采样率等相关参数。

  <Expandable>
    * `format` `string` ***required***<br />音频容器格式，支持 `wav`、`mp3`、`pcm`、`ogg`、`m4a`。
    * `codec` `string`<br />编码格式，可选 `raw` / `opus`，默认 `raw`（pcm）。
    * `rate` `int`<br />采样率；`pcm` 格式必填。
    * `bits` `int`<br />采样位深，默认 `16`，当前仅支持 16bit。
    * `channel` `int`<br />声道数，`1`（单声道）/ `2`（双声道），默认 `1`；须与音频实际声道数一致。
    * `url` `string`<br />公网可访问的音频文件地址，支持 `wav`、`mp3`、`ogg`、`pcm`、`m4a`，文件需小于 100MB。
  </Expandable>

* `request` `object` ***required***<br />识别配置：模型能力与输出格式。

  <Expandable>
    * `model_name` `string` ***required***<br />模型名称，例如 `stepaudio-2.5-asr`、`step-asr-1.1`。
    * `enable_channel_split` `bool` ***optional***<br />是否启用双声道分轨识别，默认 `false`；前提是 `audio.channel` 为 `2`。
    * `show_utterances` `bool` ***optional***<br />是否输出分句、分词及时间戳信息，默认 `false`。
    * `enable_speaker_info` `bool` ***optional***<br />是否启用说话人识别，默认 `false`；开启后每个 utterance 附带 `speaker.id`，需同时设置 `show_utterances=true`。单个任务最多可区分 10 个说话人。
  </Expandable>

### 请求示例

```json theme={null}
{
  "audio": {
    "format": "wav",
    "codec": "pcm",
    "rate": 16000,
    "bits": 16,
    "channel": 1,
    "url": "https://example.com/audio.wav"
  },
  "request": {
    "model_name": "stepaudio-2.5-asr",
    "enable_channel_split": false,
    "show_utterances": false
  }
}
```

### 返回

* `task_id` `string`<br />任务 ID，用于后续查询结果。

```json theme={null}
{
  "task_id": "018f2f1a-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

## 查询结果

根据任务 ID 查询识别进度或获取最终结果。

请求地址：`POST https://api.stepfun.com/v1/audio/asr/file/query`

### 请求参数

* `task_id` `string` ***required***<br />提交任务时返回的任务 ID。

### 返回字段

* `status` `string`<br />任务状态。排队中返回 `PENDING`、运行中返回 `RUNNING`，此时响应体仅含该字段；处理失败时返回 `FAILED`。

* `error` `object`<br />失败原因，仅 `status` 为 `FAILED` 时返回。

  <Expandable>
    * `stage` `string`<br />失败阶段，例如 `audio_download`（音频下载失败）。
    * `message` `string`<br />失败描述，例如 `invalid audio url`。
  </Expandable>

* `duration` `float`<br />音频时长（秒），仅识别成功时返回。

* `result` `object array`<br />识别结果，仅识别成功时返回。

  <Expandable>
    * `text` `string`<br />整段音频的识别文本。
    * `utterances` `object array`<br />分句信息，开启 `show_utterances` 时返回。

        <Expandable>
          * `text` `string`<br />分句文本。

          * `start_time` `int`<br />分句起始时间（毫秒）。

          * `end_time` `int`<br />分句结束时间（毫秒）。

          * `words` `object array`<br />字 / 词级信息。

                <Expandable>
                  * `text` `string`<br />字 / 词文本。
                  * `start_time` `int`<br />起始时间（毫秒）。
                  * `end_time` `int`<br />结束时间（毫秒）。
                </Expandable>

          * `speaker` `object`<br />该句所属说话人，开启 `enable_speaker_info` 且 `show_utterances=true` 时返回。

                <Expandable>
                  * `id` `string`<br />说话人 ID（如 `spk_1`），同一任务内稳定、跨任务不保证。
                </Expandable>
        </Expandable>
  </Expandable>

#### 示例

处理中（排队时返回 `PENDING`，运行中返回 `RUNNING`）：

```json theme={null}
{ "status": "RUNNING" }
```

处理成功：

```json theme={null}
{
  "duration": 5.901375,
  "result": [
    {
      "text": "识别出的完整文本",
      "utterances": [
        {
          "text": "你好",
          "start_time": 0,
          "end_time": 500,
          "words": [
            { "text": "你", "start_time": 0, "end_time": 200 },
            { "text": "好", "start_time": 200, "end_time": 500 }
          ]
        }
      ]
    }
  ]
}
```

处理失败：

```json theme={null}
{
  "status": "FAILED",
  "error": {
    "stage": "audio_download",
    "message": "invalid audio url"
  }
}
```

### 声道拆分说明

当 `enable_channel_split=true` 且输入为立体声时，服务端会拆分为多个声道分别识别，`result` 数组长度可能为 2，每个元素对应一个声道的输出。

### 说话人识别说明

在本接口可选开启说话人识别：

* `enable_speaker_info=true`：每个 utterance 附带 `speaker.id`，标识该句属于哪个说话人。需同时设置 `show_utterances=true`（`speaker.id` 挂在 utterance 下，无 utterances 则无处体现）。
* 单个任务最多可区分 10 个说话人。
* `speaker.id`（如 `spk_1`）同一任务内稳定、跨任务不保证。
* 可与 `enable_channel_split` 并存：分声道后在各声道内再区分说话人。

请求示例（开启说话人识别）：

```json theme={null}
{
  "audio": { "format": "wav", "url": "https://example.com/meeting.wav" },
  "request": {
    "model_name": "stepaudio-2.5-asr",
    "show_utterances": true,
    "enable_speaker_info": true
  }
}
```

返回示例（含说话人标记，节选）：

```json theme={null}
{
  "duration": 8.5,
  "result": [
    {
      "text": "你好请问有什么可以帮助您的吗在的我想咨询一下退款流程",
      "utterances": [
        { "text": "你好请问有什么可以帮助您的吗", "start_time": 0, "end_time": 1820, "speaker": { "id": "spk_1" } },
        { "text": "在的我想咨询一下退款流程", "start_time": 2000, "end_time": 4500, "speaker": { "id": "spk_2" } }
      ]
    }
  ]
}
```

## 错误处理

接口以标准 JSON 错误响应返回失败原因（HTTP 状态码与错误结构以网关 / 服务端实现为准）。常见场景：

* 鉴权失败：未提供或提供了错误的 `Authorization` 头（`Bearer $STEPFUN_API_KEY`）。
* 模型不支持：`request.model_name` 非 `stepaudio-2.5-asr`。
* 限流 / 白名单限制：请求被限流或不在白名单。
* 任务不存在：`task_id` 不存在或不属于当前 uid。
* 任务失败：后台处理失败（下载失败 / 转码失败 / 识别失败等）。

完整错误码参见 [错误码](/docs/zh/api-reference/error-codes)。

## 示例

<Tabs>
  <Tab title="提交任务">
    ```bash theme={null}
    curl -sS -X POST "https://api.stepfun.com/v1/audio/asr/file/submit" \
        -H 'Content-Type: application/json' \
        -H 'Authorization: Bearer $STEPFUN_API_KEY' \
        -d '{
            "audio": {
                "format": "wav",
                "codec": "pcm",
                "rate": 16000,
                "bits": 16,
                "channel": 1,
                "url": "https://example.com/audio.wav"
            },
            "request": {
                "model_name": "stepaudio-2.5-asr",
                "enable_channel_split": false,
                "show_utterances": true
            }
        }'
    ```
  </Tab>

  <Tab title="轮询查询">
    ```bash theme={null}
    curl -sS -X POST "https://api.stepfun.com/v1/audio/asr/file/query" \
        -H 'Content-Type: application/json' \
        -H 'Authorization: Bearer $STEPFUN_API_KEY' \
        -d '{"task_id":"018f2f1a-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}'
    ```
  </Tab>
</Tabs>

## 最佳实践

* 轮询节流：建议 1s\~3s 轮询一次，避免过于频繁造成限流。
* 超时控制：客户端设置总体超时，避免无限等待。
* URL 可达性：确保 `audio.url` 可被服务端直接下载（建议 HTTPS、可公网访问，或在服务网络内可访问）。
* 结果粒度：只需整段文本时用 `show_utterances=false`；需要时间戳 / 字幕对齐时用 `show_utterances=true`。
* 声道拆分：双人对话、左右声道分别录制的场景可开启 `enable_channel_split=true`。

## 音频建议

* 优先使用清晰、背景噪音较少的录音。
* 若可控制录制格式，建议 16kHz / 16bit / 单声道。
* 立体声场景如需分别识别两路说话人，可开启声道拆分。
