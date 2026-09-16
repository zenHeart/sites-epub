> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

通过**多人协作模式**，团队成员可以像在群聊一样，与 Agent 实时对话，共同开发项目、查看项目进展、修改代码并调试项目。

## 什么是多人协作 AI 编程 {#0a9b6aa3}

多人协作 AI 编程，是让多个成员在同一个编程项目中，共同与 Agent 对话、查看开发进度、修改项目代码的一种协作开发方式。你可以把它理解为：原本是一个人和 Agent 一起开发项目，现在变成一个团队在同一个项目里，像群聊一样一起和 Agent 协作开发。

多人协作支持以下能力：

* **添加协作者**：邀请团队成员加入项目，协同开发。
* **共同工作区**：所有协作者在同一对话中协作，需求、回复、代码变更全员实时可见，Agent 始终基于最新状态推进开发。
* **多人多端实时同步**：所有协作者可在网页端、桌面端或移动端实时同步查看对话、代码变更和项目进展。
* **有序协作**：多人同时发送需求时，Agent 按顺序逐一处理，避免冲突。

## 使用场景 {#57b36afc}

多人协作 AI 编程支持团队成员共同参与应用开发。无论是产品、设计、运营还是研发，都可以直接参与功能讨论、界面修改与逻辑调整，边讨论、边开发、边实现产品。

多人协作 AI 编程能够帮助团队降低沟通成本，加快产品迭代速度，并让更多非技术成员真正参与到应用开发过程中。主要使用场景如下：

* **企业团队快速做产品**：产品经理提出需求，设计师调整页面 UI，开发成员补充逻辑，编程 Agent 自动完成页面与代码修改。
* **小团队共同开发项目**：多个成员一起开发网站、工具或小游戏时，不需要复杂的任务同步流程。成员可以直接在同一个项目中提出修改需求，例如：`帮我增加一个排行榜`、`首页换成暗色风格`。
* **远程团队协作**：跨时区或非同时在线的团队成员，可以通过 Agent 对话记录和项目修改记录了解项目进展，并在最新项目状态上继续补充需求。

## 限制与权益 {#79f16e2a}

使用多人协作 AI 编程时，需要注意以下限制：

* 仅项目创建者可以添加协作者。
* 不支持添加 Agent 为协作者。
* 协作者可以发送对话、修改代码，不支持部署项目。
* 套餐权益
   任何版本用户均可被邀请为协作者。邀请他人需满足以下套餐：
   <!-- @cols-width: 192,112,112,120,120,100,120,120,100,136,120 -->
   | | | | | | | | | | | | \
   |订阅套餐 |**个人免费版** |**个人进阶版** |**个人高阶版** |**个人旗舰版** |**个人尊享版** |**团队高阶版** |**团队旗舰版** |**团队尊享版** |**企业标准版** |**企业旗舰版** |
   |---|---|---|---|---|---|---|---|---|---|---|
   |项目协作 |➖ |➖ |✔️ |✔️ |✔️ |✔️ |✔️ |✔️ |✔️ |✔️ |
   |每个项目协作者数量 |➖ |➖ |15 |30 |50 |15 |30 |50 |50 |50 |
* 访问控制权益：在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。

## 使用方式 {#84bf26c4}

本文以团队共同开发一个 AI 营销落地页为例，说明多人协作 AI 编程的使用方式。假设由产品经理创建项目并完成基础开发，然后由产品经理将设计师、研发成员、运营成员等添加为协作者，一起开发项目。

### 前提条件 {#4fcaa512}

