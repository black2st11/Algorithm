import sys

n = int(sys.stdin.readline().rstrip())

sum_array = [0] * 30001

for i in range(2, n+1):
    sum_array[i] = sum_array[i-1] + 1

    if i % 2 == 0:
        sum_array[i] = min(sum_array[i], sum_array[i//2] + 1)
    
    if i % 3 == 0:
        sum_array[i] = min(sum_array[i], sum_array[i//3] + 1)

    if i % 5 == 0:
        sum_array[i] = min(sum_array[i], sum_array[i//5] + 1)

print(sum_array[n])