# Contoh berat badan (kg) dan tinggi badan (cm)
tinggi_badan = int(input("Masukkan tinggi badan (cm): "))
berat_badan = int(input("Masukkan berat badan (kg): "))

# Fungsi untuk menghitung BMI
def hitung_bmi(berat_badan, tinggi_badan):
    tinggi_badan_m = tinggi_badan / 100  # Mengubah tinggi badan dari cm ke m
    bmi = berat_badan / (tinggi_badan_m ** 2)  # Menghitung BMI
    return bmi

# Fungsi untuk menentukan kategori berat badan berdasarkan BMI
def tentukan_kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Gemuk"
    else:
        return "Obesitas"

# Menghitung BMI
bmi = hitung_bmi(berat_badan, tinggi_badan)

# Menentukan kategori berat badan
kategori_bmi = tentukan_kategori_bmi(bmi)

# Menampilkan hasil
print(f"Berat Badan: {berat_badan} kg")
print(f"Tinggi Badan: {tinggi_badan} cm")
print(f"Index Massa Tubuh (BMI): {bmi:.2f}")
print(f"Kategori Berat Badan: {kategori_bmi}")