* 创建一个编程项目。具体操作，请参考[步骤一：创建编程项目](/cozespace/vibe_coding_web_app#f1fffc2c)。
* 完成基础开发。具体操作，请参考[步骤二：需求澄清](/cozespace/vibe_coding_web_app#a2fff1be)。
   ```Markdown
   帮我创建一个 AI 营销工具首页，包含产品介绍、价格方案和用户评价模块。
   ```
   ::::tabs
   @tab 网页端、桌面端
   ![Image=508x268](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ce51c64de13346f2b2ac652871209ca1~tplv-goo7wpa0wc-topic.webp)
   
   @tab 移动端
   ![Image=222x446](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/179ee5085d1649d59fbe1bdb2d62a7c2~tplv-goo7wpa0wc-topic.webp)
   ::::   


### 添加协作者 {#1f372864}

由项目创建者添加协作者。

* 个人版套餐可以添加其他个人版账号为协作者。
* 企业版套餐可以添加企业统一组织内的成员为协作者。如何添加组织成员，请参考[添加组织成员](/guides/add_organization_member)。
   ::::tabs
   @tab 网页端、桌面端
   1. 项目创建者添加协作者。
      在编程项目开发页面的顶部，单击**协作**，将设计师、开发等人员添加为协作者。
      ![Image=376x222](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/399b7a18f56f479cac516efb31c076be~tplv-goo7wpa0wc-topic.webp)
   2. 协作者收到邀请后，确认加入项目。
      协作者将在扣子中收到邀请通知，确认加入即可。
      ![Image=385x207](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6bfb9bbe0e7a4a4a9148d04149e5d371~tplv-goo7wpa0wc-topic.webp)
   
   @tab 移动端
   1. 项目创建者添加协作者。
      在编程项目开发页面的顶部，单击**添加协作者**图标，将设计师、开发等人员添加为协作者。
      ![Image=301x304](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/547229ef56454e2d919d28e43b086433~tplv-goo7wpa0wc-topic.webp)
   2. 协作者确认成为协作者。
      协作者将在扣子中收到邀请通知，确认加入即可。
      ![Image=145x294](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c4271e2d63074c79a76f1f75feec9a23~tplv-goo7wpa0wc-topic.webp)
   ::::   


### 分工协作 {#36773a79}

协作者加入后，可以围绕同一个项目继续补充需求，协同开发。

协作机制如下：

* **共享工作区：​**所有协作者进入项目后，看到的是同一个 Agent 对话、项目代码和开发环境。
   一个协作者让 Agent 改了页面，其他人立刻看到最新效果。
* **有序协作：​**多人同时提需求时，Agent 按先后顺序逐一处理，避免冲突。
* **权限与角色：​**项目创建者可以添加协作者、开发与部署项目。协作者可以对话、改代码、调试环境，但不能部署。
   ::::tabs
   @tab 网页端、桌面端
   ![Image=448x273](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d0f1f3c8b89c4a63946ae9df0077870d~tplv-goo7wpa0wc-topic.webp)
   
   @tab 移动端
   ![Image=154x296](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/596a1f1a25c14dce812131668c92f7ba~tplv-goo7wpa0wc-topic.webp)
   ::::   


协作示例如下：

* 设计师调整页面风格
   ```Markdown
   整体风格改成深色科技风，按钮增加渐变效果。
   ```
   Agent 会基于已有页面修改 UI 样式、按钮效果和视觉细节，其他成员可以直接看到更新后的页面效果。
* 研发补充功能逻辑
   ```Markdown
   增加文件存储与用户登录功能。
   ```
* 运营调整页面内容
   ```Markdown
   把首页标题改成「让 AI 帮你提升营销转化率」。
   ```   


## 后续操作 {#36aebda7}

项目开发完成并确认无误后，由项目创建者执行部署上线。具体操作，请参考[部署网页应用](/guides/deploy_vibe_web)。

::::tabs
@tab 网页端、桌面端
单击页面右上角的**部署**图标，然后单击**开始部署**。

![Image=442x338](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4b8c798de10f45cf810704ed9a0db539~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
单击页面右上角的**部署**图标，然后单击**开始部署**。

![Image=210x395](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a5a99f205f7b4124b1493cbcddbbfe62~tplv-goo7wpa0wc-topic.webp)
::::
