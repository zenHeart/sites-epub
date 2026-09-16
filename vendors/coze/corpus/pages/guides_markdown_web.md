> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

Markdown 组件用于渲染 Markdown 格式的文本。
## 属性设置 {#ca7558a1}
Markdown 组件提供了丰富的属性配置选项，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、指针、变换等通用属性的设置方法，请参考[设置组件属性和事件](/guides/set_properties_events)。
## 常用语法 {#0f63643b}
常用的 Markdown 语法及示例如下表所示。
<!-- @cols-width: 100,440,320 -->
| | | | \
|**元素** |**语法** |**效果图** |
|---|---|---|
| | | | \
|标题 |```Markdown |\
| |# 一级标题 |\
| |## 二级标题 |\
| |### 三级标题 |\
| |``` |\
| | |![Image=152x121](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/de221062d8144d72964c8bf25fbd56ae~tplv-goo7wpa0wc-image.image) |
| | | | \
|加粗文本 |```Markdown |\
| |**加粗文本** |\
| |``` |\
| | |![Image=358x39](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/327311f579964bc9b9ddb047643cd170~tplv-goo7wpa0wc-image.image) |\
| | | |
| | | | \
|斜体文本 |```Markdown |\
| |*斜体文本* |\
| |``` |\
| | |![Image=378x41](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d0d5689f9dc44642b34881597a9b9d8e~tplv-goo7wpa0wc-image.image) |\
| | | |
| | | | \
|有序列表 |```Markdown |\
| |1. 有序列表项一 |\
| |2. 有序列表项二 |\
| |``` |\
| | |![Image=205x66](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7e5b26e795304815abda2ca91e172cf6~tplv-goo7wpa0wc-image.image) |
| | | | \
|无序列表 |```Markdown |\
| |- 无序列表项一 |\
| |- 无序列表项二 |\
| |``` |\
| | |![Image=177x68](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4a54f6d53f2a4aa4ae300d8eeafb3617~tplv-goo7wpa0wc-image.image) |
| | | | \
|引用 |```Markdown |\
| |> 这是一个引用。 |\
| |``` |\
| | |![Image=269x54](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/413d926f41684d27880dc4b64fd336b7~tplv-goo7wpa0wc-image.image) |
| | | | \
|链接 |```Markdown |\
| |单击[链接](https://www.coze.cn/docs/guides/webview) |\
| |``` |\
| | |![Image=155x36](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cb393c907fec443d945a4bd5ba0e0c2d~tplv-goo7wpa0wc-image.image) |
| | | | \
|图片 |```Markdown |\
| |![这是一个图片](https://lf-coze-web-cdn.coze.cn/obj/coze-web-cn/flow/bot-studio/app-builder/example-cn.png) |\
| |``` |\
| | |![Image=305x191](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/058ee1282db7447e8aa8ec55c7db5c22~tplv-goo7wpa0wc-image.image) |
| | | | \
|视频 |Markdown 本身不支持插入视频，通常需借助 HTML 标签来实现。示例如下： |\
| |```Markdown |\
| |<video width="640" height="360" controls> |\
| |  <source src="https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/437e76ca80cc4b408a4003e13d5ac964" type="video/mp4"> |\
| |</video> |\
| |``` |\
| | |![Image=708x410](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e9725f8ad54e498f868b98e2b98f3384~tplv-goo7wpa0wc-image.image) |
| | | | \
|音频 |Markdown 本身不支持插入音频，通常需借助 HTML 标签来实现。示例如下： |\
| |```Markdown |\
| |<audio controls> |\
| |  <source src="path/to/your/audio.mp3" type="audio/mpeg"> |\
| |</audio> |\
| |``` |\
| | |![Image=341x74](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/07e92759aa9b47989359884350fa1cd4~tplv-goo7wpa0wc-image.image) |\
| | | |\
| | | |

