# Fungsi untuk mendapatkan input data barang dari pengguna
def input_barang(banyak_data, dict_supplier):
    for i in range(banyak_data):
        perbarang = {}  # Membuat dictionary kosong untuk setiap barang
        kode_barang = input('Masukkan Kode Barang: ')  # Mengambil input kode barang
        nama_barang = input('Masukkan Nama Barang: ')  # Mengambil input nama barang
        harga = int(input('Masukkan Harga: '))  # Mengambil input harga barang
        jumlah = int(input('Masukkan Jumlah: '))  # Mengambil input jumlah barang
        perbarang['kode_barang'] = kode_barang  # Menyimpan data ke dictionary
        perbarang['nama_barang'] = nama_barang
        perbarang['harga'] = harga
        perbarang['jumlah'] = jumlah

        dict_supplier['barang'].append(perbarang)  # Menambah data barang ke supplier

# Fungsi untuk mendapatkan input data supplier dari pengguna
def input_supplier(banyak_data, dict_pelanggan):
    for i in range(banyak_data):
        persupplier = {}  # Membuat dictionary kosong untuk setiap supplier
        kode_supplier = input('Masukkan Supplier Code: ')  # Mengambil input kode supplier
        nama_supplier = input('Masukkan Nama Supplier: ')  # Mengambil input nama supplier
        status = input('Status ? ')  # Mengambil input status supplier (tersedia atau tidak)
        persupplier['kode_supplier'] = kode_supplier  # Menyimpan data ke dictionary
        persupplier['nama_supplier'] = nama_supplier
        persupplier['status'] = status.lower()  # Mengonversi status ke huruf kecil

        if persupplier['status'] == 'tersedia':  # Memeriksa apakah status tersedia
            pass
        else:
            continue  # Melanjutkan ke supplier berikutnya jika status tidak tersedia

        kota = input('Masukkan Kota: ')  # Mengambil input kota supplier
        persupplier['kota'] = kota
        persupplier['barang'] = []  # Menambahkan list kosong untuk barang-barang dari supplier

        jumlah_barang = int(input('Masukkan jumlah barang yang akan dimasukkan: '))  # Mengambil jumlah barang

        input_barang(jumlah_barang, persupplier)  # Memanggil fungsi input_barang untuk mendapatkan barang dari pengguna
        
        dict_pelanggan['supplier'].append(persupplier)  # Menambahkan data supplier ke pelanggan

# Fungsi untuk mendapatkan input data pelanggan dari pengguna
def input_pelanggan(banyak_data, data_pelanggan):
    for i in range(banyak_data):
        perpelanggan = {}  # Membuat dictionary kosong untuk setiap pelanggan
        kode_pelanggan = input('Masukkan Kode Pelanggan: ')  # Mengambil input kode pelanggan
        nama_pelanggan = input('Masukkan Nama Pelanggan: ')  # Mengambil input nama pelanggan
        alamat = input('Masukkan Alamat: ')  # Mengambil input alamat pelanggan
        perpelanggan['kode_pelanggan'] = kode_pelanggan  # Menyimpan data ke dictionary
        perpelanggan['nama_pelanggan'] = nama_pelanggan
        perpelanggan['alamat'] = alamat
        perpelanggan['supplier'] = []  # Menambahkan list kosong untuk supplier-supplier dari pelanggan

        jumlah_supplier = int(input('Masukkan jumlah supplier yang akan dimasukkan: '))  # Mengambil jumlah supplier

        input_supplier(jumlah_supplier, perpelanggan)  # Memanggil fungsi input_supplier untuk mendapatkan supplier dari pengguna

        data_pelanggan.append(perpelanggan)  # Menambahkan data pelanggan ke list data_pelanggan

list_pelanggan = []  # Inisialisasi list kosong untuk menyimpan data pelanggan

jumlah_pelanggan = int(input('Masukkan jumlah pelanggan yang akan dimasukkan: '))  # Mengambil jumlah pelanggan dari pengguna

input_pelanggan(jumlah_pelanggan, list_pelanggan)  # Memanggil fungsi input_pelanggan untuk mendapatkan data pelanggan

print()

