> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

本教程以一个旅游助手为例，介绍如何使用 Node.js 集成扣子罗盘 SDK 实现对旅游助手的全链路追踪，从用户输入到模型响应的全过程。  在本教程中，你需要先在扣子罗盘控制台中编写 Prompt，并通过扣子罗盘 SDK 拉取 Prompt 并调用模型，然后就能在控制台中查看 SDK 上报的 Trace 数据。
# 步骤一：编写 Prompt  {#f0425135}
 为了方便演示，本教程以 CozeLoop Demo 空间中的[旅行专家](https://loop.coze.cn/console/enterprise/personal/space/7487806534651887643/pe/prompts/7490479658761207820)为例。
以下是旅行助手的 Prompt 示例。你也可以根据实际需求，开发一个 Prompt 并提交新版本，详情请参考[开发提示词](/cozeloop/create-prompt)。
![Image=606x280](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/02e8db26d2274cf5aa046f1075d9cfd8~tplv-goo7wpa0wc-image.image)
# 步骤二：上报数据 {#ee1191c3}
以下代码展示了如何使用扣子罗盘实现完整的链路追踪，从用户输入到模型响应的全过程。

1. 追踪初始化：
   * 初始化扣子罗盘全局追踪器
   * 配置追踪处理器为"simple"模式
2. 模型调用（callLLM）：
   * 配置 OpenAI 客户端连接
   * 使用 traceable 包装器创建 Model 类型的追踪节点
   * 发送请求到大模型并记录输入输出
3. 旅行规划流程（runTravelPlan）：
   * 初始化可追踪的 PromptHub
   * 获取旅行规划相关的 Prompt 模板
   * 用用户提供的参数(出发地、目的地等)替换模板变量
   *  调用模型生成旅行计划
4. 主流程（run）：
   * 创建一个名为"旅行专家"的 Agent 类型追踪节点
   * 记录整个请求的输入参数
   * 执行旅行规划并获取结果
   * 输出生成的旅行计划

```TypeScript
import { type ChatCompletionCreateParams } from 'openai/resources/chat';
import { OpenAI } from 'openai';
import { cozeLoopTracer, PromptHub, SpanKind } from '@cozeloop/ai';

// initialize tracer globally
cozeLoopTracer.initialize({
  apiClient: {
    // baseURL: 'https://api.coze.cn',
    // token: 'your_api_token',
  },
  processor: 'simple',
});

async function callLLM(messages: ChatCompletionCreateParams['messages']) {
  // config your model
  const apiKey = process.env.GPT_OPEN_API_KEY;
  const openai = new OpenAI({
    apiKey,
    baseURL: process.env.GPT_OPEN_API_BASE_URL,
    defaultQuery: { 'api-version': '2024-03-01-preview' },
    defaultHeaders: { 'api-key': apiKey },
  });

  // wrap model as a span node with `cozeLoopTracer.traceable`
  return await cozeLoopTracer.traceable(
    async span => {
      cozeLoopTracer.setInput(span, { messages });

      const resp = await openai.chat.completions.create({
        model: 'gpt-4-0613',
        messages,
      });

      return resp;
    },
    // span name and type
    { name: 'CallLLM', type: SpanKind.Model },
  );
}

interface TravelPlanOptions {
  departure: string;
  destination: string;
  people_num: number;
  days_num: number;
  travel_theme: string;
}

async function runTravelPlan(options: TravelPlanOptions) {
  // initialize traceable PromptHub
  const hub = new PromptHub({
    apiClient: {
      // baseURL: 'https://api.coze.cn',
      // token: 'your_api_token',
    },
    traceable: true,
  });

  // get prompt
  const promptKey = 'CozeLoop_Travel_Master';
  const prompt = await hub.getPrompt(promptKey);

  // format prompt with interpolation variables
  const messages = hub.formatPrompt(prompt, { ...options });

  // invoke model
  return callLLM(messages as ChatCompletionCreateParams['messages']);
}

async function run() {
  const options: TravelPlanOptions = {
    departure: '北京',
    destination: '上海',
    people_num: 2,
    days_num: 5,
    travel_theme: '休闲',
  };

  const result = await cozeLoopTracer.traceable(
    async span => {
      cozeLoopTracer.setInput(span, options);
      const { choices } = await runTravelPlan(options);

      return choices[0].message.content;
    },
    // span name and type
    { name: '旅行专家', type: 'Agent' },
  );

  console.info(result);
  // The trace reporting is asynchronous and has some latency.
  // If **running local files directly**, a short delay is required to ensure successful reporting.
}

run();
```

# 步骤三：查看 Trace 数据 {#8d4317fe}
在完成数据上报后，就可以在扣子罗盘的观测页面查看 SDK 上报的 Trace 数据了。
![Image=540x386](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/789172710cab4eee9a7506ec8d6e6b51~tplv-goo7wpa0wc-image.image)
