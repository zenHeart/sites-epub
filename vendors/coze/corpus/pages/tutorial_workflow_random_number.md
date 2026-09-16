> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程低代码工作流中的代码节点通常用于实现一些特定的逻辑或算法，或数据进行特定格式转换或处理，本教程演示如何通过代码节点生成随机数。
## 效果示例 {#dabc917c}
搭建一个生成随机数的低代码工作流，并将其绑定智能体之后，在调试区域发送生成随机数的指令，智能体会自动调用该工作流，并生成一个随机数。
![Image=341x370](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b790d2f751f24ffa87a0c32ff9b5d61e~tplv-goo7wpa0wc-image.image)
## 低代码工作流设计 {#1aad51ff}
本文构建的示例工作流节点概览如下图所示。在该工作流中：

1. 开始节点接收用户指定随机数长度。
2. 代码节点根据指定的长度生成随机数。

![Image=1358x326](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8ae4a09c8ea04663a92bb52938fa6875~tplv-goo7wpa0wc-image.image)
## 步骤一：构建低代码工作流 {#9b5b0094}
1. 登录[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。


3. 在页面右上角，单击 **+资源** > **工作流**。
   本文示例配置如下：
   * **工作流名称**：输入 `random_number`
   * **工作流描述**：输入 `生成随机数`
4. 在工作流的编辑页面，从左侧**选择节点**列表，选用**代码**节点。
5. 连接各节点，并依次配置输入输出参数。
   节点连接顺序：**开始 → 代码 → 结束**，各节点参数配置说明如下表。
   <!-- @cols-width: 127,695 -->
   | | | \
   |**节点** |**参数配置** |
   |---|---|
   | | | \
   |开始 |新增输入变量 `input_length`，并选择 **String** 数据类型。 |
   | | | \
   |代码 |* 新增输入变量 `length`，并在**参数值**区域选择**引用 Start > input_length**。 |\
   | |* 新增输出变量 `random`，数据类型选择 **String**。 |\
   | |* 在代码节点打开 IDE，清空默认内容并添加以下代码，该代码用于生成随机数。 |\
   | |   ```JavaScript |\
   | |   async function main({ params }: Args): Promise<Output> { |\
   | |       var IDX = 36, HEX = '';  |\
   | |       while (IDX--) HEX += IDX.toString(36);  |\
   | |         |\
   | |       // @see https://github.com/lukeed/uid/blob/master/src/single.js  |\
   | |       function uid(len) {  |\
   | |           var str = '', num = len || 11;  |\
   | |           while (num--) str += HEX[Math.random() * 36 | 0];  |\
   | |           return str;  |\
   | |       }  |\
   | |     |\
   | |       const ret = {  |\
   | |           "random": uid(params.length),  |\
   | |       }  |\
   | |       return ret  |\
   | |   } |\
   | |   ``` |\
   | | |
   | | | \
   |结束 |新增 `output` 输入参数，并在**参数值**区域选择**引用 代码 > random**。 |

6. 配置完成后，单击页面右上角的试运行，测试工作流。
   例如，输入 `8` 进行测试，待所有节点都运行成功（节点会展示绿色边框）后，查看指定节点的运行结果。
7. 测试工作流无问题后，单击页面右上角的**发布**。
   成功发布后，在工作流列表中可以查看到该工作流。

## 步骤二：在智能体添加工作流并测试 {#7ca2011e}

1. 前往当前工作空间的**项目开发**页面，创建或进入指定智能体。
2. 在智能体内，找到**技能**区域的**工作流**，在右侧单击加号图标。
3. 在对话框左侧单击**资源库工作流**，找到自建的 **random_number** 工作流，并在右侧单击**添加**。
   ![Image=631x240](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ceb135c7c8ed482ea77a5070796b1526~tplv-goo7wpa0wc-image.image)
4. 在智能体的**人设与回复逻辑**内，声明智能体使用 **random_number** 工作流处理任务。
   编写后，你可以单击**优化**，让 AI 帮助你生成结构化的回复逻辑。
5. 在智能体的右侧**预览与调试**区域，输入内容预览智能体实现的效果。
   例如输入 `生成一个8位随机数`。
   ![Image=330x358](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0eebbf2282e245c5886b802a29d6b8b7~tplv-goo7wpa0wc-image.image)


