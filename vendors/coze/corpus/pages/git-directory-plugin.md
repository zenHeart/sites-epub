> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

Git 目录插件可以帮你把 Agent 或项目的工作目录纳入 Git 版本管理。开启后，你可以追踪文件变更、提交版本记录，并在需要时回溯到历史版本。

## 什么时候使用 Git 目录插件 {#hMJJHSrX0}

当 Agent 需要在本地电脑和云端环境之间切换，或编程项目需要持续迭代时，建议使用 Git 目录插件。

编程项目通常会生成 `node_modules`、构建产物、缓存文件等大量临时文件。这类文件不适合反复通过云盘同步，建议只用 Git 管理源码和配置文件，依赖安装与编译过程留在当前运行环境中完成。

## 能做什么 {#hATQliznM}

Git 目录插件支持：

* **开启 Git 管理**：为当前工作目录初始化 Git，并绑定到 Git Server。
* **同步代码变更**：在本地电脑、云端环境之间同步编程项目文件。
* **提交版本记录**：将当前改动保存为一次提交，方便后续查看和回溯。
* **拉取远端更新**：从 Git Server 获取最新文件，继续在当前环境中工作。

## 选择 Git Server 类型 {#hJtSzKKYh}

你可以选择将目录绑定到扣子云端 Git Server，或绑定到自己的 GitHub 仓库。

* **扣子云端 Git Server**：默认方式。你无需提前准备仓库，开启 Git 管理后，系统会将目录绑定到扣子提供的云端 Git Server。扣子云端 Git Server 暂不提供独立管理页面。
* **GitHub 仓库**：如果你希望代码同步到自己的仓库，可以绑定到 GitHub 仓库。

## 注意事项 {#hmiRzT8yQ}


* Git 目录适合管理编程项目文件，不建议放入过大的临时文件或构建产物。
* 如果目录中存在密钥、Token、账号信息等敏感内容，建议先移除，再开启 Git 管理。
* 多人协作时，建议在提交前先查看改动，确认没有覆盖他人的修改。
* 绑定 Git Server 后，暂不支持解绑。

## 使用前准备 {#hlIJB0NV6}

根据你选择的 Git Server，提前完成如下操作：

* **扣子 Git Server**：需要先购买一台云电脑。具体操作，请参考【云电脑】。
* **GitHub 仓库**：需要准备一个可用的 GitHub 仓库，以及用于访问该仓库的 Personal Access Token（PAT）。PAT 属于敏感凭证，请妥善管理。

## 绑定扣子 Git Server {#heMJT5J74}

你可以让 Agent 为指定的工作文件夹开启 Git 管理。默认情况下，工作文件夹会绑定到扣子提供的云端 Git Server。

你可以通过如下两种方式绑定扣子 Git Server。

::::cols
@col 50
一键开启

在 Agent 的工作目录中找到目标文件夹，单击··· > **使用 Git 管理**，然后在确认框中，再次单击**使用 Git 管理**。系统会自动在对话中向 Agent 发送开启 Git 管理的指令。

![Image=2278x1682](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d611abe6327640a2b1894a7119c4c0f3~tplv-goo7wpa0wc-topic.webp)

@col 50
在对话中发送指令

你也可以直接在对话中告诉 Agent 要为哪个目录开启 Git 管理。

例如你可以说：

```Plain Text
为 travel-guide 开启 git 管理
```


::::

Agent 会帮你完成以下操作：

1. 检查当前工作目录。
2. 初始化 Git 目录。
   Git Server 会部署在你已购买的云电脑中。
3. 将目录绑定到扣子云端的 Git Server。
4. 后续文件变更会进入 Git 管理范围。

开启 Git 管理后，该文件夹会显示 **Git 目录**标识，并不再支持在 Agent 的工作目录中直接查看文件内容。后续需要通过 Git 的 **pull** 和 **push** 操作同步文件；如需查看具体内容，可以让 Agent 拉取后再展示。

![Image=350x278](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/df9eade3accb4347a5dced06acc9794f~tplv-goo7wpa0wc-topic.webp)

## 绑定 Github 仓库 {#hO6lcudfb}

默认情况下，开启 Git 管理后，会默认绑定到扣子提供的云端 Git Server。你也可以指定绑定到自己的 Github 仓库。

你可以说：

```Plain Text
把 image 文件夹同步到 GitHub 仓库 https://github.com/<YOUR_GITHUB_NAME>/<YOUR_REPO_NAME>。
```

Agent 会根据你的指令完成后续操作：

1. 检查 `image` 文件夹是否适合开启 Git 管理。
2. 引导你提供要绑定的 GitHub 仓库地址。
3. 引导你创建 Personal Access Token（PAT）。
4. 将 `image` 文件夹初始化为 Git 目录，并绑定到对应仓库。
5. 提交当前文件，并推送到 GitHub。
   ::::cols
   @col 50
   ![Image=310x176](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/00f588dc6e864fe1b5c70546453f52c8~tplv-goo7wpa0wc-topic.webp)
   
   @col 50
   ![Image=2504x840](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b67cb792087347f58ccede48be63d153~tplv-goo7wpa0wc-topic.webp)
   ::::   


## Pull 和 Push 操作 {#hiP91W1Qj}

开启 Git 管理后，文件同步主要通过 **Pull** 和 **Push** 完成。

* **Pull**：从远程仓库拉取最新内容到当前工作目录。比如协作者在 GitHub 上提交了更新，你可以让 Agent 拉取最新代码后继续开发。
* **Push**：将已提交的文件版本推送到远程仓库。比如 Agent 完成一次修改并提交后，你可以让它把代码推送到扣子 Git Server 或 GitHub 仓库。

::::cols
@col 50
Pull 操作

![Image=1960x1382](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/50df1b8843bd4fcb94a9f8890f18da73~tplv-goo7wpa0wc-topic.webp)

@col 50
Push 操作

![Image=1986x1264](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0f165102ae19436ab6869730bd655c58~tplv-goo7wpa0wc-topic.webp)
::::
