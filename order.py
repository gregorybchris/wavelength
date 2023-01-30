from pathlib import Path

import pandas as pd


filepath = Path(__file__).parent / "extremes.csv"
df = pd.read_csv(filepath, header=None)

records = df.to_records(index=False)
records = sorted(records, key=lambda r: len(r[0] + r[1]))

for low, high in records:
    print(f"{low},{high}")
