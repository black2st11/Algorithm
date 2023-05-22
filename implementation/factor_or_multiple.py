import sys

while True:
    n, m = map(int, sys.stdin.readline().rstrip().split())

    if n == m:
        break

    if n % m == 0:
        print("multiple")
    elif m % n == 0:
        print("factor")
    else:
        print("neither")
