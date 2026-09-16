> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 部署 MiniMax-M2.7

> 参考 SGLang Cookbook 部署 MiniMax-M2.7，并通过 OpenAI 兼容接口验证推理、思考内容和工具调用。

MiniMax-M2.7 是面向 Agent、软件工程和复杂生产力任务的语言模型。新项目需要原生多模态输入或 1M 上下文时，建议选择 [MiniMax-M3](/docs/guides/local-deploy-m3)；已有 M2.7 工作流可以按本页继续部署。

## 开放内容与 License

| 项目              | 说明                                                                                      |
| :-------------- | :-------------------------------------------------------------------------------------- |
| 模型仓库            | [`MiniMaxAI/MiniMax-M2.7`](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)               |
| License         | [MiniMax-M2.7 License](https://huggingface.co/MiniMaxAI/MiniMax-M2.7/blob/main/LICENSE) |
| SGLang Cookbook | [MiniMax-M2.7](https://docs.sglang.io/cookbook/autoregressive/MiniMax/MiniMax-M2.7)     |

MiniMax-M2.7 License 允许其中列出的个人、研究和教育等用途；商业使用包含署名和事先授权要求。生产或商用前，请阅读 License 原文。

## 硬件与镜像

SGLang Cookbook 当前列出的参考组合包括：

| 平台     | 参考硬件                      | SGLang 镜像                                     |
| :----- | :------------------------ | :-------------------------------------------- |
| NVIDIA | A100 / H100 / H200 / B200 | `lmsysorg/sglang:v0.5.10.post1`               |
| NVIDIA | B300 / GB300              | `lmsysorg/sglang:v0.5.10.post1-cu130`         |
| AMD    | MI300X / MI325X           | `lmsysorg/sglang:v0.5.10.post1-rocm720-mi30x` |
| AMD    | MI355X                    | `lmsysorg/sglang:v0.5.10.post1-rocm720-mi35x` |

NVIDIA 常见参考拓扑为 4 张高显存 GPU（TP 4）或 8 张 GPU（TP 8、EP 8）。不同硬件还支持 2、4 或 8 GPU 组合；请使用 [SGLang 配置生成器](https://docs.sglang.io/cookbook/autoregressive/MiniMax/MiniMax-M2.7) 获取对应命令。

## 参考部署：4 张 NVIDIA 高显存 GPU

### 启动服务

```bash theme={null}
docker run --gpus all \
  --shm-size 32g \
  -p 30000:30000 \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  --ipc=host \
  lmsysorg/sglang:v0.5.10.post1 \
  sglang serve \
  --model-path MiniMaxAI/MiniMax-M2.7 \
  --tp 4 \
  --tool-call-parser minimax-m2 \
  --reasoning-parser minimax-append-think \
  --trust-remote-code \
  --mem-fraction-static 0.85 \
  --host 0.0.0.0 \
  --port 30000
```

首次启动时，SGLang 会从 Hugging Face 下载模型。需要认证时，在 `docker run` 中增加：

```bash theme={null}
--env "HF_TOKEN=<your-hf-token>"
```

### 验证部署

```bash theme={null}
curl http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMaxAI/MiniMax-M2.7",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "用 Python 写一个判断素数的函数。"}
    ],
    "max_tokens": 2048
  }'
```

也可以使用 OpenAI SDK：

```python theme={null}
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:30000/v1",
    api_key="EMPTY",
)

response = client.chat.completions.create(
    model="MiniMaxAI/MiniMax-M2.7",
    messages=[{"role": "user", "content": "解释混合专家模型。"}],
    max_tokens=2048,
)

print(response.choices[0].message.content)
```

## 关键启动参数

| 参数                      | 推荐值                    | 作用                                          |
| :---------------------- | :--------------------- | :------------------------------------------ |
| `--tool-call-parser`    | `minimax-m2`           | 把模型工具调用解析为 OpenAI 兼容格式                      |
| `--reasoning-parser`    | `minimax-append-think` | 处理模型思考内容                                    |
| `--trust-remote-code`   | 启用                     | 加载模型仓库中的实现                                  |
| `--mem-fraction-static` | `0.85`                 | 为模型执行与 KV Cache 分配静态显存比例                    |
| `--tp`                  | `2`、`4` 或 `8`          | 根据硬件设置 Tensor Parallelism                   |
| `--ep`                  | 按配置生成器设置               | 8 GPU NVIDIA 或 AMD 部署可使用 Expert Parallelism |

<Warning>
  并行参数、KV Cache 容量和可用上下文长度彼此相关。不要只修改 GPU 数量；硬件发生变化时，应重新从 SGLang 配置生成器选择完整组合。
</Warning>

## 思考内容与工具调用

MiniMax-M2.7 会输出思考内容。启用 `minimax-append-think` 后，客户端应按照所用 SGLang 版本的响应格式读取或解析思考内容。启用 `minimax-m2` 后，可以通过 OpenAI 兼容的 `tools` 参数调用函数。

生产接入前，应分别验证：

* 非流式和流式文本生成
* 思考内容的展示或隐藏策略
* 单工具、并行工具和嵌套参数
* 长上下文下的显存余量

## 关于社区量化与 Mac 部署

Hugging Face 上存在 MLX、GGUF 等社区转换版本，但这些版本由各自发布者维护，不属于本页的 MiniMax + SGLang 官方参考部署范围。使用社区版本时，请单独核对模型转换方式、量化误差、License 和运行框架兼容性。

## 相关链接

<CardGroup cols={2}>
  <Card title="SGLang MiniMax-M2.7 Cookbook" icon="book-open" href="https://docs.sglang.io/cookbook/autoregressive/MiniMax/MiniMax-M2.7">
    查看完整硬件组合、配置参数和基准测试。
  </Card>

  <Card title="MiniMax-M2.7 模型仓库" icon="file-text" href="https://huggingface.co/MiniMaxAI/MiniMax-M2.7">
    查看模型卡、权重和 License。
  </Card>
</CardGroup>
