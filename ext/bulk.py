import sys

n = int(sys.stdin.readline().rstrip())

array = []
for _ in range(n):
    w, h = map(int, sys.stdin.readline().rstrip().split())
    array.append([w, h])

for i in array :
    rank  = 1 
    for j in array:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end= ' ')