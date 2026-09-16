> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 5 分钟开发「羊了个羊」小游戏

> <Note> 本教程将指导您如何通过 MiniMax Agent 设计精准开发提示词，在 MonkeyCode 平台接入 MiniMax M2.1 模型，快速开发一款具备完整玩法的 Web 端「羊了个羊」风格三消休闲游戏。 </Note>

<div style={{display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px'}}>
  <div style={{width: '40px', height: '40px', borderRadius: '50%', background: 'linear-gradient(135deg, #6366f1, #8b5cf6)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'white', fontWeight: 'bold'}}>W</div>

  <div>
    <div style={{fontWeight: 500}}>Wanling</div>
    <div style={{fontSize: '0.875rem', color: '#9ca3af'}}>2026年2月8日</div>
  </div>
</div>

## 概述

本教程将指导您如何通过 MiniMax Agent 设计精准开发提示词，在 MonkeyCode 平台接入 MiniMax M2.1 模型，快速开发一款具备完整玩法的 Web 端「羊了个羊」风格三消休闲游戏。全程无需手动编写核心代码，借助 AI 实现从需求定义到项目部署的全自动化开发，支持多技术栈选择、道具系统集成和多关卡设计，适配 PC 与移动端。

**核心亮点：**

* 计时 304.5 秒完成项目初始化与核心开发
* 支持 React / Vue / 原生 HTML/CSS/JS 多技术栈
* 内置「移出、撤回、洗牌」3 个实用道具
* 包含 3 个难度递增关卡，卡通风格 UI 与流畅动画
* 响应式设计，自动适配移动端与 PC 端
* 完整项目结构，支持二次开发与部署上线

***

## 第一部分：使用 MiniMax Agent 设计开发提示词

<Note>
  前往 [MiniMax Agent](https://agent.minimaxi.com/) 即可体验，帮助您快速完成各种任务。
</Note>

### 1. 明确核心需求

向 MiniMax Agent 提交基础开发诉求，明确游戏类型、核心要求：

> 我需要设计一个给 AI Agent 使用的提示词，用于在 MonkeyCode 中开发 Web 端「羊了个羊」小游戏，请协助完善提示词细节。

<img src="https://filecdn.minimax.chat/public/398313c1-39fd-4348-a29c-b6e5d0d9bac5.png" width="80%" />

### 2. 确认需求细节

MiniMax Agent 会自动询问关键配置项，需补充以下信息以确保提示词精准度：

* **技术栈偏好**：React / Vue / 原生 HTML/CSS/JS（任选其一，推荐 React 或原生），无需游戏引擎
* **美术风格**：卡通可爱风格
* **功能范围**：基础三消玩法 + 移出、撤回、洗牌 3 个道具 + 详细代码注释
* **构建工具**：推荐 Vite（或 Create React App / Vue CLI）
* **图标资源**：SVG 图标或 Icon Font（如 Font Awesome）

<img src="https://filecdn.minimax.chat/public/9482a24c-8c5f-4861-923a-cde24d777a78.png" width="80%" />

### 3. 生成完整开发提示词

MiniMax Agent 会基于上述需求，生成结构化开发提示词，最终版本如下：

<Accordion title="查看完整开发提示词">
  **# 「羊了个羊」Web 游戏开发提示词**

  **## 项目概述**

  开发一个基于 Web 的「羊了个羊」风格三消休闲游戏。玩家通过点击上层方块将其移动到下方槽位，三个相同图案的方块自动消除，最终清除所有方块即可通关，整体采用卡通可爱风格。

  **## 技术栈要求**

  * 前端框架：React / Vue.js / 原生 HTML5+CSS3+JavaScript（任选其一，推荐 React 或原生）
  * 样式方案：CSS3 动画 + Flexbox/Grid 布局
  * 构建工具：Vite（推荐）或 Create React App / Vue CLI
  * 图标资源：使用 SVG 图标或 Icon Font（如 Font Awesome）

  **## 核心功能要求**

  1. **基础玩法**：三层堆叠方块设计，上层方块消除后可点击下层方块，槽位最多容纳 7 个方块
  2. **道具系统**：实现「移出」「撤回」「洗牌」3 个道具，支持游戏过程中使用
  3. **关卡设计**：包含 3 个难度递增关卡（新手牧场 → 进阶草原 → 高级山脉），关卡难度差异为方块类型数量增加
  4. **交互反馈**：点击方块添加高亮+缩放效果，消除时添加淡出+缩放动画，胜利/失败弹出提示弹窗
  5. **适配要求**：响应式设计，兼容 PC 端与移动端显示

  **## 代码规范**

  1. 分模块开发，包含组件、工具函数、数据配置、样式文件等目录结构
  2. 变量命名语义化，核心函数（方块生成、消除判断、道具逻辑等）独立拆分
  3. 代码添加详细注释，说明核心逻辑与可修改参数
  4. 输出完整项目文件，包含启动、构建、预览命令说明
</Accordion>

***

## 第二部分：MonkeyCode 配置与项目开发

### 1. 登录 MonkeyCode 平台

访问 [MonkeyCode 官网](https://monkeycode-ai.com/?ic=019b4f38-64b2-7dee-959c-ec02691c290d) 进行登录。如需配置个人 MiniMax-M2.1 接口，请参考 [MonkeyCode 接入指南](/docs/token-plan/monkeycode)。

### 2. 提交开发任务

<Steps>
  <Step title="粘贴开发提示词">
    在 MonkeyCode 智能任务界面，粘贴上述生成的完整开发提示词。
  </Step>

  <Step title="配置任务参数">
    配置以下任务参数：

    | 配置项      | 值            |
    | -------- | ------------ |
    | **开发工具** | OpenCode     |
    | **大模型**  | MiniMax-M2.1 |
    | **其他**   | 保持默认配置       |

    点击「确认执行」，启动开发任务。

    <img src="https://filecdn.minimax.chat/public/c8536fb4-8b51-45f7-8c2f-afe826115a90.png" width="80%" />

    <img src="https://filecdn.minimax.chat/public/4be86c54-b6c0-4980-b7eb-d10a9d087e8b.png" width="80%" />
  </Step>

  <Step title="创建项目分支">
    MonkeyCode 会初始化一个虚拟环境，并自动生成默认分支名 `2xxxxx-feat-develop-sheep-elimination-game`，在终端需要输入指令确认创建并切换分支。

    之后 MonkeyCode 会自动初始化项目结构、安装依赖、配置 Vite 环境（允许 hosts 访问）。

    <img src="https://filecdn.minimax.chat/public/44669353-8c40-4384-b2a6-2970822b94b8.png" width="80%" />
  </Step>

  <Step title="等待开发完成">
    无需手动干预，MonkeyCode 会自动完成以下工作：

    * 创建项目目录结构与核心文件
    * 编写组件代码（方块、槽位、游戏面板、道具栏、关卡选择等）
    * 实现游戏核心逻辑（方块堆叠、消除判断、道具功能、关卡切换等）
    * 配置样式文件与动画效果
    * 部署项目至本地端口（默认 5173 端口）

    开发完成后，系统会提示项目部署成功，浏览器访问 MonkeyCode 开放的地址，即可体验游戏。

    <img src="https://filecdn.minimax.chat/public/16aac1ae-09e9-4a9f-a331-35d937b06854.png" width="80%" />
  </Step>
</Steps>

### 3. 项目目录结构

```
sheep-elimination-game/
├── .gitignore
├── vite.config.js（已配置 allowedHosts）
├── README.md
├── src/
│   ├── components/
│   │   ├── Game/（Block、Slot、GameBoard 组件）
│   │   ├── UI/（LevelCard、ResultModal 组件）
│   │   └── Props/（PropsBar 道具栏组件）
│   ├── data/
│   │   └── levels.json（关卡配置数据）
│   ├── utils/
│   │   └── gameLogic.js（游戏核心逻辑函数）
│   └── styles/
│       └── main.css（全局样式文件）
```

***

## 第三部分：核心功能验证

开发完成后，可通过以下维度验证游戏功能完整性：

| 功能模块     | 验证要点                               |
| -------- | ---------------------------------- |
| **基础玩法** | 三层方块堆叠、槽位容量限制、相同方块消除               |
| **道具系统** | 移出（删除槽位单个方块）、撤回（恢复上一步）、洗牌（打乱待选区方块） |
| **关卡切换** | 3 个关卡难度递增、关卡选择界面正常显示               |
| **交互反馈** | 点击高亮、消除动画、胜负弹窗、重新开始功能              |
| **适配性**  | 移动端 / PC 端界面无变形、点击区域响应正常           |

<img src="https://filecdn.minimax.chat/public/31e227a3-e510-4ddc-aa8d-4f5452bcf464.png" width="80%" />

<img src="https://filecdn.minimax.chat/public/39c69f43-a2b8-42c8-a407-c42c6bad86e6.png" width="80%" />

<img src="https://filecdn.minimax.chat/public/7e2e3e7f-03d6-40bd-870c-b8bd4fa691c9.png" width="80%" />

***

## 总结

通过 MiniMax Agent 设计精准提示词 + MonkeyCode 接入 MiniMax M2.1 模型，实现了「羊了个羊」小游戏的快速开发：

* **全程无需手动编写复杂逻辑**，无需任何编程基础，5 分钟内即可完成从需求到部署的全流程
* **MiniMax Agent** 的 thinking 能力使其能够精准理解需求，自动生成结构化的开发提示词
* **MiniMax M2.1 的代码生成能力**在 MonkeyCode 中表现出色，304.5 秒完成完整游戏开发
* 生成的项目结构清晰、代码可维护性强，支持二次开发（如添加排行榜、节日皮肤、更多道具等）

***

## 相关资源

<Columns cols={3}>
  <Card title="MiniMax M2.1" icon="sparkles" href="https://minimaxi.com/news/minimax-m21">
    模型详细介绍
  </Card>

  <Card title="MonkeyCode 接入指南" icon="code" href="/docs/token-plan/monkeycode">
    在 MonkeyCode 中配置 MiniMax
  </Card>

  <Card title="MiniMax 开放平台" icon="globe" href="https://platform.minimaxi.com">
    获取 API Key
  </Card>
</Columns>
