'''
https://programmers.co.kr/learn/courses/30/lessons/42842
약간 어거지 느낌 남,,,
'''
import sys

sys.setrecursionlimit(int(1e9))

finished = False


def solution(brown, yellow):
    answer = []
    answer = make_carpet(brown, yellow, yellow, 1)
    return answer


def make_carpet(brown, yellow, width, height):
    if brown == (width + 2) * 2 + (height * 2):
        return [width + 2, height + 2]
    else:
        return make_carpet(brown, yellow, yellow / (height + 1), height + 1)


n, m = map(int, sys.stdin.readline().rstrip().split())

print(solution(n, m))
