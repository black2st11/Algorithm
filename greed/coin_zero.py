"""
https://www.acmicpc.net/problem/11047
"""

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

coins = []

for i in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

coins = coins[::-1]

result = 0
for coin in coins:
    if m == 0:
        break
    if coin <= m:
        result += m // coin
        m = m % coin

print(result)
