> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

[智能抠图插件](https://www.coze.cn/store/plugin/7438917083918024738?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)支持自动识别图片中的主体部分并去除背景，实现智能抠图，输出透明背景图或蒙版矢量图。同时，你也可以输入提示词，自定义抠图的对象，满足更精准的抠图需求。
## 使用限制 {#daab689b}
扣子主账号内所有子账号共享**智能抠图插件**的并发限制 ，其值为 4。
## 计费说明 {#a2442b30}
智能抠图插件根据插件调用次数计费，对应的计费项及单价请参考[插件费用](/coze_pro/plugin_fee)。
## 配置说明 {#be909aed}
智能抠图插件包含 cutout 工具。调用该工具时，你需要上传原始图片。如果需要精细化抠图，可配置提示词，自定义抠图的对象。
### 输入参数 {#421357b7}
输入参数说明如下表所示：
<!-- @cols-width: 186,666 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|上传图 |设置原图来源，必填参数。 |\
| |支持上传图片或引用上游节点的输出参数。 |\
| |:::tip 说明 |\
| |在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。 |\
| |::: |
| | | \
|产物尺寸 |设置输出图的尺寸。 |\
| | |\
| |* 抠图结果尺寸：使用抠图结果的尺寸，去除透明部分。 |\
| |* 原图尺寸：使用原图尺寸。 |
| | | \
|输出图模式 |设置输出图的模式。 |\
| | |\
| |* 透明背景图：输出图像的背景为透明。 |\
| |* 蒙版矢量图：输出图像为矢量格式的蒙版。 |
| | | \
|提示词 |用于定义抠图内容的提示词。 |\
| |如果不填，插件会自动识别图片中的主体部分。 |

### 输出参数 {#af66dd9a}
<!-- @cols-width: 162,672 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|data |智能抠图后的图片 URL。URL 有效期为 30 天，请及时转存。 |\
| |在输入参数中，设置**输出图模式**为**透明背景图**时，`data` 参数才生效。 |
| | | \
|mask |抠图区域的蒙板矢量图 URL。URL 有效期为 30 天，请及时转存。 |\
| |在输入参数中，设置**输出图模式**为**蒙版矢量图**时，`mask` 参数才生效。 |
| | | \
|msg |执行插件时的状态描述或错误提示信息。 |

## 示例 {#13429710}
在工作流中调用智能抠图插件，完成抠图。其中，指定**输出图模式**为**透明背景图**。
![Image=577x574](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/48dc004f419f4427bf97d0426509d62d~tplv-goo7wpa0wc-image.image)
效果如下：

::::cols
@col 50
原始图片
<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f5349faaa16b4193a14f718524b1ab32~tplv-goo7wpa0wc-image.image" width="20000px" height="20075px" /></div>




@col 50
抠图后的图片
<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3137669e7e30425eae17b031b7d8a010~tplv-goo7wpa0wc-image.image" width="20000px" height="28507px" /></div>


::::




> * 智能抠图插件 ID：7438919188246413347
