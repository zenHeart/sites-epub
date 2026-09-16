> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子企业旗舰版支持两种语音降噪方案：声纹降噪（PDNS）和 AI 降噪（ANS）。你可以根据实际场景选择其中一种。本文介绍两种方案的实现方法。
:::tip 说明
* 仅扣子**企业旗舰版**、**原企业版**支持配置语音降噪。
* 声纹降噪（PDNS）和 AI 降噪（ANS）不能同时使用，你需要根据业务场景选择其中一种。
:::
## 实现方案对比 {#47565433}
<!-- @cols-width: 100,266,224,264 -->
| | | | | \
|**对比维度** |**声纹降噪（PDNS）** |**声纹降噪（PDNS）** |**AI 降噪（ANS）** |
|^^| | | | \
| |**自动提取说话人** |**主动设置说话人** |**自动提取说话人** |
|---|---|---|---|
| | | | | \
|**功能说明** |自动提取说话者的声纹特征，突出该人声并抑制其他说话人或背景噪音。 |预先设置目标说话者的声纹 ID，突出该人声并抑制其他说话人或背景噪音。 |从音频输入中精准区分人声与各类背景噪声，并自动过滤背景噪音，如键盘声、空调声、开关门等瞬态噪声。 |
| | | | | \
|**优点** |* 设置简单，即开即用。 |\
| |* 动态适应，自动识别说话人，灵活性高。 |* 降噪效果精准快速，对话开始即生效。 |\
| | |* 声纹信息可复用。 |* 无需额外配置。 |\
| | | |* 适应多种环境噪音。 |
| | | | | \
|**缺点** |* **降噪生效存在一定延迟**，服务端需先采集说话人一段时间的语音以提取声纹特征，此过程中降噪效果可能不佳。 |\
| |* 声纹提取准确性受说话环境影响，效果可能弱于主动设置说话人模式。 |需要提前录制声纹并获取声纹 ID。 |不针对特定说话人优化，多人说话场景可能识别到其他人的声音。 |
| | | | | \
|**典型场景** |多人会议、客服录音、多人访谈等。 |智能设备、专业直播等。 |* 直播/游戏（去键盘声）。 |\
| | | |* 远程办公（去空调、狗叫）。 |

## 实现声纹降噪（PDNS） {#6d416f30}
声纹降噪（PDNS）通过识别目标说话人的声纹特征，针对性地保留该人声并削弱非目标人声和环境噪音。声纹降噪支持两种模式，你可根据实际业务场景选择对应模式。
### 方案一：自动提取说话人 {#4cbc8e30}
自动提取说话人模式会在通话过程中自动提取当前说话者的声纹特征，进而优化目标人声并抑制其他说话人或背景噪音。**无需预先登记声纹**，适用于说话人不固定或不方便提前配置声纹的场景，可快速接入并降低配置成本。
当配置 `enable_pdns: true` 且未设置 `voice_print_feature_id` 时，默认启用**自动提取说话人**模式。

:::: tabs
@tab WebSocket 语音通话
建立 WebSocket 连接后，发送 `chat.update` 上行事件，在事件的 **data.voice_processing_config** 参数中设置 **enable_pdns** 为 **true**，开启声纹降噪。事件的详细说明请参见[双向流式对话上行事件](/developer_guides/streaming_chat_event)。 
```JSON
{
  "data": {
    "input_audio": {
      "format": "pcm",
      "codec": "pcm",
      "sample_rate": 48000
    },
    "voice_processing_config": {
      "enable_pdns": true
    },
    "output_audio": {
      "codec": "pcm",
      "pcm_config": {
        "sample_rate": 24000
      },
      "loudness_rate": 92
    },
    "turn_detection": {
      "type": "server_vad"
    },
    "need_play_prologue": true
  }
}
```


