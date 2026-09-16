> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程支持为低代码智能体设置对话流模式，在该模式下，低代码智能体用户的所有对话均会触发固定的对话流处理。对话流模式适用于智能体技能流程相对固定的场景，例如售后服务场景下指定某个对话流处理咨询问题、长文生成场景下根据用户的每个 query分段生成内容。

## 对话流模式介绍 {#bbe208cd}

通常情况下，我们通过人设与回复逻辑来指定智能体在不同场景下的不同技能，例如约束智能体使用指定插件回复某类问题，但用户 Query 复杂的情况下，智能体不一定会根据设计的逻辑进行处理，导致智能体回复不符合预期。

此时你可以将智能体设置为对话流模式。在该模式下无需设置人设与回复逻辑，智能体有且只有一个对话流，智能体用户的所有对话均会触发此对话流处理。智能体通过开始节点的 USER_INPUT 传入问题，并以结束节点作为智能体的回复。

对话流适用于 Chatbot 等需要在响应对话请求时进行复杂逻辑处理的对话式应用程序，例如智能客服、虚拟伴侣等。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 限制说明 {#8bee9eff}

* 对话流模式的低代码智能体只能绑定一个对话流。
* 对话流模式的低代码智能体不支持添加技能、知识等配置，但你可以将某些技能和知识配置在智能体的对话流中，例如对话流中添加知识库处理节点。

## 创建对话流模式智能体 {#00f05b3b}

### 1 创建智能体并设置对话流模式 {#76a19e46}

默认情况下，智能体使用单 Agent （自主规划模式）。你需要先按照以下步骤切换到单 Agent （对话流模式）。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
1. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**创建** > **创建智能体**。
2. 根据页面提示，创建一个新智能体。
3. 在智能体的**编排**页面，选择智能体模式为**单 Agent （对话流）模式**。
   ![Image=376x226](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/51fe3916f150469586bc48086f58f9fe~tplv-goo7wpa0wc-topic.webp)   


### 2 添加对话流 {#d12f07a0}

对话流模式下，智能体用户的对话会触发指定的对话流处理。对话流模式的智能体只能绑定一个对话流。

1. 在**对话流配置**区域，单击**点击添加对话流**。
2. 单击**创建工作流->创建对话流**，并设置对话流名称和描述。
   ![Image=280x277](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8fd59710a2984b1fb7e30154fb9be0df~tplv-goo7wpa0wc-topic.webp)   


你也可以根据页面提示添加资源库中已发布的对话流。

3. 配置开始节点。
   对话流模式下绑定的对话流开始节点，除了默认的`USER_INPUT`、`CONVERSATION_NAME`以外，还可以添加自定义变量。
   * `USER_INPUT` 变量用于传入用户当前输入的内容。例如用户咨询“产品目前的收费策略是什么？”，这句话会封装在 `USER_INPUT` 变量中透传给后续的节点处理。
   * `CONVERSATION_NAME` 变量表示对话流绑定的会话名称。
   * 自定义变量用于在智能体交互中存储和管理每个用户的特定信息，例如用户ID、地理位置等，以便实现个性化处理和差异化响应。你可以在对话流中配置自定义变量，当用户与智能体对话时可以动态更新和读取变量值。
   :::tip 说明
   * 设置了自定义用户变量的智能体只能发布 API 或 Chat SDK。
   * 在对话流开始节点设置了自定义用户变量的智能体，在扣子编程调试界面进行对话时会提示平台错误，建议发布 API 或 Chat SDK 后，通过 API 接口进行调试。
   * 如果需要在扣子编程预览调试自定义用户变量，你可以在智能体的**记忆** > **变量**中添加自定义用户变量。
   :::   


![Image=300x260](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6d7d7b8c06d84bd5a160e360726b8f97~tplv-goo7wpa0wc-topic.webp)

4. 配置其他节点，并连接各个节点。
   你可以通过拖拽的方式将节点添加到画布内，并按照任务执行顺序连接节点。扣子编程支持插件、大模型等多种对话流节点。
5. 试运行并发布对话流。
   对话流设计完成后，可以在页面下方单击**试运行**，试运行通过后才能发布对话流。
6. 根据页面提示，将对话流添加到当前智能体。
   ![Image=312x104](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1c33b219dd6841d6af5ce2e8ff0cd486~tplv-goo7wpa0wc-topic.webp)   


### 3 添加智能体配置 {#d60915ce}

你可以按需为对话流模式的智能体添加各种配置，例如为对话流绑定卡片、设置对话历史策略、添加变量、开场白等记忆和对话体验设置。

如果对话流中存在大模型节点，且节点上的输入模块已开启智能体**对话历史**参数，则可以调整对话历史策略。目前支持设置携带上下文轮数，默认为 3，取值范围为1~100。

![Image=461x170](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8a5186d6c7d74d66ac753d37e3331489~tplv-goo7wpa0wc-topic.webp)

### 4 调试并发布智能体 {#c2cb79ae}

在智能体的**编排**页面设置完成后，可以在预览与调试区域与智能体对话，体验智能体的交互效果。

调试完成后，在右上角单击**发布**，将智能体发布到各个平台中使用。

![Image=498x200](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b9751185ac85467f9b7675ca0f2b8d99~tplv-goo7wpa0wc-topic.webp)

## 示例 {#72b5d1cb}

以搭建一个产品售后机器人为例，演示如何配置对话流模式智能体的专属对话流。

![Image=603x270](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ffd17496bd0c49fc97686e12f18b94b2~tplv-goo7wpa0wc-topic.webp)

产品售后机器人主要用于售后场景，提供基础的问答服务与售后问题过滤的能力。在这个对话流中，首先通过大模型节点对问题进行分类，并通过选择器节点将不同类型的问题流转到不同的分支处理，最终在结束节点引用各个分支的输出。详细配置说明如下：

<!-- @cols-width: 116,107,294,297 -->
| **环节**  | **节点类型**  | **说明**  | **示例**  |
| --- | --- | --- | --- |
| 开始  | 开始节点  | 开始节点用于接收用户问题，并透传给后续的节点。  | ![Image=300x260](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6d7d7b8c06d84bd5a160e360726b8f97~tplv-goo7wpa0wc-topic.webp)  |
| 识别用户意图  | 大模型节点  | 本示例中，大模型节点用于识别进线用户的意图，判断用户问题的分类。  | ![Image=198x136](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/737ac1c55f0b4a0e9cc8a9b2841a4ff2~tplv-goo7wpa0wc-topic.webp)  |
| 分发用户问题  | 选择器节点  | 选择器节点用于将问题进行分发，转交给不同的分支进行处理，例如将产品咨询问题转交给咨询类知识库处理，故障排查类问题转交给故障排查知识库处理。  | ![Image=198x156](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cac9e1306f1445ee8e0bff0fcb9643aa~tplv-goo7wpa0wc-topic.webp)  |
| 处理用户问题  | 知识库节点、大模型节点  | 产品咨询分支和故障排查分支均使用此逻辑。处理流程如下： | ![Image=200x130](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5ba6e8f58d9949c9a43fcca3ca589d6d~tplv-goo7wpa0wc-topic.webp)  | \
| | | | | \
| | | 1. 知识库节点匹配用户问题。 | | \
| | | 2. 大模型节点包装回复。如果未匹配到知识库，则返回兜底文案。  | |
|^^| 文本处理节点  | 不属于以上两种问题的，转交文本处理节点，统一回复兜底文案“您的反馈已收到，我们将仔细评估”。  | ![Image=211x229](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/badde257c62246289ff029d58b2ac7d1~tplv-goo7wpa0wc-topic.webp)  |
| 结束  | 结束节点  | 根据前置步骤生成的最终答案，输出智能体的回复内容。你可以通过输出变量直接引用前置节点的返回数据。  | ![Image=213x227](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0ab34ba2635041ac80f05faa2d434a64~tplv-goo7wpa0wc-topic.webp)  |

## 常见问题 {#b45fc1ff}

### 非对话流模式的智能体，如何切换到对话流模式？ {#7f1f4fec}

如果当前是单 Agent （自主规划模式）的智能体，则你可以在智能体的**编排**页面，单击**单 Agent （自主规划模式）**，然后切换为**单 Agent （对话流模式）**。

切换后，原来模式下设置的人设与回复逻辑、变量、数据库、开场白等配置会保留，插件、工作流、知识库等不适用于对话流模式，将无法使用。

![Image=359x227](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/42c5f0742a4849c88eb274318675b6e6~tplv-goo7wpa0wc-topic.webp)

### 为什么对话流模式的智能体无法选择公开配置？ {#76df83b5}

改版后，扣子编程暂不支持发布公开配置的智能体，所有发布到商店中的智能体均为私有配置，其他用户无法复制并查看商店中智能体的详细配置信息。

### 对话流模式的智能体，如何添加工作流？ {#d497b652}

对话流模式的智能体不支持添加工作流，仅支持添加对话流。

### 对话流模式的智能体，如何输出用户问题建议？ {#c4b92ad9}

目前对话流模式的智能体不支持输出用户问题建议，如需使用该功能需切换至单 Agent （自主规划模式） 。
