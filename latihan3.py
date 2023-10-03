a = int(input("Masukan nilai A : "))
b = int(input("Masukan nilai B : "))
descision = False

decision = bool(input("Apakah anda ingin melakukan perkalian (T/F)? "))

if decision == True:
    print("Perkalian dilakukan")
    c = a * b
    print("Hasilnya adalah", c)

