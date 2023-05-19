import sys

n = sys.stdin.readline().rstrip()

array = []
result = 0
for i in n:
    array.append(i)

array.sort(reverse=True)

if not "0" in array:
    print(-1)
else:
    for i in array:
        result += int(i)

    if result % 3 != 0:
        print(-1)
    else:
        print("".join(array))

