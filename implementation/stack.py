"""
https://www.acmicpc.net/problem/10828
"""

import sys

t = int(sys.stdin.readline().rstrip())

array = []

for _ in range(t):
    spell = sys.stdin.readline().rstrip().split()

    if len(spell) == 2:
        array.append(int(spell[1]))
        continue

    if spell[0] == "top":
        if len(array) == 0:
            print(-1)
        else:
            print(array[-1])
        continue

    if spell[0] == "size":
        print(len(array))
        continue

    if spell[0] == "empty":
        length = 1 if len(array) == 0 else 0
        print(length)
        continue

    if spell[0] == "pop":
        if len(array) == 0:
            print(-1)
        else:
            print(array.pop())
