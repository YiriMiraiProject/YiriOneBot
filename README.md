<div align="center">
  Yiri OneBot
  <br />
  <a href="#about"><strong>Explore the docs »</strong></a>
  <br />
  <br />
  <a href="https://github.com/YiriMiraiProject/YiriOneBot/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/YiriMiraiProject/YiriOneBot/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .<a href="https://github.com/YiriMiraiProject/YiriOneBot/discussions">Ask a Question</a>
</div>

<div align="center">
<br />

[![Project license](https://img.shields.io/github/license/YiriMiraiProject/YiriOneBot.svg?style=flat-square)](LICENSE)

[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/YiriMiraiProject/YiriOneBot/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![code with love by YiriMiraiProject](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-YiriMiraiProject-ff1414.svg?style=flat-square)](https://github.com/YiriMiraiProject)

</div>



---

## 关于

Yiri OneBot 是一个 OneBot 12 协议上的 Python SDK，延续 YiriMirai 项目轻量级、低耦合的编码风格。

尽管 Yiri OneBot 中带有 Mirai 字样，但由于 OneBot 协议在多个平台上都有不同的实现，因此你也可以将其用于 [LagRange](https://github.com/LagrangeDev/Lagrange.Core) 等项目。并且，从 OneBot 12 开始，OneBot 标准不再与 QQ 紧耦合 ，而是适用于一切支持聊天机器人的地方，因此你也可以将本项目用于编写其他平台上的机器人。

### 特性

Yiri OneBot 在设计之初便是支持**异步并发**的，因此你可以用它来编写高性能的机器人应用，或者是开发**SaaS**应用，并将其用于多个场景之中。

Yiri OneBot 不再**与 `mirai-api-http` 耦合**，而是适用于一切支持 OneBot 11/12 标准的地方。

Yiri OneBot 的姊妹项目 YiriBot 正在开发，该框架将提供更多适用于聊天机器人开发的**高级API**和**插件系统**。

## 快速上手

### 先决条件

你需要拥有一台安装了**Windows**或**Linux**操作系统的计算机，并在上方安装**Python 3.8 及以上**的解释器和**Poetry** 包管理器。

### 安装

您可以从 PyPI 安装它:

```bash
pip install yiri-mirai-onebot
```

您也可以手动安装:
```bash
git clone https://github.com/YiriMiraiProject/YiriOneBot.git
poetry install
```

## 使用

更多详情，请查看 [快速上手 - Yiri OneBot Documents](https://docs.yiri-mirai.online/getting-started/)。

## 开发路线图

查看 [Issues](https://github.com/YiriMiraiProject/YiriOneBot/issues) 了解我们的开发计划（和可能的Bug），以及：

- [近期的新功能计划](https://github.com/YiriMiraiProject/YiriOneBot/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc)
- [最严重的 Bug](https://github.com/YiriMiraiProject/YiriOneBot/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc)
- [最新的 Bug](https://github.com/YiriMiraiProject/YiriOneBot/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

## 获取支持

你可以通过如下方式来获取我们的支持：

- [GitHub Discussions](https://github.com/YiriMiraiProject/YiriOneBot/discussions)
- 联系 [YiriMirai Project](https://github.com/YiriMiraiProject) 的组织成员

## 帮助我们的开发

如果您想对 Yiri OneBot 的积极开发表示**感谢**或/和支持：

- 为项目添加 [GitHub Star](https://github.com/YiriMiraiProject/YiriOneBot)。
- 在 Twitter 上谈论 Yiri OneBot。
- 在 [Dev.to](https://dev.to/)、[Medium](https://medium.com/) 或您的个人博客上撰写有关该项目的有趣文章。

让我们一起努力，让 Yiri OneBot 变得**更好**！

## 做出贡献

首先，感谢您抽出时间为我们做出贡献！有了您的贡献，开源社区才能成为学习、启发和创造的好地方。您的任何贡献都将惠及其他人，我们将**感激不尽**。


请阅读[我们的贡献指南](docs/CONTRIBUTING.md)，并感谢您的参与！

## 作者和其他贡献者

这个项目最初由 [Yiri Mirai Project](https://github.com/YiriMiraiProject) 的成员 [XYCode Kerman](https://github.com/XYCode-Kerman) 发起。

有关所有作者和贡献者的完整名单，请参阅[贡献者页面](https://github.com/YiriMiraiProject/YiriOneBot/contributors)。

## 安全性

Yiri OneBot 遵循良好的安全惯例，但无法保证 100% 的安全性。

Yiri OneBot 按**"原样 "**提供，不提供任何**担保**。使用风险自负。

如需了解更多信息和报告安全问题，请参阅我们的[安全文档](docs/SECURITY.md)。

> [!caution]
>
> 请勿通过 Issue 或 Discussion 报告安全性问题，你应当将其发送至 [security@yiri-mirai.online](mailto:security@yiri-mirai.online)。

## 许可证

本项目采用 **GNU 宽通用公共许可证 v3** 和 **反 996 许可证** 开源，因此使用本项目时，你需要注意以下几点：

1. 你可以自由的在代码中以`import`的形式导入并使用 YiriOneBot 提供的功能，**而不需要开源你使用 YiriOneBot 编写的业务代码**。
2. 如果你对 YiriOneBot 的代码进行了修改，**你需要同时发布你修改后的 YiriOneBot**。
3. 如果你引用或修改了本库中的代码（包括`import`本库），你就必须**遵守你所在司法管辖区与劳动和就业相关法律、法规、规则和标准**。
   如果该司法管辖区没有此类法律、法规、规章和标准或其法律、法规、规章和标准不可执行，则你**必须遵守国际劳工标准的核心公约**。
4. 使用`0d8f2f`提交以前的代码时，请遵循 AGPL-3.0 协议。
5. 有关LGPL-3.0许可证的更多详细信息，请参见 [GNU 宽通用公共许可证 v3.0 - GNU 工程 - 自由软件基金会](https://www.gnu.org/licenses/lgpl-3.0.html)。
6. 有关Anti-996许可证的更多详细信息，请参见[Anti-996 License Version 1.0](https://github.com/kattgu7/Anti-996-License)和[996.ICU](https://996.icu/#/zh_CN)。

## 虚拟形象

本项目的虚拟形象采用 **Stable Diffusion** 绘制，原画使用 CounterfeitXL-2.5 绘制，Lora 基于 SD 1.5 及以下版本。

详情可见：[[Lora] Yiri - 0.0.1](https://tusiart.com/models/741735105371917919)。

![](./docs/images/vtuber.png)

## 致谢

在本项目的开发过程中，我们深受开源软件社区的启发和支持。没有这些无私的开源贡献者，我们的项目将无法实现。

首先，我们向所有参与开源项目的开发者表示最诚挚的感谢。是你们的努力和智慧，构建了一个强大、灵活且不断进步的技术生态系统，让我们能够站在巨人的肩膀上，实现创新和突破。

特别感谢**Pydantic**和**Websockets**库的维护者和贡献者，你们的代码为我们提供了坚实的基础，使我们能够专注于项目的核心功能和创新点。

其次，我们向所有支持和推动**开源运动**、**自由软件运动**、**反 996 运动**的组织和个人以及致敬。你们的努力让开源不仅仅是一种技术实践，更是一种促进知识共享、协作和创新的文化。

我们相信，开源的力量将继续推动技术的发展和创新，我们期待与开源社区共同成长，为建设一个更加开放和协作的技术世界贡献力量。
