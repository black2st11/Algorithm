"""
https://www.acmicpc.net/problem/2108
"""

import sys

n = int(sys.stdin.readline().rstrip())

arr = []

cnt = [0] * 9000

for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
    cnt[arr[-1] + 4000] += 1

arr.sort()

max_cnt = max(cnt)
flag = 2 if cnt.count(max(cnt)) >= 2 else 1
rst = 0

for i in range(len(cnt)):
    if max_cnt == cnt[i]:
        flag -= 1
        if flag == 0:
            rst = i - 4000
            break

print(round(sum(arr) / len(arr)))
print(arr[len(arr) // 2])
print(rst)
print(max(arr) - min(arr))
