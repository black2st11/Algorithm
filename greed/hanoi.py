def hanoi(n, from_pos, to_pos, aux_pos, array):
    if n==1:
        array.append([from_pos, to_pos])
        return
    
    hanoi(n-1, from_pos, aux_pos, to_pos, array)

    array.append([from_pos, to_pos])

    hanoi(n-1, aux_pos, to_pos, from_pos, array)

n = int(input())
array = []
hanoi(n, 1, 3, 2, array)
print(len(array))
for i in array:
    for j in i :
        print(j, end=' ')
    print()