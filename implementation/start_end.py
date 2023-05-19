import sys

times = int(sys.stdin.readline().rstrip())

for _ in range(times):
    word = sys.stdin.readline().rstrip()
    print(word[0] + word[-1])
