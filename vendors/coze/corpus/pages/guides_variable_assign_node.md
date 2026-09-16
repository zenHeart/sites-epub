> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

低代码工作流中的变量赋值节点是工作流中用于修改和存储变量值的节点。

![Image=200x152](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6e2bed846bce455a82e66945f31fcb50~tplv-goo7wpa0wc-topic.webp)

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制​**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 节点说明 {#9a712e1d}

通过变量赋值节点，将特定的值赋给变量，可以实现数据的动态更新和传递，使工作流能够根据实时数据做出相应的处理和决策。变量赋值节点应用广泛，例如：

* **存储中间结果**：在工作流中，将中间计算或处理的结果通过变量赋值节点存储到变量中，以便后续节点使用。例如，在开发一个智能医疗诊断应用时，需要对患者的病历数据进行预处理，如提取关键症状、检查结果等信息。此时，可以设置一个变量`patient_info`，将患者的病历数据通过变量赋值节点存储起来，后续在进行疾病诊断时，可以直接从`patient_info`变量中获取患者的详细信息。
* **记录用户输入**：在与用户交互的工作流中，用户的输入信息是后续处理的重要依据。通过变量赋值节点，可以将用户的输入存储到变量中。例如，在开发一个智能客服机器人时，当用户向客服机器人咨询产品问题时，机器人提取用户关心的问题的关键词，然后将这些关键词通过变量赋值节点存储到一个名为`user_query`的变量中。在后续的处理节点中，机器人会根据`user_query`变量中的内容，从知识库中检索相关的答案或解决方案，并生成回复文本。
* **控制流程分支**：在工作流中，通常需要根据不同的条件来决定执行不同的分支流程。变量赋值节点可以用来设置控制流程分支的条件变量，通过赋予变量不同的值，来引导工作流走向相应的分支。例如，在开发一个个性化推荐系统时，需要收集用户的基本信息和行为数据，如年龄、性别、浏览历史等，然后分析用户的兴趣偏好，并将结果通过变量赋值节点存储到一个名为`user_preference`的变量中。在生成推荐内容时，根据`user_preference`变量值来决定推荐策略。

## 配置变量赋值节点 {#8a85e8aa}

为变量赋值时，在变量赋值节点的**输入**中添加需要赋值的参数。

* 变量名对应关联的智能体或应用中已创建的变量，如果该工作流未绑定包含变量的智能体或应用，单击变量名时根据页面提示选择智能体或应用中的相应变量。
   ![Image=300x254](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/61ca9f826aec4a7caf7a73e5086e3813~tplv-goo7wpa0wc-topic.webp)
* 变量值可以设置为固定值，也可以引用上游节点的输出参数。

:::tip 说明
变量赋值节点可以为用户变量、应用变量赋值，但不能为系统变量赋值。
:::

## 配置示例 {#d07d160b}

例如，在应用中搭建一个猜谜游戏对话流。

1. 先创建一个空白应用，并定义应用变量`score`，默认值设置为 0 。
2. 在对话流中添加变量赋值节点，每猜对一个谜语，变量`score`数值加 1，重新开始新的一局游戏时，`score`都会重置为游戏设定的初始值 0。

对话流流程如下：

![Image=2274x566](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2d7f9412d7614d53a1cb63a812f824ae~tplv-goo7wpa0wc-topic.webp)

节点配置如下：

<!-- @cols-width: 115,446,303 -->
| **节点类型**  | **说明**  | **示例**  |
| --- | --- | --- |
| 开始节点  | 工作流的起始节点，本示例保持默认参数即可。  | ![Image=354x518](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e14684820a51458eaf30493c3b85f6b1~tplv-goo7wpa0wc-topic.webp)  |
| 循环节点  | 用于指定猜谜游戏的次数，需要设置： | ![Image=200x228](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a20bf077c96a4fbd9b80eb7088ec9a01~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | * 循环类型：选择**指定循环次数**。 | | \
| | * 循环次数：本示例设置为 **5**。  | |
| 大模型节点（出谜人）  | 用于生成谜语，需要设置： | ![Image=362x1098](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f4350ec582614533bbd8407a8f6af228~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | * 系统提示词：设置出谜专家的人设，可以通过 AI 自动生成。 | | \
| | * 输出：定义两个变量。 | | \
| |    * riddle：模型生成的谜语。 | | \
| |    * answer：谜语的谜底。  | |
| 问答节点  | 用于向用户提出谜语问题，需要设置： | ![Image=360x772](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0241997d50aa46d88ada39f923754b0c~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | * 输入：定义 `riddle` 参数，引用大模型节点（出谜人）生成的谜语问题。 | | \
| | * 提问内容：本示例设置为`{{riddle}}`。 | | \
| | * 回答类型：本示例选择直接回答。 | | \
| | * 输出：定义 `user_answer` 参数，用于接收用户的回答。  | |
| 大模型节点（谜语裁判）  | 用于判断用户回答的正确性，需要设置： | ![Image=344x1213](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/dc48377a798d41dd8ac134e9d6b5495b~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | * 输入：定义四个变量。 | | \
| |    * `riddle`：引用大模型节点（出谜人）生成的谜语问题。 | | \
| |    * `answer`：引用大模型节点（出谜人）生成的谜底。 | | \
| |    * `user_answer`：引用问答节点的输出参数。 | | \
| |    * `score`：引用应用变量`score`。 | | \
| | * 系统提示词：设置谜语裁判的人设，可以通过 AI 自动生成。 | | \
| | * 用户提示词：设置为`谜语的谜面是{{riddle}}，正确答案是{{answer}}，用户的回答是{{user_answer}}`。 | | \
| | * 输出：定义两个参数。 | | \
| |    * `total_score`：用户猜谜游戏的分数。 | | \
| |    * `conclusion`：用户猜谜的结果。  | |
| 变量赋值节点  | 用于存储用户在猜谜游戏中的分数，将大模型节点（谜语裁判）中 `total_score` 的值赋给变量 `score`。  | ![Image=352x259](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/989e3f91d9ef43c39d7a8bff9d3e6634~tplv-goo7wpa0wc-topic.webp)  |
| 输出节点  | 用于输出用户猜谜的结论，并告知游戏的得分，需要设置： | ![Image=356x385](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/63ebb3241c604c3bab9eb219e0f7e003~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | * 输出变量：定义两个变量。 | | \
| |    * `output`：引用大模型节点（谜语裁判）的输出参数 `conclusion`。 | | \
| |    * `score`：引用应用变量 `score`。 | | \
| | * 输出内容：设置为`{{output}}，你当前得分为：{{score}}`。  | |
| 文本处理节点  | 用户游戏结束，展示最终的游戏得分，需要设置： | ![Image=358x459](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/efff408e62e74800b2196f3c06a9dec1~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | * 输入：将应用变量 score 的值赋给 String1。 | | \
| | * 字符串拼接：设置为`游戏结束！你本次总得分为{{String1}}，欢迎再次挑战哦~`。  | |
| 结束节点  | 选择返回文本模式，并设置输出变量和回答内容。 | ![Image=358x391](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a24d334efd1443da9976e511b257b023~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | * 输出变量：定义 `output` 参数，引用文本处理节点的输出参数 `output`。 | | \
| | * 回答内容：设置为`{{output}}`。  | |

## 常见问题 {#89e09316}

### **变量赋值节点能为系统变量赋值吗？** {#da388d31}

系统变量仅可读不可写，所以不能通过变量赋值节点为系统变量赋值。

### **变量赋值节点能读取变量值吗？** {#831223c3}

目前，除了开始节点、输入节点、知识库写入节点外，其他所有节点都能读取变量值，详细可参考[读取变量值](/guides/add_variables_in_app#bab45a00)。
