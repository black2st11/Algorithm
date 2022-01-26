"""
https://www.acmicpc.net/problem/10808
"""

import sys

word = sys.stdin.readline().rstrip()

array = [0] * 26

for i in word:
    array[ord(i) - ord("a")] += 1

for i in array:
    print(i, end=" ")
