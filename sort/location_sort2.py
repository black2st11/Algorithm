"""
백준 11651
"""
import sys

t = int(sys.stdin.readline().rstrip())

array = []
for _ in range(t):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

array.sort(key=lambda x: (x[1], x[0]))

for i in range(t):
    print(array[i][0], array[i][1])
