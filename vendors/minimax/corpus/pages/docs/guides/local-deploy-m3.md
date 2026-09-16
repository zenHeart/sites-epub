> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 自托管部署 MiniMax-M3

> 运行 MiniMax-M3 的 SGLang 实验性基线，验证服务，并规划安全的自托管部署。

MiniMax-M3 是原生多模态混合专家模型，总参数约 428B，每个 token 激活参数约 23B，模型上下文上限为 1M token。本页介绍使用 SGLang 进行的**服务器级自托管部署**，不属于消费级设备本地推理。

<Warning>
  **部署状态：Experimental。** 截至 2026 年 8 月 26 日，MiniMax-M3 支持仍通过 SGLang 开发镜像提供，尚未进入带版本号的 SGLang 正式版本。请固定下方模型 revision 和镜像 digest，并使用自己的负载完成验证；不要将本配方视为生产 SLA。
</Warning>

## 状态与参考基线

| 项目          | 参考值                                                                                             |
| :---------- | :---------------------------------------------------------------------------------------------- |
| 部署状态        | Experimental                                                                                    |
| 文档最后核验日期    | 2026 年 8 月 26 日                                                                                 |
| 参考硬件        | 8 × NVIDIA B200、单节点、TP 8                                                                        |
| 权重          | `MiniMaxAI/MiniMax-M3-MXFP8`                                                                    |
| 模型 revision | `c5454eb03678d8710e54a4e0fc681b9f3b4a3dba`                                                      |
| 权重仓库大小      | 固定 revision 下约 444 GB                                                                           |
| SGLang 镜像   | `lmsysorg/sglang@sha256:de63ac56df5d7b064451e21147eaab89634a02332d830ca8c01cb8c033b3a78f`       |
| 运行环境        | Linux、Docker 和 NVIDIA Container Toolkit；Python 与 CUDA 由固定镜像提供                                   |
| 验证来源        | [SGLang MiniMax-M3 Cookbook](https://docs.sglang.io/cookbook/autoregressive/MiniMax/MiniMax-M3) |

官方来源没有公布本配方的最低主机内存、峰值显存、最低 NVIDIA 驱动版本或完整生产磁盘余量。部署前，请确认宿主机驱动与固定镜像内的 CUDA Runtime 兼容，并准备大于权重仓库大小的可用磁盘。

<Warning>
  总权重仍需完整加载或分片。“23B 激活参数”不代表部署只需为 23B 权重准备显存。
</Warning>

## 硬件配置

下表报告 SGLang 当前支持矩阵。“已验证”表示经过 SGLang Cookbook 验证，不代表本文档完成了 MiniMax 独立复测。

| 硬件                  | 权重                     | GPU / TP | SGLang 状态         | 权重存储     | 峰值显存 | 主机内存 | 拓扑  |
| :------------------ | :--------------------- | :------- | :---------------- | :------- | :--- | :--- | :-- |
| NVIDIA B200         | MXFP8                  | 8 / 8    | 已验证；参考基线          | 约 444 GB | 未公布  | 未公布  | 单节点 |
| NVIDIA B300         | MXFP8                  | 4 / 4    | 已验证               | 约 444 GB | 未公布  | 未公布  | 单节点 |
| NVIDIA GB300        | MXFP8                  | 4 / 4    | 已验证               | 约 444 GB | 未公布  | 未公布  | 单节点 |
| NVIDIA GB200        | MXFP8                  | 4 / 4    | SGLang 推定支持；未直接测试 | 约 444 GB | 未公布  | 未公布  | 单节点 |
| NVIDIA H200         | BF16                   | 8 / 8    | 已验证               | 约 854 GB | 未公布  | 未公布  | 单节点 |
| AMD MI355X          | MXFP8                  | 8 / 8    | 已验证文本负载           | 约 444 GB | 未公布  | 未公布  | 单节点 |
| AMD MI300X          | MXFP8，加载时转换为 Block FP8 | 8 / 8    | 已验证文本负载           | 约 444 GB | 未公布  | 未公布  | 单节点 |
| AMD MI350X / MI325X | MXFP8                  | 8 / 8    | 根据同架构 GPU 推定      | 约 444 GB | 未公布  | 未公布  | 单节点 |

如需 B300、GB 系列、H200 或 AMD 的准确命令，请使用 [SGLang 配置生成器](https://docs.sglang.io/cookbook/autoregressive/MiniMax/MiniMax-M3#hw=b200\&variant=default\&quant=mxfp8\&strategy=balanced\&nodes=single)。未经重新验证，不要直接把这些命令参数替换到本页 B200 基线中。

## Quickstart：8 × B200

开始前，请确认宿主机有足够空间存放约 444 GB 权重、容器镜像和缓存。

### 1. 拉取固定运行时

```bash theme={null}
docker pull lmsysorg/sglang@sha256:de63ac56df5d7b064451e21147eaab89634a02332d830ca8c01cb8c033b3a78f
```

### 2. 验证 GPU 访问

输出必须列出全部 8 张 B200 GPU：

```bash theme={null}
docker run --rm --gpus all \
  lmsysorg/sglang@sha256:de63ac56df5d7b064451e21147eaab89634a02332d830ca8c01cb8c033b3a78f \
  nvidia-smi
```

### 3. 启动服务

```bash theme={null}
docker run --rm --name minimax-m3 \
  --gpus all \
  --shm-size 32g \
  --ipc=host \
  -p 127.0.0.1:30000:30000 \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  lmsysorg/sglang@sha256:de63ac56df5d7b064451e21147eaab89634a02332d830ca8c01cb8c033b3a78f \
  sglang serve \
  --trust-remote-code \
  --model-path MiniMaxAI/MiniMax-M3-MXFP8 \
  --revision c5454eb03678d8710e54a4e0fc681b9f3b4a3dba \
  --reasoning-parser auto \
  --tool-call-parser auto \
  --tp 8 \
  --attention-backend fa4 \
  --mm-attention-backend flashinfer_cudnn \
  --moe-runner-backend deep_gemm \
  --chunked-prefill-size 8192 \
  --mem-fraction-static 0.65 \
  --host 0.0.0.0 \
  --port 30000
```

进程在**容器内部**监听所有接口，但 `-p 127.0.0.1:30000:30000` 只将端口发布到宿主机回环地址。首次启动需要下载约 444 GB 权重，所需时间取决于存储和网络吞吐。

### 4. 检查就绪状态

服务日志显示已经就绪后，在另一个终端运行：

```bash theme={null}
curl --fail --silent --show-error http://127.0.0.1:30000/health
```

检查成功时，命令以状态码 `0` 退出。如果失败，请保持服务进程运行并检查日志，再发送推理请求。

### 5. 验证文本生成

```bash theme={null}
curl http://127.0.0.1:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMaxAI/MiniMax-M3-MXFP8",
    "messages": [
      {"role": "user", "content": "Explain sparse attention in one sentence."}
    ],
    "temperature": 1.0,
    "top_p": 0.95,
    "max_tokens": 1024
  }'
```

成功响应包含非空的 `choices[0].message.content`。模型产生推理轨迹时，SGLang 会将其单独放在 `choices[0].message.reasoning_content`。

### 6. 验证图片输入

```bash theme={null}
curl http://127.0.0.1:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMaxAI/MiniMax-M3-MXFP8",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "Describe this image in one sentence."},
        {"type": "image_url", "image_url": {"url": "https://raw.githubusercontent.com/sgl-project/sglang/2511743bd784e69e5a81ca3d926a000711dae4ab/examples/assets/example_image.png"}}
      ]
    }],
    "temperature": 1.0,
    "top_p": 0.95,
    "max_tokens": 1024
  }'
```

示例图片由 SGLang 项目维护。生产环境只接受可信或已加入白名单的远程 URL，或者在网关校验文件后发送 Base64 data URI。

## 能力边界

| 能力      | 模型原生能力      | 本页 B200 SGLang 配方             | 说明                                                     |
| :------ | :---------- | :---------------------------- | :----------------------------------------------------- |
| 文本输入与输出 | 支持          | SGLang 已验证                    | OpenAI 兼容 Chat Completions                             |
| 推理      | 支持          | SGLang 已验证                    | 需要 `--reasoning-parser auto`                           |
| 工具调用    | 支持          | SGLang 已验证                    | 需要 `--tool-call-parser auto`；上游覆盖单个、并行、对象和数组参数         |
| 图片输入    | 支持          | SGLang 已验证 URL 和 Base64 输入    | Blackwell 需要 `--mm-attention-backend flashinfer_cudnn` |
| 视频输入    | 模型支持        | 本 SGLang 配方未验证                | 未自行验证前，不要宣称本配方支持视频服务                                   |
| 上下文长度   | 最高 1M token | SGLang 报告已验证 1K～128K 输入 token | 1M 是模型上限，不是本配置已验证的生产默认值                                |

在 AMD 平台上，SGLang 已验证文本对话、推理内容分离和工具调用；ROCm 路径尚未验证视觉输入。

## 已发布性能数据

SGLang 报告了以下服务测量结果。这些数据是上游参考结果，不构成 MiniMax 性能保证。

| 硬件       | 权重 / TP      | 负载                                 | 平均 TTFT  | 平均 TPOT | 单 GPU 吞吐       |
| :------- | :----------- | :--------------------------------- | :------- | :------ | :------------- |
| 8 × B200 | MXFP8 / TP 8 | 随机数据；2,048 输入、256 输出、并发 64、128 个请求 | 1,580 ms | 24.1 ms | 2,385 tokens/s |
| 8 × H200 | BF16 / TP 8  | 随机数据；2,048 输入、256 输出、并发 64、128 个请求 | 1,054 ms | 70.8 ms | 1,044 tokens/s |

两项测试都使用 SGLang PR `#27944`、CUDA Graph、清空缓存和预热后的稳态运行。来源未公布峰值显存、主机内存、冷启动时间和生产并发建议。容量规划前，请使用自身的提示词长度、输出长度、多模态请求比例和并发进行压测。

## 权重、缓存与离线部署

运行时默认将 Hugging Face 文件下载到容器内的 `/root/.cache/huggingface`；Quickstart 命令将其映射到宿主机 `~/.cache/huggingface`。

如需准备离线副本，请在联网机器上安装 [Hugging Face CLI](https://huggingface.co/docs/huggingface_hub/guides/cli)，并下载固定 revision：

```bash theme={null}
hf download MiniMaxAI/MiniMax-M3-MXFP8 \
  --revision c5454eb03678d8710e54a4e0fc681b9f3b4a3dba \
  --local-dir /data/models/MiniMax-M3-MXFP8
```

将该目录复制到部署主机，然后在不访问 Hub 的情况下启动：

```bash theme={null}
docker run --rm --name minimax-m3 \
  --gpus all \
  --shm-size 32g \
  --ipc=host \
  -p 127.0.0.1:30000:30000 \
  -e HF_HUB_OFFLINE=1 \
  -v /data/models/MiniMax-M3-MXFP8:/models/MiniMax-M3-MXFP8:ro \
  lmsysorg/sglang@sha256:de63ac56df5d7b064451e21147eaab89634a02332d830ca8c01cb8c033b3a78f \
  sglang serve \
  --trust-remote-code \
  --model-path /models/MiniMax-M3-MXFP8 \
  --reasoning-parser auto \
  --tool-call-parser auto \
  --tp 8 \
  --attention-backend fa4 \
  --mm-attention-backend flashinfer_cudnn \
  --moe-runner-backend deep_gemm \
  --chunked-prefill-size 8192 \
  --mem-fraction-static 0.65 \
  --host 0.0.0.0 \
  --port 30000
```

ModelScope 已提供官方镜像：[`MiniMax/MiniMax-M3-MXFP8`](https://modelscope.cn/models/MiniMax/MiniMax-M3-MXFP8) 和 [`MiniMax/MiniMax-M3`](https://modelscope.cn/models/MiniMax/MiniMax-M3)。ModelScope 页面没有使用本基线所采用的 Hugging Face commit 标识快照，因此，在固定 revision 的部署中替换镜像前，请重新验证文件。

下载中断时，使用相同 revision 和目录重新运行 `hf download`，客户端会从缓存继续。如果加载时报权重分片缺失或损坏，请先确认可用磁盘空间并重新下载对应 revision，再调整运行参数。

## 生产部署与安全

开发环境请保留回环地址绑定。将服务暴露给其他主机前：

* 设置不可预测的 SGLang `--api-key`，并通过 `Authorization: Bearer <key>` 发送。
* 在反向代理或可信入口终止 TLS，使用防火墙或安全组限制来源网络，并增加请求速率和并发限制。
* 除非数据策略明确允许，否则不要记录 API Key、完整提示词、Base64 媒体或模型输出。
* 在网关拒绝任意远程媒体 URL。应用域名白名单，阻止私有地址和链路本地地址，限制重定向次数、下载时间、字节大小、图片像素和视频时长，并在转发请求前校验媒体类型。
* 监控 GPU 内存、队列深度、请求延迟、错误率、进程健康和磁盘使用量。仅得到成功的 `/health` 响应不能代表已达到生产就绪状态。

SGLang 支持 `--api-key`，但当前 MiniMax-M3 Cookbook 未提供完整的远程媒体安全策略。请在网关和网络层实施这些控制。

## 故障排查

| 症状                                                                | 最可能原因                           | 最短修复步骤                                                                                                        |
| :---------------------------------------------------------------- | :------------------------------ | :------------------------------------------------------------------------------------------------------------ |
| 启动或预填充阶段出现 `CUDA out of memory`                                   | 激活值余量不足或预填充分块过大                 | 将 `--mem-fraction-static` 降至 `0.65` 以下，再将 `--chunked-prefill-size` 降为 `4096` 或 `2048`；这会降低 KV 容量或预填充速度，需要重新压测 |
| 权重加载失败或缺少分片                                                       | 下载不完整、磁盘不足或 revision 不一致        | 确认模型路径、可用磁盘和 revision；使用固定 revision 重新运行 `hf download`                                                        |
| CUDA Graph 捕获阶段出现 `AttributeError: Module has no function 'plan'` | 多个 TP rank 并发 JIT 编译 MSA Kernel | 在相同镜像和缓存中单进程运行一次 SGLang Cookbook 的 `msa_available()` 检查，然后重启服务                                                |
| B200 上没有启用 MSA                                                    | 镜像错误、GPU 架构不支持或缺少 `fa4` 后端      | 确认使用固定镜像和 `--attention-backend fa4`；按照 Cookbook 的 Gate 检查确认输出为 `True`                                         |
| NCCL 初始化卡住或超时                                                     | 未暴露全部 GPU、共享内存不足，或拓扑/驱动异常       | 使用 `nvidia-smi` 确认 8 张 GPU，保留 `--ipc=host` 和 `--shm-size 32g`，再启用 `NCCL_DEBUG=INFO` 并检查首个失败 rank              |
| `content` 中出现原始 `<mm:think>` 或 MiniMax 工具调用 token                 | 未启用对应 Parser，或运行时不同于固定镜像        | 恢复 `--reasoning-parser auto` 和 `--tool-call-parser auto`，然后使用固定 digest 重启                                     |
| 进程启动后 `/health` 仍失败                                               | 模型仍在下载/加载、Worker 已退出或端口映射错误     | 检查容器日志、宿主机磁盘和 GPU 状态，并确认发布了 `127.0.0.1:30000:30000`                                                           |
| 远程图片请求失败                                                          | 服务端无法访问 URL，或网关阻止该 URL          | 改用白名单 URL 或经过校验的 Base64 data URI；不要全局关闭网络防护                                                                   |

## License 与使用限制

BF16 和 MXFP8 权重均按 [MiniMax Community License](https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/LICENSE) 发布，其中包含署名要求、商业使用通知或授权要求以及禁止用途。生产或商用前，请阅读完整 License 并完成适用流程；本页不构成法律建议。

## 相关链接

<CardGroup cols={2}>
  <Card title="SGLang MiniMax-M3 Cookbook" icon="book-open" href="https://docs.sglang.io/cookbook/autoregressive/MiniMax/MiniMax-M3">
    查看上游硬件矩阵、配置生成器、性能测试条件和高级调优。
  </Card>

  <Card title="MiniMax-M3 模型卡" icon="file-text" href="https://huggingface.co/MiniMaxAI/MiniMax-M3">
    查看官方权重、模型能力、推理参数和 License。
  </Card>

  <Card title="MiniMax-M3 MXFP8 权重" icon="database" href="https://huggingface.co/MiniMaxAI/MiniMax-M3-MXFP8">
    打开参考部署使用的 MXFP8 Checkpoint。
  </Card>

  <Card title="MiniMax Sparse Attention" icon="bolt" href="https://github.com/MiniMax-AI/MSA">
    查看 MSA Kernel 源码和 Blackwell 要求。
  </Card>
</CardGroup>
