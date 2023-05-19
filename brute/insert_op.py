"""
https://www.acmicpc.net/problem/14888"""

import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

op = list(map(int, sys.stdin.readline().rstrip().split()))

min_result = int(1e9)
max_result = -1 * int(1e9)


def calculate(i, l, r):
    if i == 0:
        return l + r
    elif i == 1:
        return l - r
    elif i == 2:
        return l * r
    elif i == 3:
        # 예제를 계산해보다가 틀려서 확인해보니 -1 // 3 을 -1 로 반환 기댓값은 0
        return int(l / r)


def pick(rst, remain, flag):
    global min_result, max_result
    if len(remain) == 0:
        min_result = min(min_result, rst)
        max_result = max(rst, max_result)
        return

    for i in range(len(op)):
        if op[i] != 0:
            op[i] -= 1
            if flag == False:
                r = calculate(i, remain[0], remain[1])
                pick(r, remain[2:], True)
            else:
                r = calculate(i, rst, remain[0])
                pick(r, remain[1:], True)
            op[i] += 1


pick(0, arr, False)

print(max_result)
print(min_result)
