from collections import defaultdict

students = defaultdict(set)

n = int(input())
count_array = [[] for _ in range(101)]

for i in range(n):
    n, m = input().split(' ')
    count_array[int(m)].append(n)


for i in count_array:
    if i :
        for j in i:
            print(j, end=' ')


