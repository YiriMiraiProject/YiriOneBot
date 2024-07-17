from typing import Any, Optional


class InterfaceCallFailed(BaseException):
    def __init__(self, action: str, params: Optional[dict[str, Any]], retcode: int):
        super().__init__(
            f"调用 API {action}(params: {params}) 时出错，错误代码：{retcode}"
        )
