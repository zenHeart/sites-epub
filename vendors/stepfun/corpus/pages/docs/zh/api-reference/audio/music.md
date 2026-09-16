> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 音乐生成

文本生成音乐接口采用异步的“提交 + 查询”模式：先创建生成任务并获取 `task_id`，再轮询任务状态，直到任务进入 `SUCCESS` 或 `FAILED` 终态。

<Note>
  音乐生成是自回归长任务，生成一首完整歌曲通常需要数十秒到数分钟。
</Note>

## 服务地址

`POST https://api.stepfun.com/v1/audio/music`

## 能力范围

本次提供三个任务类型，覆盖四种用法：

| 用法          | `task`                                | 输入                | 输出          |
| :---------- | :------------------------------------ | :---------------- | :---------- |
| 歌曲生成        | `text_to_music`                       | 风格描述 + 可选歌词       | 带人声的完整歌曲    |
| 纯器乐生成       | `text_to_music` + `instrumental=true` | 风格描述              | 无人声器乐       |
| 歌曲翻唱 / 风格切换 | `music_cover`                         | 参考歌曲 + 风格描述 + 歌词  | 跟随原曲旋律的翻唱   |
| 干声配乐        | `vocal_to_music`                      | 无伴奏干声 + 风格描述 + 歌词 | 保留输入音色的完整歌曲 |

`text_to_music` 未提供 `lyrics` 时，服务端会自动生成歌词。

## 通用约定

### 请求头

| Header          | 必填 | 说明                                |
| :-------------- | :- | :-------------------------------- |
| `Authorization` | 是  | `Bearer $STEP_API_KEY`            |
| `Content-Type`  | 是  | `application/json; charset=utf-8` |

### 统一错误响应

所有非 2xx 响应采用以下结构：

```json theme={null}
{
  "error": {
    "message": "错误描述",
    "type": "错误类型标识"
  }
}
```

客户端应根据 `error.type` 做程序化判断，不要匹配 `message` 文本。

响应同时返回 `x-should-retry` 头：

* 参数、鉴权和资源类错误（400 / 401 / 404）：`false`
* 速率限制和临时服务故障（429 / 500 / 503）：`true`
* 额度类 429 重试无效，仍需根据 `error.type` 单独处理。

音频输入字段使用原始文件字节的 Base64 字符串，不包含 `data:` 前缀。

## 提交音乐生成任务

`POST https://api.stepfun.com/v1/audio/music/submit`

### 请求参数

* `task` `string` ***required***<br />任务类型，支持 `text_to_music`、`music_cover` 和 `vocal_to_music`。
* `model_id` `string` ***required***<br />音乐模型标识，固定填 `stepaudio-3-music-preview`。
* `caption` `string` ***required***<br />曲风、人声、情绪、调式等风格描述。
* `lyrics` `string` ***optional***<br />歌词，支持歌曲结构标签。`music_cover` 和 `vocal_to_music` 必填；`text_to_music` 不传时由服务端自动写词。
* `instrumental` `boolean` ***optional***<br />是否生成纯器乐，默认 `false`，仅 `text_to_music` 支持。
* `song_audio` `string` ***optional***<br />完整参考歌曲的 Base64 编码，`music_cover` 必填。
* `vocal_audio` `string` ***optional***<br />无伴奏干声的 Base64 编码，`vocal_to_music` 必填。
* `response_format` `string` ***optional***<br />输出格式，支持 `wav`、`flac`、`opus`、`mp3` 和 `pcm`，默认 `wav`。
* `sample_rate` `integer` ***optional***<br />输出采样率，默认 `48000`；省略或传 `0` 时保持模型原生采样率。
* `bit_rate` `integer` ***optional***<br />MP3 / Opus 比特率，单位为 kbps。
* `lyrics_rewrite` `boolean` ***optional***<br />是否改写传入的歌词，默认 `false`。
* `disable_caption_rewrite` `boolean` ***optional***<br />是否跳过 `caption` 自动改写，默认 `false`。
* `max_tokens` `integer` ***optional***<br />生成 token 数上限，默认 `16000`。
* `temperature` `number` ***optional***<br />采样温度，默认 `0.85`，暂不支持 `0`。
* `top_k` `integer` ***optional***<br />采样参数，默认 `80`。
* `top_p` `number` ***optional***<br />采样参数，默认 `0.92`。
* `repetition_penalty` `number` ***optional***<br />重复惩罚，默认 `1.08`。

### 参数适用矩阵

| 参数             | `text_to_music` 歌曲 | `text_to_music` 器乐 | `music_cover` | `vocal_to_music` |
| :------------- | :----------------- | :----------------- | :------------ | :--------------- |
| `caption`      | 必填                 | 必填                 | 必填            | 必填               |
| `lyrics`       | 可选，留空自动写词          | 禁止传                | 必填            | 必填               |
| `instrumental` | 省略或 `false`        | 必须为 `true`         | 不支持           | 不支持              |
| `song_audio`   | 不使用                | 不使用                | 必填            | 不使用              |
| `vocal_audio`  | 不使用                | 不使用                | 不使用           | 必填               |

