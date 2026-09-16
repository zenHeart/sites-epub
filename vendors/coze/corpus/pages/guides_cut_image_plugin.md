> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

[图片裁剪插件](https://www.coze.cn/store/plugin/7438917857070743588?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)用于对图片进行自定义裁剪。当你需要从原始图片中裁剪出特定区域（例如风景照中的特定风景、人物照中的脸部特写等）时，可以调用该插件，定义裁剪的起始位置、宽度、高度等属性来指定裁剪的区域。
## 使用限制 {#540a6ae5}
扣子主账号内所有子账号共享**图片裁剪插件**的并发限制 ，其值为 4。
## 计费说明 {#a1038057}
图片裁剪插件根据插件调用次数计费，对应的计费项及单价请参考[插件费用](/coze_pro/plugin_fee)。
## 配置说明 {#857a6050}
图片裁剪插件绑定了 cut_image 工具进行图片裁剪。裁剪前，你需要选择裁剪点的初始位置，还可以设置坐标轴偏移量 `x` 和 `y` 调整裁剪起始点的位置，然后指定`高度`和`宽度`来确认图片的裁剪区域，最终完成图片的裁剪。

::::cols
@col 50
**裁剪起始点**
![Image=258x282](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f67301e312da40999c338a9583894236~tplv-goo7wpa0wc-image.image)



@col 50
**裁剪方式**
![Image=268x320](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/737ce520cee24697b630b7bcd355f122~tplv-goo7wpa0wc-image.image)

::::

### 输入参数 {#ab7664d5}
输入参数说明如下表所示：
<!-- @cols-width: 216,638 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|原图 |设置原始图片来源，必填参数。 |\
| |支持上传图片或引用上游节点的输出参数。 |\
| |:::tip 说明 |\
| |在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。 |\
| |::: |
| | | \
|高度 |设置裁剪后的图片高度。 |\
| | |\
| |* 取值范围：[0,图片原始高度]。 |\
| |* 单位：px。 |\
| |* 默认值：图片原始高度。 |
| | | \
|位置 |设置裁剪点的起始位置。 |\
| | |\
| |* nw（默认值）：左上。 |\
| |* north：中上。 |\
| |* ne：右上。 |\
| |* west：左中。 |\
| |* center：中部。 |\
| |* east：右中。 |\
| |* sw：左下。 |\
| |* south：中下。 |\
| |* se：右下。 |
| | | \
|宽度 |设置裁剪后的图片宽度。 |\
| | |\
| |* 取值范围：[0,图片原始宽度]。 |\
| |* 单位：px。 |\
| |* 默认值：图片原始宽度。 |
| | | \
|x |设置裁剪起始点的横坐标偏移量。 |\
| | |\
| |* 设置为正值，表示横坐标向右偏移。 |\
| |* 设置为负值，表示横坐标向左偏移。 |\
| |* 单位：px。 |
| | | \
|y |设置裁剪起始点的纵坐标偏移量。 |\
| | |\
| |* 设置为正值，表示纵坐标向下偏移。 |\
| |* 设置为负值，表示纵坐标向上偏移。 |\
| |* 单位：px。 |

### 输出参数 {#e559d827}
:::tip 说明
关闭指定输出参数的**开启**功能后，该输出参数将不会被返回给大模型。
:::
<!-- @cols-width: 212,647 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|data |被裁剪后的图片 URL。URL 有效期为 30 天，请及时转存。 |
| | | \
|msg |执行插件时的状态描述或错误提示信息。 |

## 示例 {#700134b0}
在工作流中调用图片裁剪插件，裁剪图片。其中，指定左上角（nw）为起始点，x 轴偏移量为 100 像素，y 轴偏移量为 100 像素，裁剪后图片的宽度和高度均为 200 像素。
![Image=831x853](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cb1e97c2b9794ecbabfd9aff87b7c14c~tplv-goo7wpa0wc-image.image)
裁剪后效果

::::cols
@col 33
原始图片
![Image=200x231](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8034b7a51ed342a0ae72ceaed274ca4b~tplv-goo7wpa0wc-image.image)



@col 33
 确认裁剪位置和尺寸
![Image=930x913](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/627e72fb00014085951b61166adf669d~tplv-goo7wpa0wc-image.image)



@col 33
裁剪后的图片
![Image=200x200](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f4f013406d094b79add4cf6266110312~tplv-goo7wpa0wc-image.image)


::::

> * 裁剪插件 ID：7438919975403880460
