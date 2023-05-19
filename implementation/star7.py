"""
https://www.acmicpc.net/problem/2444
"""

# import sys

# n = int(sys.stdin.readline().rstrip())

# array = [""] * (2 * n - 1)


# for i in range(n):
#     array[i] = " " * (n - i - 1) + "*" * (2 * i + 1)
#     array[2 * n - 2 - i] = " " * (n - i - 1) + "*" * (2 * i + 1)


# for i in array:
#     print(i)

"""
https://www.acmicpc.net/problem/2443
"""

import sys

n = int(sys.stdin.readline().rstrip())

array = [""] * (n)


for i in range(n):
    array[i] = " " * i + "*" * (2 * (n - i) - 1)

for i in array:
    print(i)
