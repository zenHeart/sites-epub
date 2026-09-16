> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 组织与项目

组织让一个团队共用同一份额度调用模型。企业完成企业认证后获得一个组织，开通企业套餐后，Credit 发放至组织的 Credit 账户。团队成员受邀加入组织，在项目下创建 API Key 调用模型，产生的费用统一从组织的 Credit 账户扣减，无需为每位成员单独充值。开通流程见[开通企业套餐](/docs/zh/guides/organization/subscribe)。

## 账号与空间

一个账号对应一位使用者。账号可以在个人空间与组织空间之间切换，两个空间的 API Key、额度与用量相互独立。

| 空间   | 使用的 API Key   | 费用承担方         |
| ---- | ------------- | ------------- |
| 个人空间 | 账号自己的 API Key | 账号自身          |
| 组织空间 | 各项目下的 API Key | 组织的 Credit 账户 |

切换空间的入口位于控制台右上角的「用户中心 > 空间切换」。账号完成企业认证，或被邀请加入某个组织后，该入口才会出现。

一个账号可以同时属于多个空间，例如在本企业的组织中是主账号，同时又是合作方组织的成员。

## 组织的构成

| 概念      | 说明                                  |
| ------- | ----------------------------------- |
| 组织      | 团队的容器，持有一个 Credit 账户，账户中的额度由全体成员共用  |
| 主账号     | 完成企业认证并开通企业套餐的账号，负责管理组织的成员、项目与额度    |
| 成员      | 由主账号邀请加入组织的账号，在所参与的项目下调用模型          |
| 项目      | 组织内的分组单位，用于隔离 API Key 并分配 Credit 额度 |
| API Key | 调用凭证，归属于某位成员在某个项目下，每位成员在每个项目中最多创建一个 |

组织下的默认项目不支持删除。主账号可以按业务线、团队或运行环境另行创建项目，并控制每个项目的成员与额度上限，详见[管理成员与项目](/docs/zh/guides/organization/manage)。

成员需先被添加到项目，才能在该项目下创建 API Key。

## 组织之间相互独立

组织之间的 Credit、成员、项目与额度上限均不互通。一个账号可以同时加入多个组织，在每个组织中使用该组织自己的额度。

## 调用方式

项目下 API Key 的调用方式与个人 API Key 一致，不需要额外传递组织或项目标识。平台按 API Key 的归属结算费用，并把每次调用计入对应的项目与成员。创建 API Key 与发起调用的步骤见[创建并使用项目 API Key](/docs/zh/guides/organization/api-keys)，额度的折算与上限规则见 [Credit 额度规则](/docs/zh/guides/organization/credits)。
