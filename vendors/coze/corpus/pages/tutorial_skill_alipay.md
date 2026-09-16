> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程技能中上架了支付宝提供的**支付宝支付集成**、**支付商家入驻**技能，用于为**网页应用**快速集成支付宝支付能力。

## 支付宝技能介绍 {#9f1d9678}

你是否正在使用扣子编程开发商城类网页应用，并希望用户能在应用内直接下单付款？现在通过支付宝官方编程技能包（**支付宝支付集成、支付商家入驻**）和扣子编程的**支付宝支付密钥托管**技能，就能为你的应用快速搭建完整的支付能力。

你只需在开发过程中调用对应技能，扣子 AI 便会根据技能指引，自动完成流程化的支付功能开发。

### 技能说明 {#1bbe0729}

支付相关的技能功能与使用场景说明如下表所示：

<!-- @cols-width: 148,398,312 -->
|**技能** |**说明** |**使用场景** |
|---|---|---|
|支付宝支付集成 |创建沙箱环境、生成支付集成代码、引导完成支付流程调试。 |**每个项目都需要加载**。开发应用时，调用此技能完成支付功能接入。 |
|支付商家入驻 |商家入驻是支付宝对收款方的资质审核流程。调用支付商家入驻技能，能够智能规划入驻方案、自动处理支付宝侧的产品开通与应用上架。 |\
| | |\
| |入驻后你会获得： |\
| | |\
| |* 正式的商家身份和收款权限 |\
| |* 支付宝应用，用于标识你的收款项目 |\
| |* 签约的支付产品（如电脑网站支付、手机网站支付） |**按支付宝账户级别生效，无需每个项目加载。​**如果你的支付宝账户已完成商户入驻，并且已有可用的支付宝网页应用，可跳过此技能。 |
|支付宝支付密钥托管 |安全存储支付宝公钥和应用私钥。 |**每个项目都需要加载**。开发应用时，调用此技能配置支付宝密钥。 |

### 集成后的效果 {#20b3f114}

你的应用集成支付能力且你具备收款资质后，用户可直接在应用内下单购买商品。支付完成后，交易金额将直接进入你签约的支付宝账户。

体验地址：https://y39hjgm54d.coze.site/

::::cols
@col 50
![Image=514x323](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4d3f4452970b478087db0caeda2e3f98~tplv-goo7wpa0wc-image.image)

@col 50
![Image=403x287](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bfc1f29227d24192b348d85e18babc0b~tplv-goo7wpa0wc-image.image)
::::

## 使用须知 {#adc298a0}

<!-- @cols-width: 134,686 -->
|**类目** |**说明** |
|---|---|
|费用 |* **扣子编程**：与扣子 AI 的每轮对话，将消耗积分。 |\
| |* **支付宝**：按照支付宝官方标准向商家收取交易手续费，标准费率通常为 0.6%，具体请以签约协议为准。 |
|适用范围 |目前，支付宝相关技能仅适用于**网页应用**。 |
|推荐模型 |为获得最佳开发体验，建议使用 `GLM-5` 模型。 |
|推荐套餐版本 |推荐使用**个人版**套餐。 |\
| | |\
| |目前，企业版的**支付宝支付密钥托管**集成服务配置较为繁琐，我们正在加急优化升级，敬请期待。 |

## 开发流程 {#d91ea130}

1. **开发应用**：完成应用的基础功能开发。
2. **集成支付能力**：使用`支付宝支付集成`技能，由扣子 AI 生成代码，为应用集成支付能力。
3. **完成商家入驻**：使用`支付商家入驻`技能，由扣子 AI 生成代码，完成商家入驻。
4. **配置密钥**：使用**支付宝支付密钥托管**技能托管密钥，并完成密钥配置。
5. **部署应用**：正式上线应用，供用户使用。

## 步骤一：开发应用 {#258ab6db}

:::tip 说明
本文中的截图仅作参考，实际以开发展示界面为准。
:::

在集成支付能力前，建议先完成应用的基础开发。以下以壁纸售卖网页为例说明。

1. 在扣子编程首页，单击**网页应用**选项卡。
2. 在文本框输入你的提示词，明确应用需求。
   ```Markdown
   开发一款支持壁纸展示与购买功能的网页应用。
   1. 提供壁纸缩略图展示功能，包括多张不同风格的壁纸预览。
   2. 针对每张壁纸提供购买按钮，点击后可进入购买流程。
   3. 支持壁纸的分类筛选功能，用户可按风格、分辨率等条件筛选壁纸。
   4. 提供壁纸详情页，展示壁纸规格、价格及相关介绍。
   5. 购买后可以下载壁纸。
   ```
