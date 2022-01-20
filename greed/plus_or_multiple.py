import sys

string = sys.stdin.readline().rstrip()

answer = 0

for number in string:
    answer = max(int(number) + answer, int(number) * answer )

print(answer)