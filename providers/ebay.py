import os
import requests

from models import Listing
from providers.base import MarketplaceProvider


class Provider(MarketplaceProvider):

    name = "eBay"

    def __init__(self):

        self.token = self.get_token()

    def get_token(self):

        response = requests.post(
            "https://api.ebay.com/"
            "identity/v1/oauth2/token",
            auth=(
                os.environ["EBAY_CLIENT_ID"],
                os.environ["EBAY_CLIENT_SECRET"]
            ),
            headers={
                "Content-Type":
                "application/x-www-form-urlencoded"
            },
            data={
                "grant_type":
                "client_credentials",
                "scope":
                "https://api.ebay.com/oauth/api_scope"
            }
        )

        response.raise_for_status()

        return response.json()[
            "access_token"
        ]

    def search(
        self,
        gpu_name,
        max_price
    ):

        response = requests.get(
            "https://api.ebay.com/"
            "buy/browse/v1/item_summary/search",
            headers={
                "Authorization":
                f"Bearer {self.token}"
            },
            params={
                "q": gpu_name,
                "limit": 50,
                "filter":
                f"price:[..{max_price}]"
            }
        )

        response.raise_for_status()

        listings = []

        for item in (
            response
            .json()
            .get(
                "itemSummaries",
                []
            )
        ):

            listings.append(
                Listing(
                    source=self.name,
                    listing_id=item["itemId"],
                    title=item["title"],
                    gpu_name=gpu_name,
                    price=float(
                        item["price"]["value"]
                    ),
                    condition=item.get(
                        "condition",
                        "unknown"
                    ),
                    url=item.get(
                        "itemWebUrl",
                        ""
                    )
                )
            )

        return listings