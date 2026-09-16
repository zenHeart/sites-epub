> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

低代码工作流中的JSON 序列化节点用于将数据结构（变量）转换为 JSON 格式的字符串，便于下游节点处理。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制​**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 节点说明 {#0fd5e35d}

扣子编程的低代码工作流节点支持 Object、Array 等多种复杂类型的输入和输出格式，在数据传输和处理的过程中，往往需要转换数据类型以便下游节点处理。JSON 序列化和反序列化是常见的数据类型转换方式，例如将某个节点输出的 Object 对象保存在扣子数据库中，需要先将 Object 对象转换为 JSON 字符串，再通过数据库节点保存到 String 类型的字段中。

低代码工作流现已支持 JSON 序列化和反序列化节点，支持将 Object 对象等常见数据类型转换为 JSON 字符串，以及将 JSON 字符串还原为指定数据结构（变量）。相较于代码节点，JSON 序列化和反序列化节点无需编写代码，可视化程度高、操作更加便捷。关于 JSON 反序列化节点的详细说明，可参考[JSON 反序列化节点](/guides/json_deserialization_node)。

## 添加节点 {#1f024beb}

在工作流画布中，单击 **+ 添加节点**，在**组件**区域选择 **JSON 序列化**节点，即可将节点添加到画布中。

![Image=588x319](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ca2f5dcb39b0419394333c0fc91b856e~tplv-goo7wpa0wc-topic.webp)

## 配置节点 {#9eb6b569}

配置节点的输入和输出变量：

* **输入**：设置需要处理的变量，也就是待进行 JSON 序列化处理的数据结构。输入变量支持引用上游节点的输出变量，或者直接输入一段固定的内容，例如 JSON 格式的文本。
* **输出**：固定的输出参数为 output，String 类型，表示 JSON 序列化之后的字符串。

![Image=443x291](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3bbb805f7a0847a380c9ae1fe4f80b58~tplv-goo7wpa0wc-topic.webp)

## 示例 {#3f4eecaf}

[JSON 序列化和反序列化](/tutorial/workflow_json)
