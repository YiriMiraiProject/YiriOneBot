# Changelog

<a name="0.0.1-infdev.1"></a>
## 0.0.1-infdev.1 (2024-06-15)

### Added

- ✨ 新增API调用功能 [[359f9ab](https://github.com/YiriMiraiProject/YiriOneBot/commit/359f9aba40b6d0bdaf6eaa94d38bc9e54de9f6a4)]
- ✨ (bot) 自动设置self值 [[05d7c0f](https://github.com/YiriMiraiProject/YiriOneBot/commit/05d7c0fa152e64993164c22004f9df852ff0d572)]
- ✨ (api) 支持发送私聊、频道消息 [[b3c416c](https://github.com/YiriMiraiProject/YiriOneBot/commit/b3c416c85140c55b10749ece09694b601a5357bc)]
- ✨ (api) 支持基本API [[4cd4af5](https://github.com/YiriMiraiProject/YiriOneBot/commit/4cd4af5b27a109ef495337b0e213b5758c251af6)]
- ✨ 新增Bot类，并且可通过EventBase来监听事件 [[2bff5c5](https://github.com/YiriMiraiProject/YiriOneBot/commit/2bff5c5a753e2d556815770105324ff8cb462ab8)]
- ✨ (adapters) 新增启动、停止适配器的接口 [[336f596](https://github.com/YiriMiraiProject/YiriOneBot/commit/336f596d0c4cde97cc4a66081a5e6c1ec6a7e14b)]

### Changed

- ♻️ 修改标准示例 [[877750b](https://github.com/YiriMiraiProject/YiriOneBot/commit/877750b976873d7d3e64456c199e8de9c3350880)]
- ♻️ 提升代码质量 [[fe39d55](https://github.com/YiriMiraiProject/YiriOneBot/commit/fe39d5501bce8c0e8c729ecf400be343ba65f43a)]

### Fixed

- 🐛 (message/message_components) 修复测试错误 [[0d8f2f7](https://github.com/YiriMiraiProject/YiriOneBot/commit/0d8f2f74f72e7df9f96c1439932a81c71324df5c)]
- 🐛 (adapters/reverse_websocket_adapter) 修复OneBot实现发送的数据不符合规范时程序异常退出的问题 [[ec827ed](https://github.com/YiriMiraiProject/YiriOneBot/commit/ec827ed2bff197cf5786428e99531c20d9e9854a)]

### Miscellaneous

- 📄 换用LGPL和Anti-996许可证 [[7f0e791](https://github.com/YiriMiraiProject/YiriOneBot/commit/7f0e7910204d7876d3b77dbf3ee35a20ec988f1e)]
- 🗑️ (examples) 示例用.py文件写而不是jupyter notebook [[70b9ab1](https://github.com/YiriMiraiProject/YiriOneBot/commit/70b9ab19789e332b84c73e3310383f3af3c576e1)]
-  新增：EventBus可以监听基于EventBase的事件 [[b93a946](https://github.com/YiriMiraiProject/YiriOneBot/commit/b93a9464071c217a4159ce2ef055f0743d4db5d3)]
-  新增：常见事件 [[f8200fb](https://github.com/YiriMiraiProject/YiriOneBot/commit/f8200fb08bba6b8558e0e4b5965929bb233fdf88)]
-  新增：可从字典加载MessageChain [[bd9137f](https://github.com/YiriMiraiProject/YiriOneBot/commit/bd9137f1815d9c9d2f82fd440feb901b0a82b67a)]
-  修复：Audio类的message_type依然是image [[4291bb9](https://github.com/YiriMiraiProject/YiriOneBot/commit/4291bb944177e1a7732fa1d3b9682f0406a61e01)]
-  新增：完善测试覆盖率到100% [[ed23553](https://github.com/YiriMiraiProject/YiriOneBot/commit/ed235530a66cbcd5d939943653f95365e4dffde9)]
-  新增：构造消息链、消息组件 [[74eef55](https://github.com/YiriMiraiProject/YiriOneBot/commit/74eef55160a7551693dc7b5397b7389721663d3b)]
-  修改：README [[6a23153](https://github.com/YiriMiraiProject/YiriOneBot/commit/6a231538053b7f34184bcc6a6d2a76025c6517d5)]
-  Merge pull request [#1](https://github.com/YiriMiraiProject/YiriOneBot/issues/1) from YiriMiraiProject/develop [[7afb211](https://github.com/YiriMiraiProject/YiriOneBot/commit/7afb211be01464ccdea2f108f24db4729f729bb5)]
-  修改：改进CodeCov显示 [[c4fe874](https://github.com/YiriMiraiProject/YiriOneBot/commit/c4fe874f313024ffe0e81bedbd7de095c6188d1a)]
-  修复：Linux下rwebsocket测试无法正常运行 [[0ed8329](https://github.com/YiriMiraiProject/YiriOneBot/commit/0ed8329aa025d05d02959e148fa6f6167f479fa8)]
-  增加：基于Github Actions的自动测试 [[f1691a8](https://github.com/YiriMiraiProject/YiriOneBot/commit/f1691a83ae24b1e6183eae70d11dd4d1605dda05)]
-  修复：反向Websocket适配器BUG [[7c8e254](https://github.com/YiriMiraiProject/YiriOneBot/commit/7c8e254d822374ac821292f2a60456a1e95d4854)]
-  增加：反向Websocket适配器（待测试） [[1647144](https://github.com/YiriMiraiProject/YiriOneBot/commit/1647144c22dd38c293e893f732697c6a4703430a)]
-  修改：默认日志等级修改为INFO [[708008d](https://github.com/YiriMiraiProject/YiriOneBot/commit/708008d40e42bed5ffe584fd9c923a574315721c)]
-  修复：触发未被监听的事件时报错 [[1bd016a](https://github.com/YiriMiraiProject/YiriOneBot/commit/1bd016afd9088b2ffebd5759d6a2d8b34861c7f2)]
-  修改：格式化代码 [[9fd1c88](https://github.com/YiriMiraiProject/YiriOneBot/commit/9fd1c88a07260d52b5cbc323064e5bf0a52e66c7)]
-  新增：实现事件总线 [[4676de2](https://github.com/YiriMiraiProject/YiriOneBot/commit/4676de27cdbd2ad2f1ae9a4aff60fc443db6a2c9)]
-  初始化项目 [[f7361e7](https://github.com/YiriMiraiProject/YiriOneBot/commit/f7361e7850190d3ab51de2c1d7384b001b08a585)]
-  Initial commit [[7df2164](https://github.com/YiriMiraiProject/YiriOneBot/commit/7df216497e1ad0c9cbd683b178772faa2cd391be)]


