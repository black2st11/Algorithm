"""
백준 2156 (다시 생각)
"""
import sys

n = int(sys.stdin.readline().rstrip())

wines = [0]
dp = [0] * (n + 4)

for _ in range(n):
    wines.append(int(sys.stdin.readline().rstrip()))

if n < 3:
    print(sum(wines))
else:
    dp[1] = wines[1]
    dp[2] = wines[2] + wines[1]
    dp[3] = max(wines[3] + wines[1], wines[3] + wines[2], dp[2])
    for i in range(3, n + 1):
        dp[i] = max(
            wines[i] + dp[i - 2], wines[i] + wines[i - 1] + dp[i - 3], dp[i - 1]
        )

    print(dp[n])