### 参数说明

#### 器乐与歌词

`instrumental=true` 时不得同时传入 `lyrics`。歌词中的 `[Instrumental]` 仅表示局部器乐段，不能代替顶层的 `instrumental=true`。

#### 翻唱

`music_cover` 的旋律跟随参考歌曲，`caption` 控制风格、音色、编曲和情绪。建议传入与原曲演唱内容一致的歌词。

#### 干声配乐

`vocal_to_music` 的旋律主要跟随干声，并保留输入干声的人声音色。干声实际演唱内容需要是 `lyrics` 的子集或全集。

#### Caption 改写

服务端默认将 `caption` 改写为规范的英文 style prompt，并通过查询接口的 `rewritten_caption` 返回。

`disable_caption_rewrite=true` 不能与 `lyrics_rewrite=true` 同时使用；在非器乐 `text_to_music` 场景使用时，必须显式提供歌词。

#### 输出时长

输出时长由模型决定，无法通过参数精确控制。同一输入多次生成的时长可能不同，通常为 1～3 分钟。

### 歌词结构标签

歌词结构标签需要独占一行。

常用标签：

* `[Intro]`
* `[Verse 1]`
* `[Pre-Chorus]`
* `[Chorus 1]`
* `[Bridge]`
* `[Instrumental]`
* `[Hook]`
* `[Break]`
* `[Drop]`
* `[Ad-lib]`
* `[Outro]`

```text theme={null}
[Verse 1]
青椒还沾着晨露
你挑的番茄滚到脚边

[Instrumental]

[Chorus 1]
初秋的菜场挤着人潮
你背影越走越渺小
```

### Caption 写法建议

`caption` 支持中文或英文，建议描述以下维度：

| 维度   | 示例                            |
| :--- | :---------------------------- |
| 曲风   | lo-fi、R\&B、city pop、dance-pop |
| 人声   | 女声、男声、温暖、气声、颤音                |
| 律动   | 缓慢、中速、轻快、适合跳舞                 |
| 音色质感 | 温暖、开阔、颗粒感、朦胧                  |
| 情绪   | 怀旧、惆怅、振奋、有希望                  |
| 调式   | B 小调、D 小调、C 大调                |

### 响应

```json theme={null}
{
  "task_id": "01959f5e-0f31-7a2b-9c4d-1234567890ab"
}
```

`task_id` 用于查询任务结果和问题排查。

### 错误码

| HTTP | `error.type`                                                             | 触发条件                      |
| :--- | :----------------------------------------------------------------------- | :------------------------ |
| 400  | `request_params_invalid`                                                 | JSON 非法、缺少必填字段、参数值或参数组合错误 |
| 401  | `not_allowed`                                                            | 鉴权令牌缺失或无效                 |
| 402  | `insufficient_credit`                                                    | Credit 余额不足               |
| 404  | `model_invalid`                                                          | 模型 ID 错误或账号没有模型权限         |
| 429  | `rate_limited`                                                           | 请求速率或并发超过限制               |
| 429  | `project_credit_limit_exceeded` / `member_project_credit_limit_exceeded` | 项目或成员达到 Credit 上限         |
| 503  | `service_unavailable`                                                    | 服务负载过高或任务入队失败             |

内容审核可能在提交阶段同步返回 451，也可能在任务执行阶段以 `FAILED` + `error.stage=censor` 返回。

### 调用示例

<Tabs>
  <Tab title="歌曲生成">
    ```bash theme={null}
    curl -X POST "https://api.stepfun.com/v1/audio/music/submit" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "task": "text_to_music",
        "model_id": "stepaudio-3-music-preview",
        "caption": "A soul and R&B song, female vocal, D minor, warm and nocturnal",
        "lyrics": "[Verse 1]\n...\n[Chorus 1]\n...",
        "response_format": "mp3"
      }'
    ```
  </Tab>

  <Tab title="纯器乐">
    ```bash theme={null}
    curl -X POST "https://api.stepfun.com/v1/audio/music/submit" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "task": "text_to_music",
        "model_id": "stepaudio-3-music-preview",
        "instrumental": true,
        "caption": "流行风格古筝曲，穿插长笛和萧声，温暖辽阔",
        "response_format": "mp3"
      }'
    ```
  </Tab>

  <Tab title="歌曲翻唱">
    ```bash theme={null}
    curl -X POST "https://api.stepfun.com/v1/audio/music/submit" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "task": "music_cover",
        "model_id": "stepaudio-3-music-preview",
        "caption": "Soul and R&B with funk influences, warm and breathy vocal",
        "lyrics": "[Verse 1]\n...",
        "song_audio": "<base64 of reference song>",
        "response_format": "mp3"
      }'
    ```
  </Tab>

  <Tab title="干声配乐">
    ```bash theme={null}
    curl -X POST "https://api.stepfun.com/v1/audio/music/submit" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "task": "vocal_to_music",
        "model_id": "stepaudio-3-music-preview",
        "caption": "Vibrant dance-pop with uplifting R&B influences",
        "lyrics": "[Verse 1]\n...",
        "vocal_audio": "<base64 of dry vocal>",
        "response_format": "mp3"
      }'
    ```
  </Tab>
