import csv

from models import TargetGPU


def load_targets(path):

    targets = []

    with open(path, newline="", encoding="utf-8-sig") as f:

        reader = csv.DictReader(f)

        for row in reader:

            targets.append(
                TargetGPU(
                    priority=int(row["Priority"]),
                    name=row["GPU"].strip(),
                    max_used=float(row["MaxUsed"]),
                    max_new=float(row["MaxNew"]),
                )
            )

    return targets