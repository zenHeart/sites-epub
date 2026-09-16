> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# AI 播客生成：多模态 AI 应用实战

> <Note> 本教程将带您使用 MiniMax 语音模型 & 语言模型  构建一个完整的 AI 播客生成应用，实现从用户输入到播客成品的全流程自动化。 </Note>

<div style={{display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px'}}>
  <div style={{width: '40px', height: '40px', borderRadius: '50%', background: 'linear-gradient(135deg, #f59e0b, #ef4444)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'white', fontWeight: 'bold'}}>M</div>

  <div>
    <div style={{fontWeight: 500}}>Meepo</div>
    <div style={{fontSize: '0.875rem', color: '#9ca3af'}}>2026年1月25日</div>
  </div>
</div>

<a href="https://github.com/MiniMax-OpenPlatform/minimax_aipodcast" target="_blank" style={{display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '8px 16px', borderRadius: '8px', border: '1px solid #e5e7eb', textDecoration: 'none', color: 'inherit', marginBottom: '24px'}}>
  <svg height="20" width="20" viewBox="0 0 16 16" fill="currentColor">
    <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z" />
  </svg>

  Download from GitHub
</a>

**AI 播客生成方案**通过集成 MiniMax 多模态模型，实现从用户输入需求到播客成品的**全流程自动化**。

👉 [在线体验](https://solution.minimaxi.com/minimax-aipodcast)

<Columns cols={4}>
  <Card title="语言模型" icon="file-text">
    播客脚本
  </Card>

  <Card title="语音合成" icon="volume-2">
    TTS 音频
  </Card>

  <Card title="语音克隆" icon="mic">
    自定义音色
  </Card>

  <Card title="文生图" icon="image">
    播客封面
  </Card>
</Columns>

***

## 效果演示

<video controls className="audio-container" src="https://filecdn.minimax.chat/public/11f624b3-7607-438d-abde-fbe352ad580d.mp3" />

<Columns cols={2}>
  <img src="https://filecdn.minimax.chat/public/f64e4f2b-1bfa-4769-a407-e83fec73dd90.png" alt="前端界面" style={{borderRadius: '8px', width: '100%'}} />

  <img src="https://filecdn.minimax.chat/public/6e7dbc2d-f911-4f49-9fcb-67c3404504d5.png" alt="执行结果" style={{borderRadius: '8px', width: '100%'}} />
</Columns>

***

## 核心特点

<AccordionGroup>
  <Accordion title=" 多种内容输入方式">
    支持**话题文本、URL、PDF** 三种方式输入，基于 BeautifulSoup 和 PyPDF2 进行网页和 PDF 的解析，提取文本内容作为 LLM 生成播客内容的依据。
  </Accordion>

  <Accordion title=" 灵活的音色选择">
    提供多种音色选择方案：使用预设的默认音色、输入 voice\_id 选取自定义音色，或直接上传音频来复刻说话者的音色。
  </Accordion>

  <Accordion title=" 双主播对话生成">
    支持两个播音员角色，先分别生成各自的语句音频，再用 FFmpeg 将音频智能合并，形成自然的对话节奏。
  </Accordion>

  <Accordion title=" 自动生成播客封面">
    先用语言模型基于播客内容生成封面图制作的 prompt，再用该 prompt 生成精美的播客封面图。
  </Accordion>
</AccordionGroup>

***

## 快速上手

<Steps>
  <Step title="克隆仓库">
    ```bash theme={null}
    git clone -b main https://github.com/MiniMax-OpenPlatform/minimax_aipodcast.git
    cd minimax_aipodcast
    ```
  </Step>

  <Step title="安装依赖">
    **安装 FFmpeg**（用于音频处理）：

    <Tabs>
      <Tab title="macOS">
        ```bash theme={null}
        brew install ffmpeg
        ```
      </Tab>

      <Tab title="Windows/Linux">
        通过 [FFmpeg 官网](https://ffmpeg.org/download.html) 下载并安装
      </Tab>
    </Tabs>

    **安装项目依赖**：

    ```bash theme={null}
    pip install -r requirements.txt
    cd frontend && npm install
    ```
  </Step>

  <Step title="一键启动">
    ```bash theme={null}
    chmod +x start.sh  # 初次使用时执行
    ./start.sh
    ```
  </Step>
</Steps>

***

## 核心 API 详解

<Tabs>
  <Tab title="语言模型">
    使用 MiniMax 语言模型生成播客内容脚本。

    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.minimax.cn/v1")

    response = client.chat.completions.create(
        model="MiniMax-M2.1",
        messages=[
            {"role": "system", "content": "你是一个专业的播客脚本编写助手。"},
            {"role": "user", "content": "<Your_Prompt>"}
        ]
    )

    script = response.choices[0].message.content
    ```

    <Note>
      建议使用 [OpenAI 兼容接口](/docs/api-reference/text-openai-api) 或 [Anthropic 兼容接口](/docs/api-reference/text-anthropic-api)。
    </Note>
  </Tab>

  <Tab title="语音合成">
    使用 MiniMax Speech 2.8 模型生成播客音频。

    ```python theme={null}
    import requests

    response = requests.post(
        "https://api.minimax.cn/v1/t2a_v2",
        headers={
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json"
        },
        json={
            "model": "speech-2.8-hd",
            "text": "您好，这是 MiniMax TTS 合成的语音。",
            "stream": False,
            "voice_setting": {
                "voice_id": "Chinese (Mandarin)_Gentle_Senior",
                "speed": 1,
                "emotion": "happy"
            },
            "audio_setting": {
                "sample_rate": 32000,
                "format": "mp3"
            }
        }
    )

    audio_hex = response.json()["data"]["audio"]
    ```

    | 参数         | 说明                       |
    | ---------- | ------------------------ |
    | `model`    | 推荐 `speech-2.8-hd`       |
    | `voice_id` | 系统预设或自定义音色 ID            |
    | `emotion`  | 情感参数：happy, sad, angry 等 |
  </Tab>

  <Tab title="语音克隆">
    上传参考音频，创建自定义音色。

    ```python theme={null}
    import requests

    # Step 1: 上传复刻音频
    upload_resp = requests.post(
        "https://api.minimax.chat/v1/files/upload",
        headers={"Authorization": "Bearer YOUR_API_KEY"},
        files={'file': ('ref.wav', open('ref.wav', 'rb'), 'audio/wav')},
        data={'purpose': 'voice_clone'}
    )
    file_id = upload_resp.json()["file"]["file_id"]

    # Step 2: 克隆音色
    clone_resp = requests.post(
        "https://api.minimax.chat/v1/voice_clone",
        headers={
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json"
        },
        json={
            "file_id": file_id,
            "voice_id": "my_custom_voice",
            "model": "speech-02-turbo"
        }
    )
    ```

    <Tip>
      参考音频要求：清晰人声，时长 10s-5min（建议 15 秒），支持 wav/mp3/m4a 格式。
    </Tip>
  </Tab>

  <Tab title="文生图">
    生成精美的播客封面图。

    ```python theme={null}
    import requests

    response = requests.post(
        "https://api.minimax.cn/v1/image_generation",
        headers={
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json"
        },
        json={
            "model": "image-01-live",
            "prompt": image_prompt,
            "aspect_ratio": "1:1",
            "response_format": "url",
            "style": {"style_type": "漫画", "style_weight": 1}
        }
    )

    image_url = response.json()["data"]["image_urls"][0]
    ```

    <Warning>
      返回图片的 URL 有效期为 **24 小时**，请及时下载保存。
    </Warning>
  </Tab>
</Tabs>

***

## 实用技巧

| 场景   | 建议                                                                                                  |
| ---- | --------------------------------------------------------------------------------------------------- |
| 音色试听 | 使用 [语音调试台](https://platform.minimaxi.com/examination-center/voice-experience-center/t2a_v2) 试听并选择音色 |
| 模型选择 | `speech-2.8-hd` 自然度最高；`speech-2.8-turbo` 生成速度快                                                      |
| 语音克隆 | 上传音频时长建议 **15 秒左右**，效果更佳                                                                            |

***

## 应用拓展

<Columns cols={2}>
  <Card title="多角色播客" icon="users">
    支持多角色灵活对话，无固定发言顺序
  </Card>

  <Card title="实时信息增强" icon="search">
    加入搜索能力，提供最新消息
  </Card>

  <Card title="多语言播客" icon="globe">
    接入翻译能力，生成多语言版本
  </Card>

  <Card title="情感控制" icon="heart">
    利用情感参数，丰富表现力
  </Card>
</Columns>

***

## 总结

本教程展示了如何使用 **MiniMax 多模态 AI 能力**构建完整的 AI 播客生成应用。通过集成文本生成、TTS 语音合成、语音克隆、文生图四大核心能力，实现了从用户输入到播客成品的全流程自动化。

开发者可以基于本项目的架构思路，将 AI 能力组合成更多创新应用。

***

## 相关资源

<Columns cols={3}>
  <Card title="TTS API" icon="volume-2" href="/docs/api-reference/speech-t2a-http">
    语音合成接口
  </Card>

  <Card title="语音克隆" icon="mic" href="/docs/api-reference/voice-cloning-clone">
    音色克隆接口
  </Card>

  <Card title="文生图" icon="image" href="/docs/api-reference/image-generation-t2i">
    图像生成接口
  </Card>
</Columns>
