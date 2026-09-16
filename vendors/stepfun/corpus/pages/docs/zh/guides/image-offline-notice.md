> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 图像模型下线公告

`step-2x-large`、`step-image-edit-2` 将于 **2026 年 10 月 10 日** 下线；`step-1x-edit` 目前已不支持调用。2026 年 10 月 10 日起，文生图、图生图、图片编辑三类接口将在国内和海外同步停止服务，继续调用的业务将无法正常返回结果。

<Warning>
  请在 **2026 年 10 月 10 日** 前完成相关业务的调整，保障线上服务稳定运行。
</Warning>

## 下线信息

| 项目   | 内容                                                                                  |
| ---- | ----------------------------------------------------------------------------------- |
| 下线时间 | 2026 年 10 月 10 日                                                                    |
| 影响范围 | 国内、海外同步下线                                                                           |
| 涉及模型 | `step-2x-large`、`step-image-edit-2`（2026 年 10 月 10 日前仍可调用）；`step-1x-edit`（目前已不支持调用） |
| 涉及能力 | 文生图、图生图、图片编辑                                                                        |

## 下线接口及影响

以下开放平台 API 和 Step Plan 图像接口将于 **2026 年 10 月 10 日** 在国内和海外同步停止服务：

| 服务        | 能力   | 请求方式 | 接口路径                               |
| --------- | ---- | ---- | ---------------------------------- |
| 开放平台 API  | 文生图  | POST | `/v1/images/generations`           |
| 开放平台 API  | 图生图  | POST | `/v1/images/image2image`           |
| 开放平台 API  | 图片编辑 | POST | `/v1/images/edits`                 |
| Step Plan | 文生图  | POST | `/step_plan/v1/images/generations` |
| Step Plan | 图片编辑 | POST | `/step_plan/v1/images/edits`       |

* **开放平台 API 和 Step Plan**：上述图像接口在国内和海外同步停止服务。Step Plan 的文本、推理、语音与智能路由等其余模型不受影响，详见[图像模型接入](/docs/zh/step-plan/integrations/image-api)。
* **Studio**：生图能力将不再提供。

## 常见问题

<AccordionGroup>
  <Accordion title="下线前这些模型还能调用吗？">
    `step-2x-large` 和 `step-image-edit-2` 在 **2026 年 10 月 10 日** 前仍可调用；`step-1x-edit` 目前已不支持调用。2026 年 10 月 10 日起，开放平台 API 和 Step Plan 图像接口将停止服务，继续调用将无法正常返回结果。
  </Accordion>

  <Accordion title="step-1x-edit 现在还能调用吗？">
    不能。`step-1x-edit` 目前已不支持调用；2026 年 10 月 10 日前仍可调用 `step-2x-large`、`step-image-edit-2`。
  </Accordion>

  <Accordion title="已经生成的图片链接还能访问吗？">
    图片下载链接本身存在有效期限制，与本次下线无关。建议将需要长期保留的图片及时下载并存储到您自己的存储服务。
  </Accordion>
</AccordionGroup>

如有疑问，可通过[联系我们](/docs/zh/guides/contact-us)获取支持。
