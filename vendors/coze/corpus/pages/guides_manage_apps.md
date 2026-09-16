> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

在扣子编程中创建低代码应用之后，可以管理空间中的低代码应用，例如同空间复制低代码应用、跨空间复制低代码应用、删除自己创建的低代码应用。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 查看引用资源 {#224dade2}

你可以通过资源引用页面，快速查看低代码应用中已添加的工作流、插件、数据库等资源，帮助你理解低代码应用中各项资源的引用关系，以便更高效地管理资源、定位问题。

在应用业务逻辑页面左上角单击引用关系，页面将自动跳转到资源引用页面。

![Image=373x205](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2598a3c303164f09bf417a1543d54f35~tplv-goo7wpa0wc-topic.webp)

资源引用页面展示低代码应用中每个工作流引用的子工作流、插件、数据库、知识库等资源，箭头从 A 指向 B 表示 A 引用了 B。例如在下图中，gen_zhuzhu_image 工作流直接引用了 test 知识库、头条搜索插件和 search 工作流。你还可以单击资源卡片，在新标签页中查看资源详情。

![Image=1356x441](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b082636311584a4d8d9ff4972e9356d5~tplv-goo7wpa0wc-topic.webp)

## 复制应用 {#d50cdc8d}

工作空间中的所有成员都可以浏览空间下的应用，并复制自己感兴趣的应用，再将其改造为更适合自己业务场景的应用。复制出的应用和原应用配置完全一致，应用中已创建的工作流、插件、变量、知识库等资源也完全一致。

<!-- @cols-width: 203,642 -->
| **个人空间应用限制**  | 个人空间中的应用不支持复制到工作空间。  |
| --- | --- |
| **订阅套餐差异**  | * 各个扣子编程套餐均支持同空间下复制应用。 | \
| | * 企业版（标准版、旗舰版）支持跨空间复制应用，即企业工作空间成员可以将其所在工作空间内的任意应用复制到已加入的其他工作空间中。  |
| **应用内容的复制范围**  | 复制应用时，会同步复制应用中的插件、工作流等资源。复制应用期间调整应用或资源可能导致复制失败，你可以根据页面提示进行失败重试。  |
| **应用复制后的所有权及状态**  | * 原应用中已添加的协作者会被清除。 | \
| | * 操作者将成为新应用的所有者。 | \
| | * 如果应用存在多个历史版本，仅复制最新草稿版。 | \
| | * 复制后的新应用，为草稿版状态。  |

### 同空间复制低代码应用 {#2475b475}

在[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的目标工作空间中，找到需要复制的应用，将鼠标悬浮在该应用区域内，然后在其右下角展开列表，单击**创建副本**。

![Image=462x295](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d7a1282901c2441d94dbe3c05a6e419c~tplv-goo7wpa0wc-topic.webp)

### 跨空间复制低代码应用 {#7589ff87}

在[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的目标工作空间中，找到需要复制的应用，将鼠标悬浮在该应用区域内，然后在其右下角展开列表，单击**复制到其他空间**。

![Image=315x248](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6c7ea8aabf284663bfc8caf79f2f66e6~tplv-goo7wpa0wc-topic.webp)

## 移动低代码应用到文件夹 {#243bb1c4}

扣子编程支持通过文件夹对目标工作空间下的项目和资源进行更细粒度的管理。工作空间的所有者、管理员及应用的所有者均可以移动应用到指定目标文件夹。

在[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的目标工作空间中，找到需要移动的应用，将鼠标悬浮在该应用区域内，然后在其右下角展开列表，单击**移动**。

![Image=308x242](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/524c1ac3da244101bd624de318d495ae~tplv-goo7wpa0wc-topic.webp)

## 删除低代码应用 {#56876603}

工作空间的所有者、管理员及应用的所有者均可以随时按需删除应用，删除应用时会同步删除应用中的所有工作流、插件、知识库、数据库等资源，但不会删除应用工作流中引用的资源库中的资源。

:::tip 说明
删除应用时会同步删除应用中的所有资源，且不可恢复，请谨慎操作。
:::

在[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的目标工作空间中，找到需要删除的应用，将鼠标悬浮在该应用区域内，然后在其右下角展开列表，单击**删除**。删除时，需在**项目名称**中输入应用名称进行二次确认。

![Image=326x255](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/29b973eea18d44768a027b4c1fbc45c6~tplv-goo7wpa0wc-topic.webp)
