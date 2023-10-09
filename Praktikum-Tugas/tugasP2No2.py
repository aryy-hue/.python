# Nama : Muhammad Fauzan Aryawardhana
# NRP : 152022135
# Kelas : EE

# Masukan nilai nama dalam bentuk string
nama = input("Masukan nama kamu :")
# Masukan jumlah perulangan yang ingin diinputkan
jumlah_perulangan = int(input("Masukan jumlah perulangan :"))

# Melakukan perulangan tergantung pada seberapa banyak perulangan yang diinputkan
for i in range(jumlah_perulangan):
    print(f"No {i+1}. {nama}")
