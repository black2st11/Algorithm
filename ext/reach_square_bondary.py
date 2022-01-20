'''
백준 1085
'''
import sys

x, y, w, h = map(int, sys.stdin.readline().rstrip().split())

a = min(w - x, x-0)
b = min(h - y, y-0)

print(min(a,b))