> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程支持低代码智能体以卡片形式发送消息，提升低代码智能体的聊天交互体验。

:::notice 注意
* 目前卡片仅在豆包客户端、飞书客户端内生效。
* 仅工作流和插件支持添加卡片。
* 在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 权限说明 {#b4766e45}

卡片暂不支持多人协作。只有卡片的所有者支持编辑和删除自己创建的卡片，工作空间所有者、管理员以及普通成员都没有权限编辑和删除其他成员创建的卡片。

## 使用官方卡片 {#bbc505d3}

扣子编程提供了卡片模板，你可以选择适用的模板，并根据页面提示配置卡片参数。

1. 在智能体**编排**页面找到要配置卡片的工作流或插件，单击**卡片**图标。
   ![Image=638x105](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/32e9a4567b4e40b7b7cdfc5ec95d79eb~tplv-goo7wpa0wc-topic.webp)
2. 配置卡片。
   1. 选择卡片模板。
      ![Image=204x342](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e639abd684104e759e52fec915fcd550~tplv-goo7wpa0wc-topic.webp)
   2. 选择卡片样式及配置对应参数。
      <!-- @cols-width: 103,427,281 -->
      | **卡片样式**  | **说明**  | 配置示例  |
      | --- | --- | --- |
      | 单张卡片  | 仅展示一张卡片，适用于展示单一内容。 | ![Image=950x479](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6ac40f1b6da3451cb72d538c1e9f7d17~tplv-goo7wpa0wc-topic.webp)  | \
      | | | | \
      | | 选择单张卡片时，需完成如下配置： | | \
      | | | | \
      | | * **为卡片内的元素绑定数据**：为不同的元素绑定不同的变量。例如为卡片标题绑定 `data.doc_results[0].title` 变量，卡片标题将展示数组第一个元素中的 `title` 属性。 | | \
      | |    单张卡片只支持绑定数组中的第一个元素。 | | \
      | | * **点击卡片跳转**：单击卡片时，是否支持跳转到对应的 URL 页面。 | | \
      | |    打开**点击卡片跳转**开关，并绑定表示 URL 的变量。设置完成后，当你单击卡片时，将跳转到对应的 URL 页面。  | |
      | 竖项卡片  | 支持展示多张卡片。例如搜索到多条新闻时，可通过卡片列表依次展示新闻内容。 | ![Image=982x648](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8227a30cd422425b9149069a8c300413~tplv-goo7wpa0wc-topic.webp)  | \
      | | | | \
      | | * **卡片列表最大长度**：卡片列表的最大数量，最大值为 20。 | | \
      | | * **为卡片整体绑定一个数组**：为卡片绑定一个数组类型的变量，例如 `data.doc_results`。 | | \
      | | * **为卡片内的列表项绑定数据**：为不同的卡片元素绑定不同的变量。例如为卡片标题绑定 `title`，即表示绑定 `data.doc_results` 数组中 `title` 属性。 | | \
      | | * **点击卡片跳转**：选择单击卡片时，是否支持跳转到对应的 URL 页面。 | | \
      | |    打开**点击卡片跳转**开关，并绑定表示 URL 的变量。设置完成后，当你单击卡片时，将跳转到对应的 URL 页面。  | |
   3. 单击**确认**。
      配置完成后，你在与智能体对话时，智能体将以卡片形式回复消息。      


## 使用自定义卡片 {#49d1ad95}

如果扣子编程官方提供的卡片模板不能满足你的需求，你可以自定义卡片样式。

### 步骤 1 ：创建卡片 {#6cb8c8a9}

1. 在**智能体回复卡片配置**页面中，单击**新增，​**页面将跳转至卡片编辑页面。
2. 在页面左侧的**卡片**页签内，选择模板或者自行拖拽组件构建卡片样式。
   * **模板**：双击使用模板，你可以基于模板构建属于你的卡片。
      ![Image=1520x786](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/93bcfe26144846d6ad4530a39f597ccb~tplv-goo7wpa0wc-topic.webp)
   * **组件**：通过拖拽布局组件和基础组件，自定义卡片内容。
   * **结构**：以导航树的形式展示卡片的组件布局。
3. 在页面左侧的**变量**页签内，创建变量。
   为卡片组件创建变量，智能体会根据插件或工作流的返回值展示对应的内容。例如，新增 `newMovies` 变量，Array 类型，默认值如下所示。
   ![Image=445x331](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/043a175a425e4cea91e4ef35e5ca892c~tplv-goo7wpa0wc-topic.webp)
4. 为卡片组件绑定变量。
   在卡片画布内，选中需要添加变量的组件，然后在组件**基本配置**的**内容**区域，单击**变量**图标并选择要使用的变量。
   ![Image=768x177](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f29247bd6cdb4acc8ad5a344798c3422~tplv-goo7wpa0wc-topic.webp)
5. 在页面右上角单击**预览**，扫描二维码在豆包或飞书中查看预览效果。
6. 在页面右上角单击**发布**。

### 步骤 2 ：为卡片绑定数据 {#a90127aa}

发布自定义卡片后，你需要为卡片绑定数据，例如插件的返回参数。

1. 在**智能体回复卡片配置**对话框的**工作空间卡片**页签中，单击你已创建的卡片。
2. 为卡片绑定数据。
   例如绑定淘票票（GetMovieAndShow）插件的返回参数 `data.return_value`。
   ![Image=585x365](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cee00dcb5b8a44718e62e3f94dfa42c8~tplv-goo7wpa0wc-topic.webp)
   当你在智能体中查询最近上映的电影时，智能体将以卡片形式回复。
   ![Image=224x244](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/49db68867ecc41aeb6e2ad12517a21be~tplv-goo7wpa0wc-topic.webp)   


## 示例 {#a53e3d8a}

例如搭建一个新闻助手智能体，其中添加头条搜索插件搜索新闻，并为插件的输出内容配置卡片，以卡片形式回复新闻内容。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**创建** > **创建智能体**。
3. 根据页面提示，创建一个新智能体。
4. 在智能体**编排**页面，添加**头条搜索**插件，并单击其对应的**绑定卡片数据**图标。
   ![Image=739x135](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/44671d4bf42e4cc9948e63cdd41cf927~tplv-goo7wpa0wc-topic.webp)
5. 在智能体**回复卡片配置**对话框，完成如下配置。
   1. 选择扣子编程提供的某款官方卡片，并选择**竖向列表**。
   2. 设置**卡片列表最大长度**为 **5**。
   3. 在**为卡片整体绑定一个数组**中，绑定数组`data.doc_results`。
      即为卡片绑定新闻插件的搜索结果集合。
   4. 为卡片内的列表项绑定数据。
      * **①标题**：为卡片标题绑定变量 `title`，即绑定 `data.doc_results` 数组中 `title` 字段，用于展示搜索到的新闻标题。
      * **②内容**：为卡片内容绑定变量 `summary`，即绑定 `data.doc_results` 数组中 `summary` 字段，用于展示搜索到的新闻内容。
   5. 设置卡片跳转链接。
      打开**点击卡片跳转**开关，并设置卡片跳转链接为 `url`。设置完成后，当你单击卡片时，将跳转到对应的 URL 页面。
   6. 单击**确认**。
      ![Image=556x424](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f258796ad2794a7aaa887c8b9be87eb7~tplv-goo7wpa0wc-topic.webp)
6. 查看卡片效果。
   当你在智能体中查询今天的科技新闻时，智能体将以卡片形式回复。单击目标卡片，将打开对应的新闻网页。
   ![Image=440x425](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0d1d07548cd64350b0446a77c83f6c23~tplv-goo7wpa0wc-topic.webp)
