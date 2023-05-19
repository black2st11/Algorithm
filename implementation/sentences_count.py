import sys

n = []
for line in sys.stdin:
    n.append(line[:-1])


for line in n:
    up, low, num, space = 0, 0, 0, 0
    for i in line:
        if ord("A") <= ord(i) and ord(i) <= ord("Z"):
            up += 1
        if ord("a") <= ord(i) and ord(i) <= ord("z"):
            low += 1
        if ord(" ") == ord(i):
            space += 1
        if ord("0") <= ord(i) and ord(i) <= ord("9"):
            num += 1
    print(low, up, num, space)
