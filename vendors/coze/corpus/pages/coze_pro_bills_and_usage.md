> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

本文介绍如何查看账单、分账账单、账号积分消耗、成员积分消耗等信息，以及如何设置积分额度等相关操作。

## 查询账单 {#c9e25140}

### 查看总账单 {#7785e05f}

::::tabs
@tab 团队版、个人版
如果是扣子团队版和个人版套餐，需要通过**购买记录**自行查看和统计账单。

1. 在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)或[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的左下角，单击**积分**卡片。
2. 在**订阅管理**页面，单击**购买记录**，查看详细的记录。

@tab 企业版
:::tip 说明
当前企业版出账存在小时级的延时，例如 16:00～17:00 期间产生的费用，可能在 17:30:00 才出账并扣款。
:::

购买企业版后，你可以在火山引擎费用中心的[账单详情](https://console.volcengine.com/finance/bill/detail)页面，筛选产品为**扣子**、**扣子-三方插件**，查看扣子账单。其中，iSlide 、悠船、飞常准、天眼查等付费插件在账单中的产品名为**扣子-三方插件**。

账单详情说明，请参考[账单管理](https://www.volcengine.com/docs/6269/94010)。

![Image=571x286](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7704ccd52bd54d95bf6b64c29286816d~tplv-goo7wpa0wc-topic.webp)
::::

### 查看企业版分账账单 {#aaac0dd6}

购买企业版后，你可以通过分账账单功能，以**组织和工作空间**维度查看各个工作空间内资源用量和对应的分拆费用。

:::tip 说明
首次使用时，需要先开通分账账单功能。开通后，新生成的账单明细将生成对应的分账账单明细，开通前的存量账单明细无对应分账数据，数据最晚存在 2 天延迟。
:::

* **支持按组织和工作空间维度分账的费用**：任务编程费用、内置集成费用、模型费用、插件费用、语音通话费用、视频通话费用、声纹识别费用、语音合成费用和语音识别费用支持按照空间维度分账，但由于使用场景的多样性，不保证这些费用在所有场景下都能实现按组织和工作空间维度的分账。
* **不支持按组织和工作空间维度分账的费用**：购买套餐、购买积分、购买增购项（增购声音复刻-音色数量等）、扣子费用、知识库空间费用、购买商店模板费用等仅支持按账号维度查看。

支持按组织和工作空间维度分账的计费项，其拆分项标识为`[org:****]-[ws:****]` 或 `[org:****]`；不支持按组织和工作空间维度分账的计费项，其拆分项标识为 `[acc:2***]`。

:::tip 说明
如果要在分账账单中查看当前账号下的所有扣子账单，则需将分拆项名称或 ID 筛选项留空。
:::

* `[org:****]`：组织名称或组织 ID
* `[ws:****]`：工作空间名称或工作空间 ID
* `[acc:2***]`：火山账号 ID

你可以在火山引擎费用中心的[分账账单](https://console.volcengine.com/finance/bill/split-bill)页面，根据分拆项名称或 ID 筛选分账账单。筛选时，输入的值必须与分拆项的 ID 或名称完全匹配。常见的筛选格式为 `[org:组织名称]-[ws:工作空间名称]`、`[org:组织ID]-[ws:工作空间ID]`、`[org:组织名称]`、`[org:组织ID]`、`[acc:2***]`。

分账账单中的各个字段说明，请参考[分账账单](https://www.volcengine.com/docs/6269/177196)。

![Image=773x148](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1a22b0ee6231439580161a1e8e723017~tplv-goo7wpa0wc-topic.webp)

## 查看积分消耗明细 {#dec2911a}

各个订阅套餐均支持查看个人积分用量明细。

:::tip 说明
* 个人版、团队版支持近实时统计积分消耗情况。
* 企业版**积分消耗**页面仅展示预估值，实际扣减以火山账单为准。
* 如果是团队版、企业版，个人积分用量**按当前组织统计**；切换组织后，展示的个人积分用量也会相应变化。
:::

::::tabs
@tab 网页、桌面端
1. 在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)或[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的左下角，单击**积分**卡片。
2. 在**订阅管理**页面，单击**积分管理**，查看指定时间范围内积分总消耗以及积分消耗明细。

@tab 移动端
1. 在扣子 App 的右下角，单击**更多**。
2. 在订阅套餐卡片中，单击积分剩余比例。
3. 在**消耗明细**页签中，查看指定时间范围内积分总消耗以及积分消耗明细。
::::

![Image=500x277](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/190b399dc3d54af6bacaa809e1861c8f~tplv-goo7wpa0wc-topic.webp)

<!-- @cols-width: 100,183,572 -->
| **序号**  | **功能**  | **说明**  |
| --- | --- | --- |
| ①  | 剩余总积分  | 当前账号剩余总积分。  |
| ②  | 指定时间内消耗的积分  | 你可以选择默认时间段或自定义时间段，查看指定时间段内积分累计用量和明细。还可在明细列表中，单击**时间**列的 **↑↓** 图标，按时间排序积分消耗记录。 | \
| | | | \
| | | 企业版、团队版的企业超级管理员、管理员可在页面右上角单击**切换到企业消费**，查看指定时间内的总消耗，以及按组织、项目和成员维度查看累计积分消耗。  |
| ③  | 按使用来源查看积分消耗  | 个人版账户或者企业成员可以根据使用来源查看个人消耗。积分消耗会按使用来源归类展示，例如 **Agent 项目、扣子编程、云设备、其他**等，展开来源名称，会有更细化的分类。详细说明如下表所示。  |
| ④  | 按积分消耗量排序  | 在明细列表中，单击**累计积分消耗**列的 **↑↓** 图标，查看积分消耗最多的项目。  |
| ⑤  | 查看消耗明细  | 单击指定记录对应的统计，查看该项目每天的积分消耗。  |

根据项目类型查看个人积分消耗的详细说明如下表所示：

<!-- @cols-width: 131,765 -->
| **分类**  | **说明**  |
| --- | --- |
| Agent 项目  | 你可以按 Agent 或项目会话查看积分消耗情况，包括 Coze Agent、三方精选 Agent、Agent 项目等类型。打开具体 Agent 或项目后，可以查看该 Agent 或项目会话产生的积分消耗记录。例如： | \
| | | \
| | * 你在对话中输入的每条 Query，都会生成一条对应的积分消耗记录。 | \
| |    支持查看 2026 年 8 月 27 日之后产生的单条 Query 级别积分消耗明细。 | \
| | * 定时任务运行时，会生成对应的积分消耗记录。 | \
| | * 你在画布上进行音视频分离等付费操作时，会生成对应的积分消耗记录。 | \
| | | \
| | 如果需要排查某一次具体对话的积分消耗，可以在对话明细中单击**复制 ID**，将复制出的完整排查信息发送给扣子售后团队，以便查询更详细的消耗记录。联系方式请参考[获取帮助](https://docs.coze.cn/cozespace_help_and_support)。 | \
| | | \
| | ![Image=370x105](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/198774e20e8d42d6ba210f8206e650a9~tplv-goo7wpa0wc-topic.webp)  |
| 扣子编程  | 统计扣子编程相关项目产生的积分消耗，包括 AI 编程项目、低代码项目。支持以下两种查看维度： | \
| | | \
| | * **项目维度**：按项目统计积分消耗，包括智能体、工作流、应用、小程序、技能等的积分消耗。单击各个项目对应的**明细**，可查看产生积分消耗的具体计费项。 | \
| | * **功能维度**： 统计各个扣子编程功能的积分消耗，例如大模型、知识库等。 | \
| | | \
| | ![Image=354x91](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b10e808dfad841c787e777812a623f57~tplv-goo7wpa0wc-topic.webp)  |
| 旁听  | 统计会议旁听消耗的积分。  |
| 云设备  | 云电脑：按天统计云电脑消耗的积分。 | \
| | | \
| | 云手机：按天统计云手机消耗的积分。 | \
| | | \
| | ![Image=376x92](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/253957788f3e47b0ba40e0884f362b43~tplv-goo7wpa0wc-topic.webp)  |
| 其他  | 不在以上统计维度内的消耗记录。  |

> * 针对企业版用户，还可以跳转至火山引擎费用中心的[资源包管理](https://console.volcengine.com/finance/resource-package)页面，查看积分消耗情况。积分抵扣明细的各个字段说明，请参考[抵扣明细](https://www.volcengine.com/docs/6269/165227)。
> * 低代码项目积分消耗明细注意事项如下：
>    * **积分消耗**页面不包含知识库空间和声音复刻的积分消耗记录。
>    * **积分消耗**中会展示由智能体开发者承担费用的公共渠道消耗记录，不会展示由公共渠道创建者承担费用的公共渠道消耗记录。


## 查看企业多维度积分用量 {#hyYi3BIbh}

除上述账号维度的积分消耗外，企业超级管理员、管理员还可以按组织、空间、成员、项目等维度查看用量明细。

:::tip 说明
**套餐限制**：**团队高阶版、团队旗舰版、团队尊享版、企业标准版**、**企业旗舰版**
:::

### 查看组织维度的用量明细 {#cd9f3cc8}

1. 企业超级管理员、管理员在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)或[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的左下角，单击**积分**卡片。
2. 在**订阅管理**页面，单击**积分管理**。
3. 在页面右上角单击**切换至企业消耗**，然后在**组织维度**下，查看各个组织消耗的积分总用量以及近一年内每日积分消耗量。
   支持单击**积分消耗**列的 **↑↓** 图标，查看积分消耗最多的组织。
   ::::cols
   @col 50
   ![Image=3226x1063](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/187f75d207ac4f53a5d5c4c171083cf3~tplv-goo7wpa0wc-topic.webp)
   
   @col 50
   ![Image=382x320](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/9ff39f9750a247a79b97ecea44748712)
   ::::
4. 在**订阅管理**页面，单击**限额管理**，然后在**组织**页签下，查看各个组织消耗的积分总用量、月总量以及每日按功能模块分类的积分消耗明细。
   ::::cols
   @col 50
   ![Image=3200x878](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b8bf7c920a4d408eabc995af9a906d67~tplv-goo7wpa0wc-topic.webp)
   
   @col 50
   ![Image=383x325](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/0fe9aab3558d4d93be26377820e19c2e)
   ::::   


### 查看空间维度的用量明细 {#hJQxRPyBb}


1. 企业超级管理员、管理员在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)或[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的左下角，单击**积分**卡片。
2. 在**订阅管理**页面，单击**限额管理**，然后在**工作空间**页签下，查看各个空间消耗的积分总用量、月总量以及每日按功能模块分类的积分消耗明细。

::::cols
@col 50
![Image=3194x891](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/03d683ef6fd0417b88f5ee5569c9aa8c~tplv-goo7wpa0wc-topic.webp)

@col 50
![Image=382x321](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6a9af24700064c4eb23978db69a64c4f)
::::

### 查看成员维度的用量明细 {#hOHVs7Wgh}

企业超级管理员、管理员可以查看各个企业成员（包括超级管理员、管理员、员工、访客）和未加入企业用户的积分消耗情况，包括历史累计的积分用量、本月的积分用量以及每日按功能模块分类的积分消耗明细。

#### 用户范围 {#hMGMuRbSs}

**成员限额**页签中的用户包括企业成员和未加入企业用户。

* 企业成员：包括超级管理员、管理员、员工、访客。
* 未加入企业用户：企业版套餐存在如下情况。
   * 已在火山扣子控制台创建的成员，但还未加入企业。
   * 其他非企业成员，但是消耗了企业积分的用户。

#### 操作步骤 {#hs8P5p3vX}


1. 企业超级管理员、管理员在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)或[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的左下角，单击**积分**卡片。
2. 在**订阅管理**页面，单击**积分管理**。
3. 在页面右上角单击**切换至企业消耗**，然后在**成员维度**页签下，查看各个成员消耗的积分总用量以及近一年内每日积分消耗量。
   支持单击**积分消耗**列的 **↑↓** 图标，查看积分消耗最多的成员。
   ::::cols
   @col 50
   ![Image=3188x1043](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b4596de50bf947c8b6246e2c1b9e8e61~tplv-goo7wpa0wc-topic.webp)
   
   @col 50
   ![Image=292x233](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/eb470f9c33e34beb8f020b64bb28d2eb)
   ::::
4. 在**限额管理**>**成员**页签下，查看各个成员消耗的积分总用量、月总量以及每日按功能模块分类的积分消耗明细。
   ::::cols
   @col 50
   ![Image=3218x1428](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6a71dea8e402470ba9cfdbd3da49b2e9~tplv-goo7wpa0wc-topic.webp)
   
   @col 50
   ![Image=299x253](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2a37d04bf3aa46989bd38cb7d9bff29d)
   ::::   


### 查看项目维度的用量明细 {#hDGPnObBg}


1. 企业超级管理员、管理员在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)或[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的左下角，单击**积分**卡片。
2. 在**订阅管理**页面，单击**积分管理**。
3. 在页面右上角单击**切换至企业消耗**，然后**项目维度**页签下，查看各个项目消耗的积分总用量以及近一年内每日积分消耗量。
   支持单击**积分消耗**列的 **↑↓** 图标，查看积分消耗最多的项目。
   ::::cols
   @col 50
   ![Image=3244x1061](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5ae6e8fba3694293b2b09e557e059ebc~tplv-goo7wpa0wc-topic.webp)
   
   @col 50
   ![Image=309x261](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/bae4d2a4c592480abc3be0fbc36e0709)
   ::::   


### 查看计费项维度的用量明细（企业版） {#hRwnDl7bH}

购买企业版后，你可以在[火山引擎扣子控制台](https://console.volcengine.com/coze-pro/overview)的**用量统计**页面，查看各个计费项的用量。

* **编程项目**：查看指定时段内，大语言模型、生图模型、语音模型、联网搜索等各个内置集成服务的使用量。
* **低代码项目**：查看指定时段内，低代码项目相关的大模型用量、智能语音用量、实时音视频用量、插件用量、知识库用量、大模型 TPM 保障额度、成员用量、记忆库用量。
* **扣子罗盘**：查看指定时段内，扣子罗盘智能调优功能消耗的积分。

![Image=611x259](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f642b0571038440285b3cf18dc478733~tplv-goo7wpa0wc-topic.webp)

## 导出企业积分消耗明细 {#cfe19d09}

:::tip 说明
* **套餐限制**：**企业标准版、企业旗舰版**
* 单次最多可导出 60 天的账单数据。
:::

企业超级管理员、管理员可以导出积分消耗明细表格到本地。

在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)或[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的左下角，单击**积分**卡片，然后在**积分消耗**页签下，选择成员、组织或项目维度，单击**用量账单导出**。

系统将根据你选择的维度和时间范围，导出对应的积分消耗明细表。

## 设置企业积分额度限制 {#hiP1c3Kle}

:::tip 说明
**套餐限制**：**团队高阶版、团队旗舰版、团队尊享版、企业标准版、企业旗舰版**
:::

企业超级管理员、管理员可以设置组织、空间、成员维度的积分额度限制。此处以企业旗舰版套餐的界面为例。

### 额度限制规则 {#0e3e23b2}

企业超级管理员、管理员可以为组织、空间或成员开启累计额度限制和每月额度限制。

:::tip 说明
系统会**同时执行你所设置的所有额度限制**，其中任一额度达到上限时，其对应范围内的成员均将无法继续使用需要消耗积分的扣子功能。
:::

<!-- @cols-width: 159,448,297 -->
| **额度限制类型**  | **配置说明**  | **重置机制**  |
| --- | --- | --- |
| 累计额度限制  | 开启额度限制后，当该组织、空间或成员的积分使用量达到额度上限值时，将无法继续使用需要抵扣积分的扣子功能。  | 无自动重置，需超级管理员手动调整额度。  |
| 每月额度限制  | 开启额度限制后，当该组织、空间或成员在当月的积分使用量达到额度上限值时，当月将无法继续使用需要抵扣积分的扣子功能。  | 每月 1 号自动重置当月额度。  |

### 设置组织积分额度限制 {#eab15e3f}

1. 企业超级管理员、管理员在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)或[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的左下角，单击**积分**卡片。
2. 在**订阅管理**页面，单击**限额管理**。
3. 在**组织**页签下，单击目标组织对应的**编辑**，设置积分额度限制。
   ![Image=235x200](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bc6a77814ab84d0fa6fad88dd85edd96~tplv-goo7wpa0wc-topic.webp)   


### 设置空间积分额度限制 {#82366f35}


1. 企业超级管理员、管理员在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)或[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的左下角，单击**积分**卡片。
2. 在**订阅管理**页面，单击**限额管理**。
3. 在**工作空间**页签下，单击目标空间对应的**编辑**，设置积分额度限制。
   ![Image=224x194](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5ed06ac6a54f47ef9b3321007ed32ce3~tplv-goo7wpa0wc-topic.webp)   


### 设置成员积分额度限制 {#eb6eeb46}

企业超级管理员、管理员可以为企业成员（管理员、员工、访客）设置积分额度限制，来管理企业成员的积分用量，避免成员过度消耗积分。

:::tip 说明
不支持为超级管理员配置积分额度限制。
:::

企业超级管理员、管理员可以在[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)中，单击**积分**卡片，然后在**限额管理**>**成员限额**页签下，通过如下方式为成员配置积分额度限制。

* 成员维度：为单个成员或批量为多个成员设置积分额度限制。
* 角色维度：为各个角色设置积分额度限制。如果同时设置了成员积分限额和角色积分限额，那么将以成员维度的积分限额为准。

::::tabs
@tab 配置角色积分额度
在**角色限额配置**区域中，单击目标角色对应的**编辑**图标，为各个角色设置积分额度限制。例如为管理员角色设置积分额度限制后，那么所有管理员将统一遵循该限额。

![Image=404x123](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/53c56e8b891843968e18ec24ec2e98ae~tplv-goo7wpa0wc-topic.webp)

@tab 配置单个成员积分额度
在成员用量列表中，单击目标成员对应的**编辑**，为其设置积分额度限制。

* **跟随角色**：跟随角色积分额度限制。
* **不限额**：不设置积分额度。
* **用户限额**：设置成员的累计额度限制值、每月额度限制值。

![Image=474x175](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/643ab83719064839a6e8e4883fd503ef~tplv-goo7wpa0wc-topic.webp)

@tab 批量配置成员积分额度
在成员用量列表的右上角，单击**批量配置**，然后勾选目标成员，为其设置积分额度限制。 单次最多勾选 100 个成员。

* **跟随角色**：跟随角色积分额度限制。
* **不限额**：不设置积分额度。
* **用户限额**：设置成员的累计额度限制值、每月额度限制值。

![Image=488x139](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/483c46fc31a94731ba897d7c38759ebf~tplv-goo7wpa0wc-topic.webp)
::::

## 查看单次调用的积分消耗明细（低代码项目） {#34c3f40e}

在[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)的低代码项目中，使用模型、插件、工作流、智能语音、知识库、记忆库等扣子付费资源，均会产生相应的费用。扣子支持统计并展示单次智能体对话、工作流试运行所涉及的扣子付费资源、计费项、消耗的积分等信息。该积分统计存在一定的延时，详情请参考[出账延迟说明](/coze_pro/bills_and_usage#9d2ae772)。

:::tip 说明
此处展示的积分预估值，实际扣减以火山账单为准。如何查看账单，请参考[查看总账单](/coze_pro/bills_and_usage#7785e05f)。
:::

### 查看入口 {#a6dd15e0}

你可以在如下页面查看单次智能体对话、工作流试运行所消耗的积分。

<!-- @cols-width: 115,395,425 -->
| **查看入口**  | **说明**  | **示例**  |
| --- | --- | --- |
| 低代码智能体调试区  | 在智能体编排页面与智能体对话后，可以查看单次对话涉及的扣子付费资源、计费项、单价、用量及消耗的积分。 | ![Image=2549x691](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/60ba29282ca64a3794734176776a40f8~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | 1. 单击**调试**图标。 | | \
| | 2. 选择目标对话。 | | \
| |    筛选对话名称，可以查看历史对话的积分消耗情况。 | | \
| | 3. 单击**积分**。 | | \
| | 4. 查看此次对话的积分消耗情况。  | |
| 低代码工作流调试区  | 在工作流编排页面，可以查看单次试运行涉及的扣子付费资源、计费项、单价、用量及消耗的积分。 | ![Image=2544x810](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/22f76dc0f1d44d0eb54cca8b6483ca97~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | 1. 单击**调试**图标。 | | \
| | 2. 选择目标试运行时间。 | | \
| |    筛选试运行时间，可以查看历史试运行的积分消耗情况。 | | \
| | 3. 选择**积分**。 | | \
| | 4. 查看此次试运行的积分消耗情况。  | |

### 出账延迟说明 {#9d2ae772}

单次智能体对话、工作流试运行所展示的积分消耗明细存在一定延迟，并且不同付费资源的延迟时间不同。

* 智能语音相关功能的积分用量展示存在小时级别延迟。
   智能语音涉及声纹识别、语音合成、语音识别、音频通话、视频通话等计费场景，详细的计费项说明，请参考[音视频费用](/coze_pro/asr_tts_fee)。
* 插件、模型、知识库、记忆库等功能消耗的积分展示存在秒级延迟。
