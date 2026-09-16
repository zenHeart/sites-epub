> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

## 主动干活 {#f5148e83}
OpenClaw 不止会给你出主意，更能**直接动手帮你完成任务**。从定时自动执行重复工作、操控浏览器获取信息，到记住你的习惯偏好、用语音高效交互，让 AI 成为你身边随叫随到的「全能助理」，真正解放你的双手与时间。
### 定时任务 {#5041dbf5}
**什么是定时任务**
OpenClaw 可以按照你指定的时间/周期，自动执行预设好的任务，不需要你每次手动触发。比如定时查消息、定时推菜单、定时发提醒、定时总结待办等等。
**定时任务是如何实现的**
OpenClaw 使用内置的 Cron 调度器，和标准 Linux Cron 语法完全兼容：

* 支持三种调度模式：一次性定时（"明天下午3点提醒我"）、固定间隔（"每半小时检查一次消息"）、Cron 表达式（精确到分钟的复杂时间规则）。
* 所有定时任务都在独立隔离的会话中运行，不会干扰当前对话。
* 任务执行完成后会自动把结果/通知推送给你，不需要手动查询。
* 支持任务开关、运行历史查看、出错自动重试等能力。

**如何设置定时任务**
你只需要用自然语言告诉 OpenClaw 你的需求就可以，格式：`[时间规则] + [要做的任务]`。例如：
<!-- @cols-width: 259,336,269 -->
| | | | \
|**喝水提醒** |**检查飞书消息** |**每日工作总结** |
|---|---|---|
| | | | \
|```Plain Text |\
|工作日 11 点、15 点、17 点提醒我喝水 |\
|``` |\
| |```Plain Text |\
| |每小时整点、半点执行，检查所有未读私信和群聊中@我的消息。按🔴紧急 / 🟡关注 / 🟢其他三级分类推送给我 |\
| |``` |\
| | |```Plain Text |\
| | |每天下午六点，总结你今天完成的工作，并推送给我 |\
| | |``` |\
| | | |\
| | | |
| | | | \
|![Image=1500x1120](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4ad455a1363a46bc8c21e92b69912acf~tplv-goo7wpa0wc-image.image) |![Image=228x400](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c8d38eeb8fe748749a8d8af3f1fe54f5~tplv-goo7wpa0wc-image.image) |![Image=612x860](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/221e223f3c114ac180038b1c00e5c657~tplv-goo7wpa0wc-image.image) |

### 浏览器工具 {#c15c4fa7}
扣子编程 OpenClaw 配备了 Agent 专用的浏览器，可以帮你完成多种网页相关的操作。例如：

* **浏览网页**：自动打开任意网页，阅读网页中的文本、表格等内容。
* **抓取信息**：提取网页中的数据和信息，例如商品规格、新闻内容、搜索结果等。
* **UI 自动化操作**：模拟用户点击按钮、填写表单、提交信息、滚动页面等操作，可用于网页自动化测试等场景。
* **截图**、**导出 PDF 等**：支持完整页面截图、指定区域截图、将网页内容导出为 PDF 文件等。

**使用方法：**
无需复杂的指令，用自然语言告诉 OpenClaw 你的需求即可，例如：
<!-- @cols-width: 343,404,297 -->
| | | | \
|**访问网页** |**提取Markdown** |**网页截图** |
|---|---|---|
| | | | \
|```Plain Text |\
|帮我访问GitHub查看OpenClaw的最新Release版本 |\
|``` |\
| |```Plain Text |\
| |把这个网页（https://docs.coze.cn/guides/long_memory）的内容完整保存成Markdown格式 |\
| |``` |\
| | |```Plain Text |\
| | |帮我打开扣子编程的首页，截个图看看 |\
| | |``` |\
| | | |
| | | | \
|![Image=264x315](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/48751efa006446f59162f9a095cbd06a~tplv-goo7wpa0wc-image.image) |![Image=310x317](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b7ba41ad94ca477caee3d56b7d28f573~tplv-goo7wpa0wc-image.image) |![Image=1402x1388](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b89bc874c19f4078ae7bc97653206fd6~tplv-goo7wpa0wc-image.image) |

