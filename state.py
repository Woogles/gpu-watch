import json
from pathlib import Path


def load_state(path):
    if not path.exists():
        return {}

    try:
        return json.loads(path.read_text())
    except Exception:
        return {}


def save_state(path, data):
    path.parent.mkdir(exist_ok=True)

    path.write_text(
        json.dumps(data, indent=2)
    )