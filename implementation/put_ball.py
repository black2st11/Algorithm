import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().rstrip().split())

baskets = {i: 0 for i in range(1, n + 1)}

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())

    for b in range(i, j + 1):
        baskets[b] = k

print(*baskets.values(), sep=" ")
