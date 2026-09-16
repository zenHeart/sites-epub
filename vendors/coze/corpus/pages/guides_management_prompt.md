> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

提示词可以作为资源保存在资源库中，提示词资源库是团队共享和使用的宝贵资产，它包含了用于指导大语言模型（LLM）行为的一系列提示。通过本文档，你可以了解如何在资源库中创建、引用、编辑和删除提示词，以确保提示词资源库的持续更新和优化。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 创建提示词 {#0a99aebe}

### 在资源库中创建资源 {#d52e0629}

你可以在资源库中创建提示词。创建提示词时，你可以根据业务需要直接编写提示词，也可以通过 AI 自动生成提示词，编写提示词可参考[编写提示词](/guides/write_prompt)，通过 AI 生成提示词可参考[AI 生成提示词](/guides/set_prompt#4f0e8ff4)。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 在页面右上角，选择**资源** > **提示词**。
   ![Image=443x141](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/65d925ae15b44069a7a25310c6f9c938~tplv-goo7wpa0wc-topic.webp)
4. 设置提示词的名称、描述和内容，并单击**确认**。
   ![Image=261x381](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fc1c375e30244ae59e95d5c92eb28ad5~tplv-goo7wpa0wc-topic.webp)   


### 将提示词保存为资源 {#31c23440}

你可以将低代码智能体中的提示词保存为资源，资源会存储在资源库中，可以供其他成员使用。

:::tip 说明
目前，仅低代码智能体的提示词可以保存为资源，而工作流的大模型节点不支持此操作。
:::

1. 在**人设与回复逻辑**面板，单击**提示词库**图标。
   ![Image=400x253](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/26b5e64b989e4f90ab126c60e5e25102~tplv-goo7wpa0wc-topic.webp)
2. 单击 **+ 新建提示词**。
   ![Image=272x228](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7f415b08604a4b4cb59e73422340e5a7~tplv-goo7wpa0wc-topic.webp)
3. 在**创建提示词**弹窗中，设置提示词名称和描述，单击**导入当前提示词**，然后单击**确认。**
   ![Image=273x307](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d8f7ef6caef246c3825905d5d155f0bc~tplv-goo7wpa0wc-topic.webp)   


保存为资源后，你可以在资源库中查看已保存的提示词。

![Image=2231x376](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/90052adc35374dd4bd7f85ac629c8e1f~tplv-goo7wpa0wc-topic.webp)

## 引用提示词 {#221bec0a}

提示词可以作为资源保存在资源库中，供工作空间内的其他成员引用。无论是智能体还是工作流的大模型节点，都可以引用资源库中的提示词，详情可参考[引用提示词资源](/guides/set_prompt#2ab4afd7)。

## 编辑提示词 {#02e89766}

提示词的所有者可以编辑自己创建的提示词，工作空间所有者和管理员可以编辑工作空间内其他成员创建的提示词，但工作空间内的普通成员没有此权限。

1. 在资源库的**提示词**页签中，找到目标提示词，然后在**操作**列中，选择 **···** > **编辑**。
   ![Image=595x188](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1286b434a48649deb7499e9b09051ddf~tplv-goo7wpa0wc-topic.webp)
2. 在**编辑提示词**对话框中，设置提示词，然后单击**确认。**
   ![Image=337x381](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/37c47fdd063d40f6bbae7740fead7a28~tplv-goo7wpa0wc-topic.webp)   


## 删除提示词 {#8524635d}

删除资源库中的提示词，对使用了该提示词的智能体和工作流没有影响。提示词的所有者可以删除自己创建的提示词，工作空间所有者和管理员可以删除工作空间内其他成员创建的提示词，但工作空间内的普通成员没有此权限。

1. 在资源库的**提示词**页签中，找到目标提示词，然后在**操作**列中，选择 **···** > **删除**。
   ![Image=2236x423](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ab2bfd82ca6348168afe0dea30a660ed~tplv-goo7wpa0wc-topic.webp)
2. 在弹出的对话框中，单击**确定**。
   ![Image=579x173](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/89479c4e451b4de2aec88a4e28735833~tplv-goo7wpa0wc-topic.webp)
