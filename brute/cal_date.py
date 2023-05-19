"""
https://www.acmicpc.net/problem/1476
"""

import sys

e, s, m = map(int, sys.stdin.readline().rstrip().split())

e1, s1, m1 = 0, 0, 0
rst = 0
while e1 != e or s1 != s or m1 != m:
    rst += 1
    e1 += 1
    s1 += 1
    m1 += 1
    if e1 > 15:
        e1 = 1

    if s1 > 28:
        s1 = 1

    if m1 > 19:
        m1 = 1

print(rst)
