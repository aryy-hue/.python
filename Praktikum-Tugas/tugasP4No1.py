# Fungsi untuk menjumlahkan angka-angka dalam list dan memisahkan ganjil dan genap
def jumlah_dan_pisah(angka_list): # Menggunakan fungsi sebagai parameter
    total_angka_ganjil = 0
    total_angka_genap = 0
    
    for angka in angka_list: # Melakukan for looping untuk menghitung total angka ganjil dan genap
        if angka % 2 == 0:  # Jika angka genap
            total_angka_genap += angka # total_angka_genap diisi = total_angka_genap + angka
        else:  # Jika angka ganjil
            total_angka_ganjil += angka # total_angka_ganjil diisi = total_angka_ganjil + angka
    
    return total_angka_ganjil, total_angka_genap # Me-return total angka ganjil dan genap

# Contoh list angka
angka_list = [23,50,100,1,34,2,6,44]

# Memanggil fungsi dan menampilkan hasil
total_ganjil, total_genap = jumlah_dan_pisah(angka_list) # Memanggil fungsi jumlah_dan_pisah
print("Total angka ganjil:", total_ganjil) # Menampilkan total angka ganjil
print("Total angka genap:", total_genap) # Menampilkan total angka genap

