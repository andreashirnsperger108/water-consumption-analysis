from __future__ import annotations
from pathlib import Path
import pandas as pd

def load_table(path: str | Path) -> pd.DataFrame:
    """Load CSV/Excel into a DataFrame. Extend as needed."""
    path = Path(path)
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    return pd.read_csv(path)
