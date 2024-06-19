import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Baca dataset
df = pd.read_excel('dataafter.xlsx')

# Pisahkan fitur (X) dan target (y)
X = df.drop(['Sparepart'], axis=1)  # Fitur kecuali 'sparepart'
y = df['Sparepart']  # Target

# Inisialisasi model Decision Tree
model = DecisionTreeClassifier()

# Latih model Decision Tree
model.fit(X, y)

# Fungsi untuk mendapatkan jawaban pengguna
def get_user_input():
    user_input = {}
    user_input['ODO Kilometer'] = input("Apakah ODO Kilometer kurang dari 10.000 km? (iya/tidak): ").lower()
    user_input['Batas Waktu Terakhir Layanan'] = input("Apakah Batas Waktu Terakhir Layanan lebih dari 1 tahun sejak layanan terakhir? (iya/tidak): ").lower()
    # Tambahkan pertanyaan lain sesuai kebutuhan
    
    return user_input

# Fungsi untuk mendapatkan rekomendasi spare part berdasarkan jawaban pengguna
def get_recommendation(user_input):
    user_data = pd.DataFrame([user_input])
    prediction = model.predict(user_data)
    recommended_spareparts = df[df['Sparepart'] == prediction[0]]
    return recommended_spareparts

# Fungsi untuk menjalankan aplikasi
def main():
    print("Selamat datang di Sistem Pendukung Keputusan Servis Motor")
    print("Silakan jawab beberapa pertanyaan untuk mendapatkan rekomendasi spare part:")
    print()

    # Dapatkan jawaban dari pengguna
    user_input = get_user_input()

    # Dapatkan rekomendasi spare part
    recommendation = get_recommendation(user_input)

    # Tampilkan rekomendasi
    print("\nRekomendasi Spare Part:")
    print(recommendation)

# Jalankan aplikasi
if __name__ == "__main__":
    main()
