> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子项目默认使用云盘文件夹作为工作目录，用来存放项目中的资料、文件和生成产物。现在，创建项目时也支持选择你电脑上的本地目录作为工作目录。选择本地目录后，项目里的 Agent 可以围绕这个目录读取、分析、编辑文件，并将生成结果保存到这个目录中，无需先把文件上传到云端。

## 什么时候在项目中选择本地目录 {#hAAMXuJmE}

大多数情况下，创建项目时选择云盘文件夹即可，不需要额外配置。

如果你有下面这些需求，可以选择本地目录作为项目工作目录。

* **你电脑上已经有现成的东西，不想搬迁**
   * 一个写了一半的代码仓库，想让 Agent 接着改。
   * 一份本地积累的资料目录，想让 Agent 帮你整理分析。
   * 文件太大（视频、数据集），上传云盘不现实。
* **希望产物直接保存在本地目录**
   * 让 Agent 整理资料、生成报告、修改代码后，结果直接落在本地文件夹中。
   * 需要继续使用本地工具打开、编辑或运行这些文件。

## 使用须知 {#hETcrrDgl}

**选择本地目录作为工作目录后**，项目里的 Agent 可以在你授权后围绕该目录处理文件。使用前，建议先了解以下限制和安全规则。

<!-- @cols-width: 100,724 -->
| **须知**  | **说明**  |
| --- | --- |
| 使用限制  | * 在项目中，你需要 @Agent，让指定 Agent 处理任务。 | \
| | * 一个项目只能绑定一个本地目录，创建后不支持更换目录。 | \
| | * 目前只能在桌面端创建使用本地目录作为工作目录的项目。手机端和网页端可以查看、使用已有项目，但不能新建。 | \
| | * 使用本地目录作为工作目录时，项目中只能添加本地 Agent 或云端 Agent，不支持添加人类成员。 | \
| | * 如果你删除、移动或重命名了本地目录，项目不会被同步删除，但会导致项目文件相关功能不可用。 | \
| | * 创建项目后，建议开启“合盖不休眠”。电脑关机、断网、进入休眠状态，或 bridge 服务停止运行，电脑与扣子的连接会断开。  |
| 安全提醒  | * 本地目录文件始终在你电脑上，不会上传到云端。 | \
| | * **你始终拥有最终控制权**：Agent 在访问本地文件夹、执行敏感指令前，会先请求你的授权。你可以随时查看、修改或撤销已授予的权限。 | \
| | * **默认最小权限**：Agent 只能在项目绑定的工作目录中操作文件，并会按任务需要申请必要权限。不建议让 Agent 处理高度敏感、涉密或受严格合规限制的数据。  |

## 前提条件 {#hFPT2lzJH}

创建使用本地目录作为工作目录的项目时，需要通过**扣子桌面端**与你的电脑建立连接。安装并登录桌面端后，系统会自动在你电脑上运行一个后台服务（coze-bridge）。通常情况下，你不需要额外配置，连接会自动建立并保持。

> coze-bridge 是运行在你电脑本地的连接组件，用于在授权后连接扣子云端服务，完成任务下发、执行状态同步等必要通信。它是扣子桌面端用于支持本地目录项目的基础服务。

## 选择工作目录 {#hDltT09s0}

你可以参考如下步骤，在桌面端创建使用本地目录作为工作目录的项目。

1. 在桌面端的**项目**区域，单击+ > **新建项目**。
2. 设置项目名称，选择**本地目录**，然后选择一个本地文件夹。
3. 单击**创建项目**。
   ::::cols
   @col 49
   ![Image=313x263](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9bdc8768a7a54bcdb9eb74ccea732251~tplv-goo7wpa0wc-topic.webp)
   
   @col 50
   ![Image=325x221](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/646fcaff33b64ef094a3209c1defe83f~tplv-goo7wpa0wc-topic.webp)
   ::::
   创建完成后，进入项目的**文件**页签。你将看到所选本地目录中的文件和文件夹。后续 Agent 会围绕这个本地目录工作，读取、处理文件以及保存生成的产物。
   ![Image=346x262](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7855ae4e4b7142e49c5dc1f80a66c306~tplv-goo7wpa0wc-topic.webp)   


## 怎么使用本地工作目录 {#hC38K5qqv}

选择本地目录后，该目录会作为项目工作目录。项目里的 Agent 会默认围绕这个目录工作，上传的附件、生成产物，都会保存到这个工作目录中。

### 下达任务并完成授权 {#hX8XnfSxF}

在项目中，你可以@ Agent，告诉 Agent 需要完成的任务，例如`读一下 README.md 的内容`。

为了保护你的本地文件安全，Agent 访问或操作本地文件夹前，需要先获得你的授权。

当 agent 首次操作一个未授权的文件夹时，对话中会出现授权卡片。授权卡片会说明本次请求的操作内容、目标设备、目标文件夹和请求原因。你同意后，Agent 才会继续执行对应文件操作。

![Image=300x279](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3b729414f8a2498e888bc6ce347dfe71~tplv-goo7wpa0wc-topic.webp)

### 操作本地文件 {#hWVwxo6v2}

你可以让 Agent 在项目工作目录中处理本地文件和文件夹，包括查看、分析、编辑、移动文件。

常见指令示例：

