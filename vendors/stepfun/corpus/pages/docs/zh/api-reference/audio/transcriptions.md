> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 音频转写

将上传的音频文件识别为文本，一次性返回完整结果，适合简单的整段转写场景。推荐使用模型 `stepaudio-2.5-asr`。

<Info>
  如需分句与字 / 词级时间戳、双声道分轨、说话人识别等进阶能力，请使用 [音频文件识别](/docs/zh/api-reference/audio/asr)。
</Info>

## 请求地址

`POST https://api.stepfun.com/v1/audio/transcriptions`

请求体为 `multipart/form-data`。

## 请求参数

* `model` `string` ***required***<br />模型名称，支持 `stepaudio-2.5-asr`、`step-asr`（旧模型名称）。
* `response_format` `string` ***required***<br />输出格式，支持 `json`、`text`。
* `file` `File` ***required***<br />待识别的音频文件，支持 `mp3`、`pcm`、`ogg`、`wav`，文件需小于 100MB。
* `hotwords` `string` ***optional***<br />热词列表，为可解析的 JSON 数组字符串，如 `["热词1", "热词2"]`。

## 返回

接口根据 `response_format` 返回对应格式的识别结果。

<Tabs>
  <Tab title="json">
    * `text` `string`<br />识别所得的完整文本。

    ```json theme={null}
    { "text": "测试录制音频" }
    ```
  </Tab>

  <Tab title="text">
    ```text theme={null}
    测试录制音频
    ```
  </Tab>
</Tabs>

## 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -L 'https://api.stepfun.com/v1/audio/transcriptions' \
      -H "Authorization: Bearer $STEPFUN_API_KEY" \
      -F 'model="stepaudio-2.5-asr"' \
      -F 'response_format="json"' \
      -F 'file=@"sample.mp3"'
    ```
  </Tab>
</Tabs>
