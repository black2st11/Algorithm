import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

home = []

for _ in range(n):
    home.append(int(sys.stdin.readline().rstrip()))

home.sort()

lt = 1
rt = home[-1] - home[0]

answer = 0

while lt <= rt:
    step = (lt + rt) // 2
    result = 1
    current = home[0]
    for i in range(1, len(home)):
        if home[i] >= current + step:
            result += 1
            current = home[i]

    if result >= k:
        lt = step + 1
        answer = step
    else:
        rt = step - 1

print(answer)
