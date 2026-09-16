> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

图片上传组件用于上传和展示图片，常用于图像内容的管理。
## 使用说明 {#7ec8447c}
图片上传组件的值为 String 类型，格式为 `{"bytes":204010,"created_at":1745759048,"file_name":"Snipaste_2025-04-27_17-22-45.png","id":"7497976797368516618","file_id":"7497976797368516618"}`。即通过图片上传组件上传图片后，仅生成图片 ID，不会直接生成图片 URL。
你可以在工作流中，将输入参数的数据类型设置为 `Image`，然后将图片上传组件的值传递给该输入参数。系统会自动解析并获取图片的 URL，再将该 URL 传递给下游节点，从而实现图片数据的高效处理。具体配置，请参考[配置示例](/guides/image_upload_web#5ca37417)。
![Image=338x224](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c578be9d425743e882131d0c07f4c885~tplv-goo7wpa0wc-image.image)
## 属性设置 {#d6df8334}
图片上传组件提供了丰富的属性配置选项，以下是一些关键属性配置说明。关于组件尺寸、位置、样式、指针、变换等通用属性的设置方法，请参考[设置组件属性和事件](/guides/set_properties_events)。
### 设置图片数量 {#4e109cee}
图片上传组件支持上传单张或多张图片，最多支持 10 张。
:::tip 说明
* 如果选择**单张图**，则图片上传组件的值为 `Image` 或 `File` 类型。
* 如果选择**多张图**，则图片上传组件的值为 `Array<Image>` 或 `Array<File>` 类型。
:::
![Image=352x222](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/56aea418fa974ad0b485a498729e9e26~tplv-goo7wpa0wc-image.image)
### 设置标签和提示文案 {#050834b8}
图片上传组件支持设置标签、提示文案，使开发者能够更精准、高效地描述组件的功能和用途。
![Image=611x136](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9b8c99c5c4284ce4aebb6a7533a6c464~tplv-goo7wpa0wc-image.image)
### 设置上传区图标 {#42824947}
图片上传组件支持设置上传区图标，开发者可以根据应用的视觉设计风格或具体业务需求，灵活选择和设置上传区的图标样式。
![Image=612x124](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ca5294e42d1b475e8927ea903d2c200a~tplv-goo7wpa0wc-image.image)
### 隐藏组件 {#77314fff}
图片上传组件的可见性可通过设置常用条件或表达式灵活控制，以实现特定场景下的隐藏或显示。

* 表达式方式
   * 设置为 false：显示组件。
   * 设置为 true：隐藏组件。
   * 设置为变量：通过变量值（true 或 false）动态控制组件的可见性。配置示例，请参考[隐藏组件](/guides/set_properties_events#46d8e38f)。
* 常用条件方式
   支持通过可视化界面设置条件，以控制组件的可见性。配置示例，请参考[隐藏组件](/guides/set_properties_events#46d8e38f)。

## 事件设置 {#b8894162}
通过配置图片上传组件的事件，可以为图片上传组件添加丰富的交互功能，以增强用户体验和界面的互动性。
<!-- @cols-width: 148,709 -->
| | | \
|**事件项** |**说明** |
|---|---|
| | | \
|事件类型 |数据改变时：在图片上传过程中，图片数据发生变化时触发事件。 |
| | | \
|组件方法 |支持以下方法： |\
| | |\
| |* 清除：清除选择的选项内容。 |\
| |* 清除验证：移除组件上的所有验证错误信息。 |\
| |* 验证：检查组件的当前值是否符合预设的验证规则。 |\
| |* 重置：将组件恢复到初始状态。 |\
| |* 滚动到视图：将组件滚动到可视区域内。 |\
| |* 设置禁用：使组件变为禁用状态，用户无法与之交互。 |\
| |* 设置隐藏：隐藏组件，使其不可见。 |\
| |* 上传：上传图片 |

## 配置示例 {#5ca37417}
例如，当你想要搭建一个一键替换图片背景的应用时，可以通过图片上传组件分别上传背景图和主体图，再将这些图片 ID 传递给工作流，作为工作流的输入参数进行后续的图片处理操作。

1. 创建工作流。
   使用背景替换（background_change）插件为图片替换背景。
   * 在**开始**节点中，设置输入参数 `front_input` 和 `background_input`，变量类型需设置为 `Image`。
   * 在**背景替换**插件节点，将**背景图**和**主体图**分别引用开始节点的`front_input` 和 `background_input` 变量。
   * 在**结束**节点，将 `output` 变量设置为**背景替换**插件节点输出结果中的 `data`，其为 `Image` 类型。
   ![Image=1591x516](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c7262d6e225c4cda9b764b1394b54011~tplv-goo7wpa0wc-image.image)
2. 搭建应用页面。
   * **ImageUpload1**：图片上传组件，用于上传原图。
   * **ImageUpload2**： 图片上传组件，用于上传背景图。
   * **Image1**：图片组件，用于展示处理后的图片。
   * **Button1**：按钮组件，用于触发工作流。
   * **Div**：容器组件，用于页面布局。
   ![Image=1819x649](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/0947bad177654350bdbade66baebc770~tplv-goo7wpa0wc-image.image)
3. 为按钮组件（Button1）配置事件。
   单击按钮时，触发工作流，将上传图片组件 **ImageUpload1** 和 **ImageUpload2** 的值作为输入参数传递给工作流，由工作流完成图片处理操作。
   ![Image=1891x767](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/363d1e99ee59454aa17c3751f01c239f~tplv-goo7wpa0wc-image.image)
4. 为图片组件（Image1）绑定值 `{{ image.data.output }}`。
   `{{ image.data.output }}` 为工作流的输出结果，即处理后的图片。
   ![Image=297x219](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/1f0a7b1ecae440949787785ff76e8717~tplv-goo7wpa0wc-image.image)
5. 预览效果。
   上传原图和背景图后，单击**替换图片背景**按钮，系统将自动调用工作流替换原图的背景，并返回处理后的图片。
   ![Image=1969x664](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/74d0d9a9e91a46f7b3a4aa0fb1f11c13~tplv-goo7wpa0wc-image.image)


