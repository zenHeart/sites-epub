> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

低代码工作流中的查看会话列表节点用于查看当前用户的会话列表。

## 节点说明 {#58374453}

增删改查是会话管理类节点的常见操作，创建会话之后可以通过查看会话列表节点查看当前终端用户的所有会话，包括静态会话和动态会话。通过此节点可查看会话的名称及 ID。

会话类、消息类节点往往需要指定会话名称，你也可以通过查看会话列表节点快速筛选出要操作的会话名称。

:::tip 说明
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制​**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
* 会话类节点只能在应用中使用。低代码智能体暂不支持会话管理类节点，即创建会话、修改会话、删除会话、查看会话列表节点。
:::

## 添加节点 {#bdbfd815}

在工作流画布中，单击 **+ 添加节点**，在**会话管理**区域选择**查看会话列表**节点，即可将节点添加到画布中。

![Image=701x366](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8f6ada6a145d454b8a88448fddd3e040~tplv-goo7wpa0wc-topic.webp)

## 配置节点 {#f04cb78c}

### 输入 {#ed003c83}

查看会话列表节点无需指定任何输入参数，默认查看当前用户的所有会话，包括动态会话和静态会话。

### 输出 {#d6fac0f1}

查看会话列表节点的输出参数固定为 conversationList，即会话列表，其中包含：

* conversationName：会话的名称。
* conversationId：会话的 ID。

## 试运行节点 {#182693a0}

对于资源库中的工作流或对话流，试运行查看会话列表节点时，需要关联应用，表示查看指定应用的会话。试运行工作流节点时，操作的是草稿态的数据，也就是应用中存储的临时会话。线上执行工作流时，操作的是线上数据。

![Image=384x327](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4e353e6a386e4d2a9992e8823b988c90~tplv-goo7wpa0wc-topic.webp)

试运行成功后，可以在节点卡片中单击**查看数据**，在应用的**会话管理**页面中可见会话列表和试运行的结果完全一致。

![Image=662x325](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d4587187102449af929f23359e2e1d93~tplv-goo7wpa0wc-topic.webp)
