> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

Seedream 4.0 及更高版本均支持高达 4K 高清精美图像生成，能够帮助用户高效生成/编辑高质量图像，解决复杂多模态创作需求。本文将介绍该系列模型的生图效果与各版本迭代升级亮点，并提供了详细的教程，指导你搭建生图工作流和智能体。

## 模型概览 {#f574c095}

为了帮助你根据具体需求快速选择最合适的模型，下表直观展示了 Seedream 4.0、4.5 及 5.0 Lite 的核心特性。

<!-- @cols-width: 100,100,213,213,213 -->
| || | | | \
|模型名称 | |**Doubao-Seedream-5.0-lite** |**Doubao-Seedream-4.5** |**Doubao-Seedream-4.0** |
|---|---|---|---|---|
| || | | | \
|文生图 | |✔️ |✔️ |✔️ |
| || | | | \
|生成组图 | |✔️ |✔️ |✔️ |
| || | | | \
|图像编辑 | |✔️ |✔️ |✔️ |
| || | | | \
|联网搜索 | |✔️ |➖ |➖ |
|模型参数 |分辨率 |2K, 3K |2K, 4K |1K, 2K, 4K |
|^^| | | | | \
| |输出格式 |png, jpeg |jpeg |jpeg |
| || | | | \
|模型迭代亮点 | |具备联网实时检索、编辑精准可控、智能逻辑推理三大升级亮点。 |人像场景效果、画面美观度、一致性、编辑准确度等方面均有提升。 |首次支持多模态生图，支持文生图、图像编辑、生成组图。能够通过自然语言灵活控制画面细节。 |

:::tip 说明
输入的参考图数量 + 最终生成的图片数量 ≤ 15张
:::

## 模型迭代亮点 {#98546604}

### Seedream 5.0 Lite {#ceb88c7a}

与 Seedream 4.5 相比，Seedream 5.0 Lite 具备联网实时检索、编辑精准可控、智能逻辑推理三大升级亮点。

* **联网实时搜索**
   首次支持检索生图功能，能够融合实时网络信息，提升生图时效性。
   <!-- @cols-width: 412,200,201 -->
   |**指令** |**效果图（开启联网）** |**效果图（关闭联网）** |
   |---|---|---|
   |```Plain Text |\
   |制作一张杭州未来5日的天气预报图，采用现代扁平化插画风格，清晰展示每日天气、温度和穿搭建议。 整体为横向排版，标题为“杭州未来5日天气预报”，包含5个等宽的垂直卡片，从左到右依次排列。 整体风格为现代、干净、友好的扁平化矢量插画风格，线条清晰，色彩柔和。 人物形象采用年轻男女的卡通插画，表情自然，姿态放松，服装细节清晰。 |\
   |``` |![Image=2048x2048](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bd6b65445d494003b36040a669fcaf86~tplv-goo7wpa0wc-image.image) |![Image=177x177](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bbfbe0c247154bb69076b81ae8520176~tplv-goo7wpa0wc-image.image) |
* **编辑精准可控**
   生成图像与输入文本的契合度提升，能够精准响应复杂指令需求。
   <!-- @cols-width: 417,201,214 -->
   |**指令** |**原图** |**效果图** |
   |---|---|---|
   |```Plain Text |\
   |一只熊正在和一只驴在玩跷跷板，驴比熊重得多 |\
   |``` |➖ |![Image=2048x2048](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/54d87dc7f3a14b33ba2f6787fb910114~tplv-goo7wpa0wc-image.image) |
   |```Plain Text |\
   |将图中蓝色框内的水果改成葡萄，绿色框内的水果改成切开的苹果，在红色框内增加一个蓝莓。 |\
   |``` |![Image=1080x1080](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ed387fb7d3e4437492877948a33a9fc2~tplv-goo7wpa0wc-image.image) |![Image=2048x2048](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6b1d8a2b92ed4a0197f783f35046b948~tplv-goo7wpa0wc-image.image) |
