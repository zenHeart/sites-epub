> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 基于 PDF 内容进行问答

> 使用 Kimi API 实现基于 PDF 内容的问答，附真实运行输出。

用 Kimi API 做 PDF 问答，流程只有两步：先通过文件接口上传文件并提取文本，再把提取出的文本放入 messages。反复查询同一份文档时，只要文档前缀保持稳定，API 提供的 Context Caching 功能可以帮助节省成本。

本文将一步步演示：

* **上传与读取**：用 file-extract 两步拿到模型可读的文本；
* **提问**：把文件内容作为 system 消息放入 messages；
* **多轮对话**：固定前缀不动，问答记录追加在 messages 末尾；
* **多文件问答**：每个文件一条 system 消息，统一放在 messages 头部；
* **约束输出**：追加一段固定的作答规则，约束格式、篇幅等输出形态；
* **控制成本**：复用稳定的文档前缀，让 Context Caching 自动生效；
* **清理已上传的文件**：提取结果本地留存，定期删除云端文件。

## 1. 准备工作

Kimi API 兼容 OpenAI SDK，直接安装 openai 库即可：

```bash theme={null}
pip install -U openai
```

创建客户端时，把 base\_url 指向 Kimi API 的地址，API Key 从环境变量读取：

```python theme={null}
import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MOONSHOT_API_KEY"],  # 运行前请设置 MOONSHOT_API_KEY 环境变量
    base_url="https://api.moonshot.cn/v1",
)
```

