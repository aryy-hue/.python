angka1 = int(input("Masukan angka : "))
angka2 = int(input("Masukan angka : "  ))
ref = input("Masukan operator : ")
def kalkulator(operator, angka1, angka2):
    switch = {
        "+": (angka1 + angka2),
        "-": (angka1 - angka2),
        "/": (angka1 / angka2),
        "*": (angka1 * angka2)

    }
    return switch.get(operator, "Tidak ada operator")

print("Hasilnya :",kalkulator(ref,angka1,angka2))