* **智能逻辑推理**
   更懂现实规律，支持复杂的逻辑推演与多步推理需求，并且内置了垂直行业专业知识库。
   <!-- @cols-width: 416,214 -->
   |**指令** |**效果图（Seedream 5.0 Lite）** |
   |---|---|
   |```Plain Text |\
   |一张英文石油系统信息图表，显示石油钻井平台和地质层 |\
   |``` |![Image=167x167](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/034c64cd5d4e4e7fa277e4354380402d~tplv-goo7wpa0wc-image.image) |
   |```Plain Text |\
   |两把文具尺子，上面是20cm塑料尺，下面是10cm钢尺 |\
   |``` |![Image=2048x2048](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/352c5526e8294fa7a743720b3132c870~tplv-goo7wpa0wc-image.image) |   


### **Seedream 4.5** {#87eb8553}

与 Seedream 4.0 相比，Seedream 4.5 在人像场景效果、画面美观度、一致性、编辑准确度等方面均有提升。

* 人像场景效果优化
   <!-- @cols-width: 319,164,193,196 -->
   |**指令** |**原图** |**效果图 （Seedream 4.5）** |**效果图 （Seedream 4.0）** |
   |---|---|---|---|
   |```Plain Text |\
   |将人物自然地嵌入罗马广场背景，适当拉远构图以展现更多建筑空间与景深层次，保持人物比例与环境透视关系自然真实。 |\
   |``` |![Image=1024x1024](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d551683048734f5e8510ed3ad17cf8e8~tplv-goo7wpa0wc-image.image) |![Image=141x141](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/15897e03e8ac4a45932c0e8595228018~tplv-goo7wpa0wc-image.image) |![Image=1568x675](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/265272e1b4bc45d29822afa913b68835~tplv-goo7wpa0wc-image.image) |
* 美观度提升
   <!-- @cols-width: 410,193,196 -->
   |**指令** |**效果图 （Seedream 4.5）** |**效果图 （Seedream 4.0）** |
   |---|---|---|
   |```Plain Text |\
   |哥特式美学，水墨淡彩，女，披甲穆桂英，特写镜头，金属光泽，对比度，张扬，色彩鲜艳，流光，烟雾环绕，动态模糊，抽象，右下角手写签名:大爱中国 |\
   |``` |![Image=540x540](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8a9390c450c0437fab20f8c720218215~tplv-goo7wpa0wc-image.image) |![Image=1024x1024](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cf21e3fe605044ce9ac61e703276b916~tplv-goo7wpa0wc-image.image) |
* 编辑准确度提升
   <!-- @cols-width: 319,164,193,196 -->
   |**指令** |**原图** |**效果图 （Seedream 4.5）** |**效果图 （Seedream 4.0）** |
   |---|---|---|---|
   |```Plain Text |\
   |完成此图像以形成完整的恐龙形象并为其着色。 |\
   |``` |![Image=131x82](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ad4fe117022a4ad587c6835e08cf381d~tplv-goo7wpa0wc-image.image) |![Image=149x103](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3447e59f947b4d6f9651b47e401df3ba~tplv-goo7wpa0wc-image.image) |![Image=155x106](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/604fc1b0d9914081b9007d978ae13229~tplv-goo7wpa0wc-image.image) |   


### **Seedream 4.0** {#916daedf}

首次支持多模态生图，支持文生图、图像编辑、生成组图。

<!-- @cols-width: 410,204 -->
|**指令** |**效果图** |
|---|---|
|```Plain Text |\
|一个童话绘本风格的女孩 |\
|``` |![Image=174x131](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d48a3bc4230c4b8ab01ad3eb279f3267~tplv-goo7wpa0wc-image.image) |
|```Plain Text |\
|采用雷蒙德·布里格斯（Raymond Briggs）和马蒂亚斯·阿道夫松（Mattias Adolfsson）风格的插画，白色简洁背景，运用钢笔与水彩混合媒介创作，小兔子上幼儿园的绘本 |\
|``` |![Image=171x171](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/92b51e49d515443da1c9cf5d833eb97f~tplv-goo7wpa0wc-image.image) |

## 基本能力 {#hvNtYftny}

