> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Credit 额度规则

组织的额度以 Credit 计量。全部 Credit 存放在组织级的 Credit 账户中，由组织成员共用。成员调用模型时，平台先按模型定价算出费用，再折算为 Credit 从该账户扣减。

## 计量口径

调用产生的消耗按 1 元 = 1,000,000 Credit 折算。各模型的单价见[定价详情](/docs/zh/guides/pricing/details)，单价乘以 1,000,000 即为对应的 Credit 消耗量。

到账的 Credit 数量由合同约定的价格与折扣确定，开通与发放流程见[开通企业套餐](/docs/zh/guides/organization/subscribe)。

## Credit 的有效期

Credit 的有效期为合同到期日之后 180 天。到期未使用的 Credit 自动失效且不可恢复。账户中存在多笔 Credit 时，平台按到期时间由近及远依次扣除。

## 项目与成员的额度上限

Credit 账户由全体成员共用。在此基础上，主账号可以为项目、以及项目中的个别成员设置月度 Credit 上限，用于约束用量分布。上限只约束 Credit 用量，不影响速率限制。

* **项目月度上限**：默认不设置，即该项目不单独受限。设置后，项目当期用量达到上限时，该项目下的所有 API Key 停止调用。
* **成员在项目内的月度上限**：默认不设置，即该成员仅受所在项目的上限约束。设置后，该成员在该项目下的 API Key 达到上限时停止调用，项目内其他成员不受影响。

上限的统计周期为自然月，每月 1 号 00:00 重置。月中启用上限时，当月按完整上限计算，不按剩余天数折算；月中修改上限值时，已用量不清零、周期不重置，新的上限值直接减去已用量。

项目上限之和可以超过 Credit 账户余额，成员上限之和也可以超过所在项目的上限，实际可用额度取其中最紧的一项。

## 单次调用的扣减上限

一次调用实际可扣减的 Credit 不超过以下三者中的最小值：

```text theme={null}
min(Credit 账户余额, 项目当期剩余上限, 成员当期剩余上限)
```

本次调用的用量超过该值时，调用被拒绝，且不产生扣费。

## 额度不足时的返回

| 情况            | 状态码 | 错误标识                                   | 恢复方式                     |
| ------------- | --- | -------------------------------------- | ------------------------ |
| Credit 账户余额不足 | 402 | `insufficient_credit`                  | 联系销售补充 Credit            |
| 项目达到月度上限      | 429 | `project_credit_limit_exceeded`        | 由主账号调高项目上限，或等待下月 1 号重置   |
| 成员在项目内达到月度上限  | 429 | `member_project_credit_limit_exceeded` | 由主账号调高该成员的上限，或等待下月 1 号重置 |

额度上限与速率限制返回的状态码同为 429，收到 429 时请以错误标识区分两种情况，错误标识的对照见[错误码](/docs/zh/api-reference/error-codes)。速率限制本身的说明见[基本介绍](/docs/zh/guides/basic-concepts)。

## 查看用量

主账号在「组织管理 > 组织用量」查看整个组织的 Credit 消耗与调用明细，可按项目、成员与模型筛选并导出，详见[管理成员与项目](/docs/zh/guides/organization/manage)。

成员在「账户管理 > 使用详情」查看自己的调用明细，详见[创建并使用项目 API Key](/docs/zh/guides/organization/api-keys)。
