> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

低代码工作流支持通过可视化的方式，对插件、大语言模型、代码块等功能进行组合，从而实现复杂、稳定的业务流程编排，例如旅行规划、报告分析等。当目标任务场景包含较多的步骤，且对输出结果的准确性、格式有严格要求时，适合配置工作流来实现。

关于低代码工作流的详细介绍，请参考[低代码工作流介绍](/guides/workflow)。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 添加低代码工作流 {#dbac4c01}

为低代码智能体添加低代码工作流，并在提示词中引用工作流的名称来调用工作流，智能体会按照工作流编排的流程来响应用户需求。工作流开始节点通常设置了输入参数，用户和智能体对话时的用户提示词（Query）中必须包含开始节点的必选参数，否则工作流可能不会按预期执行。

用户通过与智能体的对话输入指令或问题，智能体首先会解析这些输入内容。例如，用户在对话框中输入“查询北京的天气”，智能体会将这段文本解析为工作流的输入参数，作为工作流的初始输入传递到开始节点。工作流的开始节点会根据预设的逻辑，将数据传递到后续节点。

### 前提条件 {#8400cdbe}

在工作空间资源库中，已经创建了工作流，且工作流的状态为已发布，详情请参见[步骤一：创建工作流](/guides/use_workflow#48a39ed2)。

### 操作步骤 {#0e5c427f}

参考以下操作，为智能体添加资源库中的工作流：

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**创建** > **创建智能体**。
3. 根据页面提示，创建一个新智能体。
4. 在智能体编排页面的**工作流**区域，单击右侧的加号图标。
5. 在**添加工作流**对话框，选择目标工作流。
   ![Image=1420x397](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c54ded8d7e774598b129a8cb8f43a5f9~tplv-goo7wpa0wc-topic.webp)
7. 在智能体的**人设与回复逻辑**区域，引用工作流的名称来调用工作流。
   ![Image=1567x372](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8b272a1d73174175821070fde1a5a3ef~tplv-goo7wpa0wc-topic.webp)   


## 设置异步运行 {#ce12c336}

:::notice 注意
功能升级中，暂不支持新建的智能体设置异步运行。
:::

工作流默认为同步运行，即智能体必须在工作流运行完毕后才会将工作流的输出传递给智能体用户。如果工作流复杂，或包含一些运行耗时长的节点，可能会导致工作流整体运行耗时长、智能体判断工作流运行超时，并在其运行完毕前就结束对话。例如包含图像流节点、多个大模型节点，或编排逻辑复杂的工作流节点。

:::tip 说明
* 如果工作流或节点运行超时，智能体可能无法提供符合预期的回复。各场景的超时时间说明如下：
   * 未开启工作流异步运行：
      * 工作流整体超时时间为 **10** 分钟，数据库等部分节点的超时时间为 1分钟，具体请参见[低代码工作流使用限制](/guides/workflow_limits)。
      * 用户问题和智能体回复的时间间隔最长为 2 分钟，如果智能体回复耗时 2 分钟以上，智能体可能会判断工作流超时。如果工作流运行耗时大于 2 分钟，建议添加输出节点用于输出中间消息，或者结束节点开启流式输出，保持对话状态。
   * 开启工作流异步运行后：工作流整体超时时间为 24 小时，模型节点等部分节点为 10 分钟，数据库节点等部分节点为 1 分钟，具体请参见[低代码工作流使用限制](/guides/workflow_limits)。
* 工作流异步运行，仅在调试智能体或与商店中的智能体对话时生效，飞书、豆包等渠道暂不支持工作流异步运行。
* 工作流开启异步运行后，模型节点无法查看智能体对话历史。
:::

在这种场景下，你可以设置工作流为异步运行，设置后，智能体对话不依赖工作流的运行结果。工作流异步运行时会默认返回一条预设的回复内容，用户可以继续与智能体对话，工作流运行完毕后智能体会针对触发工作流的指令做出最终回复。

### 操作步骤 {#ab683fa2}

参考以下操作，为工作流开启异步运行：

1. 在指定工作流右侧单击**设置**。
   ![Image=398x90](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/71bcdd8074b04433b755510f64b41749~tplv-goo7wpa0wc-topic.webp)
2. 开启**异步运行**，并设置**回复内容**。
   回复内容是工作流在异步运行时，智能体回复用户的默认文案。
   ![Image=398x129](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/375d31be323948f4b5848e77fca9cdf7~tplv-goo7wpa0wc-topic.webp)   


异步运行效果：

![Image=424x309](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bf8d2e39320f4aaa8bd1a68c35f6a121~tplv-goo7wpa0wc-topic.webp)

## 绑定卡片数据 {#5e7b06b8}

添加到智能体的工作流支持绑定消息卡片。绑定成功后，智能体以消息卡片的形式发送消息。

:::notice 注意
目前，消息卡片仅在豆包客户端、飞书客户端内生效。
:::

### 操作步骤 {#202df19b}

参考以下操作，为智能体中的工作流绑定消息卡片：

1. 在指定工作流右侧，单击**绑定卡片数据**图标，并单击**绑定卡片**。
   ![Image=664x150](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d26e526b16614d31b416705577b59820~tplv-goo7wpa0wc-topic.webp)
2. 在智能体**回复卡片配置**对话框，选择扣子提供的**官方卡片**，或创建自定义卡片。
   ![Image=622x324](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/59ac7083816a4b23b78acc8d1062476e~tplv-goo7wpa0wc-topic.webp)
3. 配置消息卡片后，卡片图标将会显示绿点。
   ![Image=449x122](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/839a26448b2746fab953ccf4975c2ae3~tplv-goo7wpa0wc-topic.webp)
4. 发布智能体，使配置生效。

## 移除低代码工作流 {#1760dc12}

你可以为智能体移除一个不需要的工作流。移除后，智能体将不会按照该工作流编排的流程执行任务。

在指定工作流右侧，单击**移除**图标，即可移除添加到智能体中的工作流。

![Image=379x232](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a307ec819e8148489b5a01b11ef065cf~tplv-goo7wpa0wc-topic.webp)
