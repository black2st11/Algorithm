"""
https://www.acmicpc.net/problem/2331
"""
import sys

a, p = map(int, sys.stdin.readline().rstrip().split())

graph = []

graph.append(a)
idx = 0

while True:
    next_step = str(graph[idx])

    temp = 0
    for i in next_step:
        temp += pow(int(i), p)

    if temp in graph:
        print(graph.index(temp))
        break
    else:
        graph.append(temp)
        idx += 1
