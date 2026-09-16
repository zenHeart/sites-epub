> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

[视频剪辑工具插件](https://www.coze.cn/store/plugin/7514607196831940643?from=add_plugin_menu&surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)主要用于视频剪辑操作，包括为视频添加字幕、音视频合成、视频拼接、音频和图片合成视频、视频插帧处理、视频超分辨率处理等功能。
:::tip 说明
视频剪辑工具插件 QPS 限额为 1，即包括子用户在内的每个用户 1 秒内最多只能调用 1 次。
:::
## 计费说明 {#b6202753}
视频剪辑工具插件的计费方式为**基准计费项✖️抵扣系数✖️时长（分钟）**，具体的计费项、单价及免费额度，请参考[插件费用](/coze_pro/plugin_fee)。
不同工具输出不同分辨率的视频或音频时，对应的抵扣系数不同，抵扣系数列表如下。
例如调用 image_to_video 工具生成一个 90 秒视频，视频分辨率固定为 1080 P，则该工具对应的计费抵扣系数为 6，消耗的积分为 **`10 积分/分钟 ✖️ 6（系数） ✖️ 1.5 分钟    = 90 积分`。**
<!-- @cols-width: 322,396 -->
| | | \
|**工具** |**抵扣系数** |
|---|---|
| | | \
|[add_subtitles 工具](/guides/video_Editing_plugin#217cd7ca) |该类工具中，不同视频输出规格对应的抵扣系数如下： |\
| | |\
| |* 4K（3840x2160）分辨率及以下：24 |\
| |* 2K（2560x1440）分辨率及以下：12 |\
| |* 1080P（1920x1080)分辨率及以下：6 |\
| |* 720P（1280x720）分辨率及以下：3 |\
| |* 540P （720x540）分辨率及以下：2 |\
| |* 480P （640x480）分辨率及以下：1.5 |\
| |* 360P（480x360）分辨率及以下：1 |\
| |* 音频：1 |
| |^^| \
|[compile_video_audio 工具](/guides/video_Editing_plugin#489696fe) | |
| |^^| \
|[audio_extract 工具](/guides/video_Editing_plugin#7b3f070a) | |
| |^^| \
|[video_trim 工具](/guides/video_Editing_plugin#ef134354) | |
| |^^| \
|[concat_videos 工具](/guides/video_Editing_plugin#3d8c73ef) | |
| |^^| \
|[compile_image_audio 工具](/guides/video_Editing_plugin#74133b43) | |
| |^^| \
|[add_subvideo 工具](/guides/video_Editing_plugin#5ebf0a38) | |
| |^^| \
|[add_text 工具](/guides/video_Editing_plugin#44b6a676) | |
| |^^| \
|[image_to_video 工具](/guides/video_Editing_plugin#7f84a015) | |
| |^^| \
|[audio_mix 工具](/guides/video_Editing_plugin#ef9ed5b3) | |
| |^^| \
|[video_speed 工具](/guides/video_Editing_plugin#b6e21434) | |
| |^^| \
|[ajust_audio_volume 工具](/guides/video_Editing_plugin#57d54cf6) | |
| |^^| \
|[ajust_video_resolution 工具](/guides/video_Editing_plugin#792d8474) | |
| |^^| \
|[video_fps 工具](/guides/video_Editing_plugin#7fcfe094) | |
| |^^| \
|[video_flip 工具](/guides/video_Editing_plugin#cb1aa420) | |
| |^^| \
|[audio_loudness_normalization 工具](/guides/video_Editing_plugin#506411f9) | |
| | | \
|[insert_frame 工具](/guides/video_Editing_plugin#77bde67c) |该类工具中，不同视频输出规格对应的抵扣系数如下： |\
| | |\
| |* 4K（3840x2160）分辨率及以下：600 |\
| |* 2K（2560x1440）分辨率及以下：300 |\
| |* 1080P（1920x1080)分辨率及以下：150 |\
| |* 720P（1280x720）分辨率及以下：75 |
| |^^| \
|[video_super_resolution 工具](/guides/video_Editing_plugin#9be4feb1) | |
| |^^| \
|[video_hdr 工具](/guides/video_Editing_plugin#7dd34d4c) | |
| |^^| \
|[audio_denoise 工具](/guides/video_Editing_plugin#f77d3447) | |
| | | \
|[audio_to_subtitle 工具](/guides/video_Editing_plugin#1ccc340a) |5 |
| | | \
|[audio_separate 工具](/guides/video_Editing_plugin#41a7cd80) |7 |

## add_subtitles 工具 {#217cd7ca}
add_subtitles 工具会基于视频 URL、字幕文件 URL/自定义文本、字幕样式，为视频添加字幕。配置 add_subtitles 工具时，你可以使用 `subtitle_url` 参数传入字幕文件 URL 为视频添加字幕，也可以使用`text_list` 参数传入自定义文本及对应定位信息，在指定位置精准添加字幕。你还可以配置 `subtitle_config` 参数，用于指定字幕样式配置，包括字体大小、字体 ID、字体颜色及字幕显示位置和尺寸等。
### 演示效果 {#d527b724}
![Image=503x282](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bde464ac330c47b29ac7e62204deb84e~tplv-goo7wpa0wc-image.image)
### 输入参数 {#f279f5eb}
输入参数说明如下表所示：
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|subtitle_config |设置字幕的样式，Object 类型，包含如下字段： |\
| | |\
| |* `font_size`：字幕的字体大小，Integer 类型，单位：像素。 |\
| |* `font_type`：字幕的字体 ID，String 类型，详情请参考[字体 ID](https://www.volcengine.com/docs/4/102412#%E5%AD%97%E4%BD%93-id)。 |\
| |* `font_color`：字幕的字体颜色，String 类型，RGBA 格式，例如 #FFFFFFFF。 |\
| |* `background_border_width`：字幕背景的边框大小，Number 类型，单位：像素。 |\
| |* `background_color`：字幕背景的边框颜色，String 类型，RGBA 格式，例如 #FFFFFFFF。 |\
| |* `border_color`：字幕内容描边的颜色，String 类型，RGBA 格式，例如 #FFFFFFFF。`border_width`：字幕内容描边的宽度，Integer 类型，单位：像素。 |\
| |* `font_pos_config.width`：字幕的宽度，支持设置为百分比（相对于视频宽度）或具体像素值，String 类型，例如 100% 或 1000。 |\
| |* `font_pos_config.height`：字幕的高度，支持设置为百分比（相对于视频高度）或具体像素值，String 类型，例如 10% 或 100。 |\
| |* `font_pos_config.pos_x`：字幕在水平方向（X 轴）的位置，以视频正上方居中位置为原点，单位：像素，String 类型。例如值为 0 时，表示字幕在水平位置居中；值为 - 100 时，表示字幕向左移动 100 像素；值为 100 时，表示字幕向右移动 100 像素。 |\
| |* `font_pos_config.pos_y`：水印在垂直方向（Y 轴）的位置，以视频正上方居中位置为原点，单位：像素，String 类型。例如值为 0 时，表示字幕在视频顶部；值为 100 时，表示字幕向下移动 100 像素。 |\
| | |\
| |配置示例如下： |\
| |```JSON |\
| |{ |\
| |    "font_size": 20, |\
| |    "font_type": "1525745", |\
| |    "font_color": "#FFFFFFFF", |\
| |    "background_color":"#646464FF", |\
| |    "background_border_width":2, |\
| |    "border_color":"#646464FF", |\
| |    "border_width":2, |\
| |    "font_pos_config": { |\
| |      "width": "100%", |\
| |      "height": "100", |\
| |      "pos_x": "0", |\
| |      "pos_y": "0" |\
| |    } |\
| |  } |\
| |``` |\
| | |
| | | \
|video |需添加字幕的视频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* **固定值**：直接输入视频 URL。 |\
| |* **变量**：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |
| | | \
|subtitle_url |字幕文件 URL。常见的字幕文件为 SRT、VTT、ASS 等格式。支持如下两种配置方式： |\
| | |\
| |* **固定值**：直接输入字幕文件 URL。 |\
| |* **变量**：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现字幕文件的动态输入。 |\
| | |\
| |`text_list`、`subtitle_url` 参数二选一配置即可。 |
| | | \
|text_list |自定义添加字幕文本，Array 类型。包含如下字段： |\
| | |\
| |* `start_time`：该段字幕的开始时间。 |\
| |* `end_time`：该段字幕的结束时间。 |\
| |* `text`：字幕内容。 |\
| | |\
| |配置示例如下： |\
| |```Plain Text |\
| |[ |\
| |    { |\
| |        "text": "今天是星期一", |\
| |        "start_time": 4.309, |\
| |        "end_time": 5.912 |\
| |    }, |\
| |    { |\
| |        "text": "今天是星期二", |\
| |        "start_time": 5.962, |\
| |        "end_time": 7.638 |\
| |    }, |\
| |    { |\
| |        "text": "今天是星期三", |\
| |        "start_time": 7.688, |\
| |        "end_time": 9.059 |\
| |    } |\
| |] |\
| |``` |\
| | |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#f3e125a5}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |添加字幕后的视频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率信息。 |\
| |* type：输出结果的类型，固定为 video。 |\
| |* duration：视频的时长。 |

## audio_to_subtitle 工具 {#1ccc340a}
audio_to_subtitle 工具用于将音频转换为字幕文件。配置 audio_to_subtitle 工具时，你需要配置 `source`，用于输入视频或音频 URL，配置 `subtitle_type`  参数，用于指定输出的字幕文件的格式。
### 输入参数 {#a429a72a}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|source |视频或音频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频或音频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |\
| | |\
| |音频要求： |\
| | |\
| |* 支持处理 MP3、WAV、FLAC 等常见格式的音频。 |
| | | \
|subtitle_type |生成的字幕文件类型，可选值为 webvtt、srt。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#2ca587fb}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |字幕文件 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|message |执行插件时的状态描述或错误提示信息。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |

## compile_video_audio 工具 {#489696fe}
compile_video_audio 工具用于合成音视频，通过指定待合成的音频和视频 URL，即可轻松合成音视频。此外，该工具还提供额外的灵活配置选项，包括是否保留原视频的音频轨道，以及配置音频、视频同步功能，通过设置同步方法（加速或裁剪）和同步模式（以视频或音频时长为准）来对齐音频和视频时长，从而生成同步的视听内容。
### 演示效果 {#8ed20577}
为原本无声的视频配上背景音乐，效果如下：
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/14e77496dec044bdae30dcab114caccb~tplv-goo7wpa0wc-image.image"></Player>
### 输入参数 {#6aba5cb3}
输入参数说明如下表所示：
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|audio |待合成的音频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* **固定值**：直接输入音频 URL。 |\
| |* **变量**：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |音频要求： |\
| | |\
| |* 支持处理 MP3、WAV、FLAC 等常见格式的音频。 |
| | | \
|video |待合成的视频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* **固定值**：直接输入视频 URL。 |\
| |* **变量**：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |
| | | \
|is_audio_reserve |是否保留原视频流中的音频。 |\
| | |\
| |* true：保留。 |\
| |* false：不保留。 |
| | | \
|is_video_audio_sync |是否对齐音频和视频时长。 |\
| | |\
| |* true：通过 `output_sync` 配置，对齐音频和视频时长。 |\
| |* false（默认值）：保持原样输出，不做音视频对齐。最终合成的视频时长，以较长的流为准。 |
| | | \
|output_sync |设置 `is_video_audio_sync` 为 `true` 时，须设置对齐模式，包括对齐基准和对齐方式， Object 类型，包含如下字段： |\
| | |\
| |* `sync_mode`：当音频和视频时长不相等时，可指定对齐基准，可选项：video、audio。 |\
| |   * video：以视频的时长为准。 |\
| |   * audio：以音频的时长为准。 |\
| |* `sync_method`：指定对齐方式，支持通过裁剪或加速的方式，对齐音频和视频的时长。可选项：speed、trim。 |\
| |   * speed：通过加快音频或视频的速度，对齐音频和视频的时长。 |\
| |   * trim：通过裁剪音频或视频，对齐音频和视频的时长。从头开始计算并裁剪。 |\
| | |\
| |示例如下： |\
| |添加如下配置，指定以视频时长为准，当音频时长超过视频时长时，裁剪音频多余部分，如果音频时长短于视频时长时，不足部分则无音频。 |\
| |```JSON |\
| |{ |\
| |  "sync_mode":"video",  |\
| |  "sync_method":"trim" |\
| |} |\
| |``` |\
| | |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#de46ab4f}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |合成后的视频 URL。有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定。请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率信息。 |\
| |* type：输出结果的类型，固定为 video。 |\
| |* duration：视频的时长。 |

## audio_separate 工具 {#41a7cd80}
audio_separate 工具用于分离并输出音频或视频中的人声和背景音乐。在配置 audio_separate 工具时，你需要配置 `source` 参数，用于输入音频或视频 URL。
### 输入参数 {#3e9fd7e6}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|source |视频或音频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频或音频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |\
| | |\
| |音频要求： |\
| | |\
| |* 支持处理 MP3、WAV、FLAC 等常见格式的音频。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#d0459c46}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|background |背景音乐 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定。请及时转存。 |
| | | \
|voice |人声音频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定。请及时转存。 |
| | | \
|duration |视频时长，单位：秒。 |
| | | \
|message |执行插件时的状态描述或错误提示信息。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |

## audio_extract 工具 {#7b3f070a}
audio_extract 工具用于抽取视频中的音频，并支持将其保存为指定格式的音频文件。在配置 audio_extract 工具时，你需要配置 `video` 参数，用于输入视频 URL，配置 `format` 参数，用于指定输出音频的格式。
### 输入参数 {#38bd959e}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|video |视频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |
| | | \
|format |输出音频的格式，支持 mp3、m4a 格式。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#8af917fc}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出音频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定。请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出音频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：固定为 unknown。 |\
| |* type：输出结果的类型，固定为 audio。 |\
| |* duration：音频的时长，单位：秒。 |

## video_trim 工具 {#ef134354}
video_trim 工具用于裁剪视频时长，保留从指定的裁剪开始时间到结束时间范围内的视频。在配置 video_trim 工具时，你需要配置 `video` 参数，用于输入视频 URL，配置 `start_time`、`end_time` 参数，用于指定视频裁剪的开始时间和结束时间。
### 演示效果 {#3da79d73}

::::cols
@col 50
原始视频
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0e5d28824903484cb9436e242bb0fc49~tplv-goo7wpa0wc-image.image"></Player>


@col 50
输出视频
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/51ee8af71f0342cdbfe17851869a220e~tplv-goo7wpa0wc-image.image"></Player>

::::

### 输入参数 {#3fba8d90}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|video |视频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |
| | | \
|end_time |裁剪结束时间，默认为片源结尾。支持设置为 2 位小数，单位：秒。 |\
| |设置设置为 8，则表示在 8 秒位置结束裁剪。 |
| | | \
|start_time |裁剪开始时间，默认为 0， 表示从头开始裁剪。支持设置为 2 位小数，单位：秒。 |\
| |例如设置为 2，则表示从 2 秒的位置开始裁剪。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#6f0c0b58}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率信息。 |\
| |* type：输出结果的类型，固定为 video。 |\
| |* duration：视频的时长。 |

## concat_videos 工具 {#3d8c73ef}
concat_videos 工具内置多种转场效果，只需输入视频 URL 列表和对应的转场效果 ID 列表，工具即会自动按顺序拼接视频，并在各视频片段的拼接处添加指定的转场效果。在配置 concat_videos 工具时，你需要配置 `videos` 参数，用于输入视频的 URL，并配置 `transitions` 参数，用于指定视频转场。
### 演示效果 {#47bf301d}
将两个视频合成一个视频，并添加转场，效果如下：
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d1b734fc04ec42669db360d4ae8645f8~tplv-goo7wpa0wc-image.image"></Player>
### 输入参数 {#026544d3}
输入参数说明如下表所示：
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|videos |待拼接的视频列表，`Array<string>` 类型。支持如下两种配置方式： |\
| | |\
| |* **固定值**：直接输入视频 URL。 |\
| |* **变量**：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现音频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议总视频时长在 5 分钟以内。 |
| | | \
|transitions |转场效果 ID，`Array<string>` 类型，例如 `["1182359"]`。concat_videos 工具支持非交叠转场的效果，详情请参考[转场 ID](https://www.volcengine.com/docs/4/102412#%E8%BD%AC%E5%9C%BA-id)。 |\
| |当视频数量超过转场数量 2 个及以上时，系统将自动循环使用转场。例如有 10 个视频，2 种转场效果，那么在 9 处拼接点上，这 2 种转场效果将被依次循环使用。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#5e34c44d}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |剪辑后的视频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率信息。 |\
| |* type：输出结果的类型，固定为 video。 |\
| |* duration：视频的时长。 |

## compile_image_audio 工具 {#74133b43}
compile_image_audio 工具用于将音频和图片集合成视频，该工具还提供了多种转场效果，让图片之间的衔接更自然流畅。视频的长度取决于音频长度。在配置 compile_image_audio 工具时，你需要配置 `audio` 和 `images` 参数，用于上传视频 URL 和图片 URL，并配置 `transitions` 参数，用于指定视频转场。
### 演示效果 {#177596be}
基于音频和图片集生成视频，视频效果如下：
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a0f4ff61833d4efd8c5f2b01b7cd95b4~tplv-goo7wpa0wc-image.image"></Player>
### 输入参数 {#23be4dea}
输入参数说明如下表所示：
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|audio |音频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* **固定值**：直接输入音频 URL。 |\
| |* **变量**：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现音频的动态输入。 |\
| | |\
| |音频要求： |\
| | |\
| |* 支持处理 MP3、WAV、FLAC 等常见格式的音频。 |
| | | \
|images |图片 URL，Array<String> 类型。支持如下两种配置方式： |\
| | |\
| |* **固定值**：直接输入图片 URL。 |\
| |* **变量**：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现图片的动态输入。 |\
| | |\
| |图片要求： |\
| | |\
| |* 支持处理 JPEG、PNG、WebP 等常见格式的图片。 |
| | | \
|transitions |转场效果 ID，`Array<string>` 类型，例如 `["1182359"]`。compile_image_audio 工具支持非交叠转场的效果，详情请参考[转场 ID](https://www.volcengine.com/docs/4/102412#%E8%BD%AC%E5%9C%BA-id)。 |\
| |当图片数量超过转场数量 2 个及以上时，系统将自动循环使用转场。例如有 10 张图片，2 种转场效果，那么在 9 处拼接点上，这 2 种转场效果将被依次循环使用。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#3f020178}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率信息。 |\
| |* type：输出结果的类型，固定为 video。 |\
| |* duration：视频的时长。 |

## insert_frame 工具 {#77bde67c}
insert_frame 工具基于智能算法，能够在原视频相邻帧之间生成过渡自然的新帧，使视频帧率提升至原来的 2 倍，即如果原视频为 15 FPS，经处理后可变为 30 FPS，能有效改善视频播放时的卡顿感，让画面动作更流畅连贯。在配置 insert_frame 工具时，你需要配置 `video` 参数，用于输入视频 URL。
### 演示效果 {#51a8bf21}

::::cols
@col 50
原始视频
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d12c041679e849b08eb0f71cf4dd8202~tplv-goo7wpa0wc-image.image"></Player>


@col 50
输出视频（2倍帧率）
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/97def9bf99b7456cb6a7bca52158dce0~tplv-goo7wpa0wc-image.image"></Player>

::::

### 输入参数 {#bfa82733}
输入参数说明如下表所示：
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|video |视频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 视频时长需在 15 秒以内。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#c54b8075}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|message |执行插件时的状态描述或错误提示信息。 |
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率信息。 |\
| |* fps：视频的帧率，即每秒包含的帧数。 |\
| |* duration：视频的时长。 |

## video_super_resolution 工具 {#9be4feb1}
video_super_resolution 工具基于深度学习方法，能够根据视频信息对其进行空域、时域建模重构出缺失的细节，将低分辨率的视频重建出高分辨率视频。在配置 video_super_resolution 工具时，你需要配置 `video` 参数，用于输入视频 URL，配置 `resolution`  参数，用于指定输出视频的分辨率。
### 演示效果 {#89a08c65}

::::cols
@col 50
原始视频（分辨率 480P）
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a4b140431bc14221b0244e3bd3ae55a0~tplv-goo7wpa0wc-image.image"></Player>


@col 50
输出视频（分辨率 4K）
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bc83dce30b454ecdb676a7a1fce0b778~tplv-goo7wpa0wc-image.image"></Player>

::::

### 输入参数 {#51b5077d}
输入参数说明如下表所示：
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|resolution |输出视频的分辨率，支持设置为 720P、1080P、2K、4K。 |
| | | \
|video |原始视频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 视频时长需在 15 秒以内。 |\
| |* 原始视频最大支持的分辨率为 1920*1080。 |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#888943ce}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|message |执行插件时的状态描述或错误提示信息。 |
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率。 |\
| |* fps：视频的帧率，即每秒包含的帧数。 |\
| |* duration：视频的时长，单位：秒。 |

## add_subvideo 工具 {#5ebf0a38}
add_subvideo 工具用于为视频添加图片或视频水印。在配置 add_subvideo 工具时，你需要配置 `video` 参数，用于输入视频 URL，配置 `subvideo_url` 参数用于输入水印内容，配置 `subvideo_config` 参数，用于指定水印的样式，包括位置、大小等。其中，水印位置说明如下：
![Image=306x217](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2265e9d824b14dd68b65ca69c2424a69~tplv-goo7wpa0wc-image.image)
### 演示效果 {#18cceb56}

::::cols
@col 50
原始视频
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3f83a0e0ccc846958f604efc1ae985a8~tplv-goo7wpa0wc-image.image"></Player>


@col 50
输出视频（添加图片水印）
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/851031b80ae043a380bd567109237f8c~tplv-goo7wpa0wc-image.image"></Player>

::::

### 输入参数 {#30e211fa}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|subvideo_config |设置水印的格式，Object 类型，包含如下字段： |\
| | |\
| |* `height`：水印的高度，支持设置为百分比（相对于视频高度）或具体像素值，String 类型，例如 100% 或 100。 |\
| |* `width`：水印的宽度，支持设置为百分比（相对于视频高度）或具体像素值，String 类型，例如 100% 或 100。 |\
| |* `pos_x`：水印在水平方向（X 轴）的位置，以视频左上角为原点，单位：像素，String 类型。例如值为 0 时，表示水印处于水平方向的最左侧；值为 100 时，表示水印相对原点向右移动 100 像素。 |\
| |* `pos_y`：水印在垂直方向（Y 轴）的位置，以视频左上角为原点，单位：像素，String 类型。例如值为 0 时，表示水印在垂直方向的最上侧；值为 100 时，表示水印相对原点向下移动 100 像素。 |\
| |* `start_time`：水印的开始时间，Number 类型，单位：秒。 |\
| |* `end_time`：水印的结束时间，Number 类型，单位：秒。 |\
| | |\
| |:::tip 说明 |\
| |如果设置的水印开始时间、结束时间超出原始视频时长，那么输出视频的长度将以水印的结束时间为准，超出原始视频部分将以黑屏形式延续。例如原始视频为 20 秒，设置 `end_time` 为 30，那么输出时长为 30 秒。 |\
| |::: |\
| |```JSON |\
| |{ |\
| |  "height": "100", |\
| |  "width": "100", |\
| |  "pos_x": "100", |\
| |  "pos_y": "100", |\
| |  "start_time": 0, |\
| |  "end_time": 10 |\
| |} |\
| |``` |\
| | |\
| | |
| | | \
|subvideo_url |水印图片或视频 URL。 |
| | | \
|video |原始视频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#138052a4}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率。 |\
| |* type：输出结果的类型，固定为 video。 |\
| |* duration：视频的时长，单位：秒。 |

## add_text 工具 {#44b6a676}
add_text 工具用于为视频添加文字水印。在配置 add_text 工具时，你需要配置 `video` 参数，用于输入视频 URL，配置 `text` 参数用于设置水印的内容，配置 `text_config` 参数，用于指定水印的样式，包括位置、大小、颜色等。其中，水印位置说明如下：
![Image=306x217](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2265e9d824b14dd68b65ca69c2424a69~tplv-goo7wpa0wc-image.image)
### 演示效果 {#f9f21a0b}

::::cols
@col 50
原始视频
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3f83a0e0ccc846958f604efc1ae985a8~tplv-goo7wpa0wc-image.image"></Player>


@col 50
输出视频（添加水印）
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/704d9104cb244d1898980fd838cc8f7f~tplv-goo7wpa0wc-image.image"></Player>

::::

### 输入参数 {#61c2d916}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|text |设置水印的内容。 |
| | | \
|text_config |设置水印内容的格式、位置、颜色等属性，Object 类型，包含如下字段： |\
| | |\
| |* `font_color`：水印文字的颜色，RGBA 格式，例如 #FFFFFFFF，String 类型。 |\
| |* `font_size`：水印文字的大小，单位：像素，Integer 类型。 |\
| |* `font_type`：水印文字的字体类型，String 类型，详情请参考[字体 ID](https://www.volcengine.com/docs/4/102412#%E5%AD%97%E4%BD%93-id)， |\
| |* `background_color`：水印的背景颜色，RGBA 格式，例如 #FFFFFFFF，String 类型。 |\
| |* `background_border_width`：水印背景的边框宽度，Number 类型，单位：像素。 |\
| |* `border_color`：水印文字的描边颜色，RGBA 格式，例如 #FFFFFFFF，String 类型。 |\
| |* `border_width`：水印文字的描边宽度，Number 类型，单位：像素。 |\
| |* `start_time`：水印的开始时间，Number 类型，单位：秒。 |\
| |* `end_time`：水印的结束时间，Number 类型，单位：秒。 |\
| |* `font_pos_config.height`：水印的高度，支持设置为百分比（相对于视频高度）或具体像素值，例如 100% 或 100，String 类型。 |\
| |* `font_pos_config.width`：水印的宽度，支持设置为百分比（相对于视频高度）或具体像素值，例如 100% 或 100，String 类型。 |\
| |* `font_pos_config.pos_x`：水印在水平方向（X 轴）的位置，以视频左上角为原点，单位：像素，String 类型。例如值为 0 时，表示水印处于水平方向的最左侧；值为 100 时，表示水印相对原点向右移动 100 像素。 |\
| |* `font_pos_config.pos_y`：水印在垂直方向（Y 轴）的位置，以视频左上角为原点，单位：像素，String 类型。例如值为 0 时，表示水印在垂直方向的最上侧；值为 100 时，表示水印相对原点向下移动 100 像素。 |\
| | |\
| |:::tip 说明 |\
| |如果设置的水印开始时间、结束时间超出原始视频时长，那么输出视频的长度将以水印的结束时间为准，超出原始视频部分将以黑屏形式延续。例如原始视频为 20 秒，设置 `end_time` 为 30，那么输出时长为 30 秒。 |\
| |::: |\
| |```JSON |\
| |{ |\
| |    "font_color": "#FFFFFFFF", |\
| |    "font_size": 50, |\
| |    "font_type": "1525745", |\
| |    "background_color":"#646464FF", |\
| |    "background_border_width":2, |\
| |    "border_color":"#646464FF", |\
| |    "border_width":2, |\
| |    "start_time":0, |\
| |    "end_time":10, |\
| |    "font_pos_config": { |\
| |      "width": "10%", |\
| |      "height": "10%", |\
| |      "pos_x": "100", |\
| |      "pos_y": "100" |\
| |    } |\
| |  } |\
| |``` |\
| | |
| | | \
|video |原始视频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#4cbec785}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频 URL。 |
| | | \
|url_timeout |输出视频 URL 的有效期。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率。 |\
| |* type：输出结果的类型，固定为 video。 |\
| |* duration：视频的时长，单位：秒。 |

## video_hdr 工具 {#7dd34d4c}
video_hdr 工具基于智能算法将 SDR（标准动态范围）视频转换为 HDR （高动态范围）视频，从而提升视频的对比度、色彩丰富度，实现更好的视觉效果。在配置 video_hdr 工具时，你需要配置 `video` 参数，用于输入视频 URL。
### 演示效果 {#f877fa78}

::::cols
@col 50
原始视频
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/56cacc931fc141ef9b45f09381b3d5f4~tplv-goo7wpa0wc-image.image"></Player>



@col 50
输出视频
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9447b1eeb7db43a2ba5ab3aff9dd0209~tplv-goo7wpa0wc-image.image"></Player>


::::

### 输入参数 {#d7e69f5d}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|video |原始视频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#72f58ff3}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率。 |\
| |* fps：视频的帧率。 |\
| |* duration：视频的时长，单位：秒。 |

## ajust_video_resolution 工具 {#792d8474}
ajust_video_resolution 工具用于将视频从高分辨率转为低分辨率，例如将 1080P 转换为 720P，用于不同场景的播放。在配置 ajust_video_resolution 工具时，你需要配置 `video` 参数，用于输入视频 URL。
### 演示效果 {#23c252fe}

::::cols
@col 50
原始视频（4K）
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bc83dce30b454ecdb676a7a1fce0b778~tplv-goo7wpa0wc-image.image"></Player>



@col 50
输出视频（720P）
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4e7ade8439d54415805f06974aabc8ab~tplv-goo7wpa0wc-image.image"></Player>


::::

### 输入参数 {#69f02882}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|resolution |设置输出视频的分辨率， 支持 360p、480p、540p、720p、1080p、2k、4k。 |
| | | \
|video |原始视频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#89c80ab2}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率。 |\
| |* type：输出结果的类型，固定为 video。 |\
| |* duration：视频的时长，单位：秒。 |

## audio_mix 工具 {#ef9ed5b3}
audio_mix 工具用于对多个音频进行叠加处理，实现混音的效果。在配置 audio_mix 工具时，你需要配置 `audios` 参数，用于输入多个音频 URL。
### 输入参数 {#d1fcc691}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|audios |原始音频 URL，Array<String> 类型。输出音频的时长以最长的音频为准。 |\
| | |\
| |* **固定值**：直接输入多个音频 URL。 |\
| |* **变量**：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |音频要求： |\
| | |\
| |* 支持处理 MP3、WAV、FLAC 等常见格式的音频。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#4eee1da8}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出音频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出音频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：固定为 unknown。 |\
| |* type：输出结果的类型，固定为 audio。 |\
| |* duration：音频的时长，单位：秒。 |

## video_speed 工具 {#b6e21434}
video_speed 工具用于调整视频或音频的播放速度。在配置 video_speed 工具时，你需要配置 `video` 参数，用于输入视频 URL，配置 `speed` 参数用于指定速度调整的倍数。
### 演示效果 {#5c3cd589}

::::cols
@col 50
原始视频
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bc83dce30b454ecdb676a7a1fce0b778~tplv-goo7wpa0wc-image.image"></Player>



@col 50
输出视频（加速2倍）
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/366ca1aa8c4840d3ad14b3f9d509c84f~tplv-goo7wpa0wc-image.image"></Player>


::::

### 输入参数 {#2cc72ad4}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|speed |调整速度的倍数，取值范围为 0.1～4。 |\
| | |\
| |* 0.1：放慢至原速的 0.1 倍。 |\
| |* 1（默认值）：原速。 |\
| |* 4：加速至原速的 4 倍。 |
| | | \
|video |原始视频或音频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频或音频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |\
| | |\
| |音频要求： |\
| | |\
| |* 支持处理 MP3、WAV、FLAC 等常见格式的音频。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#d56aedfe}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频或音频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频或音频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率，仅输入源为视频时生效。 |\
| |* type：输出结果的类型，audio 或 video。 |\
| |* duration：输出结果的时长，单位：秒。 |

## ajust_audio_volume 工具 {#57d54cf6}
ajust_audio_volume 工具用于调整视频或音频中的音量。在配置 ajust_audio_volume 工具时，你需要配置 `video` 参数，用于输入视频或音频 URL，配置 `volume` 参数用于指定视频或音频中音量的扩大倍数。
### 输入参数 {#a09337a8}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|video |原始视频或音频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频或音频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |\
| |* 包含声音。 |\
| | |\
| |音频要求： |\
| | |\
| |* 支持处理 MP3、WAV、FLAC 等常见格式的音频。 |
| | | \
|volume |指定音量的扩大倍数，取值范围为0～4。 |\
| | |\
| |* 0：静音。 |\
| |* 1（默认值）：音量不变。 |\
| |* 4：声音扩大至原来的 4 倍。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#a23837e9}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频或音频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频或音频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率，仅输入源为视频时生效。 |\
| |* type：输出结果的类型，audio 或 video。 |\
| |* duration：输出结果的时长，单位：秒。 |

## video_fps 工具 {#7fcfe094}
video_fps 工具用于转换视频帧率。配置 video_fps 工具时，你需要配置 `video` 参数，用于输入视频 URL，配置 `fps` 参数，用于指定视频的目标帧率。
### 演示效果 {#1ffd115c}

::::cols
@col 50
原始视频（帧率 24）
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ac23094c63b64e84832f688905a3a78d~tplv-goo7wpa0wc-image.image"></Player>


@col 50
输出视频（帧率 60）
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a4f71521278a4ce7aba68943466ca9af~tplv-goo7wpa0wc-image.image"></Player>

::::

### 输入参数 {#8e3e423d}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|fps |设置输出视频的帧率。 |\
| |设置的帧率大于原始视频的帧率时，默认采用复制帧方式实现。 |
| | | \
|video |原始视频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#843450af}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率。 |\
| |* type：输出结果的类型，固定为 video。 |\
| |* duration：视频的时长，单位：秒。 |

## audio_loudness_normalization 工具 {#506411f9}
audio_loudness_normalization 工具用于均衡调整音频或视频的音量，避免音量过大过小的现象，提升播放体验。配置 audio_loudness_normalization 工具时，你需要配置 `video` 参数，用于输入视频或音频 URL。
### 输入参数 {#8ca82ee9}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|video |原始视频或音频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频或音频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#4c7943d9}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频或音频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频或音频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率，仅输入源为视频时生效。 |\
| |* type：输出结果的类型，audio 或 video。 |\
| |* duration：输出结果的时长，单位：秒。 |

## audio_denoise 工具 {#f77d3447}
audio_denoise 工具用于去除视频或音频中的噪声，提升音质体验。配置 audio_denoise 工具时，你需要配置 `video` 参数，用于输入视频或音频 URL。
### 输入参数 {#08f22fd0}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|video |原始视频或音频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频或音频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |\
| | |\
| |音频要求： |\
| | |\
| |* 支持处理 MP3、WAV、FLAC 等常见格式的音频。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#f1fd9695}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频或音频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率。 |\
| |* fps：输出视频的帧率。 |\
| |* duration：输出结果的时长，单位：秒。 |\
| | |\
| |:::tip 说明 |\
| |仅输入源为视频时，该输出参数才有效。 |\
| |::: |

## video_flip 工具 {#cb1aa420}
video_flip 工具用于对视频画面进行翻转，支持上下翻转、左右翻转。配置 video_flip 工具时，你需要配置 `video` 参数，用于输入视频 URL，你还可以配置 `xflip`或 `yflip` 参数，用于指定视频的翻转方向
### 演示效果 {#caefac9b}

::::cols
@col 50
原始视频
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1a3514d1cedc4cf6b429db93e919de4e~tplv-goo7wpa0wc-image.image"></Player>


@col 50
输出视频（左右翻转）
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/be002df33fef4219ab418fbc18e6e92c~tplv-goo7wpa0wc-image.image"></Player>

::::

### 输入参数 {#d35f303d}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|video |原始视频 URL，String 类型。支持如下两种配置方式： |\
| | |\
| |* 固定值：直接输入视频 URL。 |\
| |* 变量：引用开始节点的输入参数、上游节点的输出参数、用户变量、应用变量、系统变量等变量，实现视频的动态输入。 |\
| | |\
| |视频要求： |\
| | |\
| |* 支持处理 MP4、AVI、MKV、MOV 等常见格式的视频。 |\
| |* 建议视频时长在 5 分钟以内。 |
| | | \
|xflip |是否对视频进行上下翻转。Boolean 类型。默认值为 false， 表示不翻转。 |
| | | \
|yflip |是否对视频进行左右翻转。Boolean 类型。默认值为 false， 表示不翻转。 |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#904033aa}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率。 |\
| |* type：输出结果的类型，固定为 video。 |\
| |* duration：视频的时长，单位：秒。 |

## image_to_video 工具 {#7f84a015}
image_to_video 工具用于将图片转换为视频。在配置 image_to_video 工具时，你需要配置 `images` 参数，用于输入图片 URL、图片播放时长和动画效果等信息。
### 演示效果 {#7d64fba2}

::::cols
@col 50
输入参数
```JSON
[
  {
    "source": "https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7b6f8ff887f64e4bab28771e2253627f~tplv-goo7wpa0wc-image.image",
    "duration": 3,
    "animation_type": "move_up",
    "animation_in":0,
    "animation_out":2 
  }, 
  {
    "source": "https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/61f7f308f0d7411ca716767123844fc7~tplv-goo7wpa0wc-image.image",
    "duration": 3,
    "animation_type": "move_down",
     "animation_in":0,
    "animation_out":2 
  },
  {
    "source": "https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6e7d570111aa44489256a7b8591f1e30~tplv-goo7wpa0wc-image.image",
    "duration": 3,
    "animation_type": "zoom_out",
     "animation_in":0,
    "animation_out":2 
  }
]
```



@col 50
视频
<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1edc1a1728c9453e97691d121bcaa2ce~tplv-goo7wpa0wc-image.image"></Player>

::::

### 输入参数 {#e789b9ff}
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|images |原始图片 URL 合集。Array<object> 类型。包含如下子字段： |\
| | |\
| |* source：原始图片 URL。 |\
| |* duration：图片播放时长，选填，默认值：3，单位：秒，支持 2 位小数。 |\
| |* animation_type：图片的动画类型，选填，不填时无动画效果。 |\
| |   * move_up：向上移动 |\
| |   * move_down：向下移动 |\
| |   * move_left：向左移动 |\
| |   *  move_right：向右移动 |\
| |   * zoom_in：放大 |\
| |   * zoom_out：缩小 |\
| |* animation_in：动画开始时间，选填，支持2位小数。默认值：0，表示动画随图片播放同时开始，单位：秒。 |\
| |* animation_out：动画结束时间，选填，支持2位小数。默认为图片展示时长，表示动画随图片播放同时结束，单位：秒， |\
| | |\
| |```JSON |\
| |[ |\
| |  { |\
| |    "source": "image_url01", |\
| |    "duration": 3, |\
| |    "animation_type": "move_up", |\
| |    "animation_in":0, |\
| |    "animation_out":2    |\
| |  }, |\
| |  { |\
| |    "source": "image_url02", |\
| |    "duration": 3, |\
| |    "animation_type": "move_down", |\
| |    "animation_in":0, |\
| |    "animation_out":2  |\
| |  } |\
| |] |\
| |``` |\
| | |
| | | \
|url_expire |设置结果 URL 的有效期。单位：秒，默认值为 86400（1 天），最长可设置为 2592000（30 天）。 |

### 输出参数 {#5568cdd8}
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|req_id |请求 ID。 |
| | | \
|url |输出视频 URL。URL 有效期为 1 ~ 30 天，由输入参数 `url_expire` 决定，请及时转存。 |
| | | \
|bill_info |计费参考信息，Object 类型，包括如下子字段： |\
| | |\
| |* duration：视频的时长，单位：秒。 |\
| |* ratio：计费的抵扣系数。 |
| | | \
|video_meta |输出视频的元数据，Object 类型，包括如下子字段： |\
| | |\
| |* resolution：视频的分辨率。 |\
| |* type：输出结果的类型，固定为 video。 |\
| |* duration：视频的时长，单位：秒。 |

##  {#555332ad}
> * 视频剪辑工具插件 ID：7514607540051640360
