import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Definisikan kolom
col_names = ['sparepart', 'merk', 'Harga', 'kualitas', 'spesifikasi teknis', 'ratings', 'id', 'km']

# Baca data dari file Excel
pima = pd.read_excel("./dataafterfix.xlsx", names=col_names)

# Proses label encoding untuk kolom yang memiliki data kategorikal
label_encoder_sparepart = LabelEncoder()
label_encoder_kualitas = LabelEncoder()
pima['sparepart'] = label_encoder_sparepart.fit_transform(pima['sparepart'])
pima['kualitas'] = label_encoder_kualitas.fit_transform(pima['kualitas'])
pima['merk'] = label_encoder_kualitas.fit_transform(pima['merk'])

# Ekstrak fitur dan target
X = pima[['km', 'kualitas', 'Harga', 'ratings']].values
y = pima['sparepart'].values

# Train Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Fungsi untuk merekomendasikan perawatan berdasarkan input pengguna
def rekomendasikan_maintenance():
    # Langkah 1: Odometer (km)
    odometer = int(input("Masukkan pembacaan odometer kendaraan Anda (dalam km): "))
    if odometer < 10000:
        # Langkah 2: Umur Kendaraan
        umur = input("Apakah kendaraan Anda lebih dari 5 tahun? (ya/tidak): ").lower()
        if umur == 'ya':
            # Langkah 4: Jarak Tempuh Kendaraan
            jarak_tempuh = int(input("Masukkan jarak tempuh kendaraan (dalam km): "))
            if jarak_tempuh > 30000:
                print("Perawatan yang direkomendasikan: Layanan besar")
            else:
                print("Perawatan yang direkomendasikan: Layanan sedang")
        else:
            # Langkah 5: Keluhan atau Masalah yang Dialami
            keluhan = input("Apakah Anda memiliki keluhan atau masalah tertentu? (ya/tidak): ").lower()
            if keluhan == 'ya':
                print("Perawatan yang direkomendasikan: Layanan berdasarkan keluhan")
            else:
                # Langkah 6: Kondisi Kendaraan Saat Ini
                kondisi = input("Apakah kendaraan Anda membutuhkan perbaikan besar? (ya/tidak): ").lower()
                if kondisi == 'ya':
                    print("Perawatan yang direkomendasikan: Layanan besar")
                else:
                    # Langkah 7: Ketersediaan Suku Cadang
                    suku_cadang = input("Apakah suku cadang tertentu tersedia? (ya/tidak): ").lower()
                    if suku_cadang == 'ya':
                        print("Perawatan yang direkomendasikan: Layanan berdasarkan ketersediaan suku cadang")
                    else:
                        # Langkah 8: Lokasi Penggunaan Kendaraan
                        lokasi = input("Apakah kendaraan digunakan di perkotaan? (ya/tidak): ").lower()
                        if lokasi == 'ya':
                            print("Perawatan yang direkomendasikan: Layanan ringan")
                        else:
                            print("Perawatan yang direkomendasikan: Layanan sedang")
    else:
        # Langkah 3: Penggunaan Kendaraan
        penggunaan = input("Apakah kendaraan hanya digunakan di akhir pekan? (ya/tidak): ").lower()
        if penggunaan == 'ya':
            print("Perawatan yang direkomendasikan: Layanan ringan")
        else:
            # Langkah 9: Batas Waktu Terakhir Layanan
            waktu_terakhir = input("Apakah sudah lebih dari 1 tahun sejak layanan terakhir? (ya/tidak): ").lower()
            if waktu_terakhir == 'ya':
                print("Perawatan yang direkomendasikan: Layanan sedang")
            else:
                # Langkah 10: Budget untuk Layanan
                budget = input("Apakah Anda memiliki anggaran tertentu untuk layanan? (ya/tidak): ").lower()
                if budget == 'ya':
                    print("Perawatan yang direkomendasikan: Sesuaikan rekomendasi layanan dengan anggaran")
                else:
                    # Langkah 11: Waktu Terakhir Pergantian Oli
                    pergantian_oli = input("Apakah sudah lebih dari 6 bulan sejak pergantian oli terakhir? (ya/tidak): ").lower()
                    if pergantian_oli == 'ya':
                        print("Perawatan yang direkomendasikan: Penggantian oli")
                    else:
                        # Langkah 12: Pengecekan Kelistrikan
                        kelistrikan = input("Apakah ada masalah kelistrikan? (ya/tidak): ").lower()
                        if kelistrikan == 'ya':
                            print("Perawatan yang direkomendasikan: Pemeriksaan kelistrikan")
                        else:
                            # Langkah 13: Pemeriksaan Sistem Bahan Bakar
                            bahan_bakar = input("Apakah ada masalah dengan sistem bahan bakar? (ya/tidak): ").lower()
                            if bahan_bakar == 'ya':
                                print("Perawatan yang direkomendasikan: Pemeriksaan sistem bahan bakar")
                            else:
                                # Langkah 14: Pemeriksaan Sistem Rem
                                rem = input("Apakah ada masalah dengan sistem rem? (ya/tidak): ").lower()
                                if rem == 'ya':
                                    print("Perawatan yang direkomendasikan: Pemeriksaan sistem rem")
                                else:
                                    # Langkah 15: Pemeriksaan Sistem Pendingin
                                    pendingin = input("Apakah ada masalah dengan sistem pendingin? (ya/tidak): ").lower()
                                    if pendingin == 'ya':
                                        print("Perawatan yang direkomendasikan: Pemeriksaan sistem pendingin")
                                    else:
                                        # Langkah 16: Pemeriksaan Sistem Suspensi
                                        suspensi = input("Apakah ada masalah dengan sistem suspensi? (ya/tidak): ").lower()
                                        if suspensi == 'ya':
                                            print("Perawatan yang direkomendasikan: Pemeriksaan sistem suspensi")
                                        else:
                                            # Langkah 17: Pemeriksaan Sistem Transmisi
                                            transmisi = input("Apakah ada masalah dengan sistem transmisi? (ya/tidak): ").lower()
                                            if transmisi == 'ya':
                                                print("Perawatan yang direkomendasikan: Pemeriksaan sistem transmisi")
                                            else:
                                                # Langkah 18: Pemeriksaan Sistem Knalpot
                                                knalpot = input("Apakah ada masalah dengan sistem knalpot? (ya/tidak): ").lower()
                                                if knalpot == 'ya':
                                                    print("Perawatan yang direkomendasikan: Pemeriksaan sistem knalpot")
                                                else:
                                                    # Langkah 19: Pemeriksaan Sistem Kelistrikan
                                                    kelistrikan_ulang = input("Apakah ada masalah dengan sistem kelistrikan? (ya/tidak): ").lower()
                                                    if kelistrikan_ulang == 'ya':
                                                        print("Perawatan yang direkomendasikan: Pemeriksaan sistem kelistrikan")
                                                    else:
                                                        print("Perawatan yang direkomendasikan: Layanan ringan")

# Panggil fungsi untuk memulai proses rekomendasi
rekomendasikan_maintenance()