### 元素增删 {#hAu8YJ9zu}

<!-- @cols-width: 188,159,154,161,169,183 -->
| | ||||| \
|**分类** |**操作** | | | | |
|---|---|---|---|---|---|
|**增加元素** |\
| |\
|`给 XX 加 XX` |原图 |\
| | |\
| |![Image=60x61](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7b6f8ff887f64e4bab28771e2253627f) |加上眼镜 |\
| | | |\
| | |![Image=59x59](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/fa1c05e29cf04bd595b8483583b0b6fd) |加上围巾 |\
| | | | |\
| | | |![Image=61x61](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6e7d570111aa44489256a7b8591f1e30) |加上茶杯 |\
| | | | | |\
| | | | |![Image=61x61](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/af9b11831b6644edba7b406dd3d10419) |加上帽子 |\
| | | | | | |\
| | | | | |![Image=61x61](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/61f7f308f0d7411ca716767123844fc7) |
|**删除元素** |\
| |\
|`去除 XX` |原图 |\
| | |\
| |![Image=60x60](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2eefe16897b54d9396e487f3167f8888) |去掉眼镜 |\
| | | |\
| | |![Image=60x60](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/8f708f80b6e947608dd5e32f95dd438a) |去掉床 |\
| | | | |\
| | | |![Image=61x61](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4c403337e11f4d41b88d832ab68458c2) |去掉围巾 |\
| | | | | |\
| | | | |![Image=60x60](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f48b468671ba446faf9615039a87e13e) |去掉小IP |\
| | | | | | |\
| | | | | |![Image=61x61](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d49886c5849847a08510f4773e016753) |



### 改变风格 {#hLEhISA0u}

<!-- @cols-width: 188,100,100,100,100,100,100 -->
| | |||||| \
|**分类** |**操作** | | | | | |
|---|---|---|---|---|---|---|
|**改变风格** |\
| |\
|`将画面改成 XX 风格` |原图 |\
| | |\
| |![Image=606x512](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/3cee7d7b0ef2466aab7b25bc53c4c20a) |绘本 |\
| | | |\
| | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/8cba5b7b137146768e770c96d4161773) |像素 |\
| | | | |\
| | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a8403cd6531e4a99a5e39eda2482ae48) |2D卡通 |\
| | | | | |\
| | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d1a10ef21ca741af86c37abb61908ed4) |盲盒 |\
| | | | | | |\
| | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4cc5b69bd831472abad10a8bc9c35311) |水墨 |\
| | | | | | | |\
| | | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/25efdcad41a645f0bd20d2073f77eafd) |

### 改变光影&色调 {#hWekZRXcx}

<!-- @cols-width: 191,100,100,100,100,100,100,100 -->
| | ||||||| \
|**分类** |**操作** | | | | | | |
|---|---|---|---|---|---|---|---|
|**改变光影** |\
| |\
|`将画面光影改成 XX` |原图 |\
| | |\
| |![Image=1440x1440](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/cf640cc6ba6a484dae893cce85a13fe5) |逆光 |\
| | | |\
| | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d964b070b50549f2bdb90b676482134d) |侧光 |\
| | | | |\
| | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/56338f48599f4e41a2d7fbd9c9b08a56) |侧逆光 |\
| | | | | |\
| | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4f55cae1abb443ef86e62e323b6d6a6a) |柔光 |\
| | | | | | |\
| | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d3eb7287b9e740e2b0cd2266acf78f8f) |夕阳 |\
| | | | | | | |\
| | | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/cfc28c143bab43f0bc9c621f1aed2e38) |光影斑驳 |\
| | | | | | | | |\
| | | | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f3510febe59346b1ba50b873aa942eda) |
|**改变色调** |\
| |\
|`将画面色调改成 XX` |原图 |\
| | |\
| |![Image=1440x1440](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/cf640cc6ba6a484dae893cce85a13fe5) |暖色调 |\
| | | |\
| | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/77b1df57658b42f0908112c97f497196) |冷色调 |\
| | | | |\
| | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b4d527b70a4949d1b04b8648f4bae016) |亮色调 |\
| | | | | |\
| | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2fcf092360ee468cab52f4251467b971) |黑白 |\
| | | | | | |\
| | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/775f5432179a4e42bff276e77025930d) |低对比 |\
| | | | | | | |\
| | | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2e56d1165b4c44aab0f9e4a305ad9ae6) |低饱和 |\
| | | | | | | | |\
| | | | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f8993808127d42d594e9e6a5db2938f7) |

