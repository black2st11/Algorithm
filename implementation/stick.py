"""
https://www.acmicpc.net/problem/10799
"""

import sys

stick = sys.stdin.readline().rstrip()
array = []
count = 0

for i in range(len(stick)):
    if stick[i] == "(":
        array.append(stick[i])
    else:
        if stick[i - 1] == "(":
            array.pop()
            count += len(array)
        else:
            array.pop()
            count += 1
print(count)
