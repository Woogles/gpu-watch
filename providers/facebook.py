from urllib.parse import quote

from models import Listing
from providers.base import MarketplaceProvider


class Provider(MarketplaceProvider):

    name = "Facebook"

    def search(
        self,
        gpu_name,
        max_price
    ):

        url = (
            "https://www.facebook.com/"
            "marketplace/search/"
            f"?query={quote(gpu_name)}"
        )

        return [
            Listing(
                source=self.name,
                listing_id=gpu_name,
                title=f"Search {gpu_name}",
                gpu_name=gpu_name,
                price=0,
                condition="unknown",
                url=url
            )
        ]