### 改变材质&背景 {#hCo3pUOl7}

<!-- @cols-width: 191,100,100,100,100,100,100,100 -->
| | ||||||| \
|**分类** |**操作** | | | | | | |
|---|---|---|---|---|---|---|---|
|**改变材质** |\
| |\
|`将材质改成 XX` |原图 |\
| | |\
| |![Image=727x736](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7b6f8ff887f64e4bab28771e2253627f) |粘土 |\
| | | |\
| | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/12d6d059108c4017ba56f5b995628bbe) |毛绒 |\
| | | | |\
| | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/88e9c8749dff4ff7ac616ce9159dbce8) |毛毡 |\
| | | | | |\
| | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/0e592567c65a4170979b060364c7e857) |石头 |\
| | | | | | |\
| | | | | |![Image=20000x20000](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1db9620be3d2440986453f607bf9f454) |金属 |\
| | | | | | | |\
| | | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/09d83c23dd874dfd92889dd9ffbbac68) |亚克力 |\
| | | | | | | | |\
| | | | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d877578f48a34cbcb67c3c1119023934) |
|**改变背景** |\
| |\
|`将背景改成 XX` |原图 |\
| | |\
| |![Image=727x736](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7b6f8ff887f64e4bab28771e2253627f) |森林 |\
| | | |\
| | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c83eafdf23e2460dacb40feb8808481b) |儿童房 |\
| | | | |\
| | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/83210bd94a324d139252487b038cf230) |图书馆 |\
| | | | | |\
| | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/520d06da7f1c4058af3c617a2d07ade6) |商场 |\
| | | | | | |\
| | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2765c01be30a4274b26135354d21f2f5) |➖ |➖ |

### 改变视角&景别 {#hutDEfXxB}

<!-- @cols-width: 188,100,100,100,100,100 -->
| | ||||| \
|**分类** |**操作** | | | | |
|---|---|---|---|---|---|
|**改变视角** |\
| |\
|`将视角改成 XX` |原图 |\
| | |\
| |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4c4fbd9d94804e52a2c3f9d658725c56) |正面平视 |\
| | | |\
| | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b8f1317adc33449bab58d65b792cba4f) |侧面视角 |\
| | | | |\
| | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/0aa7840fad844a32b4974dc27acd1936) |背面视角 |\
| | | | | |\
| | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ecf94549024e45c49a1da341047f188c) |斜侧视角 |\
| | | | | | |\
| | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/5b0bccf40f9e4499af2488cfb248fe2b) |
|**改变景别** |\
| |\
|`将景别改成  XX` |原图 |\
| | |\
| |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4c4fbd9d94804e52a2c3f9d658725c56) |远景 |\
| | | |\
| | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/fabf5688e6af4de0a878871be4463869) |全景 |\
| | | | |\
| | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ccbfe1336cc0497db1f7cc0b67992b35) |特写 |\
| | | | | |\
| | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/61ef0a3af76b4903b4ff31ab821d9aeb) |大特写 |\
| | | | | | |\
| | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7acfd885c46242d5973759836efe9c58) |

### 海报编辑 {#hMQbXSqdx}

