import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

baskets = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    baskets = baskets[: i - 1] + list(reversed(baskets[i - 1 : j])) + baskets[j:]

print(*baskets, sep=" ")
