import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().rstrip().split())

members = Counter()

for _ in range(n):
    members[sys.stdin.readline().rstrip()] += 1

for _ in range(m):
    members[sys.stdin.readline().rstrip()] += 1

dudbojob = []

for k, v in members.items():
    if v == 2:
        dudbojob.append(k)

dudbojob.sort()

print(len(dudbojob))
for member in dudbojob:
    print(member)
