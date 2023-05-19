n, m = map(int, input().split(' '))

array1 = list(map(int, input().split(' ')))    
array2 = list(map(int, input().split(' ')))

array1.sort()
array2.sort()

for i in range(n):
    for j in range(n-1, 0, -1):
        if array1[i] < array2[j]:
            array1[i], array2[j] = array2[j], array1[i]
            m -= 1
            break
    if m == 0 :
        break

print(sum(array1))


