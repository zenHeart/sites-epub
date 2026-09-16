> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程提供了低代码应用搭建调试台，助力开发者快速定位及修复低代码应用搭建中的问题。在搭建低代码应用过程中，开发者能够实时对页面组件的属性配置及交互事件配置进行调试，验证各个组件功能与交互逻辑符合预期。例如当属性配置错误时，调试台会即时展示错误信息；当执行页面操作失败时，调试台将精准定位到该操作所绑定的事件及失败原因。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 功能入口 {#4793b474}

你可以在低代码应用的**用户界面**页签中，单击**调试**，展开调试台。调试台包含如下两个核心部分：

* 时间线：提供组件交互事件的实时运行视图，便于开发者追溯事件执行过程。
* 错误：集中展示组件属性配置的错误或警告信息，便于开发者及时发现并修改属性配置。

![Image=2217x1201](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/429aa62ca9344b77ab3185ebac4453bc~tplv-goo7wpa0wc-topic.webp)

## 时间线 {#e72f561a}

触发组件的事件时，**时间线**页签中会实时展示具体事件的详细信息，包括触发事件的组件、事件类型、触发动作、事件执行的时间点、事件耗时、事件执行状态、事件执行顺序、事件详情等信息，便于开发者快速追溯操作顺序并精准定位问题。

以[拍照解题](https://www.coze.cn/template/project/7475734454254895131?&surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)应用为例，使用者通过拍照功能上传题目图片后，单击**开始解题**，应用随即自动解答题目。其中，**开始解题**按钮已绑定交互事件，即单击时调用解题工作流并进行页面跳转。因此当你单击**开始解题**时，时间线中会记录并展示对应的事件信息。如果未上传题目，直接单击**开始解题，​**工作流调用将失败，并展示失败原因。当上传题目后并再次单击**开始解题**，时间线中会继续记录事件的运行过程，此时显示工作流正常运行直到运行成功，并展示具体的输入值、输出值。

::::cols
@col 33
**执行失败**

![Image=1899x1137](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/74129c899dc640f4ad84e57b7929ce00~tplv-goo7wpa0wc-topic.webp)

@col 33
**执行中**

![Image=1905x1140](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/86674aecda0045c28c5290668b57bf3d~tplv-goo7wpa0wc-topic.webp)

@col 33
**执行成功**

![Image=1892x1133](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/599aab11c2c64d8fb75150809d25fd9a~tplv-goo7wpa0wc-topic.webp)
::::

你还可以单击**成功**、**错误**、**加载中**，筛选对应类型的事件。当你不再需要查看当前时间线内容时，可以单击**清除**图标，清除内容。

:::notice 注意
清除时间线内容后，不可恢复。
:::

## 错误 {#4dce8a8b}

当你配置的组件属性不符合平台规范时，调试台的**错误**页签中将实时展示对应的错误或警告信息。例如**可见性**属性仅允许设置为 `false`、`true` 或变量，如果输入非预期的值，**错误**页签中将立刻提示错误信息。当你将值修改正确后，错误信息自动清除。

![Image=2211x550](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/24a9671d23da40a1b0efe470a05a986f~tplv-goo7wpa0wc-topic.webp)