### 记忆能力 {#b3ff90ae}
OpenClaw 的记忆分为短期会话记忆和长期持久记忆两层，所有记忆都存储在你本地的工作区中，不会上传到任何第三方，完全私密安全。重要的信息、规则、偏好会永久存在云端文件里，即使重启、会话结束也不会丢失。
你可以这样感受到 OpenClaw 的记忆能力：

* **定时任务永久生效**：你设置的定时会一直按规则执行，无需每次提醒
* **偏好自动适配**：你表达过的偏好（喜欢的风格、格式、禁忌）等，OpenClaw 会永久记住，每次回复都自动适配。
* **帮你回忆对话**：你和 OpenClaw 聊过的内容都会记录在短期记忆里，可以随时续上之前中断的话题。

直接说`记住：xxxx`，让它主动记录：

* `记住：我的常用地址是杭州市余杭区仓前街道xxx`
* `记住：我喜欢简洁的回复，语气专业但不失俏皮`

<!-- @cols-width: 328,318,289 -->
| | | | \
|**强调记忆** |**唤起回忆** |**总结对话** |
|---|---|---|
| | | | \
|```Plain Text |\
|记住：我的常用地址是杭州市余杭区仓前街道仓南广场 |\
|``` |\
| |```Plain Text |\
| |还记得我的地址在哪里吗 |\
| |``` |\
| | |```Plain Text |\
| | |我们今天都聊了啥，总结一下 |\
| | |``` |\
| | | |
| | | | \
|![Image=745x643](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/df90a60811d24adebf2b46f3afa0d0b2~tplv-goo7wpa0wc-image.image) |![Image=678x303](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9f143272f63e4a138222a39b6454065c~tplv-goo7wpa0wc-image.image) |![Image=731x727](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cf912628decd443bb9a3d9f93a6e1fe1~tplv-goo7wpa0wc-image.image) |

## 全能工具 {#176ae423}
从文档改写、信息检索，到创意文案、日程管理，OpenClaw 内置的实用工具覆盖你日常工作与生活的方方面面。不管是需要快速处理文字、搜集资料，还是辅助内容创作、规划时间，都能通过一次对话搞定。
### 文本创作 {#d926a73f}
支持工作汇报、演讲稿、通知公告、邮件往来、自媒体文案、随笔感悟等多场景文本一键生成。还能按需调整语气风格、篇幅长短与内容侧重点，从初稿搭建到细节优化全程辅助，省去大量构思与撰写时间，高质量内容快速落地，轻松应对各类文字输出任务。
<!-- @cols-width: 419,378,374 -->
| | | | \
|**小红书种草文案** |**小学生日记范文** |深度分析 |
|---|---|---|
| | | | \
|```Plain Text |\
|帮我写个小红书种草文案，介绍下我们的新品：扣子牌的薯片。主要卖点和特色是清新的口味、低油低糖的健康配方、时尚的包装设计，适合各个年龄段，尤其是青少年聚会场景。 |\
|``` |\
| |```Plain Text |\
| |我在辅导小孩写作业，帮我写个小学生日记给他作参考，主题是春天来了。写三篇不同风格的 |\
| |``` |\
| | |```Plain Text |\
| | |帮我做个 OpenClaw 的深度分析，加上一些你的个人观点 |\
| | |``` |\
| | | |\
| | | |
| | | | \
|![Image=1195x890](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2e66ce794dce4c4f97a0b15c1f3d3247~tplv-goo7wpa0wc-image.image) |![Image=1622x1558](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/02166901b03c4ac4952cf5c21a829369~tplv-goo7wpa0wc-image.image) |![Image=1496x1584](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5ac5941acf8a4bc8b1bdf4788e707ed9~tplv-goo7wpa0wc-image.image) |

