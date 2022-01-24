"""
백준 11054(다시 생각)
"""
import sys

x = int(sys.stdin.readline().rstrip())

case = list(map(int, sys.stdin.readline().rstrip().split()))
reverse_case = case[::-1]

increase = [1 for i in range(x)]
decrease = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

result = [0 for i in range(x)]
for i in range(x):
    result[i] = increase[i] + decrease[x - i - 1] - 1

print(max(result))


# 생각은 해봄
# lis를 구한 후 해당하는 인덱스에서 잘라서 lds를 구한 후 자기 자신이 겹치니 -1

n = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [1] * n
dp_s = [1] * n
for i in range(len(array)):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(len(array) - 1, -1, -1):
    for j in range(i, len(array)):
        if array[i] > array[j]:
            dp_s[i] = max(dp_s[i], dp_s[j] + 1)

for i in range(len(array)):
    dp[i] = dp[i] + dp_s[i] - 1

print(max(dp))
