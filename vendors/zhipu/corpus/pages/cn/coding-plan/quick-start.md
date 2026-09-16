> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速开始

本指南将帮助您快速上手 GLM Coding Plan，只需几分钟即可完成。

<Note>
  GLM Coding Plan 仅限在官方支持的[指定工具与产品环境](https://docs.bigmodel.cn/cn/coding-plan/tool/others#%E4%B8%80%E3%80%81%E9%80%82%E7%94%A8%E5%B7%A5%E5%85%B7)中使用
</Note>

## 开始使用

<Steps>
  <Step title="注册账号">
    访问[智谱开放平台](https://open.bigmodel.cn)，点击右上角的「注册/登录」按钮，按照提示完成账号注册流程。
  </Step>

  <Step title="订阅 GLM Coding Plan">
    登录后，前往 [套餐详情页](https://zhipuaishengchan.datasink.sensorsdata.cn/t/Gd) 选择适合您的订阅套餐。
  </Step>

  <Step title="获取 API Key">
    订阅套餐后:

    * 个人版套餐（或领取体验卡）的用户，通过 [个人编程套餐 > 套餐概览](https://bigmodel.cn/coding-plan/personal/overview)，新建 API Key
    * 团队版套餐的成员，通过 [团队编程套餐 > 我的套餐](https://bigmodel.cn/coding-plan?z_plan=team)，获取 API Key（团队套餐 Key 与平台其他 API Key 不通用，使用团队额度请务必使用团队套餐 Key）

    <Warning>
      请妥善保管您的 API Key，不要泄露给他人，也不要直接硬编码在代码中。
    </Warning>
  </Step>

  <Step title="接入编码工具">
    GLM Coding Plan 仅限在官方支持的[指定工具与产品环境](https://docs.bigmodel.cn/cn/coding-plan/tool/others#%E4%B8%80%E3%80%81%E9%80%82%E7%94%A8%E5%B7%A5%E5%85%B7)中使用，您可以根据自己的偏好选择下方工具点击进入配置参考：

    <CardGroup cols={3}>
      <Card title="ZCode（1.5倍用量）" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rocket.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=859cb435da005a3984eae8dc9f60ea7c)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/zcode">
        面向 Long Horizon Task 的全功能 ADE
      </Card>

      <Card title="Claude Code" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f67130d1597ee0b68135487ec31662f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/claude">
        智能终端编码助手，支持自然语言编程
      </Card>

      <Card title="Codex" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/plug.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=ee8b6362dc2efcf3b5e159abe7f85bc0)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/codex">
        AI 编程智能体，能帮你编写、审查和调试代码。
      </Card>

      <Card title="Autoclaw" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/hammer.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2f79760a2b8464f3d2cea1c006663f5f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/autoclaw">
        专业领域工作助手，深度适配 GLM
      </Card>

      <Card title="Cline" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/rectangle-code.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=82ca857a2fed05569953c4d6b97ce735)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/cline">
        VS Code 扩展，提供智能代码补全和调试
      </Card>

      <Card title="OpenCode" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/AteIdKqxoD35bkVX/resource/icon/window.svg?fit=max&auto=format&n=AteIdKqxoD35bkVX&q=85&s=ce809df2afccb242815db53bdf9452a1)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/opencode">
        开源编码工具，支持多种编程语言
      </Card>

      <Card title="Kilo Code" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/feather.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=fe0922491e9f5f9c18209a21791882bc)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/kilo">
        高效编码工具，专注性能优化
      </Card>

      <Card title="Cursor" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/box.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=e306f71ed712216941329f8a99ee858a)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/cursor">
        AI 原生 IDE，智能代码编辑器
      </Card>

      <Card title="其他工具" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/puzzle-piece.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=54b1866aa0f6e170bb6a4f9d2977c138)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>} href="/cn/coding-plan/tool/others">
        其它 Coding 工具支持持续扩展中
      </Card>
    </CardGroup>
  </Step>

  <Step title="接入端点说明">
    GLM Coding Plan 支持 Anthropic 协议和 OpenAI 协议两种接入方式，接入时请注意配置正确的 `Base URL`:

    | 协议类型                      | Base URL                                      |
    | ------------------------- | --------------------------------------------- |
    | Anthropic Message 协议      | `https://open.bigmodel.cn/api/anthropic`      |
    | OpenAI Chat Completion 协议 | `https://open.bigmodel.cn/api/coding/paas/v4` |
    | OpenAI Response 协议        | `https://open.bigmodel.cn/api/v1`             |
  </Step>

  <Step title="开始编码">
    配置完成后，您就可以开始使用 GLM 模型进行编码了！

    <Tabs>
      <Tab title="对话编程">
        ```
        # 在 Claude Code 中输入自然语言指令
        请帮我创建一个 React 组件，包含用户登录表单
        ```
      </Tab>

      <Tab title="代码调试">
        ```
        # 描述遇到的问题
        我的 API 请求返回 404 错误，请帮我检查代码
        ```
      </Tab>

      <Tab title="代码优化">
        ```
        # 请求代码优化
        这个函数性能不好，请帮我优化一下
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

## 高级功能

<AccordionGroup>
  <Accordion title="视觉理解 MCP Server">
    套餐用户可以使用视觉理解 MCP Server，可以通过旗舰视觉推理模型 GLM-4.6V 来理解和分析图像内容。

    * 分析 UI 设计图并生成对应代码
    * 理解流程图和架构图
    * 从截图中提取文本和信息

    详细使用方法请参考 [视觉理解 MCP Server](/cn/coding-plan/mcp/vision-mcp-server) 文档。
  </Accordion>

  <Accordion title="网络搜索 MCP Server">
    套餐用户可以使用网络搜索 MCP Server，获取最新的技术信息。

    * 搜索最新的技术文档和 API 变更
    * 获取开源项目的最新信息
    * 查找解决方案和最佳实践

    详细使用方法请参考 [网络搜索 MCP Server](/cn/coding-plan/mcp/search-mcp-server) 文档。
  </Accordion>

  <Accordion title="网页读取 MCP Server">
    套餐用户可以使用网页读取 MCP Server，获取并解析网页内容。

    * 抓取任意网页的完整文本与链接
    * 提取标题、正文、元数据等结构化信息
    * 解析页面内链接列表，辅助知识提取

    详细使用方法请参考 [网页读取 MCP Server](/cn/coding-plan/mcp/reader-mcp-server) 文档。
  </Accordion>

  <Accordion title="开源仓库 MCP Server">
    套餐用户可以使用开源仓库 MCP Server，访问开源仓库文档、目录结构和文件内容。

    * GitHub 代码仓库检索文档、代码与注释
    * 获取 GitHub 仓库的目录结构和文件列表，快速掌握项目布局
    * 读取 GitHub 仓库中指定文件的完整代码内容，深入分析实现细节

    详细使用方法请参考 [开源仓库 MCP Server](/cn/coding-plan/mcp/zread-mcp-server) 文档。
  </Accordion>
</AccordionGroup>

## 其他相关

* 查看我们的 [最佳实践](/cn/coding-plan/learning-resources/best-practice)，了解如何使用 GLM Coding Plan 高效完成复杂项目开发。
* 如果您在使用过程中遇到任何问题，可以查阅开发者文档或联系我们的 [技术支持](https://bigmodel.cn/online-book/customerService)。
