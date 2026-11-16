import praw

from models import Listing
from providers.base import MarketplaceProvider


class Provider(MarketplaceProvider):

    name = "Reddit"

    def __init__(self):

        self.client = praw.Reddit(
            client_id="REPLACE_ME",
            client_secret="REPLACE_ME",
            user_agent="gpuwatch"
        )

    def search(
        self,
        gpu_name,
        max_price
    ):

        listings = []

        results = (
            self.client
            .subreddit("hardwareswap")
            .search(
                gpu_name,
                sort="new",
                limit=25
            )
        )

        for post in results:

            listings.append(
                Listing(
                    source=self.name,
                    listing_id=post.id,
                    title=post.title,
                    gpu_name=gpu_name,
                    price=0,
                    condition="used",
                    url=f"https://reddit.com{post.permalink}"
                )
            )

        return listings