3. 在键盘中敲击回车，开发你的项目。
   扣子 AI 会根据提示词自动设计并开发应用。
4. 确认开发结果。
   建议在应用基础功能开发完成并验证通过后，再集成支付能力，避免后期返工。
   ![Image=680x314](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1eb3d6e6cdce4f74903ace124ac8674d~tplv-goo7wpa0wc-image.image)   


## 步骤二：集成支付能力 {#850281f5}

使用支付宝支付集成技能，为应用集成支付能力。开发完成后，你可以使用测试账号完成调试，不会产生真实的交易资金。

1. 在对话区，单击**技能**，添加**支付宝支付集成**技能。
   ![Image=638x336](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/09011defe42a4529b6de80eb9ffce12c~tplv-goo7wpa0wc-image.image)
2. 输入加载技能的提示词。
   ```Markdown
   为当前应用集成支付宝支付功能
   ```
3. 扣子 AI 加载**支付宝支付集成技能**，逐步完成操作。
   扣子 AI 会根据技能指引，完成如下 6 步操作。
   1. 产品决策。
      扣子 AI 会展示产品决策供你确认，包括：
      * 接入的支付方式（电脑网站支付、手机网站支付）
      * 协议内容：使用本服务需遵守法律法规、自行审核测试并承担使用责任，我方不对使用效果、正确性担保；禁止在代码、大模型对话等公网透露敏感信息（密码、API Keys、私钥等）。
         确认无误后，输入**同意**。如果不符合预期，可以通过自然语言调整。
         ![Image=188x331](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/97cd4cda746f4b19b8f64b3d6afcc4e6~tplv-goo7wpa0wc-image.image)
   2. 沙箱初始化。
      **无需准备真实的支付宝账号**，系统会自动创建沙箱及测试账号。支付功能开发完成后，你可以直接使用这个测试账号登录支付宝，完成下单支付。
      ::::cols
      @col 50
      创建沙箱环境
      
      ![Image=342x266](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a549b2fd1c2e46c7a8da145a508b76cd~tplv-goo7wpa0wc-topic.png)
      
      @col 50
      提供测试账号
      
      ![Image=319x323](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2281b852f8d14525be3b2726bba46b4b~tplv-goo7wpa0wc-image.image)
      ::::
3. 集成前置步骤。
   ![Image=212x276](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e102d538e26449ff86c1246917540465~tplv-goo7wpa0wc-image.image)
4. 集成代码。
   阅读支付接入文档，生成支付集成代码。
   ![Image=221x228](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/09ff48c7650949d4a56ef650736dcdf5~tplv-goo7wpa0wc-image.image)
5. 输出集成后说明。
   完成代码开发后，系统会自动生成集成安全红线说明，**请务必仔细阅读**。
   ![Image=355x276](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/082df42dadb9463cbe7ea7e047e8777e~tplv-goo7wpa0wc-image.image)
6. 集成校验。
   你确认同意开启集成校验后，扣子 AI 会自动逐项检测代码是否符合校验清单要求。
   ![Image=260x275](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/199c13a589ec4e6c86df71e38330fc6c~tplv-goo7wpa0wc-image.image)
4. 验证支付能力。
   完成以上开发步骤后，单击网站中的**购买**，并使用【沙箱初始化】环节获取的测试账号登录支付宝，即可完成测试支付，无需额外下载沙箱 App。
   沙箱环境仅适用于开发调试，如需正式收款，请完成商家入驻流程。若测试支付遇到流程卡住、流程报错等问题，可直接将问题截图或报错信息粘贴到对话中，让大模型修复，直至测试支付完成为止。
   ::::cols
   @col 50
   ![Image=398x188](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d28ca48816ea4c37a73096a65c185f00~tplv-goo7wpa0wc-image.image)
   
   @col 50
   ![Image=378x223](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/6605ee989e3a4ec2a54fcc6cca63682e~tplv-goo7wpa0wc-image.image)
   ::::   


## 步骤三：完成商家入驻 {#9f1312ad}

沙箱测试通过后，调用支付商家入驻技能，启动正式商家入驻流程。

:::tip 说明
如果你的支付宝账户已完成商户入驻，并且已有可用的支付宝网页应用，可跳过此步骤。
:::

1. 在对话区域，单击**技能**，添加**支付商家入驻**技能。
   ![Image=572x337](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e358c9f08cca4b11b5b788172a1a60f9~tplv-goo7wpa0wc-image.image)
