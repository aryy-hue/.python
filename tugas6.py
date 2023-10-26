# Daftar mahasiswa
mahasiswa = ["Diash", "Firdaus", "Lisa", "Kristiana", "Yusup", "Miftahuddin"]

# Daftar mahasiswa aktif
mahasiswa_aktif = {"Diash", "Firdaus", "Lisa"}  # Menggunakan set untuk mahasiswa aktif

# Menggunakan input untuk menentukan apakah mahasiswa aktif atau tidak
while True:
    nama_mahasiswa = input("Masukkan nama mahasiswa (atau ketik 'selesai' untuk mengakhiri): ")

    if nama_mahasiswa.lower() == 'selesai':
        break

    if nama_mahasiswa in mahasiswa_aktif:
        print(f"{nama_mahasiswa} adalah mahasiswa aktif.")
    elif nama_mahasiswa in mahasiswa:
        print(f"{nama_mahasiswa} adalah mahasiswa tidak aktif.")
    else:
        print(f"{nama_mahasiswa} tidak terdaftar.")

# Menampilkan mahasiswa yang tidak aktif
mahasiswa_tidak_aktif = set(mahasiswa) - mahasiswa_aktif
print(f"Mahasiswa yang tidak aktif: {', '.join(mahasiswa_tidak_aktif)}")

print("Perulangan selesai.")
