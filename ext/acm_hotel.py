'''
백준 10250
'''
import sys

t = int(sys.stdin.readline().rstrip())

array = []
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().rstrip().split())
    ho1 = 1
    ho2 = 1  

    while n > h:
        if n>h :
            n -= h
            ho2 += 1

    ho1 = n
    array.append('{0}{1:0>2}'.format(ho1, ho2))

for i in array:
    print(int(i))