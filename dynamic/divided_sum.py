"""
백준 2225 생각 필요
"""
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

array = [[0] * (m + 1)] * (n + 1)
array[0][0] = 1

for i in range(n + 1):
    for j in range(1, m + 1):
        array[i][j] = array[i - 1][j] + array[i][j - 1]

print(array[n][m - 1] % 1000000000)
