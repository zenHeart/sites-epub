> ## Documentation Index
> Fetch the complete documentation index at: https://docs.bigmodel.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 异步解析

## 产品简介

智谱文件解析 API 是一款面向开发者和企业的统一文件解析解决方案，实现了多格式文件解析、智能内容抽取、灵活结果输出的一站式服务。

该 API 支持主流办公文档（`PDF、Word、Excel、PPT`）、结构化/非结构化数据文件（`CSV、MD、TXT`）以及多种图片格式（`JPG、PNG`等），能够**快速提取文件中的文本、表格、图片和版面结构**，生成标准化输出，便于直接接入下游业务系统或大模型处理链路。

## 应用场景

<Tabs>
  <Tab title="大模型前置解析">
    将PDF、Word、PPT等复杂文档解析为结构化文本或Markdown，减少手工清洗，直接作为大模型输入，提升问答与推理效果。

    **典型应用：** 智能问答系统、文档对话、内容生成等。
  </Tab>

  <Tab title="知识库构建管理">
    批量解析并标准化企业海量文档，形成结构化知识库，支持全文检索、语义搜索、知识问答等。

    **典型应用：** 企业内部知识管理、客服知识库、行业垂直知识图谱。
  </Tab>

  <Tab title="OCR识别及扫描件处理">
    对扫描版合同、财务报表、试卷、票据等非可编辑文件进行高精度识别，支持版面还原和图片提取。

    **典型应用：** 合同归档、档案数字化、试卷批改系统。
  </Tab>

  <Tab title="行业垂直解决方案">
    针对行业特定文档类型，提供高适配解析能力：

    * **教育行业：** 试题、讲义、教材解析入库
    * **金融行业：** 财报、招股书、研究报告结构化处理
    * **法律与合同管理：** 合同、协议、法律文书精确提取条款和内容
    * **出版与媒体：** 图文混排杂志、论文、新闻稿数字化处理
  </Tab>
</Tabs>

## 能力支持

<CardGroup cols={2}>
  <Card title="多样化解析能力整合" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/cubes.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=68f7e70811d7c842eb5b9d34c8ce53ec)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    一套API选择三种解析服务
  </Card>

  <Card title="多格式文件支持" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/images.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=5c7540ca4af57e6640b793cfd531ab54)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    涵盖主流文档及图片格式
  </Card>

  <Card title="多输出方式" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/arrows-rotate.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=2b334fa767b3736a3afc9babb9c6d575)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    • 下载链接：图片 + Markdown 文件 + 包含布局信息的json文件<br />
    • 纯文本：适配大模型输入
  </Card>

  <Card title="文件大小灵活支持" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/box.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=e306f71ed712216941329f8a99ee858a)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    不同服务最大可支持至 **100M** 文件
  </Card>

  <Card title="下载时效" icon={<svg style={{maskImage: "url(https://mintcdn.com/zhipu-ef7018ed/6jZAOYw-eXEZh1pv/resource/icon/clock.svg?fit=max&auto=format&n=6jZAOYw-eXEZh1pv&q=85&s=01942bdb6d8270b01215f52b5fe64363)", maskRepeat: "no-repeat", maskPosition: "center center",}} className={"h-6 w-6 bg-primary dark:bg-primary-light !m-0 shrink-0"}/>}>
    解析结果下载有效期 **24** 小时
  </Card>
</CardGroup>

## 解析服务对比

|    服务类型    | 支持格式                                                                                                                                              | 最大文件大小                                                                  | 解析结果                                        | 计费方式                                 | 核心优势                                                              |
| :--------: | :------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------- | :------------------------------------------ | :----------------------------------- | :---------------------------------------------------------------- |
|  **Prime** | pdf,docx,doc,xls<br />xlsx,ppt,pptx,png<br />jpg,jpeg,csv,txt<br />md,html,bmp<br />gif,webp,heic,eps<br />icns,im,pcx,ppm<br />tiff,xbm,heif,jp2 | PDF/DOC/DOCX/PPT ≤100MB<br />XLS/XLSX/CSV ≤10MB<br />PNG/JPG/JPEG ≤20MB | 图片 + Markdown 文件<br />+ 包含布局信息的<br />json文件 | 按解析页数消耗后付费<br />优惠后**0.12 元/页**      | - 适配双栏、混排、三栏等复杂版式<br />- 高精度解析图文、公式、表格等元素<br />- 多模态能力强，适合高要求解析场景 |
| **Expert** | pdf                                                                                                                                               | ≤100M                                                                   | 图片 + Markdown 文件                            | 按页数计费，限时 6 折优惠<br />优惠后**0.012 元/页** | - PDF、图片解析能力突出<br />- 表格与公式识别精度高<br />- 多领域表现稳定，兼顾精度与成本           |
|  **Lite**  | pdf,docx,doc,xls<br />xlsx,ppt,pptx,png<br />jpg,jpeg,csv,txt,md                                                                                  | ≤50M                                                                    | 纯文本（无图片）                                    | 按调用次数计费<br />**当前免费**                | - 支持常见办公文档解析<br />- 基础结构化能力完备，解析速度快<br />- 成本低，适合批量处理与轻量任务        |

