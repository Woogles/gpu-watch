from pathlib import Path

ROOT = Path(__file__).parent

CSV_FILE = ROOT / "gpus.csv"

DATABASE_FILE = ROOT / "state" / "gpuwatch.db"

REPORT_DIR = ROOT / "reports"

PROVIDERS_FILE = ROOT / "config" / "providers.json"

ZIP_CODE = "20155"

EMAIL_TO = "your@email.com"