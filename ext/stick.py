'''
백준 1094
'''
import sys

x = int(sys.stdin.readline().rstrip())

stick = 64
count = 0

while x > 0:
    if stick > x :
        stick = stick // 2
    else :
        x = x - stick
        count += 1
print(count) 