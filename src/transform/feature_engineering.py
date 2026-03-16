# Importando bibliotecas necessárias
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Definindo o caminho para o arquivo CSV
BASE_DIR = Path(__file__).resolve().parents[2]
csv_path = BASE_DIR / "data" / "processed" / "human_clean.csv"
df = pd.read_csv(csv_path)
figures_dir = BASE_DIR / "outputs" / "figures"

# Criando novas features a partir da sequência
df["length"] = df["sequence"].str.len()
df["A"] = df["sequence"].str.count("A")
df["T"] = df["sequence"].str.count("T")
df["G"] = df["sequence"].str.count("G")
df["C"] = df["sequence"].str.count("C")

df["GC_content"] = (df["G"] + df["C"]) / df["length"]

# Visualizando as distribuições das novas features
plt.figure(figsize=(8, 5))

df["length"].hist(bins=50, color="skyblue")

plt.title("Distribution of Sequence Lengths")
plt.xlabel("Length")
plt.ylabel("Frequency")

plt.grid(True)

plt.savefig(figures_dir / "length_distribution.png")
#plt.show()
plt.close()

# Visualizando a distribuição do conteúdo GC
plt.figure(figsize=(8, 5))

df["GC_content"].hist(bins=50, color="lightgreen")

plt.title("Distribution of GC Content")
plt.xlabel("GC Content")
plt.ylabel("Frequency")

plt.grid(True)

plt.savefig(figures_dir / "gc_content_distribution.png")
#plt.show()
plt.close()

# Visualizando a relação entre comprimento e conteúdo GC
plt.figure(figsize=(8, 5))
plt.scatter(df["length"], df["GC_content"], alpha=0.5, color="salmon")

plt.title("GC Content vs Sequence Length")
plt.xlabel("Length")
plt.ylabel("GC Content")

plt.grid(True)

plt.savefig(figures_dir / "gc_content_vs_length.png")
#plt.show()
plt.close()

#print(df[["length", "A", "T", "G", "C", "GC_content"]].describe())

