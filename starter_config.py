from __future__ import annotations

import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

FAILED_DATASET = DATA_DIR / "orders_failed.csv"
PASSED_DATASET = DATA_DIR / "orders_passed.csv"
SUMMARY_FILE = OUTPUT_DIR / "validation_summary.json"

VALID_STATUSES = {"completed", "pending", "cancelled"}

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "")
DEFAULT_INPUT_FILE = os.getenv("AIRFLOW_INPUT_FILE", str(PASSED_DATASET))
