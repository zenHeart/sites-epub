> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

[图片缩放插件](https://www.coze.cn/store/plugin/7438917029320491008?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)用于按照指定的长边或短边尺寸来等比例缩放图片。当你需要调整图片尺寸以满足不同场景需求（网页端图片、移动应用端图片等）时，可以自定义调整插件参数，以实现图片尺寸定制化处理。
## 注意事项 {#ea24b690}
缩小图片不会改变图片的清晰度，放大图片通常会使图像变模糊。
## 计费说明 {#6f6cc8b0}
图片缩放插件根据插件调用次数计费，对应的计费项及单价请参考[插件费用](/coze_pro/plugin_fee)。
## 配置说明 {#0fc3363a}
图片缩放插件包含 resize 工具。调用该工具时，你需要上传原始图片并设定缩放的最大尺寸。
### 输入参数 {#d90dc553}
输入参数说明如下表所示：
<!-- @cols-width: 205,638 -->
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
|最大尺寸 |设置图片缩放后的最大尺寸，必填参数。单位为像素。 |
| | | \
|缩放模式 |设置缩放模式，即按图片的长边或短边缩放。 |\
| | |\
| |* 1（默认值）：长边。 |\
| |* 2：短边。 |

### 输出参数 {#824a9edc}
<!-- @cols-width: 162,672 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|data |图片缩放后的图片 URL。URL 有效期为 30 天，请及时转存。 |
| | | \
|msg |执行插件时的状态描述或错误提示信息。 |

## 示例 {#28ba84b2}
在工作流中调用图片缩放插件，缩放图片。其中，指定按照长边（默认模式）等比例缩小图片，并指定缩小后的图片长边为 100 像素。
![Image=811x779](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ff46fc34ba8a483aa7bd79db4e515ac0~tplv-goo7wpa0wc-image.image)
效果如下：

::::cols
@col 50
原始图片

   <div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/47c6220766d2451c8a6e10fd034e477a~tplv-goo7wpa0wc-image.image" width="304px" height="279px" />   </div>





@col 50
缩放后的图片
![Image=100x92](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bc7a2c6a410e408ba073cced42a2dc9d~tplv-goo7wpa0wc-image.image)


::::

> * 缩放插件 ID：7438918747382890511