### 解析耗时

解析时长与文档结构复杂度等因素密切相关，最终耗时以实际解析结果为准。

## 使用资源

[接口文档](/api-reference/%E5%B7%A5%E5%85%B7-api/%E6%96%87%E4%BB%B6%E8%A7%A3%E6%9E%90)：API 调用方式

**接口使用方法**

1. 调用接口创建解析任务，获取 `task_id`；
2. 保存并记录下 `task_id`；
3. 使用该 `task_id` 轮询查询接口，获取解析结果。

**字段属性**

| 字段名称         | 字段描述                                                                                                                                                        |
| :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| file         | 本地待解析文件                                                                                                                                                     |
| tool\_type   | 使用的解析工具类型: `lite, expert, prime`                                                                                                                            |
| file\_type   | 文件类型: `PDF, DOCX, DOC, XLS, XLSX, PPT, PPTX, PNG, JPG, JPEG, CSV, TXT, MD, HTML, EPUB, BMP, GIF, WEBP, HEIC, EPS, ICNS, IM, PCX, PPM, TIFF, XBM, HEIF, JP2` |
| taskId       | 文件解析任务 ID                                                                                                                                                   |
| format\_type | 结果返回格式类型: `text, download_link`                                                                                                                             |

## 调用示例

> 调用示例里面的参数属性参考上方字段属性和对应的 API 文档。

### 创建文件解析任务

