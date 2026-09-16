> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 在 Playground 中配置 ModelScope MCP 服务器

> 在 Kimi Playground 中同步并启用 ModelScope 托管的 MCP 服务，让模型调用已配置的工具。

Kimi 开放平台与 ModelScope（魔搭）官方合作：在 Kimi Playground 中输入魔搭 API 令牌，即可一键同步账号下所有已配置托管的 MCP 服务。需要让 Playground 中的模型调用 MCP 工具时，按本页完成同步与启用即可。

## 同步魔搭托管的 MCP 服务

登录 Kimi Playground（[https://platform.kimi.com/playground），确保可以使用](https://platform.kimi.com/playground），确保可以使用) Kimi K2 模型进行基本对话。

MCP 服务在「MCP 服务器设置」中添加，Playground 默认已选中 ModelScope 作为 MCP 服务提供商。如果之前未使用过 ModelScope MCP 广场，先参考 [ModelScope 官方文档](https://modelscope.cn/mcp/kimi-playground) 选择并托管 MCP 服务；也可以在 ModelScope 社区发现海量 MCP 服务器。

### 打开 MCP 服务器设置

点击配置按钮，进入「MCP 服务器设置」：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/config.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=fc006cb865dabb5c768b3994d94937f8" alt="mcp-server-setting" width="1280" height="1210" data-path="assets/pics/modelscope/config.png" />

### 填入魔搭 API 令牌并同步

在弹出的面板中选择同步外部平台：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/syc.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=0df616e043a5211396fbed093511e032" alt="syc" width="1280" height="1038" data-path="assets/pics/modelscope/syc.png" />

API 令牌可在[魔搭首页-访问令牌](https://modelscope.cn/my/myaccesstoken)页面获取：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/get-keys.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=49ec6e6279e9ca620973394bd4aa586b" alt="keys" width="1280" height="1117" data-path="assets/pics/modelscope/get-keys.png" />

获取令牌后，粘贴到步骤 3 的空格中，点击「开始同步」：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/start-syc.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=8860fe307c651ba0dc3b403acc88038d" alt="start-syc" width="1280" height="1093" data-path="assets/pics/modelscope/start-syc.png" />

同步完成后，所有已配置连接的魔搭 Hosted MCP 服务会出现在 Kimi Playground 的可用 MCP 服务列表中：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/mcp-list.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=abb50a339f3dd82192b00c2de2c999d1" alt="mcp-list" width="1280" height="1151" data-path="assets/pics/modelscope/mcp-list.png" />

### 增量同步 MCP 服务

后续在 ModelScope MCP 广场新增或删除托管 MCP 服务后，在"设置-MCP 服务器-同步服务器"中点击同步按钮，即可增量更新：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/add-mcp.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=d1a9195291d0ba2382ec62095d9ad019" alt="add-mcp" width="1280" height="1058" data-path="assets/pics/modelscope/add-mcp.png" />

## 在对话中启用 MCP 服务

同步完成后，Kimi Playground 页面左侧会显示已导入的「MCP 服务列表」，在其中多选并启用本次对话需要使用的 MCP 服务：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/manage-mcp.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=c03d77ddcf9117e64a95a082663190ee" alt="manage-mcp" width="1280" height="1206" data-path="assets/pics/modelscope/manage-mcp.png" />

例如，在列表中启用高德地图相关的 MCP 服务，即可让助手帮你规划行程：

<img src="https://mintcdn.com/moonshotcn/3bxMseHtiQ3oOhqL/assets/pics/modelscope/maps.png?fit=max&auto=format&n=3bxMseHtiQ3oOhqL&q=85&s=639a21d90b7d21f5736bd5ce64a236da" alt="maps" width="1280" height="1234" data-path="assets/pics/modelscope/maps.png" />