# Inisialisasi variabel untuk pelanggan dengan barang terbanyak dan transaksi terbesar
pelanggan_barang_terbanyak = {
    'kode_pelanggan': list_pelanggan[0]['kode_pelanggan'],
    'nama_pelanggan': list_pelanggan[0]['nama_pelanggan'],
    'jumlah_barang': 0
}

pelanggan_transaksi_terbesar = {
    'kode_pelanggan': list_pelanggan[0]['kode_pelanggan'],
    'nama_pelanggan': list_pelanggan[0]['nama_pelanggan'],
    'total_transaksi': 0
}

print('Data Pelanggan:')
# Iterasi melalui setiap pelanggan dalam data_pelanggan
for perpelanggan in list_pelanggan:
    jumlah_barang = 0  # Inisialisasi variabel jumlah barang untuk setiap pelanggan
    total_transaksi = 0  # Inisialisasi variabel total transaksi untuk setiap pelanggan
    print(f"Kode Pelanggan: {perpelanggan['kode_pelanggan']}")
    print(f"Nama Pelanggan: {perpelanggan['nama_pelanggan']}")
    print(f"Alamat: {perpelanggan['alamat']}")

    print('Supplier yang disediakan:')
    # Iterasi melalui setiap supplier dalam pelanggan
    for persupplier in perpelanggan['supplier']:
        print(f"Supplier Code: {persupplier['kode_supplier']}")
        print(f"Nama Supplier: {persupplier['nama_supplier']}")
        print(f"Status: {persupplier['status']}")

        if persupplier['status'] == 'tersedia':  # Memeriksa apakah status supplier tersedia
            pass
        else:
            continue  # Melanjutkan ke supplier berikutnya jika status tidak tersedia

        print(f"Kota: {persupplier['kota']}")

        print('Barang yang dibeli:')
        # Iterasi melalui setiap barang dalam supplier
        for perbarang in persupplier['barang']:
            jumlah_barang = jumlah_barang + perbarang['jumlah']  # Menambahkan jumlah barang
            total_harga = perbarang['harga'] * perbarang['jumlah']  # Menghitung total harga barang
            total_transaksi = total_transaksi + total_harga  # Menambahkan total harga ke total transaksi
            print(f"Kode Barang: {perbarang['kode_barang']}")
            print(f"Nama Barang: {perbarang['nama_barang']}")
            print(f"Harga: {perbarang['harga']}")
            print(f"Jumlah: {perbarang['jumlah']}")

    # Membandingkan jumlah barang dan total transaksi dengan pelanggan dengan barang terbanyak dan transaksi terbesar sebelumnya
    if jumlah_barang > pelanggan_barang_terbanyak['jumlah_barang']:
        pelanggan_barang_terbanyak['kode_pelanggan'] = perpelanggan['kode_pelanggan']
        pelanggan_barang_terbanyak['nama_pelanggan'] = perpelanggan['nama_pelanggan']
        pelanggan_barang_terbanyak['jumlah_barang'] = jumlah_barang

    if total_transaksi > pelanggan_transaksi_terbesar['total_transaksi']:
        pelanggan_transaksi_terbesar['kode_pelanggan'] = perpelanggan['kode_pelanggan']
        pelanggan_transaksi_terbesar['nama_pelanggan'] = perpelanggan['nama_pelanggan']
        pelanggan_transaksi_terbesar['total_transaksi'] = total_transaksi

print()
print('Pelanggan dengan jumlah barang terbanyak:')
print(f"Kode Pelanggan: {pelanggan_barang_terbanyak['kode_pelanggan']}")
print(f"Nama Pelanggan: {pelanggan_barang_terbanyak['nama_pelanggan']}")
print(f"Jumlah Barang: {pelanggan_barang_terbanyak['jumlah_barang']}")

print()
print('Pelanggan dengan transaksi terbesar:')
print(f"Kode Pelanggan: {pelanggan_transaksi_terbesar['kode_pelanggan']}")
print(f"Nama Pelanggan: {pelanggan_transaksi_terbesar['nama_pelanggan']}")
print(f"Total Transaksi: {pelanggan_transaksi_terbesar['total_transaksi']}")
