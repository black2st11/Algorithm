import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

array = []
for _ in range(n):
    array.append(list(sys.stdin.readline().rstrip()))

for i in range(n):
    for j in range(m//2):
        if array[i][j] != '.':
            array[i][-1 * (1 +j)] = array[i][j]
            continue
        if array[i][-1 * (1 +j)] != '.':
            array[i][j] = array[i][-1 * (1 +j)] 
            continue

for i in array:
    for j in i:
        print(j,end='')
    print()