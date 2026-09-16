> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

[Doubao-图像生成插件](https://www.coze.cn/store/plugin/7449356651498471463?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)用于根据输入的文本描述生成全新的图像或编辑指定的图像。

Doubao-图像生成插件包含 gen_image 工具、seed_edit 工具。不同工具的配置项不同，生成结果也不同。

## 使用限制 {#38b08345}

扣子主账号内所有子账号共享**Doubao-图像生成插件**的并发限制，其值为 5。

## 计费说明 {#e3e196a3}

Doubao-图像生成插件根据插件调用次数计费，对应的计费项及单价请参考[插件费用](/coze_pro/plugin_fee)。

:::tip 说明
Doubao-图像生成插件内包含多个工具，调用这些工具的次数将共同计入该插件的免费额度。
:::

## gen_image 工具 {#78e2361d}

gen_image 工具支持根据输入的提示词生成图片。

### 效果展示 {#2d5c2039}

::::cols
@col 50
提示词

```Plain Text
一个中国年轻女孩,白色背景,黑色头发,长波 波头,正面脸,特写,工作室灯光,工作室,侧 光,化妆肖像,穿白色上衣
```

@col 50
生成图片

![Image=512x512](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1926c744dc784092ac463c13128983e1~tplv-goo7wpa0wc-topic.webp)
::::

### 配置说明 {#6dd71bb6}

Doubao-图像生成插件中包含 gen_image 工具。配置该工具时，你需要配置 `prompt` 参数，用于输入生成图片的提示词；配置 `req_schedule_conf` 参数，用于选择模型配置。你还可以进一步配置参数 `height`、`width`，用于指定图片的高度和宽度。

#### 输入参数 {#019aae4b}

输入参数说明如下表所示：

<!-- @cols-width: 173,666 -->
| **参数**  | **说明**  |
| --- | --- |
| prompt  | 设置用于生成图像的提示词 ，支持中英文。必填参数。 | \
| | | \
| | 如果希望在图片中展示对应的文字，可以在提示词中使用双引号包裹文字，例如提示词为`生成一张圣诞节海报，上面写着 “Merry Christmas”`。  |
| req_schedule_conf  | 选择模型配置，必填参数。 | \
| | | \
| | * general_v20_9B_pe：图文匹配度更好，结构表现更好。 | \
| | * general_v20_9B_rephraser：美感更好，出图多样性更多。  |
| height  | 设置生成图像的高度。 | \
| | | \
| | * 取值范围：[256, 768]。 | \
| | * 默认值：512。 | \
| | * 单位：像素。  |
| width  | 设置生成图像的宽度。 | \
| | | \
| | * 取值范围：[256, 768]。 | \
| | * 默认值：512。 | \
| | * 单位：像素。  |

#### 输出参数 {#953a58b2}

<!-- @cols-width: 162,672 -->
| **参数**  | **说明**  |
| --- | --- |
| log_id  | 日志 ID。  |
| msg  | 执行插件时的状态描述或错误提示信息。  |
| code  | 状态码。  |
| data.message  | data 为 Object 类型。 | \
| | | \
| | `data.message` 表示图片生成时的返回信息。  |
| data.time_elapsed  | 图片生成所需的时间。  |
| data.code  | 图片生成时的状态码。  |
| data.data.image_urls  | 图片生成后的图片链接。URL 有效期为 30 天，请及时转存。 | \
| | | \
| | `image_urls` 为 Array 类型，当后续节点需要 String 类型的 URL 时，你需要先提取数组中的 URL，具体操作请参考[如何从数组类型的输出参数中提取字符串？](/guides/workflow_faq#70ad28e1)。  |
| data.data.pe_result  | 图片的描述信息。  |

## seed_edit 工具 {#f2a046bb}

seed_edit 工具支持根据提示词修改指定图片。

### 效果展示 {#5967ffc3}

::::cols
@col 33
提示词

```Plain Text
改成红色衣服，短发
```

@col 33
原始图片

<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/52ac366bd0dc42178dd636bc716d7c6f~tplv-goo7wpa0wc-image.image" width="20000px" height="20000px" /></div>

@col 33
生成图片

<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/14951514abe44af694bae04146ebdba0~tplv-goo7wpa0wc-image.image" width="20000px" height="20000px" /></div>
::::

### 配置说明 {#d248fe2a}

Doubao-图像生成插件中包含 seed_edit 工具。配置该工具时，你需要配置 `prompt` 参数，用于输入编辑图片的提示词；配置 `image_url` 参数，用于上传原始图片。

#### 输入参数 {#bc5aa88e}

输入参数说明如下表所示：

<!-- @cols-width: 173,666 -->
| **参数**  | **说明**  |
| --- | --- |
| image_url  | 设置原始图片来源，必填参数。 | \
| | | \
| | 支持上传图片或引用上游节点的输出参数。 | \
| | | \
| | :::tip 说明 | \
| | 在调试节点效果时，建议上传一张示例图，用于调整参数配置，并仅测试该节点，快速查看效果。 | \
| | ::: | \
| | | \
| | 图片要求： | \
| | | \
| | * 图片格式：仅支持 JPG（JPEG）、PNG，建议使用 JPG 格式。 | \
| | * 图片大小：小于 4.7MB，小于 4096*4096 px。 | \
| | * 长边与短边比例在 3 以内，超出此比例或比例相对极端，会导致报错。  |
| prompt  | 设置用于编辑图像的提示词。 | \
| | | \
| | * 建议使用单指令。 | \
| | * 局部编辑时，尽量输入精准的提示词，尤其是画面有多个实体的时候，描述清楚对谁做什么。 | \
| | * 建议长度小于等于 120 字符，提示词过长有概率出图异常或不生效。  |

#### 输出参数 {#f43980b7}

<!-- @cols-width: 162,672 -->
| **参数**  | **说明**  |
| --- | --- |
| log_id  | 日志 ID。  |
| msg  | 执行插件时的状态描述或错误提示信息。  |
| code  | 状态码。  |
| data.message  | data 为 Object 类型。 | \
| | | \
| | `data.message` 表示图像生成时的相关信息。  |
| data.time_elapsed  | 编辑图像所花费的时长。  |
| data.code  | 编辑图像时的业务状态码。  |
| data.data.vlm_result  | 图像编辑结果的描述。  |
| data.data.image_urls  | 图像编辑后的链接。URL 有效期为 20 天，请及时转存。 | \
| | | \
| | * 输出图片的分辨率与原始图片的宽高比有关，与原始分辨率的大小无关。 | \
| | * 输出图片的宽高比与原图接近，单边长度范围为 512～1536 px。 | \
| | | \
| | `image_urls` 为 Array 类型，当后续节点需要 String 类型的 URL 时，你需要先提取数组中的 URL，具体操作请参考[如何从数组类型的输出参数中提取字符串？](/guides/workflow_faq#70ad28e1)。  |

> * Doubao-图像生成插件 ID：7449357316584996883
