import numpy as np

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

gabungan = np.concatenate((array1,array2),axis = 0) # menggabungkan menjadi 1 baris

sliced_array = gabungan[1:4]
print(sliced_array)