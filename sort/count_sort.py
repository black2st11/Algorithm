array = [1,2,3,1,45,1,2,3,45,51,2,3,54,12,2,4,6,7,34]

count_array = [0 for i in range(100)]



for i in array : 
    count_array[i] += 1

for i in range(len(count_array)):
    for _ in range(count_array[i]):
        print(i, end=' ')