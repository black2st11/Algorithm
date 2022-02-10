"""
https://www.acmicpc.net/problem/2448
생각 필요
"""
import sys

N = int(sys.stdin.readline())


def top(x):
    blank = " " * ((len(x[0]) + 1) // 2)
    return [blank + i + blank for i in x]


def bottom(x):
    return [i + " " + i for i in x]


def star(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    n //= 2
    x = star(n)
    return top(x) + bottom(x)


print("\n".join(star(N)))

