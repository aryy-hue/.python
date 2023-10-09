# Nama : Muhammad Fauzan Aryawardhana
# NRP : 152022135
# Kelas : EE

# Memasukan nilai dalam bentuk int lalu masukan kedalam variable bilangan_angka
bilangan_angka = int(input("Masukan nilai bilangan: "))

# Menampilkan kelipatan 3
if bilangan_angka % 3 == 0:  # Jika bilangan_angka adalah kelipatan 3
    print(bilangan_angka, "adalah kelipatan 3 ")
else:
    print(
        bilangan_angka,
        "bukan kelipatan 3 ",  # Menampilkan bahwa bilangan tersebut bukan kelipatan 3
    )
