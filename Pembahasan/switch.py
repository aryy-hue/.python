kesatu = int(input("Masukan angka : "))
kedua = int(input("Masukan angka : "))
switch = {1: kesatu * kedua, 2: kesatu + kedua, 3: kesatu - kedua, 4: kesatu / kedua}
print("Perkalian :", switch.get(1))
print("Penjumlahan :", switch.get(2))
print("Pengurangan :", switch.get(3))
print("Pembagian :", switch.get(4))
