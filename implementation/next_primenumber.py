import sys
from math import sqrt, floor

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    t = int(sys.stdin.readline().rstrip())
    result = t
    while True:
        if result == 0 or result == 1:
            result += 1
            continue
        for i in range(2, int(sqrt(result)) + 1):
            if result % i == 0:
                result += 1
                break
        else:
            print(result)
            break
