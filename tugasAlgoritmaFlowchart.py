import time

nilai = int(input("Masukan nilai: "))
time.sleep(1)
print("Melakukan komputasi")
print("-------------------")

if nilai >= 50:
    arsitektur = "Schematic Illustration of Memory Hierarchy"
    print("Anda menggunakan ", arsitektur)
    print(
        "Register dan memori chace memiliki akses yang relatif cepat dan kapasistas rendah"
    )
else:
    arsitektur = "Von Neumann Architecture"
    print("Anda menggunakan ", arsitektur)
    print("Meminimalkan pergerakan data , sehingga konsumsi dan latensi  lebih rendah")

time.sleep(2)
print("--------------------------------------------------")
dayaBesar = bool(input("Apakah memerlukan daya yang besar? "))
if dayaBesar == True:
    jenisIMC = "Dynamic IMC"
    print("Anda menggunakan ", jenisIMC)
    print(
        "Menggabungkan kemungkinan Static IMC dengan tambahan kekuatan memungkinkan peralihan terkontrol dari perangkat memori ke mereproduksi fungsi tambahan"
    )
else:
    jenisIMC = "Static IMC"
    print("Anda menggunakan ", jenisIMC)
    print(
        "Menyimpan data dana melakukan komputasi tanpa menguhab atau memperbarui status terprogramnya"
    )

print("----------------------------------------------------------")
print("Melakukan Multiplikasi Matriks Vector")

if nilai <= 50 and dayaBesar == False:
    print("Anda menggunakan One-resistor")
    print("Selnya terdiri dari perangkat resistif pasif")
