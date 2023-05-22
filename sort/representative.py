import sys

numbers = []

for i in range(5):
    numbers.append(int(sys.stdin.readline().rstrip()))
    numbers.sort()
print(sum(numbers) // 5)
print(numbers[2])
