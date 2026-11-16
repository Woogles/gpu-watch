import json
import importlib

from config import (
    CSV_FILE,
    DATABASE_FILE,
    PROVIDERS_FILE
)

from csv_loader import load_targets
from database import Database
from filters import passes_price_filter
from reporting import generate_report
from mailer import send_report


def load_providers():

    config = json.loads(
        PROVIDERS_FILE.read_text()
    )

    loaded = []

    for name in config["providers"]:

        module = (
            importlib.import_module(
                f"providers.{name}"
            )
        )

        loaded.append(
            module.Provider()
        )

    return loaded


def main():

    providers = (
        load_providers()
    )

    targets = (
        load_targets(CSV_FILE)
    )

    db = Database(
        DATABASE_FILE
    )

    matches = []

    for gpu in targets:

        ceiling = max(
            gpu.max_used,
            gpu.max_new
        )

        for provider in providers:

            try:

                listings = (
                    provider.search(
                        gpu.name,
                        ceiling
                    )
                )

            except Exception as ex:

                print(
                    provider.name,
                    ex
                )

                continue

            for listing in listings:

                if not passes_price_filter(
                    listing,
                    gpu
                ):
                    continue

                previous = (
                    db.get_previous_price(
                        listing.listing_id
                    )
                )

                if (
                    previous is None
                    or
                    listing.price < previous
                ):
                    matches.append(
                        listing
                    )

                db.save_listing(
                    listing
                )

    if not matches:

        print(
            "No deals found."
        )

        return

    html = generate_report(
        matches
    )

    send_report(html)

    print(
        f"Found {len(matches)} matches."
    )


if __name__ == "__main__":
    main()