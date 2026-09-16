> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

Lottie 动画是一款轻量级、高性能的动画解决方案。扣子低代码应用支持添加 Lottie 动画组件用于播放 Lottie 动画，增强低代码应用的视觉效果和交互体验。
## 属性设置 {#c997c6cd}
Lottie 动画组件提供了丰富的属性配置选项，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、指针、变换等通用属性的设置方法，请参考[设置组件属性和事件](/guides/set_properties_events)。
### 内置丰富的动画库 {#99b8e14d}
Lottie 动画组件内置了丰富的动画资源库，你可以直接挑选并应用合适的动画效果。
![Image=257x356](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1c5f6a0c09a745e58c02f4ea9d01fd0d~tplv-goo7wpa0wc-image.image)
### 自定义 Lottie 动画 {#6e7a89d2}
支持从本地上传 Lottie  JSON 文件并自动解析。
![Image=563x227](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a2e3fe7b9f2846ecb57cf983f30720f1~tplv-goo7wpa0wc-image.image)
### 循环播放 {#93742e48}
打开**循环播放**后，Lottie 动画会在界面加载时循环播放。
![Image=289x166](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3df0ac8913c24e30a1ee6594da80d1ba~tplv-goo7wpa0wc-image.image)
### 自动播放 {#a9c69c3b}
打开**自动播放**后，Lottie 动画会在界面加载时自动播放。
![Image=292x201](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8cde5c76da344bfebaae09d07a95f18f~tplv-goo7wpa0wc-image.image)
### 隐藏组件 {#ba990e00}
控制 Lottie 动画组件隐藏或显示的参数，支持在特定条件下隐藏 Lottie 动画组件。

* 设置为 false：显示组件。
* 设置为 true：隐藏组件。
* 设置为变量：通过变量值（true 或 false）动态控制 Lottie 动画组件的可见性。

例如在**解题详情**页面，添加了 Lottie 动画组件（Lottie1）和文本组件（text14），Lottie 动画组件用于展示应用正处于解题状态中，文本组件用于展示解题分析内容。为了实现当文本组件开始输出解题内容时，自动隐藏 Lottie 动画组件的效果，你可以在 Lottie 动画组件的**可见性**属性中，添加变量`{{ Text14.content }}`。当文本组件中开始输出解题内容时，`{{ Text14.content }}` 值变为 true，Lottie 动画组件将自动隐藏。

::::cols
@col 33
**可见性配置**
![Image=749x1024](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3e78516a6e8d474681cf72aeff8b914d~tplv-goo7wpa0wc-image.image)





@col 33
**开始解题时播放动画**
![Image=431x970](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/804eba6181244f4c9de333ca37597cae~tplv-goo7wpa0wc-image.image)



@col 33
**出现答案解析时隐藏 Lottie 动画组件**
![Image=441x945](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ca27eb5cc7f94ffe856af83c3022539a~tplv-goo7wpa0wc-image.image)


::::

## 事件设置 {#22022e78}
通过配置 Lottie 动画组件的事件，可以为 Lottie 动画组件添加丰富的交互功能，以增强用户体验和界面的互动性。
<!-- @cols-width: 148,709 -->
| | | \
|**事件项** |**说明** |
|---|---|
| | | \
|事件类型 |支持以下事件类型： |\
| | |\
| |* 点击时：当用户点击 Lottie 动画组件时触发。 |\
| |* 加载时：当 Lottie 动画组件完成加载时触发。 |\
| |* 播放完成时：当 Lottie 动画播放完成时触发。 |
| | | \
|组件方法 |支持以下方法： |\
| | |\
| |* 播放：播放 Lottie 动画。 |\
| |* 停止：停止 Lottie 动画。 |\
| |* 暂停：暂停 Lottie 动画。 |\
| |* 设置隐藏：隐藏 Lottie 动画。 |

## 配置示例 {#82120aac}
[拍照解题模板](https://www.coze.cn/template/project/7475734454254895131?from=store_search_suggestion&surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)为扣子编程的官方模板，本示例基于拍照解题模板，添加了 Lottie 动画，提升应用的交互体验。例如使用者上传题目，单击**开始解题**后，应用立即开始解题并自动播放 Lottie 动画，清晰地表达应用正在解题的状态中，使得界面交互更加生动友好；当应用完成解题后，Lottie 动画消失同时界面上展示具体的答案。
![Image=2441x1044](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/aad241aeee5a47e68d270d20b96f4263~tplv-goo7wpa0wc-image.image)
具体效果图如下：

::::cols
@col 33
开始解题时自动播放动画
![Image=431x970](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/804eba6181244f4c9de333ca37597cae~tplv-goo7wpa0wc-image.image)



@col 33
解题过程中循环播放动画
![Image=436x967](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/47c8aa38f6bd4920be9fbe2c3f9fa6c1~tplv-goo7wpa0wc-image.image)



@col 33
展示答案后隐藏动画
![Image=434x971](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/938c9e2879344c22abfc655028da81e0~tplv-goo7wpa0wc-image.image)


::::





