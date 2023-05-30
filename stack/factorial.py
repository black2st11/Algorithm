import sys


def factorial(n):
    if n == 0 or n == 1:
        return 1

    return factorial(n - 1) * n


N = int(sys.stdin.readline().rstrip())

print(factorial(N))
