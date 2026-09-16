> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

本文介绍如何在乐鑫 ESP32 芯片上实现与智能体音视频通话，你可以选择基于 RTC 实现音视频通话，或基于 WebSocket 实现语音通话。
## RTC 音视频通话 {#a7921a41}
乐鑫提供了 [esp-adf 示例项目源码](https://github.com/espressif/esp-adf)，本文将基于该示例项目源码，详细演示如何在乐鑫 ESP32-S3 芯片的 ESP32-S3-Korvo-2 开发板上实现与智能体的音视频通话功能。该开发板适用于开发多种智能产品，包括但不限于音视频通话设备、智能门铃、宠物监控系统、智能音响、儿童玩具以及智能家具面板等。
### 搭建开发环境 {#f5ede349}
本文基于 [esp-adf 示例项目源码](https://github.com/espressif/esp-adf)进行实现，该仓库已内置稳定版本的 ESP-IDF，无需额外安装。详细的 ESP32-S3 开发环境信息请参见 [ESP-IDF 快速入门](https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32s3/get-started/index.html)。

1. 获取示例代码。
   1. 在终端创建一个 esp 目录用于存放相关代码。
   ```Bash
   mkdir ~/esp
   ```

   2. 进入 esp 目录并克隆代码。
   ```Bash
   cd ~/esp
   git clone https://github.com/espressif/esp-adf.git
   ```

   3. 递归更新子模块。
   ```Bash
   git submodule update --init --recursive
   ```

2. 在 adf 仓库下运行安装脚本。
   ```Bash
   sh ./install.sh
   sh ./export.sh
   ```

3. 配置环境变量，`ADF_PATH` 和 `IDF_PATH` 的获取方法请参见 [ESP ADF 快速入门](https://docs.espressif.com/projects/esp-adf/en/latest/get-started/index.html#get-started-setup-esp-idf)。
   ```Bash
   ADF_PATH={{你的 adf 路径}}
   IDF_PATH={{你的 idf 路径}}
   ```


### 适配硬件 {#2edd1703}
#### 1. 选择开发板 {#5c8eb563}

1. 进入本地 esp-adf 代码的 `volc_rtc` 目录。
   ```Bash
   cd ~/esp/esp-adf/examples/ai_agent/volc_rtc
   ```

2. 设置目标芯片型号，本文使用 esp32s3。
   ```Bash
   idf.py set-target esp32s3
   ```

3. 选择开发板。
   ```Bash
   idf.py menuconfig
   ```

4. 在弹出的交互界面中选择使用的开发板，本文使用 **ESP32-S3-Korvo-2** ，按 `S` 保存。

#### 2. 修改 I/O 配置（可选） {#4d2af897}

:::tip 说明
如果使用乐鑫官方的 ESP32-S3-Korvo-2 开发板，请忽略该步骤。
由于本示例使用的 01_RTC_LCD 开发板在视频流和扬声器的针脚与官方 ESP32-S3-Korvo-2 不一致，需修改驱动代码以确保正常运行。
:::

1. 使用编码 IDE 打开 esp-adf 目录，单击`components/audio_board/esp32_s3_korvo2_v3/board.c`文件。

<div style="text-align: center"><img src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/d50f2f27029f4d4fbb35e7908d3bff4e~tplv-goo7wpa0wc-image.image" width="800px" height="333px" /></div>


2. 修改以下内容：
   *  扬声器 PA 针脚：找到 `audio_board_init` 函数，将 PA 针脚修改为 **TCA9554 的 0 号针脚**。将下面的代码替换掉`audio_board_init` 函数。
      ```C
      audio_board_handle_t audio_board_init(void)
      {
          ESP_LOGW(TAG, "Init board Start!");
          if (board_handle) {
              ESP_LOGW(TAG, "The board has already been initialized!");
              return board_handle;
          }
          board_handle = (audio_board_handle_t) audio_calloc(1, sizeof(struct audio_board_handle));
          AUDIO_MEM_CHECK(TAG, board_handle, return NULL);
          board_handle->audio_hal = audio_board_codec_init();
          board_handle->adc_hal = audio_board_adc_init();
          esp_tca9554_config_t pca_cfg = {
              .i2c_scl = GPIO_NUM_18,
              .i2c_sda = GPIO_NUM_17,
              .interrupt_output = -1,
          };
          tca9554_init(&pca_cfg);
          tca9554_set_io_config(BIT(0), TCA9554_IO_OUTPUT);
          tca9554_set_output_state(BIT(0), TCA9554_IO_HIGH);
          return board_handle;
      }
      ```

   * 屏幕偏选信号：屏幕型号为 ST7789，触摸 IC 为 GT911。找到 `audio_board_lcd_init` 函数中的 `io_config` 对象，将如下代码替换掉`io_config`中的初始化代码。
      ```C
      esp_lcd_panel_io_spi_config_t io_config = {
              .dc_gpio_num = LCD_DC_GPIO,
              .cs_gpio_num = LCD_CS_GPIO,
              .pclk_hz = 60 * 1000 * 1000,
              .lcd_cmd_bits = 8,
              .lcd_param_bits = 8,
              .spi_mode = 0,
              .trans_queue_depth = 10,
              .on_color_trans_done = cb,
              .user_ctx = NULL,
          };
      ```


### 修改示例项目源码 {#7f8838de}
你需要修改 [esp-adf](https://github.com/espressif/esp-adf) 示例代码中的 WiFi 信息和扣子编程配置。

1. 配置 WiFi 信息。
   在 menuconfig 中，填写 SSID 和 PASSWORD，然后编译下载到开发板中。
2. 配置扣子编程。
   在 [coze_http_request.h](https://github.com/espressif/esp-adf/blob/master/examples/ai_agent/volc_rtc/main/coze_http_request.h) 中修改如下配置：
   <!-- @cols-width: 100,100,610 -->
   | | | | \
   |**参数** |**是否必选** |**说明** |
   |---|---|---|
   | | | | \
   |uri |必选。 |请填写 `https://api.coze.cn/v1/audio/rooms`。 |
   | | | | \
   |authorization |必选。 |请填写扣子编程的访问密钥，用于身份认证与鉴权。 |\
   | | | |\
   | | |* **体验或调试场景**：建议开发者生成一个短期的个人访问令牌（PAT），快速跑通 Realtime SDK 的整体流程。个人访问令牌获取方式可参考[添加个人访问令牌](/developer_guides/pat)。 |\
   | | |* **线上环境**：线上环境应使用 OAuth 鉴权方案。OAuth 鉴权方案的详细说明可参考[OAuth 应用管理](/developer_guides/oauth_apps)。 |
   | | | | \
   |bot_id |必选。 |智能体 ID，获取方法如下： |\
   | | |进入智能体的开发页面，开发页面 URL 中 `bot` 参数后的数字即为智能体 ID。例如， URL 为`https://www.coze.cn/space/341****/bot/73428668*****`，则智能体 ID 为`73428668*****`。 |
   | | | | \
   |voice_id |可选。 |音色 ID。默认采用`柔美女友`音色，音色 ID 为 7426720361733046281。你可以调用[查看音色列表](/developer_guides/list_voices) API 查看当前可用的音色列表，也可以使用[系统音色列表](/dev_how_to_guides/sys_voice)。 |

3. 修改 HTTP 请求配置。
   :::tip 说明
   你也可以自行配置 TLS 证书，配置之后无需修改。
   :::
   在 `byte_rtc_request.c` 文件中，找到 `byte_rtc_request` 函数中的 `http_client_config` 变量，将该变量的声明替换为如下的代码：
   ```C
   esp_http_client_config_t http_client_config = {
       .url = config->uri,
       .query = "esp",
       .event_handler = _http_event_handler,
       .user_data = &rsp_data,
       .disable_auto_redirect = true,
       .buffer_size = DEFAULT_STACK_SIZE,
       .buffer_size_tx = DEFAULT_STACK_SIZE,
       .skip_cert_common_name_check = true,
       .cert_pem = NULL,
       .transport_type = HTTP_TRANSPORT_OVER_SSL,
       .crt_bundle_attach = esp_crt_bundle_attach,
       .is_async = false,
       .timeout_ms = 10000,
       .keep_alive_enable = true
   };
   ```

4. 创建并加入扣子房间。
   你需要调用扣子编程的[创建房间](/developer_guides/create_room)接口创建房间，再加入房间，才可以与智能体进行对话。在[乐鑫示例代码的 volc_rtc.c](https://github.com/espressif/esp-adf/blob/master/examples/ai_agent/volc_rtc/main/volc_rtc.c) 文件中已经实现了创建房间的代码，在实际使用的时候，你需要执行如下操作才能使用相关代码。
   1. 声明一个全局变量。
      ```C
      const char* g_default_room_id = NULL;  // 定义全局变量
      ```

   2. 修改文件中的`byte_rtc_engine_create`方法，引入请求扣子编程的代码，并使用扣子编程返回的 app_id 创建 RTC 引擎。
      ![Image=800x74](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/49aaf656bc0b4c379593576013effbb9~tplv-goo7wpa0wc-image.image)
   3. 使用扣子编程返回的 `room_id` 赋值给全局变量 `g_default_room_id` 。
      ![Image=800x61](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/5e600c4475524dddb74966267de8dc7f~tplv-goo7wpa0wc-image.image)
   4. 在`voice_read_task`方法中，用扣子编程返回的 `room_id` 指定对话时的 `room_id`。
      ```Bash
      byte_rtc_send_audio_data(s_volc_rtc.engine, g_default_room_id, voice_data, voice_data_read_sz, &audio_frame_info);
      ```


##  WebSocket 语音通话 {#70a12298}
乐鑫推出基于扣子编程 WebSocket 封装的轻量级 Espressif Coze SDK，能在 ESP32 嵌入式设备上接入扣子编程 WebSocket Open API，实现语音通话，具体请参见 [Espressif Coze 官网](https://components.espressif.com/components/espressif/esp_coze/versions/0.5.0?language=en)，示例项目源码请参见 [esp_websocket_client 示例项目源码](https://github.com/espressif/esp-protocols/tree/master/components/esp_websocket_client/examples)。
## 相关文档 {#81a9f7de}
[集成音视频 Realtime 嵌入式 SDK](/dev_how_to_guides/realtime_embedded)
[硬件设备基于 WebSocket 实现语音交互](/tutorial/websocket_voice_best_practices)

