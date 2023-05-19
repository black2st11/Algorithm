import sys

n = int(sys.stdin.readline().rstrip())

cards = list(map(int, sys.stdin.readline().rstrip().split()))

cards = [0] + cards
dp = cards[:]


for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + dp[j])
print(max(dp))
