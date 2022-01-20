'''
백준 4153
'''
import sys
import math

math.pi
while True:
    question = []
    x, y, z = map(int, sys.stdin.readline().rstrip().split())

    if x == 0 or y == 0 or z == 0:
        break
    else :
        question.append(x)
        question.append(y)
        question.append(z)
        question.sort()

        if question[0]**2 + question[1]**2 == question[2]**2:
            print("right")
        else :
            print('wrong')