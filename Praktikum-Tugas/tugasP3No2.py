# Membaca input dari pengguna untuk i (angka batas)
i = int(input("Masukkan angka batas (i): "))

# Membaca input dari pengguna untuk memilih ganjil atau genap
jenis_bilangan = input("Apakah Anda ingin melihat bilangan ganjil atau genap? (ganjil/genap): ").lower()

# Memeriksa jenis bilangan yang dipilih oleh pengguna dan menampilkan hasilnya
if jenis_bilangan == "ganjil":
    # Menampilkan semua bilangan ganjil dari 1 hingga i
    ganjil = [bilangan for bilangan in range(1, i + 1) if bilangan % 2 != 0]
    print("Bilangan ganjil dari 1 hingga", i, "adalah:", ganjil)
elif jenis_bilangan == "genap":
    # Menampilkan semua bilangan genap dari 1 hingga i
    genap = [bilangan for bilangan in range(1, i + 1) if bilangan % 2 == 0]
    print("Bilangan genap dari 1 hingga", i, "adalah:", genap)
else:
    print("Pilihan tidak valid. Silakan masukkan 'ganjil' atau 'genap'.")
