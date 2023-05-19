"""
https://www.acmicpc.net/problem/1158 - 이거는 진심 생각할 필요 있음

내장함수로 풀려고 하면 절대 시간내에 못 품
펜윅 트리 사용 해야함
"""
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

bottom = deque()

answer = []

for i in range(1, n + 1):
    bottom.append(i)

while bottom:
    bottom.rotate(-m)
    answer.append(str(bottom.pop()))
print("<" + ", ".join(answer) + ">")


## 펙윈트리 (볼려고 복붙함)
input = sys.stdin.readline


def update(i, diff):
    while i < size:
        bit[i] += diff
        i |= i + 1


def get(x):
    left, right = 0, size
    for i in range(exp + 1):
        mid = (left + right) >> 1
        val = bit[mid - 1]
        if val >= x:
            right = mid
        else:
            left = mid
            x -= val
    return left


n, k = map(int, input().split())

exp, size = 0, 1
while size < n:
    exp += 1
    size *= 2
bit = [0] * size
for i in range(n):
    update(i, 1)


ans = []
x = 0
for j in range(n, 0, -1):
    x = (x + k - 1) % j

    val = get(x + 1)
    update(val, -1)
    ans.append(val + 1)

sys.stdout.write(f'<{", ".join(map(str, ans))}>')
