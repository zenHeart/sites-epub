> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

大模型由于其工作原理，虽然可以回答通用的问题，但在专业技术的垂直领域中，模型知识的技术深度、更新及时性和准确性非常有限。如果对于模型生成的文本准确性的要求较高，例如企业智能客服、高精尖科学技术服务等应用场景中，往往需要通过知识库集成私有的知识数据，丰富 AI 应用的知识范围、提高模型回复的可靠性。

创建扣子知识库或关联火山知识库后，你可以将知识库直接与低代码智能体进行关联用于响应用户回复；可以在低代码工作流中添加知识库写入节点、知识库检索节点或知识库删除节点，成为工作流中的一环。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 在低代码智能体中使用知识库 {#83de81c0}

参考以下操作，在智能体中添加知识库。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**项目开发**。
3. 选择一个已创建的低代码智能体。
4. 在**编排**页面的**知识**区域，选择**扣子知识库**或**火山知识库**，然后单击对应的 **+** 图标，添加要使用的知识库。
   ![Image=657x187](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/940b526c16234444b778f3ffefdcb576~tplv-goo7wpa0wc-topic.webp)   


## 在低代码工作流中使用知识库 {#bfacec97}

低代码应用的业务流程中，检索知识库的时机与方式由工作流的节点编排决定。

* 如果需要在知识库中检索知识，可以在工作流中添加**知识库检索节点**，工作流运行到这个节点时，会根据节点设置的检索和召回逻辑，选择最符合用户需求的一批知识，通过输出参数传递到后续节点。知识库检索节点的详细说明，可参考[知识库检索节点](/guides/knowledge_node)。
* 如果需要上传新的文档到指定的文档知识库，可以在工作流中添加**知识库写入节点**，工作流运行到这个节点时，系统会根据业务逻辑向指定文档知识库中上传文档，为知识库增加新的知识。知识库写入节点的详细说明，可参[知识库写入节点](/guides/knowledge_base_writing_node)。
* 如果需要删除知识库中的文档，可以在工作流中添加**知识库删除节点**，工作流运行到这个节点时，系统会根据业务逻辑删除指定知识库中的文档。知识库删除节点的详细说明，可参考[知识库删除节点](/guides/knowledge_delete_node)。

参考以下操作，在工作流中添加知识库检索节点、知识库写入节点或知识库删除节点。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 在**工作流**页签下，选择一个目标工作流或创建一个新的工作流。
4. 在工作流中添加知识库检索节点、知识库写入节点或知识库删除节点，并选择要添加的知识库。
   ![Image=658x217](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/aee9bfdef5a14cea88541e7d05a2806c~tplv-goo7wpa0wc-topic.webp)
