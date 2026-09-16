> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

会话指的是用户与模型之间基于同一主题的一系列连续的对话交互，会话中存储用户输入的消息和模型回复的消息。创建会话节点用于在低代码工作流或对话流中创建一个空的会话。

## 节点说明 {#58374453}

会话用于存储用户和模型的会话消息。每个对话流都需要绑定一个会话作为开始节点的默认会话，执行对话流时产生的消息都会自动写入到这个会话中。创建会话节点用于在低代码工作流或对话流中生成一个新的会话，新会话中默认没有任何消息记录，它被绑定对话流并运行一次后才会有消息接入。

在一些需要在运行过程中创建会话的场景，可以通过会话节点创建会话，再将新会话作为对话流的入参，运行对话流、写入消息。

:::tip 说明
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制​**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
* 会话类节点只能在应用中使用。低代码智能体暂不支持会话管理类节点，即创建会话、修改会话、删除会话、查询会话列表节点。
* 创建会话节点创建出的是动态会话，试运行时会展示在应用会话列表的动态会话区域，是应用的草稿态临时数据，与线上数据隔离。
:::

## 配置创建会话节点 {#f04cb78c}

### 输入 {#ed003c83}

创建会话节点的输入参数固定为 conversationName，必选，String 类型，表示新会话的名称。同一个应用中会话名称必须唯一。会话名称参数可以指定为一个固定值，或引用上游节点的输出参数。

### 输出 {#d6fac0f1}

创建会话节点的输出参数用于展示创建会话节点的执行结果。参数固定为：

* isSuccess：Boolean 类型，表示创建会话节点是否执行成功。
* isExisted：Boolean 类型，表示应用中是否已存在此名称的会话。
* conversationId：新会话的 ID。

输出示例如下：

* 应用中没有同名的会话，创建新会话成功，返回会话 ID：
   ```Markdown
   conversationId : 7444890359211262037
   isSuccess : true
   isExisted : false
   ```
* 应用中已有同名的会话，所以未创建会话，此时返回原会话的 ID：
   ```Markdown
   conversationId : 7444890359211262004
   isSuccess : true
   isExisted : true
   ```   


## 试运行创建会话节点 {#60761d31}

对于资源库中的工作流或对话流，试运行创建会话节点时，需要关联应用，表示在指定的应用中创建会话。

![Image=565x361](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b63e4b5618a04d0089db04eb482161aa~tplv-goo7wpa0wc-topic.webp)
