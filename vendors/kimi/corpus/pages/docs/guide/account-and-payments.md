> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 账号与财务

> 查看 Kimi 开放平台的充值、余额、赠送金、发票、账单和企业实名认证等账号与财务问题。

<AccordionGroup>
  <Accordion title="如何充值？">
    * 个人用户充值：请先进行个人认证，然后在用户充值页面进行在线充值，在线充值支持微信/支付宝扫码支付两种方式，充值成功后会按照您的累积充值金额进行用户等级调整；
    * 企业用户充值：请先进行企业认证，企业认证通过后，您可以选择以下两种方式充值：
      1. **在线充值**：支持微信/支付宝扫码支付，充值成功后立即到账，充值成功后会按照您的累积充值金额进行用户等级调整；
      2. **银行对公汇款**：平台会为您提供专属收款账号，请使用与实名认证主体一致的银行账户进行汇款。线下对公汇款预计1-5个工作日到账（具体到账时间以银行的实际到账时间为准），我方银行账户到账后，转账充值金额将在10分钟左右自动转入您的账户，充值成功后会按照您的累积充值金额进行用户等级调整。
  </Accordion>

  <Accordion title="如何控制成本、设置消费上限？ ">
    在使用大模型进行代码生成时，由于模型的随机性和复杂性，可能需要多次尝试才能生成符合预期的代码。编程工具会自动进行多轮重试和调用，这可能导致 token 用量快速增长。为了更好地控制成本和使用体验，我们建议您注意以下几点：

    * **预算控制**
      * **设置日消费上限**：在使用前，请前往 [Kimi 开放平台项目设置](https://platform.kimi.com/console/projects/settings) 配置「项目日消费预算」。一旦达到预算上限，系统将自动拒绝该项目下所有 API 请求（注：由于计费延迟，限制生效可能有约 10 分钟延迟）。设置方式请见 [组织管理最佳实践](/docs/guide/org-best-practice)
      * **余额预警提醒**：建议开启账户余额提醒功能。当账户余额低于预设金额（默认 ¥20）时，系统会通过短信通知您及时充值。
    * **使用建议**
      * 建议先用较短上下文明确提示词测试，再逐步加入完整业务上下文。
      * **持续监控**：建议在编程软件运行期间保持监控，及时处理异常情况，避免因无限循环或过度重试造成不必要的资源消耗。
      * **模型选择**：如果对成本敏感，可以选择使用 `kimi-k2.6` 模型。
  </Accordion>

  <Accordion title="如何提升 API 调用速率？ ">
    为了整体资源分配的公平性，同时防止恶意攻击，我们目前将基于账户的累计充值金额进行速率限制，具体如下表，详细信息请查看 [充值与限速](https://platform.kimi.com/docs/pricing/limits) 页面。
  </Accordion>

  <Accordion title="如何进行个人以及企业认证？">
    * 个人：请登录我们的 [用户中心](https://platform.kimi.com/console/auth) 进行实名认证；
    * 企业：请登录我们的 [用户中心](https://platform.kimi.com/console/auth) 进行企业认证，请提前准备企业相关信息（企业名称，与企业名称相同的银行账号，统一社会信用代码），平台会向您公司账户打款随机金额，用于验证企业信息。请联系贵公司财务确认，填入来自北京月之暗面科技有限公司的打款金额，金额匹配成功后，企业认证通过。
    * 认证成功后会为您赠送 15 元代金券，可用于支持该代金券的模型（Kimi K3 不支持使用新用户代金券，详见下方说明）。
  </Accordion>

  <Accordion title="新用户赠送的 15 元代金券可以体验 Kimi K3 吗？">
    不可以。模型发布后，国内注册并完成认证的用户获赠的 15 元代金券不可用于体验 Kimi K3，请充值后解锁使用。
  </Accordion>

  <Accordion title="Kimi K3 如何计费？">
    Kimi K3 上下文长度为 1M tokens，计费不按上下文长度分段：所有用量均按量付费，输入（区分缓存命中与未命中）与输出分别按统一单价计费，详见 [Kimi K3 定价](/docs/pricing/chat)。
  </Accordion>

  <Accordion title="是否有针对企业客户的专属产品和服务？">
    * Kimi 销售团队可为企业调用 Kimi API 提供更多资源与支持，请前往 [https://platform.kimi.com/contact-sales](https://platform.kimi.com/contact-sales) 填写表单联系销售

    * Kimi 智能助手现已推出 Kimi Business 企业会员权益，请前往 [https://www.kimi.com/membership/pricing](https://www.kimi.com/membership/pricing) 线上下单
  </Accordion>

  <Accordion title="是否支持变更认证类型？">
    * 认证状态仅支持个人认证变更为企业认证，变更成功后，账号充值请按照企业账号充值的指引操作；
    * 不支持企业认证账号变更。
  </Accordion>

  <Accordion title="如何开发票？">
    * 平台支持按消耗金额或充值金额开具发票，请线上发起开票申请 [发票管理](https://platform.kimi.com/console/invoice)
    * 个人认证可以开具个人抬头/公司抬头发票；企业认证仅以开具企业认证主体抬头的发票
    * 开票主体为北京月之暗面科技有限公司；发票项目名称为“技术服务费”，税收分类编码简称为“生产生活服务”，税率为 6%。发票票面显示为 `*生产生活服务*技术服务费`。
  </Accordion>

  <Accordion title="是否支持账号密码登陆？">
    * 支持账号密码设置，密码设置成功后，可以通过手机号/密码登陆和账号名/密码登陆。[账号密码设置](https://platform.kimi.com/profile)
  </Accordion>

  <Accordion title="是否支持手机号换绑？">
    * 支持手机号换绑。换绑的目标手机号需未注册过 Kimi 开放平台或 Kimi 智能助手。
  </Accordion>

  <Accordion title="是否支持账号注销？">
    * 不支持账号注销。
  </Accordion>
</AccordionGroup>