2. 输入加载技能的提示词。
   ```Markdown
   为当前应用集成商家入驻技能
   ```
   ![Image=257x250](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8fe4b2834c614fd3b26b1f4c4d2f430b~tplv-goo7wpa0wc-image.image)
3. 启动支付宝商家入驻流程。
   1. 检测支付宝凭证。
      当扣子 AI 未检测到支付宝凭证时，你可以根据提示，输入**我要入驻**。
   2. 方案规划与确认。
      扣子 AI 将自动完成前置检查，然后生成入驻方案，包括：
      * 产品类型
      * 经营类目
      * 适用场景
      * 所需资料清单
         其中，经营类目的具体说明如下：
      <!-- @cols-width: 172,432 -->
      |**场景** |**处理方式** |
      |---|---|
      |可唯一确认类目 |扣子 AI 直接输出方案。 |
      |候选类目 ≤ 3 个 |扣子 AI 展示候选类目供你选择。 |
      |候选类目过多 |扣子 AI 将引导澄清类目，缩小范围后再选择。例如输入我的业务是线上零售电商、我是做餐饮外卖的等。 |
      确认方案符合需求后，输入**符合**，确认使用。如不符合，输入**不符合**，重新选择。
      未及时确认时，系统将默认使用当前方案。如需修改，可在后续步骤中重新发起。
      ![Image=245x278](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/acf3c9e958044381b1557855b2e452b5~tplv-goo7wpa0wc-image.image)
   3. 授权与协议签署。
      1. 单击授权链接，页面会展示授权二维码，使用支付宝 App 扫描。
      2. 在**授权**页面，请仔细阅读支付宝平台的收费信息和相关协议，然后确认授权。
         :::notice 注意
         * 如果没有生成授权链接或单击授权链接报错，你可以在对话框中输入`重新生成链接`、`没有看到链接`、`报错信息为xxx`等提示词，让扣子 AI自行修复。
         * 授权有效期为 12 小时。
         :::
         ::::cols
         @col 50
         ![Image=175x245](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/15e38bc8f308413c867260424cb2e943~tplv-goo7wpa0wc-topic.png)
         
         @col 50
         ![Image=175x384](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/7af247546e364d4988c90b1129fd1acb~tplv-goo7wpa0wc-image.image)
         ::::
      1. 返回到扣子编程项目的会话页面，输入**已授权**，流程将自动继续。
   4. 采集资料。
      根据界面提示，截取并上传应用的首页、商品页以及支付页的图片。
      ![Image=237x306](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/10cdf7d26d9a40b8995376256602740c~tplv-goo7wpa0wc-image.image)
   5. 自动完成产品签约和应用上架。
      ::::cols
      @col 50
      **产品签约**
      
      在产品签约阶段，系统会自动检查签约状态。
      
      * 已有合约且已开通：跳过签约，直接进入下一步。
      * 已有合约审核中：提示等待审核结果。
      * 已有合约被驳回：展示驳回原因，引导修改后重新提交。
      * 无合约：发起产品签约开通。
      
      ![Image=658x255](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e367a96500534103aaa119c22b737ee1~tplv-goo7wpa0wc-topic.png)
      
      @col 50
      **上架应用**
      
      在创建与上架应用阶段，系统会检查你的支付宝账号中是否已有网页应用。
      
      * 已有，推荐复用现有应用。需要注意的是，确认当前支付宝网页应用未绑定其他业务应用。
      * 没有，创建开放平台应用。
      
      ![Image=595x502](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8e3a9aaec4f54cdb84b5c1df58654290~tplv-goo7wpa0wc-image.image)
      ::::      


## 步骤四：配置密钥 {#2cc53872}

发布应用前，需先完成**支付宝公钥**与**应用私钥**配置，保障支付数据安全与接口通信可信。本步骤涉及三个平台的操作（支付宝密钥工具、支付宝开放平台、扣子编程），请仔细阅读，按顺序执行。

:::notice 注意
* 密钥包含敏感信息，请妥善保管，切勿将私钥等敏感信息暴露在模型上下文或公开环境中。
* 如果你已有可用密钥，无需反复生成，避免造成密钥混淆。多个扣子编程项目，可共用同一套密钥。
* 每个空间在同一时间只能托管一套密钥，若你在同一空间有多个应用且密钥不同，可能导致前序已部署的应用失效。
:::

