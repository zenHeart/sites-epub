> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 用对话指挥机械臂：让机器人听懂你说的话

> <Note> 本教程将带您使用 MiniMax 语言模型 & MCP 视觉理解，构建一个能够理解自然语言指令并执行复杂机械臂操作任务的智能机器人。 </Note>

<div style={{display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px'}}>
  <div style={{width: '40px', height: '40px', borderRadius: '50%', background: 'linear-gradient(135deg, #3b82f6, #8b5cf6)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'white', fontWeight: 'bold'}}>D</div>

  <div>
    <div style={{fontWeight: 500}}>Devin</div>
    <div style={{fontSize: '0.875rem', color: '#9ca3af'}}>2026年1月26日</div>
  </div>
</div>

<a href="https://github.com/MiniMax-OpenPlatform/MiniMax-Agent-VLA-Demo" target="_blank" style={{display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '8px 16px', borderRadius: '8px', border: '1px solid #e5e7eb', textDecoration: 'none', color: 'inherit', marginBottom: '32px'}}>
  <svg height="20" width="20" viewBox="0 0 16 16" fill="currentColor">
    <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z" />
  </svg>

  Download from GitHub
</a>

# 项目简介

**机器人 Agent** 基于 **MiniMax M2.1** 语言模型和 **Pi05 VLA**（Vision-Language-Action）模型，在 LIBERO 仿真环境中实现自然语言驱动的机械臂操作。

<img src="https://filecdn.minimax.chat/public/8eaae90f-5762-424a-9b32-732a58678d77.webp" alt="Demo" style={{borderRadius: '8px', marginBottom: '16px', maxWidth: '100%'}} />

<AccordionGroup>
  <Accordion title=" MiniMax M2.1 任务规划">
    理解用户的自然语言指令，将复杂任务分解为可执行的操作步骤，并协调多步骤任务的执行流程。
  </Accordion>

  <Accordion title=" MiniMax MCP 视觉理解">
    通过 MCP 调用视觉理解能力，分析场景图像，验证任务执行结果，实现闭环反馈控制。
  </Accordion>

  <Accordion title=" Pi05 VLA 动作执行">
    基于 PaliGemma 的视觉-语言-动作模型，根据场景图像和任务指令，生成精确的机械臂控制动作。
  </Accordion>

  <Accordion title=" LIBERO 仿真环境">
    在 MuJoCo 物理引擎驱动的仿真环境中，执行多种机器人操作任务。
  </Accordion>
</AccordionGroup>

***

## 系统架构

```
用户指令 → MiniMax LLM (任务规划) → Pi05 VLA (动作执行) → LIBERO仿真
               ↑                                              ↓
         MCP视觉理解 ← ─────────── 场景图像 ←──────────────────┘
```

| 模块   | 技术方案            | 说明          |
| ---- | --------------- | ----------- |
| 任务规划 | MiniMax M2.1    | 理解用户意图，分解任务 |
| 视觉理解 | MiniMax MCP     | 场景分析，结果验证   |
| 动作执行 | Pi05 VLA        | 视觉-语言-动作模型  |
| 仿真环境 | LIBERO / MuJoCo | 机器人操作仿真     |

***

## 快速上手

<Steps>
  <Step title="克隆仓库">
    ```bash theme={null}
    git clone https://github.com/MiniMax-OpenPlatform/MiniMax-Agent-VLA-Demo.git
    cd MiniMax-Agent-VLA-Demo
    ```
  </Step>

  <Step title="配置 API Keys">
    ```bash theme={null}
    # MiniMax API Key (用于LLM和MCP视觉理解)
    # 获取: https://platform.minimaxi.com/
    export ANTHROPIC_API_KEY="your-minimax-api-key"

    # HuggingFace Token (用于下载Pi05模型)
    # 获取: https://huggingface.co/settings/tokens
    export HF_TOKEN="your-huggingface-token"
    ```
  </Step>

  <Step title="下载 Pi05 模型">
    ```bash theme={null}
    # 安装 huggingface_hub
    pip install huggingface_hub

    # 登录 HuggingFace
    huggingface-cli login

    # 下载 Pi05 LIBERO 微调模型
    python -c "
    from huggingface_hub import snapshot_download
    snapshot_download(
        repo_id='lerobot/pi05_libero',
        local_dir='./models/pi05_libero_finetuned'
    )
    "
    ```

    <Tip>
      模型默认路径：`./models/pi05_libero_finetuned`，如需修改请编辑 `agent_mode.py` 中的 `MODEL_PATH` 变量。
    </Tip>
  </Step>

  <Step title="安装依赖">
    ```bash theme={null}
    # 创建虚拟环境
    python -m venv .venv
    source .venv/bin/activate

    # 一键安装所有依赖
    pip install -r requirements.txt
    ```

    **依赖项说明：**

    | 依赖      | 说明                         |
    | ------- | -------------------------- |
    | LeRobot | HuggingFace 机器人学习库（已包含）    |
    | MuJoCo  | DeepMind 物理仿真引擎            |
    | LIBERO  | 机器人操作仿真基准环境                |
    | MCP     | Model Context Protocol 客户端 |
  </Step>

  <Step title="运行 Agent">
    ```bash theme={null}
    # 设置显示 (VNC环境)
    export DISPLAY=:2

    # 运行Agent
    python agent_mode.py
    ```

    启动后选择任务场景：

    * `libero_object` - 不同物体泛化
    * `libero_spatial` - 空间关系理解
    * `libero_goal` - 不同动作目标（推荐）
  </Step>
</Steps>

***

## 支持的任务

在 LIBERO Goal 场景中，Agent 支持以下 10 个操作任务：

| #  | 任务指令                                          | 描述          |
| -- | --------------------------------------------- | ----------- |
| 1  | `open the middle drawer of the cabinet`       | 打开橱柜中间抽屉    |
| 2  | `put the bowl on the stove`                   | 把碗放在炉子上     |
| 3  | `put the wine bottle on top of the cabinet`   | 把红酒瓶放在橱柜上   |
| 4  | `open the top drawer and put the bowl inside` | 打开顶部抽屉把碗放进去 |
| 5  | `put the bowl on top of the cabinet`          | 把碗放在橱柜上     |
| 6  | `push the plate to the front of the stove`    | 把盘子推到炉子前面   |
| 7  | `put the cream cheese in the bowl`            | 把奶油奶酪放进碗里   |
| 8  | `turn on the stove`                           | 打开炉子        |
| 9  | `put the bowl on the plate`                   | 把碗放在盘子上     |
| 10 | `put the wine bottle on the rack`             | 把红酒瓶放在架子上   |

***

## 核心代码解析

### Agent 工具定义

Agent 通过两个核心工具与环境交互：

```python theme={null}
AGENT_TOOLS = [
    {
        "name": "execute_task",
        "description": "Execute a manipulation task using the robot arm.",
        "input_schema": {
            "type": "object",
            "properties": {
                "task": {
                    "type": "string",
                    "description": "A manipulation task instruction"
                }
            },
            "required": ["task"]
        }
    },
    {
        "name": "get_scene_info",
        "description": "Capture camera image and use VLM to analyze the current scene.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]
```

### MiniMax M2.1 任务规划

使用 Anthropic 兼容接口调用 MiniMax M2.1：

```python theme={null}
from anthropic import Anthropic

client = Anthropic(
    base_url="https://api.minimax.cn/anthropic",
    api_key=api_key,
    default_headers={"Authorization": f"Bearer {api_key}"}
)

response = client.messages.create(
    model="MiniMax-M2.1",
    max_tokens=4096,
    system=system_prompt,
    messages=conversation_history,
    tools=AGENT_TOOLS
)
```

### MCP 视觉理解

通过 MCP 调用 MiniMax 视觉理解能力验证任务结果：

```python theme={null}
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="uvx",
    args=["minimax-coding-plan-mcp", "-y"],
    env={
        "MINIMAX_API_KEY": api_key,
        "MINIMAX_API_HOST": "https://api.minimax.cn"
    }
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        result = await session.call_tool("understand_image", {
            "image_source": image_path,
            "prompt": "Verify if the task was completed successfully."
        })
```

***

## 技术细节

### Pi05 模型参数

| 参数   | 值                        |
| ---- | ------------------------ |
| 基础模型 | PaliGemma                |
| 输入   | 2个相机图像 + 机械臂状态 + 语言指令    |
| 输出   | 7维动作（末端位置增量 + 姿态增量 + 夹爪） |
| 控制频率 | 10Hz                     |
| 最大步数 | 280步/任务                  |

### Agent 工作流程

1. **用户输入**：接收自然语言指令（中文或英文）
2. **任务规划**：MiniMax M2.1 理解意图，映射到支持的任务
3. **动作执行**：Pi05 VLA 生成机械臂控制序列
4. **结果验证**：MCP 视觉理解分析场景，确认任务完成
5. **反馈循环**：如验证失败，自动重试任务

***

## 常见问题

<AccordionGroup>
  <Accordion title="API 调用报错 'Invalid API Key'">
    检查 `ANTHROPIC_API_KEY` 是否正确设置为 MiniMax 的 API Key。
  </Accordion>

  <Accordion title="模型加载失败">
    1. 检查 `HF_TOKEN` 是否配置
    2. 检查 `MODEL_PATH` 路径是否正确
  </Accordion>

  <Accordion title="MCP 视觉理解报错">
    确保已安装：`pip install mcp` 并且 `uvx` 命令可用。
  </Accordion>

  <Accordion title="可视化窗口不显示">
    设置 `export DISPLAY=:2`（VNC）或确保有 X11 环境。
  </Accordion>
</AccordionGroup>

***

## 应用拓展

基于当前架构，开发者可以考虑以下拓展方向：

* **多任务串联**：实现复杂任务的自动分解和顺序执行
* **失败恢复**：增强 Agent 的错误检测和自动恢复能力
* **实物部署**：将仿真中的策略迁移到真实机械臂
* **多模态交互**：结合语音识别实现语音控制机器人

***

## 总结

在本教程中，我们展示了如何使用 **MiniMax M2.1** 和 **MCP 视觉理解**构建一个智能机器人 Agent：

* **MiniMax M2.1** 负责理解用户意图，将自然语言指令转化为具体的操作任务
* **MiniMax MCP** 提供视觉理解能力，验证任务执行结果，实现闭环控制
* **Pi05 VLA** 作为底层执行器，根据视觉输入生成精确的机械臂动作
* **LIBERO/MuJoCo** 提供逼真的物理仿真环境

这套 LLM + VLM + VLA 的协同架构，展示了大模型在机器人控制领域的应用潜力。

***

## 相关资源

<Columns cols={3}>
  <Card title="Anthropic API" icon="book-open" href="/docs/api-reference/text-anthropic-api">
    MiniMax M2.1 接入指南
  </Card>

  <Card title="MCP 指南" icon="plug" href="/docs/token-plan/mcp-guide">
    MCP 工具配置说明
  </Card>

  <Card title="LeRobot" icon="github" href="https://github.com/huggingface/lerobot">
    HuggingFace 机器人学习库
  </Card>
</Columns>
