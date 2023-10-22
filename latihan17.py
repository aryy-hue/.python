data = [5,12,8,20,7,14,3]
filter_data = []
i = 0

while i < len(data):
    if data[i] > 10:
        filter_data.append(data[i])
    i += 1

print('Data yang sudah di filter:', filter_data)