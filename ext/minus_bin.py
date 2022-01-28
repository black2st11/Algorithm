"""
https://www.acmicpc.net/problem/2089
"""

import sys

n = int(sys.stdin.readline().rstrip())

result = ""


while n:
    if n % 2 == 0:
        n //= -2
        result += "0"
    else:
        n = n // -2 + 1
        result += "1"

if result == "":
    result = "0"
print(result[::-1])
