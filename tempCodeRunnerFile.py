# Daftar karyawan
karyawan = ["Dani", "Duki", "Duke", "Deni", "Dena"]
masa_kerja = [2, 1, 1, 5, 6]
gaji = [4200000, 4800000, 5300000, 5900000, 6400000]

# Menghitung jumlah total gaji karyawan dengan indeks ganjil
total_gaji_ganjil = 0
for i in range(len(karyawan)):
    if i % 2 == 0:
        total_gaji_ganjil += gaji[i]

# Menghitung rata-rata gaji seluruh karyawan
rata_rata_gaji = sum(gaji) / len(gaji)

# UMR Bandung
umr_bandung = 5000000

# Menentukan apakah rata-rata gaji memenuhi UMR atau tidak
if rata_rata_gaji >= umr_bandung:
    status_umr = "memenuhi"
else:
    status_umr = "tidak memenuhi"

# Menghitung total gaji dengan kenaikan gaji setiap tahun
total_gaji_dengan_kenaikan = sum(gaji) + (masa_kerja.count(1) * 1250000)

# Menampilkan hasil
print("Total gaji karyawan dengan indeks ganjil:", total_gaji_ganjil)
print("Rata-rata gaji karyawan:", rata_rata_gaji)
print("Rata-rata gaji karyawan", status_umr, "UMR Bandung.")
print("Total gaji dengan kenaikan gaji setiap tahun:", total_gaji_dengan_kenaikan)
