"""
https://www.acmicpc.net/problem/1931

예시에서는 정렬 순서가 끝나는 순서, 시작 순서로 되어있었지만 어떻게 나올지 모르니 이 순으로 정렬 후
회의실을 순서대로 배정
"""
import sys

n = int(sys.stdin.readline().rstrip())

array = []
conference = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    array.append([start, end])

array.sort(key=lambda x: (x[1], x[0]))


cnt = 0

end_time = 0

# 이전 끝나는 시간과 다음 시작시간과 비교해서 같거나 클 경우 배정하는 방식
for i in array:
    start, end = i
    if start >= end_time:
        cnt += 1
        end_time = end
print(cnt)
