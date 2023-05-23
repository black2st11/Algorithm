import sys

total_count = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

sorted_numbers = sorted(numbers)
numbers_dict = {}

count = 0
for i in sorted_numbers:
    if i not in numbers_dict:
        numbers_dict[i] = count
        count += 1

result = []
for i in numbers:
    result.append(numbers_dict[i])

print(*result, sep=" ")
