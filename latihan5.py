import time

operasi = [1, 2, 3, 4]
time.sleep(2)
print("=================")
print(operasi[0], ". Jumlah [+]")
print(operasi[1], ". Kurang [-]")
print(operasi[2], ". Perkalian [*]")
print(operasi[3], ". Pembagian [/]")
print("=================")

time.sleep(1)
pilih_operasi = int(input("Pilihan operasi (1/2/3/4) : "))
nilai_pertama = int(input("Masukan nilai pertama : "))
nilai_kedua = int(input("Masukan nilai kedua : "))

time.sleep(1)
print("=================")
if pilih_operasi == 1:
    print(
        "Hasil operasi dari",
        nilai_pertama,
        "+",
        nilai_kedua,
        "=",
        nilai_pertama + nilai_kedua,
    )
elif pilih_operasi == 2:
    print(
        "Hasil operasi dari ",
        nilai_pertama,
        "-",
        nilai_kedua,
        "=",
        nilai_pertama - nilai_kedua,
    )
elif pilih_operasi == 3:
    print(
        "Hasil operasi dari ",
        nilai_pertama,
        "*",
        nilai_kedua,
        "=",
        nilai_pertama * nilai_kedua,
    )
elif pilih_operasi == 4:
    print(
        "Hasil operasi dari ",
        nilai_pertama,
        "/",
        nilai_kedua,
        "=",
        int(nilai_pertama / nilai_kedua),
    )
else:
    print("Pilihan tidak ada")
