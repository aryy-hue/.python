# Fungsi untuk melakukan pertambahan
def tambah(a, b):
    return a + b

# Fungsi untuk melakukan pengurangan
def kurang(a, b):
    return a - b

# Fungsi untuk melakukan perkalian
def kali(a, b):
    return a * b

# Fungsi untuk melakukan pembagian
def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan nol tidak diizinkan."

# Meminta input dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Menampilkan menu operasi
print("Pilih operasi:")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta input operasi dari pengguna
pilihan = input("Masukkan nomor operasi (1/2/3/4): ")

# Memeriksa pilihan pengguna dan melakukan operasi yang sesuai
if pilihan == "1":
    print("Hasil: ", tambah(angka1, angka2))
elif pilihan == "2":
    print("Hasil: ", kurang(angka1, angka2))
elif pilihan == "3":
    print("Hasil: ", kali(angka1, angka2))
elif pilihan == "4":
    print("Hasil: ", bagi(angka1, angka2))
else:
    print("Pilihan tidak valid.")
