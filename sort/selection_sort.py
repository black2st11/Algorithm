array = [5,6,1,4,8,2,3,9,7]

for i in range(len(array)):
    least = i
    for j in range(i, len(array)):
        if array[least] > array[j]:
            least = j
    
    array[i], array[least] = array[least], array[i]
    print(array)

print(array)