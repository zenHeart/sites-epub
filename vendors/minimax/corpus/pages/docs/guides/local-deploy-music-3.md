> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 自托管部署 MiniMax Music 3

> 使用固定版本的 SGLang-Omni 部署 MiniMax Music 3，并通过 Speech API 生成歌曲。

MiniMax Music 3 根据歌词和音乐描述生成包含人声与伴奏的完整歌曲。本页介绍如何使用 SGLang-Omni 在 NVIDIA CUDA GPU 上部署 HTTP 服务；这是面向服务器的**自托管部署**，不是消费级设备本地运行指南。

<Note>
  模型卡声明模型原生支持最长约 5 分钟的歌曲。SGLang-Omni 最多接受 `9,000` 个声学帧，按每秒 25 帧换算为 6 分钟请求上限。框架上限不代表模型额外验证了 1 分钟能力。需要保持在模型已公开的 5 分钟范围内时，请将 `max_new_tokens` 设为不超过 `7,500`。
</Note>

## 部署状态

| 项目          | 基线                                                                                           |
| :---------- | :------------------------------------------------------------------------------------------- |
| 部署状态        | 官方未公开稳定性等级；MiniMax 发布完整硬件与性能基线前，请将本页作为参考部署方案                                                 |
| 已验证 API 路径  | 通过 `POST /v1/audio/speech` 输入歌词和音乐描述，获得非流式 WAV 响应                                            |
| 模型          | `MiniMaxAI/MiniMax-Music3`                                                                   |
| 模型 revision | `fbdf52fbaaca799592917417eb05f1899f1255ec`                                                   |
| 推理框架        | `sglang-omni==0.1.3`（[tag `v0.1.3`](https://github.com/sgl-project/sglang-omni/tree/v0.1.3)） |
| Python      | 3.10–3.12；本文使用 3.12                                                                          |
| 文档核验日期      | 2026 年 8 月 26 日                                                                              |

固定模型 revision 和推理框架版本可以避免命令随 `main` 分支变化，但不代表 MiniMax 已验证所有兼容的 GPU、驱动和操作系统组合。

## 硬件基线

SGLang-Omni 只公开了一套参考音频配置和两种阶段放置方式，尚未公开 Music 3 的峰值显存、最低 GPU 显存、主机内存、最低驱动版本、生成耗时或实时系数。

| 配置                  | GPU 放置                           | 参考负载                      | 峰值显存 | 主机内存 | 性能  | 状态           |
| :------------------ | :------------------------------- | :------------------------ | :--- | :--- | :-- | :----------- |
| 1 × NVIDIA H200     | 自回归和声学阶段位于同一张 GPU                | 使用默认设置生成 5 个不超过 30 秒的参考片段 | 未公开  | 未公开  | 未公开 | 上游参考配置       |
| 2 × NVIDIA CUDA GPU | 自回归阶段位于 GPU 0；DiT 和音频解码器位于 GPU 1 | 未公开                       | 未公开  | 未公开  | 未公开 | 支持阶段放置，未验证容量 |

单 GPU 命令不代表任意 CUDA GPU 都具备足够显存。接收生产流量前，请先在实际硬件上验证短音频请求。模型仓库当前显示文件总量约 57.4 GB；还需为 Python 环境、下载元数据和临时文件预留额外磁盘空间。

## 快速开始

### 安装固定版本的运行环境

请使用配有 NVIDIA CUDA GPU 的干净 Linux 环境。SGLang-Omni `0.1.3` 固定使用 CUDA 13 运行时组件、PyTorch `2.11.0` 和 SGLang `0.5.16`。上游尚未为 Music 3 配置公开准确的 NVIDIA 最低驱动版本；安装前请确认主机驱动支持所安装的 CUDA 运行时。

```bash theme={null}
uv venv .venv --python 3.12
source .venv/bin/activate
uv pip install --prerelease=allow "sglang-omni==0.1.3"

python -c "import sglang_omni, torch; print(sglang_omni.__version__, torch.__version__, torch.cuda.is_available())"
```

继续操作前，最后一个值必须为 `True`。UCX 与 CUDA 编译依赖请参阅 [SGLang-Omni 安装指南](https://sgl-project.github.io/sglang-omni/get_started/installation.html)。

### 下载固定版本的权重

```bash theme={null}
export MUSIC3_MODEL_DIR=/data/models/MiniMax-Music3-fbdf52f

hf download MiniMaxAI/MiniMax-Music3 \
  --revision fbdf52fbaaca799592917417eb05f1899f1255ec \
  --local-dir "$MUSIC3_MODEL_DIR"
```

### 启动服务

快速开始默认只监听本机回环地址。保持当前终端运行：

```bash theme={null}
CUDA_VISIBLE_DEVICES=0 sgl-omni serve \
  --model-path "$MUSIC3_MODEL_DIR" \
  --model-name MiniMaxAI/MiniMax-Music3 \
  --host 127.0.0.1 \
  --port 8000
```

### 检查服务健康状态

在另一个终端执行：

```bash theme={null}
curl -fsS http://127.0.0.1:8000/health
curl -fsS http://127.0.0.1:8000/v1/models
```

`/health` 应返回 HTTP `200`，状态为 healthy 且 running。`/v1/models` 应包含 `MiniMaxAI/MiniMax-Music3`。

### 生成并验证歌曲

```bash theme={null}
curl --fail-with-body -X POST http://127.0.0.1:8000/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMaxAI/MiniMax-Music3",
    "input": "[Verse]\n晨光穿过安静的窗\n街道在微风中醒来\n[Chorus]\n向着今天出发\n让歌声越过云海",
    "instructions": "温暖的原声流行歌曲，96 BPM，女声主唱，指弹吉他与柔和钢琴，副歌逐渐加入鼓组并扩展立体声场。",
    "seed": 7,
    "max_new_tokens": 750,
    "response_format": "wav",
    "stream": false
  }' \
  --output minimax_music3.wav

python -c 'import wave; f=wave.open("minimax_music3.wav"); print({"channels": f.getnchannels(), "sample_rate": f.getframerate(), "sample_width_bytes": f.getsampwidth(), "duration_seconds": round(f.getnframes()/f.getframerate(), 2)})'
```

文件必须是非空 WAV，并显示 `channels=2`、`sample_rate=32000` 和 `sample_width_bytes=2`。`750` 帧最多允许 30 秒音频；模型输出音频结束标记时，实际时长可以更短。

## 能力边界

| 能力                 | 模型原生能力                | 当前部署路径已验证能力                               |
| :----------------- | :-------------------- | :---------------------------------------- |
| 歌词与音乐描述生成完整歌曲      | 支持                    | 支持                                        |
| 输出格式               | 32 kHz、16-bit 立体声 WAV | 支持                                        |
| 歌曲时长               | 最长约 5 分钟              | 上游参考音频只验证了不超过 30 秒的片段；MiniMax 尚未公开长音频性能基线 |
| 流式生成               | 不支持                   | `stream` 必须为 `false`                      |
| 音色选择或克隆            | 当前请求协议不支持             | `voice` 和参考音频字段会被拒绝                       |
| 精确 BPM、调性、乐器、歌词或结构 | 属于生成控制，不是严格保证         | 不保证                                       |

SGLang-Omni 声明，在相同环境中保持歌词、instructions、seed 和长度完全一致，可以得到字节级一致的音频。不要假设不同模型 revision、推理框架版本或硬件栈之间仍可保持字节级一致。

## 请求协议

| 字段                | 要求                                                                     |
| :---------------- | :--------------------------------------------------------------------- |
| `input`           | 必填且不能为空，用于提供歌词。`[Verse]`、`[Chorus]`、`[Bridge]`、`[Outro]` 等结构标签必须单独占一行。 |
| `instructions`    | 必填且不能为空，用于描述曲风、乐器、速度、情绪、人声、编曲和制作风格。                                    |
| `seed`            | 非负 64-bit 整数。默认值 `0` 也是固定 seed，并非随机值。                                  |
| `max_new_tokens`  | 声学帧数上限，每秒 25 帧。服务端最大值为 `9,000`；要保持在模型公开的 5 分钟范围内，请不超过 `7,500`。         |
| `response_format` | 必须为 `wav`。                                                             |
| `stream`          | 必须为 `false`；模型生成完成后才返回响应。                                              |

文本提示分词后最多为 5,000 token。如果其他字段均有效但请求因这一限制被拒绝，请缩短歌词或 instructions。

<Warning>
  结构标签必须单独占一行。例如，应写成 `[Verse]\nWalking down the street`。如果把歌词写在标签同一行，规范化阶段可能在不报错的情况下删除该行歌词。
</Warning>

不要传入 `temperature`、`top_p`、`top_k`、`repetition_penalty`、`voice`、参考音频字段、`language` 或 `task_type`。速度和人声特征应写入 `instructions`。

HTTP 客户端还有一种名为 **streaming response** 的机制，表示客户端把已经产生的 HTTP 响应体分块写入磁盘。它不会让 Music 3 的模型生成变成流式。本指南统一使用普通的 `curl --output`，避免混淆这两个概念。

## 权重、缓存与离线部署

* 官方权重：[`MiniMaxAI/MiniMax-Music3`](https://huggingface.co/MiniMaxAI/MiniMax-Music3)
* 本文固定的权重：[revision `fbdf52f`](https://huggingface.co/MiniMaxAI/MiniMax-Music3/tree/fbdf52fbaaca799592917417eb05f1899f1255ec)
* Hugging Face 默认缓存目录为 `~/.cache/huggingface/hub`；可通过 `HF_HOME` 或 `HF_HUB_CACHE` 调整。
* 本文使用 `--local-dir`，服务启动时直接加载固定本地路径，不解析远程 `main`。
* 截至文档核验日期，Music 3 模型卡没有链接 MiniMax 官方 ModelScope 镜像。

离线部署时，先在联网机器下载固定 revision，再把完整目录复制到目标主机，并使用本地路径启动。可通过以下环境变量阻止意外访问网络：

```bash theme={null}
export HF_HUB_OFFLINE=1
export MUSIC3_MODEL_DIR=/data/models/MiniMax-Music3-fbdf52f

CUDA_VISIBLE_DEVICES=0 sgl-omni serve \
  --model-path "$MUSIC3_MODEL_DIR" \
  --model-name MiniMaxAI/MiniMax-Music3 \
  --host 127.0.0.1 \
  --port 8000
```

下载中断或文件损坏时，请使用相同 revision 重新执行 `hf download`。只有需要替换本地文件，而不是续传或复用已有文件时，才添加 `--force-download`。

## 生产部署与安全

### 使用两张 GPU

SGLang-Omni 会把自回归阶段放在第一张可见 GPU，把 DiT 和音频解码阶段放在第二张：

```bash theme={null}
CUDA_VISIBLE_DEVICES=0,1 sgl-omni serve \
  --model-path "$MUSIC3_MODEL_DIR" \
  --model-name MiniMaxAI/MiniMax-Music3 \
  --host 127.0.0.1 \
  --port 8000
```

这只是阶段放置选项，不代表任何特定双 GPU 组合具备最低显存或性能保证。

### 规划并发

Music 3 在两个生成阶段都使用 classifier-free guidance。每个请求会在自回归引擎中占用两行 KV Cache。提高请求上限时，需要按准入请求数的两倍规划容量：

```bash theme={null}
CUDA_VISIBLE_DEVICES=0,1 sgl-omni serve \
  --model-path "$MUSIC3_MODEL_DIR" \
  --model-name MiniMaxAI/MiniMax-Music3 \
  --host 127.0.0.1 \
  --port 8000 \
  --max-running-requests 32
```

在实际硬件上测量峰值显存和延迟之前，不要提高此值。先用 10 秒、250 帧的片段验证歌词和音乐描述，再生成完整歌曲，可以降低迭代成本。

### 安全地开放服务

尽可能让模型服务监听 `127.0.0.1`。需要远程访问时，应在前面部署带身份验证的 API 网关或反向代理，并配置 TLS、请求大小限制、速率限制、超时和网络白名单。不要把未经鉴权的 `0.0.0.0:8000` 直接暴露到互联网。配置访问日志和可观测性时，应将歌词和音乐描述视为潜在敏感数据。

## 故障排查

| 现象                                                    | 常见原因                                    | 处理方式                                                                                                           |
| :---------------------------------------------------- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| `torch.cuda.is_available()` 输出 `False`，或 CUDA 动态库加载失败 | 驱动、CUDA 运行时、PyTorch 与 SGLang-Omni 依赖不兼容 | 使用全新的 Python 3.10–3.12 环境，严格重装 `sglang-omni==0.1.3`，并在启动前确认主机驱动支持其 CUDA 运行时。                                   |
| 进程被终止或出现 CUDA OOM                                     | 单 GPU 无法容纳共置阶段，或并发/KV Cache 过大          | 将 `--max-running-requests` 设为 `1`，先测试 250 帧，停止其他 GPU 任务，或改用双 GPU 放置。不要假设降低 `mem_fraction_static` 可以解决声学阶段显存问题。 |
| 权重下载停滞、失败或加载报错                                        | 磁盘不足、网络中断或本地文件损坏                        | 检查剩余磁盘，按固定 revision 重新下载；只有需要替换损坏文件时才使用 `--force-download`。                                                    |
| `/health` 返回 `503` 或无法连接                              | 模型 Worker 仍在加载，或某个阶段启动失败                | 等待所有阶段就绪，再从服务日志中查找第一条 CUDA、依赖、权重或阶段间传输错误。                                                                      |
| 请求返回 HTTP `4xx`                                       | 必填字段为空，或传入了不支持的 Speech API 字段           | 从上面的最小请求开始，保持 `stream=false` 和 WAV 输出，并删除 TTS 采样、音色和参考音频字段。                                                    |
| 歌词缺失或音频短于请求长度                                         | 结构标签和歌词写在同一行，或模型输出了结束标记                 | 让标签单独占一行；`max_new_tokens` 是上限，不是目标时长。                                                                          |

遇到多 GPU NCCL 或 UCX 错误时，先确认单 GPU 命令可以启动，再检查 GPU 可见性、GPU 间连接，以及 SGLang-Omni 文档中的 UCX 前置依赖。

## License 与相关资源

| 资源         | 链接                                                                                                                              |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------ |
| 模型仓库       | [`MiniMaxAI/MiniMax-Music3`](https://huggingface.co/MiniMaxAI/MiniMax-Music3)                                                   |
| 推理代码与提示词工具 | [MiniMax-AI/MiniMax-Music3](https://github.com/MiniMax-AI/MiniMax-Music3)                                                       |
| 模型 License | [MiniMax-Music3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-Music3/blob/main/LICENSE)                           |
| 推理参考       | [SGLang-Omni `v0.1.3` Music 3 Cookbook](https://github.com/sgl-project/sglang-omni/blob/v0.1.3/docs/cookbook/minimax_music3.md) |

模型 License 包含产品署名、商业收入门槛、安全措施、知识产权和 Acceptable Use Policy 等要求。向第三方提供 Music 3 服务前，请阅读权威 License 原文并落实全部适用条款。SGLang-Omni 另行采用 Apache-2.0 License。
