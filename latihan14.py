def hewan():
    def hewan1():
        jenis = "angsa"
    def hewan2():
        nonlocal jenis
        jenis = "harimau"
    def hewan3():
        global jenis
        jenis = "gajah"

    jenis = "ayam"
    hewan1()
    print(f"jenis hewan pertama adalah {jenis}")
    hewan2()
    print(f"jenis hewan kedua adalah {jenis}")
    hewan3()
    print(f"jenis hewan ketiga adalah {jenis}")

hewan()
print(f"Jenis heawan adalah {jenis}")


