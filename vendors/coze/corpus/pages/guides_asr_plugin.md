> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程官方提供两款语音识别插件：[语音识别插件](https://www.coze.cn/store/plugin/7506776373675966516?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)和[大模型语音识别插件](https://www.coze.cn/store/plugin/7506777203359629350?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)，支持识别音频并转换为文字，适用于播客内容总结、会议记录整理、采访内容加工等场景。本文介绍语音识别插件的使用方法。
## 插件说明 {#88705f52}
语音识别插件基于火山引擎[大模型录音文件识别 API](https://www.volcengine.com/docs/6561/1354868) 和[录音文件识别极速版 API](https://www.volcengine.com/docs/6561/192519) 开发，内置自动标点、语义顺滑、数字规整、智能分句等功能，支持准确地将音频转换为文字，详细功能说明请参见[大模型语音识别简介](https://www.volcengine.com/docs/6561/1354871)和[语音识别简介](https://www.volcengine.com/docs/6561/109880)。
大模型语音识别插件和语音识别插件的区别如下表所示。
<!-- @cols-width: 100,388,349 -->
| | | | \
|**维度** |**大模型语音识别插件** |**语音识别插件** |
|---|---|---|
| | | | \
|**核心定位** |支持更多使用场景，且准确率更高。 |通用的语音转文字服务。 |
| | | | \
|**核心优势** |* 较强抗噪、抗干扰能力。 |\
| |* 复杂口语化表达识别更准确，例如吞音、重复、语气词等。 |\
| |* 专业领域术语识别显著提升，例如音乐、科技、教育、医疗等垂直领域。 |\
| |* 上下文理解能力更强，给出更贴合语境的识别效果。 |* 支持更多小语种。 |\
| | |* 成本更低，支持超额累进的阶梯价，用量越大、单价越低。 |\
| | | |\
| | | |
| | | | \
|**语种方言覆盖** |中英文、上海话、闽南语，四川、陕西、粤语。 |普通话、粤语、四川话、上海话、英文、日语、韩语、法语、西班牙语、葡萄牙语、印尼语。 |
| | | | \
|**使用场景** |支持**音视频字幕**、**歌词识别**、**游戏语音输入**、内容审核质检、会议访谈转写、课堂内容分析等场景。 |支持会议访谈内容转写、内容审核质检、课堂内容分析等场景。 |

## 使用限制 {#8fbe4734}

* 扣子主账号内的所有子账号共享语音识别的并发限制，最大并发数为 10。
* 音频文件需满足如下要求：
   * 大模型语音识别的文件格式：opus、ogg、mp3、wav、m4a、mp4、pcm、raw、spx、aac、amr
   * 小模型语音识别的文件格式：ogg、mp3、wav、mp4、m4a
   * 音频时长：小于 30 分钟。
   * 文件大小：小于 10 MB。

## 计费说明 {#73bd1c83}
使用语音识别插件时，将根据语音文件时长计算**语音识别**费用，对应的价格请参考[音视频费用](/coze_pro/asr_tts_fee)。涉及的计费项如下： 

* 使用[大模型语音识别](https://www.coze.cn/store/plugin/7506777203359629350?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)插件时，将根据语音文件时长收取**大模型录音文件识别时长**费用。 
* 使用[语音识别](https://www.coze.cn/store/plugin/7506776373675966516?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)插件时，将根据语音文件时长收取**录音文件识别（极速版）​**费用。

## 大模型语音识别插件 {#90aab9fc}
[大模型语音识别](https://www.coze.cn/store/plugin/7506777203359629350?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)插件具备上下文理解能力，能够更准确识别语音内容，更好地支持中英混说等场景。
### 输入参数 {#a6c0fbe1}
输入参数说明如下表所示。
<!-- @cols-width: 172,105,500 -->
| | | | \
| **参数名称**  | **是否必填**  | **说明**  |
|---|---|---|
| | | | \
|audio_url |必选 |待转换为文本的音频。你可以引用开始节点的输入、上游节点的输出、用户变量、应用变量、系统变量，实现音频文件的动态输入。 |

### 输出参数 {#39779b54}
输出参数说明如下表所示。
<!-- @cols-width: 172,609 -->
| | | \
| **参数** | **说明**  |
|---|---|
| | | \
| code  | 返回状态码，`0` 表示成功，非 `0` 表示失败。  |
| | | \
| data.text  | 通过语音识别功能生成的文字内容。 |
| | | \
| log_id  | 日志 ID，用于问题排查和调试。  |
| | | \
| msg  | 执行插件时的状态描述或错误提示信息。  |

## 语音识别插件 {#f776456f}
[语音识别](https://www.coze.cn/store/plugin/7506776373675966516?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)插件支持方言和小语种，你可以根据实际语音内容选择合适的语种以优化语音识别效果。
### 输入参数 {#6b9bd9ff}
输入参数说明如下表所示。
<!-- @cols-width: 172,105,500 -->
| | | | \
| **参数名称**  | **是否必填**  | **说明**  |
|---|---|---|
| | | | \
|audio_url |必选 |待转换为文本的音频。你可以引用开始节点的输入、上游节点的输出、用户变量、应用变量、系统变量，实现音频文件的动态输入。 |
| | | | \
|language |必选 |填写语种的值，包括普通话、粤语、四川话、上海话、英文、日语、韩语、法语、西班牙语、葡萄牙语、印尼语。 |

### 输出参数 {#715ef463}
输出参数说明如下表所示。
<!-- @cols-width: 172,609 -->
| | | \
| **参数** | **说明**  |
|---|---|
| | | \
| code  | 返回状态码，`0` 表示成功，非 `0` 表示失败。  |
| | | \
| data.text  | 通过语音识别功能生成的文字内容。 |
| | | \
| log_id  | 日志 ID，用于问题排查和调试。  |
| | | \
| msg  | 执行插件时的状态描述或错误提示信息。  |

## 示例 {#36207197}
在工作流中添加大模型语音识别插件中的 `asr_llm` 工具。通过上传语音文件或填写语音文件 URL 输入待转换为文本的音频，语音识别插件输出转换后的文本。
![Image=700x265](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f7b6ea3183cd49f78d86cab9ff4f6803~tplv-goo7wpa0wc-image.image)
<!-- @cols-width: 141,422,298 -->
| | | | \
|**节点** |**说明** |**示例** |
|---|---|---|
| | | | \
|开始节点 |输入参数使用默认的 `input` 参数，用于输入待转换的语音文件 URL。 |![Image=200x105](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4e1089a3f9dd4ada92b51f3be7a68cd7~tplv-goo7wpa0wc-image.image) |
| | | | \
|大模型语音识别插件 |添加大模型语音识别插件中的 `asr_llm` 工具，输入参数 `audio_url` 的值引用开始节点的` input` 变量，用于获取待转换为文本的音频。 |\
| | |![Image=200x269](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/aa8ca8107c1e428bba1b21b2257273ca~tplv-goo7wpa0wc-image.image) |
| | | | \
|结束节点 |结束节点输出变量的值引用语音识别插件输出的 `data.text` 参数。 |![Image=200x133](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/de23f3b1fa1449a7a8c333b90455b678~tplv-goo7wpa0wc-image.image) |



> * 语音识别插件 ID：7506818401994735616
