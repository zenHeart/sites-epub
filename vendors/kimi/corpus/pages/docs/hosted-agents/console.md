> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用控制台

> 通过 Kimi 托管智能体控制台创建智能体、配置技能和插件、准备环境并创建会话。

Kimi 托管智能体控制台适合在不写代码的情况下完成基础配置并体验任务。

当前的基本流程是：创建智能体、配置技能和插件、准备环境、按需创建凭据库，然后创建会话。

**控制台不覆盖全部 API 能力。记忆库、定时任务等功能需要通过 API 使用，详见 [快速开始](/docs/hosted-agents/quickstart)。**

## 快速开始：创建智能体并启动会话

“快速开始”页面是创建智能体并启动首次会话的向导，分为三步：创建智能体、配置环境、启动会话。

<img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/console/create-agent-templates.png?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=b6500e5a12b57684e1a8af7906b59ec4" alt="创建智能体向导：选择模板并填写基础信息" width="2996" height="1404" data-path="assets/pics/console/create-agent-templates.png" />

### 第一步：创建智能体

你可以从模板开始，也可以从空白配置开始：

<Steps>
  <Step title="选择模板">
    在侧边栏打开“快速开始”，选择“PPT 助手”“金融投资分析助手”或“空白智能体”。模板会预填一部分配置，创建后仍然可以修改。
  </Step>

  <Step title="填写基础信息">
    在“表单视图”中填写名称和模型，也可以补充描述和系统提示词。页面同时提供“Raw 配置”视图，适合需要直接检查配置的场景。
  </Step>

  <Step title="配置能力">
    按需添加多智能体委派、技能、插件、内置工具与工具权限，以及 MCP 服务器。只选择当前任务需要的能力，详细配置说明见 [创建与管理智能体](/docs/hosted-agents/agents)。
  </Step>

  <Step title="保存并继续">
    点击“保存并继续”，进入环境配置。创建成功后，保存返回的智能体 ID，后续创建会话时需要选择这个智能体。
  </Step>
</Steps>

<img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/console/create-agent-capabilities.png?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=75614f45ac87c8929e62da816adf89a6" alt="配置多智能体、技能、插件和工具，点击“保存并继续”" width="1642" height="2058" data-path="assets/pics/console/create-agent-capabilities.png" />

### 第二步：配置环境

可以直接使用“默认执行环境”（推荐，通用云端沙箱，适合大多数任务），也可以选择“创建新环境”基于当前组织新建。按需配置网络访问范围，然后点击“创建并继续”。

<img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/console/wizard-environment.png?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=38e0e69d6add63d684119a47dea966ba" alt="配置环境：选择环境并点击“创建并继续”" width="3024" height="1430" data-path="assets/pics/console/wizard-environment.png" />

### 第三步：启动会话

确认本次会话使用的智能体与环境（向导已预填），可选绑定凭据库、添加文件，然后点击“启动并进入会话”。创建成功后将自动进入会话工作区。

<img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/console/wizard-session.png?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=30614852dd5f18107d80ee56237def17" alt="启动会话：确认资源并点击“启动并进入会话”" width="3024" height="1550" data-path="assets/pics/console/wizard-session.png" />

## 控制台中的资源页面

### 智能体

“智能体”页面以表格展示可见的智能体，包含以下信息：

* 智能体 ID、名称和模型；
* 归属和状态；
* 创建人、创建时间和最近更新。

可以按名称或智能体 ID 搜索，并按状态和创建时间筛选。使用“创建智能体”按钮进入创建流程。官方智能体带有“官方”标记，项目中创建的智能体带有“项目”标记。列表行尾的操作菜单根据资源状态和权限提供可用操作。

<img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/console/official-agent-list.png?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=4758cd60f7e882b2eeb38bc97e90cceb" alt="智能体列表：点击右上角“创建智能体”按钮" width="3006" height="1418" data-path="assets/pics/console/official-agent-list.png" />

### 技能

“技能”页面按“全部、官方、组织、项目”查看技能，支持搜索和按状态筛选，也可以选择是否显示已归档技能。列表显示技能 ID、名称、归属、状态、最新版本和最近更新。

使用“上传技能”添加项目技能，然后在创建或配置智能体时选择它。官方技能在控制台中只读。技能的版本和使用方式见 [技能](/docs/hosted-agents/skills)。

<img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/console/official-skill-list.png?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=45fea6c05db7ccfdf213dbafcd7176c9" alt="技能列表：点击右上角“上传技能”按钮" width="3006" height="1398" data-path="assets/pics/console/official-skill-list.png" />

### 插件

“插件”页面以卡片目录展示已上架插件，可以按分类浏览，例如金融数据、投研工作流、办公协作和开发者工具。插件卡片会显示名称、简介，以及其中包含的技能或 MCP 服务数量。

在创建智能体时，可以从插件目录选择插件并加入配置。插件的具体能力和凭据要求以插件详情为准。

