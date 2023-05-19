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

parent = [0] * (n + 1)

for i in range(n+1):
    parent[i] = i

answer = []

for _ in range(m):
    spell, a, b = map(int, sys.stdin.readline().rstrip().split())

    if spell == 0 :
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
    else :
        if find_parent(parent, a) != find_parent(parent, b):
            answer.append('NO')
        else :
            answer.append('YES')

for i in answer:
    print(i)
