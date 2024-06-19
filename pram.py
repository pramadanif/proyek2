import pandas as pd
import numpy as np

# Definisikan kolom
col_names = ['sparepart', 'merk', 'Harga', 'kualitas', 'spesifikasi teknis', 'ratings', 'id', 'km']

# Baca data dari file Excel
pima = pd.read_excel("./dataafter.xlsx", names=col_names)

# Lihat data yang ada
print("Data sebelum penambahan km:")
print(pima.head())

# Menambahkan data acak pada kolom 'km'
np.random.seed(42)  # Untuk menghasilkan hasil yang sama setiap kali dijalankan
pima['km'] = np.random.randint(1000, 50000, size=len(pima))

# Menyimpan data kembali ke file Excel
output_file = "./dataafterfix.xlsx"
pima.to_excel(output_file, index=False)

print("Data setelah penambahan km:")
print(pima.head())

print(f"Data berhasil disimpan ke {output_file}")
