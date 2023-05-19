"""
백준 1149 (다시생각)
"""

import sys

t = int(sys.stdin.readline().rstrip())

rgb = []

for i in range(t):
    rgb.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1, t):
    rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + rgb[i][2]

print(min(rgb[t - 1]))
print(rgb)
