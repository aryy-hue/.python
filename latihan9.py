def jumlahkan(*args):
    total=0
    for angka in args:
        total += angka
    return total
hasil = jumlahkan(4,6,8,10)
print(hasil) #output 28