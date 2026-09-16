> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

[火山联网问答插件](https://www.coze.cn/store/plugin/7516843155833045026?from=add_plugin_menu&surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)基于豆包大模型及联网能力，提供联网搜索及智能体服务，在通用问答、新闻、知识百科、天气等各类业务场景中，帮助客户快速获取搜索结果。
火山联网问答插件包含 search 工具和 search_sync 工具，均用于提供搜索服务，最终返回内置的内容联网 Agent 总结过的搜索结果，开发者可以直接展示搜索结果，也可以通过基于搜索结果进一步总结和提炼。其中，search_sync 工具除了总结过的结果以外，还会返回大模型的参考内容等信息，便于开发者进一步包装，例如通过卡片 SDK 包装为检索来源卡片等。
## 使用限制 {#02c3eea6}

* 扣子主账号内所有子账号共享**火山联网问答插件**的并发限制，其值为 5。
* search_sync 工具最多只能返回 300 个字符。

## 计费说明 {#6e95b6dd}
火山联网问答插件根据插件调用次数计费，对应的计费项及单价请参考[插件费用](/coze_pro/plugin_fee)。
:::tip 说明
火山联网问答插件内包含多个工具，调用这些工具的次数将共同计入该插件的免费额度。
:::
## search 工具 {#e10f0468}
### 配置说明 {#ec88ded2}
调用 search 工具时，你需要输入核心的**搜索提示词**，以明确指定搜索的主题或目标。此外，你还可以进一步输入**背景知识**和**地址位置**，以补充搜索背景，帮助 search 工具更精准地理解搜索提示词的意图，提供更具相关性和针对性的搜索结果。
#### 输入参数 {#b556e234}
输入参数说明如下表所示：
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|content |输入需要搜索的问题，必填参数。 |
| | | \
|knowledge |设置背景知识。当需要附加环境信息、背景知识时，可以使用该字段。例如设置为`当前正在驾驶问界M8增程MAX版，车内正在播放音乐《天黑黑》`。 |
| | | \
|location_info |设置当前地理位置信息，Object 类型，支持配置 `province`、`city`、`district`、`town`、`longitude`、`latitude` 字段。示例如下： |\
| |```json |\
| |{ |\
| |        "province": "陕西省", |\
| |        "city": "西安市", |\
| |        "district": "未央区", |\
| |        "town": "玄武路", |\
| |        "longitude": 108.962354, |\
| |        "latitude": 34.303007 |\
| |    } |\
| |``` |\
| | |

#### 输出参数 {#22a6c683}
输出参数说明如下表所示：
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|sse_data |内置 Agent 总结过的搜索结果。 |

### 示例 {#9cfc948b}
例如，你可以在工作流中，通过火山联网问答插件节点添加 **search 工具**，用来搜索杭州的经典景点。示例中的节点说明如下：

* 在**开始**节点，使用默认输入参数 `input`。
* 在插件（**search**）节点，设置 `content` 参数引用开始节点的 `input` 参数，作为搜索关键词。
* 在**结束**节点，设置输出变量 `output`引用 **search** 节点输出结果中的 `sse_data` 参数，展示内置 Agent 总结过的搜索结果。

![Image=626x337](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5a16e8512daf4f048c5ebe45b525293e~tplv-goo7wpa0wc-image.image)
## search_sync 工具 {#071f2f45}
### 配置说明 {#723e8e4e}
调用 search_sync 工具时，你需要输入核心的**搜索提示词**，以明确指定搜索的主题或目标。此外，你还可以进一步输入**背景知识**和**地理位置**，以补充搜索背景，帮助 search_sync 工具更精准地理解搜索提示词的意图，提供更具相关性和针对性的搜索结果。
#### 输入参数 {#2b5e5fdf}
输入参数说明如下表所示：
<!-- @cols-width: 173,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|content |输入需要搜索的问题，必填参数。 |
| | | \
|knowledge |设置背景知识。当需要附加环境信息、背景知识时，可以使用该字段。例如设置为`当前正在驾驶问界M8增程MAX版，车内正在播放音乐《天黑黑》`。 |
| | | \
|location_info |设置当前地理位置信息，Object 类型，支持配置 `province`、`city`、`district`、`town`、`longitude`、`latitude` 字段。示例如下： |\
| |```json |\
| |{ |\
| |        "province": "陕西省", |\
| |        "city": "西安市", |\
| |        "district": "未央区", |\
| |        "town": "玄武路", |\
| |        "longitude": 108.962354, |\
| |        "latitude": 34.303007 |\
| |    } |\
| |``` |\
| | |

#### 输出参数 {#d9f5e6bd}
输出参数说明如下表所示：
<!-- @cols-width: 233,619 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|msg |执行插件时的状态描述或错误提示信息。 |
| | | \
|code |执行插件时的状态码。 |
| | | \
|log_id |日志 ID。 |
| | | \
|data.created |本次响应创建的时间戳。 |
| | | \
|data.id |本次响应的唯一 ID。 |
| | | \
|data.object |响应对象的类型，固定值为 chat.completion，表示完整聊天回复内容。 |
| | | \
|data.choices.finish_reason |搜索终止的原因。其中，stop 表示已返回完整的模型输出。 |
| | | \
|data.choices.index |当前选择的索引编号。 |
| | | \
|data.choices.message.content |内置 Agent 总结过的搜索结果。 |
| | | \
|data.choices.message.role |角色信息，固定为 assistant，代表 Agent 角色。 |
| | | \
|data.references.cover_image.url |封面图片的 URL。 |
| | | \
|data.references.id |参考内容的唯一 ID。 |
| | | \
|data.references.site_name |参考内容所属的站点名称。 |
| | | \
|data.references.source_type |参考内容来源的类型，例如 search_engine。 |
| | | \
|data.references.title |参考内容的标题。 |
| | | \
|data.references.url |参考内容的 URL。 |
| | | \
|data.usage.prompt_tokens |本次请求中模型输入 token 数量（包含意图、改写、总结等环节）。 |
| | | \
|data.usage.total_tokens |本次请求消耗的总 token 数量（输入 + 输出）。 |
| | | \
|data.usage.completion_tokens |本次请求中模型输出的 token 数量（包含意图、改写、总结等环节）。 |

### 示例 {#7cdb925b}
例如，你可以在工作流中，通过火山联网问答插件节点添加 **search_sync 工具**，用来搜索杭州的经典景点。示例中的节点说明如下：

* 在**开始**节点，使用默认输入参数 `input`。
* 在插件（**search_sync**）节点，设置 `content` 参数引用开始节点的 `input` 参数，作为搜索关键词。
* 在**结束**节点，设置输出变量 `output`引用 **search_sync** 节点输出结果中的 `data.choices.message.content` 参数，展示内置 Agent 总结过的搜索结果。

![Image=618x456](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c95bd7fe865c4f74a01da4fdd67cbb79~tplv-goo7wpa0wc-image.image)

> * 火山联网问答插件 ID：7516843396187766818




