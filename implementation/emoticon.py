import sys

N = int(sys.stdin.readline().rstrip())

emoticon = []
index = -1
for _ in range(N):
    command = sys.stdin.readline().rstrip()
    if command == "ENTER":
        index += 1
        emoticon.append(set())
    else:
        emoticon[index].add(command)

result = 0
for i in emoticon:
    result += len(i)
print(result)
