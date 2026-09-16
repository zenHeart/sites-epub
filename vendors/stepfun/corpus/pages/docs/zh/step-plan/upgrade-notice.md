> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Step Plan 升级公告

Step Plan 自 2026 年 6 月 18 日起升级为 **Credit 月池** 计费，新套餐为 **Token Plan**。旧版 **Coding Plan** 当前周期权益不受影响；已开启自动续费的用户可继续按 Coding Plan 自动续订，未开启自动续费的用户到期后需升级至 Token Plan 才能继续使用。升级至 Token Plan 为单向操作，确认后不可回退。

## 本次变更

Token Plan 在计量单位、套餐方式与超额承接三方面进行了升级：

| 改动项  | 旧版 Coding Plan | 新版 Token Plan                  |
| ---- | -------------- | ------------------------------ |
| 计量单位 | 按请求次数（Prompt）  | Credit（统一计费单位，1M Credit = ¥1）  |
| 套餐方式 | 5 小时 / 周限额     | Credit 月池：额度按月发放，月内任意时段消耗，月末清零 |
| 超额承接 | 额度用尽即切断        | 加油包当月加购补充额度，周期单独 30 天          |

新套餐的档位价格、Credit 额度、加油包与计费规则，详见 [Step Plan 概述](/docs/zh/step-plan/overview)。

## 旧套餐用户须知

如果您正在使用旧版 Coding Plan，当前周期内的额度、权益与到期时间保持不变，可正常使用至周期结束。后续是否需要升级，取决于您是否开启了自动续费：

* **已开启自动续费**：将继续按旧版 Coding Plan 自动续订下一周期，无需升级即可持续使用。您也可以随时主动升级至 Token Plan。请注意，续费扣款失败会导致 Coding Plan 被取消。Coding Plan 被取消后无法重新订购，如需继续使用 Step Plan，只能购买新版 Token Plan。若希望继续使用 Coding Plan，请在每次续费日前确认绑定的支付方式可用、额度充足。
* **未开启自动续费**：Coding Plan 不支持手动续订，当前周期到期后如需继续使用 Step Plan，需升级至新版 Token Plan。

<Warning>
  升级至 Token Plan 为单向操作，确认后无法回退至旧版 Coding Plan。Coding Plan 一旦到期未续或被取消，均无法重新订购，届时只能购买 Token Plan，建议及时处理以免服务中断。
</Warning>

## 升级到 Token Plan

旧套餐用户可在控制台主动升级至新版 Token Plan，升级规则如下：

* **到期时间保持不变**：原本几号到期，升级后仍是几号到期。
* **完整额度发放**：升级后立即按新套餐当月完整 Credit 额度发放，不按剩余天数折算。
* **自动续费选项**：若升级前已开启自动续费，升级时会展示续费勾选项（默认勾选），您可选择保留或取消；若升级前未开启自动续费，则不展示该选项。目前暂不支持手动开启自动续费。
* **单向操作**：升级确认后不可回退至旧套餐。
* **暂不支持升级同时升档**：本次升级仅完成「旧套餐 → 新套餐同档」切换，不支持在升级的同时变更档位。如需更高档位，请在升级完成后再进行档位升级（见下文）。

## 档位升级

完成升级后，您可在周期内将当前 Token Plan 档位升级至更高档位，按剩余时间比例补差价：

* **补差价金额** = 原档位价格 ×（1 − 已用时间 / 总周期），仅就尚未使用的周期部分计算差价，不涉及 Credit 余量折算。
* 升级后立即按新档位刷新整月 Credit。
* 升档约束：新档位价格须不低于原档位价格，且新档位周期须不短于当前剩余权益时间。

以上规则的具体金额与展示，均以控制台订阅页实际为准。

## 常见问题

<AccordionGroup>
  <Accordion title="旧套餐（Coding Plan）到期后还能继续用吗？">
    取决于是否开启了自动续费。已开启自动续费的用户，会继续按旧版 Coding Plan 自动续订下一周期，无需升级即可继续使用；未开启自动续费的用户，Coding Plan 不支持手动续订，到期后需升级至 Token Plan 才能继续使用。
  </Accordion>

  <Accordion title="我开启了 Coding Plan 自动续费，会被强制升级到 Token Plan 吗？">
    不会。只要自动续费正常完成，您会继续按旧版 Coding Plan 自动续订，是否升级至 Token Plan 完全由您决定。但如果续费扣款失败，Coding Plan 会被取消，且无法重新订购，此后只能购买 Token Plan。
  </Accordion>

  <Accordion title="自动续费扣款失败会怎样？">
    Coding Plan 将被取消。Coding Plan 被取消后无法重新订购，如需继续使用 Step Plan，只能购买新版 Token Plan。建议提前确认绑定的支付方式可用、额度充足。
  </Accordion>

  <Accordion title="升级会改变我的到期时间吗？">
    不会。升级后到期时间与原套餐保持一致，原本几号到期仍是几号到期。
  </Accordion>

  <Accordion title="升级后我的 Credit 会按剩余天数折算吗？">
    不会。升级后立即按新套餐当月完整额度发放，与升级时点在周期内的位置无关。
  </Accordion>

  <Accordion title="升级可以回退到旧套餐吗？">
    不可以。升级为单向操作，确认后无法回退至旧版 Coding Plan。
  </Accordion>

  <Accordion title="可以在升级的同时升档吗？">
    暂不支持。本次升级仅完成「旧套餐 → 新套餐同档」切换。如需更高档位，请在升级完成后再单独进行档位升级，届时按剩余时间比例补差价。
  </Accordion>

  <Accordion title="1M Credit 等于多少钱？">
    Credit 与支付金额按 1M Credit = ¥1 换算。各档位的 Credit 月度额度与价格，详见 [Step Plan 概述](/docs/zh/step-plan/overview#套餐档位)。
  </Accordion>
</AccordionGroup>

更多关于 Credit、月池、加油包与档位的说明，请参阅 [Step Plan 概述](/docs/zh/step-plan/overview)。
