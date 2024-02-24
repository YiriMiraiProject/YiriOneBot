import abc


class ApiProvider(abc.ABC):
    """用于提供Api调用。"""

    @abc.abstractmethod
    async def call_api(self, api: str, **params):
        """调用Api

        Args:
            api (str): 该api的名称，例如send_message。
            params (dict): 调用api的参数。
        """
