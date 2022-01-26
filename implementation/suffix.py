"""
https://www.acmicpc.net/problem/11656
"""

import sys

word = sys.stdin.readline().rstrip()
array = []
for i in range(len(word)):
    array.append(word[i:])

array.sort()

for i in array:
    print(i, end=" ")
