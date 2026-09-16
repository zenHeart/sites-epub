> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

通过端插件，低代码智能体能够直接与硬件设备进行交互，实现对硬件设备的控制和信息获取。本文介绍创建端插件的步骤，你可以通过页面创建端插件、或通过 JSON 和 YAML 导入插件。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 场景描述 {#22212a08}

以“控制电脑完成简单任务”为例，端插件需要实现以下两个功能：

* 获取电脑电量：通过截图和图片理解技术，获取当前电脑的电量状态。
* 总结文件内容：读取本地目录中的文件，并提取其主要内容。

为了实现这些功能，需要在一个端插件中创建三个工具：

* 截图工具：该工具没有参数，其功能是直接对电脑屏幕进行全屏截图，并将截图结果作为返回值。
* 列出目录下文件工具：该工具的参数是具体的目录地址，其功能是列出指定目录下的所有文件，并将文件列表作为返回值。
* 读取文件内容工具：该工具的参数是具体的文件路径，其功能是读取指定文件的内容，并将文件内容作为返回值。

本文以该场景为例，介绍具体的创建步骤。

## 实现原理 {#83901f12}

本场景中，三个端插件的实现原理如下图所示。

![Image=700x557](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e97349e444f84f2db00d8859f994063a~tplv-goo7wpa0wc-topic.webp)

## 方式一：通过页面创建插件 {#a91f2e9a}

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 在页面右上角，选择 **+资源** > **插件**。
4. 填写插件基础信息，**插件工具创建方式**选择**端侧插件**，单击**确认**。
   ![Image=400x480](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7acc7a71a1e245a6a36ea26b2ab53795~tplv-goo7wpa0wc-topic.webp)
5. 创建工具。
   1. 在本场景中，你需要创建三个工具，分别是截图、列出目录下文件、读取文件内容，具体如下图所示。
      ::::cols
      @col 33
      截图
      
      ![Image=400x435](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6bf059ca046c4908980177ad8a48499b~tplv-goo7wpa0wc-topic.webp)
      
      @col 33
      列出目录下文件
      
      ![Image=400x432](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2e8867e2c2fc437a9c2fc97a6535debb~tplv-goo7wpa0wc-topic.webp)
      
      @col 33
      读取文件内容
      
      ![Image=400x434](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/963c06a60853405ebab5551c390854f3~tplv-goo7wpa0wc-topic.webp)
      ::::
   2. 配置工具的输入参数、输出参数。在本场景中，三个工具的参数分别如下：
      <!-- @cols-width: 172,230,172,197 -->
      | **工具名称**  | **工具说明**  | **输入参数**  | **输出参数**  |
      | --- | --- | --- | --- |
      | 截图  | 直接对电脑屏幕进行全屏截图  | 无  | 图片  |
      | 列出目录下文件  | 列出指定目录下的所有文件  | 目录地址（字符串）  | 文件列表（数组）  |
      | 读取文件内容  | 读取指定文件的内容并返回  | 文件路径（字符串）  | 文件内容（字符串）  |
      ::::cols
      @col 33
      截图
      
      ![Image=400x286](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5f7950fbfe4c49cbaff4e68f53baef76~tplv-goo7wpa0wc-topic.webp)
      
      @col 33
      列出目录下文件
      
      ![Image=400x312](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a0dbc1ffb89442c98426a94d95a1ddbb~tplv-goo7wpa0wc-topic.webp)
      
      @col 33
      读取文件内容
      
      ![Image=400x298](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/14dcf14c992648d0b05e5fa7d604792c~tplv-goo7wpa0wc-topic.webp)
      ::::
6. 单击右上角的**发布**，发布端插件。

## 方式二：通过 JSON 和 YAML 导入插件 {#0c08191a}

当需要快速部署多个插件，或插件中工具的参数较多且较为复杂时，通过 JSON 和 YAML 文件导入插件的方式更为高效和灵活。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 在**资源库**页面右上角，选择 **+资源** > **插件**。
4. 在新建插件页面，单击右上角的命令图标，分别输入JSON 格式和 YAML 格式的命令脚本。
   本场景的 JSON 和 YAML 的完整示例代码请参见 [plugin.json](https://github.com/coze-dev/coze-cookbook/blob/main/examples/local_plugin/plugin.json) 和 [plugin.yaml](https://github.com/coze-dev/coze-cookbook/blob/main/examples/local_plugin/plugin.yaml)。
   ::::cols
   @col 50
   ![Image=400x478](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/89d6fdf13e364a2cb96cc2ada939db9f~tplv-goo7wpa0wc-topic.webp)
   
   @col 50
   ![Image=600x277](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0ef8ff4a1372415eb34e5dcd8419bada~tplv-goo7wpa0wc-topic.webp)
   ::::
   :::tip 说明
   * plugin.json：以 JSON 格式定义插件的基本信息，包括插件的名称、描述。
   * plugin.yaml：以 YAML 格式定义插件的配置信息，包括插件中所有工具的名称、描述、函数信息，以及工具的输入参数和输出参数。
   :::
5. 检查插件中的参数等相关配置，确认无误后，单击右上角的**发布**，发布端插件。