@tab RTC 语音通话
1. 调用[创建房间](/developer_guides/create_room) API 创建扣子房间。 
2. 发送 `session.update` 上行事件，在事件的 **data.voice_processing_config** 参数中设置  **enable_pdns** 为 **true**，开启声纹降噪。事件的详细说明请参见[更新房间配置](/developer_guides/signaling_uplink_event#bb460fb4)。
   ```JSON
   {
       "id": "1",
       "event_type": "session.update",
       "data": {
        "voice_processing_config": {
         "enable_pdns": true
            }
        }
   }
   ```


::::

### 方案二：主动设置说话人 {#1ab8e18c}
主动设置说话人模式基于预先登记的声纹 ID，在会话开始即可精准优化目标人声。当配置`enable_pdns: true`且指定`voice_print_feature_id`（声纹 ID）时，启用**主动设置说话人**模式。
#### 1 录制声纹并获取声纹 ID {#358b02f0}
你可以通过扣子编程录制声纹并获取声纹 ID，具体请参见[声纹识别](/guides/voiceprint_recognition)，或通过[创建声纹](/developer_guides/create_voiceprint) API 上传声纹并获取声纹 ID。

* **方式一：通过扣子编程获取声纹 ID**
   1. 组织超级管理员或管理员在扣子编程的**组织管理** > **声纹管理**页面创建声纹组和声纹。具体步骤请参见[声纹识别](/guides/voiceprint_recognition)。
      
      ::::cols
      @col 50
      创建声纹组
      ![Image=400x258](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/18d78ae2cec747d283c60b16d634dcd4~tplv-goo7wpa0wc-image.image)
      
      
      @col 50
      创建声纹
      ![Image=400x249](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1e90186eea884149a0ae03f00233983b~tplv-goo7wpa0wc-image.image)
      
      ::::

   2. 在声纹列表中获取声纹 ID。
      ![Image=400x153](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/eef3f7c732464c108e83f25f7e8cdd7e~tplv-goo7wpa0wc-image.image)
* **方式二：通过 API 获取声纹 ID**
   调用[创建声纹](/developer_guides/create_voiceprint) API 上传声纹并获取声纹 ID。
   ```JSON
   POST https://api.coze.cn/v1/audio/voiceprint_groups/75143038117378***/features \
   --header 'Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****' \
   --header 'Content-Type: multipart/form-data' \
   -F 'file=@/voice_test_data/test_1.wav;type=audio/wav' \
   -F 'name=吴经理的声纹' \
   -F 'desc=吴经理的声纹'
   ```


#### 2 开启声纹降噪 {#975bf41d}
在 WebSocket 或 RTC 语音通话的上行事件中，开启声纹降噪。

:::: tabs
@tab WebSocket 语音通话
建立 WebSocket 连接后，发送 `chat.update` 上行事件，在事件的 **data.voice_processing_config** 参数中： 

* 设置 **enable_pdns** 为 **true**，开启声纹降噪。
* 设置声纹 ID，填入预先获取的目标说话人的声纹 ID。

事件的详细说明请参见[双向流式对话上行事件](/developer_guides/streaming_chat_event)。 
```JSON
{
  "data": {
    "input_audio": {
      "format": "pcm",
      "codec": "pcm",
      "sample_rate": 48000
    },
    "voice_processing_config": {
      "enable_pdns": true,
      "voice_print_feature_id": "756356415658709***" 
    },
    "output_audio": {
      "codec": "pcm",
      "pcm_config": {
        "sample_rate": 24000
      },
      "loudness_rate": 92
    },
    "turn_detection": {
      "type": "server_vad"
    },
    "need_play_prologue": true
  }
}
```


@tab RTC 语音通话
1. 调用[创建房间](/developer_guides/create_room) API 创建扣子房间。 
2. 发送 `session.update` 上行事件，在事件的 **data.voice_processing_config** 参数中： 
   * 设置 **enable_pdns** 为 **true**，开启声纹降噪。
   * 设置声纹 ID，填入预先获取的目标说话人的声纹 ID。
   事件的详细说明请参见[更新房间配置](/developer_guides/signaling_uplink_event#bb460fb4)。
   ```JSON
   {
       "id": "1",
       "event_type": "session.update",
       "data": {
        "voice_processing_config": {
         "enable_pdns": true,
         "voice_print_feature_id": "756356415658709***" 
           }
       }
   }
   ```


::::

## 实现 AI 降噪（ANS） {#0fcca067}
ANS 专注于识别与抑制环境噪音，包括键盘敲击、空调持续噪声、开关门、街道嘈杂等，从而凸显说话者的人声。它对说话者身份不敏感，适合“背景噪音重、说话者不固定”的普适场景。

:::: tabs
@tab WebSocket 语音通话
建立 WebSocket 连接后，发送 `chat.update` 上行事件，在事件的 **data.voice_processing_config** 参数中设置 **enable_ans** 为 **true**，开启 AI 降噪。事件的详细说明请参见[双向流式对话上行事件](/developer_guides/streaming_chat_event)。
```JSON
{
  "data": {
    "input_audio": {
      "format": "pcm",
      "codec": "pcm",
      "sample_rate": 48000
    },
    "voice_processing_config": {
     "enable_ans": true
    },
    "output_audio": {
      "codec": "pcm",
      "pcm_config": {
        "sample_rate": 24000
      },
      "loudness_rate": 92
    },
    "turn_detection": {
      "type": "server_vad"
    },
    "need_play_prologue": true
  }
}
```


@tab RTC 语音通话
1. 调用[创建房间](/developer_guides/create_room) API 创建扣子房间。 
2. 发送 `session.update` 上行事件，在事件的 **data.voice_processing_config** 参数中设置 **enable_ans** 为 **true**，开启 AI 降噪。事件的详细说明请参见[更新房间配置](/developer_guides/signaling_uplink_event#bb460fb4)。

```JSON
{
    "id": "1",
    "event_type": "session.update",
    "data": {
        "voice_processing_config": {
            "enable_ans": true
        }
    }
}
```


::::


