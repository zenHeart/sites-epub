> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 静态托管 CLI 与 MCP

> 使用 steppage CLI 或 Page MCP Server 部署和管理静态网站

本指南面向在**生产环境**使用 StepFun 静态托管的开发者与 CI 集成方，覆盖 `steppage` 命令行工具（CLI）与 Page MCP Server 两种接入方式。二者共用同一把 `sk-` 托管密钥：CLI 面向人工操作与 CI/CD 流水线，MCP 面向 Claude 等 MCP 客户端、由模型直接调用。当前版本 1.0.0。

## 准备工作

两种方式都要求本机已安装 **Node.js 20 或更高版本**（安装脚本会做校验，低于 20 直接报错退出）。同时需要一把以 `sk-` 开头的 Page 托管 API Key，可在[阶跃星辰开放平台](https://platform.stepfun.com)控制台获取；CLI 与 MCP 都用这把 Key 认证，认证后仅能访问该 Key 拥有的站点。

## steppage CLI

### 安装

生产渠道通过 curl 一键脚本安装，脚本会下载自包含独立产物到 `~/.steppage/bin/`，并在 `~/.local/bin/steppage` 写入可执行包装器：

```bash theme={null}
curl -fsSL https://dl.stepfun.com/steppage-cli/p/install.sh | bash
```

如需固定到某个版本，在命令前加 `VERSION` 环境变量（默认 `latest`）：

```bash theme={null}
VERSION=v1.0.0 curl -fsSL https://dl.stepfun.com/steppage-cli/p/install.sh | bash
```

若安装后提示 `~/.local/bin` 不在 PATH 中，将下面一行加入 shell 配置（如 `~/.zshrc`）后重开终端：

```bash theme={null}
export PATH="$HOME/.local/bin:$PATH"
```

验证安装：`steppage --version`；查看全部命令：`steppage --help`。

### 认证

推荐先登录一次，校验并保存密钥。`login` 会向服务端探测身份，成功后把密钥写入 `~/.steppage/config.json`（文件权限 600）：

```bash theme={null}
steppage login --key sk-xxxxxxxx
steppage whoami   # 打印当前 key 对应的 uid
steppage logout   # 清除已保存的 key
```

在 CI 等无状态环境中可跳过 `login`，直接用环境变量 `STEPFUN_API_KEY` 提供密钥，所有命令都会自动读取。

### 快速开始：部署一个目录

一条 `deploy` 命令即可完成「构建产物 → 上传 → 发布版本」。首次部署用 `--name` 新建站点，加 `--go-live` 在发布同时上线：

```bash theme={null}
steppage deploy ./dist --name my-site --go-live
```

向**已有**站点发布新版本则用 `--site <id>`。`deploy` 接受一个目录（递归扫描）或单个 `.zip`。产物根目录若无 `index.html`，需用 `--root <file>` 指定站点首页，或用 `--no-root-page` 声明不提供首页；交互终端下会提示选择根文件，CI（非 TTY）下则直接报错要求显式传参。

### 命令参考

| 命令               | 说明                         | 关键参数                                                                   |
| ---------------- | -------------------------- | ---------------------------------------------------------------------- |
| `login`          | 校验并保存托管 API key            | `--key sk-...`（不填则交互输入）                                                |
| `logout`         | 清除已保存的 API key             | —                                                                      |
| `whoami`         | 打印当前 key 对应身份              | —                                                                      |
| `deploy <path>`  | 构建产物并发布                    | `--site`、`--name`、`--root`、`--no-root-page`、`--go-live`                |
| `list`           | 列出你的站点                     | —                                                                      |
| `get`            | 查看单个站点                     | `--site`（必填）                                                           |
| `update`         | 重命名站点或修改服务模式               | `--site`（必填）、`--name`、`--serving-mode`（可选值为 `spa` 或 `static`，后两者至少填一个） |
| `delete`         | 删除站点（不可逆）                  | `--site`（必填）、`--yes`（跳过确认；非 TTY 必填）                                    |
| `versions`       | 列出站点版本                     | `--site`（必填）                                                           |
| `promote`        | 将暂存版本上线                    | `--site`、`--version`（必填）                                               |
| `rollback`       | 回滚到较旧版本                    | `--site`、`--version`（必填）                                               |
| `preview mint`   | 获取或创建某版本的持久预览链接            | `--site`、`--version`（必填）                                               |
| `preview expiry` | 设置或清除预览链接过期时间              | `--site`、`--version`、`--expires`（可设为 `never`、小时数或天数，例如 `24h`、`7d`）     |
| `preview revoke` | 撤销某版本的预览链接                 | `--site`、`--version`（必填）                                               |
| `config --show`  | 打印解析后的环境、是否已配置 key 及配置文件路径 | —                                                                      |

**全局选项**（可用于任意命令）：`--json` 让命令在 stdout 输出机读 JSON（错误仍走 stderr），便于 CI 解析；`-H, --header "Name: value"` 注入自定义 HTTP 请求头，可重复；`-v, --version` 打印版本。

### 典型工作流

\*\*预发布再上线。\*\*先发布但不上线，取预览链接验收，确认无误后再上线：

```bash theme={null}
steppage deploy ./dist --site 123                # 发布新版本（不上线）
steppage preview mint --site 123 --version 456   # 取预览链接验收
steppage promote --site 123 --version 456        # 验收通过后上线
```

\*\*回滚。\*\*线上版本出问题时，回滚到历史版本：

```bash theme={null}
steppage versions --site 123                  # 查历史版本
steppage rollback --site 123 --version 400    # 回滚到指定版本
```

\*\*CI 集成。\*\*流水线中设置 `STEPFUN_API_KEY` 免登录，并加 `--json` 解析结果：

```bash theme={null}
export STEPFUN_API_KEY=sk-xxxxxxxx
steppage deploy ./dist --site 123 --go-live --json
```

`promote`、`rollback` 会改变线上版本，`delete` 不可逆。`delete` 在交互终端下需输入站点名二次确认，在无 TTY 的 CI 中必须显式加 `--yes` 才会执行。

## Page MCP Server

MCP Server 把上述部署、上线、回滚、巡检能力封装成 MCP 工具，供 Claude 等客户端由模型直接调用。它以 stdio 方式运行，**纯环境变量认证**（不读写任何配置文件），与 CLI 使用同一把 `sk-` 密钥。

### 安装

```bash theme={null}
curl -fsSL https://dl.stepfun.com/steppage-mcp/p/install.sh | bash
```

同样支持 `VERSION=v1.0.0` 固定版本。脚本安装产物到 `~/.steppage-mcp/bin/`，并在 `~/.local/bin/steppage-mcp` 写入包装器——这个路径就是要填给 MCP 客户端的命令。

### 配置 MCP 客户端

在客户端的 MCP 配置中，把 `command` 指向安装好的包装器，并通过 `env` 传入密钥。以 Claude 为例：

```json theme={null}
{
  "mcpServers": {
    "steppage": {
      "command": "/Users/<you>/.local/bin/steppage-mcp",
      "env": {
        "STEPFUN_API_KEY": "sk-xxxxxxxx"
      }
    }
  }
}
```

把 `<you>` 换成你的用户名（用绝对路径最稳妥）。`STEPFUN_API_KEY` 是唯一必填认证项。

### 工具参考

| 工具                    | 说明                                         | 关键参数                                                         |
| --------------------- | ------------------------------------------ | ------------------------------------------------------------ |
| `page_deploy`         | 构建并发布本地目录 / .zip，返回预览 URL（goLive 时附线上 URL） | `path`（必填）、`site`、`name`、`root`、`noRootPage`、`goLive`        |
| `page_list_sites`     | 列出当前 key 拥有的站点                             | —                                                            |
| `page_get_site`       | 查看单个站点                                     | `site`（必填）                                                   |
| `page_update_site`    | 重命名站点或修改服务模式                               | `site`（必填）、`name`、`servingMode`（可选值为 `spa` 或 `static`）       |
| `page_delete_site`    | 永久删除站点（不可逆）                                | `site`（必填）                                                   |
| `page_list_versions`  | 列出站点版本                                     | `site`（必填）                                                   |
| `page_promote`        | 将暂存版本上线                                    | `site`、`version`（必填）                                         |
| `page_rollback`       | 回滚到较旧版本                                    | `site`、`version`（必填）                                         |
| `page_inspect`        | 查看服务配置（含 header 规则）与版本列表                   | `site`（必填）                                                   |
| `page_preview_mint`   | 获取或创建持久预览链接                                | `site`、`version`（必填）                                         |
| `page_preview_expiry` | 设置或清除预览链接过期时间                              | `site`、`version`、`expires`（可设为 `never`、小时数或天数，例如 `24h`、`7d`） |
| `page_preview_revoke` | 撤销预览链接                                     | `site`、`version`（必填）                                         |
| `page_whoami`         | 查看当前 key 对应身份                              | —                                                            |

说明：ID 类参数均为数值型字符串，工具内部做了 bigint 安全处理；多文件产物若无 `index.html`，`page_deploy` 需传 `root` 或 `noRootPage`（MCP 无交互提示）。`page_promote`、`page_rollback`、`page_delete_site` 为破坏性操作，调用前请确认。

## 环境变量与语言

| 变量                 | 适用        | 说明                                      |
| ------------------ | --------- | --------------------------------------- |
| `STEPFUN_API_KEY`  | CLI + MCP | `sk-` 托管密钥。CLI 可用它免 `login`；MCP 的唯一认证方式 |
| `STEPPAGE_OVERSEA` | CLI + MCP | 设为真值时输出英文（海外）；默认中文（国内）。安装脚本已按区域预置默认值    |
| `VERSION`          | 安装脚本      | 固定安装版本，如 `v1.0.0`；默认 `latest`           |

## 故障排查

| 现象                            | 处理                                                                    |
| ----------------------------- | --------------------------------------------------------------------- |
| 安装报 Node 版本过低或找不到 node        | 安装 / 升级到 Node.js 20+ 后重跑脚本                                            |
| `steppage: command not found` | `~/.local/bin` 未在 PATH：加 `export PATH="$HOME/.local/bin:$PATH"` 并重开终端 |
| API key 被服务器拒绝                | 确认 key 以 `sk-` 开头且有效；重新 `login` 或检查 `STEPFUN_API_KEY`                 |
| 部署报缺少 index.html              | 用 `--root <file>` 指定首页，或 `--no-root-page` 声明不提供首页                     |
| CI 中 delete 无反应 / 报错          | 非 TTY 环境删除必须加 `--yes`                                                 |