</Tabs>

## 查询任务结果

`POST https://api.stepfun.com/v1/audio/music/query`

建议每 5 秒轮询一次，直到 `status` 进入终态；成功后请及时保存音频。

### 请求参数

```json theme={null}
{
  "task_id": "01959f5e-0f31-7a2b-9c4d-1234567890ab"
}
```

| 参数        | 类型     | 必填 | 说明           |
| :-------- | :----- | :- | :----------- |
| `task_id` | string | 是  | 提交接口返回的任务 ID |

### 任务状态

| 状态        | 说明          |
| :-------- | :---------- |
| `PENDING` | 任务已入队       |
| `RUNNING` | 任务正在处理      |
| `SUCCESS` | 生成完成，可以获取音频 |
| `FAILED`  | 生成失败，不会回退   |

### 进行中响应

```json theme={null}
{
  "status": "RUNNING",
  "task": "text_to_music",
  "caption": "A soul and R&B song, female vocal, D minor",
  "lyrics": "[Verse 1]\n...",
  "response_format": "mp3",
  "sample_rate": 48000
}
```

### 成功响应

```json theme={null}
{
  "status": "SUCCESS",
  "task": "text_to_music",
  "caption": "A soul and R&B song, female vocal, D minor",
  "lyrics": "[Verse 1]\n...",
  "response_format": "mp3",
  "sample_rate": 48000,
  "audio": "<base64-encoded generated audio>",
  "rewritten_caption": "A soul and R&B song, female vocal, D minor, warm and nocturnal",
  "rewritten_lyrics": "[Verse 1]\n...\n[Chorus 1]\n..."
}
```

### 失败响应

```json theme={null}
{
  "status": "FAILED",
  "task": "music_cover",
  "caption": "...",
  "lyrics": "...",
  "response_format": "mp3",
  "error": {
    "stage": "audio_transcode",
    "message": "unsupported audio format"
  }
}
```

`FAILED` 是业务终态，HTTP 状态码仍为 200。

### 响应字段

| 字段                  | 类型             | 说明                                     |
| :------------------ | :------------- | :------------------------------------- |
| `status`            | string         | `PENDING`、`RUNNING`、`SUCCESS`、`FAILED` |
| `task`              | string         | 提交时的任务类型                               |
| `caption`           | string         | 提交时的风格描述                               |
| `lyrics`            | string         | 提交或生成的歌词                               |
| `response_format`   | string         | 输出格式                                   |
| `sample_rate`       | integer        | 输出采样率                                  |
| `audio`             | string（Base64） | 生成音频，仅 `SUCCESS` 返回                    |
| `rewritten_caption` | string         | 服务端改写后的风格描述，仅 `SUCCESS` 返回             |
| `rewritten_lyrics`  | string         | 服务端生成或改写后的歌词，仅 `SUCCESS` 返回            |
| `error`             | object         | 失败原因，仅 `FAILED` 返回                     |

### 失败阶段

| `error.stage`        | 含义              | 建议处理              |
| :------------------- | :-------------- | :---------------- |
| `audio_transcode`    | 音频无法解码、转码或采样率非法 | 检查音频格式、文件和参数      |
| `no_speech_detected` | 干声中未检测到有效人声     | 更换清晰且空白较少的干声      |
| `censor`             | 文本或音频被安全审核拦截    | 调整内容后重新提交         |
| `internal`           | 服务端内部错误         | 稍后重试并保留 `task_id` |

### 查询错误码

| HTTP | `error.type`             | 触发条件               |
| :--- | :----------------------- | :----------------- |
| 400  | `request_params_invalid` | 请求体非法或缺少 `task_id` |
| 401  | `not_allowed`            | 鉴权 Header 缺失或无效    |
| 404  | `task_not_found`         | 任务不存在或已超过保留期       |
| 429  | `rate_limited`           | 查询过于频繁             |
| 503  | `service_unavailable`    | 服务负载过高或结果读取失败      |

### 查询示例

```bash theme={null}
curl -X POST "https://api.stepfun.com/v1/audio/music/query" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $STEP_API_KEY" \
  -d '{
    "task_id": "01959f5e-0f31-7a2b-9c4d-1234567890ab"
  }'
```

## 音频与输出约束

| 项目    | 约束                              |
| :---- | :------------------------------ |
| 输入编码  | 音频原始字节的 Base64，不含 `data:` 前缀    |
| 输入容器  | `wav`、`flac`、`opus`、`mp3`       |
| 输出格式  | `wav`、`flac`、`opus`、`mp3`、`pcm` |
| 输出采样率 | 原生 48 kHz 立体声，支持服务端重采样          |

推荐使用 MP3 输出以降低响应体积。PCM 为无文件头裸流，需按 48 kHz、16 bit、立体声自行解析。

## 合规说明

生成内容对外分发、发布或用于商业用途时，调用方应根据适用法律法规添加人工智能生成内容标识。
