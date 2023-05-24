import sys
from math import gcd

n, m = map(int, sys.stdin.readline().rstrip().split())
print(int(n * m / gcd(n, m)))
