> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

[风格滤镜插件](https://www.coze.cn/store/plugin/7438921896516763698?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)用于为图片添加各种独特的滤镜效果，包括毛毡、粘土、积木、美漫、玉石、搞笑涂鸦、工笔画、水彩画和僵尸 3D 等风格。
## 使用限制 {#ce087cee}
扣子主账号内所有子账号共享**风格滤镜插件**的并发限制 ，其值为 4。
## 计费说明 {#3b48fc64}
风格滤镜插件根据插件调用次数计费，对应的计费项及单价请参考[插件费用](/coze_pro/plugin_fee)。
## 配置说明 {#3f8ef449}
风格滤镜插件包含 style_transfer 工具。调用该工具时，你需要上传原始图片并指定滤镜风格。
### 输入参数 {#f7f6fb67}
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
|风格 |设置风格滤镜，必填参数。支持设置为毛毡、粘土、积木、美漫、玉石、搞笑涂鸦、工笔画、水彩画和僵尸3D等风格。默认值为毛毡。 |

### 输出参数 {#6a3550ac}
<!-- @cols-width: 162,672 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|data |添加滤镜后的图片 URL。URL 有效期为 30 天，请及时转存。 |
| | | \
|msg |执行插件时的状态描述或错误提示信息。 |

## 示例 {#69f0588e}
在工作流中调用风格滤镜插件，为图片添加滤镜。其中，指定滤镜风格为毛毡。
![Image=460x426](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7dee6a39be84406c9ccc7ee6c7cc1014~tplv-goo7wpa0wc-image.image)
效果如下：

::::cols
@col 50
原始图片

   <div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/47c6220766d2451c8a6e10fd034e477a~tplv-goo7wpa0wc-image.image" width="200px" height="183px" />   </div>





@col 50
添加滤镜后的图片
<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b508379371354ea9a44eee7bd457c7f5~tplv-goo7wpa0wc-image.image" width="200px" height="183px" /></div>



::::



> * 风格滤镜插件 ID：7438923452805054473