### 信息检索 {#29ecbc10}
通过扣子编程 OpenClaw 内置的联网搜索技能，你输入关键词即可快速获取全网核心有效信息，涵盖行业资讯、专业知识、数据资料、热点内容、常识科普等各类信息。同时 OpenClaw 自动梳理信息脉络、提炼核心要点，过滤冗余无效内容，帮你快速锁定关键内容，节省海量搜索与整理时间，精准获取所需资料。
<!-- @cols-width: 371,375,323 -->
| | | | \
|**检索热点新闻** |**查询天气** |**事实查证** |
|---|---|---|
| | | | \
|```Plain Text |\
|听说香港要禁烟了，查查相关的新闻资讯 |\
|``` |\
| |```Plain Text |\
| |下周三杭州天气怎么样 |\
| |``` |\
| | |```Plain Text |\
| | |劳动法规定的年假怎么计算？ |\
| | |``` |\
| | | |
| | | | \
|![Image=1602x1544](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bc037d6cfca8494589e97b9f6ada387a~tplv-goo7wpa0wc-image.image) |\
| |![Image=1444x950](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7c75a717a29242d1859c4533aace001a~tplv-goo7wpa0wc-image.image) |\
| | |![Image=1504x1152](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2b9d81c2072545518345d3901be9b44b~tplv-goo7wpa0wc-image.image) |\
| | | |

### 语音能力 {#0f50d4cb}
扣子编程的 OpenClaw 内置了语音能力，包括基于字节跳动豆包大模型的语音合成（TTS）和语音识别（ASR）能力：

* **语音合成（回复你）**：OpenClaw 要回复的文本内容会自动通过TTS接口转换成自然流畅的中文语音，直接发送到飞书会话，单击即可播放。
* **语音识别（接收你的消息）**：向 OpenClaw 发语音消息的时候，它会自动把语音转成文字理解内容，不需要你手动转文字。

你只需要在提问的时候说明想要语音回复，或者直接说`把XX内容用语音读出来`，OpenClaw 就会自动把回复内容转换成语音发送给你。例如：
<!-- @cols-width: 391,387,393 -->
| | | | \
|**语音讲故事** |**语音播报新闻** |**语音识别** |
|---|---|---|
| | | | \
|```Plain Text |\
|用语音给我讲个童话故事 |\
|``` |\
| |```Plain Text |\
| |制作一个 AI 新闻日报，然后用语音读给我听 |\
| |``` |\
| | |```Plain Text |\
| | |帮我总结一下 A 项目进展群里的消息 |\
| | |``` |\
| | | |
| | | | \
|![Image=754x601](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d98592a3951948938c1a1f1548f670fa~tplv-goo7wpa0wc-image.image) |![Image=687x634](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d0163d61acf84422840cdd01a771bfdb~tplv-goo7wpa0wc-image.image) |![Image=1428x1184](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c4bdc69a633d40b3a23024a0ba437b40~tplv-goo7wpa0wc-image.image) |\
| | | |

### 创意制作 {#ba95e497}
除了文本内容的生成以外，扣子编程 OpenClaw 还安装了图片制作和视频生成技能，辅助各类创意内容落地。只要你有灵感，无论是营销海报，还是图文排版、广告视频、AI 漫剧、AI 短剧，都能都能提供多元灵感方案零基础也能轻松做出优质创意内容，让创作不再受限，随心打造专属创意作品。
<!-- @cols-width: 314,293,290 -->
| | | | \
|**制作手抄报** |**制作节气海报** |**制作商品宣传视频** |
|---|---|---|
| | | | \
|```Plain Text |\
|帮我制作一个「清明节」主题的手抄报 |\
|``` |\
| |```Plain Text |\
| |做一个「谷雨」节气海报 |\
| |``` |\
| | |```Plain Text |\
| | |做一个1分钟左右的，小狗带逛卢浮宫的视频，9:16比例。从平静地带逛开始，但是在看完蒙娜丽莎之后，卢浮宫现场被黑衣人打劫了。 |\
| | |``` |\
| | | |
| | | | \
|![Image=264x352](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5feb05adabbd4647adfc819e5527f9d7~tplv-goo7wpa0wc-image.image) |\
| |![Image=254x339](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/90cf219072a54a48a23a67d572d72feb~tplv-goo7wpa0wc-image.image) |\
| | |<Player src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b447ccb8a4da49a18fbc693f364c73ba~tplv-goo7wpa0wc-image.image"></Player> |

