"""
https://www.acmicpc.net/problem/1541

괄호의 경우 +에만 치는 것으로 생각을 해서 처음에 -로 분리 후
+ 가 있는 문자열은 합연산 후 
첫번째 인덱스에 있는 것은 무조건 + 연산으로 시작이기 때문에 
넣은 후 - 연산 진행
"""
import sys

n = sys.stdin.readline().rstrip().split("-")

for i in range(len(n)):
    if "+" in n[i]:
        temp = sum(list(map(int, n[i].split("+"))))
        n[i] = temp

result = int(n[0])

for i in range(1, len(n)):
    result -= int(n[i])

print(result)
