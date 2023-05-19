"""
https://www.acmicpc.net/problem/5585
"""
import sys

money = int(sys.stdin.readline().rstrip())

cnt = 0
remain = [500, 100, 50, 10, 5, 1]
money = 1000 - money
while money != 0:
    for i in range(len(remain)):
        if money >= remain[i]:
            money -= remain[i]
            cnt += 1
            break
print(cnt)
