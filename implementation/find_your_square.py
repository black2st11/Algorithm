import sys

T = int(sys.stdin.readline().rstrip())
ns = []
ms = []

for _ in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())

    ns.append(n)
    ms.append(m)

line1 = max(ns) - min(ns)
line2 = max(ms) - min(ms)

print(line1 * line2)
