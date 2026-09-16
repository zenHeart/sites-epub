> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coze.cn/llms.txt
> Use this file to discover all available pages before exploring further.

扣子编程 Realtime SDK iOS 版基于火山引擎 RTC SDK 进行封装，支持将扣子编程的智能体功能与火山引擎 RTC SDK 集成，实现与智能体的实时音视频通话。扣子编程提示 Swift 和 Objective-C 语言的示例项目源码，你可以参考示例项目源码，快速从零开始构建一个简单的音视频通话应用。

## 准备工作 {#7f1d65fd}

开始集成 Realtime SDK 前，请确保开发环境满足以下要求：

<!-- @cols-width: 158,658 -->
|**操作** |**说明** |
|---|---|
|发布智能体 |已成功搭建并发布智能体为 API 服务。搭建步骤可参考[搭建可视化智能体](/tutorial/video_bot)或[搭建低延时语音助手](/tutorial/low_latency_voice_assistant)，发布步骤请参见[发布为 API 服务](/guides/publish_agent_api)。 |\
| | |\
| |:::tip 说明 |\
| |若需使用视频理解能力，请为智能体配置一个视觉模型，例如**豆包视觉理解**模型。 |\
| |::: |\
| | |\
| | |
|获取访问密钥 |获取访问密钥，用于身份认证与鉴权。 |\
| | |\
| |* **体验或调试场景**：建议生成短期的个人访问令牌（PAT），以快速完成 Realtime SDK 的整体流程。个人访问令牌的获取方法请参见[添加个人访问令牌](/developer_guides/pat)。 |\
| |* **线上环境**：在线上环境中，应使用服务访问令牌（SAT）或 OAuth 鉴权方案，各鉴权方式的详细说明请参考[鉴权方式概述](/developer_guides/authentication)。 |\
| | |\
| |:::tip 说明 |\
| |扣子编程 SDK 封装了多种鉴权方式，能够有效简化鉴权流程，你可以参考[鉴权示例代码](https://github.com/coze-dev/coze-js/tree/main/examples/coze-js-node/src/auth)实现不同方式的 OAuth 认证，以获取和管理访问扣子编程 API 所需的令牌。 |\
| |::: |\
| | |\
| | |
|准备开发环境 |* macOS 电脑，且可以正常访问互联网。 |\
| |* Xcode 14.1 或以上版本。本示例采用 **** 16.2 版本。 |\
| |* Apple 开发者账号，开发阶段可以使用个人免费账号。 |\
| |* iOS 11.0 或以上版本真机设备，且可以正常访问互联网。本示例采用 iOS 18.1。 |\
| |* 安装 CocoaPods。 |

## 跑通示例项目源码 {#b30cc298}

### 示例项目目录结构 {#dff43b6c}

[音视频通话 iOS 示例项目](https://github.com/coze-dev/coze-ios)的目录结构如下：

::::tabs
@tab Swift
```Markdown
├── Podfile
├── coze-swift
│   ├── AppDelegate.swift
│   ├── Assets.xcassets
│   ├── Base.lproj
│   ├── Config                        //配置 API 相关信息
│   ├── Info.plist
│   ├── Models                       //创建房间相关数据结构
│   ├── SceneDelegate.swift
│   ├── Services                       //API 请求封装
│   └── ViewController.swift           //主界面
├── coze-swift.xcodeproj
└── coze-swift.xcworkspace
```



@tab Objective-C
```Markdown
├── Podfile
├── Pods
├── coze-objc
│   ├── AppDelegate.h
│   ├── AppDelegate.m
│   ├── Assets.xcassets
│   ├── Base.lproj
│   ├── Config
│   ├── Info.plist
│   ├── Models
│   ├── SceneDelegate.h
│   ├── SceneDelegate.m
│   ├── Services
│   ├── ViewController.h
│   ├── ViewController.m
│   └── main.m
├── coze-objc.xcodeproj
└── coze-objc.xcworkspace
```


::::

### 配置并跑通示例项目源码 {#d754c0ac}

1. 克隆[音视频通话 iOS 示例项目源码](https://github.com/coze-dev/coze-ios)到本地。
   ```Bash
   git clone https://github.com/coze-dev/coze-ios
   ```
2. 在项目根目录下运行以下命令，初始化并安装项目依赖。
   ```Bash
   pod install
   ```
3. 在配置文件中设置 accessToken 和 botid。
   ::::tabs
   @tab Swift
   1. 在项目根目录下，复制`coze-swift/Config/APIConfig.swift.template`文件为。
   2. 编辑`APIConfig.swift`配置文件，配置 `accessToken` 和 `botId`。
   
   ```Swift
   import Foundation
   
   struct APIConfig {
       static let baseURL = "https://api.coze.cn"
       static let accessToken = "pat_sWaR9V4Yr8***" // 替换为从 https://www.coze.cn/open/oauth/pats 获取到的token
       static let botId = "74415109067667***" // 替换为自己的bot ID
       static let voiceId:String? = nil // 音色ID，可选
   } 
   ```
   
   关键参数说明如下：
   
   * **accessToken**：请替换为准备工作中获取的访问密钥，用于身份认证与鉴权。
   * **botId**：智能体 ID，获取方法如下：
      进入智能体的开发页面，开发页面 URL 中 `bot` 参数后的数字即为智能体 ID。例如， URL 为`https://www.coze.cn/space/341****/bot/73428668*****`，则智能体 ID 为`73428668*****`。
   * **voiceId**：音色 ID。可选。你可以调用[查看音色列表](/developer_guides/list_voices) API 查看当前可用的音色列表，也可以使用[系统音色列表](/dev_how_to_guides/sys_voice)。
   
   @tab Objective-C
   1. 在项目根目录下，复制 `coze-objc/Config/APIConfig.h.template` 文件为`coze-objc/Config/APIConfig.h`。
   2. 编辑`APIConfig.h`配置文件，配置 `API_ACCESS_TOKEN` 和 `API_BOT_ID`。
      ```objectivec
      #ifndef APIConfig_h
      #define APIConfig_h
      
      #define API_BASE_URL @"https://api.coze.cn" // 替换为从 https://www.coze.cn/open/oauth/pats 获取到的token
      #define API_ACCESS_TOKEN @"pat_KWQlw2nvTlLTMISAz***"
      #define API_BOT_ID @"74281773215***"
      #define API_VOICE_ID nil
      
      #endif /* APIConfig_h */
      ```   
   
   
   关键参数说明如下：
   
   * **API_ACCESS_TOKEN**：请替换为准备工作中获取的访问密钥，用于身份认证与鉴权。
   * **API_BOT_ID**：智能体 ID，获取方法如下：
      进入智能体的开发页面，开发页面 URL 中 `bot` 参数后的数字即为智能体 ID。例如， URL 为`https://www.coze.cn/space/341****/bot/73428668*****`，则智能体 ID 为`73428668*****`。
   * **API_VOICE_ID**：音色 ID。可选。你可以调用[查看音色列表](/developer_guides/list_voices) API 查看当前可用的音色列表，也可以使用[系统音色列表](/dev_how_to_guides/sys_voice)。
   ::::
4. 编译并运行项目。
   1. 使用 Xcode 打开`coze-swift.xcworkspace`或 `coze-objc.xcworkspace`。
   2. 在 Xcode 中连接并选择你的 iOS 真机设备，单击 XCode 窗口左上角的运行按钮（或使用 **Command ⌘** + **R** 快捷键）。
   3. 在 iOS 设备上打开 Demo 应用时，在弹窗中选择开启麦克风和摄像头权限。
   4. 体验 Demo 效果，界面类似如下：
      ::::cols
      @col 50
      ![Image=235x509](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e93461f33405432d99de1d06e5b573d4~tplv-goo7wpa0wc-image.image)
      
      @col 50
      <Player class="topic-video-player"  src="https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/38f98a104b21455cb60a9b127e5cc9b1~tplv-goo7wpa0wc-image.image"></Player>
      ::::
   5. 在音视频通话界面单击**连接**，连接成功后，你可以与智能体开始实时语音对话。你还可以体验打开或关闭摄像头、静音或取消静音、打断语音通话。

## 实现音视频通话 {#709433cc}

### 步骤一：（可选）新建项目 {#57f11d74}

本步骤为如何创建一个新项目，如集成到已有项目，请跳过该步骤。

1. 打开 Xcode，单击 **Create New Project…** 新建项目。
2. 在项目模板页选择 **iOS** > **App**，单击 **Next**。
3. 配置项目信息，单击 **Next。**
   ![Image=444x318](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/8d3f9fea28834bc7a5235024124d65ac~tplv-goo7wpa0wc-image.image)
   <!-- @cols-width: 160,573 -->
   |**参数** |**说明** |
   |---|---|
   |Product Name |输入项目的名称，该名称将用于标识应用程序。 |
   |Team |选择开发团队。如果尚未登录 Apple 账户，请点击 **Add account…** 按钮，并按照提示完成登录。登录完成后，即可从下拉菜单中选择您的 Apple 账户作为开发团队。 |
   |Organization Identifier |输入组织标识符，通常为反向域名格式（例如  com.yourcompany ）。 |
   |Interface |选择 **Storyboard**，用于定义用户界面布局。 |
   |Language |选择 **Swift** 或 **Objective-C**，作为项目开发的主要编程语言。 |
4. 选择项目的存储位置，单击 **Create** 完成项目创建。

### 步骤二：配置签名 {#e04738df}

选中项目，进入 **TARGETS** > **coze-objc** > **Signing & Capabilities**，选择 **Automatically manage signing**。

![Image=599x309](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/586424463cb14456b91e6019e16c3322~tplv-goo7wpa0wc-topic.png)

### 步骤三：配置权限 {#6767e283}

音视频通话需要使用麦克风、摄像头和网络权限，操作步骤如下：

1. 在 Xcode 中，打开项目的 **Info.plist** 文件。如果该文件不可编辑，可以通过鼠标右键选择 **Info**，然后选择 **Open As** > **Source Code**，以源代码形式查看和编辑。
2. 在 **Info.plist** 文件中，新增以下配置内容，明确告知系统和用户应用程序需要访问的权限及其用途。
   ![Image=604x332](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a18d202d7b834cb08420ae6a0be3bd2a~tplv-goo7wpa0wc-topic.png)
   ```XML
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
     <dict>
       <key>UIApplicationSceneManifest</key>
       <dict>
         <key>UIApplicationSupportsMultipleScenes</key>
         <false />
         <key>UISceneConfigurations</key>
         <dict>
           <key>UIWindowSceneSessionRoleApplication</key>
           <array>
             <dict>
               <key>UISceneConfigurationName</key>
               <string>Default Configuration</string>
               <key>UISceneDelegateClassName</key>
               <string>$(PRODUCT_MODULE_NAME).SceneDelegate</string>
               <key>UISceneStoryboardFile</key>
               <string>Main</string>
             </dict>
           </array>
         </dict>
       </dict>
   
       <!-- 新增配置 -->
       <key>NSCameraUsageDescription</key>
       <string>需要访问您的相机以进行视频通话</string>
   
       <key>NSMicrophoneUsageDescription</key>
       <string>需要访问您的麦克风以进行语音通话</string>
   
       <key>NSAppTransportSecurity</key>
       <string>需要网络权限</string>
       <dict>
         <key>NSAllowsArbitraryLoads</key>
         <true />
       </dict>
       <!-- 新增配置  -->
   
     </dict>
   </plist>
   ```   


### 步骤四：集成 Realtime SDK {#2dbad977}

本文以通过 CocoaPods 直接集成为例。如需手动集成，请参考[火山引擎 RTC 文档。](https://www.volcengine.com/docs/6348/70133)

1. 在终端窗口执行如下命令安装 [CocoaPods](https://cocoapods.org/)。
   ```Bash
   sudo gem install cocoapods
   ```
2. 进入项目根目录，执行如下命令，创建 `Podfile `文件。
   ```Bash
   pod init
   ```
3. 打开 `Podfile` 文件，并将其内容替换为以下代码。建议使用 VSCode 或其他代码编辑器打开项目文件。
   :::tip 说明
   请将 **`3.58.1.19400` **替换为 RTC 的目标版本号，具体版本信息可在[下载 RTC SDK](https://www.volcengine.com/docs/6348/75707#%E4%B8%8B%E8%BD%BD-sdk) 页面查看。
   :::
   ```Ruby
   # Uncomment the next line to define a global platform for your project
   # platform :ios, '9.0'
   source 'https://cdn.cocoapods.org/'
   source 'https://github.com/volcengine/volcengine-specs.git'
   
   target 'coze-swift' do
     # Comment the next line if you don't want to use dynamic frameworks
     use_frameworks!
     pod 'VolcEngineRTC', '3.58.1.19400'
   
     # Pods for RTCDemo-Swift
   
   end
   ```
4. 在终端窗口执行 `pod install` 命令安装 `VolcEngineRTC` 相关库。
   安装完成后，项目文件夹中将生成一个 **coze-objc.xcworkspace** 文件。使用 Xcode 打开该文件，以进行后续开发操作。
   ![Image=800x442](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/43b31dad4b4e4a6c8bae47110f06ceb3~tplv-goo7wpa0wc-image.image)
5. 编译与运行。
   编译项目，检查是否存在错误。在 Xcode 中，连接并选择 iOS 真机设备。单击 XCode 窗口左上角的运行按钮（或使用 **Command ⌘** + **R** 快捷键）。
   :::tip 说明
   仅支持在 iOS 真机设备上运行，不支持在模拟器运行。
   
   如果编译过程中提示错误，请参见[常见问题](/dev_how_to_guides/realtime_iOS#f92f0e6f)。
   :::   


### 步骤五：实现音视频通话 {#7cd845d2}

:::tip 说明
本文以 [ViewController.m](https://github.com/coze-dev/coze-ios/blob/main/coze-objc/coze-objc/ViewController.m) 中的实现步骤为例，讲解如何实现一个基本的音视频通话功能。本示例并未覆盖全部代码内容，如需查看完整代码，请从[音视频通话 iOS 示例项目](https://github.com/coze-dev/coze-ios)获取完整代码。
:::

#### 引入头文件 {#d3026267}

在`ViewController.swift` 或 `ViewController.h` 中引入必要的模块，并声明相关属性和方法。

::::tabs
@tab Swift
```Swift
import UIKit
import VolcEngineRTC

class ViewController: UIViewController, ByteRTCVideoDelegate, ByteRTCRoomDelegate {
    var rtcVideo: ByteRTCVideo?
    var rtcRoom: ByteRTCRoom?
    private var roomInfo: RoomData?
}
```



@tab Objective-C
```objectivec
#import <UIKit/UIKit.h>
#import <VolcEngineRTC/VolcEngineRTC.h>
#import "ApiResponse.h"

NS_ASSUME_NONNULL_BEGIN

@interface ViewController : UIViewController <ByteRTCVideoDelegate, ByteRTCRoomDelegate, UITableViewDelegate, UITableViewDataSource>
@end

NS_ASSUME_NONNULL_END
```


::::

#### 创建用户界面 {#36041f68}

在 `ViewController` 中实现 `createUI` 方法，创建本地视频预览视图，定义控制按钮。

::::tabs
@tab Swift
```Swift
func createUI() {
    let width = self.view.bounds.size.width
    let height = self.view.bounds.size.height
    
    // 本地预览视图占上半部分
    let previewHeight = height * 0.4
    localView.frame = CGRect(x: 0, y: 0, width: width, height: previewHeight)
    self.view.addSubview(localView)
    
    // 按钮区域
    let buttonY = previewHeight + 10
    let buttonWidth = (width - 30) / 2
    
    joinButton.frame = CGRect(x: 10, y: buttonY, width: buttonWidth, height: 44)
    cameraButton.frame = CGRect(x: width - buttonWidth - 10, y: buttonY, width: buttonWidth, height: 44)
    
    self.view.addSubview(joinButton)
    self.view.addSubview(cameraButton)
}
```



@tab Objective-C
```objectivec
- (void)createUI {
  CGFloat width = self.view.bounds.size.width;
  CGFloat height = self.view.bounds.size.height;

  // 本地预览视图
  CGFloat previewHeight = height * 0.4;
  self.localView = [[UIView alloc] initWithFrame:CGRectMake(0, 0, width, previewHeight)];
  self.localView.backgroundColor = [UIColor lightGrayColor];
  [self.view addSubview:self.localView];

  // 按钮区域
  CGFloat buttonY = previewHeight + 10;
  CGFloat buttonWidth = (width - 30) / 2;

  // 创建连接按钮
  self.joinButton = [UIButton buttonWithType:UIButtonTypeCustom];
  self.joinButton.frame = CGRectMake(10, buttonY, buttonWidth, 44);
  [self.joinButton setTitle:@"连接" forState:UIControlStateNormal];
  [self.joinButton addTarget:self action:@selector(connectButtonTapped) forControlEvents:UIControlEventTouchUpInside];
  
  // 创建其他控制按钮...
  
  [self.view addSubview:self.joinButton];
}
```


::::

#### 创建房间并获取房间信息 {#efdd29b4}

调用扣子编程的[创建房间](/developer_guides/create_room)接口创建房间，通过 `NetworkService` 获取房间信息。

::::tabs
@tab Swift
```Swift
do {
    // 获取房间信息
    let response = try await NetworkService.shared.createRoom(
        botId: APIConfig.botId,
        voiceId: APIConfig.voiceId
    )
    
    // 异常处理
    if response.code != 0 {
        throw NSError(
            domain: "", code: Int(response.code),
            userInfo: [NSLocalizedDescriptionKey: response.msg])
    }
    roomInfo = response.data
} catch {
    print("连接失败: \(error)")
}
```



@tab Objective-C
```objectivec
[[NetworkService shared] createRoomWithBotId:API_BOT_ID
                                   voiceId:API_VOICE_ID
                                completion:^(RoomResponse *response, NSError *error) {
    if (error || response.code != 0) {
        // 处理错误...
    } else {
        self.roomInfo = response.data;
        [self buildRTCEngine];
        [self bindLocalRenderView];
        [self joinRoom];
    }
}];
```


::::

:::tip 说明
创建房间后返回的 Token，其默认有效期为 3 分钟，如果 3 分钟内没有用户加入房间，或者用户静音 3 分钟，智能体将自动退出房间，房间随即被释放，后续若要再次和智能体对话，则需重新创建房间。
:::

#### 创建 RTC 引擎 {#c71812a7}

创建并初始化 RTC 引擎。

::::tabs
@tab Swift
```Swift
func buildRTCEngine() {
    guard let roomInfo = self.roomInfo else { return }
    
    self.rtcVideo = ByteRTCVideo.createRTCVideo(
        roomInfo.app_id, delegate: self, parameters: [:])
}
```



@tab Objective-C
```objectivec
- (void)buildRTCEngine {
  if (!self.roomInfo) {
    return;
  }

  self.rtcVideo = [ByteRTCVideo createRTCVideo:self.roomInfo.app_id
                                    delegate:self
                                  parameters:@{}];
  [self.rtcVideo startAudioCapture];
}
```


::::

#### 采集音视频并设置本端渲染 {#aa0df0f7}

1. 调用 `startAudioCapture()` 开启麦克风音频流采集，调用 `startVideoCapture()` 开启摄像头视频流采集。
2. 调用 `setLocalVideoCanvas()` 方法设置本端视频渲染视图。
   ::::tabs
   @tab Swift
   ```Swift
   // 开启音频采集
   self.rtcVideo?.startAudioCapture()
   
   // 开启视频采集（可选）
   self.rtcVideo?.startVideoCapture()
   ```
   
   
   
   @tab Objective-C
   ```objectivec
   // 开始音频采集
   [self.rtcVideo startAudioCapture];
   
   // 开始视频采集
   [self.rtcVideo startVideoCapture];
   
   - (void)bindLocalRenderView {
     ByteRTCVideoCanvas *canvas = [[ByteRTCVideoCanvas alloc] init];
   
   //设置本端视频渲染视图
     canvas.view = self.localView;
     canvas.renderMode = ByteRTCRenderModeHidden;
     [self.rtcVideo setLocalVideoCanvas:ByteRTCStreamIndexMain withCanvas:canvas];
   }
   ```
   
   
   ::::   


#### 创建并加入房间 {#2d194123}


1. 调用 `createRTCRoom` 接口创建 RTC 房间。
2. 调用 `joinRoom` 接口加入 RTC 房间。
   ::::tabs
   @tab Swift
   ```Swift
   // 创建房间
   self.rtcRoom = self.rtcVideo?.createRTCRoom(roomInfo.room_id)
   self.rtcRoom?.delegate = self
   
   let userInfo = ByteRTCUserInfo()
   userInfo.userId = roomInfo.uid
   
   let roomCfg = ByteRTCRoomConfig()
   roomCfg.isAutoPublish = true
   roomCfg.isAutoSubscribeAudio = true
   roomCfg.isAutoSubscribeVideo = true
   
   // 加入房间
   self.rtcRoom?.joinRoom(roomInfo.token, userInfo: userInfo, roomConfig: roomCfg)
   ```
   
   
   
   @tab Objective-C
   ```objectivec
   - (void)joinRoom {
     self.rtcRoom = [self.rtcVideo createRTCRoom:self.roomInfo.room_id];
     self.rtcRoom.delegate = self;
   
     ByteRTCUserInfo *userInfo = [[ByteRTCUserInfo alloc] init];
     userInfo.userId = self.roomInfo.uid;
   
     ByteRTCRoomConfig *roomConfig = [[ByteRTCRoomConfig alloc] init];
     roomConfig.isAutoPublish = YES;
     roomConfig.isAutoSubscribeAudio = YES;
     roomConfig.isAutoSubscribeVideo = YES;
   
     [self.rtcRoom joinRoom:self.roomInfo.token
                   userInfo:userInfo
                 roomConfig:roomConfig];
   }
   ```
   
   
   ::::   


#### 渲染本端视频流 {#588625f5}

调用 `setLocalVideoCanvas` 方法配置本端视频渲染视图。

::::tabs
@tab Swift
```Swift
func bindLocalRenderView() {
    let canvas = ByteRTCVideoCanvas.init()
    canvas.view = self.localView
    canvas.renderMode = .hidden
    self.rtcVideo?.setLocalVideoCanvas(.indexMain, withCanvas: canvas)
}
```



@tab Objective-C
```objectivec
- (void)bindLocalRenderView {
  ByteRTCVideoCanvas *canvas = [[ByteRTCVideoCanvas alloc] init];
  canvas.view = self.localView;
  canvas.renderMode = ByteRTCRenderModeHidden;
  [self.rtcVideo setLocalVideoCanvas:ByteRTCStreamIndexMain withCanvas:canvas];
}
```


::::

#### 实时字幕显示 {#690a6c24}

处理接收到的用户消息并实时显示字幕。

::::tabs
@tab Swift
当收到 `conversation.message.delta` 事件时，系统会根据事件类型处理消息：

* 如果是新消息，则通过`messageList.append(message)`将其添加到消息列表中。
* 如果是消息的增量更新，则通过`lastMessage += message`对最后一条消息进行追加更新。

处理完成后，调用`messageTableView.reloadData()`方法，刷新 UITableView 并显示最新的字幕内容。

```Swift
func addMessage(_ message: String, eventType: String) {
    DispatchQueue.main.async {
        if self.lastEventType == "conversation.message.delta" {
            if var lastMessage = self.messageList.last {
                lastMessage += message
                self.messageList[self.messageList.count - 1] = lastMessage
            }
        } else if eventType == "conversation.message.delta" {
            self.messageList.append(message)
        }
        
        self.lastEventType = eventType
        self.messageTableView.reloadData()
    }
}
```



@tab Objective-C
监听 `onUserMessageReceived` 回调，将收到的 `messageDict` 用户消息更新到界面上。

```objectivec
- (void)rtcRoom:(ByteRTCRoom *)rtcRoom
    onUserMessageReceived:(NSString *)uid
                  message:(NSString *)message {
  NSError *error;
  NSData *jsonData = [message dataUsingEncoding:NSUTF8StringEncoding];
  NSDictionary *messageDict = [NSJSONSerialization JSONObjectWithData:jsonData
                                                            options:0
                                                              error:&error];

  if (!error) {
    NSString *eventType = messageDict[@"event_type"];
    if ([eventType isEqualToString:@"conversation.message.delta"]) {
      NSString *content = messageDict[@"data"][@"content"] ?: @"";
      [self addMessage:content eventType:eventType];
    }
  }
}
```


::::

#### 开启或关闭本端视频流采集 {#20a10a13}

在 `cameraButtonTapped` 回调中，通过按钮的 `isSelected` 状态切换，调用 `startVideoCapture()` 或 `stopVideoCapture()`方法，实现摄像头的启用或禁用功能。

::::tabs
@tab Swift
```Swift
@objc private func cameraButtonTapped() {
    cameraButton.isSelected = !cameraButton.isSelected
    
    if cameraButton.isSelected {
        self.rtcVideo?.startVideoCapture()
    } else {
        self.rtcVideo?.stopVideoCapture()
    }
}
```



@tab Objective-C
```objectivec
- (void)cameraButtonTapped {
  self.cameraButton.selected = !self.cameraButton.selected;

  if (self.cameraButton.selected) {
    [self.rtcVideo startVideoCapture];
  } else {
    [self.rtcVideo stopVideoCapture];
  }
}
```


::::

#### 静音或取消静音 {#4c9e153d}

在 `muteButtonTapped` 回调中，根据按钮的选中状态调用 `startAudioCapture()` 或 `stopAudioCapture()`方法，从而实现麦克风的启用或静音功能。

::::tabs
@tab Swift
```Swift
@objc private func muteButtonTapped() {
    muteButton.isSelected = !muteButton.isSelected
    
    if muteButton.isSelected {
        self.rtcVideo?.stopAudioCapture()
    } else {
        self.rtcVideo?.startAudioCapture()
    }
}
```



@tab Objective-C
```objectivec
- (void)muteButtonTapped {
  self.muteButton.selected = !self.muteButton.selected;

  if (self.muteButton.selected) {
    [self.rtcVideo stopAudioCapture];
  } else {
    [self.rtcVideo startAudioCapture];
  }
}
```


::::

#### 打断通话 {#133b44c4}

调用 `sendUserMessage` 方法，实现在语音通话过程中，用户可以打断通话。打断通话后，将停止音频流输出。

::::tabs
@tab Swift
```Swift
@objc private func interruptButtonTapped() {
    let message = [
        "id": "event_1",
        "event_type": "conversation.chat.cancel",
        "data": "{}"
    ]
    
    do {
        let jsonData = try JSONSerialization.data(withJSONObject: message)
        if let jsonString = String(data: jsonData, encoding: .utf8) {
            self.rtcRoom?.sendUserMessage(
                APIConfig.botId, 
                message: jsonString,
                config: ByteRTCMessageConfig.reliableOrdered)
        }
    } catch {
        print("Error creating JSON: \(error)")
    }
}
```



@tab Objective-C
```objectivec
- (void)interruptButtonTapped {
  NSDictionary *message = @{
    @"id" : @"event_1",
    @"event_type" : @"conversation.chat.cancel",
    @"data" : @"{}"
  };

  NSError *error;
  NSData *jsonData = [NSJSONSerialization dataWithJSONObject:message
                                                   options:0
                                                     error:&error];

  if (!error) {
    NSString *jsonString = [[NSString alloc] initWithData:jsonData
                                               encoding:NSUTF8StringEncoding];
    [self.rtcRoom sendUserMessage:API_BOT_ID
                        message:jsonString
                         config:ByteRTCMessageConfigReliableOrdered];
  }
}
```


::::

#### 停止音视频通话 {#a763391f}

1. 依次调用 `leaveRoom` 和`destroy` 接口离开并销毁房间。
2. 调用`destroyRTCVideo` 接口释放引擎资源，避免内存泄漏。

::::tabs
@tab Swift
```Swift
deinit {
    // 销毁房间
    self.rtcRoom?.leaveRoom()
    self.rtcRoom?.destroy()
    self.rtcRoom = nil
    
    // 销毁引擎
    ByteRTCVideo.destroyRTCVideo()
    self.rtcVideo = nil
}
```



@tab Objective-C
```objectivec
- (void)dealloc {
  [self.rtcRoom leaveRoom];
  [self.rtcRoom destroy];
  self.rtcRoom = nil;
  [ByteRTCVideo destroyRTCVideo];
  self.rtcVideo = nil;
}
```


::::

:::tip 说明
在实现音视频通话后，如遇无声音、无画面、视频卡顿等问题时，您可以使用[诊断工具](https://www.volcengine.com/docs/6348/125643)快速排查和定位异常房间及用户，并获取异常根因分析、处理建议、分析报告等。
:::

### 信令事件 {#25b45f09}

#### **事件类型** {#1d42d962}

智能语音信令事件包括上行事件和下行事件。每个事件有 ID 和 EventType， 通过 EventType 可以区分具体的事件类型，每个事件类型对应的 Payload 在 Data 中，开发者可以按需去提取需要的内容。

* **上行事件**：设备端上报给服务端的事件。应用程序需要根据扣子编程提供的事件结构，在触发事件时填充字段内容并上报事件。设备端需要在监听到 Realtime SDK 的 onUserJoined 回调智能体进房后才能发送上行事件，可通过 Realtime SDK 的 `sendUserMessage` 发送，如果是嵌入式设备集成音视频，可通过 Realtime SDK 的 `byte_rtc_rts_send_message` 发送。详细信息可参考[Realtime 上行事件](/developer_guides/signaling_uplink_event)。
* **下行事件**：服务端下发给设备端的事件，可订阅 Realtime SDK的 `onUserMessageReceived`回调，如果是嵌入式设备集成音视频，可订阅 Realtime SDK 的 ` on_message_received`回调，接收下行事件。应用程序需要解析下行事件，并根据业务需求进行下一步操作。详细信息可参考[Realtime 下行事件](/developer_guides/signaling_downlink_event)。

#### **公共参数** {#782ae389}

智能语音信令事件的公共参数如下：

<!-- @cols-width: 100,162,500 -->
|**参数名称** |**类型** |**描述** |
|---|---|---|
|id |String |事件 ID，也就是事件的唯一标识。由客户端或服务端生成，在故障排查场景下用于定位具体的事件，便于排查问题。 |
|event_type |String |事件的类型。 |
|data |JSON |事件的详细信息，其中包含具体事件的业务字段。 |

#### 信令事件的使用流程 {#6dc71b67}

信令事件的使用流程如下：

1. 初始化。通过监听 `session.created` 事件，确认房间初始化完成。
2. 发送请求。使用上行事件（如 `conversation.message.create`）向智能体发送消息。
3. 处理响应。监听下行事件（如 `conversation.message.delta`）获取智能体的增量回复。
4. 插件交互。在收到事件 `conversation.chat.requires_action` 后，执行插件操作并通过事件 `conversation.chat.submit_tool_outputs` 提交结果。
5. 错误处理。通过监听 `error` 事件捕获和处理异常情况。

使用示例如下：

::::tabs
@tab Swift
```Swift
// 发送消息
let message = [
    "id": "event_1",
    "event_type": "conversation.message.create",
    "data": [
        "role": "user",
        "content_type": "text",
        "content": "讲一个笑话"
    ],
]

do {
    let jsonData = try JSONSerialization.data(withJSONObject: message)
    if let jsonString = String(data: jsonData, encoding: .utf8) {
        self.rtcRoom?.sendUserMessage(
            APIConfig.botId, message: jsonString,
            config: ByteRTCMessageConfig.reliableOrdered)
    }
} catch {
    print("Error creating JSON: \(error)")
}
```



@tab Objective-C
```Java
// 发送消息
  NSDictionary *message = @{
    @"id" : @"event_1",
    @"event_type" : @"conversation.message.create",
    @"data" : @{
        @"role": @"user",
        @"content_type": @"text",
        @"content": @"讲一个笑话"
    }
  };

  NSError *error;
  NSData *jsonData = [NSJSONSerialization dataWithJSONObject:message
                                                     options:0
                                                       error:&error];

  if (!error) {
    NSString *jsonString = [[NSString alloc] initWithData:jsonData
                                                 encoding:NSUTF8StringEncoding];
    [self.rtcRoom sendUserMessage:API_BOT_ID
                          message:jsonString
                           config:ByteRTCMessageConfigReliableOrdered];
  }
```


::::

#### 信令事件的处理思路 {#9a07e634}

在处理信令事件时，建议采用以下思路：

* **监听所有事件**：捕获客户端和服务端的所有交互，便于调试和监控。扣子编程推荐你监听所有的事件，你也可以根据实际的业务需求，监听不同类型的事件，例如客户端事件、服务端事件等。
* **处理特定事件**：根据业务需求，监听和处理特定的事件，例如连接成功、中断、断开、音频状态变化等。
* **错误处理**：捕获和处理错误事件，确保应用的稳定性和用户体验。

示例代码如下：

::::tabs
@tab Swift
```Swift
func rtcRoom(_ rtcRoom: ByteRTCRoom, onUserMessageReceived uid: String, message: String) {
    print("收到用户消息 - 用户ID: \(uid), 消息: \(message)")

    do {
        if let jsonData = message.data(using: .utf8) {
            let messageData = try JSONDecoder().decode(MessageData.self, from: jsonData)

            if messageData.event_type == "conversation.message.delta"
                || messageData.event_type == "conversation.message.completed"
            {
                let content = messageData.data?.content ?? ""
                self.addMessage(content, eventType: (messageData.event_type)!)
            }
        }
    } catch {
        print("JSON 解析错误: \(error)")
    }
}
```



@tab Objective-C
```objectivec
// 监听所有事件
- (void)rtcRoom:(ByteRTCRoom *)rtcRoom
    onUserMessageReceived:(NSString *)uid
                  message:(NSString *)message {
  NSLog(@"收到用户消息 - 用户ID: %@, 消息: %@", uid, message);

  NSError *error;
  NSData *jsonData = [message dataUsingEncoding:NSUTF8StringEncoding];
  NSDictionary *messageDict = [NSJSONSerialization JSONObjectWithData:jsonData
                                                              options:0
                                                                error:&error];
}
```


::::

## 常见问题 {#f92f0e6f}

### 编译时提示 **`Sandbox: rsync.samba(xxxxx) deny(1)`** {#41116782}

Xcode 15 及以上版本如果提示该错误，请按以下步骤进行处理：

在 Xcode 中，选中项目，选择 **TARGETS** > **项目名称** > **Build Settings**，在 **Build Options** 区域，将 **User Script Sandboxing** 的值修改为 **No**。

![Image=800x376](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/83e4d9e67b1243aab894fd22412f4a92~tplv-goo7wpa0wc-image.image)

### 编译时提示 **`No such module 'VolcEngineRTC'`** {#cc56d79f}

请使用 iOS 真机进行测试，不支持使用模拟器运行。

![Image=800x380](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c9d586da690b42ac809907d185a98441~tplv-goo7wpa0wc-image.image)

### 提示 `doesn't match RTCDemo-Swift.app's iOS  deployment target` {#2c0300d6}

![Image=600x454](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/00d46886cb1a4409a44035b00b22a99b~tplv-goo7wpa0wc-image.image)

该错误可能是由于真机的 iOS 版本与 Xcode 的配置版本不一致导致的。解决方法如下：

在 Xcode 中，选中项目，选择 **TARGETS** > **项目名称** > **General**。在 **Minimum Deployments** 区域，将 iOS 版本号修改为与真机一致的版本。

![Image=800x597](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/ecd24e44926447cdbf1ddaeaa3a63fa3~tplv-goo7wpa0wc-image.image)

##  {#9a2d4d4d}

