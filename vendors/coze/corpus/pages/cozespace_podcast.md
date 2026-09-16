> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子 Agent 提供文本转播客的内置技能“**播客**”，帮助你将文章链接、图片、PDF 等各类文件或文本转为播客音频，一键制作播客。
## 功能特色 {#c2984880}
播客作为一种受欢迎的内容传播形式，正吸引越来越多的用户。传统的播客制作流程繁琐、效率较低，对硬件设备、录制环境都有较高要求，制作成本和入门门槛高，难以快速落地各类灵感创意，实现高频的音频内容创作。然而，传统 AI 播客创作存在诸多痛点，如内容重复废话连篇、不够口语化、听感机械且缺乏互动，严重影响了用户体验。
扣子推出文本转播客的内置工具，支持将 URL、文本或文档转为专业质量的播客。扣子功能的播客功能默认双说话人模式，智能理解并改写指定的文本内容，生成流畅而自然的播客音频，支持双人对谈，交叉附和，听觉效果高度拟人。
相比普通的 AI 播客，扣子全新升级的播客有以下特点：

* **更生动**：不同于以往 AI 生成的生硬语音，扣子模拟真人专业播客的口语习惯，双人对谈，交叉附和，“捧哏”与“逗哏”配合默契。
* **更自然**：扣子全面升级播客音色，相较于传统方案的机械音，扣子在拟人音色中加入丰富的情感波动和丝滑的语气转换，拟人程度更高。
* **更专业**：扣子输出的播客以漫谈开场，自然切入话题，吸引听众注意力；话术巧妙、循序渐进，实现播客听众的长效留存。

:::tip 说明
仅扣子 Agent 内置**播客**技能，本地 Agent 等其他类型的 Agent，可前往[技能商店](https://www.coze.cn/skills?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)或[虾评社区](xiaping.coze.com)查找合适的播客技能。
:::
## 效果体验 {#f00f4d50}

::::cols
@col 50
输入目标受众，扣子自主寻找创意、构思脚本，一键生成播客。
播客试听：[大学生暑假逆袭指南](https://www.coze.cn/s/aSF_0QNFcFI/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)
![Image=2534x1515](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/846fa49d844f4a6bac89c9f41731d645~tplv-goo7wpa0wc-image.image)


@col 50
输入文章链接，扣子根据文章内容总结、专项脚本，一键生成播客。
播客试听：[扣子空间创意玩法](https://www.coze.cn/s/BWNMPXB3gqY/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)
![Image=2564x1503](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f6510580647b47ddad204c702b429c01~tplv-goo7wpa0wc-image.image)

::::

## 使用方式 {#27f3d275}
### 链接和文件转播客 {#cfd7ee4a}
你可以将已有的文档链接和文件内容转成播客音频，支持文章链接、图片、表格、文章、PPT、PDF 等各类常见的文件格式。其中文章链接必须是一个公开可访问的 URL 地址，例如公众号、知乎专栏地址等，扣子可以灵活提取 URL 中的文本，并将其改写为播客脚本、转为播客音频，最终生成的音频文件可插入在各类第三方页面中播放。
使用方式如下：

1. 在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)主对话页面，通过对话框输入斜杠（/），在技能页签选择**播客**，输入任务提示词，然后敲击回车键发送你的指令。
   例如“https://docs.coze.cn/cozespace/overview，帮我基于这个文档生成一段播客音频。”


::::cols
@col 50
   ![Image=2032x1593](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5d8358fcadad419187f91a9d05f70b2f~tplv-goo7wpa0wc-image.image)

<div style="text-align: center">查找技能</div>



@col 50
![Image=390x308](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d73da8e3bf464dc08316552f6dda83ef~tplv-goo7wpa0wc-image.image)
<div style="text-align: center">下发指令</div>


::::


2. 扣子 AI Agent 自动制作播客音频。
   过程中， Agent 会调用网页读取工具来读取网页内容，并提取文本、生成播客脚本，最后将播客脚本转为播客音频。
3. 预览播客音频。
   任务执行完毕后，你可以单击扣子制作产物，预览音频文件。
   ![Image=479x303](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/94bf868bbb194e83a9584e0a60e28c7a~tplv-goo7wpa0wc-image.image)

### AI 生成脚本并转播客 {#7725ece6}
如果你有一个绝妙的灵感创意主题，也可以通过自然语言告诉扣子，让它为你全流程自动化完成选题策划、脚本创作、音频合成，实现从素材灵感到专业播客的一键转化。
使用方式如下：

1. 在[扣子](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)主对话页面，通过对话框输入斜杠（/），在技能页签选择**播客**，输入任务提示词，然后敲击回车键发送你的指令。
   例如“我是一个校园博主，粉丝为20岁左右的大学生群体，我想要做一期“大学生如何暑假提升自己“的播客，提升我的账号粉丝，请生成台本创意，并输出完整的播客。”
   ![Image=402x336](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/43506cf7c5dc42cab12490ddbd636c86~tplv-goo7wpa0wc-image.image)
2. 扣子 AI Agent 自动生成脚本，并制作播客网页。
   过程中， Agent 会公开检索相关信息，根据主题和要求生成播客脚本，最后将播客脚本转为播客音频。
   ![Image=420x334](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d7369df98a5e412c900b79c73497bd62~tplv-goo7wpa0wc-image.image)
3. 预览播客页面。
   任务执行完毕后，你可以单击扣子制作产物，预览音频文件。
   ![Image=421x336](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f01e0c045cb94642970691bb7cdfef4b~tplv-goo7wpa0wc-image.image)


