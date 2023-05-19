"""
백준 2133 (생각 필요)
"""
import sys

n = int(sys.stdin.readline().rstrip())

tile = [0] * 1001

tile[0] = 1
tile[1] = 0
tile[2] = 3


for i in range(4, 1001):
    if i % 2 != 0:
        continue

    for j in range(2, i + 1, 2):
        another = 3 if j == 2 else 2
        tile[i] += another * tile[i - j]

print(tile[n])
