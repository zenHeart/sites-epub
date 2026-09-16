> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 音频生成

基于文本描述统一生成人声、音效、环境音和背景音乐等多种声音要素。

## 服务地址

`POST https://api.stepfun.com/v1/audio/generate`

## 请求头

* `Content-Type` `string` ***required***<br />固定为 `application/json`。
* `Authorization` `string` ***required***<br />认证令牌，格式为 `Bearer $STEP_API_KEY`。

## 请求参数

* `model` `string` ***required***<br />模型名称，当前支持 `stepaudio-3-gen-preview`。

* `task` `string` ***required***<br />任务类型，当前仅支持 `text_to_audio`：通过自然语言描述设计音色，生成人声、音效、背景音乐等多种声音要素。使用该任务时，`scripts` 或 `instruction` 至少必填其一，`roles` 选填。

* `roles` `array` ***optional***<br />生成时使用的角色与音色描述，所有 `name` 和 `description` 合计最多 500 个字符。

  <Expandable>
    * `name` `string` ***optional***<br />自定义角色或音色名称，例如“主唱”。
    * `description` `string` ***optional***<br />自定义角色或音色描述，例如“二十多岁的青年男性，嗓音略带沙哑，演唱时气息饱满”。`name` 与 `description` 需要同时填写或同时留空。
  </Expandable>

* `scripts` `array` ***optional***<br />要生成的台词、音效或背景音乐描述，合计最多 1000 个字符。台词通过 `speaker` 指定说话人，并可用 `()` 描述说话的语气、风格、情绪等；音效和背景音乐描述用 `[]` 包裹，可不传 `speaker`。

  <Expandable>
    * `speaker` `string` ***optional***<br />台词对应的 `roles.name`。纯音效或 BGM 描述可以不传。
    * `text` `string` ***required***<br />台词、音效或 BGM 描述。
  </Expandable>

* `instruction` `string` ***optional***<br />全局自然语言指导，用于设定环境、BGM 和情绪基调，最多 500 个字符。

* `response_format` `string` ***optional***<br />返回音频格式，支持 `wav`、`mp3`、`flac`、`opus` 和 `pcm`。

* `speed` `number` ***optional***<br />语速，范围为 0.5～2。

* `volume` `number` ***optional***<br />音量，范围为 0.1～2.0。

* `sample_rate` `integer` ***optional***<br />采样率，支持 8000、16000、22050、24000 和 48000。

* `pronunciation_map` `object` ***optional***<br />发音替换规则。

* `text_normalization` `string` ***optional***<br />文本归一化策略，支持 `standard` 和 `enhanced`。

* `stream_format` `string` ***optional***<br />返回模式，默认为 `audio`：`audio` 直接返回生成的音频，`sse` 通过 Server-Sent Events 持续返回 Base64 编码的音频分片。

* `return_url` `boolean` ***optional***<br />是否返回音频 URL。

<Note>
  使用官方音色或复刻音色合成的参考音色任务（`reference_to_audio`）暂未开放，后续支持后会在本页补充。
</Note>

## 请求示例

### 音频生成

```bash theme={null}
curl --location 'https://api.stepfun.com/v1/audio/generate' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer '"$STEP_API_KEY" \
  --data '{
    "model": "stepaudio-3-gen-preview",
    "task": "text_to_audio",
    "roles": [
      { "name": "地勤", "description": "三十岁上下的男性，声音干练利落，语速快，带着停机坪作业的专注，需盖过引擎噪音而略提高音量" },
      { "name": "机长", "description": "中年男性，声音通过无线电传来，带航空通讯特有的电子压缩与背景电流，沉稳职业" },
      { "name": "塔台", "description": "女性，声音同样经无线电传输，字正腔圆略带失真，冷静下达指令" }
    ],
    "scripts": [
      { "text": "[客机APU持续的高频呜鸣，混着牵引车低沉的引擎声]" },
      { "speaker": "地勤", "text": "（对着头戴通话器，略提高音量盖过噪音）左发进气口检查完毕，轮挡已撤，可以推出。" },
      { "speaker": "机长", "text": "（无线电话音，压缩失真）收到，请求后推许可，目视地面信号。" },
      { "text": "[无线电“嗤”的一声接通，传来带电流的话音]" },
      { "speaker": "塔台", "text": "（无线电话音，冷静）同意后推，跑道两三右，地面风零九零三节，祝一路顺风。" },
      { "speaker": "地勤", "text": "（挥动荧光棒指引，大声回应）明白，牵引车开始后推，注意左侧翼尖间距！" }
    ],
    "instruction": "夜间机场停机坪，一架客机正在做起飞前的最后地面检查",
    "response_format": "mp3"
  }'
```

## 限制与兼容性

* `instruction` 和 `roles` 字段最多 500 字符，`scripts` 字段最多 1000 字符。
* `stepaudio-3-gen-preview` 不支持 `voice`、`voice_label`、`timestamp` 参数。
* 超出长度限制或传入不支持的参数时，接口返回 HTTP 400。
