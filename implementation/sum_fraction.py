import sys
from math import gcd

n, x = map(int, sys.stdin.readline().rstrip().split())
m, y = map(int, sys.stdin.readline().rstrip().split())

bottom = int(x * y / gcd(x, y))
top = int(n * bottom / x) + int(m * bottom / y)

while gcd(bottom, top) != 1:
    divisor = gcd(bottom, top)
    bottom = int(bottom / divisor)
    top = int(top / divisor)

print(top, bottom, sep=" ")
