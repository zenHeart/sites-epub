> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

本教程以搭建一个`AI 助手`的用户界面为例，为你演示如何搭建移动端的用户界面。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 前提条件 {#34251066}

你已经通过工作流编排完后端业务逻辑。本教程中的 AI 助手应用，主要是通过大模型回答用户的问题，所以只需要创建一个包含大模型节点的对话流即可，详情请参考[步骤三：编排业务逻辑](/guides/chatflow_quickstart#b13970d6)。

![Image=1842x375](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/922d674948e9467089e5d65cd64c087a~tplv-goo7wpa0wc-topic.webp)

本教程搭建用户界面的步骤如下图：

![Image=569x134](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a88137b5bcbf4621bf1599591ba76509~tplv-goo7wpa0wc-topic.webp)

## 步骤 1：设计用户界面 {#c160491d}

在开始开发前，你需要设计 AI 助手的用户界面。

AI 助手的界面应是类似通讯软件的对话式页面，以便用户能够与 AI 助手进行互动。用户界面编辑器提供了 AI 对话组件，你可以直接使用这个组件来快速搭建 AI 助手用户界面，从而简化开发流程。

![Image=365x181](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/be54f8e531154d40a0e79fb42ebc55d2~tplv-goo7wpa0wc-topic.webp)

## 步骤 2：搭建用户界面 {#cf3a840d}

扣子提供了可视化的用户界面搭建能力，你可以通过拖拉拽的方式搭建一个用户界面，无需编写一行代码。

参考以下操作，搭建 AI 助手应用的用户界面。

1. 在应用 IDE，单击页面上方的**用户界面**页签。
2. 选择页面类型。
   扣子应用支持发布为小程序等移动端应用，也可以发布为 Web 页面等网页应用。这里我们选择**小程序和 H5**。
   ![Image=451x269](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/09b19376ea2b45d7b75bf931de810295~tplv-goo7wpa0wc-topic.webp)
3. 搭建页面布局。
   AI 助手应用只有一个简单的对话窗口，所以我们只需要搭建一个页面并添加 AI 对话组件即可。
   1. 在画布中选中页面，并在右侧 Page1 配置面板中关闭导航栏。
      移动端页面默认开启首页底部的导航栏，AI 助手应用只有一个页面，所以需要手动关闭底部的导航栏。
      ![Image=388x249](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/94cd8eda061447aeadda2d81c841b62a~tplv-goo7wpa0wc-topic.webp)
   2. 在**组件**面板中，找到 **AI 组件 > AI对话**组件，然后将 AI 对话组件拖入到画布中。
      ![Image=501x242](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9b658d074a8948868450c751954e0068~tplv-goo7wpa0wc-topic.webp)
4. 设置组件属性。
   1. 在画布中，选中拖入的 **AI对话**组件。组件名称为`Chat1`。
   2. 在 `Chat1` 组件配置面板中，修改以下配置：
      <!-- @cols-width: 158,359,203 -->
      | **配置**  | **说明**  | **示例**  |
      | --- | --- | --- |
      | 对话流  | 选择步骤三中搭建的对话流，也就是 ai_assistant。  | ![Image=586x361](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a64e4a9f56f64e6ea5c019251ea02ab5~tplv-goo7wpa0wc-topic.webp)  |
      | 头像  | 单击**上传**，为你的 AI 助手上传一个头像。  | ![Image=588x192](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/83d27413f45b496f81aa44f4f8667af8~tplv-goo7wpa0wc-topic.webp)  |
      | bot名称  | 此名称会作为 AI 助手的名称显示在对话页面。默认为 coze Assistant，此处我们修改为 `AI 助手`。  | ![Image=592x128](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/128f046c24004c1695e391b29e5d4050~tplv-goo7wpa0wc-topic.webp)  |
      | 开场白  | AI 助手的开场白，可以直接使用以下示例文案。 | ![Image=574x309](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6bbc4ea1ba594188a38dd1cf8812986c~tplv-goo7wpa0wc-topic.webp)  | \
      | | | | \
      | | ```Plain Text | | \
      | | 你好！我是你的专属 AI 助手。无论你需要查询信息、提供建议、还是简单的聊天，我都在这里为你服务。 | | \
      | | 告诉我你的需求，让我们开始愉快的对话吧！ | | \
      | | ```  | |
      | 开场白预置问题。  | AI 对话组件预置了三个开场白问题，这里我们改为以下三个开场白问题： | ![Image=576x281](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/66bc5f7ae61f4853ae28eaabf41c53ac~tplv-goo7wpa0wc-topic.webp)  | \
      | | | | \
      | | * 双子座有什么特点 | | \
      | | * 推荐一本好书 | | \
      | | * 想去新疆，有什么行程建议吗  | |      


配置效果如下：

![Image=588x385](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ebf41e1e40ea4f25a79c41e109f5e63e~tplv-goo7wpa0wc-topic.webp)

## 步骤 3：预览用户界面 {#c8a016ab}

完成上述所有配置后，单击**预览**查看整体功能并进行体验。

![Image=277x196](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/60165dadec35445ca438f955bec83792~tplv-goo7wpa0wc-topic.webp)

页面会展示 AI 助手在移动端的页面预览效果，你可以在页面下方的输入框中输入一段文字，并按回车键发送消息。AI 助手会立即回复你的问题。

![Image=203x418](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5a02b798916841b48c0b5f338603a7cd~tplv-goo7wpa0wc-topic.webp)
