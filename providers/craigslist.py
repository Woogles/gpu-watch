import feedparser

from models import Listing
from providers.base import MarketplaceProvider


class Provider(MarketplaceProvider):

    name = "Craigslist"

    def search(
        self,
        gpu_name,
        max_price
    ):

        feed_url = (
            "https://washingtondc.craigslist.org/"
            f"search/sss?query={gpu_name}"
            "&format=rss"
        )

        feed = feedparser.parse(
            feed_url
        )

        listings = []

        for item in feed.entries:

            listings.append(
                Listing(
                    source=self.name,
                    listing_id=item.id,
                    title=item.title,
                    gpu_name=gpu_name,
                    price=0,
                    condition="unknown",
                    url=item.link
                )
            )

        return listings