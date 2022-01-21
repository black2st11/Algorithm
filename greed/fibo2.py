'''
백준 1003   
'''
import sys

array = [0] * 41
array[0] = [1, 0]
array[1] = [0, 1]
for i in range(2, 41):
    array[i] =  [array[i-1][0] + array[i-2][0], array[i-1][1] + array[i-2][1]]

t= int(sys.stdin.readline().rstrip())

for _ in range(t):
    n= int(sys.stdin.readline().rstrip())
    print(array[n][0], array[n][1])
