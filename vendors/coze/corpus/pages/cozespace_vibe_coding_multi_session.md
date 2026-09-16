> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子 AI 编程项目支持创建多个会话，让你可以在同一个项目中并发处理多项独立的开发任务。

## 什么时候使用多会话 {#42750e80}

当你需要在同一个项目中同时处理多个独立任务，或者需要一个空白的上下文时，可以使用多会话功能。例如：

* 在一个会话里让编程 Agent 开发新功能。
* 在另一个会话里让编程 Agent 修复 Bug。

## 核心特性 {#5bbb6bb5}

多会话的核心特性是“文件共享，上下文隔离”：

* **文件共享**：所有会话都作用于同一个项目。因此，在任何一个会话中修改项目文件，都会实时反映在其他会话中。
   如果多个会话任务同时修改同一个代码文件，可能会产生冲突。为确保代码稳定，编程 Agent 在开发过程中会实时同步文件变更，并在检测到代码存在逻辑问题或运行异常时，自动进行修复。
* **上下文隔离**：每个会话都拥有独立的会话上下文。编程 Agent 在某个会话中的交互，不会受到其他会话内容的影响。

此外，当你新建会话时，编程 Agent 会自动加载项目中最新的代码，并在此基础上继续开发。

## 使用限制 {#39279a5b}

一个 AI 编程项目中，最多可创建 100 个会话。

## 前提条件 {#9102b85f}

已创建一个编程项目并完成基础开发。具体操作，请参考[开发流程](/cozespace/5uu7ba6t#fa6b267b)。

## 新建会话 {#28c2ffd1}

你可以通过如下三种方式新建会话。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

### 全新会话 {#0b3b11fb}

创建一个完全独立的会话，新会话不会继承任何历史对话上下文。

1. 在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的会话列表中，单击目标 AI 编程项目。
2. 在左侧导航栏中，单击**新建对话**。
   ![Image=504x325](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2160a002dade4b5eae663f7edb5fa95d~tplv-goo7wpa0wc-topic.webp)   


### 复制会话 {#d9520f8b}

复制一个现有的会话，新会话会继承原会话的全部上下文。

1. 在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的会话列表中，单击目标 AI 编程项目。
2. 在会话列表中，单击目标会话对应的 **···** > **复制**，复制一个新的会话。
   ![Image=362x296](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ad83ebb9a44d4f3e8e50052399edd390~tplv-goo7wpa0wc-topic.webp)   


### 复制对话到新会话 {#c624a0f5}

基于某个会话中的某一条对话新建，新会话会继承该条对话之前的所有上下文。

1. 在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的会话列表中，单击目标 AI 编程项目。
2. 在目标会话中，单击某条对话中的**复制上下文到新**会话。
   系统会新建一个会话，并将整条对话内容复制到新会话中。
   ![Image=271x241](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/785f65c70736426ba42b82b8ba128879~tplv-goo7wpa0wc-topic.webp)   


## 在新会话中开发 {#bc4c9b77}

创建多个独立会话，同时开发不同的任务。

* **并行开发多个模块**：在一个会话中开发支付模块，同时在另一个会话中开发用户功能模块。
* **开发与修复同步进行**：在一个会话中修复 Bug，同时在另一个会话中调整 UI 风格。
* **基于空白上下文继续开发**：当会话中积累了过多的对话或报错历史，导致大模型响应变慢时，你可以新建一个会话。新对话将提供一个**空白上下文**，更专注于新任务的开发。

下文将通过一个具体示例，演示如何在一个会话中修复 Bug，同时在另一个新会话中修改 UI 风格，从而实现两个开发任务的并行处理。

1. 在**默认会话**中，修复 Bug。
   例如，输入指令：
   ```Plain Text
   单击生成卡片没有反应
   ```
   ![Image=391x441](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/52334badad3f4449b9c53981da630f69~tplv-goo7wpa0wc-topic.webp)
2. 在**新会话**中调整 UI 风格。
   例如，输入指令：
   ```Plain Text
   将 UI 配色改成浅色系
   ```
   ![Image=405x461](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6433368b3a01417aa34a8b23cbc17b09~tplv-goo7wpa0wc-topic.webp)
3. 预览开发结果。
   所有会话共用一份项目代码和同一个预览环境。你可以在任意一个会话中，预览开发结果。
   ![Image=550x314](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2d0a3a1e80764f53acd9c7da1c36b60d~tplv-goo7wpa0wc-topic.webp)   


## 相关操作 {#829bce4b}

创建会话后，你还可以重命名、关闭、置顶会话等操作。

![Image=288x235](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8deaf818dc3e4038ac987252d422d60c~tplv-goo7wpa0wc-topic.webp)

<!-- @cols-width: 222,603 -->
| | | \
|**操作** |**说明** |
|---|---|
|重命名会话 |在会话列表中，双击目标会话名称，或者单击目标会话对应的 **···** > **重命名**，重新设置会话名称。 |
|关闭会话 |在会话列表中，单击目标会话对应的 **···** > **关闭**，关闭会话。 |\
| | |\
| |:::tip 说明 |\
| |* 如果会话中有任务正在进行，则暂时无法关闭该会话。如需关闭，请先手动停止正在进行的任务。 |\
| |* 关闭会话后，该会话中的记录将被清除，未合并的代码改动将丢失。该操作不可撤销，请谨慎操作。 |\
| |::: |\
| | |\
| | |
|置顶会话 |在会话列表中，单击目标会话对应的 **···** > **置顶**，将该会话固定在会话列表顶部。 |

## 常见问题 {#5d42ce62}

* [多会话的任务是并发进行的吗？](/guides/vibe_coding_faq#b62c2c74)
* [多会话模式下，同时发送需求会冲突吗？](/guides/vibe_coding_faq#494718ea)
* [多会话模式下，新会话是基于一个全新的空项目吗？](/guides/vibe_coding_faq#5ceca401)
* [多会话模式下，我可以在不同的会话中预览不同的开发效果吗？](/guides/vibe_coding_faq#9785de24)
