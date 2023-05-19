import sys

number = int(sys.stdin.readline().rstrip())

result = 0
for i in range(1, number + 1):
    array = list(map(int, str(i)))

    temp = i + sum(array)
    if temp == number:
        result = i
        break

print(result)