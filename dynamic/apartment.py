'''
백준 2775
'''

import sys

array = [] 
for _ in range(15):
    array.append([i for i in range(1, 16)])


for i in range(1, 15):
    for j in range(1, 15):
        array[i][j] = array[i][j-1] + array[i-1][j]

t = int(sys.stdin.readline().rstrip())

result = []
for i in range(t):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    result.append(array[k][n-1])

for i in result:
    print(i)