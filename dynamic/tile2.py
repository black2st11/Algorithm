"""
백준 11726
"""
import sys

n = int(sys.stdin.readline().rstrip())

tile = [0] * 1001

tile[1] = 1
tile[2] = 2


for i in range(3, 1001):
    tile[i] = tile[i - 1] + tile[i - 2]


print(tile[n] % 10007)
