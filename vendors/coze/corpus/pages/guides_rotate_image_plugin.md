> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

[图片旋转插件](https://www.coze.cn/store/plugin/7438921878921560102?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)用于对图片进行旋转操作。它能根据你指定的旋转角度，对输入的原始图片进行顺时针方向的旋转处理，轻松调整图片方向。

## 计费说明 {#2108c00a}

图片旋转插件根据插件调用次数计费，对应的计费项及单价请参考[插件费用](/coze_pro/plugin_fee)。

## 配置说明 {#c333e7bc}

图片旋转插件包含 image_rotate 工具。调用该工具时，你需要上传原始图片并指定旋转角度。

### 输入参数 {#e0156e6a}

输入参数说明如下表所示：

<!-- @cols-width: 205,638 -->
| **参数**  | **说明**  |
| --- | --- |
| 原图  | 设置原始图片来源，必填参数。 | \
| | | \
| | 支持上传图片或引用上游节点的输出参数。 | \
| | | \
| | :::tip 说明 | \
| | 在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。 | \
| | ::: | \
| | | \
| |   |
| 旋转角度  | 设置图片的旋转角度。 | \
| | | \
| | * 取值范围：[0~360]，即支持 360° 顺时针旋转。 | \
| | * 默认值：0，表示不旋转。  |

### 输出参数 {#66a0be89}

<!-- @cols-width: 162,672 -->
| **参数**  | **说明**  |
| --- | --- |
| data  | 图片旋转后的图片 URL。URL 有效期为 30 天，请及时转存。  |
| msg  | 执行插件时的状态描述或错误提示信息。  |

## 示例 {#b20e3c7c}

在工作流中调用图片旋转插件，旋转图片。其中指定图片旋转角度为 90 度。

![Image=750x717](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/46d75d4da0aa481983961b62404db2d6~tplv-goo7wpa0wc-topic.webp)

效果如下：

::::cols
@col 50
原始图片

   <div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/47c6220766d2451c8a6e10fd034e477a~tplv-goo7wpa0wc-image.image" width="200px" height="183px" />   </div>

@col 50
旋转后的图片

<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6a1833304a7c485684ae8b39924bd163~tplv-goo7wpa0wc-image.image" width="200px" height="217px" /></div>
::::

> * 旋转插件 ID：7438922485959245834