1. 生成应用公钥、应用私钥。
   参考支付宝文档[密钥工具下载](https://opendocs.alipay.com/common/02kipk?pathHash=0d20b438)，下载并安装支付宝开放平台密钥工具，然后**生成**并**妥善记录**应用公钥、应用私钥。
   ![Image=359x265](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ed714e74a1cb4332ae88a74921fc17f2~tplv-goo7wpa0wc-image.image)
2. 生成支付宝公钥。
   ::::tabs
   @tab 方式一：通过对话形式生成
   1. 返回扣子编程项目的对话区域，输入`继续设置应用公钥，公钥为：xxxx`指令。
      ![Image=179x223](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e4b52bd7c0764aba985083c721f7f946~tplv-goo7wpa0wc-image.image)
   2. 单击确认连接，然后使用支付宝 App 扫描二维码，**确认并复制**支付宝公钥。
      ![Image=263x200](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/52e70d2957564d21b645bd2a7b8febe2~tplv-goo7wpa0wc-image.image)
      ![Image=257x291](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8abeab2604e641ceac2ad7a2179cdf16~tplv-goo7wpa0wc-image.image)
   3. 返回扣子编程项目的对话区域，输入**已确认**。
   
   @tab 方式二：通过支付宝开放平台生成
   1. 登录[支付宝开放平台](https://open.alipay.com/develop/manage)，在**网页/移动应用**页签中，单击目标应用。
      该应用为你在【完成商家入驻】中，生成的应用。你可以输入应用 ID， 搜索该应用。
      ![Image=446x194](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/626686ff51d9466db8c48986f56ec63c~tplv-goo7wpa0wc-image.image)
   2. 在**开发设置**页面，单击**接口加签方式（密钥/证书）​**对应的**设置**，然后单击**确认**。
      ![Image=566x198](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8d7645016e544f4396240fe689527d17~tplv-goo7wpa0wc-image.image)
   3. 设置**加签方式**为**密钥**，单击**下一步**。
   4. 在**生成密钥文件**中，单击**下一步**。
   5. 在**上传**中输入你的**应用公钥**，然后单击**确认上传**。
      系统将根据你的应用公钥，生成支付宝公钥。
      ![Image=502x219](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f33d3268789c49909b8a5fd076783c03~tplv-goo7wpa0wc-image.image)
   6. 复制支付宝公钥。
   ::::
3. 返回扣子编程项目的对话区域，单击**技能**，添加**支付宝支付密钥托管**技能。
   ![Image=458x268](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/2278f839153d4af997aec9e13aba29f8~tplv-goo7wpa0wc-image.image)
4. 输入加载技能的提示词。
   ```Markdown
   使用支付宝专属密钥托管技能
   ```
5. 扣子 AI 加载**支付宝支付密钥托管**技能，完成密钥配置。
   * 如果尚未在当前工作空间的**支付宝支付密钥托管**集成服务中输入支付宝公钥和应用私钥，系统会弹出配置界面，引导你完成密钥录入。
   * 如果已填写过密钥，请自行**核对现有密钥仍与当前支付宝应用匹配。​**扣子 AI 将直接使用现有密钥，完成后续开发。
      ![Image=498x332](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/791806c7a5e141e6a3911a6cbdeb9f9b~tplv-goo7wpa0wc-image.image)
6. 单击确认链接，然后使用支付宝App 扫描二维码，确认密钥。
   ::::cols
   @col 50
   ![Image=180x283](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9b2d2f0e258041e7b0ca7433b8a2bf74~tplv-goo7wpa0wc-image.image)
   
   @col 50
   ![Image=156x342](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0fe62995cfc241b89dd7ae3b9bdff736~tplv-goo7wpa0wc-image.image)
   ::::
7. 返回到扣子编程项目的会话页面，输入**已确认**。
8. 等待审核通过。
   开发完成后，需要等待应用审核通过后（通常 1-3 个工作日），才能正式使用支付功能。
   如果审核不通过，你可以登录[支付宝开放平台](https://open.alipay.com/)，查看具体拒绝原因。
   ![Image=428x270](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/552121ccfd8d4c94920ca0acc78dfdcf~tplv-goo7wpa0wc-image.image)   


## 步骤五：部署应用 {#25e804cd}

审核通过后，你可以将应用部署到线上，用户即可通过链接访问应用并购买商品。真实交易金额将直接进入你签约的支付宝账户。

:::notice 注意
电脑网页应用须通过电脑打开并支付，否则可能无法走通。
:::

1. 单击右上角的**部署**。
2. 配置部署参数。
   参数说明，请参考[部署网页应用](https://docs.coze.cn/guides/deploy_vibe_web)。
   ::::cols
   @col 50
   ![Image=2864x1312](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/bf69c96828b947c19fa1944002c76e1e~tplv-goo7wpa0wc-image.image)
   
   @col 50
   ![Image=1436x1118](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/de3f3535713f420986489078ad0ea7de~tplv-goo7wpa0wc-image.image)
   ::::   


## 技术支持 {#495e45ce}

当你反复修复问题失败时，可通过如下方式，**联系支付宝支付技能团队**。

::::cols
@col 50
**加入钉钉群**

打开钉钉扫一扫

![Image=200x198](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5725b7afe6524aeab7f20b5d3d8723b4~tplv-goo7wpa0wc-image.image)

@col 50
**加入企业微信群**

打开微信或企业微信扫一扫

![Image=189x189](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8112c1728c91429f9c893f6392cdd4c5~tplv-goo7wpa0wc-image.image)
::::

## 常见问题 {#dd8ac105}

### **密钥托管是否安全？** {#bbaff045}

密钥托管是安全的。密钥托管服务通过加密措施确保你的密钥信息在存储和使用过程中的安全。相比手动在对话或代码中暴露密钥，托管是更安全的方式。

### 如何判断应用已通过支付宝审核？ {#9ef4c768}

你可以登录[支付宝开放平台](https://open.alipay.com/)，单击右上角的**控制台**，然后在**网页/移动应用**页面中，查看目标应用的状态。

如果状态为**已上线**，则表示审核通过。

![Image=562x270](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/cfcdd8a4cfcd4271bf55929d11036367~tplv-goo7wpa0wc-image.image)

### **如果支付宝审核不通过，我该怎么办？** {#aa590d17}

首先确认是产品签约审核不通过，还是开放平台应用上架审核不通过。

* 产品签约不通过：你可以登录[支付宝商家平台](https://b.alipay.com/page/ar-center/ar-manage)，单击**电脑网站支付**对应的**查看详情**，查看具体拒绝原因，并按指引完成相关操作。然后你可以在详情页直接重新提交或者回到扣子编程对话区输入**我要入驻**指令，系统会引导你重新提交申请。
* 应用上架审核不通过：你可以登录[支付宝开放平台](https://open.alipay.com/develop/manage)，找到目标应用，查看具体拒绝原因，并按指引完成相关操作。然后你可以重新向扣子 AI 发起**`我要入驻`​**的指令，系统会引导你重新提交申请。

### 测试失败或报错，如何处理？ {#61d82633}

在开发过程中，如果出现测试失败或者报错问题，你可以在对话中，直接描述问题，扣子 AI 会自行进行修复。例如：

::::cols
@col 50
![Image=367x270](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/323c3392416c4906acdf8b585e1930c6~tplv-goo7wpa0wc-image.image)

@col 50
![Image=347x254](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/3d0b82e6ba464870b70612fa03e3ab16~tplv-goo7wpa0wc-image.image)
::::

### 能否使用模型生成的应用密钥？ {#70555551}

不能。在配置密钥环节，模型可能会自行生成一组密钥，但这组密钥并非真实的支付宝密钥，无法实现支付。必须使用**支付宝开放平台密钥工具**生成应用公钥和应用私钥，以及通过**支付宝开放平台**生成支付宝公钥。

### 反复修复失败时，如何处理？ {#0d8a4703}

当你修复问题反复失败时，建议滚动到之前已验证成功的版本，重新开发。如果还有问题，可参考[技术支持](/tutorial/skill_alipay#495e45ce)，联系支付宝支付技能团队。

### 出现“应用私钥与支付宝公钥不匹配”错误时，如何处理？ {#b2eb6512}

该错误主要由密钥配置错误（如公私钥配反、支付宝公钥错配为应用公钥、公私钥实际不配对）引起，请勿让模型反复修改，容易导致模型幻觉加重，越改越错。请严格按照以下步骤自查密钥。

1. 确认公私钥已正确配对、正确配置，或重置公私钥。
   重置操作：在**支付宝开放平台密钥工具**中重置应用公钥、应用私钥；复制重置后的应用公钥到[支付宝开放平台](https://open.alipay.com/)重新配置支付宝公钥。
2. 在密钥托管集成服务中，重新输入正确的支付宝公钥和应用私钥。
3. 更新完成后，单击页面右上角的**重启**图标，重启项目。
   ![Image=366x291](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5422e4efb7fa417592069257344fbd91~tplv-goo7wpa0wc-image.image)