## 多渠道对话 {#9f7906bc}
不用再频繁切换软件，在你最熟悉的飞书、微信等聊天工具里，就能直接召唤 OpenClaw。无论是收发消息、整理会议纪要，还是安排日程、撰写周报，一句话就能让 AI 帮你高效处理，让办公沟通更流畅、更省心。
此外，所有渠道的数据、记忆是完全同步的，不会因为换了渠道就"失忆"。
### 飞书渠道 {#8a06b6c5}
飞书渠道是工作场景的首选，支持交互式卡片、文件上传下载、日程/任务/文档等飞书生态深度集成。
为了能在飞书和你的 OpenClaw 龙虾对话，参考以下步骤完成飞书渠道的配置。

1. 在[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)中找到你的 OpenClaw 项目。
   ![Image=501x282](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c31cf07587da4d9896529de53d1814b9~tplv-goo7wpa0wc-image.image)
2. 在页面右上角单击设置图标，打开 **OpenClaw 配置**页面。
   ![Image=468x256](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/77764c59db6d48e69d894f3e0493ef8b~tplv-goo7wpa0wc-image.image)
3. （可选）找到**飞书**渠道，为你的 OpenClaw 龙虾助手设置名称。
   ![Image=238x274](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e063d43a9567458aaef9b2f6af7cf214~tplv-goo7wpa0wc-image.image)
4. 单击**授权并创建**。
   ![Image=257x291](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e973e9da4a6f444ca5bc672802c491c4~tplv-goo7wpa0wc-image.image)
5. 根据页面提示完成授权。
   ![Image=293x312](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0694eda71d2d4d23ad5e432e29d640fd~tplv-goo7wpa0wc-image.image)
6. 创建成功，单击去飞书对话。
   ![Image=274x287](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ba9ae004341d4789b863c1f7a8aca7e3~tplv-goo7wpa0wc-image.image)

  页面会自动跳转到飞书客户端，你可以直接发送消息和你的 OpenClaw 助手对话。

   ![Image=292x257](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/72e265b997514362b19754a36343c851~tplv-goo7wpa0wc-image.image)

### 微信渠道 {#a731a92f}
微信是当前热门且普遍使用的 IM 聊天工具，为你的 OpenClaw 配置微信渠道，在微信里和它对话，操作更编辑。
参考以下步骤完成微信渠道的配置。

1. 在[扣子编程](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)中找到你的 OpenClaw 项目。
   ![Image=375x211](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/750e0fa9285a410da7b9af21db5dde28~tplv-goo7wpa0wc-image.image)
2. 页面右上角单击设置图标，打开 **OpenClaw 配置**页面。
   ![Image=409x224](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bb2aaa6a8c3647d5a3c093f8c047d035~tplv-goo7wpa0wc-image.image)
3. 找到微信渠道，单击**去创建**。
   ![Image=490x253](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/be84741b0736487a8407c4184c109226~tplv-goo7wpa0wc-image.image)
4. 打开微信客户端，扫描屏幕显示的二维码。根据微信客户端提示，单击**连接**。
5. 后台会自动完成渠道连接，并自动打开一个名为**微信 ClawBot** 的对话页面。
   输入任意一条消息，测试微信机器人是否能正常回复。 


::::cols
@col 50
   ![Image=193x418](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/15da3218e8834e928ff2b40446ade6be~tplv-goo7wpa0wc-image.image)


@col 50
   ![Image=192x415](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/22d419efbb0a42188fd160766566b799~tplv-goo7wpa0wc-image.image)

::::

### 其他渠道 {#a76245c8}
此外，扣子编程 OpenClaw 还支持绑定钉钉、企业微信等渠道，参考以下使用指南完成配置：

* [OpenClaw 集成钉钉](/tutorial/openclaw_dingding)
* [OpenClaw 集成企业微信](/tutorial/openclaw_work_wechat)
