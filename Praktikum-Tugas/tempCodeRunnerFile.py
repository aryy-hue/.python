# Nama : Muhammad Fauzan Aryawardhana
# NRP : 152022135
# Kelas : EE

# Menyimpan variabel banyaknya mahasiswa
jumlah_mahasiswa = int(input("Masukan banyak mahasiswa: "))

# Menyimpan variaple data nilai mahasiswa
data_nilai = {}

# memproses input dan perulangan setiap mahasiswa
for mahasiswa1 in range(jumlah_mahasiswa):
    nama_mahasiswa = input(f"Masukan nama mahasiswa ke {mahasiswa1}: ")
    jumlah_mahasiswa = int(input(f"Masukan jumlah matakuliah untuk {nama_mahasiswa}: "))

    nilai_matkul = (
        []
    )  # Meninympan data dari nilai matkul ke dalam array kosong yang nantinya dapat diisi

    for matkul1 in range(jumlah_mahasiswa):
        nilai = float(input(f"Masukan nilai mata kuliah ke-{matkul1}: "))
        nilai_matkul.append(nilai)

    data_nilai[nama_mahasiswa] = nilai_matkul

# Menampilkan data nilai mahasiswa
print("\nData nilai Mahasiswa: ")
for nama, nilai_matkul in data_nilai.items():
    print(f"{nama}: ")
    for matkul1, nilai in enumerate(nilai_matkul):
        print(f"Nilai Mata Kuliah ke-{matkul1}: {nilai}")
