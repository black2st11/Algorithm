"""
https://www.acmicpc.net/problem/9012
"""

import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    array = []

    long = sys.stdin.readline().rstrip()
    temp = long[:]
    for short in temp:
        if short == "(":
            array.append("(")
        else:
            try:
                array.pop()
            except:
                print("NO")
                break
    else:
        if len(array) == 0:
            print("YES")
        else:
            print("NO")
