> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

低代码工作流中的 JSON 反序列化节点用于从 JSON 格式字符串中提取其中的字段内容作为变量。

## 节点说明 {#bc614e02}

在扣子编程的低代码工作流中，某些节点的输出往往是 JSON 格式的字符串，需要格式化后提取其中的字段作为变量，以供后续节点调用。例如通过 HTTP 节点调用业务 API 查询用户信息，节点返回的输出变量 body 为 JSON 字符串，可以使用 JSON 反序列化节点提取其中的姓名、年龄、地址等字段内容作为变量，存储到扣子数据库中以供查询。

JSON 反序列化节点可省去通过代码节点进行 JSON 字符串转换的步骤，使 JSON 格式数据处理操作更加简单便捷。

:::tip 说明
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制​**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
* 每次执行 JSON 反序列化节点只能处理一个 JSON 字符串，如需批量处理多个，可以考虑使用批处理节点，详细说明可参考[批处理节点](/guides/batch_node)。
* JSON 反序列化节点最多可解析 JSON 格式的第 3 层嵌套结构。
:::

## 添加节点 {#2885dd19}

在工作流画布中，单击 **+ 添加节点**，在**组件**区域选择 **JSON 反序列化**节点，即可将节点添加到画布中。

![Image=573x308](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/98ce372882bb40aabb6881b1b764ed0f~tplv-goo7wpa0wc-topic.webp)

## 配置节点 {#2ba236bf}

### 输入 {#6b288d99}

输入需要处理的变量，也就是待进行 JSON 反序列化处理的 JSON 字符串。支持引用上游节点的 String 格式输出变量，或者直接输入一个固定的 JSON 字符串。待处理的字符串必须是一个合法的 JSON 格式字符串，String 格式，否则反序列化处理可能失败，无法正确提取 JSON 中的字段。

### 输出 {#616516ba}

固定的输出参数为 output，默认为 Object 类型，也支持 String、Integer 等其他格式。

如果下游节点需要使用对象中的某个元素，则需要为 output 配置子项。例如 JSON 字符串中包含姓名、ID、地址、电话号码，需要提取其中的姓名和 ID 两列记录到数据库中，则可以仅为 output 配置姓名和 ID 两个子项。支持手动配置子项，你也可以导入一个 JSON 示例，系统会自动解析出所有字段，并将其配置为 output 对象的子项。

![Image=608x353](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fbb49b2bac464bbbacae8749359921f5~tplv-goo7wpa0wc-topic.webp)

## 示例 {#627c0382}

[JSON 序列化和反序列化](/tutorial/workflow_json)
