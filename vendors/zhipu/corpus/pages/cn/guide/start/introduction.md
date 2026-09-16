> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 平台介绍

> 智谱 · 一站式大模型开发平台

智谱大模型开放平台 [bigmodel.cn](http://bigmodel.cn)，提供功能丰富、灵活易用、高性价比的大模型 API 服务，支持模型精调、推理、评测等，致力于构建高效通用的“一站式模型即服务” AI 开发新范式。

## 平台能力

<CardGroup cols={3}>
  <Card title="模型调用" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book-open.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=6b5cd60a0c16c81255cbee52c2caf401)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    通过 API 调用文本、视觉、图像、视频、音频等模型，接入业务系统或开发工具。
  </Card>

  <Card title="模型部署" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/flask.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=0a7cbe49e29f718244f4ec7caf677b68)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    在专属资源上部署模型实例，完成模型推理、实例管理与调用配置。
  </Card>

  <Card title="模型微调" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/list.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=145d86f1639b1f1ac6744c2f4c8a871b)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    使用自有数据创建微调任务，训练并部署适配特定场景的模型。
  </Card>

  <Card title="模型评测" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/helmet-safety.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=6e68280ea52d21888fe2337a33e4bf95)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    基于数据集和指标评估模型效果，对比准确性、效率与稳定性。
  </Card>

  <Card title="联网搜索" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/book-open.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=6b5cd60a0c16c81255cbee52c2caf401)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    接入网页检索、问答增强或搜索智能体，为应用补充实时信息来源。
  </Card>

  <Card title="知识库检索" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/box.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=e306f71ed712216941329f8a99ee858a)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    上传文档、网页或结构化数据，构建可用于问答和检索增强的知识库。
  </Card>
</CardGroup>

## 查看模型

平台已上架数十个模型，覆盖文本生成、语言推理、图像理解、视频生成、音视频处理等多场景。前往 [模型概览](/cn/guide/start/model-overview)，即可查看所有模型的功能定位、模型价格、上下文长度等基本信息。

您可前往智谱大模型 [体验中心](https://bigmodel.cn/trialcenter/modeltrial)，极速体验模型能力。

## 快速开始

[快速开始](/cn/guide/start/quick-start) 将引导您逐步完成 API 调用流程，涵盖注册账号、环境配置、获取 API Key、SDK 使用等关键步骤。帮助您分钟级完成模型调用服务，并集成到您的业务或应用中。

## 开发指南

平台提供多种开发方式，满足不同开发者的需求和技术栈偏好。无论您是初学者还是经验丰富的开发者，都能找到适合的集成方案。

<CardGroup cols={2}>
  <Card title="HTTP API 调用" href="/cn/guide/develop/http/introduction">
    标准 RESTful API 接口，支持多种编程语言和平台
  </Card>

  <Card title="官方 Python SDK" href="/cn/guide/develop/python/introduction">
    功能完整的 Python 开发工具包，支持异步调用和类型安全
  </Card>

  <Card title="官方 Java SDK" href="/cn/guide/develop/java/introduction">
    企业级 Java 开发工具包，支持高并发和高可用性
  </Card>

  <Card title="OpenAI SDK 兼容" href="/cn/guide/develop/openai/introduction">
    兼容 OpenAI SDK，快速迁移现有应用
  </Card>

  <Card title="LangChain 集成" href="/cn/guide/develop/langchain/introduction">
    集成 LangChain 框架，构建复杂的 AI 应用和智能代理
  </Card>
</CardGroup>

## 核心概念

<Tabs>
  <Tab title="GLM">
    <Card title="GLM - General Language Model" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/brain.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=b04e181006c02a51715f85395cd9735f)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
      GLM 系列模型基于先进的预训练技术，具备优秀的语言理解、文本生成和复杂推理能力。模型支持自然语言指令、多轮对话、代码生成及 Agent 应用，并通过标准 API 接口为开发者提供灵活、高效的大模型服务。
    </Card>
  </Tab>

  <Tab title="Token">
    <Card title="Token - 文本处理单位" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/coins.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=d140ba7189994790a79f83f5a763f59a)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
      Token 是模型用来表示自然语言文本的基本单位，可以直观的理解为“字”或“词”；通常 1 个中文词语、1 个英文单词、1 个数字或 1 个符号计为 1 个 token。

      GLM 系列模型中 token 和字数的换算比例约为 1:1.6 ，但因为不同模型的分词不同，所以换算比例也存在差异，每一次实际处理 token 数量以模型返回为准，您可以从返回结果的 usage 中查看。
    </Card>
  </Tab>

  <Tab title="上下文窗口">
    <Card title="Context Window - 上下文窗口" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/AteIdKqxoD35bkVX/resource/icon/window.svg?fit=max&auto=format&n=AteIdKqxoD35bkVX&q=85&s=ce809df2afccb242815db53bdf9452a1)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
      上下文窗口是指模型在一次对话中能够处理的最大长度。包括：

      * 用户输入的内容
      * 模型生成的回复
      * 模型在生成回复过程中进行推理或调用工具时产生的中间内容

      <Danger>
        **如果超出上下文窗口限制，会发生什么？**

        请求可能无法正常处理，并返回上下文长度超限相关的错误。

        模型的回答质量和上下文连贯性可能会受到影响。
      </Danger>

      查看模型的上下文限制，或者使用 Tokenizer 工具估算上下文长度。
    </Card>
  </Tab>
</Tabs>
