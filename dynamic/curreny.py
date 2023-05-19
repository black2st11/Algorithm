n, m = map(int, input().split())

array = [-1] * 10001

gte = 0
currency = []
for _ in range(n):
    temp = int(input())
    array[temp] = 1
    currency.append(temp)

for i in range(max(currency), 10001):
    compare = []
    for j in currency:
        if array[i - j] != -1:
            compare.append(array[i-j])
    
    if compare:
        array[i] = min(compare) + 1 

print(array[m])