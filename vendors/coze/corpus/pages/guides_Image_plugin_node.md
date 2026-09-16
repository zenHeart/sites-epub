> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程提供了丰富的图像处理插件，你可以在低代码工作流中添加不同的图像处理插件节点，实现抠图、优化图像提示词、裁剪图片、美颜、画质提升等功能。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制​**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 使用限制 {#34d5f35c}

<!-- @cols-width: 210,581 -->
| **限制**  | **说明**  |
| --- | --- |
| 并发限制  | 扣子主账号及其所有子账号共享并发限制，具体的并发限制请参考[插件费用](/coze_pro/plugin_fee)。  |
| 图片有效期  | 大多数图像处理插件输出的图片为链接格式，有效期为 1 年，建议在到期前及时保存。 | \
| | | \
| | :::tip 说明 | \
| | [Doubao-图像生成插件](/guides/doubao_image_plugin)中的 SeedEdit 工具输出的图片有效期约为 20 天。 | \
| | ::: | \
| | | \
| |   |

## 节点说明 {#2a212d4c}

在 AI 智能处理场景下，你可以在低代码工作流中添加各个图像处理节点来处理图像，以优化图像质量和满足特定需求。例如添加抠图插件节点分离主体与背景；添加画质提升插件节点增强图片清晰度；添加图像美颜插件节点优化人像图片等。

不同图像处理插件节点的输入参数和输出参数有所差异，基本配置流程为上传原始图片，根据各个插件特有参数完成配置，最终获取处理后的图片。

![Image=532x170](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ea56434d86c444d7ad1c5e618bb141d5~tplv-goo7wpa0wc-topic.webp)

其中官方插件使用说明可参考：

* [添加文字插件](/guides/add_text_to_image_plugin)
* [提示词优化插件](/guides/better_prompt_plugin)
* [图片裁剪插件](/guides/cut_image_plugin)
* [图片叠图插件](/guides/add_image_to_image_plugin)
* [图片缩放插件](/guides/resize_image_plugin)
* [图片旋转插件](/guides/rotate_image_plugin)
* [图像美颜插件](/guides/facepretty_plugin)
* [图像调整插件](/guides/change_image_plugin)
* [ByteArtist 插件](/guides/byteartist_plugin)
* [背景替换插件](/guides/change_background_plugin)
* [宠物风格化插件](/guides/pet_image_plugin)
* [Doubao-图像生成插件](/guides/doubao_image_plugin)
* [风格滤镜插件](/guides/style_transfer_plugin)
* [光影融合插件](/guides/light_plugin)
* [画质提升插件](/guides/improve_image_quality_plugin)
* [指令编辑插件](/guides/instruction_editing_plugin)
* [智能抠图插件](/guides/cutout_plugin)
* [智能扩图插件](/guides/intelligent_image_expansion_plugin)
* [智能绘图_文生图插件](/guides/gen_image_pay_plugin)
* [火山图像增强插件](/guides/image_enhancement_plugin)
* [图片超分辨率插件](/guides/image_super_resolution_plugin)
* [商品图像分割插件](/guides/product_image_segmentation_plugin)
* [Doubao-Seedream-3.0 插件](/guides/image_generation_seedream3_plugin)
* [Doubao-Seedream-4.0 插件](/guides/doubao_seedream_4_plugin)

## 配置图像处理插件节点 {#e88a9f43}

不同图像处理插件节点对应的配置不同。本文以抠图插件为例，介绍图像处理插件节点的基本配置。

![Image=936x695](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/35861e51b9424c8796aa68f2eda8fc64~tplv-goo7wpa0wc-topic.webp)

### 输入 {#db86d093}

图像处理插件节点的输入参数。以抠图插件节点为例，输入参数如下所示：

* **上传图**：设置原图来源，支持上传图片或引用上游节点的输出参数。
* **输出图模式**：设置输出图的模式。可选项包括透明背景图和蒙版矢量图。
   * **透明背景图**：输出图像的背景为透明。
   * **蒙版矢量图**：输出图像为矢量格式的蒙版。
* **提示词**：用于定义抠图内容的提示词。如果不填，插件会自动识别图片中的主体部分。

### 输出 {#fbd97df2}

抠图插件节点的输出参数固定为：

* **data**：抠图后的最终图像。通常是一个公开可访问的 URL 链接。在输入参数中，设置**输出图模式**为**透明背景图**时，`data` 参数才生效。
* **mask**：抠图区域的蒙版矢量图。在输入参数中，设置**输出图模式**为**蒙版矢量图**时，`mask` 参数才生效。
* **msg**：节点执行状态，success 表示处理成功。

## 示例 {#33e63ea2}

例如添加一个抠图工作流，通过头条图片搜索（ToutiaoPictureSearch）插件从互联网中搜索图片，并通过智能抠图（cutout）插件对搜索结果进行智能抠图，最终返回抠图后的图像和搜索到的原始图像。重要配置说明如下：

* 智能抠图插件的输入参数
   * **上传图**：设置为变量，即引用 **ToutiaoPictureSearch** 节点的输出参数 `display_url`，获取搜索到的图片。
   * **输出图模式**：选中**透明背景图**。
* 结束节点的输出变量
   * output：引用 **cutout** 节点的输出变量 `data`，即返回截图后的图像。
   * output1：引用 **ToutiaoPictureSearch** 节点的输出参数 `display_url`，即返回通过头条图片搜索插件搜索到的原始图像。

![Image=740x232](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a2a7db558147401a8596b72136ffdaed~tplv-goo7wpa0wc-topic.webp)
