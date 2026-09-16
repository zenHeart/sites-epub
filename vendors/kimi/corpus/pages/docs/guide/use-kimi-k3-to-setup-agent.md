> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 用 Kimi K3 搭建 Agent

> 以行业信息整理为例，组合 Kimi K3、官方联网搜索和自定义工具，构建可运行的 Agent。

Kimi K3 具备面向复杂任务的推理、编码和工具调用能力。本指南以“行业信息整理 Agent”为例，演示如何组合官方联网搜索工具与一个自定义工具，构建可运行、可控的 Agent。

## 任务拆解

先把行业研究任务拆成三个阶段，再决定工具和提示词：

1. **检索**：确定研究范围，搜索最新数据、企业信息和新闻；
2. **分析**：比较来源、识别冲突，区分事实、估算和推断；
3. **输出**：生成包含摘要、关键发现、风险和来源的结构化报告。

这种拆解让模型负责规划和判断，让工具负责检索或执行确定性逻辑。不要把工具能够完成的工作重复写进冗长的 system prompt。

## 工具设计

本示例组合两类工具：

* 官方 `web-search`：检索实时行业资料。平台还提供 `fetch`、`code-runner`、`excel` 等工具，完整列表和 Formula 调用方式见[官方工具](/docs/guide/use-official-tools)；
* 自定义 `build_research_plan`：根据主题、地区和年份生成确定性的研究范围，展示如何声明并在本地执行函数工具。

自定义工具使用 JSON Schema 描述参数。将 `additionalProperties` 设为 `false`，并在 `required` 中列出必填字段，可以减少模型生成无效参数的概率。

当工具增加到几十个甚至更多时，不要把所有 schema 都放进每次请求。请参考 [Kimi K3 工具调用最佳实践](/docs/guide/kimi-k3-tool-calling-best-practice)和[动态加载工具](/docs/guide/use-dynamic-tool-loading)，先检索候选工具，再按需加载。

## Prompt 设计

System prompt 只描述角色、工作流程和质量边界，把具体工具参数留给工具 schema：

```python theme={null}
SYSTEM_PROMPT = """你是行业研究助手。请先明确研究范围，再检索并交叉验证信息，最后输出简洁报告。
要求：
- 区分已确认事实、估算和推断；关键结论尽量由多个来源支持。
- 不得编造数据或来源；资料不足时说明搜索范围和缺口。
- 报告包含执行摘要、关键发现、风险与限制、来源列表。
- 使用与用户相同的语言回答。
"""
```

业务格式、合规要求或受众发生变化时，再增量补充约束。更多建议见 [Prompt 最佳实践](/docs/guide/prompt-best-practice)。

## K3 API 配置

请使用 Python 3.9 或更高版本，并安装 OpenAI Python SDK 和用于调用官方 Formula 工具的 HTTP 客户端：

```bash theme={null}
python3 -m pip install --upgrade openai httpx
export MOONSHOT_API_KEY="YOUR_API_KEY"
```

CN 站点使用 `https://api.moonshot.cn/v1`，模型为 `kimi-k3`。API Key 仅从 `MOONSHOT_API_KEY` 环境变量读取。

Kimi K3 始终进行推理，推理强度通过请求顶层 `reasoning_effort` 配置，支持 `"low"` / `"high"` / `"max"`（默认 `"max"`）。工具循环必须把 SDK 返回的完整 assistant message 追加到 `messages`，不能只复制 `content` 和 `tool_calls`，否则会丢失可能返回的 `reasoning_content`，破坏后续工具调用上下文。参数和不同模型的差异请以[思考模式](/docs/guide/use-thinking-models)、[推理强度](/docs/guide/use-reasoning-effort)和[模型参数参考](/docs/api/models-overview)为准。

## 完整 Agent Loop

将下面代码保存为 `agent.py`。示例动态读取 `web-search` 的工具声明，在本地执行自定义工具，并用最多 8 轮的循环处理工具调用。

