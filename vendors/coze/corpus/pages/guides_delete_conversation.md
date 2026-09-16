> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

低代码工作流中的删除会话节点用于删除通过创建会话节点创建的会话。

## 节点说明 {#58374453}

增删改查是会话管理类节点的常见操作，每个用户的会话上限为 200 个。超过 200 个后，建议先通过删除会话节点删除历史会话，否则直接创建会话会报错。

删除会话节点每次执行时，删除一个指定名称的会话，同时删除会话中的所有消息。会话及消息删除后不可恢复。

:::tip 说明
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制​**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
* 会话类节点只能在应用中使用。低代码智能体暂不支持会话管理类节点，即创建会话、修改会话、删除会话、查询会话列表节点。
:::

## 添加节点 {#a9a079ad}

在工作流画布中，单击 **+ 添加节点**，在**会话管理**区域选择**删除会话**节点，即可将节点添加到画布中。

![Image=636x335](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/724d6d56aaf94664bd1aa3f69768f5e4~tplv-goo7wpa0wc-topic.webp)

## 配置节点 {#f04cb78c}

### 输入 {#ed003c83}

删除会话节点的输入参数固定为 conversationName，必选，String 类型，表示待删除的会话名称。会话名称参数可以指定为一个固定值、引用上游节点的输出参数或者引用变量。

### 输出 {#d6fac0f1}

删除会话节点的输出参数用于展示节点的执行结果。参数固定为 isSuccess，Boolean 类型，表示删除会话节点是否执行成功。

![Image=324x269](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0bbecd4d65f74c25ab9d807a4fa50de9~tplv-goo7wpa0wc-topic.webp)

## 试运行节点 {#60ff149b}

对于资源库中的工作流或对话流，试运行删除会话节点时，需要关联应用，表示在指定的应用中删除会话。试运行工作流节点时，操作的是草稿态的数据，也就是应用中存储的临时会话。线上执行工作流时，操作的是线上数据。

![Image=400x356](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/952097e0da0d4dd8bae6d5c46870b615~tplv-goo7wpa0wc-topic.webp)

试运行成功后，可以在节点卡片中单击**查看数据**，在应用的**会话管理**页面中可见指定的临时会话已被成功删除。

![Image=662x325](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d4587187102449af929f23359e2e1d93~tplv-goo7wpa0wc-topic.webp)
