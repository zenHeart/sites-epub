> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子面向企业推出两种企业订阅套餐。购买企业订阅套餐之后，操作者默认成为企业的管理员，可以搭建企业、添加企业成员，和成员协同开发智能体、使用企业内的资源和高级权益。

## 场景说明 {#feb6d15c}

为了享受企业版的各种高级权益，例如更大的企业用户规模、更丰富的安全特性，扣子用户可以购买企业版套餐，实现中大型 AI 应用的多人协作。购买企业版之后，操作者默认为企业的超级管理员，需要创建企业、组织、管理权限。关于企业的概念，可参考[了解企业团队](/guides/team_and_enterprise_overview)。

本文档以从零搭建企业组织为例，演示购买企业版、创建企业并添加企业成员的操作步骤。

## 准备工作 {#aac2d80a}

* 了解企业版的高级权益与计费规则。你可以在订阅套餐页面查看高级权益，通过文档[计费概述](/coze_pro/billing_overview)了解计费规则。
* 如果你需要将个人版中已搭建的资源、已创建的子用户添加到企业中，建议你参考[迁移至企业版](/vg08lpq5/coze_pro_upgrade_to_premium)。

## 步骤一：购买企业旗舰版 {#c8ae60d6}

登录扣子编程后，参考以下步骤购买企业版订阅套餐。

