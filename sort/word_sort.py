"""
https://www.acmicpc.net/problem/1181
"""

import sys

n = int(sys.stdin.readline().rstrip())

array = [[] for _ in range(51)]
array_1 = set()
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    array_1.add(word)

array_1 = sorted(array_1)

for i in array_1:
    array[len(i)].append(i)

for i in array:
    for j in i:
        print(j)
