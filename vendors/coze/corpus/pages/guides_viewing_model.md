> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

你可以通过查看模型的性能指标和并发指标，评估模型的效率和效果。同时，你还可以通过查看用量记录，跟踪模型的使用情况，对于资源规划和成本管理至关重要。

## 查看性能指标 {#46d97ac5}

通过模型管理功能，你能够全面监控和评估模型的关键性能指标，包括模型的首 Token 延时、非首 Token 延时和成功率。

:::tip 说明
不同的模型，性能指标的统计方式存在差异，具体差异如下：

* MinMax、Kimi 模型：其性能指标是根据所有使用该模型的用户的综合数据而统计。
* 豆包模型：豆包模型的性能指标是根据空间内所有成员使用该模型的综合数据而统计。因此，即使是查看同一豆包模型，不同空间的用户查看的性能指标数据也可能存在差异。
:::

<!-- @cols-width: 136,541,267 -->
| **指标**  | **说明**  | **统计频率**  |
| --- | --- | --- |
| 首 Token 延时  | 记录用户输入 Prompt 到模型输出第一个 token 所需时间，单位为毫秒。 | 每 10 分钟统计一次。  | \
| | | | \
| | 首 Token 延时越低，代表模型的响应速度越快，用户的体验越好。  | |
| 非首 Token 延时  | 记录模型完成首 token 输出后，后续输出每个 token 所需的平均时长，不包括首 token 输出，单位为毫秒。  | 每 10 分钟统计一次。  |
| 成功率  | 记录模型调用成功次数占总调用次数的比例。  | 每 10 分钟统计一次。  |

通过综合考量这些性能指标，你可以对模型的整体表现有一个清晰的认识，并据此进行优化和调整。

参考以下操作，查看模型的性能指标。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在左侧导航栏中，单击**空间配置**。
3. 在**模型管理**页面的模型列表中，单击目标模型。
4. 在模型详情页，单击**性能监控**，查看各性能指标。
   统计图表中支持展示性能指标的平均值、P60 值、P95 值、P99 值，用于反映指标的分布集中程度。
   ![Image=679x529](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f1b92041c8504fcb9318e464991e57ee~tplv-goo7wpa0wc-topic.webp)   


## 查看用量记录 {#a577759d}

你可以通过**用量记录**看板追踪模型的用量，包括当前空间下模型每天处理的 tokens 数量以及当前模型在不同智能体、工作流中的具体用量，为资源管理与成本优化提供数据支撑。

