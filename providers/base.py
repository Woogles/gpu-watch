from abc import ABC
from abc import abstractmethod


class MarketplaceProvider(ABC):

    name = "Base"

    @abstractmethod
    def search(
        self,
        gpu_name,
        max_price
    ):
        pass