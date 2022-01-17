'''
백준 2839
'''

import sys

n = int(sys.stdin.readline().rstrip())

array = [99999] * (5001)

array[3] = 1
array[5] = 1

for i in range(6,5001):
    temp1 = 999999
    temp2 = 999999
    flag = 0
    if array[i-3] != 0:
        temp1 = array[i-3]
        flag = 1

    if array[i-5] != 0:
        temp2 = array[i-5]
        flag = 1
    if flag == 1 :
        array[i] = min(temp1, temp2) + 1
    else :
        array[i] = -1



if array[n] == -1 or array[n] >= 99999 :
    print(-1)
else:
    print(array[n])