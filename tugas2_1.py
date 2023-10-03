import time

nilai = int(input("Masukan nilai: "))
time.sleep(1)
print("Melakukan komputasi")
print("-------------------")

if nilai >= 50:
    arsitektur = "Schematic Illustration of Memory Hierarchy"
    print("Anda menggunakan ", arsitektur)
    print(
        "Register dan memori chace memiliki akses yang relatif cepat dan kapasistas rendah"
    )
else:
    arsitektur = "Von Neumann Architecture"
    print("Anda menggunakan ", arsitektur)
    print("Meminimalkan pergerakan data , sehingga konsumsi dan latensi  lebih rendah")

time.sleep(2)
print("--------------------------------------------------")
dayaBesar = bool(input("Apakah memerlukan daya yang besar? "))
if dayaBesar == True:
    jenisIMC = "Dynamic IMC"
    print("Anda menggunakan ", jenisIMC)
    print(
        "Menggabungkan kemungkinan Static IMC dengan tambahan kekuatan memungkinkan peralihan terkontrol dari perangkat memori ke mereproduksi fungsi tambahan"
    )
else:
    jenisIMC = "Static IMC"
    print("Anda menggunakan ", jenisIMC)
    print(
        "Menyimpan data dana melakukan komputasi tanpa menguhab atau memperbarui status terprogramnya"
    )

time.sleep(2)
print("----------------------------------------------------------")
print("Melakukan Multiplikasi Matriks Vector")

if nilai <= 50 and dayaBesar == False:
    print("Anda menggunakan One-resistor")
    print("Selnya terdiri dari perangkat resistif pasif")

elif nilai >= 50 and dayaBesar == False:
    print("Anda menggunakan One-Selector/One-Resistor")
    print(
        "Selnya dimana masalah jalur diam diam dihindari oleh perangkat pemilih non linier tanpa mempengaruhi kepadatan integrasi"
    )

elif nilai <= 50 and dayaBesar == True:
    print("Anda menggunakan One-Transistor/One-Resistor")
    print(
        "Memungkinkan pemilihan sel individual selama pemrograman dan pembacaan dengan mengorbankan kepadatan integrasi yang lebih rendah"
    )
if nilai >= 50 and dayaBesar == True:
    print("Anda menggunakan One-Capacitor")
    print("Mencegah kebocoran statis selama MVM")

time.sleep(2)
print("----------------------------------------------------------")
print("MVM for neural network accelerators")

if nilai >= 50 and dayaBesar == True:
    print(
        "Korelasi plot efisiensi energi sebagai fungsi throuput untuk akselerator perangkat keras"
    )
else:
    print("Sketsa DNN yang terhubung sepenuhnya untuk klasifikasi")
    print("Arsitektur multi-inti di mana setiap ubin menjalankan MVM")
    print(
        "Inti individual yang terdiri dari susuan titik periferal untuk komunikasi dan konversi I/O"
    )


time.sleep(2)
print("----------------------------------------------------------")
print("MVM for combinatorial Optimization")

if nilai >= 50 and dayaBesar == True:
    print(
        "Evolusi energi rata rata RNN Hopfield berbasis RRAM untuk berbagai strategi optimasi"
    )
elif nilai <= 50 and dayaBesar == False:
    print("Pencarian minimum global yang mewakili solusi optimal")
else:
    print("Sketsa jaringan saraf berulang tipe Hopfield")


time.sleep(2)
print("----------------------------------------------------------")
print("MVM for Stochastic Computing")

if nilai >= 50 and dayaBesar == True:
    print(
        "Rangkaian PUF berbasis NVM berdasarkan rangkaian titik silang pasif perangkat memori"
    )
elif nilai <= 50 and dayaBesar == False:
    print("Realisasi jaringan saraf bayesian berbasis RRAM")
else:
    print("Sketsa jaringan saraf Bayesian dimana sinapsis dan neuron diwakili")


time.sleep(2)
print("----------------------------------------------------------")
print("Closed-Loop IMC Circuits for IMVM")
matriks = bool(input("Apakah memerlukan matriks? "))
linear = bool(input("Apakah memerlukan linear? "))

if linear == True and matriks == True:
    print("Rangkaian komputasi matriks pseudoinvers untuk penyelesaian masalah")