### 绑定数据 {#91df0bb2}
Markdown 组件支持引用工作流的返回数据、组件内容、局部上下文、系统变量、界面变量等变量内容。你可以通过引用变量为 Markdown 组件绑定动态数据。详情请参见[设置组件内容参数](/guides/set_content_parameters)。
例如创建一个搜索图片的工作流，将该工作流的搜索结果（图片 URL），绑定到 Markdown 组件的图片元素中，并为 Markdown 组件配置一个事件，当 Markdown 组件加载时，自动触发工作流的调用，从而实现动态更新组件内容。

::::cols
@col 33
**绑定数据**
![Image=835x255](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e7e030b0c4844f9986c014c8844a2f8b~tplv-goo7wpa0wc-image.image)


@col 33
**配置事件**
![Image=470x702](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ea26244df9094b60b23a284d408acd3d~tplv-goo7wpa0wc-image.image)


@col 33
**展示效果**
![Image=439x314](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e6ebe9867cef467e9b83c110989492b1~tplv-goo7wpa0wc-image.image)


::::

### 设置元素对齐方式 {#a96610fc}
 你可以通过 Markdown 组件属性中的**水平对齐**、**垂直对齐**配置项，一键调整 Markdown 元素的对齐方式。
![Image=580x434](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/edb153e0f2fe4e7593d0e54dc28d4e86~tplv-goo7wpa0wc-image.image)
### 设置文本颜色 {#6d5ab758}
你可以通过 Markdown 组件属性中的**颜色**配置项，设置 Markdown 组件中纯文本元素的显示颜色。
![Image=568x420](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7b3aa9a54a0a442dacb5bf5f9267762b~tplv-goo7wpa0wc-image.image)
### 设置最大行数 {#9a692439}
你可以通过 Markdown 组件属性中的**最大行数**配置项，配置 Markdown 组件中标题和正文元素的最大显示行数，超过最大行数后显示为` ...`。
![Image=555x388](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fc4ef7ccba7c4db488f1287d13ee8719~tplv-goo7wpa0wc-image.image)
### 配置指针 {#660d6b63}
配置鼠标在指定组件区域内的指针样式。
你可以选择**根据元素类型自动显示**，也可以指定某一特定的指针样式。

::::cols
@col 50
属性配置项
![Image=212x215](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/53cbb4d927384ee28857b044f9a76f76~tplv-goo7wpa0wc-image.image)



@col 50
效果图
![Image=163x216](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8222d87281a149b499efd69cfd35fa00~tplv-goo7wpa0wc-image.image)


::::

### 添加边框和阴影效果 {#014822cf}
你可以通过 Markdown 组件属性中的**圆角**、**边框**、**阴影**等配置项，设置 Markdown 组件添加边框及阴影效果。
![Image=594x443](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/929260fbb39b4621b5e0871dd98e7eea~tplv-goo7wpa0wc-image.image)
### **隐藏组件** {#e5b1752d}
Markdown 组件的可见性可通过设置常用条件或表达式灵活控制，以实现特定场景下的隐藏或显示。

* 表达式方式
   * 设置为 false：显示组件。
   * 设置为 true：隐藏组件。
   * 设置为变量：通过变量值（true 或 false）动态控制组件的可见性。配置示例，请参考[隐藏组件](/guides/set_properties_events#46d8e38f)。
* 常用条件方式
   支持通过可视化界面设置条件，以控制组件的可见性。配置示例，请参考[隐藏组件](/guides/set_properties_events#46d8e38f)。

### 事件设置 {#18e09164}
通过配置 Markdown 组件的事件，可以为 Markdown 组件添加丰富的交互功能，以增强用户体验和界面的互动性。
<!-- @cols-width: 148,709 -->
| | | \
|**事件项** |**说明** |
|---|---|
| | | \
|事件类型 |当 Markdown 组件完成加载时触发事件。 |
| | | \
|组件方法 |支持以下方法： |\
| | |\
| |* 清除：清除组件的内容，例如 Markdown 组件中的文字。 |\
| |* 滚动到视图：将组件滚动到可视区域内。 |\
| |* 设置内容：为组件设置或更新内容。 |\
| |* 复制到剪切板：复制文本内容到剪切板。 |


