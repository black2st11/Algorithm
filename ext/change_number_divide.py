'''
백준 1075
'''
import sys
import math
n = sys.stdin.readline().rstrip()
m = int(sys.stdin.readline().rstrip())

index = 0
temp = 0


for i in range(len(n)-1, -1, -1):
    if index == 0 or index == 1:
        index += 1
        continue
    temp += int(n[i]) * (10 ** index)
    index +=1


for i in range(99):
    if (temp + i) % m == 0 :
        print('{:02d}'.format(i))
        break