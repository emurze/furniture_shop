import os
from pathlib import Path

WORKDIR = os.getenv("WORKDIR", "")

PATH = Path(f"{WORKDIR}src/modules")

FILENAME = "db_contract.py"
