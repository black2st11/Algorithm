import sys

S = sys.stdin.readline().rstrip()

result = set()

for i in range(len(S)):
    for j in range(len(S), 0, -1):
        result.add(S[i:j])

print(len(result) - 1)
