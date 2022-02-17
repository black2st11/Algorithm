"""
https://www.acmicpc.net/problem/1475

처음에는 라운드로 처리했지만 반올림이다 보니 문제에 적합하지 않았다.
그래서 무조건 올림을 하는 ceil로 해야지 맞다
"""
import sys
import math

room = sys.stdin.readline().rstrip()

arr = [0] * 9

for i in room:
    if i == "9":
        arr[6] += 1
    else:
        arr[int(i)] += 1

arr[6] = math.ceil(arr[6] / 2)


print(max(arr))
