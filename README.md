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
  * [ ] Text
  * [ ] Image
  * [ ] Mention
  * [ ] Mention_all
  * [ ] Voice
  * [ ] Audio
  * [ ] Video
  * [ ] File
  * [ ] Location
  * [ ] Reply
* 接口定义
  * [ ] 元接口
    * [ ] 元事件
    * [ ] 元动作
  * [ ] 消息接口
    * [ ] 消息段
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

参与 YiriMiraiOneBot 的开发，需要遵循 < u > 开发守则（WIP）</u>，并为新添加的代码提供测试代码。

## 开源协议

本项目采用 AGPL-3.0 协议。请注意，AGPL-3.0 是传染性协议。如果你的项目引用了 YiriMiraiOneBot，请在发布时公开源代码，并同样采用 AGPL-3.0 协议。