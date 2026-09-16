> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程默认使用动态 IP 调用插件，也支持通过固定 IP 访问插件对应的服务，助力企业实现精准访问控制与安全审计。

## 场景描述 {#d9f02f80}

为确保安全与合规，金融等对安全要求较高的企业通常要求，访问其内网服务的公网访问必须提供固定 IP 段。扣子编程推出的固定 IP 访问插件功能，既能助力企业实现精准访问控制与安全审计，又能满足其对外网访问地址的管理需求，从而更好地满足客户的实际需求。开启固定 IP 调用功能后，扣子编程将通过固定 IP 地址列表中的 IP 访问插件对应的服务，你可以将 IP 地址列表添加到防火墙白名单中，实现对公网访问的精准控制。

:::tip 说明
在团队版和企业版中，企业超级管理员可以通过**功能访问控制**和**空间资源可见性**，控制成员可见的功能入口和空间资源范围。如果你未看到预期的功能和资源，请联系企业超级管理员确认。更多信息，请参考[功能访问控制](/guides_team_config#hnd1HfjfQ)和[空间资源访问控制](/guides_team_config#hCId5unoV)。
:::

## 使用限制 {#fcf2c43f}

* 该功能目前仅对**企业旗舰版的白名单用户开放**。如果需要使用此功能，请联系商务经理，提供插件所在的空间 ID，申请加入白名单。申请通过后，扣子编程会提供具体的 IP 地址列表。
* 仅基于已有服务创建的云侧插件支持该功能，扣子编程 IDE 中创建的云侧插件和端侧插件不支持。

## 操作步骤 {#fd71d98d}

扣子编程默认使用动态 IP 调用插件，如果需要使用固定 IP 调用，请执行以下操作：

在**资源库**页面，单击需要使用固定 IP 访问的插件。单击插件名称后面的修改图标，在**编辑插件配置**页面，开启或关闭固定 IP 调用：

* 使用固定 IP 调用插件：开启**固定 IP** **调用**。开启后，扣子编程将通过固定 IP 地址列表中的 IP 访问插件对应的服务。
* 使用动态 IP 调用插件：关闭**固定 IP 调用**。关闭后，扣子编程将通过动态 IP 访问插件对应的服务。

::::cols
@col 50
![Image=1511x603](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/770ef054b3b34bd3a516f0b9ae88bd1e~tplv-goo7wpa0wc-topic.webp)

@col 50
![Image=400x757](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/232f833c4f664b57a68f005f69ea39b0~tplv-goo7wpa0wc-topic.webp)
::::
