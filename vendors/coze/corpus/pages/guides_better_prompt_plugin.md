> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

[提示词优化插件](https://www.coze.cn/store/plugin/7439196919706075136?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)用于智能优化图像提示词。当你需要生成特定主题、风格或内容的图像时，可先使用该插件优化提示词。该插件通过先进的算法和自然语言处理技术，能够对你所输入的提示词进行分析和处理，使其更加准确、生动，从而帮助你在生成图像时获得更符合预期的高质量图像。
## 计费说明 {#7643493e}
提示词优化插件根据插件调用次数计费，对应的计费项及单价请参考[插件费用](/coze_pro/plugin_fee)。
## 配置说明 {#4324c709}
提示词优化插件包含 sd_better_prompt 工具。调用该工具时，你输入图像提示词。
### 输入参数 {#ff93b464}
输入参数说明如下表所示：
<!-- @cols-width: 205,627 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|提示词 |输入图像提示词。 |

### 输出参数 {#11874488}
<!-- @cols-width: 204,627 -->
| | | \
|**参数** |**说明** |
|---|---|
| | | \
|data |优化后的图像提示词。 |
| | | \
|msg |执行插件时的状态描述或错误提示信息。 |

## 示例 {#02726095}
在工作流中调用提示词优化插件，优化提示词 `生成一张圣诞图`。优化后的提示词为 `Best quality, ultra-detailed, masterpiece, 4K, hyper detailed, realistic photo, Christmas scene, festive lighting, beautiful color composition`。
![Image=750x396](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/02e52d5b22de418f9d52c09fe56d04b9~tplv-goo7wpa0wc-image.image)

> * 提示词优化插件 ID：7439197952104710144
