from pathlib import Path
from collections import Counter
import pandas as pd

def get_kmers(sequence, k):
    kmers = []

    for i in range(len(sequence) - k + 1):

        kmer = sequence[i : i + k]

        kmers.append(kmer)

    return kmers

def count_kmers(kmers):
    return Counter(kmers)


# Definindo o caminho para o arquivo CSV
BASE_DIR = Path(__file__).resolve().parents[2]

csv_path = BASE_DIR / "data" / "processed" / "human_clean.csv"
df = pd.read_csv(csv_path)

# Features Basicas
df["length"] = df["sequence"].str.len()
df["A"] = df["sequence"].str.count("A")
df["T"] = df["sequence"].str.count("T")
df["G"] = df["sequence"].str.count("G")
df["C"] = df["sequence"].str.count("C")

df["GC_content"] = (df["G"] + df["C"]) / df["length"]

# Criando a coluna de kmers
k = 3
df["kmers"] = df["sequence"].apply(lambda seq: get_kmers(seq, k))
df["kmer_counts"] = df["kmers"].apply(count_kmers)

# Transformar em features de kmers
kmer_df = df["kmer_counts"].apply(pd.Series).fillna(0)

# Dataset final
final_df = pd.concat([df[["length", "GC_content"]], kmer_df], axis=1)

# Salvando features
outputs_dir = BASE_DIR / "outputs" / "features"

final_df.to_csv(outputs_dir / "kmer_features.csv", index=False)


# Exibindo as primeiras linhas do DataFrame para verificar os kmers
print(df[["sequence", "kmers"]].head())