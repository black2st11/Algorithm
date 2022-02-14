"""
https://www.acmicpc.net/problem/15649
"""
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

array = [1, 2, 3, 4, 5, 6, 7, 8]

is_pick = [False] * 8


def sequence(picked: list):
    if len(picked) >= m:
        print(" ".join(picked))
        return

    for i in range(n):
        if is_pick[i] == False:
            if picked:
                if int(picked[-1]) < array[i]:
                    is_pick[i] = True
                    picked.append(str(array[i]))
                    sequence(picked)
                    is_pick[i] = False
                    picked.pop()
            else:
                is_pick[i] = True
                picked.append(str(array[i]))
                sequence(picked)
                is_pick[i] = False
                picked.pop()


sequence([])
