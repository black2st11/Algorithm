"""
https://www.acmicpc.net/problem/2309
"""

import sys

array = []

for _ in range(9):
    array.append(int(sys.stdin.readline().rstrip()))

array.sort()

is_pick = [False] * 9

result = []
finish = 0


def pick_dwarf(picked: list):
    global finish
    if finish:
        return

    if len(picked) == 7 and sum(picked) == 100:
        global result
        finish = 1
        result = picked[:]
        return True

    if len(picked) > 7:
        return False

    for i in range(len(array)):
        if is_pick[i] == False:
            is_pick[i] = True
            picked.append(array[i])
            if pick_dwarf(picked):
                return
            is_pick[i] = False
            picked.remove(array[i])


pick_dwarf([])

result.sort()
for i in result:
    print(i)
