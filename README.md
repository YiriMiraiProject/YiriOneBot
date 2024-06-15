# YiriMiraiOneBot

![OneBot: 12 (shields.io)](https://img.shields.io/badge/OneBot-12-black) ![GitHub License](https://img.shields.io/github/license/YiriMiraiProject/YiriMiraiOneBot) ![GitHub Repo stars](https://img.shields.io/github/stars/YiriMiraiProject/YiriMiraiOneBot) [![codecov](https://codecov.io/gh/XYCode-Kerman/YiriMiraiOneBot/graph/badge.svg?token=6ZBJ2BfX4B)](https://codecov.io/gh/XYCode-Kerman/YiriMiraiOneBot)

YiriMiraiOneBot 是一个 OneBot 12 协议上的 Python SDK，延续 YiriMirai 项目轻量级、低耦合的编码风格。

尽管 YiriMiraiOneBot 中带有 Mirai 字样，但由于 OneBot 协议在多个平台上都有不同的实现，因此你也可以将其用于 [LagRange](https://github.com/LagrangeDev/Lagrange.Core) 等项目。并且，从 OneBot 12 开始，OneBot 标准不再与 QQ 紧耦合 
，而是适用于一切支持聊天机器人的地方，因此你也可以将本项目用于编写其他平台上的机器人。

> 警告：YiriMiraiOneBot 正处于开发状态，请勿将其用于生产环境。

## 功能
* 适配器
  * [ ] HTTP 适配器
  * [ ] HTTP Webhook 适配器
  * [ ] 正向 WebSocket 适配器
  * [x] 反向 Websocket 适配器
* 消息类型
  * [x] Text
  * [x] Image
  * [x] Mention
  * [x] Mention_all
  * [x] Voice
  * [x] Audio
  * [x] Video
  * [x] File
  * [x] Location
  * [x] Reply
* 接口定义
  * [ ] 元接口
    * [ ] 元事件
    * [ ] 元动作
  * [ ] 消息接口
    * [x] 消息段
    * [ ] 消息动作
  * [ ] 单用户接口
    * [ ] 用户消息事件
    * [ ] 用户通知事件
    * [ ] 用户动作
  * [ ] 单级群组接口
    * [ ] 群消息事件
    * [ ] 群通知事件
    * [ ] 群动作
  * [ ] 两级群组接口
    * [ ] 群组消息事件
    * [ ] 群组通知事件
    * [ ] 群组动作
  * [ ] 文件接口
    * [ ] 文件动作

## 安装

您可以将本仓库克隆到本地并作为一个目录使用：

```bash
git clone https://github.com/YiriMiraiProject/YiriMiraiOneBot.git ./YiriMiraiOneBot
cd YiriMiraiOneBot
poetry install
```

## 使用

WIP...

## 参与开发

参与 YiriMiraiOneBot 的开发，需要遵循开发守则（WIP），并为新添加的代码提供测试代码。

## 开源协议

本项目采用 LGPL-3.0、Anti-996 许可证开源，因此使用本项目时，你需要注意以下几点：

1. 你可以自由的在代码中以`import`的形式导入并使用 YiriMiraiOneBot 提供的功能，**而不需要开源你使用 YiriMiraiOneBot 编写的业务代码**。

2. 如果你对 YiriMiraiOneBot 的代码进行了修改，**你需要同时发布你修改后的 YiriMiraiOneBot**。

3. 如果你引用或修改了本库中的代码（包括`import`本库），你就必须**遵守你所在司法管辖区与劳动和就业相关法律、法规、规则和标准**。

   如果该司法管辖区没有此类法律、法规、规章和标准或其法律、法规、规章和标准不可执行，则你**必须遵守国际劳工标准的核心公约**。

4. 使用`0d8f2f`提交以前的代码时，请遵循 AGPL-3.0 协议。

5. 有关LGPL-3.0许可证的更多详细信息，请参见 [GNU 宽通用公共许可证 v3.0 - GNU 工程 - 自由软件基金会](https://www.gnu.org/licenses/lgpl-3.0.html)。

6. 有关Anti-996许可证的更多详细信息，请参见[Anti-996 License Version 1.0](https://github.com/kattgu7/Anti-996-License)和[996.ICU](https://996.icu/#/zh_CN)。