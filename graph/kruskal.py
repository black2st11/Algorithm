import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a= find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b 

n, m = sys.stdin.readline().rstrip().split()


parent = [0] * (n + 1)

for i in range(1, n+1):
    parent[i] = i

edges = []

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    edges.append((z, x, y))

edges.sort()
sum = 0
for edge in edges:
    z, x, y = edge

    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        sum += z
