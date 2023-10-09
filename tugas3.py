def cek_ketajaman():
    # Fungsi ini akan mengembalikan nilai ketajaman dari hasil kamera
    ketajaman = int(input("Masukkan nilai ketajaman: "))
    return ketajaman


def putar_ke_kanan():
    # Fungsi ini akan memutar fokus ke kanan
    print("Memutar fokus ke kanan")


def putar_ke_kiri():
    # Fungsi ini akan memutar fokus ke kiri
    print("Memutar fokus ke kiri")


def ambil_gambar():
    # Fungsi ini akan mengambil gambar
    print("Mengambil gambar")


# Main program
nilai_sebelumnya = None

while True:
    nilai_ketajaman = cek_ketajaman()
    if nilai_sebelumnya is not None:
        if nilai_ketajaman > nilai_sebelumnya:
            putar_ke_kanan()
            break
        elif nilai_ketajaman < nilai_sebelumnya:
            putar_ke_kiri()
            break
        else:
            ambil_gambar()
            break
    nilai_sebelumnya = nilai_ketajaman
