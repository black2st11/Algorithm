"""
백준 11057
"""
import sys

n = int(sys.stdin.readline().rstrip())

array = [[0] * 10 for _ in range(n + 1)]

for i in range(10):
    array[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            array[i][j] = sum(array[i - 1])
        elif j == 9:
            array[i][j] = 1
        else:
            array[i][j] = sum(array[i - 1]) - sum(array[i - 1][:j])

print(sum(array[n]) % 10007)
