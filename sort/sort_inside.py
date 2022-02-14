'''
https://www.acmicpc.net/problem/1427
'''

import sys

w = sys.stdin.readline().rstrip()
array =[]
for i in w:
    array.append(i)

array.sort(reverse=True)

print(''.join(array))