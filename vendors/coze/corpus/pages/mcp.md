> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

## 什么是 MCP？ {#hGJP9J9iV}

MCP（Model Context Protocol，模型上下文协议）是一种连接 Agent 与外部工具或服务的开放协议。为 Agent 添加 MCP 后，Agent 可以根据你的要求调用 MCP 提供的工具，完成查询信息、管理文件、操作第三方服务等任务。

例如，为 Agent 添加扣子文档 MCP 后，你可以让 Agent 查找、读取并整理扣子官方产品文档。

## 安全提示 {#hoFouyT2E}

:::warning 警告
MCP 服务由相应服务提供方提供和维护，其服务可用性、返回内容及数据处理方式由服务提供方负责，扣子仅提供相关服务的接入能力，不参与第三方 MCP 服务的实际运营，也无法控制其服务可用性、运行状态、返回内容及数据处理行为。

使用过程中，第三方 MCP 可能根据你的操作和授权，接收你发送给 Agent 的相关内容，并调用相应的第三方服务。添加或使用 MCP 前，请确认服务来源可信，充分了解相关服务的数据处理规则，并仔细核对授权范围和配置信息。
:::

## 限制说明 {#hZms4BEL2}

* 目前支持 Streamable HTTP 和 SSE 协议，暂不支持 STDIO 协议。
* 仅网页和桌面端支持创建自定义 MCP；移动端可以查看和使用已经添加的 MCP。
* 为 Agent 启用多个 MCP，可能影响工具选择和回复效果，并增加 Token 和积分消耗。建议每个 Agent 最多启用 10 个 MCP。详细说明可参考**常见问题**。

## 示例：连接并使用扣子文档 MCP {#hGPkmEB03}

下面以扣子官方文档 MCP 为例，介绍如何为 Agent 添加 MCP 并在对话中使用。扣子官方文档 MCP Server 是扣子提供的开发者专用知识库服务，为 Agent 添加扣子文档 MCP 之后，Agent 可以查看、检索最新的扣子官方文档，帮助用户快速了解产品功能和使用方法。

