> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子罗盘提供了演示空间，方便你快速了解扣子罗盘的各种功能。
:::tip 说明
演示空间的数据为测试数据，仅供演示使用。
:::
# 访问扣子罗盘体验空间 {#3c8caf5d}
参考以下步骤，访问扣子罗盘体验空间。

1. 访问[扣子罗盘](https://loop.coze.cn)，然后单击右上角的**立即体验**。
2. 使用扣子账号登录。
   如果你尚未注册扣子账号，参考[账号注册](https://www.coze.cn/open/docs/guides/sign_up)注册一个扣子账号并完成登录。
3. 展开左侧导航栏顶部的空间列表，然后选择 **Demo 空间**。
   如果是首次访问扣子罗盘，默认进入到 Demo 空间。
   ![Image=548x192](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2d8fb0e79e6940989e50a40a7f658bac~tplv-goo7wpa0wc-image.image)
4. 在显示的欢迎页面，单击**立即体验**，进入扣子罗盘的体验空间。
   ![Image=550x357](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3ef5f84b97db419ba9783059f30eb4d7~tplv-goo7wpa0wc-image.image)

# 体验提示词开发 {#424a0fed}
登录扣子罗盘后，默认进入到 **Prompt 开发**页面。在这里，你可以查看平台预设的 Prompt，单击**详情**了解 Prompt 的详细设计。扣子罗盘支持以 MessageList 的方式托管提示词模板，以满足复杂的业务场景。更多关于 Prompt 开发的详细说明，参考[开发提示词](/cozeloop/create-prompt)。
![Image=519x249](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9f78b62c8f3b49feabd42bec4b396347~tplv-goo7wpa0wc-image.image)
# 体验评测功能 {#605fadac}
评测模块为开发者提供系统化的评测能力，能够对 Prompt 和扣子智能体的输出进行评测。你可以通过分析实验结果，深入研究异常案例，并进行有针对性的优化。
你可以切换到**评测**功能模块，体验扣子罗盘的评测能力。我们将按照评测实验流程引导你一步步体验扣子罗盘的评测功能。你也可以参考[评测入门教程](/cozeloop/evaluation-quick-start)，发起一个评测实验。
## 查看评测集 {#3503520c}
要发起评测实验，需要先创建一个评测集，为评估对象添加测试数据。

1. 在左侧导航栏，选择**评测 > 评测集**。
2. 在**评测集**列表页面，单击**详情**查看已创建的评测集数据。
   ![Image=613x164](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6d70362cab704eaba9f717357a48dda8~tplv-goo7wpa0wc-image.image)
3. 在详情页面，可查看评测数据。
   示例测试数据由输入数据（input 列）和理想的预期输出数据（reference_output）两列构成。其中输入数据作为评测对象的输入信息，预期输出数据作为评测标准参考。
   ![Image=596x305](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9cebe4ebd35e4438b2e121ed9579730a~tplv-goo7wpa0wc-image.image)
4. 单击**关联实验**页签，查看这个评测集的关联的实验结果。
   你可以通过不同维度的数据指标结果，综合分析评测对象的输出效果，有针对性的进行调优。
   ![Image=638x297](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/aada5d5a5a6f4b8da87fdcab2bca78c6~tplv-goo7wpa0wc-image.image)

## 查看评估器 {#642e6b3f}
扣子罗盘支持使用大模型评估器对评估对象进行自动化评测。在准备好数据集后，就需要准备评估器，制定评测标准。

1. 在左侧导航栏，选择**评测 > 评估器**。
2. 在**评估器**列表页面，查看已创建的评估器。
   评估器支持版本管理。在发起评测实验时，可选择不同的评估器版本，针对评估器进行优化迭代。
   ![Image=654x235](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/aa0f92117071447d85a82c65e91ee82c~tplv-goo7wpa0wc-image.image)
3. 单击**详情**，查看评估器配置。
4. 在评估器配置页面，单击**调试**，输入构造的输入数据和标准输出数据，测试评估器效果。
   ![Image=580x323](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/40effa3d169e457a93cba621354248f3~tplv-goo7wpa0wc-image.image)

## 查看评测实验 {#033a53ee}
在准备好评测集和评估器后，就可以对评估对象发起评测实验了。扣子罗盘支持对 Prompt 和扣子智能体进行评估。

1. 在左侧导航栏，选择**评测 > 实验**。
2. 在**实验**列表页面，查看已发起的评测实验。
   ![Image=595x142](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9c7c4559d3d943caab14346b96fd2d2b~tplv-goo7wpa0wc-image.image)
3. 选择一个评测实验，单击详情查看评测结果。
4. 扣子罗盘支持对评测结果进行人工校准。选择要要校准的目标数据，然后单击人工校准的编辑图标。
   ![Image=603x309](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8f49f11b61e147408a5894eb6f3323b6~tplv-goo7wpa0wc-image.image)
5. 单击**指标统计**查看实验报告。
   扣子罗盘会根据实验结果自动生成可视化看板，方便对测试结果进行分析，进行决策。
   ![Image=564x270](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ec7a86137e934ba88db3001a7bdb5040~tplv-goo7wpa0wc-image.image)

# 体验观测功能 {#e661cc80}
扣子罗盘为开发者提供了全链路执行过程的可视化观测能力，完整记录从用户输入到 AI 输出的每个处理环节。
## 查看 Trace  {#93c77007}
观测功能支持平台提示词（Prompt）开发、扣子智能体、扣子 AI 应用的数据自动上报，也支持通过集成 SDK 上报其他框架（Eino/Langchain）开发的 AI 应用。详情请参考[SDK 概述](/cozeloop/sdk)。
在**观测 > Trace** 页面，选择时间范围、任务节点范围和观测对象，查看已上报的 Trace 数据。关于 Trace 数据的详细说明，参考[Trace 信息说明](/cozeloop/trace-data#dba04675)。
![Image=2828x1318](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/36f4e54bf1f740e09c094802e29ed44c~tplv-goo7wpa0wc-image.image)
## 查看统计数据 {#9cbd38d3}
扣子罗盘提供了不同维度的统计指标看板，可直观了解观测对象的运行情况和成本消耗。
![Image=2842x1437](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bcbd1dda760d43d3a5d31686f67d82a2~tplv-goo7wpa0wc-image.image)

