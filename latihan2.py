nilai = int(input("Masukan Nilai : "))
list_angka = [i for i in range(nilai)]
print("List angka =", list_angka)

# Initialize min_value and max_value with the first number in the list
min_value = list_angka[0]
max_value = list_angka[0]

# Iterate over the remaining list_angka in the list
for angka in list_angka:
    if angka < min_value:
        min_value = angka
    if angka > max_value:
        max_value = angka

print("Minimum value:", min_value)
print("Maximum value:", max_value)
