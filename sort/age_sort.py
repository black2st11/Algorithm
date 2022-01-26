"""
백준 10814
"""

import sys

t = int(sys.stdin.readline().rstrip())

array = []

for i in range(t):
    age, name = sys.stdin.readline().rstrip().split()

    array.append([int(age), i, name])

array.sort(key=lambda x: (x[0], x[1]))

for item in array:
    print(item[0], item[2])
