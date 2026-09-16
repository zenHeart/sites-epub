> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

当 AI 智能体讲话时，如果需要打断智能体发言，并开始新一轮对话，可以通过语音自动打断，包括发声即打断或通过关键词打断。本文介绍如何设置通过关键词打断语音对话。
## 场景描述 {#f14b0c1f}
扣子编程默认采用发声即打断模式，即在检测到语音输入时会中断智能体的输出。这种模式响应迅速，但在某些场景下可能导致误中断。为了更精准地控制交互，您可以切换到关键词打断模式，并设置打断关键词。该模式下，只有当用户语音中包含预设的关键词时，智能体的输出才会被中断，从而有效减少误中断，提升用户体验。
例如，在智能家居场景中，你可以通过设置关键词“你好扣子”来控制智能设备。当智能体正在播报天气信息时，用户说“你好扣子，打开客厅灯”，智能体会立即停止播报天气，转而执行打开客厅灯的操作。在智能客服场景中，你可以通过关键词“客服”打断智能客服的语音回答，直接提出新的问题，例如“客服，我想咨询退款流程”，智能客服会停止当前回答，转而解答退款相关问题。
## 效果体验 {#4b1b7479}
你可以在扣子编程智能音视频 Demo 中体验关键词打断的效果。
### Websocket 语音通话 {#b254d466}
在 [WebSocket 实时语音 Demo](https://www.coze.cn/open-platform/realtime/websocket?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=) 页面单击**发送事件**，添加如下事件，设置打断对话的关键词和打断模式。
![Image=500x336](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ceda3b8525ea4f14b4a38562d25e9048~tplv-goo7wpa0wc-image.image)
```JSON
{
  "data": {
    "input_audio": {
      "format": "pcm",
      "codec": "pcm",
      "sample_rate": 44100
    },
 "asr_config":{
              "hot_words":[
              "扣子",
              "你好扣子"
              ]
          },
    "output_audio": {
      "codec": "pcm",
      "pcm_config": {
        "sample_rate": 24000
      },
      "voice_id": ""
    },
    "turn_detection": {
      "type": "server_vad",
 "interrupt_config": {
                "mode": "keyword_contains",
                "keywords": [
                        "扣子",
                        "你好扣子"
                ]
            }
    },
    "need_play_prologue": true
  }
}
```

### RTC 音视频通话 {#8e8bf484}
在 [Realtime 智能音视频 Demo](https://www.coze.cn/open-platform/realtime/playground?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=) 页面单击 **Send Message** ，输入如下事件，设置打断对话的关键词和打断模式。
![Image=500x329](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7291201dd0a34724972dcbcc56b6cc1c~tplv-goo7wpa0wc-image.image)
```JSON
{
  "id": "1",
  "event_type": "session.update",
  "data": {
    "chat_config": {
      "allow_voice_interrupt": true,
      "interrupt_config": {
        "mode": "keyword_contains",
        "keywords": ["扣子", "你好扣子"]
      }
    }
  }
}
```

### 打断效果测试 {#d71de198}
假设预设的打断关键词为`扣子扣子`和`你好扣子`，不同场景下的触发表现如下表所示。
<!-- @cols-width: 178,106,100,516 -->
| | | | | \
|**用户的语音内容** |**智能体是否在说话** |**是否触发打断** |**表现** |
|---|---|---|---|
| | | | | \
|扣子扣子 |说话中 |✅ |智能体停止说话，进行新一轮回复，新回复的内容取决于用户智能体的设置。 |
| | | | | \
|你好扣子，给我换个故事 |说话中 |✅ |智能体停止说话，进行新一轮回复，新回复的内容取决于用户智能体的设置。 |
| | | | | \
|扣子扣子，给我换个故事 |说话中 |✅ |智能体停止说话，进行新一轮回复，新回复的内容取决于用户智能体的设置。 |
| | | | | \
|给我换个故事 |说话中 |❌ |不打断对话，智能体继续说话。 |
| | | | | \
|扣子，给我换个故事 |说话中 |❌ |不打断对话，智能体继续说话。 |
| | | | | \
|给我换个故事 |未说话 |不涉及 |智能体正常接收输入并开始回复。 |
| | | | | \
|扣子扣子，给我换个故事 |未说话 |不涉及 |智能体正常接收输入并开始回复。 |

## 设置关键词打断 {#330847fd}
### WebSocket 语音通话场景 {#eebf7ca5}
在 WebSocket 语音通话场景中，你可以通过在 `chat.update` 上行事件中设置打断对话的关键词和打断模式来实现精准打断。

1. 在 `chat.update` 上行事件中设置打断对话的关键词和打断模式，具体的事件说明可参考[更新对话配置](/developer_guides/streaming_chat_event#91642fa8)。
   <!-- @cols-width: 100,756 -->
   | | | \
   |**参数** |**说明** |
   |---|---|
   | | | \
   |keywords |打断的关键词。例如，将“扣子”和“你好扣子”设置为关键词。 |\
   | |:::tip 说明 |\
   | |支持最多 5 个关键词，每个关键词限定长度在 6 ～ 24 个字节以内（2 ～ 8 个汉字以内），不能包含标点符号。 |\
   | |::: |
   | | | \
   |hot_words |ASR 热词。为了提高 ASR 语音识别的准确性，你可以将关键词设置为热词，以便提高这些关键词的识别率。 |
   | | | \
   |mode |打断模式包括以下几种，本文以 `keyword_contains` 为例： |\
   | | |\
   | |* `keyword_contains`：说话内容**包含**关键词时，会打断模型回复。例如关键词`扣子`，用户正在说`你好呀扣子…….`或 `扣子你好呀`，模型回复会被打断。 |\
   | |* `keyword_prefix`：说话内容**前缀匹配**关键词时，会打断模型回复。例如关键词`扣子`，用户正在说`扣子你好呀……`，模型回复会被打断，而用户说`你好呀扣子……`，模型回复不会被打断。 |

   ```JSON
   { 
       "id": "event_id", 
       "event_type": "chat.update", 
       "data": { 
           "turn_detection": { 
               "type":"server_vad",
               "interrupt_config": {
                   "mode": "keyword_contains",
                   "keywords": [
                           "扣子",
                           "你好扣子"
                   ]
               }
             },
             "asr_config":{
                 "hot_words":[
                 "扣子",
                 "你好扣子"
                 ]
             }
   
       } 
   } 
   ```

2. 触发打断后，扣子编程服务端会中断语音的输出，并且发送 `conversation.chat.canceled` 下行事件，具体的事件说明可参考[智能体输出中断](/developer_guides/streaming_chat_downlink_event#fd2f7a20)。
3. 设备收到 `conversation.chat.canceled` 事件后，如果本地有缓存的音频数据，需要自行清空。
4. （可选）如果需要关闭打断模式，即设置 `type` 为 `client_vad`，或者需要切换打断模式，需要关闭当前的 WebSocket 连接后，再重新建立连接。

### RTC 音视频通话场景 {#97185c55}
在 RTC 音视频通话场景中，你可以通过在`session.update` 上行事件中设置打断对话的关键词和打断模式来实现精准打断。

1. 在 `session.update` 上行事件中设置打断对话的关键词和打断模式，具体的事件说明可参考[更新房间配置](/developer_guides/signaling_uplink_event#bb460fb4)。
   <!-- @cols-width: 100,756 -->
   | | | \
   |**参数** |**说明** |
   |---|---|
   | | | \
   |keywords |打断的关键词。例如，将“扣子”和“你好扣子”设置为关键词。 |\
   | |:::tip 说明 |\
   | |支持最多 10 个关键词，每个关键词长度不超过 8 个字。 |\
   | |::: |
   | | | \
   |mode |打断模式包括以下几种，本文以 `keyword_contains` 为例： |\
   | | |\
   | |* `all`：任意内容都可以打断模型回复。 |\
   | |* `keyword_contains`：说话内容**包含**关键词时，会打断模型回复。例如关键词`扣子`，用户正在说`你好呀扣子…….`或 `扣子你好呀`，模型回复会被打断。 |\
   | |* `keyword_prefix`：说话内容**前缀匹配**关键词时，会打断模型回复。例如关键词`扣子`，用户正在说`扣子你好呀……`，模型回复会被打断，而用户说`你好呀扣子……`，模型回复不会被打断。 |

   ```JSON
   {
     "id": "1",
     "event_type": "session.update",
     "data": {
       "chat_config": {
         "allow_voice_interrupt": true,
         "interrupt_config": {
           "mode": "keyword_contains",
           "keywords": ["扣子", "你好扣子"]
         }
       }
     }
   }
   ```

2. 触发打断后，扣子编程服务端会首先中断语音的输出，并且发送 `audio.agent.speech_stopped` 下行事件，具体的事件说明可参考[智能体结束说话 ](/developer_guides/signaling_downlink_event#78b17cf2)。

## 常见问题 {#0cd74ff4}
### **发送语音打断后，智能体仍继续说话** {#6f6e1af4}
**问题原因**：
语音打断后，扣子编程服务端不再推送音频，但本地设备端可能会缓存一段音频数据。
**解决方法**：
打断对话后，服务端会下发一个事件到客户端。客户端收到事件后，需要清空设备侧的缓冲区。