<!-- @cols-width: 101,477,280 -->
| **图表名称**  | **说明**  | 应用场景  |
| --- | --- | --- |
| 用量统计  | 系统会分别统计每天智能体输入和输出的 tokens 数量以及工作流输入和输出的 tokens 数量，并将这些数据汇总，得到当天 tokens 总量并展示。 | * 评估模型的使用频率和活跃度，便于你理解模型在实际应用中的负载情况。 | \
| | | * 通过监控 tokens 处理量，你可以预测资源需求，优化成本控制，并确保模型在高流量情况下的性能和稳定性。  | \
| | **用量统计**图表支持展示最近 7 天的用量记录。 | | \
| | | | \
| | :::tip 说明 | | \
| | 当天的用量记录可能存在延时，仅供参考。**企业版（标准版**、**旗舰版）​**的模型用量可查看[方舟用量统计](https://console.volcengine.com/ark/region:ark+cn-beijing/usageTracking)。 | | \
| | ::: | | \
| | | | \
| |   | |
| 用量详情  | **用量详情**图表展示了指定月份内，该模型在当前工作空间下的不同智能体、工作流中的具体用量，包括输入 tokens、输出 tokens、消耗 tokens。同时，支持按照输入 tokens、输出 tokens、消耗 tokens 维度进行排序。  | * 便于查询当前模型在不同智能体、工作流中的具体用量。 | \
| | | * 快速识别模型用量最高的智能体、工作流，便于资源规划和成本管理。 | \
| | | * 为模型下架或替换场景，提供排查的参考依据。  |

参考以下操作，查看模型的用量记录。

1. 在**模型管理**页面的模型列表中，单击目标模型。
2. 在模型详情页，单击**用量记录**，查看**用量统计**和**用量详情**图表。
   单击指定智能体或工作流**用量细则**列的**查看**，可以查看当前模型在指定智能体或工作流中的每日用量及变化趋势。
   ::::cols
   @col 50
   ![Image=2365x1025](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1588a81171ca4c43949fec715526380c~tplv-goo7wpa0wc-topic.webp)
   
   @col 50
   ![Image=2270x563](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/660827eac878416a9f0cd8313345a6b4~tplv-goo7wpa0wc-topic.webp)
   ::::   


## 查看并发监控 {#1c3e66a7}

通过**并发监控**看板，你可以查看模型的 RPM 限额和 TPM 限额，以及模型实际运行的 RPM、TPM 数据。这些数据可帮助你了解模型运行状态，作为未来资源规划的依据。

<!-- @cols-width: 154,688 -->
| **指标**  | **说明**  |
| --- | --- |
| RPM  | RPM 表示模型每分钟能处理的请求次数，是衡量模型的响应能力和处理速度的重要指标。 | \
| | | \
| | **RPM 图表**包含当前账号所有空间下使用该模型的请求，你可以通过 **RPM 图表**查看**分钟级**、**日级**的模型 RPM 变化趋势。  |
| TPM  | TPM 表示模型每分钟消耗的 Tokens 数量，是衡量模型处理能力的重要指标。 | \
| | | \
| | **TPM 图表**包含当前账号所有空间下使用该模型的请求，你可以通过 **TPM 图表**查看分钟级及天级的模型 TPM 变化趋势。  |

参考以下操作，查看模型的并发监控指标。

1. 在**模型管理**页面的模型列表中，单击目标模型。
2. 在模型详情页，单击**并发监控**，查看模型的 RPM 和 TPM 指标。
   ![Image=435x246](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ff4e04bf653d49a9889bb3774e90a6b4~tplv-goo7wpa0wc-topic.webp)   


## 常见问题 {#1897813e}

### 如何快速切换待下架模型？ {#88c0b61a}

当你使用的模型即将下架时，可以采用以下两种方式为低代码项目替换模型，以确保服务的连续性。

1. **方式一：逐个替换**
   项目的创建者可以在**用量详情**图表中，快速定位调用了待下架模型的智能体或工作流，并逐个为它们切换模型。此操作仅更新**编排页面**中的模型，替换后需要重新发布。
* **方式二：批量替换**
   工作空间的所有者或管理员可以在**用量详情**图表中，快速定位当前工作空间下所有使用该模型的智能体或工作流，并批量为这些项目的**线上版本**切换模型。   


::::tabs
@tab 方式一：逐个替换
建议结合 tokens 消耗数据排序，优先替换高频高消耗智能体或工作流中的模型。

:::tip 说明
本步骤仅适用于低代码智能体或工作流，且仅限其创建者可以替换模型。
:::

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在左侧导航栏中，单击**空间配置**。
3. 在**模型管理**页面的模型列表中，单击待替换的目标模型。
4. 在**用量记录**页签下，找到**用量详情**图表。
5. 单击**输入 tokens**、**输出 tokens** 或 **消耗 tokens** 列的**排序**按钮，定位 tokens 消耗高的智能体或工作流。
   ![Image=377x196](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3d184452d4f24303ac90be17c58e1249~tplv-goo7wpa0wc-topic.webp)
6. 单击目标智能体或工作流的名称，跳转至对应的智能体、工作流编排页面，进行模型替换。
   替换模型后，请确认试运行无误，并及时发布智能体或工作流。
   ![Image=350x183](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f22f1d9b320a49b7a000fa30ed2f4779~tplv-goo7wpa0wc-topic.webp)
   ![Image=344x249](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/97dcd13d83334e69b1b0f40013f67623~tplv-goo7wpa0wc-topic.webp)

@tab 方式二：批量替换
当某个模型即将停运时，工作空间的所有者或管理员可以快速定位当前工作空间下所有使用该模型的低代码项目，并批量为这些项目的线上版本切换模型。模型停运 7 天内，仍支持批量切换模型。

:::tip 说明
* 批量切换模型仅作用于已发布的**线上版本**。线上版本将在运行时动态切换至新模型，但编排界面仍会保留旧模型，你可以根据方式一，手动替换。
* 切换前后模型价格、输入输出类型与限额可能存在差异。
* 切换后新模型默认使用标准配置，若需自定义参数，可手动调整配置后重新发布即可。
* 切换后新模型的用量图表数据将在次日自动更新。
:::

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在左侧导航栏中，单击**空间配置**。
3. 在**模型管理**页面的模型列表中，单击待替换的目标模型。
4. 在**用量记录**页签下的**用量详情**图表中，单击**切换模型**。
   ![Image=526x245](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6d28948311bf470daa6d9890b087c6a2~tplv-goo7wpa0wc-topic.webp)
5. 选择一个新模型，单击**确认**。
6. 查看新模型信息，确认新模型符合需求后，单击**确定**，完成模型切换。
   ![Image=272x267](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/602de211a95049919c8be8eaa944ed4b~tplv-goo7wpa0wc-topic.webp)
   切换完成后，单击项目名称可以跳转到编排页面，系统将提示你模型已切换。单击**我已知悉**后，页面中的旧模型将被自动替换为你刚刚选择的新模型，你可以重新设置新模型的参数。
   ![Image=467x167](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8b77b9db3bf54384904a171b0434b97c~tplv-goo7wpa0wc-topic.webp)
::::
