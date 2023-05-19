import sys

black_pins = [1, 1, 2, 2, 2, 8]
white_pins = list(map(int, sys.stdin.readline().rstrip().split()))

result = [black_pins[i] - white_pins[i] for i in range(len(black_pins))]

print(*result, sep=" ")
