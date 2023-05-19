"""
https://www.acmicpc.net/problem/1654
"""
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

cables = []

for _ in range(n):
    cables.append(int(sys.stdin.readline().rstrip()))

max_size = max(cables)
min_size = 1
while min_size <= max_size:
    slice_length = (min_size + max_size) // 2
    cnt = 0
    for cable in cables:
        cnt += cable // slice_length
    if cnt >= k:
        min_size = slice_length + 1
    elif cnt <= k:
        max_size = slice_length - 1

print(max_size)