<!-- @cols-width: 190,100,100,100,105,100 -->
| | ||||| \
|**分类** |**操作** | | | | |
|---|---|---|---|---|---|
|**改变字体** |\
| |\
|`将标题字体改成 XX` |\
| |\
| |原图 |\
| | |\
| |![Image=1296x1728](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b7d375a8d4b04be48feb1f7dedd5aeb2) |手写体 |\
| | | |\
| | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/acbf08a8201e440f9edbec388b076856) |书法体 |\
| | | | |\
| | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/789453bb049347389461484ad06ecae3) |粗笔刷 |\
| | | | | |\
| | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/483aa13d9b1f4a349e5ad9e146a99ef0) |哥特体 |\
| | | | | | |\
| | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e45771f8d435426f882397db3b399038) |
|**改变文字内容** |\
| |\
|`将 XX 文字内容改成 XX` |原图 |\
| | |\
| |![Image=1296x1728](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b7d375a8d4b04be48feb1f7dedd5aeb2) |效果图 |\
| | | |\
| | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/8d482c55d1fc4488845f4f77cbcd64aa) |\
| | | |\
| | | |➖ |\
| | | | |\
| | | | |\
| | | | |\
| | | | |➖ |➖ |
|**改变文字颜色** |\
| |\
|`将画面中的标题字体颜色改成 XX` |原图 |\
| | |\
| |![Image=1296x1728](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b7d375a8d4b04be48feb1f7dedd5aeb2) |白色 |\
| | | |\
| | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a49463b443ad47f8b33699a43ab5d269) |黄色 |\
| | | | |\
| | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f71b13e386e048cf9cea37bdc962935a) |渐变色 |\
| | | | | |\
| | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/70e5063c90b94a35863276892d4046b4) |➖ |
|**改变非文字内容** |\
| |\
|`将画面中的 XX 改成 XX` |原图 |\
| | |\
| |![Image=1296x1728](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/63c9d3f727cf4206a714468caa2c1e0a) |把主体改成柠檬 |\
| | | |\
| | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/69c101ae557c4b6ca6f0d983d0d3b11f) |把主体改成猫 |\
| | | | |\
| | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1008bcc2894a4d65bf4bfd542a82aaf5) |把背景改成渐变 |\
| | | | | |\
| | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b2de385325d54cf09386f277af436685) |把背景改成白色 |\
| | | | | | |\
| | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/fc2e951e6e8249a0830668b7b364488f) |
|**改变文字材质** |\
| |\
|`将画面中的文字材质改成 XX` |原图 |\
| | |\
| |![Image=1296x1728](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/63c9d3f727cf4206a714468caa2c1e0a) |云朵 |\
| | | |\
| | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/29006269627240dda528c3f96977fb8b) |液态金属 |\
| | | | |\
| | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/235d0c9d791d40a3b87284796aff4729) |手撕纸 |\
| | | | | |\
| | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/118292d3fb914d3e98db5511fbdfaa77) |涂鸦喷漆 |\
| | | | | | |\
| | | | | |![Image=2048x2048](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4d58c671802445bfa6bbcc42d8758e5e) |

## 生成效果 {#htvCcwe36}

### 设计 {#c8942d68}

<!-- @cols-width: 538,280 -->
|**指令** |**效果图** |
|---|---|
|```Plain Text |\
|用水母作为灵感来源，做一张建筑设计图。该图中需要包含第一部分：灵感来源，第二部分：概念转化，第三部分最终建筑方案。 |\
|``` |![Image=2048x2048](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b78f2fd433dd4cb392345e318b8a58cc~tplv-goo7wpa0wc-image.image) |\
| | |\
| |> **Seedream 5.0 Lite** |
|```Plain Text |\
|一只手拿着鲜黄色苏打罐，背景是蓝天。罐上的标签印有清晰、醒目的小字“FRESH SODA”和“100% Natural”。罐上有水滴。细节高度还原，采用商业产品摄影风格。 |\
|``` |![Image=2304x1732](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ace7eed11ba540e7a8173b26b186db2d~tplv-goo7wpa0wc-image.image) |\
| | |\
| |> **Seedream 4.5** |
|```Plain Text |\
|基于这个 IP，延展 4 个 3D 品牌物料，每个物料都展现高级质感。例如杯子、贴纸、包装盒、手提袋等。每个物料上面都有这个 IP。一个物料一张图 |\
|``` |![Image=258x258](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b933a982d84b452ab3a4d6ecbbdab0b8~tplv-goo7wpa0wc-image.image) |\
| | |\
| |> **Seedream 4.0** |

