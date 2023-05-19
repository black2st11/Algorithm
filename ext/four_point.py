'''
백준 3009
'''
import sys


x_point = []
y_point = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    if x_point.count(x) == 0:
        x_point.append(x)
    else :
        x_point[x_point.index(x)] = 0

    if y_point.count(y) == 0:
        y_point.append(y)
    else :
        y_point[y_point.index(y)] = 0

for i in x_point:
    if i != 0:
        print(i, end=' ')

for i in y_point:
    if i != 0:
        print(i)
