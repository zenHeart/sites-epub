> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子知识库提供了高效便捷的方式来存储和管理外部数据（包括文本、表格及图片），使低代码智能体可以与指定数据进行交互，提升回复内容的准确性和可用性。本文介绍如何上传本地图片到知识库。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 注意事项 {#26b51646}

创建知识库前，请先阅读[知识库概述](/guides/knowledge)、[使用限制](/guides/knowledge_limits)了解其功能特性及使用限制。

## 操作流程 {#25d5ac5c}

参考以下操作，上传图片到知识库。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 在页面右上角，选择 **+资源** > **知识库**。
   ![Image=482x154](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4f8f1dcf6d244a16a838bc470c2c60e6~tplv-goo7wpa0wc-topic.webp)
4. 在图片知识库中添加图片。
   1. 选择导入类型。
      ![Image=262x239](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0981e477fc4f46058c298ff3d6bade91~tplv-goo7wpa0wc-topic.webp)
   2. 上传图片。
   3. 设置标注方式。
      ![Image=2090x271](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d683799f66d74ffc8663147510c10a88~tplv-goo7wpa0wc-topic.webp)
5. 等待服务器根据你所配置的标注方式对图片进行处理后，可查看上传的图片。

## 配置说明 {#e8757029}

扣子编程支持用户将本地图片导入到知识库，配置说明如下：

<!-- @cols-width: 159,525 -->
| **操作**  | **说明**  |
| --- | --- |
| 上传配置  | 在**上传图片**页面，单击上传或拖拽图片到上传区域。  |
| 标注设置  | 标注是为了让系统能够更准确地检索和召回相关的图片数据。如果不进行图片标注，尤其是对于包含表格数据的图片，系统将无法理解图片中的数据结构和内容，导致无法有效地建立索引。目前支持两种标注方式： | \
| | | \
| | * 智能标注：系统会深度理解图片内容，自动提供详细的内容描述信息。 | \
| | * 人工标注：根据图片内容，手动添加图片描述信息。 | \
| |    如果选择**人工标注**，则需等待服务器处理完成后，单击图片手动添加标注信息。  |

## 相关操作 {#0f67ddf0}

创建知识库后，你可以在智能体或工作流中使用知识库。同时，你还可以依据业务发展的实际需求，对知识库进行更新、删除、停用、启用等操作。相关操作说明如下：

* [使用知识库](/guides/use_knowledge)：在智能体或工作流中添加知识库，丰富 AI 应用的知识范围，提高模型回复内容的可靠性。
* [维护知识库](/guides/maintain_knowledge)：根据业务变化，你可以对知识库进行停用、启用、编辑、删除等操作。
