def is_palindrome(sentence): #mendeklarasi function
    # Menghapus spasi dan mengubah kalimat menjadi huruf kecil
    cleaned_sentence = ''.join(sentence.split()).lower()
    # Memeriksa apakah kalimat adalah palindrom
    return cleaned_sentence == cleaned_sentence[::-1]

# Membaca input dari pengguna
kalimat = input("Masukkan kalimat: ")

# Memanggil fungsi is_palindrome dan menampilkan hasilnya
if is_palindrome(kalimat):
    print("Kalimat ini adalah palindrom.")
else:
    print("Kalimat ini bukan palindrom.")
