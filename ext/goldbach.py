"""
https://www.acmicpc.net/problem/2960
"""

import sys

MAX = 1000001

# n, m = map(int, sys.stdin.readline().rstrip().split())

array = [-1] * MAX
prime_array = []

result = []

for i in range(2, MAX):
    if array[i] == 0:
        continue

    if array[i] == -1:
        array[i] = 1
        prime_array.append(i)
    for j in range(2, MAX // 2 + 1):
        if i * j >= MAX:
            break

        array[j * i] = 0

while True:
    k = int(sys.stdin.readline().rstrip())

    if k == 0:
        break

    for i in range(1, k):
        try:
            if array[k - prime_array[i]] == 1:
                print(f"{k} = {prime_array[i]} + {k - prime_array[i]}")
                break
        except:
            pass
