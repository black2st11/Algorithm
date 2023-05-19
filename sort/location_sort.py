"""
백준 11650
"""
import sys

t = int(sys.stdin.readline().rstrip())

array = []
for _ in range(t):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

array.sort(key=lambda x: (x[0], x[1]))

for i in range(t):
    print(array[i][0], array[i][1])
