import sys

code = sys.stdin.readline().rstrip()

dp = [0] * (len(code) + 1)
dp[0] = dp[1] = 1

if not code:
    print("0")
elif code[0] == "0":
    print("0")
else:
    code = "0" + code
    for i in range(2, len(code)):
        if int(code[i]) > 0:
            dp[i] += dp[i - 1]

        if int(code[i - 1] + code[i]) >= 10 and int(code[i - 1] + code[i]) <= 26:
            dp[i] += dp[i - 2]
    print(dp[len(code) - 1] % 1000000)
