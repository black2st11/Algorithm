'''
1. N 길이의 배열이 있다.
2. M 번을 더할 수 있다.
3. 같은 수는 K 번만 연속으로 더하는 게 가능하다. 그 이후에는 다른 숫자를 더한 후 다시 더하는게 가능하다.
'''

n, m, k= map(int, input().split(' '))

array = list(map(int, input().split(' ')))

array.sort()
count = 0
sum = 0
for i in range(m):
    if k > count:
       sum += array[n-1]
       count += 1 
    else :
        sum += array[n-2]
        count = 0

print(sum)