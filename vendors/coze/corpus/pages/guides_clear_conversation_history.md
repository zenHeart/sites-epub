> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

低代码工作流中的清空会话历史节点用于清除指定会话中存储的上下文消息。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制​**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 节点说明 {#b97bf3ac}

会话中的历史消息也被称为上下文，对大模型的性能和文本生成效果有重要影响。较长的上下文可以为模型提供更多的信息参考，生成与上下文语义匹配的文本片段，使模型生成更为连贯、逻辑性更强的内容。

多轮对话中启动新话题时，过时的上下文也会同样影响模型的生成效果，例如模型可能召回一些过时的知识或记忆。此时可以使用清空会话历史节点，清除会话中已存储的上下文，成功清除后，对话流中的大模型节点会读到的对话历史为空，之后的对话不会受到之前历史消息的影响。

例如以下对话中，清空会话历史后模型的回复会更加准确：

* 用户：最近看了几个恐怖电影。
* 模型：真是非常刺激和紧张的观影体验！你看了哪些恐怖电影？
* 用户：你有什么别的好电影推荐吗？
* 模型：当然！恐怖电影《闪灵》你感兴趣吗？
* 【清空会话历史】
* 用户：你有什么别的好电影推荐吗？
* 模型：根据最新的搜索结果，这里有一些 2025 年备受期待和推荐的电影。

:::tip 说明
* 试运行清空会话历史节点时，只能清除应用中测试数据的上下文，无法清除线上数据。
* 清空会话历史只会清除模型可见的上下文，不会真正删除会话中存储的历史消息。所以清空会话历史之后，仍旧可以通过[查询消息列表节点](/guides/query_message_list)查看完整的消息内容。
:::

## 配置清空会话历史节点 {#bef23f32}

### 输入 {#88605b7f}

清空会话历史节点的输入参数固定为 conversationName，必选，String 类型，表示待清空会话历史的会话名称。会话名称参数可以指定为一个固定值，或引用上游节点的输出参数。

### 输出 {#131b39c5}

清空会话历史节点的输出参数用于展示清空会话历史节点的执行结果。参数固定为 isSuccess，Boolean 类型，表示此节点是否执行成功。

![Image=600x219](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c497a1a160f2481baea36da9333d08e5~tplv-goo7wpa0wc-topic.webp)

## 试运行清空会话历史节点 {#2f4e9c38}

对于资源库中的工作流或对话流，试运行清空会话历史节点时，需要关联智能体或应用，表示清除指定智能体或应用中的上下文。

![Image=489x412](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/aba856e1cc9443978aa4da63fc7a3d1c~tplv-goo7wpa0wc-topic.webp)

试运行成功后，可以进入此应用的**会话管理**页面，可以在指定会话的对话框中看到页面提示“清空上下文”。

![Image=524x350](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3ddca68f8c2f4e60943c820c03136d0a~tplv-goo7wpa0wc-topic.webp)
