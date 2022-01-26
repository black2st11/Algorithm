import sys

n = int(sys.stdin.readline().rstrip())

game_map = []

for i in range(n):
    if i == 0 or i == n - 1:
        game_map.append([1] * n)
    else:
        game_map.append([1] + [0] * (n - 2) + [1])

apple_count = int(sys.stdin.readline().rstrip())

for _ in range(apple_count):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    game_map[x - 1][y - 1] = 2

spell_count = int(sys.stdin.readline().rstrip())
spell = []

for _ in range(spell_count):
    spell.append(sys.stdin.readline().rstrip().split())

second = 0
snake = [[0] * apple_count for _ in range(len(apple_count))]

while True:
