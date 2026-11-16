def normalize_condition(condition):

    c = condition.lower()

    if "new" in c:
        return "new"

    if "used" in c:
        return "used"

    return "unknown"


def passes_price_filter(
    listing,
    target
):

    condition = normalize_condition(
        listing.condition
    )

    if condition == "used":
        return listing.price <= target.max_used

    if condition == "new":
        return listing.price <= target.max_new

    return (
        listing.price <= target.max_used
        or
        listing.price <= target.max_new
    )