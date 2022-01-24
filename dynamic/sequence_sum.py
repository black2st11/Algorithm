import sys

n = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().rstrip().split()))

dp = array[:]

for i in range(1, len(array)):
    dp[i] = max(dp[i], dp[i - 1] + array[i])
print(max(dp))