本文示例使用 **kimi-k3** 模型。换用 kimi-k2.6 等其他模型时只需替换 model 字段，但各模型的参数配置存在差异，详见[模型参数参考](https://platform.kimi.com/docs/api/models-overview)。

示例材料是 [Kimi K3 技术报告](https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf)的 PDF，来自 MoonshotAI 官方 GitHub 仓库，通过下方代码下载（你也可以换成任何自己的 PDF，文件接口支持 .pdf、.txt、.csv、.doc、.docx 等格式，单文件不超过 100MB）：

```bash theme={null}
curl -sSL -O https://raw.githubusercontent.com/MoonshotAI/Kimi-K3/main/k3_tech_report.pdf
ls -lh k3_tech_report.pdf
```

<Accordion title="输出示例">
  ```text theme={null}
  -rw-r--r--  1 user  staff   1.7M  8月 16 19:37 k3_tech_report.pdf
  ```
</Accordion>

## 2. 上传文件

通过文件上传接口把 PDF 传到 Kimi 服务器，purpose 设为 file-extract，表示这份文件用于提取文本内容。文件上传接口还支持 image、video 等 purpose 值，用于模型的原生理解：

```python theme={null}
file_object = client.files.create(file=Path("k3_tech_report.pdf"), purpose="file-extract")
print(file_object.id)
```

<Accordion title="输出示例">
  ```text theme={null}
  fc1t3y77tkk111gafm81
  ```
</Accordion>

## 3. 读取提取结果

上传之后，通过文件抽取接口拿回提取后的文本，它已经对齐成官方推荐的、模型易于理解的格式：

```python theme={null}
# 旧示例中的 retrieve_content 已标记 warning，files.content 是其替代
file_content = client.files.content(file_id=file_object.id).text
print(file_content[:200])  # 看看前 200 个字
```

<Accordion title="输出示例">
  ```text theme={null}
  {"content":"# KIMI K3:OPEN FRONTIER INTELLIGENCE\n\n\nTECHNICAL REPORT OF KIMI K3\n\n\nKimi Team\n\n\n# ABSTRACT\n\n\nWe introduce Kimi K3,a 2.8T parameter Mixture-of-Experts model with 104billion act
  ```
</Accordion>

如果这份文档要反复提问，建议把提取结果存到本地，下次问答直接读本地文件复用，不必重新上传和提取：

```python theme={null}
# 保存提取结果到本地
Path("k3_tech_report_extract.txt").write_text(file_content)

# 下次问答：直接读本地文件，不用再上传和提取
file_content = Path("k3_tech_report_extract.txt").read_text()
```

> **两个常见错误**：
>
> 1. **不要把 file\_id 放进 messages。** file\_id 只是文件的句柄，模型看不到任何内容。必须先读取提取结果，再把文本放进 messages。
> 2. **不要用 base64 编码 PDF 内联进 messages。** 使用 base64 编码文件会导致产生巨量的 Tokens 消耗；如果文件类型是 /v1/files 文件接口支持的格式，使用文件接口上传并抽取文件内容即可。

## 4. 提问

把提取出的文件内容作为一条 system 消息放进 messages，然后在 user 消息里提问：

```python theme={null}
persona = "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"

messages = [
    {"role": "system", "content": persona},
    {"role": "system", "content": file_content},  # 提取后的文件内容（注意是内容，而不是文件 ID）
    {"role": "user", "content": "这份技术报告介绍了 K3 的哪些能力？请分点概括。"},
]

completion = client.chat.completions.create(
    model="kimi-k3",
    messages=messages,
)
print(completion.choices[0].message.content)
```

<Accordion title="输出示例">
  ```text theme={null}
  # Kimi K3 技术报告能力概览

  ## 一、基础模型能力（架构层面）

  - **规模与稀疏性**：2.8T 总参数的混合专家模型（MoE），每 token 激活 104B 参数；896 个路由专家中激活 16 个，稀疏度达 56
  - **超长上下文**：支持最高 **100 万 token** 的上下文窗口，通过 KDA（Kimi Delta Attention）+ Gated MLA 混合注意力（3:1 比例）实现高效长序列建模
  - **原生多模态**：文本、图像、视频由同一主干网络在同一上下文中处理，无需事后模态对齐；支持写代码→看渲染截图→迭代优化的"视觉闭环"工作流
  - **深度信息流**：Attention Residuals（AttnRes）让每层可选择性访问此前所有层的表示
  - **多档推理强度**：支持 low / high / max 等多级推理努力程度（reasoning effort），在 token 效率与性能间灵活权衡
  - 整体缩放效率较 Kimi K2 提升约 **2.5 倍**

  ## 二、评测表现突出的任务能力

  **编程（Coding）**
  - ProgramBench 第一（77.8%）；SWE-Marathon（GPU 内核方向）领先第二名 7 分；Terminal-Bench 2.1（88.3%）接近最强闭源模型；FrontierSWE 长程任务排名第二（81.2%）

  **智能体（Agentic）**
  - 多项第一：BrowseComp（91.2%）、DeepSearchQA（95.0% F1）、ResearchRubrics、MCPMark-Verified（94.5%）、AutomationBench、SpreadsheetBench 2、τ³-Banking、Harvey Lab-AA
  - 支持跨数百至数千次工具调用、累计数百万 token 的长程任务执行

  **推理与知识**
  - GPQA Diamond 达 93.5%，与前沿持平；研究级任务（HLE-Full、CritPt）仍落后于最强闭源模型

  **视觉**
  - OmniDocBench 第一（91.1%）；Math-Vision 94.3%（配合 Python 工具升至 97.8%）；ZeroBench 与 Claude Fable 5 并列第一

  ## 三、案例研究中展示的实际能力

  - **GPU 内核优化**：在 24 小时预算内自主完成 profiling、重写与基准测试，将 AttnRes 延迟从 283.6ms 降至 114.4ms，KDA 运行时间减少 73.6%
  - **GPU 编译器开发**：从零构建 MiniTriton——含 DSL 前端、MLIR 优化层、PTX 代码生成、自动微分与分布式训练原语
  - **芯片设计**：48 小时内自主完成一款推理芯片原型（nano-KPU）的设计、优化与验证
  - **科研编程**：约 2 小时复现天体物理 I–Love–Q 普遍关系（人工通常需 1–2 周）
  - **知识工作**：生成 AI ASIC 行业 42 年交互式研究网站；用 20+ 并发子智能体分析 391 个引力波事件
  - **视频剪辑与动效设计**：制作 3Blue1Brown 风格的架构讲解动画与预告片
  - **网络安全**：发现真实漏洞（含 Linux 内核中两个此前未知漏洞），并能完成用户态端到端漏洞利用开发，但与人类专家仍有明显差距

  ## 四、其他特点

  - **成本效率**：在编程与智能体套件上以 Claude Fable 5 约 1/3 至 1/10 的成本达到接近顶级的分数
  - **开放权重**：作为首个开放的 3T 级模型发布完整权重
  - 总体定位：整体仍落后于最强的闭源模型（Claude Fable 5、GPT-5.6 Sol），但在评测套件中稳定优于其他所有参评的开源与闭源模型
  ```
</Accordion>

> 注：本文所有输出均为真实运行示例，模型输出有随机性，你的实际结果可能略有差异。

## 5. 多轮对话

追问只需要把问答记录追加在 messages 末尾，文件内容和指令保持在最前面不动。这个"固定内容在前、对话追加在后"的结构不只是写法习惯，它决定了后文的缓存能否命中：

```python theme={null}
# 在第 4 节 messages 的基础上继续追加：前缀不动，问答记录追加在末尾
messages.append({"role": "assistant", "content": completion.choices[0].message.content})
messages.append({"role": "user", "content": "其中对开发者最有用的是哪一点？"})

completion = client.chat.completions.create(
    model="kimi-k3",
    messages=messages,
)
print(completion.choices[0].message.content)
```

<Accordion title="输出示例">
  ```text theme={null}
  如果只选一点，我会选：**完整开放权重**。它是其他一切能力对开发者生效的前提——可以自己部署、微调、量化、二次开发，不受 API 限流、定价和供应商策略的约束，敏感代码和数据也不必离开自己的环境。作为首个开放的 3T 级模型，这一点把此前只有闭源 API 才有的前沿能力变成了可自主掌控的基础设施。

  不过"最有用"其实取决于你是哪类开发者：

  **应用开发者 / 日常使用（走 API 或产品）**
  - **成本效率**最实际：编程和智能体任务上以 Claude Fable 5 约 1/3~1/10 的成本拿到接近顶级的分数，ProgramBench 第一、Terminal-Bench 88.3%
  - **多档推理强度（low/high/max）**：可以按任务难度控制 token 开销，简单任务省钱、难任务冲性能

  **做代码工具的开发者**
  - **1M 上下文**：整个仓库级别的代码可以一次性放入上下文，不再需要复杂的 RAG 切分
  - **原生视觉闭环**：写前端代码 → 看渲染截图 → 迭代修改，在同一上下文内完成，适合做 UI 生成、网页开发类工具（报告案例：WebDev Arena 排名第一）

  **有基础设施的团队**
  - 开放权重之外，报告还开源了配套基建：**MoonEP**（专家并行训练）、**FlashKDA**（注意力内核）、**AgentENV**（沙箱）等，训练和部署方案可复现
  - **MXFP4 量化感知训练**：部署时显存占用显著降低，且训练阶段就适配了量化，精度损失小

  **一个需要留意的点**：2.8T 参数即便量化后，本地部署门槛依然很高，对多数个人开发者来说，"开放权重"的价值更多体现在社区生态（蒸馏小模型、二次微调版本）而非直接自托管。所以从"今天就能用起来"的角度，**低成本的强编程/智能体能力 + 1M 上下文**可能是更直接的答案。
  ```
</Accordion>

## 6. 多文件问答

针对多份文件提问，实现方式很直接：**每个文件单独放在一条 system 消息里**，并把这些消息放在 messages 列表的头部：

```bash theme={null}
# 多文件示例还需要 K2 技术报告（同样来自官方仓库，下载后统一命名为 k2_tech_report.pdf）
curl -sSL -o k2_tech_report.pdf https://raw.githubusercontent.com/MoonshotAI/Kimi-K2/main/tech_report.pdf
ls -lh k2_tech_report.pdf
```

<Accordion title="输出示例">
  ```text theme={null}
  -rw-r--r--  1 user  staff   4.9M  8月 16 19:40 k2_tech_report.pdf
  ```
</Accordion>

```python theme={null}
def upload_files(files):
    """上传所有文件并提取内容，每个文件生成一条 role 为 system 的消息。"""
    messages = []
    for file in files:
        file_object = client.files.create(file=Path(file), purpose="file-extract")
        file_content = client.files.content(file_id=file_object.id).text
        messages.append({"role": "system", "content": file_content})
    return messages

file_messages = upload_files(["k3_tech_report.pdf", "k2_tech_report.pdf"])  # 两份报告均可从 MoonshotAI 的 GitHub 仓库下载

messages = [
    *file_messages,  # 文件消息在前
    {"role": "system", "content": persona},
    {"role": "user", "content": "对比这两份技术报告，K3 相比 K2 有哪些提升？"},
]

completion = client.chat.completions.create(
    model="kimi-k3",
    messages=messages,
)
print(completion.choices[0].message.content)
```

<Accordion title="输出示例">
  ```text theme={null}
  # Kimi K3 相比 K2 的主要提升

  ## 一、模型规模与架构

  K3 报告中的 Table 1 直接给出了两代模型的对比：

  | 维度 | Kimi K2 | Kimi K3 | 变化 |
  |---|---|---|---|
  | 总参数量 | 1.04T | 2.78T | ↑167% |
  | 激活参数量 | 32.6B | 104.2B | ↑220% |
  | 层数 | 61 | 93 | ↑52% |
  | 路由专家数 | 384 | 896 | ↑133% |
  | 每 token 激活专家 | 8 | 16 | ↑100% |
  | 共享专家 | 1 | 2 | ↑100% |
  | 训练上下文长度 | 128K | 1M | 8× |
  | 注意力机制 | 全部 MLA | 69 KDA + 24 MLA 混合 | 架构换代 |
  | 视觉能力 | 无（纯文本） | 原生多模态（MoonViT-V2, 0.4B） | 新增 |

  ## 二、架构层面的三大创新

  **1. 混合注意力（Hybrid Attention）**：K3 每个 block 采用 3 层 Kimi Delta Attention（KDA，线性注意力变体）+ 1 层 Gated MLA 的组合，替代 K2 的全 MLA 架构。KDA 引入通道级遗忘门和下界衰减（scaled sigmoid，g_min=-5），解决了数值溢出问题，使对角 tile 也能用 Tensor Core 密集计算。MLA 层采用 NoPE（无位置编码），因此无需 YaRN 等位置编码修改即可外推到 1M 上下文——K2 当年还需要用 YaRN 从 32K 扩展到 128K。

  **2. Attention Residuals（AttnRes）**：替代标准残差连接，让每层通过注意力机制选择性地从所有前序层检索表示，打通深度维度的信息流。K3 采用 Block AttnRes（8 个 block，每块 12 层）控制开销。

  **3. Stable LatentMoE**：为解决 896 专家、56 倍稀疏度带来的不稳定，引入三项技术——上投影前的 RMSNorm、有界激活函数 SiTU-GLU（替代 SwiGLU，输出上界 β₁β₂=100，抑制激活爆炸）、以及 Quantile Balancing（分位数负载均衡，替代 K2 沿用的固定步长 sign 更新）。

  这些改进合计带来约 **2.5× 的缩放效率提升**（相对 K2）。

  ## 三、预训练

  - **优化器**：K2 用 MuonClip（Muon + QK-Clip 防 logit 爆炸）；K3 升级为 Per-Head Muon（按头分别正交化，各头更新幅度更均衡），并保留权重裁剪机制。
  - **学习率调度**：K3 通过独立 scaling law 搜索证明 cosine decay 优于 K2 使用的 WSD，遂改为 cosine。
  - **上下文扩展课程**：K2 是 4K→32K→YaRN 到 128K；K3 是 8K→64K（预训练）→256K→1M（cooldown），并合成了必须依赖全 1M 上下文才能解决的任务数据，防止注意力退化为局部模式。
  - **原生多模态**：K3 从头联合训练语言与视觉，MoonViT-V2 不依赖 SigLIP 等对比学习初始化（纯 next-token prediction 训练），梯度更稳定。

  ## 四、后训练

  - **多推理档位 RL**：K3 在通用、通用 Agent、编码三大领域 × low/high/max 三个推理强度共训练 9 个专家模型，再通过 Multi-Teacher On-Policy Distillation（MOPD）蒸馏合并为统一模型；K2 没有这种 effort 分级与多教师蒸馏机制。
  - **RL 环境大幅扩展**：统一白盒环境（可组合出 Kimi Code、Claude Code、Codex 等不同 harness 防过拟合）、知识图谱引导的任务合成、kernel 优化任务（含防 reward hacking 检测）、跨多天的持久化个人助理任务（单次 rollout 可达数千次工具调用）、AET 自主执行任务（verify-in-the-loop）等。
  - **部署感知训练**：K3 从 SFT 起全程 MXFP4 量化感知训练（QAT），并将 MTP 层微调为 EAGLE-3 风格投机解码草稿模型（用 LK loss 直接优化接受率）；K2 均未涉及。
  - **奖励模型**：K2 用 self-critique rubric；K3 升级为带强制评分协议和冗长惩罚的 Agentic GRM。

  ## 五、基础设施

  - **KDA 系统协同设计**：FlashKDA 融合 kernel、KDA Context Parallelism（KCP，固定大小状态 all-gather 替代随序列增长的 KV 交换）。
  - **MoonEP**：完美均衡的专家并行（每 rank 恰好 S×K tokens，冗余专家上界 E/R 有理论证明），零拷贝通信、静态计算形状，消除逐层 host 同步。
  - **内存效率**：统一激活管理器、Pipeline ZeRO-2 梯度分片与 offload、P2P 式 Muon 正交化、ViT 计算藏入流水线气泡。
  - **1M Agentic RL**：外部 KV cache 池、自动节流调度、AgentENV 微虚拟机沙箱（支持暂停/恢复/分叉/快照，训练评估共创建超 5100 万个沙箱）。
  - **推理侧**：KDA 感知前缀缓存（两种缓存统一分页管理，512-token 细粒度命中）、舰队级缓存亲和调度与按预算准入控制。

  ## 六、性能表现

  注意两代报告的对比基线不同（K2 对标 DeepSeek-V3-0324、Claude Sonnet 4、GPT-4.1 等；K3 对标 Claude Fable 5、GPT-5.6 Sol 等新一代模型），分数不能直接横比，但能力提升明显：

  - **K2**：SWE-bench Verified 65.8、Tau2-Bench 66.1、LiveCodeBench v6 53.7、GPQA-Diamond 75.1，是当时最强的开源非思考模型。
  - **K3**：GPQA-Diamond 93.5、BrowseComp 91.2、Terminal-Bench 2.1 88.3、SWE-Marathon 42.0（领先 Claude Fable 5 达 7 分）、WebDev Arena 排名第一（首个登顶的开源模型），整体仅次于 Claude Fable 5 和 GPT-5.6 Sol，稳定领先其他所有参评模型；还新增了视觉（OmniDocBench 91.1 第一）、网络安全（发现 16 个未知漏洞）等全新能力维度。
  - **成本效率**：K3 在多套基准上接近最高分的同时，成本仅为 Claude Fable 5 的约 1/3 到 1/10。

  此外，K3 的案例研究展示了 K2 时代没有的长时程能力：24 小时自主优化 GPU kernel（AttnRes 延迟降低 60%）、从零开发 MiniTriton 编译器、48 小时完成芯片原型设计等。

  **一句话总结**：K3 在规模（1T→2.8T）、架构（混合线性注意力 + 深度注意力残差 + 超稀疏 LatentMoE）、上下文（128K→1M）、模态（纯文本→原生视觉）、训练方法（多档位 RL + 多教师蒸馏）和基础设施六个维度全面换代，并以约 2.5× 的缩放效率成为首个开源的 3T 级模型。
  ```
</Accordion>

## 7. 约束模型的作答

第 4 节的 system 消息是身份设定，告诉模型「你是谁」；实际使用中还经常需要追加一条 **作答规则**，告诉模型「回答要长什么样」——格式、篇幅、风格，都可以用一段固定的指令约束下来。这条规则和身份设定、文件内容一样属于稳定前缀，不影响下一节 Context Caching 的命中：

```python theme={null}
answer_rules = """回答规则：
1. 分点概括，不超过 5 点；
2. 每点一句话，并附上对应的原文片段作为出处；
3. 全文不超过 200 字。"""

question = "这份技术报告介绍了 K3 的哪些能力？"

base_messages = [
    {"role": "system", "content": persona},
    {"role": "system", "content": file_content},
    {"role": "user", "content": question},
]
messages_with_rules = [
    {"role": "system", "content": persona},
    {"role": "system", "content": file_content},
    {"role": "system", "content": answer_rules},  # 追加的作答规则
    {"role": "user", "content": question},
]
```

同一个问题，带着这条规则和不带规则各跑一次：不加规则时模型自由发挥，输出是一篇带小标题的长文；加上规则后，输出被收进规则限定的形态，分点概括、每点附原文出处、篇幅大幅收紧：

```python theme={null}
# 不带规则，模型自由发挥
completion = client.chat.completions.create(
    model="kimi-k3",
    messages=base_messages,
)
print(completion.choices[0].message.content)
```

<Accordion title="输出示例">
  ```text theme={null}
  这份技术报告介绍了 Kimi K3 的多方面能力，可以概括如下：

  ## 核心模型能力

  - **规模与架构**:2.8T 总参数的 MoE 模型，每 token 激活 104B 参数，是首个开源的 3T 级模型
  - **超长上下文**：支持 100 万 token 上下文窗口，通过 KDA(Kimi Delta Attention）混合注意力和 NoPE 设计直接外推，无需 RoPE 重缩放
  - **原生多模态**：文本、图像、视频由同一骨干网络处理，视觉编码器 MoonViT-V2 从零开始用 next-token prediction 训练，支持"视觉在环"的迭代工作流（写代码→看渲染结果→改进）
  - **扩展效率**：架构与训练配方改进带来相对 Kimi K2 约 2.5× 的整体扩展效率提升

  ## 评测展现的任务能力

  | 领域 | 代表性表现 |
  |---|---|
  | **推理与知识** | GPQA Diamond 93.5%；但研究级任务（HLE、CritPt）仍落后最强专有模型 |
  | **编程** | ProgramBench 最佳（77.8%),SWE-Marathon(GPU kernel 导向）42.0% 领先，Terminal-Bench 2.1 88.3% 接近 GPT-5.6 Sol |
  | **智能体** | BrowseComp 91.2%、DeepSearchQA 95.0%、MCPMark-Verified 94.5%、Harvey Lab-AA 94.6% 等多项 SOTA |
  | **视觉** | OmniDocBench 最高（91.1%),Math-Vision 配合 Python 工具达 97.8%,ZeroBench 与 Claude Fable 5 持平 |

  ## 长时程智能体能力

  - 通过跨通用、智能体、编程三大领域、多推理努力档位（low/high/max）的 RL 训练，支持数百到数千次工具调用、数百万 token 累积上下文的长期执行
  - 内部评测显示其在 Swarm Bench（多智能体编排）和 Deep Research Bench 上领先

  ## 案例研究展示的实际能力

  - **GPU kernel 优化**:24 小时内将 AttnRes 延迟从 283.6ms 降至 114.4ms
  - **编译器开发**：从零构建类 Triton 编译器 MiniTriton，性能接近 cuBLAS
  - **芯片设计**:48 小时自主完成推理芯片原型（nano-KPU）的设计、验证与时序收敛
  - **科研工作**：约 2 小时完成通常需 1-2 周的计算天体物理复现工作
  - **知识工作与视频编辑**：如分析 391 个引力波事件、制作 3Blue1Brown 风格动画

  ## 其他

  - **网络安全**：能发现真实漏洞（含 16 个未知漏洞，涉及 Linux 内核），并具备用户态端到端漏洞利用能力，但内核利用与完整利用链仍是瓶颈
  - **成本效率**：在四项编程/智能体套件上处于或接近成本效率前沿，以 Claude Fable 5 的一小部分成本达到接近的分数

  **整体定位**：报告明确指出，K3 整体仍落后于最强的专有模型 Claude Fable 5 和 GPT-5.6 Sol，但在评测套件中持续优于其他所有开源和专有模型，并完整开源了模型权重。
  ```
</Accordion>

```python theme={null}
# 加上规则，输出被收进规则限定的形态
completion = client.chat.completions.create(
    model="kimi-k3",
    messages=messages_with_rules,
)
print(completion.choices[0].message.content)
```

<Accordion title="输出示例">
  ```text theme={null}
  1. 架构规模：2.8T MoE、104B激活参数、1M上下文（"2.8T parameter…104 billion activated…1-million-token context"）；
  2. 原生视觉多模态（"native vision capabilities"）；
  3. 前沿编程与智能体能力（"frontier-level performance across long-horizon coding, agentic…"）；
  4. 多档推理强度的RL训练（"multiple reasoning effort levels"）；
  5. 高性价比（"cost-efficiency frontier"）。
  ```
</Accordion>

## 8. 控制成本：Context Caching

文件问答的计费有一个结构性特点：文档内容作为固定前缀出现在每一次请求里，同一份文档问得越多，这部分前缀被重复计费的次数就越多。Context Caching 就是消除这部分重复成本的机制。Kimi API 对所有请求自动启用，当检测到重复的初始上下文（system prompt、文件内容、工具定义等）时，直接复用已缓存的前缀，按缓存命中计费，而不是每次全价重算。

不需要任何额外代码。无需手动创建缓存，无需引用缓存 ID，也无需管理 TTL，只要像平常一样调用 /v1/chat/completions 即可。你要做的只有一件事：让文件内容、system prompt、工具定义这些固定部分保持稳定，并放在 messages 数组的最前面。

官方文档里的两个细节：

* 前一个请求的 prompt tokens 大于 256 时，后续请求才能命中前缀缓存；小于 256 的请求不会被缓存。文件问答天然满足这个条件。
* 收益方面，官方给出的参考是：特定场景下成本最高可降 90%，长文本场景首 Token 延迟平均可降至 5 秒内。具体计费方式以产品定价页为准。

我们可以再发一次与第 7 节完全相同的请求，从 usage 里看缓存命中情况：

```python theme={null}
completion = client.chat.completions.create(
    model="kimi-k3",
    messages=messages_with_rules,  # 与上一节完全相同的请求
)

usage = completion.usage
cached = usage.prompt_tokens_details.cached_tokens or 0
print(f"本次请求 prompt tokens: {usage.prompt_tokens:,}")
print(f"其中缓存命中: {cached:,}，占比 {cached / usage.prompt_tokens:.1%}")
```

<Accordion title="输出示例">
  ```text theme={null}
  本次请求 prompt tokens: 60,248
  其中缓存命中: 60,160，占比 99.9%
  ```
</Accordion>

和 RAG 方案对比，官方的建议是：频繁查询固定内容（如 FAQ、文档问答）优先使用 Context Caching；内容极长且查询方向不固定时，可以考虑 RAG 方案。两者的对比如下：

| 维度   | Context Caching            | RAG                                    |
| ---- | -------------------------- | -------------------------------------- |
| 业务成本 | 特定场景下成本压缩程度极高，最高可降本 90%    | 任何业务均可降本，但召回精度问题可能导致回答准确率下降            |
| 研发成本 | 相对较低，系统自动处理缓存，无需额外接入或调优    | 相对较高，需 RAG 与 Embedding 结合，并持续进行业务定制化调优 |
| 额外优势 | 长文本场景下首 Token 延迟平均可降至 5s 内 | 原始文本长度可扩展到非常长，适合一次性数百万字上下文的场景          |

## 9. 清理已上传的文件

已上传文件会占用组织总存储配额（默认 10 GiB）。提取完成后，可以删除不再需要的文件释放配额。如需定期全量清理，可以用 `files.list` 列出所有文件后逐一通过 `files.delete` 删除：

```python theme={null}
# 删除本次上传的文件，释放云端配额
client.files.delete(file_id=file_object.id)
```

<Accordion title="输出示例">
  ```text theme={null}
  FileDeleted(id='file_fc1t3y77tkk111gafm81', deleted=True, object='file')
  ```
</Accordion>

```python theme={null}
# 全量清理：列出所有文件并逐一删除
file_list = client.files.list()

for file in file_list.data:
    client.files.delete(file_id=file.id)
```

## 10. 常见问题（FAQ）

<Accordion title="提取失败怎么办">
  文件提取可能失败：格式不支持、文件损坏、超过 100MB 上限等。接口不支持的格式模型无法解析，请不要放入上下文。建议把上传和提取包一层防御性处理：

  ```python theme={null}
  def extract_file(path):
      try:
          file_object = client.files.create(file=Path(path), purpose="file-extract")
          content = client.files.content(file_id=file_object.id).text
      except Exception as e:
          print(f"{path} 提取失败：{e}")
          return None
      if not content or not content.strip():
          print(f"{path} 提取结果为空，请检查文件是否损坏或格式是否支持")
          return None
      return content

  extract_file("不存在的文件.pdf")  # 演示失败分支
  ```

  ```text 输出示例 theme={null}
  不存在的文件.pdf 提取失败：[Errno 2] No such file or directory: '不存在的文件.pdf'
  ```
</Accordion>

<Accordion title="文档太长怎么办">
  借助 kimi-k3 的 1M 上下文，大多数单份文档都可以整份放入。如果文档实在过长，可以按文档自身的结构（章节、标题）切分成几段，每段作为一条 system 消息放入。

  如果你的场景是"海量文档、查询方向不固定"，比如在整个知识库里随意提问，那已经超出了单篇问答的适用范围，建议参考第 8 节给出的 Context Caching 与 RAG 的选择建议。
</Accordion>

***

参考文档：[使用 Kimi API 进行文件问答](https://platform.kimi.com/docs/guide/use-kimi-api-for-file-based-qa)、[文件上传接口（API 参考）](https://platform.kimi.com/docs/api/files-upload)、[使用 Kimi API 的 Context Caching 功能](https://platform.kimi.com/docs/guide/use-context-caching-feature-of-kimi-api)。
