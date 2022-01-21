import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

array = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0

for k in range(len(array)-2):
    for i in range(k+1, len(array)-1):
        for j in range(i+1, len(array)):
            if result < array[k]+ array[i] + array[j] and array[k]+ array[i] + array[j] <= m:
                result =  array[k]+ array[i] + array[j]
    
print(result)