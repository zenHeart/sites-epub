> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

你可以通过扣子的**本地 Agent** 功能，将扣子编程 OpenClaw、ArkClaw、云厂商 OpenClaw 接入到扣子，进行统一管理。
## 背景信息 {#7d66ef8e}
如果你已经有多个 OpenClaw，它们可能分别部署在不同的环境中---扣子编程、云厂商、本地环境等，它们各自工作，你得分别跟它们对话。
现在，你可以通过扣子的**本地 Agent** 功能将它们统一接入到扣子。不管你的 OpenClaw 部署在哪里，都可以接进扣子，与它们对话。接入后，你还可以让它们组成一个团队，协同完成任务。
> 关于项目、本地Agent 的相关说明，请参考[项目与协作](/cozespace/collaboration)、[本地 Agent](/cozespace/local_agent)。

## 接入 OpenClaw {#3e575fcf}
本文以扣子编程 OpenClaw 为例，介绍接入流程，其他平台操作类似。

1. 在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=) Agent 列表中，单击➕ > **新建 Agent**。
   ![Image=267x145](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/38a65d645c6b43639a81d2ea7d63f9f2~tplv-goo7wpa0wc-image.image)
2. 在**新建 Agent** 面板中，单击**接入本地 Agent**。
3. 单击**复制命令**，复制系统生成的连接命令。
   命令中 token 有效期为 60 分钟，请复制后，在 60 分钟内执行命令，完成配对。超过有效期后，请重新生成连接命令。
   ![Image=277x257](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1951be307ec441639f9d06c30bc95dcd~tplv-goo7wpa0wc-image.image)
4. 在扣子编程 OpenClaw 项目的终端，执行连接命令。
   1. 打开[扣子编程](https://code.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)，在**项目管理**中，找到你的 OpenClaw 项目。
      ![Image=550x224](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/698f07b8a9754e49b01923ac6606534d~tplv-goo7wpa0wc-image.image)
   2. 在**终端**位置，执行连接命令。
      ![Image=428x254](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b5934006bf8545248e340beb38240bc7~tplv-goo7wpa0wc-image.image)
      回显信息为 `已配对连接完成，请返回到 coze 平台上点击 "我已执行"`，则表示执行成功，扣子编程OpenClaw 项目已与扣子云端连接。
5. 返回扣子，单击**已粘贴执行**，系统开始识别本地 Agent。
   ![Image=334x313](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e89a1528f3a54d74979181234ef052da~tplv-goo7wpa0wc-image.image)
6. 创建 Agent。
   识别成功后，你可以设置 Agent 名称，然后单击**创建 Agent**。
   ![Image=332x297](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e1b9782da02841b09c22b2baa6035949~tplv-goo7wpa0wc-image.image)

创建完成后，你就可以在扣子中与该本地 Agent 对话。
![Image=539x318](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e815f4d7da4e46a18d0e33f30fceed19~tplv-goo7wpa0wc-image.image)
## 接入后：怎么玩？ {#b96b9de8}
所有 OpenClaw Agent 接入完成后，你可以在扣子中直接与它们对话，也可以创建项目，将它们组织起来协同工作。
**示例场景**：

* Agent A（扣子编程部署）：发布到飞书渠道，能读写飞书文档、发飞书消息、管理日程。
* Agent B（本地电脑部署）：能操作本地文件、打开应用、执行脚本。

在同一个项目中同时调度这两个 Agent，那么你可以在一个项目中同时指挥它们，帮你干活。例如让 Agent B 读取本地开发项目，汇报进展，然后让 Agent A 基于项目进展生成飞书文档。

1. 在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=) Agent 列表中，单击➕ > **新建项目**。
   ![Image=290x149](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ae2e3cdba9e146b1811a4e6809b21267~tplv-goo7wpa0wc-image.image)
2. 设置项目名称，以及选择目标 Agent，然后单击**创建项目**。
   ![Image=312x323](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/13d1d9ad032f473a8b2c0cce3a981410~tplv-goo7wpa0wc-image.image)
3. 在项目中，通过对话，给 OpenClaw Agent 下达指令。
   :::notice 注意
   在项目中给 Agent 下指令时，**必须 @ 对应的Agent**。
   :::
   ![Image=392x247](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ed6a58814205418f902c5818ec20d097~tplv-goo7wpa0wc-image.image)


