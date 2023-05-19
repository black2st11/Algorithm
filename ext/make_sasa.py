'''
백준 23825
'''

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

print(min(n //2 , m//2))