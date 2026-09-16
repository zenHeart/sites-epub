> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

[抖音支付插件](https://www.coze.cn/store/plugin/7506410574759378994?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)现已在扣子编程中上线，你可以轻松将抖音支付开放平台提供的交易创建、查询、退款等能力集成到你的低代码智能体、应用或工作流中，创建具备支付能力的智能应用、实现 AI 服务变现。
:::tip 说明
* 抖音支付插件现已暂停维护，已接入正式版插件的开发者仍可继续使用，但不再接受和通过内测申请。
* 开发者若有变现需求，建议考虑在 AI 编程项目中集成支付宝的支付能力，详细说明可参考[支付宝技能：为应用集成支付能力](/tutorial/skill_alipay)
:::
抖音支付插件是由抖音支付官方推出的应用支付插件工具，目前处于内测阶段。开发者可以先通过体验版试用插件，体验完整效果。
目前抖音支付插件提供体验版和正式版两个版本，为了提高开发者接入效率，建议先通过体验版搭建 Demo，跑通支付流程，再申请正式版内容，正式接入插件。插件版本的详细说明如下：
<!-- @cols-width: 205,620 -->
| | | \
|**版本** |**说明** |
|---|---|
| | | \
|[抖音支付插件体验版](https://www.coze.cn/store/plugin/7527870617668976679?from=store_search_suggestion&surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=) |无需开户申请，所有扣子用户均可使用体验版插件，试用支付效果。使用前应注意： |\
| | |\
| |* 体验版插件绑定了测试专用的账户号，所有订单为0.01元的测试订单，收款为测试账号，开发者不支持转账、提现。当天所有的测试订单，将在次日陆续退回到用户支付账户。 |\
| |* 该版本专用于开发者**体验、试用**下单、查询、退款等支付能力，**请勿用于真实的生产场景**。 |
| | | \
|[抖音支付插件正式版](https://www.coze.cn/store/plugin/7506410574759378994?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=) |抖音支付插件现已暂停维护，已接入正式版插件的开发者仍可继续使用，但不再接受和通过内测申请。 |

## 体验效果 {#de2ec26b}
为智能体添加抖音支付插件，用户和智能体对话时，如果要求获取某个付费服务，智能体会自动调用插件生成订单并引导用户支付。你也可以根据业务场景设计各种支付流程，例如生图场景下先提供低画质的图片，再引导用户付费获取高画质的图片。
:::tip 说明
* [单击此处体验支付效果](https://www.coze.cn/store/agent/7506127406286028800?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
* 试用时支付的费用将于次日自动退款至原账号。
* 抖音支付插件暂不支持发布到豆包和小程序。
:::

::::cols
@col 25
触发支付：
![Image=272x228](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c67c83df90d043588423e7e102772858~tplv-goo7wpa0wc-image.image)


@col 15
抖音支付页面：
![Image=1290x2798](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f20e5a27304842708556c05731a25c3b~tplv-goo7wpa0wc-image.image)


@col 28
未支付但声称已支付：
![Image=664x396](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ff8eab753bfc4d7f88071842bc418c8a~tplv-goo7wpa0wc-image.image)



@col 30
完成支付：
![Image=708x567](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1e95e73fd4054a8cb5ddb2ab6f8f6044~tplv-goo7wpa0wc-image.image)

::::


