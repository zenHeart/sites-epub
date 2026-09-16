> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

提示词是一种自然语言指令，它为大语言模型（LLM）提供任务指导。搭建低代码智能体或配置低代码工作流的大模型节点都需要设置提示词，你可以根据业务需要直接编写提示词，也可以使用提示词模版、引用提示词资源或通过 AI 自动生成提示词。

## 为低代码智能体设置提示词 {#7f198a01}

智能体是基于大语言模型的 AI 应用，搭建智能体的第一步就是设置提示词。

### 直接编写提示词 {#a9498a68}

你可以根据业务需要编写提示词，提示词编写得越清晰明确，智能体的回复也会越符合预期。关于如何编写提示词，请参考[编写提示词](/guides/write_prompt)。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**创建** > **创建智能体**。
3. 根据页面提示，创建一个新智能体。
4. 在**人设与回复逻辑**面板中编写提示词。
   ![Image=335x512](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7e98fc79185f4d45b4985b4b07df265a~tplv-goo7wpa0wc-topic.webp)   


### 使用提示词模版 {#6d20edb6}

扣子编程根据不同的业务场景提供了多套提示词模版，你可以直接使用模版，或参考模版编写提示词。

1. 在**人设与回复逻辑**面板中，单击**提示词库**图标。
   ![Image=400x253](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/26b5e64b989e4f90ab126c60e5e25102~tplv-goo7wpa0wc-topic.webp)
2. 在**推荐**页签下，选择系统推荐的提示词模版，然后单击**插入提示词**。
   ![Image=446x261](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/62a359aba0f04d3daec542e72b02833b~tplv-goo7wpa0wc-topic.webp)
   单击**插入提示词**后，系统会将选择的提示词自动填充到提示词的编辑框中，你可以基于自己的业务场景修改提示词。修改提示词时，你需要重点关注提示词中的高亮部分。
   * 添加文本：你可以根据高亮部分的文字引导，添加文本内容。
      ![Image=572x202](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/98023213ed934b5584e112dc0f6abf65~tplv-goo7wpa0wc-topic.webp)
   * 添加技能：如果提示词中引用了技能，你需要添加或替换为当前智能体或工作流中已经配置的技能，以确保技能可用。
      ![Image=575x144](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0766df5f6efd455a8624ca8d97992dc0~tplv-goo7wpa0wc-topic.webp)      


### 引用提示词资源 {#02dcbd06}