elif linear == True and matriks == False:
    print("Sirkuit perhitungkan vector eigen")
else:
    print("Rangkaian penyelesaian sistem liner 155 berbentuk Ax=B")


time.sleep(3)
print("----------------------------------------------------------")
print("Results of Closed Loop IMC for IMVM Problems")
if linear == True and matriks == True:
    print("Plot korelasi hasil experimen inversi matrix 3*3")
elif linear == True and matriks == False:
    print(
        "Plot korelasi keluaran rangkaian untuk algoritma PageRank dari kumpulan data"
    )
else:
    print("Demonstrasi eksperimental regresi linear pada perangkat RRAM")


time.sleep(3)
print("----------------------------------------------------------")
print("Content-addressable memory based on emerging memories")
time.sleep(2)
print(
    "Skema TCAM digital , dimana data biner dicocokan dengan pola yang disimpan dalam ternary himpunan"
)
time.sleep(2)
print(
    "Sel TCAM berbasis RRAM , diamna perangkat memori M1,m2 menyimpan nilai ternary sebagai kombinasi"
)
time.sleep(2)
print(
    "Analog berbasis  memristor sel CAM , diamna pola input analog dikodekan sebagai amplitudo tegangan pada jalur data (DL)"
)
time.sleep(2)
print("Pohon keputusan untuk klasifikasi kumpulan data Iris")
time.sleep(2)
print(
    "Analog-CAM implementasi pohon keputusan di (d), di mana setiap jalur akar-ke-daun berhubungan dengan baris array memory"
)

time.sleep(3)
print("----------------------------------------------------------")
print("IMC Training by an outer product")
skema = bool(input("Apakah memerlukan skema ?"))

if skema == True:
    print(
        "Representasi skema jaringan saraf tiruan , dimana pelatihan propagasi mundur bergantung pada pembaruan bobot."
    )
else:
    print("Implementasi produk luar secara crosspoint")

time.sleep(3)
print("----------------------------------------------------------")
print(
    "Experimental weight-update characteristic by pulses of equal amplitude and pulse-width for potentiation and depression"
)
RRAM = bool(input("Apakah memerlukan pembaruan RRAM ?"))
ECRAM = bool(input("Apakah memerlukan pembaruan ECRAM ?"))
CTM = bool(input("Apakah memerlukan pembaruan CTM ?"))

if RRAM == True:
    print("Perbarui karakteristik TaOx/TiO2 RRAM")
elif ECRAM == True:
    print("Perbarui karakteristik ECRAM berbasi Li ")
elif CTM == True:
    print("Perbarui karakteristik CTM berbasi MoS2 ")
else:
    print(
        "Plot korelasi faktor non-linearitas v dan jendala konduktansi yang dinormalisasi untuk berbagai perangkat sinaptik."
    )

time.sleep(3)
print("----------------------------------------------------------")
print("Long-term plasticity in memory-based artifical synapses")

if RRAM == True:
    print("Struktur sinapsis STDP berdasasrkan RRAM dengan struktur 1T1R")
elif skema == True:
    print(
        "Skema jaringan neuromorfik mirip perceptron yang mampu melakukan pembelajaran tanpa pengawasan"
    )
elif skema == True and RRAM == False:
    print("Skema konseptiual dari STDP")
else:
    print("Mengukur bobot sinaptik 1/R sebagai fungsi jumlah")

time.sleep(3)
print("----------------------------------------------------------")
print("Reservoir Computing(RC) based on volatile memory devices")
volatile = bool(input("Apakah memerlukan perangkat volatile ? "))

if skema == True and volatile == True:
    print(
        "Skema konseptial sistem RC, teridir dari lapisan reservoir acak dan terlatih lapisan pembacaan."
    )
elif skema == False or volatile == True:
    print("Jaringan memproses status reservoir untuk klasifikasi")
elif CTM == True and volatile == True:
    print("Ilustrasi charge trap memory (CTM) berbasis MoS2")
elif CTM == True or volatile == False:
    print(
        "Karakteristik terukur berbasis MoS2 Perangkat CTM menunjukan potensiasi yang diinduksi pulsa diikuti dengan peluruhan spontan"
    )
else:
    print("Pola masukan dan status reservoir")