* **查看和查找文件**：“`帮我在工作目录里找到最近修改过的 PDF。`”
* **读取和分析文件**：“`帮我读取工作目录下的需求文档，并总结重点。`”
* **创建和编辑文件**：“`帮我把整理结果保存到指定文件夹。`”
* **移动和整理文件**：“`帮我把图片文件移动到 images 文件夹中。`”

![Image=300x279](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3b729414f8a2498e888bc6ce347dfe71~tplv-goo7wpa0wc-topic.webp)

:::notice 注意
对于移动文件等敏感操作，Agent 执行前会根据权限情况向你发起确认请求；你同意后，任务才会继续。
:::

### 多 Agent 协作 {#hteXYIp6S}

项目中可以加入多个 Agent，让它们围绕同一个工作目录分工配合。例如：

* 一个 Agent 改代码，另一个 Agent 做代码评审
* 一个 Agent 整理数据，另一个 Agent 基于整理结果生成报告
* 一个 Agent 写功能，另一个 Agent 做测试

你可以在**项目设置 > Agent 管理**中，单击**添加**，添加对应的 Agent。

::::cols
@col 50
![Image=332x214](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5de0cc103333498c8176a5cae3615ca4~tplv-goo7wpa0wc-topic.webp)

@col 50
![Image=980x528](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ff0981e8bc134c45b5ba9942d597a851~tplv-goo7wpa0wc-topic.webp)
::::

### 执行 Shell 命令 {#hzNFK8dUK}

Shell 命令可以理解为本地电脑上的命令行操作。创建项目后，Agent 可以根据任务需要执行部分 Shell 命令，帮助你处理文件、运行脚本、调用工具或进行数据处理。

常见可执行的操作包括：

* **文件操作**：创建、读取、编辑文件和目录，查找文件，压缩或解压文件。
* **开发相关**：运行 Python、Node.js 等脚本，安装依赖，执行 Git 操作，管理或部署项目。
* **本地电脑操作**：执行本地命令、读取或写入授权路径下的文件，必要时进行截图等操作。
* **网络相关**：通过 curl 请求 API，下载文件，进行简单的网络连通性测试。
* **数据处理**：清洗数据、转换格式、统计计算，或生成图表。

![Image=383x244](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/17b5818fee074ab4a963ad41751ee455~tplv-goo7wpa0wc-topic.webp)

以下命令或操作会受到限制：

* 需要交互式输入的命令，例如 ssh、vim 等。
* 需要手动输入密码的命令，例如部分 Git 推送、系统提权命令等。
* 访问未授权路径的命令。
* 可能影响文件安全、系统设置或网络安全的高风险命令。

对于受限制或高风险的命令，扣子会根据实际情况提示你补充信息、完成授权或确认是否继续。只有在满足权限要求后，Agent 才会继续执行。

如果你不确定某条命令的影响，可以选择拒绝，并让 Agent 解释命令的作用或换一种更安全的处理方式。

## 场景演示 {#hbH7oYErU}

### 场景1：​继续开发本地代码项目 {#hWOi53ez1}

小李在本地电脑上开发一个代码项目，并在扣子项目中选择该代码仓库作为工作目录。离开电脑后，他突然想到某个 Bug 的解决方案，可以打开手机上的扣子 App，进入对应的扣子项目，把修复思路告诉 Agent。Agent 会在本地工作目录中读取代码、修改文件，并根据需要运行测试。

::::cols
@col 50
```Plain Text
@Agent 我想到登录失败的原因了，应该是 token 过期后没有清理缓存。帮我在本地目录里修一下，并跑一下相关测试。
```

@col 50
![Image=1351x986](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7a7f9f6353194b8abd69c95800c2ab32~tplv-goo7wpa0wc-topic.webp)
::::

### 场景2：​分析本地运营数据并生成活动方案 {#hu1W9dcWS}

运营人员小李在电脑上保存了一些不方便上传到云端的运营数据，比如用户分层、活动转化、渠道投放、订单明细等。你可以在创建项目时选择这些数据所在的本地目录作为工作目录，让 Agent 基于本地工作目录分析数据，并基于分析结果生成运营活动方案。

::::cols
@col 51
```Plain Text
@Agent 帮我分析工作目录下最近三个月的活动转化数据，找出高转化用户特征，并生成一份下个月的会员召回活动方案
```

@col 48
![Image=1076x554](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e0f7e540f132488597593cf2ea75ca3e~tplv-goo7wpa0wc-topic.webp)
::::

### 场景3：​多个 Agent 分工协作 {#hZ4iUP5P9}

一个扣子项目可以加入多个 Agent，让它们围绕同一个工作目录配合完成任务。

::::cols
@col 50
```Plain Text
@开发 Agent 把订单列表开发代码里的状态筛选改成多选；完成后@ 评审 Agent 检查这次改动有没有影响现有筛选逻辑。
```

@col 50
![Image=1324x778](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/07944e0551c148038812ac59494963e9~tplv-goo7wpa0wc-topic.webp)
::::

## 常见问题 {#hjoxU32rY}

[云盘文件夹和本地目录作为工作目录有什么区别？](/cozespace_coze_app_faq#hjLBswMKy)

[本地连接断开了，如何处理？](/cozespace_coze_app_faq#hpBzD2wDU)

[项目本地目录和本地设备有什么区别？](/cozespace_coze_app_faq#hBVQoa4BM)