<Tabs>
  <Tab title="cURL">
    **创建文件解析任务**

    ```bash theme={null}
    curl --location --request POST 'https://open.bigmodel.cn/api/paas/v4/files/parser/create' \
    --header  'Authorization: Bearer YOUR_API_KEY' \
    --form 'file=@example-file' \
    --form 'tool_type="prime"' \
    --form 'file_type="PDF"'
    ```

    **异步获取解析结果**

    ```bash theme={null}
    curl --request GET \
    --url https://open.bigmodel.cn/api/paas/v4/files/parser/result/{taskIid}/{format_type} \
    --header 'Authorization: Bearer YOUR_API_KEY'
    ```
  </Tab>

  <Tab title="Python">
    ```bash theme={null}
    # 安装最新版本
    pip install zai-sdk

    # 或指定版本
    pip install zai-sdk==0.2.3
    ```

    ```python theme={null}
    from zai import ZhipuAiClient

    client = ZhipuAiClient(api_key="YOUR_API_KEY")
    # 用于上传发起文件解析任务
    # 返回task_id
    response = client.file_parser.create(file=open('example.pdf', 'rb'), file_type='pdf', tool_type='lite')
    task_id = getattr(response, "task_id", None)

    # 获取文件内容抽取: format_type = text / download_link
    # text模式最长返回1m以内的文本内容，download_link响应更快
    res_response = client.file_parser.content(task_id=task_id, format_type="download_link")

    print(response.json())  # 新版推荐用法
    print(response.content.decode('utf-8')) # 旧版解码字节流用法依然支持
    ```
  </Tab>

  <Tab title="Python（旧）">
    **更新 SDK 至 2.1.5.20250825**

    ```bash theme={null}
    # 安装最新版本
    pip install zhipuai

    # 或指定版本
    pip install zhipuai==2.1.5.20250825
    ```

    ```python theme={null}
    from pathlib import Path
    from zhipuai import ZhipuAI

    client = ZhipuAI(api_key="YOUR_API_KEY")
    # 用于上传发起文件解析任务
    # 返回task_id
    response = client.file_parser.create(file=open('example.pdf', 'rb'), file_type='pdf', tool_type='lite')
    print(response)

    # 获取文件内容抽取
    response = client.file_parser.content(task_id="your task_id", format_type="text")
    print(response.content.decode('utf-8'))
    ```
  </Tab>

  <Tab title="Java">
    **安装 SDK**

    **Maven**

    ```xml theme={null}
    <dependency>
        <groupId>ai.z.openapi</groupId>
        <artifactId>zai-sdk</artifactId>
        <version>0.3.5</version>
    </dependency>
    ```

    ```java theme={null}
    import ai.z.openapi.ZhipuAiClient;
    import ai.z.openapi.service.fileparsing.FileParsingDownloadReq;
    import ai.z.openapi.service.fileparsing.FileParsingDownloadResponse;
    import ai.z.openapi.service.fileparsing.FileParsingResponse;
    import ai.z.openapi.service.fileparsing.FileParsingUploadReq;
    import ai.z.openapi.utils.StringUtils;

    public class FileParsingExample {

        public static void main(String[] args) {
            // 初始化客户端
            ZhipuAiClient client = ZhipuAiClient.builder().ofZHIPU()
                 .apiKey("YOUR_API_KEY")
                 .build();

            try {
                // 示例1: 创建解析任务
                System.out.println("=== 文件解析任务创建示例 ===");
                String filePath = "your file path";
                String taskId = createFileParsingTaskExample(client, filePath, "pdf", "lite");

                // 示例2: 获取解析结果
                System.out.println("\n=== 获取解析结果示例 ===");
                getFileParsingResultExample(client, taskId);

            } catch (Exception e) {
                System.err.println("发生异常: " + e.getMessage());
                e.printStackTrace();
            }
        }

        /**
        * 示例：创建解析任务（上传文件并解析）
        *
        * @param client ZhipuAiClient 实例
        * @return 解析任务的 taskId
        */
        private static String createFileParsingTaskExample(ZhipuAiClient client, String filePath, String fileType, String toolType) {
            if (StringUtils.isEmpty(filePath)) {
                System.err.println("无效的文件路径。");
                return null;
            }
            try {
                FileParsingUploadReq uploadReq = FileParsingUploadReq.builder()
                        .filePath(filePath)
                        .fileType(fileType)  // 支持: pdf, docx 等
                        .toolType(toolType) // 解析工具类型: lite, prime, expert
                        .build();

                System.out.println("正在上传并创建解析任务...");
                FileParsingResponse response = client.fileParsing().createParseTask(uploadReq);
                if (response.isSuccess()) {
                    if (null != response.getData().getTaskId()) {
                        String taskId = response.getData().getTaskId();
                        System.out.println("解析任务创建成功，TaskId: " + taskId);
                        return taskId;
                    } else {
                        System.err.println("解析任务创建失败: " + response.getData().getMessage());
                    }
                } else {
                    System.err.println("解析任务创建失败: " + response.getMsg());
                }
            } catch (Exception e) {
                System.err.println("文件解析任务错误: " + e.getMessage());
            }
            // 返回 null 表示创建失败
            return null;
        }

        /**
        * 示例：获取解析结果
        *
        * @param client ZhipuAiClient 实例
        * @param taskId 解析任务ID
        */
        private static void getFileParsingResultExample(ZhipuAiClient client, String taskId) {
            if (taskId == null || taskId.isEmpty()) {
                System.err.println("无效的任务ID，无法获取解析结果。");
                return;
            }

            try {
                int maxRetry = 100;      // 最多轮询100次
                int intervalMs = 3000;  // 每次间隔3秒
                for (int i = 0; i < maxRetry; i++) {
                    FileParsingDownloadReq downloadReq = FileParsingDownloadReq.builder()
                            .taskId(taskId)
                            .formatType("text")
                            .build();

                    FileParsingDownloadResponse response = client.fileParsing().getParseResult(downloadReq);

                    if (response.isSuccess()) {
                        String status = response.getData().getStatus();
                        System.out.println("当前任务状态: " + status);

                        if ("succeeded".equalsIgnoreCase(status)) {
                            System.out.println("解析结果获取成功！");
                            System.out.println("解析内容: " + response.getData().getContent());
                            System.out.println("内容下载链接: " + response.getData().getParsingResultUrl());
                            return;
                        } else if ("processing".equalsIgnoreCase(status)) {
                            System.out.println("解析进行中，请稍候...");
                            Thread.sleep(intervalMs);
                        } else {
                            System.out.println("解析任务异常，状态: " + status + "，消息: " + response.getData().getMessage());
                            return;
                        }
                    } else {
                        System.err.println("解析结果获取失败: " + response.getMsg());
                        return;
                    }
                }
                System.out.println("等待超时，请稍后自行查询解析结果。");
            } catch (Exception e) {
                System.err.println("获取解析结果时异常: " + e.getMessage());
            }
        }
    }
    ```
  </Tab>

  <Tab title="响应示例">
    **创建文件解析任务响应**

    ```
    {
        "message": "任务创建成功",
        "success": true,
        "task_id": "task_id"
    }
    ```

    **异步获取解析结果响应**

    ```
    {
        "status": "succeeded",
        "message": "结果获取成功",
        "content": "parsed result text",
        "task_id": "your task_id",
        "parsing_result_url": "download url"
    }
    ```
  </Tab>
</Tabs>

## 注意事项

* **文件大小限制：** 避免超出最大支持文件导致解析失败
* **优先选择适合场景的服务：** 复杂文档选择对应服务
* **下载结果后及时保存：** 下载链接 24 小时后失效
* **如需大模型处理：** 建议直接获取纯文本输出

## 常见问题

**Q：解析结果能保留原始图片吗？**

A：Prime 与 Expert 支持图片保留（打包下载），Lite 服务不保留图片。

**Q：下载链接失效怎么办？**

A：需重新调用解析API生成新链接。

**Q：为什么我的复杂 PDF 解析效果不好？**

A：Lite 服务不适合复杂排版和 OCR 场景，请使用 Prime 服务或 Expert 服务。
