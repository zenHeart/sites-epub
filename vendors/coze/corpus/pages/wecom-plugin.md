> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

[企业微信插件](https://www.coze.cn/skills?tab=space&capability=plugin&plugin_share_pid=7678912742081757238)为 Agent 提供企业微信 CLI 能力。完成一次企业微信授权后，授权信息会在当前账号下共享，账号内所有 Agent 都可以复用同一份连接，无需为每个 Agent 重复登录、扫码或配置凭证。Agent 可以根据你的指令操作企业微信中的消息、邮件、文档、表格、待办、日程、会议、微盘和通讯录等内容。

:::notice 注意
* **暂不支持在企业微信中与 Agent 对话。​**企业微信插件提供的是 CLI 办公操作能力，不会为 Agent 创建企业微信聊天渠道。
* 使用此插件，必须在扣子中和安装了此插件的 Agent 对话，在企业微信中创建的机器人仅用于执行 CLI 的身份认证，和企业微信机器人对话不会获得响应。
:::

## 能做什么 {#hTIzGHkQN}

<!-- @cols-width: 139,681 -->
| **能力**  | **支持的操作**  |
| --- | --- |
| 邮件  | 发送、回复和转发邮件，搜索邮件并获取邮件内容详情。  |
| 文档与文档管理  | 新建、导入、读取、追加和覆盖写入在线文档；搜索多种文档，管理文档名称、成员权限与加入规则。  |
| 在线表格  | 新建在线表格，导入 CSV 或 Excel，读取、修改和追加内容，并管理子表。  |
| 智能表格  | 创建智能表格，管理子表、字段、记录、视图和图表，并修改行列样式。  |
| 智能文档  | 创建智能文档，获取和编辑页面内容，读取内置数据表信息。  |
| 待办  | 创建、读取、更新和删除待办，分派参与人并完成待办。  |
| 日程与会议  | 管理日程和参与人，查询多人忙闲与会议室；创建、取消或更新预约会议，并读取会议纪要和转写原文。  |
| 微盘  | 搜索微盘文件，读取文件基本信息，上传和下载文件。  |
| 通讯录  | 按姓名、拼音或别名搜索成员，获取成员基本信息，用于日程、会议等多人协作场景。  |

完整能力及最新命令以[企业微信 CLI 官方仓库](https://github.com/WecomTeam/wecom-cli)为准。

:::notice 注意
**权限由所在企业统一控制。​**插件实际可用的能力和可访问内容，取决于企业管理员授予的应用权限以及目标资源本身的成员权限；权限不足时，请联系管理员或资源所有者处理。
:::

## 如何安装和使用 {#hBdP08L2V}

1. 打开插件商店，找到[企业微信插件](https://www.coze.cn/skills?tab=space&capability=plugin&plugin_share_pid=7678912742081757238)。
2. 单击**连接**，根据页面提示完成企业微信授权。
3. 授权成功后，回到扣子，在企业微信插件页面单击**添加**，并选择要使用插件的 Agent。
4. 直接在安装了企业微信插件的 Agent 对话中提出企业微信相关任务；无需为每个 Agent 重复授权。

例如，和企业微信 Agent 对话，让它帮忙创建一个待办“跟供应商聊聊”。

::::cols
@col 25
![Image=1266x1277](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bd0d00cae97b49ea88d4dc9f18f2ca23~tplv-goo7wpa0wc-topic.webp)

> 打开企业微信插件

@col 25
![Image=1344x1418](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c0efcec3b76a40bd85273087bea3e2c6~tplv-goo7wpa0wc-raw.image)

> 根据页面提示授权

@col 25
![Image=1652x1626](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5b4dd34ee53d469ca4b441836115fc25~tplv-goo7wpa0wc-raw.image)

> 为 Agent 添加插件

@col 25
![Image=1280x1256](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7bcc2ff910ab4584bdb6382fb35c6e36~tplv-goo7wpa0wc-topic.webp)

> 测试插件是否成功连接
::::

## 你可以这样用 {#hsqG4gUrB}

* **处理合同邮件：**`搜索主题包含“合同审批”的邮件，汇总最近一周的重要进展并起草回复。`
* **编写项目周报：**`新建项目周报在线文档，写入本周进展、风险和下周计划。`
* **整理 Excel 数据：**`将 Excel 导入在线表格，并新增负责人和完成状态两列。`
* **创建客户跟进表：**`新建智能表格，记录客户名称、跟进阶段、负责人和下次联系时间。`
* **分配合同待办：**`为张三创建明天下午到期的供应商合同复核待办。`
* **预订会议室：**`查询王芳、李明和我明天下午的共同空闲时间，并预订一间六人会议室。`
* **整理会议结论：**`查找昨天产品评审会的会议纪要和转写原文，整理决策项与待办事项。`
* **查找预算文件：**`在微盘中搜索“年度预算方案”，下载最新版本。`
