import sys

table = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

total_point = 0
result = 0.000000
for _ in range(20):
    lines = sys.stdin.readline().rstrip().split()
    if lines[2] != "P":
        total_point += float(lines[1])
        result += float(lines[1]) * table[lines[2]]

if result:
    result = round(result / total_point, 6)

print(f"{result:.6f}")