### 知识科普 {#8c8f7e23}

<!-- @cols-width: 541,273 -->
|**指令** |**效果图** |
|---|---|
|```Plain Text |\
|一张黑板报形式的手绘科普信息图，以粉笔质感呈现火山喷发过程。上方用简短文字解释岩浆积聚压力并喷发的原理，并用气球作比喻辅助理解。中央为火山剖面插画，箭头标示岩浆上升与熔岩流动，下方分模块说明各阶段，整体轻松、教学感强。 |\
|``` |![Image=2048x2048](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/af72818f93f545b49f258c8c3112353f~tplv-goo7wpa0wc-image.image) |\
| | |\
| |> **Seedream 5.0 Lite** |
|```Plain Text |\
|什么是力的相互作用？生成一张生动的黑板板书告诉我，有直观相互力的箭头展示 |\
|``` |![Image=2304x1725](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cf8d703dd87d426da1d76c8a8e212419~tplv-goo7wpa0wc-image.image) |\
| | |\
| |> **Seedream 4.5** |
|```Plain Text |\
|手账风格，出一个制作蛋糕的步骤教程图，使用中文详细介绍步骤 |\
|``` |![Image=243x243](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2c5a2c57ecc94525b8cafc1887eaa4b4~tplv-goo7wpa0wc-image.image) |\
| | |\
| |> **Seedream 4.0** |

### 修改图片 {#00e8a84e}

<!-- @cols-width: 346,242,230 -->
|**指令** |**原图** |**效果图** |
|---|---|---|
|```Plain Text |\
|基于下面的图片，给女孩加个帽子，加个双肩包，女孩闭上嘴巴微笑 |\
|``` |![Image=208x151](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3a9e1c83edeb4456bcb29a2d258cfafb~tplv-goo7wpa0wc-image.image) |![Image=148x148](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c1f8968af4cb44c7819879a3800c00dd~tplv-goo7wpa0wc-image.image) |\
| | | |\
| | |> **Seedream 5.0 Lite** |
|```Plain Text |\
|让图1中的女生变成图2的姿势 |\
|``` |![Image=154x111](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3a9e1c83edeb4456bcb29a2d258cfafb~tplv-goo7wpa0wc-image.image) |\
| | |\
| |![Image=130x214](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/84df2d7dfc8a473aba4883f067166df7~tplv-goo7wpa0wc-image.image) |![Image=151x249](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/076815952b9e43d2a9e0259171e9c464~tplv-goo7wpa0wc-image.image) |\
| | | |\
| | |> **Seedream 4.0** |

### 生成写真 {#95be26c2}

<!-- @cols-width: 346,237,239 -->
|**指令** |**原图** |**效果图** |
|---|---|---|
|```Plain Text |\
|将上传的照片转换成高分辨率的黑白肖像艺术作品，背景呈现柔和渐变效果，营造出层次感与寂静氛围。细腻的胶片颗粒质感为画面增添了一种可触摸的、模拟摄影般的柔和质地，让人联想到经典的黑白摄影。 |\
|画面中的人物非传统的摆拍，而像是被捕捉于思索或呼吸之间的瞬间。他的脸部因为光线的轮廓，唤起神秘、优雅之感。他的五官精致而深刻，散发出忧郁与诗意之美。一束温柔的定向光，柔和地漫射在他的面颊曲线，或在眼中闪现光点，这是画面的情感核心。其余部分以大量负空间占据，保持简洁，画面中没有文字、标志——只有光影与情绪交织。 |\
|整体氛围仿佛一瞥即逝的目光，有种令人怅然的美。要求没有实物的背景，每张照片换不同的动作。 |\
|``` |![Image=236x236](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c3252637f23045d9827c8bf31f77ed6f~tplv-goo7wpa0wc-image.image) |![Image=214x214](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ca5e31c12f2f4abdb1a81d1d88ec550f~tplv-goo7wpa0wc-image.image) |\
| | | |\
| | |> **Seedream 4.0** |

### 多图融合 {#28c5e25d}

