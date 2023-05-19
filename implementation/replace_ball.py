import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

baskets = [i for i in range(1, n + 1)]

for _ in range(m):
    prev, cur = map(int, sys.stdin.readline().rstrip().split())
    temp = baskets[prev - 1]
    baskets[prev - 1] = baskets[cur - 1]
    baskets[cur - 1] = temp

print(*baskets, sep=" ")