```python theme={null}
import asyncio
import json
import os

import httpx
from openai import AsyncOpenAI

BASE_URL = "https://api.moonshot.cn/v1"
MODEL = "kimi-k3"
MAX_TOOL_ROUNDS = 8
SYSTEM_PROMPT = """你是行业研究助手。请先明确研究范围，再检索并交叉验证信息，最后输出简洁报告。
要求：
- 区分已确认事实、估算和推断；关键结论尽量由多个来源支持。
- 不得编造数据或来源；资料不足时说明搜索范围和缺口。
- 报告包含执行摘要、关键发现、风险与限制、来源列表。
- 使用与用户相同的语言回答。
"""

RESEARCH_PLAN_TOOL = {
    "type": "function",
    "function": {
        "name": "build_research_plan",
        "description": "根据行业主题、地区和时间范围生成研究计划",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "要研究的行业或主题",
                },
                "region": {
                    "type": "string",
                    "enum": ["中国", "全球", "美国", "欧洲"],
                    "description": "研究地区",
                },
                "start_year": {
                    "type": "integer",
                    "description": "研究起始年份",
                },
                "end_year": {
                    "type": "integer",
                    "description": "研究结束年份",
                },
            },
            "required": ["topic", "region", "start_year", "end_year"],
            "additionalProperties": False,
        },
    },
}


def build_research_plan(
    topic: str, region: str, start_year: int, end_year: int
) -> str:
    """生成一个确定性的研究范围，作为自定义工具示例。"""
    if start_year > end_year:
        return json.dumps(
            {"error": "start_year 不能大于 end_year"}, ensure_ascii=False
        )

    plan = {
        "topic": topic,
        "region": region,
        "period": f"{start_year}-{end_year}",
        "dimensions": ["市场规模与增速", "产业链与主要企业", "技术趋势", "政策与风险"],
        "search_queries": [
            f"{region} {topic} 市场规模 {start_year} {end_year}",
            f"{region} {topic} 主要企业 技术趋势",
            f"{region} {topic} 政策 风险",
        ],
    }
    return json.dumps(plan, ensure_ascii=False)


class IndustryResearchAgent:
    def __init__(self) -> None:
        api_key = os.environ["MOONSHOT_API_KEY"]
        self.openai = AsyncOpenAI(api_key=api_key, base_url=BASE_URL)
        self.http = httpx.AsyncClient(
            base_url=BASE_URL,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=60.0,
        )

    async def load_formula(
        self, formula_uri: str
    ) -> tuple[list[dict], dict[str, str]]:
        response = await self.http.get(f"/formulas/{formula_uri}/tools")
        response.raise_for_status()
        tools = response.json().get("tools", [])
        if not tools:
            raise RuntimeError(f"Formula {formula_uri} 未返回任何工具")

        tool_to_formula = {
            tool["function"]["name"]: formula_uri
            for tool in tools
            if tool.get("type") == "function" and tool.get("function")
        }
        if not tool_to_formula:
            raise RuntimeError(f"Formula {formula_uri} 未返回可调用的函数工具")
        return tools, tool_to_formula

    async def call_formula(
        self, formula_uri: str, name: str, arguments: dict
    ) -> str:
        response = await self.http.post(
            f"/formulas/{formula_uri}/fibers",
            json={"name": name, "arguments": json.dumps(arguments)},
        )
        response.raise_for_status()
        fiber = response.json()
        context = fiber.get("context", {})

        if fiber.get("status") == "succeeded":
            result = context.get("output") or context.get("encrypted_output") or ""
        else:
            result = fiber.get("error") or context.get("error") or "未知工具错误"

        if isinstance(result, str):
            return result
        return json.dumps(result, ensure_ascii=False)

    async def run(self, question: str) -> str:
        official_tools, tool_to_formula = await self.load_formula(
            "moonshot/web-search:latest"
        )
        tools = [RESEARCH_PLAN_TOOL, *official_tools]
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ]

        for _ in range(MAX_TOOL_ROUNDS):
            response = await self.openai.chat.completions.create(
                model=MODEL,
                messages=messages,
                tools=tools,
                max_completion_tokens=8192,
            )
            choice = response.choices[0]
            message = choice.message

            # 追加完整 SDK message，保留 reasoning_content 和 tool_calls。
            messages.append(message)

            if choice.finish_reason == "length":
                raise RuntimeError(
                    "模型输出被 max_completion_tokens 截断，请提高该参数或缩短工具结果"
                )

            if not message.tool_calls:
                if choice.finish_reason != "stop":
                    raise RuntimeError(f"未预期的结束原因: {choice.finish_reason}")
                if not message.content:
                    raise RuntimeError("模型未返回最终报告")
                return message.content

            for tool_call in message.tool_calls:
                name = tool_call.function.name
                try:
                    arguments = json.loads(tool_call.function.arguments or "{}")
                    if not isinstance(arguments, dict):
                        raise ValueError("工具参数必须是 JSON 对象")

                    if name == "build_research_plan":
                        result = build_research_plan(**arguments)
                    elif name in tool_to_formula:
                        result = await self.call_formula(
                            tool_to_formula[name], name, arguments
                        )
                    else:
                        raise ValueError(f"未知工具: {name}")
                except Exception as exc:
                    result = json.dumps(
                        {"error": f"{type(exc).__name__}: {exc}"},
                        ensure_ascii=False,
                    )

                # 即使单个工具失败，也返回对应结果并继续处理本轮其他调用。
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result,
                    }
                )

        raise RuntimeError(f"工具调用超过最大轮数 {MAX_TOOL_ROUNDS}")

    async def close(self) -> None:
        try:
            await self.openai.close()
        finally:
            await self.http.aclose()


async def main() -> None:
    agent = IndustryResearchAgent()
    try:
        report = await agent.run("调研 2024-2026 年中国人形机器人行业的发展情况")
        print(report)
    finally:
        await agent.close()


if __name__ == "__main__":
    asyncio.run(main())
```

