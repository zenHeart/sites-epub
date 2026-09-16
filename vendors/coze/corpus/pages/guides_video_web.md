> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

视频组件用于播放视频内容，支持播放本地上传的视频文件，也可绑定工作流返回值或直接填写视频 URL，能够灵活满足不同视频播放需求。
![Image=536x245](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/03ee6d1ebfa44f608b5cd447afb8cf5f~tplv-goo7wpa0wc-image.image)
## 视频限制 {#b14aa668}

* 仅支持 MP4、AVI、MOV 格式。
* 视频文件大小需小于 500 MB。

## 属性设置 {#beceba4b}
视频组件提供了丰富的属性配置选项，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、指针、变换等通用属性的设置方法，请参考[设置组件属性和事件](/guides/set_properties_events)。
### 配置视频源 {#915b203a}
你可以上传本地视频文件、直接输入视频 URL（绑定静态数据）或绑定工作流返回的视频 URL（绑定动态数据）。

::::cols
@col 33
**本地上传**
在**本地上传**页签下，单击**上传**，上传本地视频文件。
![Image=272x181](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/433e3adcf94b428584d2c6fc0c37e236~tplv-goo7wpa0wc-image.image)


@col 33
**绑定静态数据**
在**绑定数据**页签下，输入视频的 URL。
![Image=268x266](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f14b31b047e04fd8af71eb6c678c4d17~tplv-goo7wpa0wc-image.image)



@col 33
**绑定动态数据**

1. 为组件添加事件，用于调用工作流。
   可以选择本应用中的任意目标组件。
2. 在**绑定数据**页签下，选择工作流的输出参数。具体操作，请参考[配置示例](/guides/video_web#271e6d71)。
   ![Image=248x224](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8e0a912c8553483cb4e86a11b2d7ac63~tplv-goo7wpa0wc-image.image)

::::

### 全屏播放 {#9f8f751b}
打开**全屏播放**开关后，视频组件中将显示**全屏播放**按钮。单击该按钮后，可以全屏播放视频。
![Image=672x228](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7f4e3bafa7f64175a6a868d84f00b561~tplv-goo7wpa0wc-image.image)
### 循环播放 {#55bcc7ca}
打开**循环播放**后，视频会在界面中循环播放。
![Image=294x273](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/72b01656e71b46c183b3c0a263096461~tplv-goo7wpa0wc-image.image)
### 隐藏组件 {#bdedf0b9}
视频组件的可见性可通过设置常用条件或表达式灵活控制，以实现特定场景下的隐藏或显示。

* 表达式方式
   * 设置为 false：显示组件。
   * 设置为 true：隐藏组件。
   * 设置为变量：通过变量值（true 或 false）动态控制组件的可见性。配置示例，请参考[隐藏组件](/guides/set_properties_events#46d8e38f)。
* 常用条件方式
   支持通过可视化界面设置条件，以控制组件的可见性。配置示例，请参考[隐藏组件](/guides/set_properties_events#46d8e38f)。

## 事件设置 {#1f886944}
通过配置视频组件的事件，可以为视频组件添加丰富的交互功能，以增强用户体验和界面的互动性。
<!-- @cols-width: 148,709 -->
| | | \
|**事件项** |**说明** |
|---|---|
| | | \
|事件类型 |支持以下事件类型： |\
| | |\
| |* 点击时：单击视频时，触发事件。 |\
| |* 开始播放时：视频开始播放时，触发事件。 |\
| |* 暂停播放时：视频暂停播放时，触发事件。 |\
| |* 播放结束时：视频结束播放时，触发事件。 |
| | | \
|组件方法 |支持以下组件方法： |\
| | |\
| |* 播放：播放视频 |\
| |* 暂停：暂停视频 |\
| |* 设置隐藏：隐藏组件，使其不可见。 |

## 配置示例 {#271e6d71}
例如搭建一个用于生成及展示视频的应用，则你可以创建一个视频生成的工作流，并通过视频组件动态展示。具体操作如下：

1. 创建工作流（video）。
   使用视频生成节点生成视频。其中，在**结束**节点中，设置输出变量 `output` 的值为视频生成节点输出结果中的 `video` 参数（生成的视频 URL）。
   ![Image=808x163](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/28650a8908824c0385666d194bc66be8~tplv-goo7wpa0wc-image.image)
2. 搭建网页。
   搭建一个视频生成网页，包括容器组件、文本输入组件、按钮组件和视频组件。
   ![Image=692x439](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6b60e403b5cf450c80fbd718d7c99897~tplv-goo7wpa0wc-image.image)
3. 为按钮组件（Button1）配置事件。
   输入提示词，单击**生成视频**按钮后，将触发工作流（video）生成视频。工作流的输入参数 `input` 引用文本输入组件（Textarea1）的值。
   ![Image=243x361](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8b8defc0938f4ce9a1902bf7f9c64d1c~tplv-goo7wpa0wc-image.image)
4. 为视频组件绑定数据，即绑定工作流（video）的输出参数 `output`。
   ![Image=244x245](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/797d0349b12b400eab0aa7674d4dd169~tplv-goo7wpa0wc-image.image)
5. 预览效果。
   输入`风吹动窗帘和花朵，光线变化，固定镜头`，单击**生成视频**后，页面中将展示生成的视频。
   ![Image=650x490](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/caa8f98d62674f80902849bb6cab0263~tplv-goo7wpa0wc-image.image)