<!-- @cols-width: 349,232,232 -->
|**指令** |**原图** |**效果图** |
|---|---|---|
|```Plain Text |\
|将图1中的几支花按品种分类，分别插在图2的三个花瓶中 |\
|``` |![Image=1084x1006](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3019a7ce9dab47cea20589375883f880~tplv-goo7wpa0wc-image.image) |\
| | |\
| |![Image=1094x937](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5142a062d2e54827a75ec73425296a9d~tplv-goo7wpa0wc-image.image) |![Image=2048x2048](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/18434de5aac74052add1343f3064e1e5~tplv-goo7wpa0wc-image.image) |\
| | | |\
| | |> **Seedream 5.0 Lite** |
|```Plain Text |\
|将图1的服装换为图2的服装 |\
|``` |![Image=135x169](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4d24dda0087246c88a01cf9320b6829f~tplv-goo7wpa0wc-image.image) |\
| | |\
| |![Image=135x135](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fd3427be5bc040b09987abf8dcd71b0a~tplv-goo7wpa0wc-image.image) |![Image=208x208](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7ca811806e4b46f1a0bbf509ab08ab94~tplv-goo7wpa0wc-image.image) |\
| | | |\
| | |> **Seedream 5.0 Lite** |

### 制作插画 {#fc1a24df}

<!-- @cols-width: 491,319 -->
|**指令** |**效果图** |
|---|---|
|```Plain Text |\
|高定羊毛毡艺术插画，几米式叙事，留白式情绪铺垫，有张力，层次，角度，水彩晕染，高饱色彩，注重线条笔触，极繁主义，高质量，电影质感，梦幻，矿物原料晕染，动态定格，强烈视觉效果，空灵，童话，惊艳， 可爱的小女孩戴着一顶红色的帽子，帽子边缘长满了各种小型植物和花卉，还有小动物在帽子上的森林奔跑 |\
|``` |![Image=259x259](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/77b5ec6f3f664edfb87cb3756c811b8f~tplv-goo7wpa0wc-image.image) |\
| | |\
| |> **Seedream 4.0** |

### 画面构图 {#54378b10}

<!-- @cols-width: 497,311 -->
|**指令** |**效果图** |
|---|---|
|```Plain Text |\
|油画质感摄影，经典框式构图。从黑暗岩洞向外望去，框出托斯卡纳清晨的金色云雾与起伏山丘。洞口坐着一位写生画家的逆光剪影。前景纹理锐利，远景柔美，光影层次极丰富。 |\
|``` |![Image=2304x1730](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0658c09c36df40b3ac08476b312fdc6b~tplv-goo7wpa0wc-image.image) |\
| | |\
| |> **Seedream 4.5** |

## 工作流与智能体应用 {#33ed482b}

本教程的核心是借助图像生成节点中的 Seedream 4.0 模型，构建了一个定制化的图像生成工作流。在此基础上，进一步搭建了一个生图智能体，该智能体绑定了上述工作流。当用户输入详细的生图提示词和参考图后，智能体会自动调用工作流生成图像，并以卡片形式返回图像。使用该智能体时，用户无需操作复杂的生图流程，仅通过与智能体对话，便能轻松生成符合需求的图像。

### 低代码工作流 {#92c44f18}

#### 工作流说明 {#d5ef6972}

该工作流旨在调用 Seedream 4.0 模型，基于用户提供的生图提示词和参考图，快速生成所需的图像。包括如下节点：

