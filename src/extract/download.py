from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

data_path = BASE_DIR / "data" / "raw" / "human.txt"

df = pd.read_csv(data_path, sep="\t")



df.to_csv(BASE_DIR / "data" / "raw" / "human.csv", index=False)
print("Processed data saved to CSV.")