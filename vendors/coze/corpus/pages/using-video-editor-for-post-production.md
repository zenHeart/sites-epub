> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

在制作 AI 视频时，生成出满意的片段只是第一步。想要让整条视频更连贯、更干净、更适合发布，还需要对视频片段进行一些后期编辑。

本教程将介绍扣子视频编辑器中的 3 个实用功能：

* **截图取帧**：让前后片段衔接更自然
* **字幕擦除**：去除视频中的字幕、乱码或文字
* **画质优化**：提升视频清晰度，适合正式发布或商业使用

这些功能可以帮助你减少重复生成的成本，也能让 AI 视频从**能看**，进一步变成**更顺、更清晰、更适合发布**。

## 截图取帧：解决片段衔接不连贯 {#hKBawOwM9}

### 适用场景 {#hnf3udbdA}

在制作长视频或多片段视频时，常见的问题是：两个片段之间的画面衔接不够流畅。

例如人物的位置、动作或状态发生了明显跳变：

* 上一个片段中，主角刚进入墓道
* 下一个片段中，主角却突然从墓道左侧出现

这类问题会让观众感觉剧情跳跃或有所中断。这时，可以使用**截图取帧**功能，将上一个片段的尾帧作为下一个片段的参考素材，让后续生成的视频更好地延续前一段画面。

:::tip 说明
此外，你还可以选取上一片段的尾帧和下一片段的首帧，通过首尾帧参考模式来生成过渡片段。这种方式相较于截图取帧模式，能够同时参考前后两个画面的状态，更适合用于处理画面变化较大、人物动作衔接复杂的场景，让过渡片段在前后内容之间衔接得更加自然。
:::

::::cols
@col 50
上一片段尾帧：

![Image=193x337](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4da67c82a45844d4acdab1f1b8d714f2~tplv-goo7wpa0wc-raw.image)

@col 50
下一片段首帧：

![Image=187x337](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/79f521aae36a4617848cb21186079286~tplv-goo7wpa0wc-raw.image)
::::

### 操作步骤 {#hYnTmnK1C}

1. 在视频编辑器的时间轴中选中需要取帧的视频片段。

  在编辑器的视频轨道上，选中需要取帧的视频片段。这里我们选择**前一个片段**，也就是希望后续画面继续承接的片段。

2. 在预览页面右上角选择截图图标，并单击**取尾帧**。

  尾帧指的是该视频片段最后一刻的画面。将它作为参考，可以帮助下一个片段延续前一个片段的场景、人物状态和画面构图。

   ![Image=409x227](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/43bf08d0b9b24d4a87c06e1f18581227~tplv-goo7wpa0wc-raw.image)
3. 查看生成的画面帧素材。
    取帧成功后，截取到的画面帧会出现在左侧的**项目文件面板**中。
4. 将取帧素材拖到下一个片段中。
    把刚刚生成的画面帧素材拖动到下一个片段上，作为该片段生成时的参考。拖动完成后，可以在右侧的片段编辑面板中看到已引用的画面帧。
   ![Image=392x218](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d74adb04c4054e1b93c094bf0de86b48~tplv-goo7wpa0wc-raw.image)
5. 输入生成提示并生成视频。
    点击引用区域，在此片段的提示词之前添加一句简短的提示词，例如：
   ```Plain Text
   [图片3]延续这一场景。
   ```
    然后点击**生成视频**。系统会基于上一片段的尾帧来生成新的片段，从而让前后画面和故事更加连续。
   ![Image=380x213](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/97f980081add4ee9b75010254eb1263c~tplv-goo7wpa0wc-raw.image)   


## 字幕擦除：去除 AI 生成的字幕 {#hB8iFnFFA}

### 适用场景 {#hDs6yGZfq}

AI 视频生成过程中，有时画面里会出现不需要的内容，例如：

* 误生成的字幕
* 乱码文字
* 多余标识
* 文字覆盖在人脸或主体画面上。

如果直接重新生成，不仅需要重新等待，还可能消耗额外积分。此时可以使用**字幕擦除**功能，对视频中的文字内容进行处理。

::::cols
@col 49
正常视频片段：

![Image=281x500](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/86162e2738324c119092f5b90a21d96c~tplv-goo7wpa0wc-raw.image)

@col 49
字幕遮挡视频主体：

![Image=284x498](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/dacf75953f494c43b2c00183aa3baacf~tplv-goo7wpa0wc-raw.image)
::::

:::tip
如果视频整体效果已经不错，只是局部出现了多余文字，优先尝试**字幕擦除**会更高效。这样可以避免因为一个小瑕疵反复重新生成整段视频。
:::

### 操作步骤 {#hVI0tkloQ}

1. 在视频编辑器的时间轴中选中需要处理的视频片段。
   在编辑器的视频轨道上选中需要去除字幕的视频片段。例如，当字幕叠加在人脸上、影响观看效果时，就可以使用该功能处理。
   ![Image=360x276](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1ec08b7fefc9410bab69ba2a08de43ca~tplv-goo7wpa0wc-raw.image)
2. 在预览页面右上角选择字幕图标，并单击**一键擦除**。
   点击**一键擦除**后，即可提交字幕擦除任务。接下来只需要等待处理完成，系统会生成擦除后的完整视频片段。
   ![Image=365x280](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c918d6b2833245b7b6ffeb6403c1ad85~tplv-goo7wpa0wc-raw.image)   


## 画质优化：提升视频清晰度 {#hAXMn5wXb}

### 适用场景 {#hJVuYExF6}

当视频准备正式发布时，画质会变得非常重要。尤其是在以下场景中，建议使用画质优化功能：

* 商业项目
* 广告投放
* 产品宣传片
* 大屏播放
* 其他对清晰度要求较高的视频内容

扣子视频编辑器内置了画质优化能力，支持将视频片段提升到更高清的规格，最高可支持 4K 画质。

### 操作步骤 {#hi9hivMEC}

1. 在编辑器的视频轨道上选中需要提升画质的视频片段。
   ![Image=369x272](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/39272295ed154a09846b1dce1c968848~tplv-goo7wpa0wc-raw.image)
2. 在预览页面右上角选择 **HD** 图标，选择画质。
    根据实际使用场景选择需要提升到的画质规格。可选项包括：
      * 1080P
      * 2K
      * 4K
     如果只是用于普通线上发布，通常可以先选择 1080P；如果用于广告投放、大屏展示等场景，可以根据需求选择更高画质。
3. 单击**一键超清**，提交优化任务，开始优化视频内容。
   ![Image=360x266](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/54edcd3d322f484d8a4b51d2ccdeb99e~tplv-goo7wpa0wc-raw.image)   


完成画质优化后，你可以回到时间轴继续预览整体效果，并根据发布场景导出对应规格的视频，让作品以更清晰、更完整的状态进入发布流程。


