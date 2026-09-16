> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程 Scraper 是一个用来提取网页上的文本内容，将这些内容上传到知识库的一个工具。你可以通过 Chrome 浏览器的应用商店进行安装。

:::tip 说明
扣子编程 Scraper 目前仅支持 Chrome 浏览器。
:::

## 通过应用商店安装 {#fd776cbf}

1. 打开 Chrome 浏览器。
2. 点击[本链接](https://chromewebstore.google.com/detail/coze-scraper/onpohiaebacahchaphmnehcnbjmamcbb)在 Chrome 应用商店中打开扣子编程 Scrapper 扩展程序。
3. 单击**添加至 Chrome**。
4. 在弹出的页面，单击**添加扩展程序**。
   至此扩展程序已成功安装至浏览器。完成安装后，你就可以使用该工具手动采集要上传到扣子知识库的内容了，详情请参考[使用知识库](/guides/use_knowledge)。   


## 本地安装 {#ef8374b1}

参考以下操作，在本地安装扣子编程 Scrapper 工具。

1. 单击[这里](https://lf-coze-web-cdn.coze.cn/obj/coze-web-cn/browser-extension/artifacts/coze-extension-1.0.1.14.zip)下载安装包，然后解压下载的文件。
2. 打开 Chrome 浏览器。
3. 在浏览器中输入`chrome://extensions`打开扩展程序页面，确认**开发者模式**处于打开状态。
   ![Image=2816x1072](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/268cebbcd63d4d95a3ee51a9a13a34ff~tplv-goo7wpa0wc-topic.webp)
4. 点击**加载已解压的扩展程序**，选择已解压的文件夹。

## 更新插件版本 {#305b9dd6}

扣子编程会不定期更新插件版本，如果使用插件时提示当前版本不是最新，可以参考以下方式更新插件版本。

* **卸载插件后重新安装**。此方式仅更新 Coze Scraper 版本，不更新其他插件的版本。
   1. 浏览器访问插件管理页面 `chrome://extensions/`。
   2. 找到旧版本的 scraper 插件，并单击 **Remove**。
      ![Image=319x182](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c7c5f01e9da84b01a78490875db5f938~tplv-goo7wpa0wc-topic.webp)
   3. 参考[安装 Scraper](/guides/scraper) 重新安装 Coze Scraper 插件。
* **更新浏览器所有插件的版本**。此方式会批量更新当前安装的所有插件版本，包括 Coze Scraper。浏览器中安装了多个插件时可能耗时较长。
   1. 浏览器访问插件管理页面 `chrome://extensions/`。
   2. 单击按钮 Update。全部插件更新完毕后，
      ![Image=319x171](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5cebc25123714ebfb3acaa2e3ade6c9c~tplv-goo7wpa0wc-topic.webp)      


## 使用扣子编程 scraper 采集数据 {#ef5d2977}

至此扩展程序已成功安装至浏览器。完成安装后，你就可以使用该工具手动采集要上传到扣子知识库的内容了。

以下操作展示如何使用该工具手动采集数据上传到知识库，更多关于知识库的内容，详情请参考[使用知识库](/guides/use_knowledge)。

1. 登录[扣子开发平台](https://www.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)。
   扣子开发平台是扣子编程的旧版本，你也可以在[扣子编程首页](https://code.coze.cn/home?surl_token=FJvCs&zlink_code=FFKdE&utm_medium=docs&utm_source=docs&utm_content=landingpage&utm_id=&utm_campaign=&utm_term=docs&utm_source_platform=)右上角单击**回到旧版**，进入低代码项目的管理入口。
2. 在页面顶部选择目标工作空间，然后在左侧导航栏中单击**资源库**。
3. 在**知识库**页签下，创建一个知识库或点击一个已存在的知识库。
4. 在页面右上角，选择**添加内容** > **在线数据**。
   ![Image=517x82](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4a91e608bfec4eb19bd91ab0c05ae4b3~tplv-goo7wpa0wc-topic.webp)
5. 单击**手动采集**，然后在弹出的页面点击**权限授予**完成授权。
   ![Image=514x276](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d262e9e8c08247bfb4fe66c2b5aa37bf~tplv-goo7wpa0wc-topic.webp)
6. 在弹出的页面输入要采集内容的网址，然后单击**确认**。
7. 在弹出的页面上，点击页面下方文本标注按钮，开始标注要提取的内容，然后单击文本框上方的**文本**或**链接**按钮。
8. 单击**查看数据**查看已采集的内容，确认无误后再点击**完成并采集**。
   ![Image=438x240](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/b1535460af434e9487d9d0006ea89c53~tplv-goo7wpa0wc-topic.webp)
