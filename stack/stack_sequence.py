"""
https://www.acmicpc.net/problem/1874
"""
import sys

n = int(sys.stdin.readline().rstrip())

array = []
comp = []
sta = []
for i in range(n, 0, -1):
    array.append(i)

for i in range(n):
    comp.append(int(sys.stdin.readline().rstrip()))
idx = 0
result = []
while array:
    if sta:
        if sta[-1] == comp[idx]:
            result.append("-")
            sta.pop()
            idx += 1
        else:
            sta.append(array.pop())
            result.append("+")
    else:
        sta.append(array.pop())
        result.append("+")
else:
    for i in range(idx, len(comp)):
        a = sta.pop()
        if a == comp[i]:
            result.append("-")
        else:
            print("NO")
            break
    else:
        print("\n".join(result))

