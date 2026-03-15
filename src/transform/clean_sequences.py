# Importando as bibliotecas necessárias
from pathlib import Path
import pandas as pd

# Definindo o caminho para o arquivo CSV
BASE_DIR = Path(__file__).resolve().parents[2]

csv_path = BASE_DIR / "data" / "raw" / "human.csv"

df = pd.read_csv(csv_path)

# Exibindo as informações básicas do DataFrame
df["sequence"].str.len().describe()
#print(df["sequence"].str.len().describe())

# Filtrando as sequências com comprimento menor que 100
df["length"] = df["sequence"].str.len()
df = df[df["length"] >= 100]
#print(df["length"].describe())

# Filtrando as sequências que contêm apenas os caracteres A, T, C e G
df = df[df["sequence"].str.contains("^[ATCG]+$", regex=True)]
#print(df["length"].describe())

# Removendo duplicatas das sequências
before = len(df)
df = df.drop_duplicates(subset="sequence")
after = len(df)
print(f"Removed {before - after} duplicate sequences.")

# Salvando o DataFrame limpo em um novo arquivo CSV
clean_csv_path = BASE_DIR / "data" / "processed" / "human_clean.csv"
df.to_csv(clean_csv_path, index=False)








