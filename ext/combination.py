"""
https://www.acmicpc.net/problem/2004
문제가 이해가 안감
"""

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())


def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


five_count = count_number(n, 5) - count_number(m, 5) - count_number(n - m, 5)
two_count = count_number(n, 2) - count_number(m, 2) - count_number(n - m, 2)

result = min(five_count, two_count)
print(result)
