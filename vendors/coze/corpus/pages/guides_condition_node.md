> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

选择器节点是一个 if-else 节点，用于设计低代码工作流内的分支流程。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制​**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::
## 条件分支 {#29f1a05a}
当向该节点输入参数时，节点会判断是否符合**如果**区域的条件，符合则执行**如果**对应的工作流分支，否则执行**否则**对应的工作流分支。
每个分支条件支持添加多个判断条件（且/或），同时支持添加多个条件分支，可通过拖拽分支条件配置面板来设定分支条件的优先级。
![Image=711x268](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/26801110f735455eb42598a147500add~tplv-goo7wpa0wc-image.image)
## 优先级 {#f51e893c}
当存在多个条件分支时，将根据优先级排序逐个判断条件是否成立，若均不成立则只运行“否则”分支。
例如以下示例中，如果开始节点的 input 既不等于 true，也不等于 false，则执行“否则”分支。
![Image=791x240](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/978132f2d8644c9b80c50fa8d5ad92fa~tplv-goo7wpa0wc-image.image)

