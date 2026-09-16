> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程 Realtime SDK 是基于火山引擎 RTC 封装的音视频 SDK，主要用于实现用户与 AI 智能体之间的音视频通话功能。本文介绍 Realtime SDK 的接入流程，帮助开发者快速搭建并实现 AI 智能体与用户之间的实时音视频互动。

## 接入方案概述 {#9324f865}

你可以基于Realtime SDK 和火山引擎 RTC SDK 实现 AI 智能体与用户之间的实时音视频互动：

* **Realtime SDK**：扣子编程 Realtime SDK 是基于火山引擎 RTC 封装的音视频 SDK，封装了音视频链路相关 API，接入流程简洁高效。 支持Android（Java、Kotlin）、iOS（Objective-c、Swift）、和 Web 平台。
* **火山引擎 RTC SDK**：火山引擎原生的 RTC 客户端 SDK，支持 Android、iOS、Windows、macOS、Electron、Flutter等多平台，请根据火山引擎 RTC 的集成文档自行接入，具体请参见[集成火山引擎 RTC SDK](/dev_how_to_guides/rtc_sdk)。

## 接入流程 {#ecedd5b5}

通过 Realtime SDK 实现音视频通话的流程如下图所示。

![Image=800x126](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/32788c2f81f149d18224dbc0d2d4798a~tplv-goo7wpa0wc-image.image)

### 步骤一：创建智能体并发布为 API 服务 {#935dcb10}

1. 搭建智能体，详细步骤请参见[搭建一个低代码智能体](/guides/agent_quick_start)。
2. 发布智能体为 API 服务，详细步骤请参见[发布为 API 服务](/guides/publish_agent_api)。

### 步骤二：创建扣子房间 {#6d6dcdb3}


1. 调用[创建房间](/developer_guides/create_room) API 创建扣子房间。
   房间是一个虚拟的概念，类似逻辑上的分组，同一个房间内的用户才能互相接收和交换音视频数据、实现音视频通话。调用扣子编程提供的创建房间 API，创建一个房间，并将指定的智能体加入房间，然后才能调用 RTC SDK 和智能体开始音视频通话。
   创建房间时可以通过 `voice_id` 参数指定智能体使用的音色，扣子编程提供一系列系统音色，如果没有合适的系统音色，你也可以调用[复刻音色](/developer_guides/clone_voices)API，复刻指定音频文件中的人声音色。此外，你还可以设置房间内的音频编码格式，提高音频通话质量。
   **创建房间后会返回 appID、roomID、userID 和 Token，调用 Realtime SDK 加入房间时需要设置这些信息。**
   ::::tabs
   @tab 请求示例
   ```Bash
   curl --location --request POST 'https://api.coze.cn/v1/audio/rooms' \
   --header 'Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****' \
   --header 'Content-Type: application/json' \
   --data-raw '{
       "bot_id": "734829333445931****"
   }'
   ```
   
   @tab 响应示例
   ```JSON
   {
       "detail": {
           "logid": "202410291302044CD1CC3B4AE0897***"
       },
       "data": {
           "room_id": "room_id_7431057983427067913",   // 房间 id
           "app_id": "6705332c79516e01****",       // app_id
           "token": "0016705*****NzkxMxcANTE1MjkFAAAAAAAAAAEAAAAAAAIAAAAAAAMAAAAAAAQAAAAAACAA58QEAvxdy3LHNzSwq6apM9PUKM2rOsxIg/VB4b1xEFA=",
           "uid": "uid_7431057983427051529"
       },
       "code": 0,
       "msg": ""
   }
   ```
   
   
   ::::
2. 智能体加入房间。
   成功创建房间后，智能体会自动加入房间。
   :::tip 说明
   * 创建房间后返回的 Token，其默认有效期为 3 分钟，如果 3 分钟内没有用户加入房间，或者用户静音 3 分钟，智能体将自动退出房间，房间随即被释放，后续若要再次和智能体对话，则需重新创建房间。
   * 若有用户进入房间，智能体在房间中最长可以持续 24 小时，直至用户主动退出房间或用户设备异常断电等导致连接断开。
   :::   


### 步骤三：实现音视频通话 {#7a27cc62}

扣子编程提供了丰富的客户端 SDK，支持多种平台和语言。请根据项目需求，选择对应的 SDK。

<!-- @cols-width: 100,491 -->
|**平台** |**参考文档** |
|---|---|
|Web |[集成音视频 Realtime Web SDK](/dev_how_to_guides/Realtime_web) |
|嵌入式 |[集成音视频 Realtime 嵌入式 SDK](/dev_how_to_guides/realtime_embedded) |
|iOS |[集成音视频 Realtime iOS SDK](/dev_how_to_guides/realtime_iOS) |
|Android |[集成音视频 Realtime Android SDK](/dev_how_to_guides/realtime_android) |

##  {#3dcc5c0e}

##  {#66c10cfa}

