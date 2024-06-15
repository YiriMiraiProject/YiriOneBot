import abc
import secrets
from typing import Any, Dict, Type, Union

from mirai_onebot.api.interfaces.base import Request, Response


class ApiProvider(abc.ABC):
    """用于提供Api调用。"""

    @abc.abstractmethod
    async def _call_api(self, action: str, params: dict, echo: str = secrets.token_hex(8)) -> Union[Dict[str, Any], None]:
        """内部接口。直接调用API

        Args:
            action (str): 动作名
            params (dict): 参数
            echo (str): 回显数值，用于标识唯一请求
        """

    async def call(self, request: Request, response_type: Type[Response]):
        """调用API

        Args:
            api (Request): API接口
        """
        resp = await self._call_api(request.action, request.params.model_dump(mode='json'), request.echo if request.echo is not None else secrets.token_hex(8))
        return response_type.model_validate(resp)
