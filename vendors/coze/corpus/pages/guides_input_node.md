> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

低代码工作流中的输入节点用于在工作流运行期间收集用户输入。

## 节点说明 {#b8df27b7}

在比较复杂的工作流场景中，某些节点的执行往往需要额外的用户输入。如果上游节点中没有获取到这些信息，你可以添加一个输入节点来主动收集信息。工作流执行到输入节点时会暂时中断，直到此节点收集到必要的用户输入。

:::tip 说明
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制​**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
* 仅扣子商店、OpenAPI 渠道支持使用输入节点。
* 如果需要通过输入节点上传文件，可以通过如下方式：
   * 试运行工作流时，在弹出的卡片中通过上传文件按钮上传本地文件。
   * 将文件上传到第三方存储工具，获取一个公开可访问的 URL 地址，将此 URL 传入输入节点。
   * 通过[上传文件](/developer_guides/upload_files) API 获取文件 ID，将文件 ID 以序列化的形式传入输入节点，例如：`{"imgs":"[{\"file_id\":\"756918943296***\"}]","img":"{\"file_id\":\"75692127211375***\"}"}`。
* 单 Agent 对话流模式和多 Agents 模式，暂不支持通过工作流的输入节点上传文件。
:::

## 配置输入节点 {#9dacfc6c}

输入节点中，只需设置输入参数即可。

<!-- @cols-width: 221,634 -->
| **配置**  | **说明**  |
| --- | --- |
| 变量名  | 输入参数的名称。  |
| 变量类型  | 输入参数的数据类型，支持 String 等多种数据类型。  |
| 描述  | 参数的描述信息。  |
| 是否必选  | 参数是否必选。工作流在执行此节点时，收集到所有必选参数之后才会继续执行后续节点。  |

你也可以直接导入 JSON 格式的数据结构，示例如下：

![Image=2814x1110](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0079337a08554a1fa3eae3593608d86f~tplv-goo7wpa0wc-topic.webp)

## 示例 {#0a3807c4}

通过输入节点获取城市名称，并调用模型节点查询该地区的热门景点。

![Image=2272x328](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/514e3e0fb1704baea194d650aa46baeb~tplv-goo7wpa0wc-topic.webp)

核心节点说明如下：

<!-- @cols-width: 221,394,237 -->
| **节点类型**  | **配置说明**  | **示例**  |
| --- | --- | --- |
| 输入节点  | 添加一个必选的输入参数，名为 `city`，即用户想去的城市。  | ![Image=400x235](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/29fd5f1018414d49a011a166defedbcc~tplv-goo7wpa0wc-topic.webp)  |
| 大模型节点  | 设置以下参数： | ![Image=671x1051](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6239f13200b84e019b1d69bc7511c6bb~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | * 输入：添加一个输入参数 `city`，引用输入节点的参数 `city`。 | | \
| | * 系统提示词：智能体的人设，按需设置。 | | \
| | * 用户提示词：需要模型回答的问题，此处引用输入节点的参数 city。 | | \
| | * 输出：维持默认设置即可。  | |

执行工作流时，系统会直接执行输入节点，引导用户输入想去的城市，并根据用户提供的城市名称，由大模型生成景点导览。实际运行效果如下：

![Image=440x358](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/78da59b00abd405d8c98dd841454b9f8~tplv-goo7wpa0wc-topic.webp)