1. 开始节点：接收用户输入的关键信息，包括图像生成提示词和参考图。本教程定义了最多可以上传 3 张参考图，这些参考图将为 Seedream 4.0 提供具体的视觉参考，帮助生成更贴近需求的图像。
   在提供提示词时，建议尽量详细且准确，以便更好地引导 Seedream 4.0 模型生成符合预期的图像。提示词的描述示例，请参考[生成效果](/tutorial/seedream4_prompt#5dc75cc0)。
2. 图像生成节点：Seedream 4.0 模型将基于用户提供的生图提示词和参考图，批量生成图像。Seedream 4.0 模型支持生成多张图像，本教程定义了单次最多可生成 15 张图像。生成的图片越多，生成的时间越长。

![Image=767x396](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/afc47a6e0dab4f16a6c661f85b23c369~tplv-goo7wpa0wc-image.image)

#### 核心节点说明 {#fbbfda8d}

各个节点的配置详情如下：

<!-- @cols-width: 185,404,272 -->
|**节点名称** |**说明** |**示例** |
|---|---|---|
|开始节点 |开始节点用于传入图像生成节点必选参数。节点配置说明如下： |\
| | |\
| |* 新增 `prompt`，必选，String 类型，用于输入**图像生成节点**所需的图像生成提示词。 |\
| |* 新增 `image1`、`image2`、`image3` 参数，可选，设置为 Image 类型，用于为**图像生成节点**提供参考图。你可以根据业务需求设置参考图数量。 |![Image=688x357](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1c9a8ff61f094ee1aebf090f146133f1~tplv-goo7wpa0wc-image.image) |
|图像生成节点 |通过**图像生成节点**中的 Seedream 4.0 模型生成图片。 |\
| | |\
| |节点配置说明如下，参数详细说明请参考[图像生成节点](/guides/image_generation_node)。 |\
| | |\
| |* **模型**：选择 **Seedream 4.0**。 |\
| |* **比例**：设置为自定义比例。 |\
| |* **图片水印**：打开**图片水印**开关。 |\
| |* **最大生成图片数量**：设置为 15 张。 |\
| |* **参考图**：引用**开始节点**的输入参数 `image1`、`image2`、`image3`，支持添加 3 张参考图。 |\
| |* **输入**： |\
| |   * 新增参数 `prompt`，引用开始节点的输入参数 `prompt`。 |\
| |* **提示词**：引用 `{{prompt}}`，模型将根据该提示词生成图像。 |![Image=662x963](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b1f2247f3fa7411bbdcaaaf6a9b75428~tplv-goo7wpa0wc-image.image) |
|结束节点 |结束节点用于输出图像的 URL。节点配置说明如下： |\
| | |\
| |* **输出模式**：选择**返回文本**。 |\
| |* **输出**：定义变量 `output`，引用**图像生成节点**的输出参数 `data`。 |\
| |* **回答内容**：设置为 `{{output}}`，表示输出图像 URL。 |![Image=682x505](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6fa516757a1b41db809e2bd90fa545c6~tplv-goo7wpa0wc-image.image) |

### 低代码智能体 {#9c960292}

搭建好图像生成工作流后，还需要搭建一个生图智能体。首先，在智能体中定义好智能体的角色和技能，确保它能够精准地理解并执行生图工作流。然后在智能体中绑定已创建好的生图工作流，并为工作流添加卡片。当用户输入生图提示词和参考图后，智能体会立即调用工作流生成图像，并以卡片形式返回生成的图像。

::::cols
@col 50
智能体提示词

```Plain Text
# 角色
你是一名经验极其丰富的资深图像处理师，拥有超过10年的专业实践经历。在图像生成、风格迁移、细节优化、内容融合以及图像编辑等图像处理核心领域有着深厚造诣，能够熟练且精准地处理各类图像相关任务。

## 技能
### 技能 1: 执行图像生成指令
1. 当用户明确给出图像生成指令、提供参考图后，迅速且准确地执行{{genimage_test}}工作流进行图片处理。

## 限制:
- 只专注于图像处理相关的任务和问题，拒绝回答与图像处理无关的话题。
```

@col 50
绑定工作流及添加卡片

本教程以返回一张卡片为例。添加卡片的具体操作，请参考[卡片](/guides/message_card)。

![Image=823x336](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8df35bf20f964a44acfa793c70974c1f~tplv-goo7wpa0wc-image.image)

![Image=575x271](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d2681deb42a74a4f957d9260f34c4951~tplv-goo7wpa0wc-image.image)
::::

搭建完成后，你可以在智能体调试页面，输入生图提示词和参考图，智能体将调用工作流生成新图片并返回。

![Image=639x306](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/672d59e76b29451fb4804db419886225~tplv-goo7wpa0wc-image.image)