<img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/console/plugin-directory.png?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=a61090db9b7a48323f8b8608655662f6" alt="插件目录：按分类浏览已上架插件" width="3008" height="1532" data-path="assets/pics/console/plugin-directory.png" />

### 环境

“环境”页面展示环境 ID、名称、状态、归属、创建人、创建时间和更新时间。可以搜索环境，按归属和状态筛选，也可以选择是否显示已归档环境。

使用“创建环境”按钮新建环境。创建或更新环境后，等待状态变为 `Ready`，再在创建会话时选择它。依赖包、网络配置和初始化脚本等详细配置见 [执行环境](/docs/hosted-agents/environments)。

<img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/console/official-environment-list.png?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=a7d79cde550fadd6530af6a1b018bfb3" alt="环境列表：点击右上角“创建环境”按钮" width="3008" height="1466" data-path="assets/pics/console/official-environment-list.png" />

### 凭据库

“凭据库”页面按“全部、组织、项目”查看凭据库，支持搜索，也可以选择是否显示已归档凭据库。列表显示凭据库 ID、名称、归属、凭据数量、状态、创建人和创建时间。

使用“新建凭据库”创建凭据库。会话需要访问外部服务时，可以在创建会话时选择凭据库，让平台在运行期间注入凭据。凭据值只写入、不回显；创建后无法再次查看明文，需要变更时轮换凭据值。详细操作见 [凭据库](/docs/hosted-agents/vaults)。

<img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/console/vault-list.png?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=bf093da7e89a3493d29e8bdd6125abde" alt="凭据库列表：点击右上角“新建凭据库”按钮" width="2964" height="464" data-path="assets/pics/console/vault-list.png" />

### 会话

“会话”页面展示会话 ID、名称、状态、智能体、归属、创建人和创建时间。可以搜索会话，也可以按智能体和状态筛选。

使用“创建会话”创建一次任务运行实例：

<Steps>
  <Step title="选择智能体和环境">
    选择已经准备好的智能体和处于 `Ready` 状态的环境。它们是创建会话所需的基本资源。
  </Step>

  <Step title="按需配置资源">
    根据控制台当前提供的选项，按需选择凭据库、文件等资源。
  </Step>

  <Step title="创建并查看状态">
    提交后，在会话列表中查看会话状态，状态包括“运行中”“空闲”和“已结束”；进入会话详情页可以继续查看该会话的内容。
  </Step>
</Steps>

<img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/console/session-list-page.png?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=b6e64fdf25c2374e7e5f06d4cf475af4" alt="控制台会话列表：状态列显示“运行中”“空闲”和“已结束”" width="3002" height="942" data-path="assets/pics/console/session-list-page.png" />

#### 会话工作区

进入会话后，中间区域展示对话与执行过程，底部输入框可以继续发送任务。右侧有两个标签页：

* “会话信息”：查看会话状态、会话 ID，以及会话绑定的资源——智能体、模型、环境、技能、插件和子智能体。

  <img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/console/session-info-panel.png?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=7355276bbc66457f1a359d2ecdd7834d" alt="“会话信息”标签页：查看会话绑定的资源" width="3024" height="1440" data-path="assets/pics/console/session-info-panel.png" />

* “文件”：查看会话工作目录的文件树。智能体生成的产物保存在 `output` 文件夹中，点击文件即可下载。

  <img src="https://mintcdn.com/moonshotcn/lKRBEYaiJs4EEiwf/assets/pics/console/session-files-panel.png?fit=max&auto=format&n=lKRBEYaiJs4EEiwf&q=85&s=8395fe9a73dcdac23c6dfedf1f67fede" alt="“文件”标签页：output 文件夹中的产物可点击下载" width="3024" height="1506" data-path="assets/pics/console/session-files-panel.png" />

创建会话的 API 流程还包括发送首条消息来启动任务，详见 [启动会话](/docs/hosted-agents/sessions)。控制台页面中的具体操作以当前项目实际显示的按钮和菜单为准。

## 官方资源

官方智能体、官方环境和官方技能在列表中带有官方标记。官方资源对项目可见，但只能读取和使用，不能修改；如需自定义配置，请创建自己的资源。

## 下一步

<CardGroup cols={2}>
  <Card title="快速开始" icon="rocket" href="/docs/hosted-agents/quickstart">
    用 API 跑通从创建智能体到完成任务的完整链路。
  </Card>

  <Card title="hakimi" icon="terminal" href="/docs/hosted-agents/hakimi">
    用 hakimi 在编程助手中以自然语言创建和使用托管智能体。
  </Card>

  <Card title="启动会话" icon="message" href="/docs/hosted-agents/sessions">
    通过 API 创建会话、绑定资源并发送首条消息。
  </Card>

  <Card title="记忆库" icon="book" href="/docs/hosted-agents/memory">
    通过 API 创建和管理记忆库。
  </Card>

  <Card title="执行环境" icon="box" href="/docs/hosted-agents/environments">
    配置会话使用的云沙箱。
  </Card>
</CardGroup>