1. 获取扣子文档 MCP Server 地址。
   扣子官方文档的 MCP Server 的 HTTP URL 和 JSON 地址固定为：
   ```JSON
   {
     "mcpServers": {
       "扣子": {
         "url": "https://docs.coze.cn/topic-api/mcp"
       }
     }
   }
   ```
   你也可以在[扣子文档中心](https://docs.coze.cn/)任意页面顶部展开折叠菜单，选择**复制 MCP 配置**。
2. 连接 MCP。
   打开你和[扣子 Agent](https://www.coze.cn/overview/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=) 的对话页面，将 MCP 配置粘贴到输入框，并请扣子 Agent 帮你连接并安装。
   例如发送以下指令：
   ```Plain Text
   帮我连接并添加扣子产品文档 MCP
   {
     "mcpServers": {
       "扣子": {
         "url": "https://docs.coze.cn/topic-api/mcp"
       }
     }
   }
   ```
3. 验证 MCP。
   进入已添加该 MCP 的 Agent 对话，发送一条指令，验证 MCP 是否可用。
   ```Plain Text
   使用扣子文档 MCP 查找产品文档，总结一下会议旁听的功能怎么用？
   ```   


## 添加 MCP {#hAKP8WTvp}

### 从扣子 MCP 商店添加 MCP {#hd97zQsjF}

你可以从公共商店或当前企业、团队的 MCP 商店查找并添加 MCP。公共商店会展示 MCP 的介绍、可用工具和服务信息；企业或团队商店展示管理员或成员上架的 MCP。

1. 下载并安装[扣子桌面端](https://ugapk.com/FJvCs)，或访问[扣子网页端](https://www.coze.cn/overview/?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
2. 查找 MCP。
   从左侧导航栏进入**扩展 >** [MCP](https://www.coze.cn/skills?capability=mcp&tab=space?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)，浏览列表或搜索 MCP。你可以打开 MCP 详情页，查看可用工具、鉴权方式、连接信息和安全提示。
3. 连接 MCP。
   1. 单击 MCP 右侧的 **+**，或在详情页单击**连接**。
   2. （可选）根据页面提示完成第三方授权或填写连接凭证。
      无需鉴权的 MCP 可以直接添加。
4. 添加给 Agent。
   根据页面提示，选择一个或多个 Agent，然后确认添加。你也可以暂时跳过，MCP 会先保存到**我的 MCP**，后续你可以在这里按需为各个 Agent 添加这个 MCP。
5. 验证 MCP。
   连接完成后，向 Agent 发送一条指令，验证 MCP 是否可用。   


### 添加自定义 MCP {#hHqy4TmS5}

如果商店中没有需要的服务，你可以在桌面端或网页端使用 MCP JSON 添加自定义 MCP。添加前，请从可信来源获取完整配置，并确认其中的服务地址、命令和凭证安全。

1. 准备 MCP JSON。
   一个 MCP JSON 可以包含一个或多个 MCP Server。系统会分别识别其中的 Server，分别连接和添加 MCP。
2. 粘贴配置。
   从扣子左侧导航栏进入**扩展 >** [MCP](https://www.coze.cn/skills?capability=mcp&tab=space?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)，在页面右上角单击**添加自定义 MCP**，然后粘贴完整的 MCP JSON。
3. 设置 MCP 名称，并选择**添加到我的 MCP**。
   MCP 配置识别通过后，你可以确认或修改自动识别的名称。确认后将保存到「我的 MCP」，不会默认自动添加到 Agent 或上架企业商店。
4. 添加并绑定 Agent。
   进入我的 > [我的 MCP](https://www.coze.cn/skills?capability=mcp&tab=my)，点击指定的 MCP，展开 Agent 列表单击**添加**，将 MCP 添加给需要使用它的 Agent。
   你也可以从 **Agent 设置**页添加，或者在 Agent 对话中安装，MCP 会默认绑定当前 Agent。例如将扣子文档的 MCP 配置发送给扣子 Agent，用自然语言让它连接并安装。
   ![Image=366x255](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a785cccb61a64983b8ae6a9ebdf78d5b~tplv-goo7wpa0wc-topic.webp)   


## 在对话中使用 MCP {#hVBhCcNDz}

将 MCP 添加给 Agent 后，你只需在对话中说明要完成的任务，Agent 会根据你的意图自动选择并调用合适的 MCP。你也可以在指令中明确指定要使用的 MCP，帮助 Agent 更准确地选择工具。

**示例：**

```Plain Text
使用扣子官方文档 MCP，查找会议旁听的相关文档，并总结具体使用步骤。
```

## 管理我的 MCP {#hc89sBfud}

进入**我的 MCP**，可以查看当前账号已经添加的 MCP，并管理它们与 Agent 的关系。

<!-- @cols-width: 220,658 -->
| **操作**  | **说明**  |
| --- | --- |
| 为 Agent 添加已连接的 MCP  | 将同一个 MCP 添加给一个或多个 Agent，无需重复保存鉴权凭证。 | \
| | | \
| | 进入我的 > [我的 MCP](https://www.coze.cn/skills?capability=mcp&tab=my&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)，点击指定的 MCP，展开 Agent 列表单击**添加**。  |
| 启用或停用 MCP  | 控制指定 Agent 是否加载该 MCP。修改从下一轮对话开始生效。 | \
| | | \
| | 在 Agent 的设置 > 扩展能力 > MCP 页面中，开启或关闭某个 MCP 的开关。  |
| 为 Agent 移除 MCP  | 仅解除 MCP 与该 Agent 的绑定，不删除 MCP，也不影响其他 Agent。 | \
| | | \
| | 进入我的 > [我的 MCP](https://www.coze.cn/skills?capability=mcp&tab=my&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)，点击指定的 MCP，展开 Agent 列表单击**移除**。  |
| 删除 MCP  | 从当前账号删除 MCP，同时会解除它与你所有 Agent 的绑定。已上架到企业或团队商店的自定义 MCP，需要先下架。 | \
| | | \
| | 进入我的 > [我的 MCP](https://www.coze.cn/skills?capability=mcp&tab=my&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)，点击指定的 MCP，单击 **···** > **删除 MCP**。  |

## 将自定义 MCP 上架到企业/团队商店 {#hnt1I9U1r}

你可以将自己创建的自定义 MCP 提交到当前企业或团队的 MCP 商店，供其他成员安装。仅 MCP 的创建者可以提交；提交和上架管理仅支持 PC 端。

1. 发起上架。
   1. 进入**扩展 > 我的 >** [我的 MCP](https://www.coze.cn/skills?capability=mcp&tab=my&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)，找到要上架的自定义 MCP。
   2. 单击 **···** > **上架到企业/团队 MCP 商店**。
2. 填写上架信息。
   填写 MCP 图标和名称，检查 MCP JSON，并选择需要成员安装时自行填写的字段。
3. （可选）提交审核。
   确认服务来源和配置安全后提交审核。如果企业或团队开启了 MCP 审核，需要等待管理员审核通过。默认情况下未开启审核，MCP 会直接上架。
4. 管理已上架的 MCP。
   在**我的 MCP** 中打开该 MCP 的菜单，进入企业或团队上架管理。你可以查看详情、更新信息或下架 MCP。
   下架后，新成员不能再安装；已经安装的成员仍可继续使用。删除已上架的 MCP 前，必须先将它下架。   


## 热门 MCP 推荐 {#hzIYNiyHJ}

<!-- @cols-width: 293,533 -->
| **MCP**  | **适用场景**  |
| --- | --- |
| [麦当劳](https://www.coze.cn/skills?tab=space&capability=mcp&mcp_share_pid=7678651439413133363)  | 麦当劳中国远程服务，支持门店与营养查询、点餐下单、优惠券、活动日历、积分商城及主题活动预约。  |
| [Notion](https://www.coze.cn/skills?tab=space&capability=mcp&mcp_share_pid=7678651416155799598)  | Notion 托管 MCP 服务，用于搜索、读取和维护工作空间页面、数据库、评论与附件。  |
| [同花顺 iFinD·基金](https://www.coze.cn/skills?tab=space&capability=mcp&mcp_share_pid=7678651449542377482)  | 提供基金筛选、基本资料、行情业绩、持有人、组合配置及管理人数据查询。  |
| [GitHub](https://www.coze.cn/skills?tab=space&capability=mcp&mcp_share_pid=7678651422908383242)  | GitHub MCP 服务，为智能助手开放仓库、议题、拉取请求与代码协作能力。  |
| [滴滴出行](https://www.coze.cn/skills?tab=space&capability=mcp&mcp_share_pid=7678651395951591450)  | 滴滴 MCP 服务，提供叫车预估、订单处理、司机位置、地点搜索与多方式路线规划。  |
| [百度地图](https://www.coze.cn/skills?tab=space&capability=mcp&mcp_share_pid=7677966103808737289)  | 提供地理编码、地点检索、路线规划、天气和路况等地图能力。  |
| [天眼查](https://www.coze.cn/skills?tab=space&capability=mcp&mcp_share_pid=7678651461806440499)  | 提供企业主体识别、工商画像、集团关系、风险合规、知识产权及经营信息查询。  |
| [百度网盘](https://www.coze.cn/skills?tab=space&capability=mcp&mcp_share_pid=7678651447189454858)  | 让智能助手查询、整理、搜索、上传和分享百度网盘文件。  |
| [法研·法规知识库](https://www.coze.cn/skills?tab=space&capability=mcp&mcp_share_pid=7678651378096685083)  | 法研开放平台法规知识库 MCP 服务，支持按法律名称、条号或自然语言精准及并发检索法条。  |

## 常见问题 {#hJ4hAxbBM}

### 为什么已经添加 MCP，Agent 仍然不能使用？ {#hFAAZSHq7}

添加到**我的 MCP**不等于已经添加给 Agent。请进入**我的 MCP**或 Agent 设置页，确认 MCP 已与目标 Agent 绑定并启用。如果已经绑定，再检查连接状态和第三方服务权限。

### 为什么 MCP 显示“需重新连接”？ {#hDzfMpIun}

通常是连接凭证失效，或 MCP 的服务配置、鉴权方式发生了变化。单击**重新连接**，按照提示重新授权或填写凭证即可。原有 Agent 绑定关系会保留。

### 从 Agent 移除 MCP 和删除 MCP 有什么区别？ {#htzkHdjTV}

从 Agent 移除只会解除该 Agent 的绑定，不影响其他 Agent。删除 MCP 会从当前账号删除该 MCP，并解除它与你所有 Agent 的绑定。

### 企业或团队商店中的 MCP 下架后还能使用吗？ {#hSkkA6aRs}

已经安装的成员可以继续使用，新成员不能再安装。

### 为什么不建议给一个 Agent 启用过多 MCP？ {#hnmA7IdmR}

建议每个 Agent 最多启用 10 个 MCP。你也可以在对话前启用当前任务需要的 MCP，原因有两点：

* MCP 太多，更难选择合适的工具。每个 MCP 都会向 Agent 提供一组工具。启用的 MCP 越多，Agent 需要判断的工具就越多，可能选错工具或降低回复效果。
* **MCP 列表占用更多上下文。​**MCP 提供的工具名称、说明和参数等信息会作为上下文提供给模型。工具越多，占用的上下文越多，可能增加 Token 和积分消耗。

建议只启用当前任务需要的 MCP，不使用时可以先停用。