1. 在[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的左下角，单击**积分**。
2. 在**订阅管理**页面中，找到企业版，选择一个版本，并单击**升级**。
   ![Image=349x231](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/83389071c42f48f1be482402302b0f00~tplv-goo7wpa0wc-topic.webp)
3. 根据页面提示完成购买与支付。
   :::tip 说明
   如果你未完成火山引擎实名认证，则需要根据页面提示先完成企业或个人实名认证。
   :::   


![Image=306x202](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2e09880884ea4b8bab2f5a8f6242abc9~tplv-goo7wpa0wc-topic.webp)

## 步骤二：创建企业 {#d185d19d}

成功购买企业版之后，系统会引导你创建企业，并为企业设置企业名称和头像。

1. 根据页面提示，输入企业名称、设置企业头像。
2. 单击**创建企业**。
   ![Image=559x293](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/69c9b97eb3784b2ca92d3e56a7cf51cf~tplv-goo7wpa0wc-topic.webp)   


## 步骤三：创建组织 {#afcc564c}

企业包含默认组织，用户加入时自动加入该默认组织。扣子企业版支持创建多个组织，企业超管和管理员可按部门或项目创建组织，实现多业务部门的独立运作与统一管理。

:::tip 说明
仅企业旗舰版支持创建多个组织，企业标准版仅支持默认组织。
:::

1. 企业超级管理员或管理员登录[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
2. 在左下角单击个人头像，选择企业版账号 > **企业管理**。
   ![Image=310x247](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5e320c7563004495996120dc681c3d6e~tplv-goo7wpa0wc-topic.webp)
3. 在左侧导航栏选择**企业组织管理**，单击右上角的 **+创建组织**。输入组织名称和描述，单击**确认**。
   ![Image=639x229](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d5021be280bd4024b515609ba9f338a2~tplv-goo7wpa0wc-topic.webp)   


## 步骤四：创建工作空间 {#2ed9733b}

:::tip 说明
* **角色限制**：组织超级管理员和管理员。
* 每个扣子账号可创建的空间数量取决于账户所属套餐类型。详细说明请参考[订阅套餐](/coze_pro/premium_package)。
:::

1. 组织超级管理员或管理员在左下角单击个人头像，选择企业版账号 > **企业管理**。
2. 在**企业组织管理**页面单击指定的组织。
3. 在空间管理页面右上角单击➕**创建空间**。
4. 在**创建新工作空间**对话框，配置工作空间名称、描述和空间头像，并单击**确认**。
   成功创建空间后，你可以在空间中创建智能体、插件等资源。   


## 步骤五：添加成员 {#52e9f526}

如果需要创建新的子用户，并使子用户同样享受企业版权益，你需要在火山扣子控制台创建新的子用户，然后将其加入企业，共享企业资源。

:::tip 说明
升级企业版之后，所有已创建子用户都会**变为个人免费版**，需要**重新添加**到企业内，才能享受高级权益。
:::

### 1 创建成员 {#afda3334}

扣子支持在火山引擎扣子控制台中通过导入已有 IAM 用户、自定义创建和批量创建三种方式创建成员。本文档以自定义创建为例。

1. 企业超级管理员进入[企业组织管理](https://admin.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)页面。
2. 在左侧导航栏选择**企业成员管理**，在**成员列表**页面右上角单击 **+成员**。
3. 在**添加新成员**对话框中，单击**创建内部成员账号**。
   单击后，页面将跳转至火山引擎扣子控制台。
   ![Image=565x351](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0a096bdaf63349ad82b544ee0bd13705~tplv-goo7wpa0wc-topic.webp)
4. 在火山引擎扣子控制台的**成员管理**页面的**01创建成员**页签下，单击**立即创建**。
   ![Image=500x232](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4026ad65b99b4b2ab03db3764a1fb3b0~tplv-goo7wpa0wc-topic.webp)
5. 在**创建成员**页面，根据页面提示完成创建。
   创建成员时，可以勾选短信或邮件通知方式，系统将在成员创建成功后自动通过短信或邮件将成员信息发送给对应用户。创建成功后，系统会自动激活成员。
   ![Image=584x300](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/822e6bdd8fc947228d456edbf906cb5f~tplv-goo7wpa0wc-topic.webp)
6. 在**成员列表**中查看该成员是否已自动加入企业。
   创建成员成功后，系统会自动尝试将成员加入企业，当成员状态变更为**已加入企业**，表示加入成功。
   如果出现特殊情况导致成员未自动加入企业时，可以手动将成员加入到企业中，具体请参考[步骤三：手动加入企业（可选）](/guides/create_member#0ec2a393)。
   ![Image=600x260](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c94f09a167024b85b5f22c262ad47c8b~tplv-goo7wpa0wc-topic.webp)
   :::tip 说明
   成员状态说明如下：
   
   * **已激活**：该成员未加入企业，不计入企业的成员费用。
   * **已加入企业**：该成员已成功加入企业，开始计算成员数量。更多成员计费信息，请参考[席位费用（已下架）](/coze_pro/member_fee)。
   :::   


### 2 手动加入企业（可选） {#a1f091ed}

创建成员成功后，系统会自动将成员加入企业，如果出现特殊情况导致成员未自动加入企业时，企业超级管理员或管理员可以参考如下步骤登录扣子编程，手动将成员加入到企业中。

1. 企业超级管理员进入[企业成员管理](https://admin.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)页面。
2. 在左侧导航栏选择**企业成员管理**，在**成员列表**页面单击右上角的 **+成员**。
   ![Image=2275x870](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c28ec5b341c445adb70c92617e4b3f01~tplv-goo7wpa0wc-topic.webp)
3. 选中上述已创建的成员，设置其身份，然后单击**确认**。
   :::tip 说明
   如果子用户较多，可以搜索用户名、用户昵称或火山成员名来快速定位用户。用户可以在**账号设置**页面查看自己的用户信息。具体操作，请参考[如何获取用户名称？](/guides_create_member#12feca48)。
   :::   


### 3 加入组织 {#669e214f}

**组织超级管理员和管理员**可以邀请员工（子用户）和外部成员（访客）加入对应的组织。成员加入对应组织后，其在默认组织中不会被删除。

1. 企业超级管理员或管理员登录[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
2. 在左下角单击个人头像，选择企业版账号 > **企业管理**，进入**企业管理**页面。
   ![Image=310x247](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5e320c7563004495996120dc681c3d6e~tplv-goo7wpa0wc-topic.webp)
3. 在**企业组织管理**页面，单击已创建的组织。
4. 在**组织管理**页面的顶部选择**组织成员管理**。
   ::::tabs
   @tab 单个添加
   1. 在成员列表页面，单击 **+成员**。
   2. 在搜索框中输入用户名、用户昵称或火山成员名搜索对应的企业员工或访客，选中成员，设置其身份，然后单击**确认**。
   
   @tab 分享链接邀请加入
   当企业成员数量较多，逐个添加工作量较大时，组织超级管理员或管理员可以通过分享链接，邀请企业成员加入组织。
   
   1. 在**成员列表**页签中，单击**分享**图标。
      ![Image=3488x640](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1fdf7ba3480d40f892d85af1d96b6ada~tplv-goo7wpa0wc-topic.webp)
   2. 成员访问对应的邀请链接，申请加入组织。
   3. 组织超级管理员或管理员在**组织成员管理**的**申请管理**页面，通过成员的加入申请。
      ![Image=500x184](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/01d95aa370484752a013cde546f7b85a~tplv-goo7wpa0wc-topic.webp)
   ::::   


### 4 加入工作空间 {#ce464cb8}

工作空间所有者和管理员登录扣子编程，邀请组织成员加入到工作空间中。

1. 在页面左上角展开空间下拉列表，单击目标工作空间右侧的管理图标。
2. 在顶部单击**成员管理**页签，在右上角单击 **+ 添加成员**。在搜索框中输入用户名搜索对应的企业员工或访客，选中成员，设置其身份，然后单击**确认**。
   ![Image=785x117](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ba3e7164c9d54401b60be59a8bb21285~tplv-goo7wpa0wc-topic.webp)   


## 后续操作 {#b571a266}

从零搭建智能体和应用：[开发儿童绘本制作工具](/guides/create_picture_book_generator)
