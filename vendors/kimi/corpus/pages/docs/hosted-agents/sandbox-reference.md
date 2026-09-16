> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 沙箱规格参考

> 托管智能体云沙箱的操作系统、预装运行时和工具、文件系统、访问权限及网络访问规则。

托管智能体的每个会话（Session）都使用独立的 **云沙箱**，智能体（Agent）在其中执行代码和读写文件。本页汇总沙箱的规格与使用边界，供你设计智能体时参考。如需配置预装依赖、网络访问策略和初始化脚本，请参阅 [执行环境（Environment）](/docs/hosted-agents/environments)。

<Info>
  每个会话使用独立沙箱，不与其他会话共享文件和进程状态。
</Info>

## 操作系统与预装软件

沙箱基于 **Debian 12（bookworm）** 镜像构建，预装常用的语言运行时、系统工具，以及文档和数据处理软件。

### 语言运行时

| 运行时     | 版本      | 附带的包管理工具   |
| ------- | ------- | ---------- |
| Python  | 3.12    | `pip`、`uv` |
| Node.js | 24      | `npm`      |
| .NET    | SDK 8.0 | `dotnet`   |
| Go      | 1.26    | `go`       |
| Rust    | 1.97    | `cargo`    |

<Note>
  上表列出的是主要版本，具体小版本号可能随镜像更新而变化。你也可以通过 [执行环境](/docs/hosted-agents/environments) 的 `packages` 字段，使用对应的包管理器安装额外依赖。
</Note>

### 系统工具

| 类别         | 预装工具                                                                                      |
| ---------- | ----------------------------------------------------------------------------------------- |
| 常用命令行      | `git`、`curl`、`wget`、`jq`、`tmux`、`vim`、`zip` / `unzip`、`rsync`、`tree`                      |
| 文档与 Office | LibreOffice、`pandoc`、`qpdf`、poppler-utils（`pdftotext` 等）、`wkhtmltopdf`、Tectonic（LaTeX 排版） |
| 媒体处理       | `ffmpeg`、Tesseract OCR（含英文识别包）                                                            |
| 浏览器        | Chromium（无头模式，供 PDF 渲染、图表截图等工具链使用）                                                        |
| 字体         | Noto CJK 等中英文字体，可直接用于文档和图片渲染                                                              |

### Python 包

<Accordion title="数据科学与可视化">
  `numpy`、`pandas`、`scipy`、`scikit-learn`、`statsmodels`、`lightgbm`、`sympy`、`networkx`、`matplotlib`、`plotly`、`seaborn`
</Accordion>

<Accordion title="文档与 PDF 处理">
  `python-docx`、`python-pptx`、`openpyxl`、`xlrd`、`xlsxwriter`、`pdfplumber`、`pypdf`、`pymupdf`、`pikepdf`、`reportlab`、`pdf2image`、`markitdown`、`beautifulsoup4`、`lxml`、`markdownify`
</Accordion>

<Accordion title="图像与视觉">
  `pillow`、`opencv-python-headless`、`scikit-image`、`imageio`、`pytesseract`、`onnxruntime`
</Accordion>

<Accordion title="地理空间与其他">
  `geopandas`、`shapely`、`pyproj`、`requests`、`jinja2`、`yfinance`、`backtrader`，以及 Jupyter 内核（`ipython` / `ipykernel`）
</Accordion>

### 通过 npm 全局安装的工具

`docx`、`pptxgenjs`、`pdf-lib`、`pdftk`、`md-to-pdf`、`@mermaid-js/mermaid-cli`（命令为 `mmdc`，Mermaid 图表渲染）、`sharp`（图像处理）等，可用于生成文档和幻灯片。

如果需要确认实际安装的版本，可以让智能体在沙箱中运行版本检查命令。常用命令包括 `python3 --version`、`node --version` 和 `pip list`。

## 文件系统布局

沙箱内 `/mnt` 下的挂载点按来源划分，访问权限各不相同：

| 路径                             | 内容                                                       | 访问权限                             |
| ------------------------------ | -------------------------------------------------------- | -------------------------------- |
| `/mnt/agents/`                 | **工作目录**：智能体在会话中默认使用的目录，用于保存代码、中间文件和产出文件                 | 读写                               |
| `/mnt/agents/upload/`          | 通过会话资源挂载的上传文件                                            | 只读                               |
| `/mnt/agents/memories/<name>/` | 绑定的 [记忆库](/docs/hosted-agents/memory)（Memory Store），每个记忆库一个目录 | 绑定时可选 `read_only` / `read_write` |
| `/mnt/agents/skills/<name>/`   | 智能体声明的 [技能](/docs/hosted-agents/skills)（Skill），随会话创建自动挂载      | 只读                               |
| `/mnt/agents/plugins/<name>/`  | [插件](/docs/hosted-agents/plugins)（Plugin）包含的技能与脚本，随会话创建自动挂载   | 只读                               |

### 只读与读写边界

**工作目录**：`/mnt/agents/` 是智能体在会话中默认使用的目录，用于保存代码、中间文件和产出文件。写入该目录的文件会同步到当前会话的持久化工作区；沙箱实例重建后，平台会重新挂载这些已同步的文件。不同会话之间不会共享工作目录。实例退出前尚未完成同步的最新写入可能丢失。会话结束后如需保留关键产物，请通过 [会话文件接口](/docs/hosted-agents/files) 取回，或使用 `save_artifact` 显式交付为不可变版本。

**只读挂载**：上传文件、技能和插件都以只读方式挂载。其中，技能和插件的内容在创建会话时确定；上传文件还可以在会话创建后通过 `POST /v1/sessions/{id}/resources` 追加挂载，详见[文件](/docs/hosted-agents/files)。智能体不能修改这些只读内容，也不应将产出写入相应目录。

**记忆库**：以 `read_write` 模式绑定记忆库后，智能体可以在对应目录中新增、修改和删除记忆文件，之后绑定同一记忆库的其他会话也能访问这些内容。以 `read_only` 模式绑定时，智能体不能修改记忆库内容。

<Warning>
  `/mnt/agents/upload/` 为只读目录。应让智能体把处理结果写入 `/mnt/agents/` 工作目录，而不要尝试直接修改上传文件。
</Warning>

## 沙箱网络边界

沙箱进程的出站网络访问由所属 [执行环境](/docs/hosted-agents/environments) 的 `networking` 配置决定。具体的网络模式、允许访问的主机和代理配置请参阅 [执行环境](/docs/hosted-agents/environments)。该配置只影响沙箱内进程，不影响平台层工具，例如 Web Search 和 Fetch。

## 相关资源

<CardGroup cols={3}>
  <Card title="执行环境" icon="layer-group" href="/docs/hosted-agents/environments">
    配置预装依赖、网络访问策略和初始化脚本。
  </Card>

  <Card title="文件" icon="file" href="/docs/hosted-agents/files">
    上传文件、挂载到会话并取回智能体产出。
  </Card>

  <Card title="记忆库" icon="database" href="/docs/hosted-agents/memory">
    以读写方式挂载记忆库，跨会话保存知识。
  </Card>

  <Card title="凭据库（Vault）" icon="key" href="/docs/hosted-agents/vaults">
    安全托管凭据，并按匹配规则注入或替换。
  </Card>

  <Card title="技能" icon="wand-magic-sparkles" href="/docs/hosted-agents/skills">
    管理技能版本，并以只读方式挂载技能。
  </Card>
</CardGroup>
