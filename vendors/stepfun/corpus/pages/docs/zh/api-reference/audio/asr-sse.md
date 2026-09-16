> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 语音识别（流式返回文本）

基于 HTTP + SSE 的语音识别：一次性提交音频，服务端通过 SSE 持续推送增量与最终识别结果，适合服务端调用、文件转写、准实时处理。推荐使用模型 `stepaudio-3-asr-max`。

<Info>
  如需基于 WebSocket 的实时双向流式识别，请参考 [流式语音识别（双向流式）](/docs/zh/api-reference/audio/asr-stream)。
</Info>

## 服务地址

`POST https://api.stepfun.com/v1/audio/asr/sse`

<Note>
  Step Plan 场景请使用 `POST https://api.stepfun.com/step_plan/v1/audio/asr/sse`。
</Note>

## 请求头

* `Content-Type` `string` ***required***<br />固定为 `application/json`。
* `Accept` `string` ***required***<br />固定为 `text/event-stream`。
* `Authorization` `string` ***required***<br />认证令牌，格式为 `Bearer $STEPFUN_API_KEY`。

## 请求参数

* `audio` `object` ***required***<br />音频数据与识别配置。

  <Expandable>
    * `data` `string` ***required***<br />Base64 编码的音频数据。
    * `input` `object` ***required***<br />识别与音频格式配置。

        <Expandable>
          * `transcription` `object`<br />识别配置。

                <Expandable>
                  * `language` `string`<br />识别语言，如 `zh`。
                  * `hotwords` `array`<br />热词列表，形如 `["热词1", "热词2"]`。
                  * `model` `string`<br />模型名称，支持 `stepaudio-3-asr-max`、`stepaudio-2.5-asr`、`stepaudio-2-asr-pro`。
                  * `enable_itn` `bool` ***optional***<br />是否开启 ITN 文本规范化，默认 `true`。
                  * `enable_timestamp` `bool` ***optional***<br />是否返回识别文本对应的音频时间戳，默认 `false`。
                </Expandable>

          * `format` `object`<br />音频格式。

                <Expandable>
                  * `type` `string`<br />音频容器格式，支持 `ogg`、`mp3`、`wav`、`pcm`、`m4a`。
                  * `codec` `string`<br />编码格式；当 `type=pcm` 时通常传 `pcm_s16le`。
                  * `rate` `int`<br />采样率；`pcm` 格式必填，其他格式选填。
                  * `bits` `int`<br />位深；`pcm` 格式必填，其他格式选填。
                  * `channel` `int`<br />通道数；`pcm` 格式必填，其他格式选填。
                </Expandable>
        </Expandable>
  </Expandable>

### 请求示例

```json theme={null}
{
  "audio": {
    "data": "audioData",
    "input": {
      "transcription": {
        "language": "zh",
        "hotwords": ["热词1", "热词2"],
        "model": "stepaudio-3-asr-max",
        "enable_itn": true,
        "enable_timestamp": true
      },
      "format": {
        "type": "pcm",
        "codec": "pcm_s16le",
        "rate": 16000,
        "bits": 16,
        "channel": 1
      }
    }
  }
}
```

<Info>
  兼容性说明：

  * SSE 不再支持 `full_rerun_on_commit`（二遍识别纠错）参数；存量代码中如仍传入该参数，将被服务端忽略，不影响识别结果。如需二遍识别能力，请改用 WebSocket 接入（见 [流式语音识别（双向流式）](/docs/zh/api-reference/audio/asr-stream)）。
</Info>

补充说明：

* 音频数据需使用 Base64 编码。
* 支持的音频格式包括 `ogg`、`mp3`、`wav`、`pcm`、`m4a`。
* 当音频格式为 `pcm` 时，`rate`、`bits`、`channel` 为必填参数；为 `ogg`、`mp3`、`wav`、`m4a` 时为选填。

## 响应

SSE 流式响应，包含以下事件类型。

### Delta 事件（transcript.text.delta）

表示增量转录文本。

```json theme={null}
{
  "type": "transcript.text.delta",
  "meta": {
    "session_id": "sse_1642694400123456789",
    "timestamp": 1642694400123
  },
  "delta": "识别的",
  "item_id": "item_xxx",
  "content_index": 0,
  "start_time": 0,
  "end_time": 500
}
```

* `type` `string`<br />事件类型，固定为 `transcript.text.delta`。
* `meta.session_id` `string`<br />会话 ID。
* `meta.timestamp` `int64`<br />服务端事件 Unix 时间戳，单位毫秒。
* `delta` `string`<br />增量转录文本。
* `item_id` `string`<br />对话项 ID。
* `content_index` `int`<br />内容索引。
* `start_time` `int64`<br />识别文本对应的音频开始时间，单位毫秒。
* `end_time` `int64`<br />识别文本对应的音频结束时间，单位毫秒。

<Note>
  当请求参数 `enable_timestamp=true` 时，Delta 事件返回结果中新增 `item_id`、`content_index`、`start_time`、`end_time` 字段；`meta.timestamp` 是服务端事件 Unix 时间戳，`start_time` / `end_time` 是识别文本在音频中的时间位置，二者单位均为毫秒。
</Note>

### Done 事件（transcript.text.done）

表示完整转录文本已经生成。

```json theme={null}
{
  "type": "transcript.text.done",
  "meta": {
    "session_id": "sse_1642694400123456789",
    "timestamp": 1642694400456
  },
  "text": "识别的完整文字内容",
  "usage": {
    "type": "realtime_asr",
    "input_tokens": 1000,
    "input_token_details": {
      "text_tokens": 0,
      "audio_tokens": 1000
    },
    "output_tokens": 50,
    "total_tokens": 1050
  }
}
```

* `type` `string`<br />事件类型，固定为 `transcript.text.done`。
* `meta.session_id` `string`<br />会话 ID。
* `meta.timestamp` `int64`<br />Unix 时间戳，单位毫秒。
* `text` `string`<br />完整转录文本。
* `usage` `object`<br />使用统计信息。

### 错误事件（error）

表示识别过程出错。

```json theme={null}
{
  "type": "error",
  "meta": {
    "session_id": "sse_1642694400123456789",
    "timestamp": 1642694400789
  },
  "message": "错误描述信息"
}
```

* `type` `string`<br />事件类型，固定为 `error`。
* `meta.session_id` `string`<br />会话 ID。
* `meta.timestamp` `int64`<br />Unix 时间戳，单位毫秒。
* `message` `string`<br />错误描述信息。

完整错误码参见 [错误码](/docs/zh/api-reference/error-codes)。
