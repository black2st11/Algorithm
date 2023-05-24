import sys
from math import gcd

n = int(sys.stdin.readline().rstrip())

trees = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
distances = []


for i in range(1, len(trees)):
    distances.append(abs(trees[i - 1] - trees[i]))

distance = gcd(*distances)

print((trees[-1] - trees[0]) // distance - len(trees) + 1)