循环中的两个上下文细节缺一不可：

1. `messages.append(message)` 追加完整 assistant message，以保留 K3 返回的 `reasoning_content`；
2. 每条 tool message 使用对应的 `tool_call_id`，让模型知道结果属于哪个调用。

示例遇到 `finish_reason="length"` 时会立即报错，避免把截断内容当作最终报告。单个工具调用失败时，错误会作为对应的 tool result 返回给模型，并继续处理本轮其他调用。

`MAX_TOOL_ROUNDS` 防止工具不断调用造成无限循环，也避免递归实现带来的调用栈增长。

## 运行与排错

运行示例：

```bash theme={null}
python3 agent.py
```

可以把 `main()` 中的问题替换为目标行业、地区和年份。最终输出应包含摘要、关键发现、风险与来源，而不是大段工具原始结果。

常见问题：

* **`finish_reason` 为 `length`**：示例会抛出 `RuntimeError`；结合[模型参数参考](/docs/api/models-overview)提高 `max_completion_tokens`，或缩短工具结果；
* **达到最大工具轮数**：检查工具描述是否重叠、工具结果是否明确，并收紧任务范围；
* **工具持续返回参数错误**：检查函数 schema、`required`、`enum` 与 `additionalProperties`，不要用 prompt 代替参数约束；
* **第二轮工具调用失败**：确认追加的是完整 SDK assistant message，且每条工具结果保留了正确的 `tool_call_id`；
* **官方工具请求失败**：确认 endpoint、API Key、Formula URI 和工具可用性，详细调用方式见[官方工具](/docs/guide/use-official-tools)。

## 自定义工具与优化

示例中的 `build_research_plan` 已完整展示“声明 schema → 本地分派 → 返回 JSON → 关联 `tool_call_id`”的流程。接入数据库、内部搜索或文件生成服务时，只需用真实实现替换该函数，并保持 schema 与返回结构一致。

进一步优化时：

* 只提供当前任务需要的工具，避免相似工具争抢；
* 对工具输入做业务校验，对错误返回结构化信息，让模型能够修正参数；
* 大型工具目录使用[动态加载工具](/docs/guide/use-dynamic-tool-loading)；
* 使用 `tool_choice`、推理强度等能力前，先核对 [Kimi K3 工具调用最佳实践](/docs/guide/kimi-k3-tool-calling-best-practice)和[模型参数参考](/docs/api/models-overview)。