提示词可以作为资源保存在资源库中，供工作空间内的其他成员引用。引用提示词资源前，请确保资源库中已经创建了提示词，详情可参考[创建提示词 ](/guides/management_prompt#0a99aebe)。

:::tip 说明
如果引用的提示词中包含了插件、工作流、图像流资源，而智能体中未配置该资源，引用提示词后，提示词中资源块名称会显示为灰色。此时，大模型不会调用对应资源，为智能体添加资源后，大模型方可按照提示词指令正常执行。
:::

1. 在**人设与回复逻辑**面板的右下角，单击**提示词库。**
   ![Image=327x489](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7b97c5bf413e4d9a89962bab2d6c3899~tplv-goo7wpa0wc-topic.webp)
2. 在**工作空间**页签下，选择工作空间内的提示词资源，然后单击**插入提示词**。
   ![Image=340x282](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/34e0ce28ce4c464489577003b8d9cc46~tplv-goo7wpa0wc-topic.webp)
   单击**插入提示词**后，系统会将选择的提示词自动填充到提示词的编辑框中，你可以基于自己的业务场景修改提示词。修改提示词时，你需要重点关注提示词中的高亮部分。
   * 添加文本：你可以根据高亮部分的文字引导，添加文本内容。
      ![Image=572x202](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/98023213ed934b5584e112dc0f6abf65~tplv-goo7wpa0wc-topic.webp)
   * 添加技能：如果提示词中引用了技能，你需要添加或替换为当前智能体或工作流中已经配置的技能，以确保技能可用。
      ![Image=575x144](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0766df5f6efd455a8624ca8d97992dc0~tplv-goo7wpa0wc-topic.webp)      


### AI 生成提示词 {#0b237851}

你可以通过自然语言告诉 AI 你希望编写或优化的提示词，大语言模型会根据你的描述，自动生成提示词；你也可以根据调试结果，告诉大语言模型提示词哪里不符合预期以及你的预期效果，大语言模型会自动帮你完成优化。

1. 在**人设与回复逻辑**面板的右上角，单击**优化。**
   ![Image=441x171](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ec3277aca13d4e13ab039733a42b8051~tplv-goo7wpa0wc-topic.webp)
2. 输入你希望编写或优化的提示词，单击发送图标，AI 会根据你的描述自动生成提示词。
   如果你的智能体已完成调试，你可以单击**根据调试结果优化**，然后输入哪里不符合预期以及你的预期效果，大语言模型会自动帮你完成优化。
   ![Image=519x188](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/75eeb3bc45fa466e8b57416d6ed87526~tplv-goo7wpa0wc-topic.webp)
3. 单击**替换**，AI 生成的提示词会自动填充到提示词编辑框中。
   你也可以对 AI 生成的提示词执行以下操作：
   * **退出**：关闭 AI 生成的页面。
   * **复制**：复制 AI 生成的提示词。
   * **重新生成**：如果你对 AI 生成的提示词不满意或想要尝试不同的结果，可以单击重新生成图标，AI 会再次根据你的输入生成新提示词。
   * **点赞**：如果 AI 生成的提示词符合你的期望或对你有帮助，可以单击点赞图标，来给予正面反馈。
   * **点踩**：如果 AI 生成的提示词不满足你的需求，可以单击点踩图标，然后选择不满意的原因，帮助 AI 学习并改进未来的输出。
      ![Image=351x372](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/af962cd9ca45408c8904c0ed339eabbe~tplv-goo7wpa0wc-topic.webp)      


## 为低代码工作流设置提示词 {#dad14c4a}

如果工作流使用了大模型节点，你需要为大模型节点设置提示词，指导大模型执行任务。

:::tip 说明
工作流中的问答节点、意图识别节点也需要设置提示词，但不能引用资源库中的提示词。
:::

### 直接编写提示词 {#325cd2b0}

你可以根据业务需要编写提示词，提示词编写得越清晰明确，大模型的回复也会越符合预期。关于如何编写提示词，请参考[编写提示词](/guides/write_prompt)。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 在**工作流**页签下，选择目标工作流或创建一个新工作流。
4. 在工作流画布中，单击大模型节点，弹出节点配置弹窗。
5. 在**系统提示词**区域，单击展开图标。
   ![Image=348x352](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/955b7c823bc34d6f8fa4d6d1e2b98fee~tplv-goo7wpa0wc-topic.webp)
6. 在提示词的编辑框中，编写提示词。
   ![Image=446x204](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5fba0c56314a4a22a05f84da702ed46d~tplv-goo7wpa0wc-topic.webp)   


### 使用提示词模版 {#ca6433b0}

扣子根据不同的业务场景提供了多套提示词模版，你可以直接使用模版，或参考模版编写提示词。

1. 在**系统提示词**区域，单击提示词库图标。
   ![Image=354x358](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/75395f1f3fb74123bd539b21aa134377~tplv-goo7wpa0wc-topic.webp)
2. 在**推荐**页签下，选择系统推荐的提示词模版，然后单击**使用提示词**。
   ![Image=445x372](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4ad1c48d33eb48e5ba4f47d1b65ae551~tplv-goo7wpa0wc-topic.webp)   


单击**插入提示词**后，系统会将选择的提示词自动填充到提示词的编辑框中，你可以基于自己的业务场景修改提示词。修改提示词时，你需要重点关注提示词中的高亮部分。

* 添加文本：你可以根据高亮部分的文字引导，添加文本内容。
   ![Image=572x202](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/98023213ed934b5584e112dc0f6abf65~tplv-goo7wpa0wc-topic.webp)
* 添加技能：如果提示词中引用了技能，你需要添加或替换为当前智能体或工作流中已经配置的技能，以确保技能可用。
   ![Image=575x144](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0766df5f6efd455a8624ca8d97992dc0~tplv-goo7wpa0wc-topic.webp)   


### 引用提示词资源 {#ded8ad3c}

提示词可以作为资源保存在资源库中，供工作空间内的其他成员引用。引用提示词资源前，请确保资源库中已经创建了提示词，详情可参考[创建提示词 ](/guides/management_prompt#0a99aebe)。

:::tip 说明
如果引用的提示词中包含了插件、工作流、图像流资源，而工作流中未配置该资源，引用提示词后，提示词中资源块名称会显示为灰色。此时，大模型不会调用对应资源，为工作流添加资源后，大模型方可按照提示词指令正常执行。
:::

1. 在**系统提示词**区域，单击提示词库图标。
   ![Image=354x358](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/75395f1f3fb74123bd539b21aa134377~tplv-goo7wpa0wc-topic.webp)
2. 在**工作空间**页签下，选择工作空间内的提示词资源，然后单击**使用提示词**。
   ![Image=332x250](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e9f17c3251344bae9b19e6b52fc5b347~tplv-goo7wpa0wc-topic.webp)
   单击**插入提示词**后，系统会将选择的提示词自动填充到提示词的编辑框中，你可以基于自己的业务场景修改提示词。修改提示词时，你需要重点关注提示词中的高亮部分。
   * 添加文本：你可以根据高亮部分的文字引导，添加文本内容。
      ![Image=572x202](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/98023213ed934b5584e112dc0f6abf65~tplv-goo7wpa0wc-topic.webp)
   * 添加技能：如果提示词中引用了技能，你需要添加或替换为当前智能体或工作流中已经配置的技能，以确保技能可用。
      ![Image=575x144](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0766df5f6efd455a8624ca8d97992dc0~tplv-goo7wpa0wc-topic.webp)      


### AI 生成提示词 {#b02de846}

你可以通过自然语言告诉 AI 你希望编写或优化的提示词，大语言模型会根据你的描述，自动生成提示词；你也可以根据调试结果，告诉大语言模型提示词哪里不符合预期以及你的预期效果，大语言模型会自动帮你完成优化。

1. 在**系统提示词**区域，单击展开图标。
   ![Image=348x352](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/955b7c823bc34d6f8fa4d6d1e2b98fee~tplv-goo7wpa0wc-topic.webp)
2. 在提示词编辑框的右上角，单击**优化。**
   ![Image=631x147](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7ca2b04611514b50a7afbabbb749d09d~tplv-goo7wpa0wc-topic.webp)
3. 输入你希望编写或优化的提示词，单击发送图标，AI 会根据你的描述自动生成提示词。
   如果你的工作流已完成调试，你可以单击**根据调试结果优化**，然后输入哪里不符合预期以及你的预期效果，大语言模型会自动帮你完成优化。
   ![Image=411x145](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9c15fc2c13694da2b877ce3331fcbef4~tplv-goo7wpa0wc-topic.webp)
4. 单击**替换**，AI 生成的提示词会自动填充到提示词编辑框中。
   你也可以对 AI 生成的提示词执行以下操作：
   * **退出**：关闭 AI 生成的页面。
   * **复制**：复制 AI 生成的提示词。
   * **重新生成**：如果你对 AI 生成的提示词不满意或者想要尝试不同的结果，可以单击重新生成图标，AI 会再次根据你的输入生成新提示词。
   * **点赞**：如果 AI 生成的提示词符合你的期望或者对你有帮助，可以单击点赞图标，来给予正面反馈。
   * **点踩**：如果 AI 生成的提示词不满足你的需求，可以单击点踩图标，然后选择不满意的原因，帮助 AI 学习并改进未来的输出。
      ![Image=351x372](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/af962cd9ca45408c8904c0ed339eabbe~tplv-goo7wpa0wc-topic.webp)
