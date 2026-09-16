> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

在扣子编程中搭建的智能体和 AI 应用都是基于模型技术开发的应用程序。通过扣子编程，你可以便捷使用各个厂商提供的模型服务，个人版用户可使用豆包、DeepSeek 等模型服务，企业标准版、企业旗舰版用户在此基础上还可以使用火山引擎方舟平台的其他模型资源，例如豆包视觉模型、豆包文生图模型等。

你可以通过智能体、工作流节点、插件等方式使用模型服务：

* 智能体和工作流节点：为你的智能体选择一个模型，用于灵活调用技能、知识和数据，响应用户的问题。大模型等工作流节点中也可以设置模型和版本，由指定的模型完成某个工作流环节。
* 插件：扣子编程将部分模型直接封装为官方插件，帮助你针对性地处理数据。例如为智能体绑定**图片理解**插件，回答用户关于指定图片的问题。

本文档介绍扣子编程中可使用的各种模型服务。

## 费用说明 {#d58af04a}

在扣子编程使用模型服务，根据模型的类型与版本收取不同的费用。详细计费策略，可参考[模型费用](/coze_pro/model_fee)。

* **方舟模型**：企业标准版、企业旗舰版用户可使用火山方舟提供的模型，根据输入和输出的 Token 数量计费。具体费用由火山方舟收取，价格可参考[火山方舟文档](https://www.volcengine.com/docs/82379/1099320)。
* **扣子模型**：所有用户均可使用扣子提供的豆包模型，根据输入和输出的 Token 数量扣减积分。具体费用由扣子统一收取，价格可参考[模型费用](/coze_pro/model_fee)。除豆包模型以外，其他扣子模型免费限额使用，超出免费额度后次日才能继续使用。

## 方舟模型 {#2479708d}

购买企业标准版、企业旗舰版之后，你可以开通火山引擎方舟平台提供方舟模型版本，例如豆包语音识别模型、语音合成模型、DeepSeek 模型等，可接入的模型列表参考[方舟模型发布公告](https://www.volcengine.com/docs/82379/1159178)，接入模型的方式可参考[接入火山方舟模型](/guides/ark_model)。

## 扣子模型 {#4bb356a3}

扣子模型指扣子编程面向用户统一提供的模型服务。

:::tip 说明
* **阶跃星辰 · 1.5v · 视频理解**、**阶跃星辰 · 1v · 图片理解**等部分模型目前仅供扣子付费套餐用户使用。
* 模型调用速度取决于模型本身的性能，不受扣子订阅套餐类型的影响。
:::

<!-- @cols-width: 100,214,105,106,239,435 -->
| **供应商**  | **模型名称**  | **模型版本**  | **模型类型**  | **高级功能配置**  | **说明**  |
| --- | --- | --- | --- | --- | --- |
| 字节跳动  | 豆包·2.0·Code  | doubao-seed-2.0-code  | 多模态模型  | * 上下文缓存（Responses API） | 豆包·2.0·Code 面向企业级编程需求优化，在 Seed 2.0 优秀的 Agent、VLM 能力基础上，特别增强了代码能力，不仅前端能力表现出众，也对企业常见的多语言编码需求做了特别优化，适合接入各种 AI 编程工具使用。  | \
| | | | | * 开启/关闭深度思考 | | \
| | | | | * 调节深度思考的程度  | |
|^^| 豆包·2.0·pro  | doubao-seed-2.0-pro  | 多模态模型  | * 上下文缓存（Responses API） | 豆包·2.0·pro 是旗舰级全能通用模型，面向 Agent 时代的复杂推理与长链路任务执行场景。强调多模态理解、长上下文推理、结构化生成与工具增强执行。复杂指令与多约束执行能力突出，可稳定应对多步复杂规划、复杂图文推理、视频内容理解与高难度分析等场景。  | \
| | | | | * 开启/关闭深度思考 | | \
| | | | | * 调节深度思考的程度  | |
|^^| 豆包·2.0·lite  | doubao-seed-2.0-lite  | 多模态模型  | * 上下文缓存（Responses API） | 豆包·2.0·lite 是面向高频企业场景兼顾性能与成本的均衡型模型，综合能力超越上一代Doubao-Seed-1.8。胜任非结构化信息处理、内容创作、搜索推荐、数据分析等生产型工作，支持长上下文、多源信息融合、多步指令执行与高保真结构化输出。在保障稳定效果的同时显著优化成本。  | \
| | | | | * 开启/关闭深度思考 | | \
| | | | | * 调节深度思考的程度  | |
|^^| 豆包·2.0·mini  | doubao-seed-2.0-mini  | 多模态模型  | * 上下文缓存（Responses API） | 豆包·2.0·mini 面向低时延、高并发与成本敏感场景，强调快速响应与灵活推理部署。模型效果与Doubao-Seed-1.6相当。支持256k上下文、4档思考长度和多模态理解，适合成本和速度优先的轻量级任务。  | \
| | | | | * 开启/关闭深度思考 | | \
| | | | | * 调节深度思考的程度  | |
|^^| 豆包·通用模型·Lite  | Doubao-lite  | 文本模型  | 无  | 轻量级大模型，拥有极致的响应速度，更好的性价比，为客户不同场景提供更灵活的选择。支持 32k 上下文窗口的推理和精调。  |
| 深度求索  | DeepSeek-V3 工具调用  | V3 functionCall 版本  | 文本模型  | 无  | V3 functionCall 版本，支持在Single-Agent模式下调用各类扣子工具（插件、工作流、知识库等）。 | \
| | | | | | | \
| | | | | | 免费使用，每个用户限制最多 80 条对话/天。  |
| 阶跃星辰  | 阶跃星辰 · 1.5v · 视频理解  | step-1.5v-mini  | 多模态模型  | 无  | 阶跃星辰·1.5v 是一款多模态大模型，专注于视频理解和图像分析。该模型具备强大的感知能力，能够准确识别视频中的物体、人物及环境，并理解整体氛围和情感。  |
|^^| 阶跃星辰 · 1v · 图片理解  | step-1v-8k  | 多模态模型  | 无  | 阶跃星辰·1v 是一款多模态大模型，专注于图像分析。该模型具备强大的感知能力，能够准确识别图片的物体、人物及环境，并理解整体氛围和情感。  |
| 月之暗面  | Kimi-8k  | moonshot-v1-8k  | 文本模型  | 无  | Kimi（8K）模型提供高容量的语言处理能力，适合处理大规模文本数据。它具备视觉能力、广泛的知识面和先进的推理能力，能准确地解决复杂问题。  |
|^^| Kimi-32k  | moonshot-v1-32k  | 文本模型  | 无  | Kimi（32K）模型进一步扩展了处理能力，适用于更复杂的语言任务和更大的数据集。它具备视觉能力、广泛的知识面和先进的推理能力。  |
|^^| Kimi-128k  | moonshot-v1-128k  | 文本模型  | 无  | Kimi（128K）模型拥有极高的参数量，能够处理极其复杂的语言理解和生成任务。它具备视觉能力、广泛的知识面和先进的推理能力。  |

## 自定义模型 {#f83dd184}

购买扣子企业旗舰版后，你可以将自部署或第三方在线模型集成至扣子编程，进一步拓展扣子可用的模型范围，具体请参见[接入自定义模型](/guides/deploy_custom_model)。

## 其他模型 {#4dcb3a7c}

此外，扣子编程还通过**官方插件**等方式提供了一些多模态模型供开发者使用。你可以直接为智能体绑定插件，并在人设与提示词中声明插件的使用场景，扣子编程智能体将在指定的对话场景下自动调用插件处理数据。那你也可以在编排工作流时添加插件节点，在流程中固定使用插件处理数据。详细说明可参考[插件介绍](/guides/plugin)。

常用的**官方模型插件**如下：

<!-- @cols-width: 207,399,441 -->
| **插件名称**  | **插件说明**  | **模型插件效果**  |
| --- | --- | --- |
| [Doubao-Seedream-4.0 插件](/guides/doubao_seedream_4_plugin)  | Doubao-Seedream-4.0 插件采用新一代图像创作模型 Seedream 4.0，能够灵活应对复杂的多模态生成任务（新增知识生图、复杂推理和参考图一致性等）。  | * 提示词：采用雷蒙德·布里格斯（Raymond Briggs）和马蒂亚斯·阿道夫松（Mattias Adolfsson）风格的插画，白色简洁背景，运用钢笔与水彩混合媒介创作，小兔子上幼儿园的绘本 | \
| | | * 生成效果： | \
| | |    ![Image=186x186](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b0575dd3c6574810b4cf52163ab9a1ed~tplv-goo7wpa0wc-topic.webp)  |
| [视频生成插件](/guides/doubao_seedance_plugin)  | 视频生成插件采用 doubao-seedance-1.0-pro 和 doubao-seedance-1.0-lite 模型，支持基于文本提示词生成视频，也支持基于文本提示词、视频首帧、尾帧图片或参考图共同生成视频。  | * 提示词：一片花丛，鲜艳的虞美人在摇曳，虞美人错落有致，有白色、黄色、大红色，阳光从花瓣后射过来，花瓣呈现出透明感 | \
| | | * 生成效果： | \
| | |    <Player class="topic-video-player"  class="topic-video-player"  src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f5a9d62c52694e899cc867991c6ed0af~tplv-goo7wpa0wc-image.image"></Player>  |
| [音乐生成插件](/guides/doubao_song_plugin)  | 豆包文生音乐可以根据用户输入生成音乐。 | 提示词：生成一段 pop 曲风、思乡主题、女性演唱者、氛围轻松愉快的音乐 | \
| | | | \
| | 此插件工具使用**豆包音乐模型**。  | 生成效果：[点击试听](https://v6-default.douyinvod.com/265471c08e5d4328f6b48d49bd7807d2/69428d72/video/tos/cn/tos-cn-v-bfc035/o4GeAhNIrrEOwAbOnGAEDWhLReB81VOEBGGCAf/?a=7518&ch=0&cr=3&dr=0&er=0&cd=0%7C0%7C0%7C3&br=1378&bt=1378&ds=5&ft=GwL5G6EEBBkq8ZmoIkWjG_vjVQWw&mime_type=audio_wav&qs=13&rc=M2h3dGs5cmdvdzczNDNoM0BpM2h3dGs5cmdvdzczNDNoM0AwcjBkMmRjZ2RgLS1kNC9zYSMwcjBkMmRjZ2RgLS1kNC9zcw%3D%3D&btag=80000e00028000&dy_q=1734433206&l=021734433196669fdbddc0100ffcd02ffffffff00000001b57f1d)  |
| [Doubao-图像生成插件](/guides/doubao_image_plugin)  | Doubao-图像生成插件是一款强大的 AI 图像助手，提供两大核心功能： | 图片生成工具： | \
| | | | \
| | * 图片编辑：上传图片并输入修改指令，AI 就能按照您的要求智能编辑图片。 | * 提示词：中世纪、现实风格、长发女孩、古堡背景 | \
| | * 图片生成：输入文字描述，AI 就能为您创作出独特的图像作品。 | * 生成效果： | \
| | |    ![Image=107x107](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b76fdcea9ea848b9bf2ef14c1c39dafe~tplv-goo7wpa0wc-topic.webp)  | \
| | 无论是修改已有图片还是从零创作，豆包都能帮您轻松实现图像创意。 | | \
| | | | \
| | 此插件工具使用**豆包图像生成模型**。  | |
|^^|^^| 图片编辑工具： | \
| | | | \
| | | ![Image=1294x829](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8201e703a52f41e697a5f4c85e7ac4b3~tplv-goo7wpa0wc-topic.webp)  |
| [图片理解](https://www.coze.cn/store/plugin/7328314686280138803?from=plugin_card&surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)  | 一款通过解析特定URL上的图片内容并为其生成含义且相关的文本描述的插件。它使用了先进的机器视觉和自然语言处理技术，旨在帮助用户理解图片的主要内容。  | ![Image=820x372](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/23f14544f3b447438377a20558258653~tplv-goo7wpa0wc-topic.webp)  |
| [ByteArtist 插件](/guides/byteartist_plugin)  | 根据文本描述生成图像，可指定图像数量和大小。  | 提示词：卡通风格，小猫 | \
| | | | \
| | | ![Image=178x178](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/feaa20c6c90749b4b06c0ff0c0d15bad~tplv-goo7wpa0wc-topic.webp)  |

## 为空间配置模型 {#97c904cb}

默认情况下，用户在工作空间中可使用模型管理页面中展示的所有模型，空间所有者和管理员可以限制空间内可用的模型。你可以在**模型管理**页面，开启或关闭某个模型。暂不支持批量开启或关闭模型。

* 开启模型：此模型将在智能体或模型节点的模型列表中展示，开发者可以使用该模型。
* 关闭模型：此工作空间中无法使用该模型。如果智能体或工作流中已使用该模型，关闭后不影响其正常运行。

模型管理功能入口如下所示：

::::cols
@col 50
**个人版**

在旧版扣子编程的左侧导航栏中，单击**空间配置**，然后在顶部选择**模型管理**，单击目标模型右侧的开关，可以开启或关闭模型。

![Image=1700x463](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d7ec0862a83049ad8cfa68e6bf248bc7~tplv-goo7wpa0wc-topic.webp)

@col 50
**企业版**

在扣子编程顶部选择目标工作空间，单击当前**空间配置管理**图标，然后在顶部选择**模型管理**，单击目标模型右侧的开关，可以开启或关闭模型。

![Image=593x165](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bb3e6b3c35824a80bb168b253a05c12d~tplv-goo7wpa0wc-topic.webp)
::::

## 常见问题 {#86ce8792}

### 如何区分方舟模型和扣子模型？ {#97c89470}

在智能体或工作流大模型节点中选择模型时，查看模型的类别即可区分方舟模型和扣子模型。

<!-- @cols-width: 119,447,209 -->
| **模型类型**  | **说明**  | **示例**  |
| --- | --- | --- |
| 方舟模型  | 由企业标准版、企业旗舰版用户在火山方舟侧通过创建接入点的方式自行接入的模型，被称为方舟模型。 | ![Image=481x462](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/df7f087f2b9a4b7998395913ab217d86~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | 在智能体或工作流大模型节点中选择模型时，如果模型分类展示为**`自开通模型|``在方舟自己开通的模型`**，表示这个分类下的模型为方舟模型。  | |
| 扣子模型  | 由扣子统一对接、面向所有扣子用户提供的模型服务，均为扣子模型。通常来说，除火山方舟以外的模型，均为扣子模型。 | ![Image=176x235](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/79dda4805d6b458fbdf1e472bd2b3529~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | 在智能体或工作流大模型节点中选择模型时，如果模型分类展示为**`扣子官方模型`**，表示此分类的模型为扣子模型。  | |

###  {#d00d49c9}

### 如何切换模型？ {#66fa01f9}

你可以为智能体、工作流大模型等节点设置或切换模型。具体操作方式如下：

<!-- @cols-width: 146,437,251 -->
| **操作类型**  | **说明**  | **示例**  |
| --- | --- | --- |
| 为智能体设置模型  | 在智能体的编排页面顶部区域，单击模型名称为智能体选择模型。  | ![Image=942x731](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/dea0fba5710246f996acffe10939a284~tplv-goo7wpa0wc-topic.webp)  |
|^^| 在模型的**用量记录**图表中，单击目标智能体名称，跳转至对应的智能体编排页面，进行模型替换。具体操作，请参考[如何快速切换待下架模型？](/guides/viewing_model#88c0b61a)。  | ![Image=2216x1151](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5302dfbd244a45068db27dbf85475bf7~tplv-goo7wpa0wc-topic.webp)  |
| 为工作流模型节点设置模型  | 工作流大模型节点中，在**模型**区域为节点设置模型。 | ![Image=932x842](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/18ea09b71ce24bfb84da6f960d89db00~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | 在工作流中，大模型节点、意图识别节点、问答节点均支持设置或切换模型。  | |
|^^| 在模型的**用量记录**图表中，单击目标工作流名称，跳转至对应的工作流编排页面，进行模型替换。具体操作，请参考[如何快速切换待下架模型？](/guides/viewing_model#88c0b61a)。 | ![Image=2216x1151](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5302dfbd244a45068db27dbf85475bf7~tplv-goo7wpa0wc-topic.webp)  | \
| | | | \
| | 在工作流中，大模型节点、意图识别节点、问答节点均支持设置或切换模型。  | |
