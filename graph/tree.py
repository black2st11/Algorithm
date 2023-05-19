"""
https://www.acmicpc.net/problem/1991
"""
import sys


def dfs(start):
    print(start, end="")

    left = tree[start]["left"]
    if left != ".":
        dfs(left)
    right = tree[start]["right"]
    if right != ".":
        dfs(right)


def mid_dfs(start):

    left = tree[start]["left"]
    if left != ".":
        mid_dfs(left)

    print(start, end="")

    right = tree[start]["right"]
    if right != ".":
        mid_dfs(right)


def back_dfs(start):
    left = tree[start]["left"]
    if left != ".":
        back_dfs(left)

    right = tree[start]["right"]
    if right != ".":
        back_dfs(right)

    print(start, end="")


n = int(sys.stdin.readline().rstrip())
graph = []
tree = {}
for _ in range(n):
    a, b, c = sys.stdin.readline().rstrip().split()
    tree[a] = {"left": b, "right": c}


dfs("A")
print()
mid_dfs("A")
print()
back_dfs("A")
