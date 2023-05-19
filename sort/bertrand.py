'''
백준 4948
'''
import sys

Flag = True
question = []
while Flag:
    n = int(sys.stdin.readline().rstrip())
    if n != 0 :
        question.append(n)
    else :
        Flag = False

n = max(question)

array = [0] * ((2 * n) +1 )

array[1] = 1
array[0] = 1

for i in range(2, ((2 * n) +1 )):
    for j in range(2, ((2 * n) +1 )):
        if i * j > ((2 * n)):
            break
        array[i * j] = 1

for j in question:
    answer = 0
    for i in range(j+1, 2 * j+1):
        if array[i] == 0:
            answer += 1
    print(answer)