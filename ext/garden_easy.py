import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

array = []

for _ in range(n+1):
    array.append([0]*(m+1))

left_side = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(1, n + 1):
    array[i][0] = left_side[i-1]

top_side = (list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1,m+ 1):
    array[0][i] = top_side[i-1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if array[i][j-1] == array[i-1][j] :
            array[i][j] = 0
        else :
            array[i][j] = 1

print(array[n][m])