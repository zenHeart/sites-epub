> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

Coze CLI 是扣子面向 AI Agent 和开发者提供的命令行工具。它把扣子编程中的项目开发、预览部署、资源管理和多媒体生成等能力，封装为 Agent 可以调用的命令。

你不需要记住具体命令。只需告诉扣子想完成什么，它就能通过 Coze CLI 创建 Web 应用、导入已有项目继续开发、连接数据库，或者批量生成图片、语音和视频。创建的项目和产物会保存在你的扣子账号下，也可以继续在扣子编程中查看和管理。

想进一步了解 Coze CLI  定位、典型场景和完整能力，可以阅读 [Coze CLI 介绍](https://docs.coze.cn/developer_guides_coze_cli)。

## 为什么需要登录授权 {#hudvK4jhJ}

扣子已经预安装 Coze CLI，无需自行安装或配置环境。打开 [coze.cn](https://www.coze.cn/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=) 并登录扣子，就可以在对话中直接提出需求。

Agent 调用 Coze CLI 时，需要使用你的扣子账号和权限执行操作，创建好的应用、数据库和生成内容也会保存在你的账号下。因此，第一次使用 Coze CLI 前，需要先完成账号授权。

## 完成首次授权 {#hqrsi43Ud}

在扣子对话中输入：

```Plain Text
使用 Coze CLI 帮我登录扣子账号。
```

扣子会自动发起登录，并返回授权链接和授权码。接下来：

1. 访问授权链接，输入授权码。
2. 确认授权范围并完成授权。
3. 回到扣子对话，告知扣子已经完成授权。
   注意：授权码有效期为 5 分钟。过期后，需要让扣子重新生成授权链接和授权码。
   不同账号版本的授权范围有所区别：
   * **个人版：​**默认授予此账号在个人版下所有空间的权限。
   * **企业版：​**你需要在授权页面选择允许访问的企业组织和工作空间。

<!-- @cols-width: 222,238,240,221 -->
| **要求登录**  | **确认授权码**  | **完成授权**  | **登录成功**  |
| --- | --- | --- | --- |
| ![Image=1564x742](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/11b43f75e9b54ba08080d190b21bd3a2~tplv-goo7wpa0wc-topic.webp)  | ![Image=2662x1550](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/fa5e9af5b0be404e98a5b81b066a383a~tplv-goo7wpa0wc-topic.webp)  | ![Image=2792x1519](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a557d1b5188f4489bc97f72c8335683a~tplv-goo7wpa0wc-topic.webp)  | ![Image=141x128](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4f9567b37629421796c8bfcf863cabe7~tplv-goo7wpa0wc-topic.webp)  |

## 登录后还可以做什么 {#hTfVWeoqn}

* **查看登录状态。** 如果创建资源时提示没有权限，或找不到组织、工作空间，可以先让扣子检查当前账号和授权状态：
   ```Plain Text
   帮我检查 Coze CLI 当前登录的是哪个账号，授权是否仍然有效。
   ```
* **刷新授权。** 扣子通常会定期刷新授权，以保持登录状态。如果意外掉线，扣子会重新生成授权链接，按照提示重新登录即可。
* **退出或切换账号。** 切换账号，或在测试结束后需要清理本机登录身份时，可以说：
   ```Plain Text
   退出 Coze CLI 当前账号，然后帮我重新登录。
   ```   


## 注意账号与信息安全 {#hqq9aFRLj}

正常的 OAuth 授权不需要向扣子提供账号密码。不要在对话中发送访问令牌、数据库密码或其他敏感信息。

企业版用户授权时，应只选择当前任务需要访问的组织和工作空间。如果后续权限发生变化，可以重新发起授权。
