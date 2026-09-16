> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimaxi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 使用模板生成视频

> 使用视频模板进行视频生成服务，可将图片或文本等素材填充至预设的视频模板中，快速生成风格统一的视频。

## 工作流程

视频模板生成是一个异步接口，流程如下：

1. 创建视频模板生成任务：根据指定的 `template_id` 和填充的素材，创建一个生成任务，获得 `task_id`
2. 查询任务并获取结果：使用 `task_id` 轮询任务状态。与通用视频生成不同，当此任务完成时，API 会在响应中直接返回可供下载的 `video_url`

更多的视频模板，可参考[视频模板列表](/docs/faq/video-agent-templates)。

## 生成“绝地求生”风格视频

### 示例代码

```python theme={null}
import os
import time
import requests

api_key = os.environ["MINIMAX_API_KEY"]
headers = {"Authorization": f"Bearer {api_key}"}


# --- 步骤 1: 提交视频生成任务 ---
# 这个函数负责调用 API，根据指定的模板和素材，启动一个异步的视频生成任务。
# 任务提交成功后，API 会立即返回一个 task_id，用于后续查询任务状态。
def invoke_template_task() -> str:
    """提交一个基于模板的视频生成任务，并返回任务 ID"""
    url = "https://api.minimax.cn/v1/video_template_generation"
    payload = {
        # 'template_id' 指定了视频的基础模板。
        "template_id": "393769180141805569",  # 示例：绝地求生
        # 填充模板中的图片、视频等媒体素材
        "media_inputs": [
            {
                "value": "https://cdn.hailuoai.com/prod/2024-09-18-16/user/multi_chat_file/9c0b5c14-ee88-4a5b-b503-4f626f018639.jpeg"
            }
        ],
        # 用于填充模板中的文本素材
        "text_inputs": [{"value": "狮子"}],
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    task_id = response.json()["task_id"]
    return task_id


# --- 步骤 2: 轮询任务状态 ---
# 由于视频生成是异步的，我们需要通过上一步获取的 task_id 定期查询任务状态。
# 当状态变为 "Success"，函数会返回视频的 URL。如果失败，则会抛出异常。
def query_task_status(task_id: str):
    url = "https://api.minimax.cn/v1/query/video_template_generation"
    params = {"task_id": task_id}
    while True:
        # 建议设置合理的轮询间隔，避免过于频繁的请求。
        time.sleep(10)
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        response_json = response.json()
        status = response_json["status"]
        print(f"当前任务状态: {status}")
        if status == "Success":
            return response_json["video_url"]
        elif status == "Fail":
            raise Exception(f"视频生成失败: {response_json}")


# --- 步骤 3: 保存视频文件 ---
# 这是一个辅助函数，用于从给定的 URL 下载视频并保存到本地。
def save_video_from_url(video_url: str):
    print(f"正在从 {video_url} 下载视频...")
    response = requests.get(video_url)
    response.raise_for_status()
    with open("output.mp4", "wb") as f:
        f.write(response.content)
    print("视频已成功保存到 output.mp4")


# --- 主流程: 串联所有步骤 ---
# 按照“提交 -> 轮询 -> 保存”的顺序，执行视频生成的整个流程。
if __name__ == "__main__":
    task_id = invoke_template_task()
    print(f"已成功提交视频生成任务，task_id: {task_id}")
    final_video_url = query_task_status(task_id)
    print(f"任务成功，视频 URL: {final_video_url}")
    save_video_from_url(final_video_url)
```

### 生成结果

<video controls src="https://filecdn.minimax.chat/public/92ed8c3b-8173-4ed6-86e3-7860fecb2c7c.mp4" />

> 绝地求生
