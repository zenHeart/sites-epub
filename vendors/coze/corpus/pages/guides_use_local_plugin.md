> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

本文介绍如何通过调用 API 与扣子编程对话并调用端插件。

## **准备工作** {#218b01d6}

* 已创建绑定了端插件的低代码智能体，并且智能体已经发布为 API 服务。
* 已申请 Access Token，且 Access Token 已授权操作会话和消息的权限。具体请参见[鉴权方式概述](/developer_guides/authentication)。

## 示例项目源码 {#bcd6b84f}

扣子编程提供端插件使用的示例项目源码， 通过扣子编程 Python SDK 实现与智能体对话并调用端插件，具体请参见 [agent_chat.py](https://github.com/coze-dev/coze-cookbook/blob/main/examples/local_plugin/agent_chat.py)。

## **使用流式响应** {#fb6b6da7}

### API 调用流程 {#72eeb921}

通过 OpenAPI 使用端插件需要关注以下几个请求：

<!-- @cols-width: 127,203,450 -->
| **API**  | **是否必须**  | **API 路径**  |
| --- | --- | --- |
| [创建会话](/developer_guides/create_conversation)  | 可选（可以复用以前的会话）  | [https://api.coze.cn/v1/conversation/create](https://api.coze.cn/v1/conversation/create)  |
| [发起对话](/developer_guides/chat_v3)  | 必选  | [https://api.coze.cn/v3/chat](https://api.coze.cn/v3/chat)  |
| [提交工具执行结果](/developer_guides/chat_submit_tool_outputs)  | 必选  | [https://api.coze.cn/v3/chat/submit_tool_outputs](https://api.coze.cn/v3/chat/submit_tool_outputs)  |

### **1 创建会话** {#8c9d6956}

调用[创建会话](/developer_guides/create_conversation) API。请求和返回示例如下：

::::tabs
@tab 请求示例
```Shell
curl --location --request POST 'https://api.coze.cn/v1/conversation/create'\
--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****' \
--header 'Content-Type: application/json' \
```



@tab 返回示例
```JSON
{
    "code": 0,
    "data": {
        "created_at": 1742820175,
        "id": "737917310581999****",
        "last_section_id": "748535563872637****",
        "meta_data": {
            "uuid": "newid1234"
        }
    },
    "detail": {
        "logid": "20250324204255377CD0E3FBFB055ADCEE"
    },
    "msg": ""
}
```


::::

### 2 **发起对话** {#8d1358a1}

调用[发起对话](/developer_guides/chat_v3) API。返回结果中， `status` 为 `requires_action`，表示已经召回了端插件。

`conversation_id` ：创建会话返回的 ID，例如上文中的 737917310581999****。

请求和返回示例如下：

::::tabs
@tab 请求示例
```Shell
curl --location --request POST 'https://api.coze.cn/v3/chat?conversation_id=748535563872637****' \
--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****' \
--header 'Content-Type: application/json' \
--data-raw '{
    "bot_id": "75049216555930***",
    "user_id": "123456789",
    "stream": true,
    "auto_save_history":true,
    "additional_messages":[
        {
            "role":"user",
            "content":"河南的降水概率",
            "content_type":"text"
        }
    ]
}'
```



@tab 返回示例
```JSON
// event:conversation.chat.requires_action 内容
{
    "id": "743436994609809****",
    "conversation_id": "743436839342099****",
    "bot_id": "737916542868753****",
    "created_at": 1730949143,
    "completed_at": 1730949146,
    "last_error": {
        "code": 0,
        "msg": ""
    },
    "status": "requires_action",
    "usage": {
        "token_count": 0,
        "output_count": 0,
        "input_count": 0
    },
    "required_action": {
        "type": "submit_tool_outputs",
        "submit_tool_outputs": {
            "tool_calls": [
                {
                    "id": "BUJJS0JKQ0dHR0VeFkNCQF5HEEZBXhJFEUJeEhFCRkESSktDREISSUI=",
                    "type": "function",
                    "function": {
                        "name": "get_rain_probability",
                        "arguments": "{\"location\":\"河南\"}"
                    },
                    "require_info": null
                }
            ]
        }
    },
    "section_id": "743436839342099****"
}
```


::::

### 3 **提交执行结果** {#991ed78e}

调用[提交工具执行结果](/developer_guides/chat_submit_tool_outputs) API。关键参数说明如下：

* `conversation_id` ：创建会话 API 返回的 ID，例如上文中的 737917310581999****。
* `chat_id` ：发起对话 API 返回的 ID，例如上文中的 743436994609809****。
* `tool_call_id` ：发起对话 API 返回的 `tool_calls.id`，例如上文中的 BUJJS0JKQ0dHR0VeFkNCQF5HEEZBXhJFEUJeEhFCRkESSktDREISSUI=。

请求和返回示例如下：

::::tabs
@tab 请求示例
```Shell
curl --location 'https://api.coze.cn/v3/chat/submit_tool_outputs?conversation_id=737917310581999****&chat_id=743436994609809****' \
--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****' \
--header 'Content-Type: application/json' \
--data '{
    "stream": true,
    "auto_save_history": true,
    "tool_outputs": [
        {
            "tool_call_id": "BUJJS0JKQ0dHR0VeFkNCQF5HEEZBXhJFEUJeEhFCRkESSktDREISSUI=",
            "output": "{\"probability\":0.5}"
        }
    ]
}'
```



@tab 返回示例
```JSON
event:conversation.chat.in_progress
data:{"id":"7434369946098090003","conversation_id":"7434368393420996671","bot_id":"737916542868753****","created_at":1730949143,"completed_at":1730949147,"last_error":{"code":0,"msg":""},"status":"in_progress","usage":{"token_count":0,"output_count":0,"input_count":0}}

event:conversation.message.completed
data:{"id":"7434371449395265576","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"tool_response","content":"{\"probability\":0.5}","content_type":"text","chat_id":"7434369946098090003","created_at":1730949495,"updated_at":1730949495}

event:conversation.message.delta
data:{"id":"7434371449395249192","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"answer","content":"河南","content_type":"text","chat_id":"7434369946098090003"}

event:conversation.message.delta
data:{"id":"7434371449395249192","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"answer","content":"的","content_type":"text","chat_id":"7434369946098090003"}

event:conversation.message.delta
data:{"id":"7434371449395249192","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"answer","content":"降水","content_type":"text","chat_id":"7434369946098090003"}

event:conversation.message.delta
data:{"id":"7434371449395249192","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"answer","content":"概率","content_type":"text","chat_id":"7434369946098090003"}

event:conversation.message.delta
data:{"id":"7434371449395249192","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"answer","content":"为","content_type":"text","chat_id":"7434369946098090003"}

event:conversation.message.delta
data:{"id":"7434371449395249192","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"answer","content":"5","content_type":"text","chat_id":"7434369946098090003"}

event:conversation.message.delta
data:{"id":"7434371449395249192","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"answer","content":"0","content_type":"text","chat_id":"7434369946098090003"}

event:conversation.message.delta
data:{"id":"7434371449395249192","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"answer","content":"$\\","content_type":"text","chat_id":"7434369946098090003"}

event:conversation.message.delta
data:{"id":"7434371449395249192","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"answer","content":"%","content_type":"text","chat_id":"7434369946098090003"}

event:conversation.message.delta
data:{"id":"7434371449395249192","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"answer","content":"$","content_type":"text","chat_id":"7434369946098090003"}

event:conversation.message.delta
data:{"id":"7434371449395249192","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"answer","content":"。","content_type":"text","chat_id":"7434369946098090003"}

event:conversation.message.completed
data:{"id":"7434371449395249192","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"answer","content":"河南的降水概率为50%。","content_type":"text","chat_id":"7434369946098090003","created_at":1730949496}

event:conversation.message.completed
data:{"id":"7434371479380312079","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"verbose","content":"{\"msg_type\":\"generate_answer_finish\",\"data\":\"{\\\"finish_reason\\\":0,\\\"FinData\\\":\\\"\\\"}\",\"from_module\":null,\"from_unit\":null}","content_type":"text","chat_id":"7434369946098090003","created_at":1730949498,"updated_at":1730949498}

event:conversation.message.completed
data:{"id":"7434371479380328463","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"follow_up","content":"影响河南降水概率的因素有哪些？","content_type":"text","chat_id":"7434369946098090003","created_at":1730949498,"updated_at":1730949498}

event:conversation.message.completed
data:{"id":"7434371479380344847","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"follow_up","content":"河南的降水概率和其他地区相比如何？","content_type":"text","chat_id":"7434369946098090003","created_at":1730949498,"updated_at":1730949498}

event:conversation.message.completed
data:{"id":"7434371479380377615","conversation_id":"7434368393420996671","bot_id":"737916542868753****","role":"assistant","type":"follow_up","content":"如何查询河南未来几天的降水概率？","content_type":"text","chat_id":"7434369946098090003","created_at":1730949498,"updated_at":1730949498}

event:conversation.chat.completed
data:{"id":"7434369946098090003","conversation_id":"7434368393420996671","bot_id":"737916542868753****","created_at":1730949143,"completed_at":1730949498,"last_error":{"code":0,"msg":""},"status":"completed","usage":{"token_count":140,"output_count":11,"input_count":129}}

event:done
data:"[DONE]"
```


::::

## **使用非流式响应** {#1e353cbe}

### API 调用流程 {#c6e9a37e}

通过 OpenAPI 使用端插件需要关注以下几个 API 请求。

<!-- @cols-width: 175,171,457 -->
| **API**  | **是否必须**  | **API 路径**  |
| --- | --- | --- |
| [创建会话](/developer_guides/create_conversation)  | 可选（可以复用以前的会话）  | [https://api.coze.cn/v1/conversation/create](https://api.coze.cn/v1/conversation/create)  |
| [发起对话](/developer_guides/chat_v3)  | 必选  | [https://api.coze.cn/v3/chat](https://api.coze.cn/v3/chat)  |
| [提交工具执行结果](/developer_guides/chat_submit_tool_outputs)  | 必选  | [https://api.coze.cn/v3/chat/submit_tool_outputs](https://api.coze.cn/v3/chat/submit_tool_outputs)  |
| [查看对话详情](/developer_guides/retrieve_chat)  | 必选  | [https://api.coze.cn/v3/chat/retrieve](https://api.coze.cn/v3/chat/retrieve)  |
| [查看对话消息详情](/developer_guides/list_chat_messages)  | 必选  | [https://api.coze.cn/v3/chat/message/list](https://api.coze.cn/v3/chat/message/list)  |

### **1 创建会话** {#3bfc0a92}

调用 API [创建会话](/developer_guides/create_conversation)。请求和返回示例如下：

::::tabs
@tab 请求示例
```Shell
curl --location --request POST 'https://api.coze.cn/v1/conversation/create'\
--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****' \
--header 'Content-Type: application/json' \
```



@tab 返回示例
```JSON
{
    "code": 0,
    "data": {
        "created_at": 1742820175,
        "id": "748535563872637****",
        "last_section_id": "748535563872637****",
        "meta_data": {
            "uuid": "newid1234"
        }
    },
    "detail": {
        "logid": "20250324204255377CD0E3FBFB055ADCEE"
    },
    "msg": ""
}
```


::::

### 2 **发起对话** {#160b7b0c}

调用[发起对话](/developer_guides/chat_v3) API。

`conversation_id` 为创建会话返回的 ID，例如上文中的 737917310581999****。

请求和返回示例如下：

::::tabs
@tab 请求示例
```Shell
curl --location --request POST 'https://api.coze.cn/v3/chat?conversation_id=737917310581999****' \
--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****' \
--header 'Content-Type: application/json' \
--data-raw '{
    "bot_id": "7504921655593****",
    "user_id": "123456789",
    "stream": false,
    "auto_save_history":true,
    "additional_messages":[
        {
            "role":"user",
            "content":"河南的降水概率",
            "content_type":"text"
        }
    ]
}'
```



@tab 返回示例
```JSON
{
    "data": {
        "id": "7434376724315504681",
        "conversation_id": "743437619659664****",
        "bot_id": "737916542868753****",
        "created_at": 1730950722,
        "last_error": {
            "code": 0,
            "msg": ""
        },
        "status": "in_progress"
    },
    "code": 0,
    "msg": ""
}
```


::::

### 3 查看对话详情 {#81f0114e}

调用[查看对话详情](/developer_guides/retrieve_chat) API。返回结果中， `status` 为 `requires_action`，表示已经召回了端插件。

::::tabs
@tab 请求示例
```Shell
curl --location 'https://api.coze.cn/v3/chat/retrieve?conversation_id=737917310581999****&chat_id=743436994609809****' \
--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****'
--header 'Content-Type: application/json' \
```



@tab 返回示例
```JSON
{
    "code": 0,
    "data": {
        "bot_id": "737916542868753****",
        "completed_at": 1730950724,
        "conversation_id": "743437619659664****",
        "created_at": 1730950722,
        "id": "743437672431550****",
        "required_action": {
            "submit_tool_outputs": {
                "tool_calls": [
                    {
                        "function": {
                            "arguments": "{\"location\":\"河南\"}",
                            "name": "get_rain_probability"
                        },
                        "id": "BUJJERJDFxISEEFeS0pEQF5HFUZBXkpASkdeQEVAEhFGEkASFRdFSUI=",
                        "require_info": {},
                        "type": "function"
                    }
                ]
            },
            "type": "submit_tool_outputs"
        },
        "status": "requires_action"
    },
    "msg": ""
}
```


::::

### **4 提交执行结果** {#c18199b1}

调用[提交工具执行结果](/developer_guides/chat_submit_tool_outputs) API。关键参数说明如下：

* `conversation_id` ：创建会话 API 返回的 ID，例如上文中的 737917310581999****。
* `chat_id` ：发起对话 API 返回的 ID，例如上文中的 743436994609809****。
* `tool_call_id` ：查看对话详情 API 返回的 `tool_calls.id`，例如上文中的 BUJJS0JKQ0dHR0VeFkNCQF5HEEZBXhJFEUJeEhFCRkESSktDREISSUI=。

请求和返回示例如下：

::::tabs
@tab 请求示例
```Shell
curl --location 'https://api.coze.cn/v3/chat/submit_tool_outputs?conversation_id=737917310581999****&chat_id=743436994609809****' \
--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****' \
--header 'Content-Type: application/json' \
--data '{
    "stream": false,
    "auto_save_history": true,
    "tool_outputs": [
        {
            "tool_call_id": "BUJJERJDFxISEEFeS0pEQF5HFUZBXkpASkdeQEVAEhFGEkASFRdFSUI=",
            "output": "{\"probability\":0.5}"
        }
    ]
}'
```



@tab 返回示例
```JSON
{
    "data": {
        "id": "7434376724315504681",
        "conversation_id": "743437619659664****",
        "bot_id": "737916542868753****",
        "created_at": 1730950722,
        "completed_at": 1730950724,
        "last_error": {
            "code": 0,
            "msg": ""
        },
        "status": "in_progress"
    },
    "code": 0,
    "msg": ""
}
```


::::

### 5 查看对话消息详情 {#e74f9425}

调用[查看对话消息详情](/developer_guides/list_chat_messages) API。关键参数说明如下：

* `conversation_id` ：创建会话 API 返回的 ID，例如上文中的 737917310581999****。
* `chat_id` ：发起对话 API 返回的 ID，例如上文中的 743436994609809****。

::::tabs
@tab 请求示例
```Shell
curl --location 'https://api.coze.cn/v3/chat/message/list?conversation_id=737917310581999****&chat_id=743436994609809****' \
--header 'Authorization: Bearer pat_xitq9LWlowpX3qGCih1lwpAdzvXNqgmpfhpV28HLWFypY37xR5Uaj2GioN****'
--header 'Content-Type: application/json' \
```



@tab 返回示例
```JSON
{
    "code": 0,
    "data": [
        {
            "bot_id": "737916542868753****",
            "chat_id": "743437672431550****",
            "content": "{\"name\":\"ts-weather_assistant-get_rain_probability\",\"arguments\":{\"location\":\"河南\"},\"plugin_id\":7374787648269074486,\"plugin_name\":\"weather_assistant\",\"api_id\":7375048893094101003,\"api_name\":\"get_rain_probability\",\"plugin_type\":6,\"thought\":\"需求为查询河南的降水概率，需要调用ts-weather_assistant-get_rain_probability工具进行查询\"}",
            "content_type": "text",
            "conversation_id": "743437619659664****",
            "created_at": 1730950724,
            "id": "743437673455807****",
            "role": "assistant",
            "type": "function_call",
            "updated_at": 1730950723
        },
        {
            "bot_id": "7379165428687536****",
            "chat_id": "743437672431550****",
            "content": "{\"msg_type\":\"interrupt\",\"data\":\"\",\"from_module\":null,\"from_unit\":null}",
            "content_type": "text",
            "conversation_id": "743437619659664****",
            "created_at": 1730950724,
            "id": "7434376734558109****",
            "role": "assistant",
            "type": "verbose",
            "updated_at": 1730950724
        },
        {
            "bot_id": "737916542868753****",
            "chat_id": "74343767243155****",
            "content": "{\"probability\":0.5}",
            "content_type": "text",
            "conversation_id": "7434376196596****",
            "created_at": 1730951153,
            "id": "7434378579980419111",
            "role": "assistant",
            "type": "tool_response",
            "updated_at": 1730951152
        },
        {
            "bot_id": "737916542868753****",
            "chat_id": "743437672431****",
            "content": "河南的降水概率为50$\\%$。",
            "content_type": "text",
            "conversation_id": "743437619659664****",
            "created_at": 1730951152,
            "id": "74343785799803****",
            "role": "assistant",
            "type": "answer",
            "updated_at": 1730951153
        },
        {
            "bot_id": "737916542868753****",
            "chat_id": "74343767243155****",
            "content": "{\"msg_type\":\"generate_answer_finish\",\"data\":\"{\\\"finish_reason\\\":1,\\\"FinData\\\":\\\"\\\"}\",\"from_module\":null,\"from_unit\":null}",
            "content_type": "text",
            "conversation_id": "743437619659664****",
            "created_at": 1730950724,
            "id": "74343767345581****",
            "role": "assistant",
            "type": "verbose",
            "updated_at": 1730950724
        },
        {
            "bot_id": "737916542868753****",
            "chat_id": "7434376724315504681",
            "content": "{\"msg_type\":\"generate_answer_finish\",\"data\":\"{\\\"finish_reason\\\":0,\\\"FinData\\\":\\\"\\\"}\",\"from_module\":null,\"from_unit\":null}",
            "content_type": "text",
            "conversation_id": "743437619659664****",
            "created_at": 1730951156,
            "id": "743437859164078****",
            "role": "assistant",
            "type": "verbose",
            "updated_at": 1730951156
        },
        {
            "bot_id": "737916542868753****",
            "chat_id": "7434376724315504681",
            "content": "降水概率的具体含义是什么？",
            "content_type": "text",
            "conversation_id": "743437619659664****",
            "created_at": 1730951156,
            "id": "74343785916407****",
            "role": "assistant",
            "type": "follow_up",
            "updated_at": 1730951156
        },
        {
            "bot_id": "737916542868753****",
            "chat_id": "743437672431550****",
            "content": "如何根据降水概率来安排户外活动？",
            "content_type": "text",
            "conversation_id": "743437619659664****",
            "created_at": 1730951156,
            "id": "743437859505464****",
            "role": "assistant",
            "type": "follow_up",
            "updated_at": 1730951156
        },
        {
            "bot_id": "737916542868753****",
            "chat_id": "7434376724315504681",
            "content": "降水概率的大小对农作物的生长有什么影响？",
            "content_type": "text",
            "conversation_id": "743437619659664****",
            "created_at": 1730951156,
            "id": "743437859505466****",
            "role": "assistant",
            "type": "follow_up",
            "updated_at": 1730951156
        }
    ],
    "msg": ""
}
```


::::

## 处理本地文件 {#36343f64}

默认情况下，通过[上传文件](/developer_guides/upload_files) API 上传本地文件仅返回文件 ID，在触发了端插件的对话中，提交端插件工具执行结果时，也仅支持将该文件 ID 返回给大模型，而大模型并无法直接理解文件 ID。为了使 [提交工具执行结果](/developer_guides/chat_submit_tool_outputs) API 能够返回大模型可理解的文件 URL， 你可参考本步骤完成相关配置。

### 步骤一：定义端插件 {#dd6cabe8}

在端插件**编辑工具**页面的**配置输入参数**区域，添加 file 类型的输入参数，支持上传 File（通用文件）、Image（图片）、Doc（文档） 和 Code（代码文件）等文件，详细类型请参考[支持的文件格式](/developer_guides/upload_files#9f8cba93)。

![Image=800x300](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7ebc4b2bdc764b1b961ff3bbace14616~tplv-goo7wpa0wc-topic.webp)

### 步骤二：上传文件 {#0bd8ac7e}

通过[上传文件](/developer_guides/upload_files) API 上传文件到扣子编程，并在返回结果中获取文件 ID（`id`）。

::::tabs
@tab 请求示例
```Shell
curl -X POST 'https://api.coze.cn/v1/files/upload' \
-H "Authorization: Bearer pat_iQhcxIIxJiKxU0OaM8sLFH7MSNZKgNW6qLoAhC9XP1oOqjIuqREhzRoMjDP2****" \
-H "Content-Type: multipart/form-data"
--form 'file=@"1120.png"'
```



@tab 返回示例
```Shell
{ 
    "code": 0, 
    "data": { 
        "bytes": 152236, 
        "created_at": 1715847583, 
        "file_name": "1120.png", 
        "id": "736949598110202****" 
    }, 
    "msg": "" 
}
```


::::

### 步骤三：提交执行结果 {#cf9e218a}

当你通过 [发起对话](/developer_guides/chat_v3) API 与绑定了端插件的智能体对话时，如果对话触发了端插件请求本地文件，那么你可以在[提交工具执行结果](/developer_guides/chat_submit_tool_outputs)API 中定义`output` 为文件 ID， [提交工具执行结果](/developer_guides/chat_submit_tool_outputs) API 会将此文件 ID 转换为可访问的文件 URL，并返回给大模型。

[提交工具执行结果](/developer_guides/chat_submit_tool_outputs) API 请求示例和返回示例如下，其中示例中的 `output` 为你在[步骤二：上传文件](/guides/use_local_plugin#0bd8ac7e)中上传的文件 ID。

::::tabs
@tab 请求示例
```Shell
curl -X POST 'https://api.coze.cn/v3/chat/submit_tool_outputs?conversation_id=747295135519236****&chat_id=747303250529034****' \
-H "Authorization: Bearer pat_iQhcxIIxJiKxU0OaM8sLFH7MSNZKgNW6qLoAhC9XP1oOqjIuqREhzRoMjDP2****" \
-H "Content-Type: application/json" \
-d '{
  "stream": false,
  "tool_outputs": [
    {
      "output": "{\"image\": \"736949598110202****\"}",
      "tool_call_id": "BUJJREUSERBBRUVeRBcXSl5HRhUVXkpFERdeFUBCRBUSEERGFhJ****"
    }
  ]
}'
```



@tab 返回示例
```Shell
{
    "id": "747524211921775****",
    "conversation_id": "747295135519236****",
    "bot_id": "746967919656768****",
    "role": "assistant",
    "type": "answer",
    "content": "为你获取到一张图片：[点击查看](https://****.png)",
    "content_type": "text",
    "chat_id": "747303250529034****",
    "created_at": 1740465986
}
```


::::

## 处理云端文件 {#c202b881}

在触发了端插件的对话中，如果涉及请求云端文件，你可参考本步骤完成相关配置。

### 步骤一：定义端插件 {#8ae56666}

在端插件**编辑工具**页面的**配置输入参数**区域，添加一个 File 类型或 String 类型的输入参数。两种类型均支持直接使用文件 URL。

![Image=800x300](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7ebc4b2bdc764b1b961ff3bbace14616~tplv-goo7wpa0wc-topic.webp)

### 步骤二：提交执行结果 {#ba79237d}

当你通过 [发起对话](/developer_guides/chat_v3) API 与绑定了端插件的智能体对话时，如果对话触发了端插件请求云端文件，那么你可以在[提交工具执行结果](/developer_guides/chat_submit_tool_outputs)API 中定义`output` 为文件 URL， [提交工具执行结果](/developer_guides/chat_submit_tool_outputs) API 会将此文件 URL 返回给大模型。

[提交工具执行结果](/developer_guides/chat_submit_tool_outputs) API  请求示例和返回示例如下：

::::tabs
@tab 请求示例
```Shell
curl -X POST 'https://api.coze.cn/v3/chat/submit_tool_outputs?conversation_id=747295135519236****&chat_id=747303250529034****' \
-H "Authorization: Bearer pat_iQhcxIIxJiKxU0OaM8sLFH7MSNZKgNW6qLoAhC9XP1oOqjIuqREhzRoMjDP2****" \
-H "Content-Type: application/json" \
-d '{
  "stream": false,
  "tool_outputs": [
    {
      "output": "{\"image\": \"https://****.png\"}",
      "tool_call_id": "BUJJREUSERBBRUVeRBcXSl5HRhUVXkpFERdeFUBCRBUSEERGFhJ****"
    }
  ]
}'
```



@tab 返回示例
```Shell
{
    "id": "747524211921775****",
    "conversation_id": "747295135519236****",
    "bot_id": "746967919656768****",
    "role": "assistant",
    "type": "answer",
    "content": "为你获取到一张图片：[点击查看](https://****.png)",
    "content_type": "text",
    "chat_id": "747303250529034****",
    "created_at": 1740465986
}
```


::::
