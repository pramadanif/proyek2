import numpy as np
import pandas as pd
from statistics import mean
import seaborn as sns
import scipy.stats as stats

# Membaca data dari file CSV
data = pd.read_excel("./sparepart.xlsx")

# Menampilkan nama-nama kolom yang ada dalam data
print("Nama Kolom dalam Data:")
print(data.columns)
print("\n")

# Mengganti atribut yang akan diproses
dataPreprocessing = data.iloc[:, [0, 1, 2, 3, 4, 5]]  # Assuming the desired columns are at positions 0-5

# Deteksi nilai yang hilang
print("Deteksi Missing Value")
print(dataPreprocessing.isna().sum())
print("\n")
print("Hapus Missing Value")
dataPreprocessing = dataPreprocessing.dropna()
print(dataPreprocessing.isna().sum())
print("\n")

# Menyimpan data setelah pra-pemrosesan ke dalam file Excel
dataPreprocessing.to_excel("./dataafter2.xlsx", index=False)
print("Data setelah pra-pemrosesan telah disimpan ke dalam file Excel.")
