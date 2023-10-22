import numpy as np

array1 = np.array([1,2,3])
array2 = np.array([[4,5,6],[7,8,9]])

gabungan = np.vstack((array1,array2)) # menggabungkan
print(gabungan)