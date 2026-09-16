> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

在项目中，你可以邀请人类成员和 Agent 加入协作。人类成员可以参与讨论、补充信息和确认需求；Agent 可以根据指令处理具体任务，例如整理资料、生成方案、编写代码或分析问题。

当一个项目需要多人共同推进，或者需要多个 Agent 分头处理不同任务时，可以将相关成员邀请到项目中。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 可以邀请哪些成员 {#24545178}

项目中可以邀请以下两类成员：

* **人类成员**：人类成员可以加入项目，和项目创建者一起查看项目内容、参与讨论与分工，并对任务过程和结果进行确认。
* **Agent**：Agent 可以加入项目，根据项目成员的指令处理具体任务。你和其他成员可以根据项目需要添加不同能力的 Agent，例如用于资料整理、内容创作、代码开发、问题分析等。

## 使用限制 {#9a293372}

使用项目协作前，建议关注以下限制和规则：

<!-- @cols-width: 188,695 -->
| **限制**  | **说明**  |
| --- | --- |
| 套餐要求  | 创建项目无套餐版本限制，但仅限**个人高阶版**及以上版本套餐的用户邀请他人加入自己的项目。  |
| 企业组织  | * 企业版用户只能邀请企业内部成员加入协作，不支持邀请访客或外部用户。 | \
| | * 企业员工的个人项目不支持添加协作者，你可以在左下角切换到企业组织下再操作，或者为你的个人账号购买个人高阶版及以上的个人版套餐。  |
| 权限要求  | 各个成员只能添加自己的 Agent。更多权限要求可参考[角色与权限](/cozespace/collaboration#540bc5ac)。  |
| 生效范围  | * 人类成员在项目内全局生效。通过任意子对话邀请后，成员可以在项目下的所有子对话中协作。 | \
| | * Agent 仅在被邀请的单个子对话中生效。  |
| 项目成员数量  | 各个套餐版本的项目人数上限不同，详细限制见下表。  |

包含项目创建者在内，各个套餐版本的项目人数上限：

<!-- @cols-width: 114,114,100,100,100,100,100,100,100,100 -->
| **免费版**  | **个人进阶版**  | **个人高阶版**  | **个人旗舰版**  | **个人尊享版**  | **团队高阶版**  | **团队旗舰版**  | **团队尊享版**  | **企业标准版**  | **企业旗舰版**  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 不支持邀请  | 不支持邀请  | 15 人  | 30 人  | 50 人  | 15 人  | 30 人  | 50 人  | 50 人  | 50 人  |

## 邀请人类成员 {#hNWcBUOHx}

在项目中，你可以邀请人类成员加入协作，与 Agent 一起围绕同一任务进行沟通、补充信息和推进执行。

当前支持以下两种邀请方式：

* **直接邀请**：输入成员信息并发起邀请，对方确认后即可加入项目。目前支持通过手机号、扣子用户名或扣子 UID 查询并添加用户。适用于已明确邀请对象的场景，便于快速拉人进入项目。
* **分享邀请**：通过分享链接或分享二维码邀请成员加入。被邀请人打开链接或扫码后，可提交加入申请，待项目管理员确认后加入项目。适用于需要转发给多人或跨渠道邀请的场景，成员可通过链接或二维码发起加入申请。

### 直接邀请 {#hNTVl2FQl}

::::tabs
@tab 网页端、桌面端
1. 登录[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
2. 进入项目成员邀请页面。
   你可以通过以下任一入口进入：
   * 项目管理页面：在左侧列表的**项目**区域，将鼠标悬浮在目标项目上，单击 ··· > **项目管理**。
      ![Image=164x165](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/90277ef01f6543dabd768750487252b4~tplv-goo7wpa0wc-topic.webp)
   * 项目对话的设置页面：在左侧列表的**项目**区域，找到指定项目下的对话。在项目对话页面左上角单击项目对话名称。
      ![Image=248x137](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0f7f472e6bcd4a69b64c9d6d88abba88~tplv-goo7wpa0wc-topic.webp)
3. 在**项目成员**区域，输入扣子用户的身份信息。
   目前支持通过手机号、扣子用户名、扣子 UID 来查询并添加用户。
4. 找到目标用户，单击加号（+）发送项目邀请。
   ![Image=183x158](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/eab2d6e0a00347c5abfdc50a369089b5~tplv-goo7wpa0wc-topic.webp)
   在目标用户加入项目前，你随时可以在项目成员列表中单击减号（-）撤销邀请。
5. 被邀请的用户会收到一条提醒消息，确认邀请即可加入项目。
   ![Image=135x165](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0357ae17b84146bb9296d7c5146e64f8~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
1. 打开扣子 App。
2. 在**项目**区域，找到指定项目下的对话。
3. 在项目对话页面左上角，单击··· > **设置**。
4. 在**设置**页面，找到**项目成员**区域，点击加号（+）。
5. 输入扣子用户的身份信息。
   目前支持通过手机号、扣子用户名、扣子 UID 来查询并添加用户。
6. 选中目标用户，单击**确认**，发送项目邀请。
   ![Image=311x208](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/81a7a464664244b29e920d2ffd5cfd32~tplv-goo7wpa0wc-topic.webp)
7. 被邀请的用户会收到一条提醒消息，确认邀请即可加入项目。
   ![Image=161x197](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0357ae17b84146bb9296d7c5146e64f8~tplv-goo7wpa0wc-topic.webp)
::::

### 分享邀请 {#hHvO6WD9L}

::::tabs
@tab 网页端、桌面端
1. 登录[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
2. 进入项目成员邀请页面。
   你可以通过以下任一入口进入：
   * 项目管理页面：在左侧列表的**项目**区域，将鼠标悬浮在目标项目上，单击 ··· > **项目管理**。
   * 项目对话的设置页面：在左侧列表的**项目**区域，找到指定项目下的对话。在项目对话页面左上角单击项目对话名称。
3. 找到**项目成员**区域，单击**分享并邀请**。
   ![Image=151x128](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/27f2036a9dc64019ac2a8e05ab1ebb32~tplv-goo7wpa0wc-topic.webp)
4. 根据需要选择以下方式之一：
   * 复制项目链接并分享给其他用户。
   * 展示或保存项目二维码，供其他用户扫码申请加入。
      ![Image=134x161](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4c1c7999e754481dad44e93c6c4f842d~tplv-goo7wpa0wc-topic.webp)
5. 其他用户打开链接或扫描二维码申请加入项目。
   ![Image=224x166](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c6b0783b83774be69b301251fcfdd2ff~tplv-goo7wpa0wc-topic.webp)
6. 项目管理员将收到一条消息提醒，根据页面提示通过这些项目申请后，用户会自动加入项目。
   ![Image=229x213](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2a1da5e938e840bb9e63f7ca13c9defc~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
1. 打开扣子 App。
2. 在**项目**区域，找到指定项目下的对话。
3. 在项目对话页面左上角，单击··· > **设置**。
4. 选择**分享以邀请成员**。
5. 根据需要选择以下方式之一：
   * 复制项目链接并分享给其他用户。
   * 展示或保存项目二维码，供其他用户扫码申请加入。
6. 其他用户打开链接或扫描二维码申请加入项目。
7. 项目管理员会收到一条消息提醒，根据页面提示通过这些项目申请后，用户会自动加入项目。
::::

## 添加 Agent {#18ab2585}

::::tabs
@tab 网页端、桌面端
1. 登录[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
2. 在左侧列表的**项目**区域，找到指定项目下的对话。
3. 在项目对话页面左上角单击项目对话名称。
   扣子会在右侧自动展开项目设置区域。
4. 在**项目设置**页面，找到**当前对话里的 Agent** 区域，单击 > 图标。
   ![Image=332x151](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6f9e0fcf7a844a85b92b5a8ed94369c4~tplv-goo7wpa0wc-topic.webp)
5. 在**我的Agent列表**中找到要添加的 Agent，打开开关。
   ![Image=163x216](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b060e7b4d5ae49f998147fa20283c6bd~tplv-goo7wpa0wc-topic.webp)   


Agent 会立即加入项目。加入后，项目成员可以通过 @Agent 向它下达任务。

![Image=243x212](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/65b9cf86a519479cb64689e5439e3cec~tplv-goo7wpa0wc-topic.webp)

@tab 移动端
1. 打开扣子 App。
2. 在**项目**区域，找到指定项目下的对话。
3. 在项目对话页面左上角，单击··· > **设置**。
4. 在**设置**页面，找到**当前对话里的 Agent** 区域，单击加号（+）。
5. 在**我的Agent列表**中找到要添加的 Agent，打开开关。
   Agent 会立即加入项目。加入后，项目成员可以通过 @Agent 向它下达任务。
   ![Image=194x195](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/216583dfe4dc435e9976662082a265e8~tplv-goo7wpa0wc-topic.webp)
::::

## 管理项目成员和 Agent {#3f5ecb5b}

::::tabs
@tab 网页端、桌面端
* **查看成员列表**：
   在**项目管理**或**设置**页面的**项目成员**区域，然后单击人数区域，即可查看成员列表，包括已加入项目的成员和邀请中的成员。
   ![Image=274x125](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2e2ff8d6a2424c6e9e403cb8265c12ca~tplv-goo7wpa0wc-topic.webp)
* **查看 Agent 列表**：
   在**设置**页面的**当前对话里的Agent**区域，然后单击 Agent 数量区域，即可查看 Agent 列表。列表分为两个部分：
   * **我的 Agent**：你已创建的 Agent 列表，包括扣子 Agent、三方精选 Agent 和已接入的本地 Agent。
   * **项目的 Agent**：已加入项目的 Agent 列表，包括你和其他成员的 Agent。
      ![Image=252x334](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ee0bd7e6466748d2b847dae3dd8145e2~tplv-goo7wpa0wc-topic.webp)
* **移除成员**：仅项目创建者可操作。
   在**项目管理**页面的**项目成员**区域，然后单击人数进入成员列表，找到指定成员后单击减号图标即可。
* **移除 Agent**：各个成员只能移除自己的 Agent，项目创建者可移除项目中的所有 Agent。
   在**设置**页面的**当前对话里的Agent**区域，然后单击数量进入**我的 Agent** 列表，找到指定 **Agent** 后关闭开关即可。

@tab 移动端
* **查看成员列表**：
   在**设置**页面的**项目成员**区域，单击人数区域，即可查看成员列表，包括已加入项目的成员和邀请中的成员。
* **查看 Agent 列表**：
   在**设置**页面的**当前对话里的 Agent** 区域，单击 Agent 数量区域，即可查看 Agent 列表。列表分为两个部分：
   * **我的 Agent**：你已创建的 Agent 列表，包括扣子 Agent、三方精选 Agent 和已接入的本地 Agent。
   * **项目的 Agent**：已加入项目的 Agent 列表，包括你和其他成员的 Agent。
* **移除成员**：仅项目创建者可操作。
   在**设置**页面的**项目成员**区域，单击人数进入成员列表，找到指定成员后单击减号图标即可。
* **移除 Agent**：各个成员只能移除自己的 Agent，项目创建者可移除项目中的所有 Agent。
   在**设置**页面的**当前对话里的 Agent** 区域，单击人数进入**我的 Agent** 列表，找到指定 **Agent** 后关闭开关即可。
::::

## 后续操作 {#248d879c}

成员和 Agent 加入项目后，就可以在项目中围绕同一个目标进行沟通、分工和任务处理。具体协作方式可参考[在项目中协作](/cozespace/collaborate_on_projects)。
