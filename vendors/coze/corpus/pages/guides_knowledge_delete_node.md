> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

低代码工作流中的知识库删除节点用于删除指定知识库中的文件。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制​**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 节点说明 {#fa0221d6}

在低代码工作流中，你可以添加**知识库删除**节点，用于动态删除指定的知识库文件。知识库文件的动态删除操作，常用于知识库文件更新场景，例如当需要更新知识库内容时，可以先通过知识库删除节点删除旧文件，再通过知识库写入节点写入新文件，避免手动操作的繁琐。

知识库删除节点需要指定待操作的知识库和文档 ID，每次执行此节点时将删除符合条件的文件。

:::notice 注意
* 删除某个知识库文件后，引用了对应知识库的低代码智能体或工作流将无法召回该内容。
* 删除操作不可撤回，请谨慎操作。
:::

## 添加节点 {#417e8564}

在工作流画布中，单击 **+ 添加节点**，在**知识库&数据**区域选择**知识库删除**节点，即可将节点添加到画布中。

![Image=496x272](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/41b8296f6c9a4e9685f5bd71759ba05f~tplv-goo7wpa0wc-topic.webp)

## 配置节点 {#c1ee0f3e}

### 输入 {#72f23f22}

知识库删除节点的输入参数固定为 `documentID`，数据类型为 String，表示需要配置待删除的文档 ID。具体配置如下：

* 引用上游节点的输出参数：将知识库写入节点或知识库检索节点作为知识库删除节点的上游节点，在知识库删除节点的输入变量 `documentID` 中，引用知识库写入节点或知识库检索节点的输出参数 `documentId`。
   如果上游节点的输出参数中存在多个 `documentId`，默认选择第一个 `documentId`。
   ![Image=455x167](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/99031e6f851a41808bfa31ede7fc6c3c~tplv-goo7wpa0wc-topic.webp)
* 输入固定值：如果是火山知识库，可以在[火山知识库控制台](https://console.volcengine.com/vikingdb/knowledge/region:vdb-knowledge+cn-beijing/collection/list)的目标知识库中，找到文档 ID，例如 `_sys_auto_gen_doc_id-1362****84360926`。
   ![Image=2824x711](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/87d1a719ad274f26a885c2c841fbd4ee~tplv-goo7wpa0wc-topic.webp)
   然后在知识库删除节点中，输入固定的文档 ID。
   ![Image=395x166](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7af44bac544245a6a6d2d70f487a3eb9~tplv-goo7wpa0wc-topic.webp)   


### 知识库 {#872f1308}

在**知识库**区域，选择待删除的知识库。

* **知识库来源**：选择**扣子知识库**或**火山知识库**。
* **添加知识库**：选择具体的知识库。

![Image=394x199](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1f57b2b59c794984b4c32fd31b266a93~tplv-goo7wpa0wc-topic.webp)

### 输出 {#a11c4f9f}

知识库删除节点中的输出参数是执行知识库删除操作后的输出内容，固定为 `isSuccess`，值为 true 或者 false，表示是否删除成功。

## 示例 {#85c0d539}

例如在工作流中，通过**知识库检索节点**检索到标题为**产品手册V1.0**的旧文档，通过**知识库删除节点**将其删除，然后通过**知识库写入节点**将**产品手册V2.0**文档写入知识库，从而完成文档内容的更新操作，整个过程高效且减少繁琐的手动操作。

![Image=2036x1001](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/08b9483d805d4411ac0b0f40dbc305df~tplv-goo7wpa0wc-topic.webp)
