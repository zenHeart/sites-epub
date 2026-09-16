> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

开发者可以在低代码智能体编排页面设置是否允许用户在扣子商店通过语音或视频与智能体实时沟通，并可设置音色和默认输入方式。

## 功能说明 {#bc435719}

在智能客服、智能穿戴、语音陪伴等音视频场景中，为智能体开启音视频通话功能并合理设置音色，可显著提升其交互的丰富性和生动性，使沟通更加直观、高效。同时，合适的音色能赋予智能体更具亲和力、专业性或个性化的语音表达，从而增强用户对智能体的好感度和信任感，更好地满足用户在不同场景下的多样化需求，进一步优化用户与智能体之间的交互体验。

开启了语音通话和视频通话的智能体，发布至扣子商店等渠道后，将支持用户通过语音、视频、或共享屏幕的方式与其交互，用户可体验到如图所示的音视频通话效果。

::::cols
@col 33
语音通话

![Image=400x358](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4733db1f1d8e40d5a710fcd4883125a7~tplv-goo7wpa0wc-topic.webp)

@col 33
视频通话

![Image=400x367](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7b22eb9e14214975a0fda03a73ba33d8~tplv-goo7wpa0wc-topic.webp)

@col 33
共享屏幕

![Image=400x365](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b90cf48e66604c458e57bbaf600a2f77~tplv-goo7wpa0wc-topic.webp)
::::

:::tip 说明
* 在团队版和企业版中，企业超级管理员可以通过***功能访问控制​***和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
* 在低代码智能体编排页面开启语音通话或视频通话后，支持在如下渠道使用：
   * 在扣子商店体验音视频通话。
   * 在豆包体验语音通话。
   * 将智能体发布 API 后，你可以在自己的产品中通过 WebSocket 或 RTC 方式实现音视频通话，具体请参见[智能音视频概述](/dev_how_to_guides/realtime_overview)。
   * 将智能体发布 Chat SDK 后，你可以在自己的产品中安装 Chat SDK 实现语音通话（暂不支持视频通话），具体请参见[安装并使用 Chat SDK](/developer_guides/install_web_sdk)。
:::

## 为智能体开启音视频通话 {#641c2bf7}

1. 在智能体编排页面的**对话体验** > **音视频**区域，选择智能体对应的音色，你可以使用扣子编程系统预置的音色或资源库中复刻的音色。
   扣子编程的系统预设音色支持多情感音色，即一个音色可以表达多种情感，例如开心、悲伤等。你可以指定其中一种情感并设置其情绪强烈程度，让智能体在通话时用对应的情感语气说话（不会针对每句话进行动态调整情感）。带有**多情感**标签的音色支持此功能。
   :::notice 注意
   试听多情感音色时，扣子编程将按照文字转语音的字符数收费，费用详细说明请参见[音视频费用](/coze_pro/asr_tts_fee)。
   :::
   ![Image=400x494](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/46e1d1f083384b448f8f19325328bdbd~tplv-goo7wpa0wc-topic.webp)
   <!-- @cols-width: 138,697 -->
   | **参数**  | **说明**  |
   | --- | --- |
   | 情感  | 情感参数用于指定智能体音色的情感类型，例如开心、悲伤等。你可以从下拉列表中选择该音色对应的情感。不同音色支持的情感范围不同。  |
   | 情感值  | 情感值用于量化情感的强度。数值越高，情感表达越强烈，例如： “开心” 的情绪值 5 比 1 更显兴奋。 | \
   | | | \
   | | 取值范围：1.0~5.0，默认值：4.0。  |
2. 开启或关闭语音通话或视频通话右侧的开关。开启后，用户在扣子商店中打开对应的智能体，可以通过语音通话、视频通话或屏幕共享的方式与智能体实时沟通。
   :::tip 说明
   开启视频通话时，智能体或工作流需要选择支持**图片理解**的模型，例如**豆包·视觉理解·Pro** 模型。
   :::
   ::::cols
   @col 50
   设置入口
   
   ![Image=350x472](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/061f9c8e961a4eac86d0fae4d990109b~tplv-goo7wpa0wc-topic.webp)
   
   @col 50
   设置后的效果
   
   ![Image=400x367](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5fbc1237eeed444bbbc30a9aec1e5138~tplv-goo7wpa0wc-topic.webp)
   ::::
3. 在视频通话过程中，扣子编程通过视频抽帧技术，将摄像头画面或共享屏幕转化为图像帧，供大模型分析理解。为保障大模型精准识别用户行为和意图，你需要设置视频抽帧的参数，参数说明如下。
   <!-- @cols-width: 148,580 -->
   | **参数**  | **说明**  |
   | --- | --- |
   | 每秒抽帧数  | 在视频通话过程中，摄像头或屏幕共享捕捉画面的频率。捕捉到的画面会作为视觉模型的输入，帮助智能体理解用户的动作和行为。抽帧数越高，智能体能够获取的画面信息越丰富，从而更准确地理解用户的意图和行为，但会增加 Token 消耗。 | \
   | | | \
   | | 默认值为 `1`，取值范围为 `[1, 24]`。  |
   | 开始说话前抽取秒数  | 在用户开始说话之前，抽取指定秒数的画面，能够帮助智能体提前了解用户在说话前的动作状态，从而更全面地理解用户的意图与行为。 | \
   | | | \
   | | 单位为秒，默认值为 `1`，取值范围为 `[1, 10]`。  |
4. （可选）设置默认的用户输入方式。
   开启语音通话或视频通话后，你可以选择默认的输入方式为语音通话或视频通话。设置后，当用户打开智能体时，默认进入语音通话页面或视频通话页面。
   ::::cols
   @col 50
   设置入口
   
   ![Image=350x543](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a25c76fb10184a15aece84a6b44727f6~tplv-goo7wpa0wc-topic.webp)
   
   @col 50
   设置后的效果
   
   ![Image=350x293](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e7a87d0e7d7648b9ab85ca8f9316bcf8~tplv-goo7wpa0wc-topic.webp)
   ::::
5. 配置完成后，你可以在调试区体验通过语音通话、视频通话或共享屏幕的方式，与智能体进行实时交流。
   ![Image=400x396](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/db0097a645d54cdba958e71dec86170f~tplv-goo7wpa0wc-topic.webp)   


## 在扣子商店体验音视频通话 {#2316cb2e}

开启了语音通话或视频通话的智能体，发布扣子商店后，如果默认输入方式是打字输入或语音输入，你可以在智能体右上角单击通话按钮，选择语音通话、视频通话或屏幕共享。如果默认输入方式为语音通话或视频通话，打开智能体并接听后，即可通过语音或视频方式与智能体交互。

::::cols
@col 33
![Image=400x367](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5fbc1237eeed444bbbc30a9aec1e5138~tplv-goo7wpa0wc-topic.webp)

@col 33
![Image=400x358](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4733db1f1d8e40d5a710fcd4883125a7~tplv-goo7wpa0wc-topic.webp)

@col 33
![Image=400x367](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7b22eb9e14214975a0fda03a73ba33d8~tplv-goo7wpa0wc-topic.webp)
::::
