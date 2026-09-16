> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程支持开发者在搭建低代码智能体时创建一些快捷指令，方便用户在与低代码智能体会话时通过快捷指令快速、准确地输入信息。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

# 功能说明 {#4f107f7d}

配置快捷指令后，智能体用户在智能体的对话框中可以直接通过指令发起预设的对话。快捷指令的行为可以是发送一段简单的文字、上传文件、使用插件或工作流等。多 Agent 模式下，全局配置中也支持添加快捷指令，默认不指定节点回答，智能体根据用户输入匹配对应的节点处理。

例如在翻译智能体中增加一个快捷指令，即原文输入框和目标语言列表，对话时你只需输入待翻译的内容和语言即可快速下发一条翻译指令。

::::cols
@col 25
快捷指令效果：

![Image=392x699](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0da970f1014543f48fc7dd8e0bf87154~tplv-goo7wpa0wc-topic.webp)

@col 74
配置示例：

![Image=1187x557](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fa552a6ce35d4afab134975a9a42a1b9~tplv-goo7wpa0wc-topic.webp)
::::

# 创建简单指令 {#768336d2}

参考以下步骤，创建一个简单快捷指令。

1. 在编排页面，定位到**快捷指令**功能，然后单击 **+**。
2. 在弹出的页面，完成以下配置。
   <!-- @cols-width: 178,507 -->
   | **配置**  | **说明**  |
   | --- | --- |
   | 按钮名称  | 输入快捷指令的按钮名称。例如：`AI `。  |
   | 指令名称  | 输入唤起该指令的名称，只支持使用字母和下划线。例如`get_ai_news`。 | \
   | | | \
   | | 仅发布到扣子商店会展示快捷指令框，其他渠道均不会展示快捷指令框，需输入指令名称唤起快捷指令。详细说明，请参考[发布渠道说明](/guides/shortcuts#6366770e)。  |
   | 指令描述  | 添加指令说明信息。  |
   | 指令行为  | 选择**直接发送**，即用户点击该指令时，直接发送一条消息给智能体。  |
   | 指令内容  | 输入用户点击该指令时发送的内容。例如：`发送最新的三条 AI 新闻`。  |
3. 配置完成后，可以在调试区，直接点击快捷指令查看效果。
   如下图所示（左侧是快捷指令配置截图，右侧是调试截图），当点击**AI新闻**指令时，会自动发送配置好的指令内容。
   ![Image=567x317](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/78b97533f7cd410f8fcb6fbad27342b2~tplv-goo7wpa0wc-topic.webp)   


::::cols
@col 50


@col 50

::::

# 创建组件指令 {#fca41e75}

扣子编程提供了选择器、上传等组件，通过添加这些组件，可以设计更符合使用场景的快捷指令。

参考以下步骤，创建一个带组件的快捷指令。

1. 在智能体编排页面，定位到**快捷指令**功能，然后单击 **+**。
2. 在弹出的页面，完成以下配置。
   <!-- @cols-width: 131,671 -->
   | **配置**  | **说明**  |
   | --- | --- |
   | 按钮名称  | 输入快捷指令的按钮名称。例如：`翻译 `。  |
   | 指令名称  | 输入唤起该指令的名称，只支持使用字母和下划线。例如`translate`。 | \
   | | | \
   | | 仅发布到扣子商店会展示快捷指令框，其他渠道均不会展示快捷指令框，需输入指令名称唤起快捷指令。详细说明，请参考[发布渠道说明](/guides/shortcuts#6366770e)。  |
   | 指令描述  | 添加指令说明信息。  |
   | 指令行为  | 选择显示**组件模板**。 | \
   | | | \
   | | 1. 添加组件名称，并选择组件的类型。 | \
   | | 2. 单击+按钮，增加组件。 | \
   | | | \
   | | 你可以在右侧面板实时预览组件效果。 | \
   | | | \
   | | ![Image=1152x289](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ef9d1bdadeab4aa7b7369a8124ed7cfb~tplv-goo7wpa0wc-topic.webp) | \
   | | | \
   | | 如果你想直接使用工作流或插件的输出结果作为组件组成，勾选**直接使用插件或工作流**，并选择一个插件/工作流。 | \
   | | | \
   | | 系统会根据选择的插件/工作流的输出数据格式自动填充组件信息。 | \
   | | | \
   | | ![Image=416x190](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c06fe7610155479a8350c4f4d1ca9bc7~tplv-goo7wpa0wc-topic.webp)  |
   | 指令内容  | 输入用户点击该指令时发送的内容。 | \
   | | | \
   | | 单击文本框上方的绑定按钮，插入组件。 | \
   | | | \
   | | ![Image=778x196](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/91f7d60ec519452aa06b8d02278a433b~tplv-goo7wpa0wc-topic.webp) | \
   | | | \
   | | 所有添加的组件都必须要在指令内容中进行关联。 | \
   | | | \
   | | ![Image=739x194](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a85fa33174074debb839047b6c38a8d3~tplv-goo7wpa0wc-topic.webp)  |
3. 配置完成后，可以在调试区，直接点击快捷指令查看效果。
   ![Image=488x300](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2942a0909c8544ba95886d71342aea73~tplv-goo7wpa0wc-topic.webp)   


::::cols
@col 50


@col 50

::::

# 内置指令名称 {#4b42cac7}

扣子编程提供了一些内置的指令名称。

:::tip 说明
微信/抖音小程序、微信、飞书、掘金渠道支持使用内置指令。
:::

* `/clear`：清除当前智能体的对话上下文。
* `/cancel_oauth`：清除当前智能体中所有插件的 OAuth 鉴权。
* `/shortcuts`：列出当前智能体所有可用的快捷名称列表，包括自定义的指令名称和内置的指令名称。
   ![Image=314x214](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/89dc5c4af5bb41a59e99fa18402b4f1f~tplv-goo7wpa0wc-topic.webp)   


# 发布渠道说明 {#6366770e}

创建快捷指令后，仅发布到扣子商店会展示快捷指令框，其他渠道均不会展示快捷指令框，需输入指令名称唤起快捷指令。

<!-- @cols-width: 196,573 -->
| **发布渠道**  | **说明**  |
| --- | --- |
| 扣子商店  | 在智能体对话页面展示快捷指令框。 | \
| | | \
| | ![Image=523x107](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cbcfc84815a14a9bbe1e29b20d6786ab~tplv-goo7wpa0wc-topic.webp)  |
| 微信/抖音小程序、微信、飞书、豆包、多维表格、掘金、Chat SDK、API  | 在智能体对话页面，输入指令名称（例如 /getweather）唤起快捷指令。 | \
| | | \
| | ![Image=527x144](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c7addad16a3646be90faad4cf94d2118~tplv-goo7wpa0wc-topic.webp)  |

# 其他操作 {#6c74d10d}

* 拖拽快捷指令卡片调整快捷指令的顺序。
* 单击编辑图标修改快捷指令。
* 单击删除图标删除快捷指令。
   ![Image=408x136](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6ed76c974c3d4ad3b21b5330d2bba9df~tplv-goo7wpa0wc-topic.webp)
