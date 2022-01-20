import sys

string = sys.stdin.readline().rstrip()

count = [0] * 2


compare = string[0]

for word in string:
    if word != compare:
        count[int(compare)] += 1
        compare = word
else:
    count[int(word)] += 1

print(min(count))