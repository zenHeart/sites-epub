> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

本文介绍如何基于 RTC 实现按键说话或语义判停。
## 功能介绍 {#2a983337}
RTC 支持按键说话、普通自由对话和语义判停自由对话三种模式，默认采用普通自由对话模式，三种模式的对比说明如下：
<!-- @cols-width: 100,274,246,242 -->
| | | | | \
|**特性** |**按键说话模式 (client_interrupt)** |**普通自由对话模式 (server_vad)** |**语义判停自由对话模式（semantic_vad）** |
|---|---|---|---|
| | | | | \
|**控制方式** |用户通过物理按键或屏幕按钮精确控制语音识别的开始和结束。 |由云端语音活动检测 (VAD) 算法自动判断用户是否在说话。 |由服务端识别语义来判断是否停止说话。 |
| | | | | \
|**核心优势** |**精准控制**：避免背景噪音干扰，只有在用户主动操作时才传输音频，保障了通信的私密性和准确性。 |**自然流畅**：用户无需任何额外操作，像正常交谈一样即可开始和结束对话，提供了“解放双手”的无缝体验。 |**智能语义感知**：基于语义理解判断语句完整性，在语义完整时自动判停，从而加速模型响应，提升交互效率。 |
| | | | | \
|**典型场景** |* **在线游戏**：避免键盘、鼠标声干扰团队语音。 |\
| |* **智能玩具**：故事机等具备实体按键的智能玩具，防止儿童误触发，同时增强互动趣味性。 |* **语音助手**：与智能设备进行自然语言交互。 |\
| | |* **智能客服**：在呼叫中心等场景下进行流畅的语音问答。 |* 智能客服：快速识别用户咨询意图完整性，在用户描述问题后立即触发处理流程，提升客服响应速度。 |\
| | | |* 智能家居：识别多指令语义完整后判停，快速执行组合操作，无需用户停顿等待。例如 “帮我把客厅灯打开，再把空调调到 26 度”。 |
| | | | | \
|**实现方式** |当用户操作按键时，客户端发送说话开始`input_audio_buffer.start`和结束事件`input_audio_buffer.complete`给扣子编程服务端。 |客户端实现简单，只需持续采集并上报音频数据流即可，语音的开始和结束由服务端自动判断。 |在 `session.update` 上行事件中配置语音检测模式为语义判停模式（`data.turn_detection.type=semantic_vad`），根据需要配置判定语音停止的语义检测策略。 |\
| | | |事件的详细说明请参见[更新房间配置](/developer_guides/signaling_uplink_event#bb460fb4)。 |

## 实现按键说话 {#d026b374}
### 步骤一：创建房间时启用按键说话模式 {#268de6a3}
在调用[创建房间](/developer_guides/create_room) API 创建 RTC 房间时，设置语音检测类型为按键说话模式，将 `turn_detection.type` 设置为 `client_interrupt`。
```Shell
curl --location --request POST 'https://api.coze.cn/v1/audio/rooms' \
--header 'Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****' \
--header 'Content-Type: application/json' \
  --data-raw '{
      "bot_id":"750346455663573***",
      "config":{
          "turn_detection":{
              "type":"client_interrupt"
          }
      }
  }'
```

### 步骤二：客户端实现按键说话 {#71560d53}
**时序图**
![Image=600x323](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a949060c6ae74bea9d9beeab020db3dd~tplv-goo7wpa0wc-image.image)
**实现方法：**

1. 当用户按下按键时，发送 `input_audio_buffer.start` 事件，通知扣子编程服务端用户开始发言。
   关于 Realtime 信令事件的详细用法请参见[信令事件](/dev_how_to_guides/Realtime_web#045a541a)，事件示例如下：
   ```JSON
   { 
       "id": "event_id", 
       "event_type": "input_audio_buffer.start", 
       "data": {} 
   }
   ```

2. 扣子编程返回 `input_audio_buffer.started` 事件，此时服务端开始识别用户说话。
   事件示例如下：
   ```JSON
   { 
       "id": "event_id", 
       "event_type": "input_audio_buffer.started", 
       "data": {} 
   }
   ```

3. 当用户松开按键时，客户端发送 `input_audio_buffer.complete` 事件，通知扣子编程服务端语音识别完毕。
   事件示例如下：
   ```JSON
   { 
       "id": "event_id", 
       "event_type": "input_audio_buffer.complete", 
       "data": {} 
   }
   ```

4. 扣子编程返回`input_audio_buffer.completed`事件，代表服务端已确认语音识别结束。
   事件示例如下：
   ```JSON
   { 
       "id": "event_id", 
       "event_type": "input_audio_buffer.completed", 
       "data": {} 
   }
   ```


:::tip 说明
客户端重复发送`input_audio_buffer.start`或`input_audio_buffer.complete` 事件，扣子编程服务端会直接忽略，不会产生重复响应。
:::
## 实现语义判停自由对话 {#01785e63}
:::tip 说明
* **套餐限制**：仅扣子**企业旗舰版**、**原企业版**支持语义判停功能。
* **语言限制**：语义判停仅适用于中文场景，其他语种建议使用 `server_vad` 模式。
:::
### 步骤一：创建房间时启用语义判停模式 {#c1f1acb7}
在调用[创建房间](/developer_guides/create_room) API 创建 RTC 房间时，设置语音检测类型为语义判停模式，将 `turn_detection.type` 设置为 `semantic_vad`。
```Shell
curl --location --request POST 'https://api.coze.cn/v1/audio/rooms' \
--header 'Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****' \
--header 'Content-Type: application/json' \
  --data-raw '{
      "bot_id":"750346455663573***",
      "config":{
          "turn_detection":{
              "type":"semantic_vad"
          }
      }
  }'
```

### 步骤二：配置语音检测模式 {#2449de67}
客户端在 `session.update` 上行事件中配置语音检测模式为语义判停模式（`data.turn_detection.type=semantic_vad`）。
根据需要配置判定语音停止的语义检测策略：

* `data.turn_detection.semantic_vad_config.silence_threshold_ms`：当用户暂停说话时，持续静音多久后，触发语义判停检测。
* `data.turn_detection.semantic_vad_config.semantic_unfinished_wait_time_ms`：当语义检测判断该语句未结束时，持续静音多久后，扣子编程认定语音结束。

上行事件示例如下，事件的详细说明请参见[更新房间配置](/developer_guides/signaling_uplink_event#bb460fb4)。
```JSON
{
    "id": "1",
    "event_type": "session.update",
    "data": {
        "turn_detection": {
            "type": "semantic_vad",
            "semantic_vad_config": {
                // 当用户暂停说话时，持续静音多久后，触发语义判停检测。单位为 ms。默认为 300ms，支持自定义，取值范围为100ms到2000ms
                "silence_threshold_ms": 300,
                // 当语义检测判断该语句未结束时，持续静音多久后，扣子编程认定语音结束。单位为 ms。默认为500ms，取值范围为100~2000
                "semantic_unfinished_wait_time_ms": 500 
            }
        }
    }
}
```


