"""
https://www.acmicpc.net/problem/11652
"""

from collections import OrderedDict
import sys

cards = OrderedDict()

t = int(sys.stdin.readline().rstrip())


for _ in range(t):
    card = int(sys.stdin.readline().rstrip())
    try:
        cards[card] += 1
    except:
        cards[card] = 1

array = []
for key, value in cards.items():
    array.append([int(key), value])

array.sort(key=lambda x: (-x[1], x[0]))

print(array[0][0])
