from collections import deque
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

cities = []

for _ in range(m):
    start, dest, cost = map(int, sys.stdin.readline().rstrip().split())

    cities.append((cost, start, dest))

cities.sort()
answer = 0
last = 0
for city in cities:
    cost, start, dest = city    

    if find_parent(parent, start) != find_parent(parent, dest):
        union_parent(parent, start, dest)
        answer += cost
        last = cost
        
print(answer - last)