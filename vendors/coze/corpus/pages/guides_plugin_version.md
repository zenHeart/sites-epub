> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

在资源库中的插件支持通过版本的方式记录插件的发布历史，你可以在插件工具列表页面查看发布记录的详细信息。

在插件工具列表页面中单击查看历史图标，可以查看插件的所有版本的发布记录。

:::tip 说明
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
* 对于工作空间资源库中的插件，工作空间内成员都可以查看发布历史。
* 低代码应用中的插件，暂不支持记录历史版本。
:::

## 生成插件版本 {#f66fefa6}

发布资源库中的插件时，你需要设置插件的版本号和版本描述，这些信息会记录在插件历史版本页面，便于后期追溯和参考。成功发布资源库中的插件之后，插件会生成一个新的发布版本和提交版本，这两个版本的内容和操作时间完全一致。

![Image=1606x611](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/12466a00839343078de280c7f0133944~tplv-goo7wpa0wc-topic.webp)

## 查看插件发布记录 {#db0da685}

在插件的编排页面右上角单击发布历史图标，可以查看插件的版本列表。此页面根据操作时间倒序展示当前插件的发布历史记录，包括版本号、版本描述和发布时间。

:::tip 说明
暂不支持查看某个历史版本的插件工具配置详情。
:::

![Image=1625x472](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/531db63373ea481598b948cbfea56748~tplv-goo7wpa0wc-topic.webp)

## 引用插件版本 {#5ec8ad38}

智能体绑定的插件，始终使用插件的最新版本。也就是说，编辑并重新发布插件后，智能体会自动使用插件的最新版本。

低代码应用的工作流中，如果插件节点使用的是项目资源库中的插件，则始终保持引用这个指定版本，即使插件发布了最新版本，应用工作流也不会同时更新，所以发布新的插件版本不会影响应用的线上运行。如果你需要在低代码应用中使用最新的插件版本，可以在工作流中根据页面提示手动升级插件版本。

![Image=368x225](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8be07a8960be4a5594560056b8c36aac~tplv-goo7wpa0wc-topic.webp)

:::tip 说明
* 引用插件或升级插件版本时，不支持选择某个历史版本，必须使用插件的最新版本。
* 升级到最新版本后，当前工作流中所有使用此资源的节点均会同步升级。
:::


