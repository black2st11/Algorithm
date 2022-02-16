"""
https://www.acmicpc.net/problem/6603
"""

import sys


def pick(step, n, f):
    if step >= 6:
        for i in range(n):
            if is_pick[i] == True:
                print(arr[i], end=" ")

        print()
        return

    for j in range(f, n):
        if is_pick[j] == True:
            continue
        if is_pick[j] != True:
            is_pick[j] = True
            pick(step + 1, n, j)
            is_pick[j] = False


while True:
    temp = list(map(int, sys.stdin.readline().rstrip().split()))

    if temp[0] == 0:
        break

    n = temp[0]
    arr = temp[1:]
    is_pick = [False] * n

    pick(0, n, 0)
    print()
