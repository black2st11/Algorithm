'''
https://www.acmicpc.net/problem/11728
'''
import sys

x = list(map(int,sys.stdin.readline().rstrip().split()))
a1 = list(map(int,sys.stdin.readline().rstrip().split()))
a2 = list(map(int,sys.stdin.readline().rstrip().split()))

p1 = 0
p2 = 0

result = []

while len(a1) > p1 and len(a2) > p2:
    if a1[p1] > a2[p2]:
        result.append(a2[p2])
        p2 += 1
    else :
        result.append(a1[p1])
        p1 += 1
else :
    if len(a1) > p1 :
        for i in range(p1, len(a1)):
            result.append(a1[i])

    if len(a2) > p2 :
        for i in range(p2, len(a2)):
            result.append(a2[i])

for i in result:
    print(i, end=' ')