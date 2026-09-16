> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

本文介绍如何通过输出节点、端插件或云侧插件实现语音控制设备，例如调节音量、拍照识别等。
## 实现方案对比 {#9e844d91}
<!-- @cols-width: 100,258,312,169 -->
| | | | | \
|**方案** |**通过输出节点传递语音指令** |**端插件** |**云侧插件** |
|---|---|---|---|
| | | | | \
|适用场景 |适用于仅需下发指令而无需设备返回数据的单向控制场景，如调节音量、控制设备移动、转人工等。 |需要从设备端获取数据（如摄像头图像、传感器数据），并根据数据执行后续处理的场景，如拍照识别、获取手机日历等。 |需要跨设备控制的场景。 |

## 方案一：通过输出节点传递语音指令 {#3bd34482}
通过对话流中的输出节点，可将意图识别后的语音指令传递至设备。适用于简单的、单向的设备控制，例如调节音量或转人工等。具体实现流程如下：
在对话流中分别配置意图识别和输出节点，当意图识别到需要调节音量等设备控制时，扣子编程向设备发送`conversation.message.completed` 事件，例如 `type= "answer", content_type="text", content = {"action": "volume_up"} `，设备根据 `content` 字段获取控制指令并执行相应的设备操作。事件详情请参见[消息完成](/developer_guides/streaming_chat_downlink_event#c817e22b)事件。
### 时序图 {#57312174}
![Image=600x458](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c0900486eb2541608dca35d64242f5c2~tplv-goo7wpa0wc-image.image)
### 1 搭建对话流 {#1bfcbbd6}
以智能家居场景下，实现语音调节音量与语音闲聊功能为例。对话流的编排详情如下图所示。
![Image=5593x1500](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/897dc0610e234a19969a17ccdaaa7397~tplv-goo7wpa0wc-image.image)
各节点的详细配置如下。
<!-- @cols-width: 141,339,343 -->
| | | | \
|**节点** |**说明** |**示例** |
|---|---|---|
| | | | \
|开始节点  |**开始节点**的输入参数保持默认值即可。 |![Image=200x124](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f5f622f2f17e4308b074ece13a4a3976~tplv-goo7wpa0wc-image.image) |
| | | | \
|意图识别（大模型节点） |通过开始节点中的用户输入进行意图识别。 |\
| | |\
| |* **模型**：选择 **doubao 1.5-lite-32k** 或**豆包·角色扮演·Pro** 等支持复杂多轮对话的模型。 |\
| |* **输入**：引用开始节点的 `USER_INPUT`。建议开启会话历史，确保模型结合上下文判断意图。 |\
| |* **系统提示词**：根据实际场景调整系统提示词中的意图，本文的系统提示词样例请参见[提示词样例](/tutorial/control_device_via_voice#70719ea2)。 |\
| | |\
| |:::tip 说明 |\
| |* 为了降低大模型的响应时间，建议参考本文通过大模型节点实现意图识别，而不是使用对话流自带的意图识别节点，因为自带的意图识别节点采用直接输出内容的方式，会导致输出的 Token 数量过多，从而增加响应时间。 |\
| |* 意图识别的输出结果用序号（例如1、2、3）来标识意图，避免让大模型直接返回完整回答，否则，会导致输出的 Token 数量过多，从而显著增加响应时间。具体原理请参见[优化大模型响应时间](/tutorial/llm_response_time)。 |\
| |::: |![Image=200x487](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/58c38af6067741cc951a57a56259eb09~tplv-goo7wpa0wc-image.image) |
| | | | \
|选择器 |智能体根据意图识别返回的值，判断进入设备控制节点或闲聊节点。 |\
| | |![Image=200x163](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/20f47684cab4490687c70b7d8f7932d0~tplv-goo7wpa0wc-image.image) |
| | | | \
|输出节点-设备控制（输出节点）  |用于下发设备控制指令。 |\
| | |\
| |* **输出内容**：根据实际场景调整输出内容中的设备控制指令。例如：`{"action": "volume_up"}`。 |\
| |* **通话中转语音**：配置音视频通话时是否朗读输出节点的消息内容。若不希望设备控制指令通过TTS 朗读，可关闭此功能。 |\
| |* **会话历史写入**：设置为不写入。 |![Image=200x222](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b1be9b3d675745aab537f5100b9ff04c~tplv-goo7wpa0wc-image.image) |
| | | | \
|闲聊（大模型节点）  |实现语音闲聊功能。 |\
| | |\
| |* **输入参数**：`input` 参数的值引用开始节点的 `USER_INPUT`。 |\
| |* **系统提示词**：根据实际情况调整闲聊的回复逻辑和风格。本文的系统提示词请参见[提示词样例](/tutorial/control_device_via_voice#70719ea2)。 |\
| |* **用户提示词**：引用输入参数中的 `input` 参数。 |![Image=200x428](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bfc550d36a6d43e7b05e0fddc7c728ed~tplv-goo7wpa0wc-image.image) |
| | | | \
|输出节点 |用于输出闲聊节点的结果，输出变量的值引用闲聊节点的输出参数。 |![Image=200x115](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f071bb22ed844656b27071f8589129a6~tplv-goo7wpa0wc-image.image) |
| | | | \
|结束节点 |因为已通过前面的输出节点输出工作流的结果，所以结束节点无需返回变量或文本。 |![Image=200x147](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/022d4272128e4dc7a56ff8b889bc8092~tplv-goo7wpa0wc-image.image) |

### 2 测试并发布智能体 {#059cc598}

1. 试运行并发布对话流。
2. 创建**单 Agent（对话流模式）​**的智能体，在智能体中添加对话流，开启语音通话并设置音色。
3. 在智能体右侧的调试页面单击通话图标，语音输入**调大音量**，智能体将返回设备控制指令 `{"action": "volume_up"}`。
   ![Image=600x371](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cd7783e1ca684ee4be5ede9a6e62f6e7~tplv-goo7wpa0wc-image.image)
4. 将智能体发布到 API 渠道或其他目标渠道。

## 方案二：端插件 {#d500e086}
本文以 AI 眼镜为例，介绍用户通过语音输入指令后，智能体如何调用端侧插件实现拍照与物体识别。
### 时序图 {#e89a0f80}
![Image=600x440](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/44670588223c4571842f8c4e6e269699~tplv-goo7wpa0wc-image.image)
### 搭建智能体 {#1c0d5267}
#### 1 复制智能体模板 {#7a6f5346}

1. 打开[AI 眼镜小助手](coze.cn/template/agent/7527496694058139686)智能体，然后单击**复制**。
   ![Image=500x250](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/179f4a83e607474388dcefa57adb6c14~tplv-goo7wpa0wc-image.image)
2. 选择智能体的所属空间并输入一个智能体名称，然后单击**确定**。
3. （可选）在复制的智能体编排页面，单击智能体名称旁的修改图标，修改智能体名称。
4. 根据实际需求，修改开场白文案和预置问题。

#### 2 调整对话流 {#b10df9f5}
对话流的编排详情如下图所示。
![Image=8266x3373](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3eb32468db7345e4888f76003963ec4a~tplv-goo7wpa0wc-image.image)
根据实际场景，在对话流中调整相应的节点和子工作流。本文重点介绍设备拍照分支的实现逻辑，其他子工作流的实现逻辑请参见[搭建低延时语音助手](/tutorial/low_latency_voice_assistant)。各节点配置要求如下：
<!-- @cols-width: 181,338,343 -->
| | | | \
|**节点** |**说明** |**示例** |
|---|---|---|
| | | | \
|意图识别（大模型节点） |通过开始节点中的用户输入进行意图识别，判断是否需要调用端插件。每种意图分别对应一个子工作流。 |\
| | |\
| |* **模型**：选择 **doubao 1.5-lite-32k** 或**豆包·角色扮演·Pro** 等支持复杂多轮对话的模型。 |\
| |* **输入**：需要开启会话历史，确保模型结合上下文判断意图。 |\
| |* **系统提示词**：根据实际场景调整系统提示词中的意图。 |\
| | |\
| |:::tip 说明 |\
| |* 为了降低大模型的响应时间，建议参考本文通过大模型节点实现意图识别，而不是使用对话流自带的意图识别节点，因为自带的意图识别节点采用直接输出内容的方式，会导致输出的 Token 数量过多，从而显著增加响应时间。 |\
| |* 意图识别的输出结果用序号（例如1、2、3）来标识意图，避免让大模型直接返回完整回答，否则，会导致输出的 Token 数量过多，从而显著增加响应时间。具体原理请参见[优化大模型响应时间](/tutorial/llm_response_time)。 |\
| |::: |![Image=200x683](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a227898248a042a3b719892044089539~tplv-goo7wpa0wc-image.image) |
| | | | \
|获取当前时间（代码节点） |通过代码获取实时日期和时间，添加输出参数`current_time` 和 `current_date`，作为后续大模型的输入参数，用于生成当前时间相关的回答。 |```Python |\
| | |from datetime import datetime |\
| | | |\
| | | |\
| | |async def main(args: Args) -> Output: |\
| | |    current_time = datetime.now() |\
| | |    formatted_date = current_time.strftime("%Y-%m-%d") |\
| | |    formatted_time = current_time.strftime("%H:%M") |\
| | |    ret: Output = { |\
| | |        "current_date": formatted_date, |\
| | |        "current_time": formatted_time         |\
| | |    } |\
| | |    return ret |\
| | |``` |\
| | | |\
| | |![Image=200x298](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/069eb3940ad74cec8732eae210b4a8d9~tplv-goo7wpa0wc-image.image) |
| | | | \
|选择器 |智能体根据意图识别返回的值，进入对应的子工作流，例如设备拍照分支。 |![Image=200x433](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3efdde55ad7a486494d12e1ee77ef8cd~tplv-goo7wpa0wc-image.image) |
| | | | \
|photograph（端插件）  |通过[设备控制端插件](https://www.coze.cn/store/plugin/7527323690468393014?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)实现设备拍照，并将图片上传到服务端。 |![Image=200x198](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cc3a5c13d780443e95f75f9bf6272acc~tplv-goo7wpa0wc-image.image) |
| | | | \
|视觉理解（大模型节点） |接收端插件上传的图片信息，并结合用户原始问题进行多模态理解。 |\
| | |\
| |* 输入参数： |\
| |   * `input` ：参数的值引用开始节点的`USER_INPUT`。 |\
| |   * `image` ：参数的值引用 photograph 端插件输出的 image。 |\
| |   * `current_date` 和 `current_time` ：参数的值引用**获取当前时间**节点的输出。 |\
| |* 系统提示词：根据实际场景，修改系统提示词中的技能。 |\
| |* 用户提示词：引用输入参数中的 `input` 和`image`参数。 |![Image=200x440](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4b120e334d7a4daf96d6ea8bdf8a0a4d~tplv-goo7wpa0wc-image.image) |
| | | | \
|输出 |将视觉理解节点的分析结果返回给用户。建议开启流式输出，以提升用户体验。 |![Image=200x272](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6867d46cacf043599191b7616fbf40b7~tplv-goo7wpa0wc-image.image) |

### 发布并验证效果 {#b7cdb493}

1. 试运行并发布对话流。
2. 将智能体发布到 API 渠道。
3. 验证效果。
   1. 访问 [Realtime 智能音视频 Demo](https://www.coze.cn/open-platform/realtime/playground?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)，单击 **Settings**，设置 Token 和对应的智能体。单击 **Connect**。
      ![Image=600x410](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5769c9e70a2349a9b02f0320b85d0256~tplv-goo7wpa0wc-image.image)
   2. 语音输入指令，例如`这是什么东西`，验证智能体是否能正确触发端插件。例如 Demo 弹出 Function Call 事件对话框表示已触发端插件。
   3. 通过[上传文件](/developer_guides/upload_files)API 获取图片 ID，并将图片 ID 填入提交端插件执行结果的 `output` 中。
      ![Image=600x325](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/31e7fa2335fa422d9c38bbe55564ce2b~tplv-goo7wpa0wc-image.image)

### 端插件实现流程 {#d7d9bdce}
设备端需要实现完整的事件监听、执行和上报闭环，具体步骤如下：
#### 1. 接收`required_action`事件 {#b51e9774}
当对话流触发端插件时，设备会收到 `conversation.chat.requires_action` 事件，其中包含需要调用的函数信息，如 `photograph`。
下行事件示例：
```JSON
{
    "id": "event_15",
    "event_type": "conversation.chat.requires_action",
    "data": {
        "id": "7527500166237***",
        "conversation_id": "7527503562080***",
        "required_action": {
            "type": "submit_tool_outputs",
            "submit_tool_outputs": {
                "tool_calls": [
                    {
                        "id": "5871369658880***",
                        "type": "function",
                        "function": {
                            "name": "photograph",
                            "arguments": ""
                        }
                    }
                ]
            }
        }
    }
}
```

#### 2. 执行设备能力并上传文件 {#7384f102}
设备根据 `function.name` 调用本地能力，例如摄像头拍照。调用[上传文件](/developer_guides/upload_files) API，将拍照的图片上传至服务端，并获取图片 ID。
上传文件 API 示例：
```Bash
curl -X POST 'https://api.coze.cn/v1/files/upload' \
-H "Authorization: Bearer cztei_qTST5l1tkfumssw***" \
-H "Content-Type: multipart/form-data" \
--form 'file=@"ai_glasses_capture.jpeg"'
```

#### 3. 提交端插件执行结果 {#8dd13de0}
设备将获取到的 `file_id` 通过 `conversation.chat.submit_tool_outputs` 事件提交给扣子编程，以驱动对话流继续执行。
:::tip 说明
`chat_id`、`tool_call_id` 需要与 `conversation.chat.requires_action` 事件中的 ID 保持一致。
:::
上行事件示例：
```JSON
{
  "id": "1",
  "event_type": "conversation.chat.submit_tool_outputs",
  "data": {
    "chat_id": "7527500166237***",
    "tool_outputs": [
      {
        "tool_call_id": "5871369658880***",
        "output": "{\"image\":\"$file_id\"}"
      }
    ]
  }
}
```

## 方案三：云侧插件 {#cac26a39}
需将设备控制相关服务封装为自定义云侧插件，具体实现方法请参见[基于 API 创建插件](/guides/services)。
在对话流中添加该云侧插件。当意图识别结果为设备控制时，智能体调用该云侧插件。插件对应的服务端接收请求后，根据请求中的通话 ID 信息，执行相应设备操作。
云侧插件的对话流编排详情如下图所示，各节点的配置和其他方案类似。
![Image=5593x1500](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ca85cf8dd70d4c25a5821c8a96bc74e4~tplv-goo7wpa0wc-image.image)
时序图
![Image=600x337](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/67c0ca19b64f46e0b1b574d510c19175~tplv-goo7wpa0wc-image.image)
## 提示词样例 {#70719ea2}

::::cols
@col 50
意图识别节点
```JSON
### 角色
你是一位杰出的意图识别专家，具备极为敏锐的洞察力，能够迅速且精准地判断用户问题的意图类型。在接收到用户问题时，需紧密结合当前用户输入以及历史消息，全面且深入地剖析问题的核心内涵。
### 技能
#### 技能 1：精准识别用户意图
依据以下意图列表，仅返回与之对应的数字序号。
| 序号 | 意图         | 描述                                                         | 示例                                                         |
| :--: | :----------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
|  1   | 设备控制     | 涉及需要控制设备的操作                         | "调大音量" |
|  2   | 无需联网     | 属于闲聊范畴，或可单纯依靠基础知识库解答；或是用户明确提出不联网需求；亦或是涉及通用概念、原理性的问题、用户的主观感受 | “三角形内角和是多少”“给我讲个笑话”“我不想联网，给我说说历史故事”“你觉得/你认为/你有没有/你平时”|
### 回复格式
- 仅回复意图对应的序号：1、2

### 示例
#### 示例 1
当前用户输入：我感觉好无聊呀
2
#### 示例 2
当前用户输入：调大音量
1
### 限制
- 若遇到难以理解或把握不准的问题，统一归类到 2。
- 用户输入中可能涵盖一个或多个上述意图，需根据输入内容输出最为贴近的一个意图序号，仅回复一个数字，无需阐述原因。  
```



@col 50
闲聊节点
```JSON
# 角色
你是一个高效且知识渊博的生活小助理，能陪伴用户

## 技能
### 技能 1: 闲聊陪伴
1. 积极与用户互动，倾听用户的心声，给予温暖的回应，回复100字左右
2. 结合历史消息和用户当前输入，根据用户的话题展开有趣的讨论，让用户感受到陪伴。


## 回答格式
- 直接输出文本，不要输出json

## 限制:
- 只回答与生活相关或百科知识范围内的问题，拒绝回答无关话题。
- 所输出的内容必须按照给定的格式进行组织，不能偏离框架要求。
- 请确保信息来源准确可靠，必要时注明引用来源。
```


::::

###  {#5e8c5626}
