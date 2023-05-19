'''
1. N행 M열 로 이루어진 카드이다.
2. 가장 높은 카드를 뽑아야한다.
3. 먼저 N행을 고른 후 그 중에서 가장 작은 카드를 골라야한다. 
'''

n, m = map(int, input().split(' '))
least = 0
for i in range(n):
    a = list(map(int, input().split(' ')))
    compare = min(a)
    print(compare)
    if least < compare:
        least = compare

print(least)