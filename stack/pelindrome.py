import sys

N = int(sys.stdin.readline().rstrip())


def recursion(s, l, r, t):
    if l >= r:
        return (1, t)
    elif s[l] != s[r]:
        return (0, t)
    else:
        return recursion(s, l + 1, r - 1, t + 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1, 1)


for _ in range(N):
    word = sys.stdin.readline().rstrip()
    result = isPalindrome(word)
    print(*result, sep=" ")
