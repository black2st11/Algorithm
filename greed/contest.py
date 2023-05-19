"""
https://www.acmicpc.net/problem/2875
"""

import sys

array = list(map(int, sys.stdin.readline().rstrip().split()))


remain = 0
team = 0
if array[0] // 2 > array[1]:
    team = array[1]
    remain = array[0] % 2 + (array[0] // 2 - array[1]) * 2
else:
    team = array[0] // 2
    remain = array[0] % 2 + (array[1] - array[0] // 2)

if remain < array[2]:
    minus_team = 0
    if (array[2] - remain) % 3:
        minus_team += 1

    minus_team += (array[2] - remain) // 3
    if team - minus_team > 0:
        print(team - minus_team)
    else:
        print(0)
else:
    print(team)
