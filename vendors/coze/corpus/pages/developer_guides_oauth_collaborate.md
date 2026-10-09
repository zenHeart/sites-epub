> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程支持多人协作场景下跨账号的 OAuth 授权，组织超级管理员可以为应用程序授予工作空间中的资源权限。

:::tip 说明
仅扣子企业版（企业标准版、企业旗舰版）支持多人协作场景，扣子个人版不支持多人协作场景。
:::

## 授权场景 {#f8ec739f}

使用[OAuth 授权码授权](/developer_guides/oauth_code)、[OAuth PKCE](/developer_guides/oauth_pkce)、[OAuth 设备授权](/developer_guides/oauth_device_code)模式时，应用程序获取的 Access Token 默认拥有 OAuth  该企业中所有资源的权限。例如权限列表中包含 chat 权限，通过这个 Token 可以调用 chat 接口，与此账号名下所有空间中的所有智能体对话。

在多人协作场景下，扣子用户往往需要跨账号授权，例如，企业 A 里的成员希望使用企业 B 的应用 B，需要给此应用授予权限。

授权流程如下：

1. 企业 B 的应用发起授权请求。
2. 企业 A 的用户通知组织超级管理员或管理员安装此 OAuth APP。
3. 企业 A 的组织超级管理员或管理员安装此 OAuth APP。
4. 企业 A 的用户通知组织超级管理员或管理员授权此 OAuth APP，应用 B 可以访问企业 A 中的资源。

:::tip 说明
会话、对话、消息为全局资源，不隶属于任何空间，所以指定空间 ID 之后无法授予 Access Token 会话相关的权限，例如创建会话 createConversation。
:::

## 实现方案 {#9b4e4e89}

在 OAuth 授权流程中，应用程序发起授权请求，申请获取授权码（code）时，可以指定空间 ID，并引导空间所有者为空间安装应用。

以授权码授权模式为例，多人协作场景下应用程序发起授权请求的流程如下。

![Image=800x373](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b5a8c3bd17e1436fbb9aa07f8852266f~tplv-goo7wpa0wc-image.image)

### 1 确定工作空间 {#dd1334c7}

空间协作者可以为应用程序授予工作空间中的资源权限，从而使用工作空间中的资源，例如和工作空间中本人创建的智能体对话、修改本人创建的知识库等。

应用程序申请企业资源权限前需要通过以下方式获取空间 ID：

* **引导用户手动输入扣子空间 ID**：扣子用户登录扣子编程后，进入指定空间，空间页面 URL 中 `space` 参数后的数字就是 Space ID。例如`https://code.coze.cn/space/736163827687053****/bot`，空间 ID 为`736163827687053****`。
* **通过 OpenAPI 获取空间列表**。应用程序完成一套简易的授权流程后，调用扣子 OpenAPI 接口[查看空间列表](/developer_guides/list_workspace)，查看指定账号下的空间列表，并在前端页面中展示空间列表，引导用户选择一个空间。
   此接口获取的空间 ID 包括以下三种：
   * 指定账号的个人空间。
   * 指定账号创建的工作空间。
   * 指定账号已加入的工作空间。

### 2 发起授权请求 {#32ecd2d4}


1. 应用程序发起授权请求。
   应用程序通过302重定向方式发起 [获取授权页面 URL](/developer_guides/oauth_code#54010bd0) API 请求，请求的 Path 中指定一个空间 ID，表示授予 Access Token 此空间下所有资源的权限。
   :::tip 说明
   扣子编程中的资源具有层级关系。授权时如果指定空间，则无法授予 Access Token 与空间平级的其他权限，例如会话相关权限。
   :::   


![Image=300x394](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d4e6a51b6dc148d7806194bcbaab9f06~tplv-goo7wpa0wc-image.image)

2. 扣子用户访问授权页面，单击**授权**，确认授权的应用及权限范围。
   * 如果你是组织超级管理员或管理员，单击**授权**后，提示授权成功。请跳转至[4 获取授权码](/developer_guides/oauth_collaborate#ad42474f)。
   * 如果你是组织成员，单击**授权**后，提示授权失败，说明超级管理员或管理员未安装该应用，请单击**发起申请**。联系超级管理员或管理员安装应用。超级管理员或管理员安装应用后，成员需要再次访问授权页面，单击**授权**，直至页面提示授权成功。
   * 如果你是组织成员，单击**授权**后，提示授权成功，说明超级管理员或管理员已安装该应用。请跳转至[4 获取授权码](/developer_guides/oauth_collaborate#ad42474f)。

### 3 组织超级管理员或管理员安装应用 {#6f5bfe3f}

当成员单击**发起申请**后，超级管理员或管理员可以通过如下三种方式安装应用：

* 在弹出的安装请求对话框中单击**安装**。
* 在**授权** > **应用安装管理**页面的**操作**列中单击**安装**。
* 访问成员提供的授权链接地址，选择空间权限，单击**授权**。

::::cols
@col 50
对话框中安装应用

![Image=307x397](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0eba72a2ad5e4a139a5b507345dfc57e~tplv-goo7wpa0wc-image.image)

@col 50
应用安装管理页面安装应用

![Image=500x182](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b7e07c0f7a61463987b91c10a8580e89~tplv-goo7wpa0wc-image.image)
::::

### 4 获取授权码 {#ad42474f}

授权成功后，扣子 OAuth Server 会在 API 接口响应中返回授权码 code。应用程序可根据授权码换取 Access Token，在被授予的权限范围内调用扣子 API。详细步骤说明可参考[2 获取访问令牌](/developer_guides/oauth_code#6c13ead3)和[步骤三：请求令牌](/developer_guides/oauth_pkce#a52cf514)部分。
