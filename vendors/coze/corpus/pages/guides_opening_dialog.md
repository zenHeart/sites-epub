> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

开场白是用户进入低代码智能体后自动展示的引导信息。它的主要目的是帮助用户理解智能体的用途，以及如何与其进行交互。

:::tip 说明
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
* 开场白功能支持如下平台：
   * 豆包、微信公众号（服务号）、微信订阅号、微信小程序、抖音小程序、飞书、Chat SDK 和 API（可通过[查看智能体配置](/developer_guides/get_metadata_draft_published) API 查看）。
   * 微信小程序和抖音小程序：仅支持展示全部预置问题，不支持展示部分预置问题。
   * 微信公众号（服务号）和微信订阅号：不支持预置问题。
:::

常见的开场白效果如下：

![Image=435x393](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/32cf8ea77dde4e77b1fca6817a122983~tplv-goo7wpa0wc-topic.webp)

## 设置开场白 {#59659940}

在智能体编排页面的**开场白**区域，可以设置**开场白文案**和**开场白预置问题**。

### 开场白文案 {#9083812f}

**开场白文案**用于帮助用户快速理解智能体的能力。用户进入智能体后，智能体会默认发送这段预先设置的开场白文案。**开场白文案**为 Markdown 格式，你可以在 Markdown 编辑器中设计智能体的开场白，调试区域会同步展示开场白的预览效果。你也可以通过 AI 自动生成开场白。

通过 Markdown 编辑器，你可以调整开场白文案样式，例如设置层级、加粗、斜体、删除线等样式效果。也可以添加链接、图片、代码块和 {{user_name}} 变量。其中，{{user_name}} 会自动引用扣子用户的昵称。

![Image=1119x466](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/18e6eaf0d7ef4881b2a26fe865f65aee~tplv-goo7wpa0wc-topic.webp)

### 开场白预置问题 {#145ee1e9}

首次使用智能体的用户往往需要一些对话示例体验智能体的能力和效果，你可以为智能体设置**开场白预置问题**，提供一些推荐问题。这些推荐问题会展示在开场白文案之下，用户单击问题即可发起一次对话，帮助用户快速体验智能体。如果设置了多个开场白问题，则默认随机显示 3 条预置问题。你也可以开启全部展示，开启后，开场白会默认按顺序显示所有预置问题。

![Image=1144x525](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7f196cb979a34287b5f54665493b2cf3~tplv-goo7wpa0wc-topic.webp)

## 示例 {#eecec1a1}

以[雅思口语专家](https://www.coze.cn/store/bot/7389299390185209892?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)智能体为例，同时设置开场白文案和预置问题。

开场白配置示例：

![Image=1150x471](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/203482faf2b24d1ebb60f1d45690b62f~tplv-goo7wpa0wc-topic.webp)

展示效果：

![Image=399x425](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/08a28cc5cc4747c2a9c45ae1c2e77b9c~tplv-goo7wpa0wc-topic.webp)
