> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子桌面端可以直接连接你的电脑，让 Agent 在获得授权后处理本地文件、使用本地软件和插件，并完成开发、整理、分析等需要本地环境的任务。项目、对话、文件和任务进度会与移动端和网页端同步，离开电脑后也能继续查看和推进。

扣子桌面端支持 macOS 和 Windows。访问[扣子官网](https://www.coze.cn/)，下载并安装适合你电脑系统的版本。

::::cols
@col 33
**直接处理本地文件**

在获得授权后，Agent 可以读取、整理和修改电脑中的文件，帮助你处理分散在本地的资料。

@col 33
**连接本地软件和插件**

通过插件连接 WPS、浏览器等本地软件，让 Agent 在实际工作环境中完成任务。

@col 34
**与其他端协同工作**

项目、对话、文件和任务进度可以多端同步。离开电脑后，你仍可以通过移动端继续查看和调度任务。
::::

<img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/cover.png" width="600" alt="扣子桌面端界面" />

## 快速开始 {#快速开始}

下面以整理桌面文件为例，带你完成第一个桌面端任务。

### 步骤一：下载并登录桌面端 {#步骤一：下载并登录桌面端}

1. 访问[扣子官网](https://www.coze.cn/overview/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)，下载适合你电脑系统的桌面端。鼠标指向**下载桌面端**，下载并安装。
   你也可以直接下载安装包：[macOS（）](https://ugapk.com/FJvCs) | [macOS（Intel）](https://ugapk.com/N752o) | [Windows](https://ugapk.com/FJvCs)
2. 完成安装并启动扣子。
3. 登录扣子账号。

### 步骤二：发起新任务 {#步骤二：发起新任务}

在页面左上角单击**新任务**，选择一个 Agent，然后在对话输入框中说明要整理的文件、分类方式和操作限制。例如：

```text
整理桌面上的文件，按照工作、学习、图片和其他分类。执行移动操作前，先把整理方案和文件移动清单发给我确认，不要直接移动或删除文件。
```

你也可以在发送指令前添加本地文件、文件夹、截图或插件，为 Agent 提供完成任务所需的上下文和工具。

<img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/quick-task.png" width="600" alt="发起桌面端任务" />

### 步骤三：授权并确认执行 {#步骤三：授权并确认执行}

为了查看桌面文件并生成整理方案，Agent 会请求使用 Bash 执行命令。检查要执行的命令和使用的工具，确认无误后，单击**允许一次**。如果不希望 Agent 执行该命令，单击**拒绝**。

<img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/authorize.png" width="520" alt="授权 Agent 执行命令" />

Agent 完成桌面文件盘点后，会列出整理方案和文件移动清单，并询问是否执行移动。确认方案符合预期后，选择**按方案执行（推荐）**，然后单击**提交回答**。如果需要调整，选择**先不执行**，并在对话中补充要求。

<img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/confirm-plan.png" width="520" alt="确认文件整理方案" />

### 步骤四：查看执行结果 {#步骤四：查看执行结果}

整理完成后，Agent 会返回各分类中的文件数量和内容摘要。你可以对照桌面上的文件夹检查结果，也可以继续提出要求，例如调整分类或移动遗漏的文件。

如果需要离开电脑，可以在移动端或网页端登录同一账号，继续查看任务进度和对话结果。

::::cols
@col 50
**桌面端查看结果**

<img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/result-desktop.png" width="360" alt="桌面端任务结果" />

@col 50
**移动端继续任务**

<img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/result-mobile.png" width="220" alt="移动端任务结果" />
::::

## 接下来你可以 {#接下来你可以}

* [添加插件](https://docs.coze.cn/plugin)：连接 WPS、浏览器等软件，扩展 Agent 可以完成的工作。
* [操作本地设备](https://docs.coze.cn/cozespace_local_device)：将当前电脑连接到扣子，让 Agent 在授权范围内读取和处理电脑中的文件。
* [创建项目](https://docs.coze.cn/cozespace_create_projects)：集中管理长期任务所需的 Agent、成员、对话、文件和成果。
* [组建 AI 团队](https://docs.coze.cn/cozespace_coze_ai_team_quickstart)：让多个 Agent 分工处理同一个项目中的不同任务。
* [切换移动端或网页端](https://docs.coze.cn/what_is_coze#1ad3c90d)：在其他设备上继续查看和处理已有任务。

## 桌面端能做什么 {#桌面端能做什么}

### 整理和处理本地文件 {#整理和处理本地文件}

在获得目录访问权限后，Agent 可以查找、读取、归类和修改本地文件，并根据文件内容生成摘要、清单或新的文档。涉及移动、覆盖或删除文件时，你可以要求 Agent 先提供计划，确认后再执行。

**示例指令**

```text
在我本地桌面“新品发布会”文件夹中找到最新的策划方案，review 一下内容，没问题的话发到“整理活动复盘”这个项目里，请小李确认。
```

<img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/local-files.png" width="600" alt="整理和处理本地文件" />

### 使用本地软件和插件 {#使用本地软件和插件}

通过插件，Agent 可以连接 WPS 等桌面端插件、内置浏览器，在你熟悉的工作环境中读取内容、生成文件或继续编辑结果。首次使用相关能力时，请按照页面提示完成安装、连接或授权。

1. 登录扣子桌面端。
2. 在左侧单击**扩展 > 插件**，找到 [WPS 插件](https://www.coze.cn/skills?tab=space&capability=plugin&plugin_share_pid=7676731098465845298)，然后单击**连接 > 去连接**。
3. 根据页面提示，选择需要添加插件的 Agent，单击**添加**。
4. 向 Agent 发送指令。例如：

```text
@WPS Office，根据我的电脑桌面“新品发布会”文件夹中活动策划方案和预算表制作一份发布会执行汇报 PPT。
```

::::cols
@col 50
**生成结果**

<img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/wps-result.png" width="360" alt="WPS 插件生成结果" />

@col 50
**PPT 预览**

<img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/ppt-preview.png" width="360" alt="PPT 预览" />
::::

### 开发和调试本地项目 {#开发和调试本地项目}

打开本地项目目录后，Agent 可以读取代码、定位问题、修改文件，并运行项目或测试进行验证。你可以在指令中明确修改范围，避免影响与当前问题无关的文件。

1. 创建新任务，设置任务运行环境为本机，并开启本机操作免确认。
   <img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/local-env.png" width="520" alt="设置本地运行环境" />
2. 发送指令，在本地开发应用。例如：

```text
@编程开发 开发一个记账小程序，能记录每天的每笔收入和支出，支持简单的分类，另外还可以查看每日/每月汇总。
```

::::cols
@col 50
**应用效果**

<img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/app-result.png" width="360" alt="本地项目运行效果" />

@col 50
**本地文件**

<img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/local-output.png" width="360" alt="本地项目文件" />
::::

### 跨端持续推进任务 {#跨端持续推进任务}

桌面端、移动端和网页端会同步项目、对话和任务进度。你可以在电脑上启动需要本地文件或软件的任务，离开电脑后再通过移动端查看进度、补充要求或继续调度。

**示例指令**

```text
@网页版游戏 帮我写一个像素风的网页版贪吃蛇小游戏，要马卡龙配色。
```

::::cols
@col 50
**在电脑端下达任务**

<img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/cross-desktop.png" width="360" alt="电脑端发起任务" />

@col 50
**在移动端查看进度和产物**

<img src="https://lf3-static.bytednsdoc.com/obj/eden-cn/%E5%AD%90%E6%89%A3/ljhwZthlaukjlkulzlp/coze-docs/quick-start-desktop/cross-mobile.png" width="220" alt="移动端查看任务" />
::::
