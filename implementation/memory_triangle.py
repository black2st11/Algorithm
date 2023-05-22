import sys


points = []

for _ in range(3):
    n = int(sys.stdin.readline().rstrip())
    points.append(n)

points.sort()

if sum(points) != 180:
    print("Error")
elif points[0] == points[1] and points[1] == points[2]:
    print("Equilateral")
elif points[0] == points[1] or points[1] == points[2] or points[2] == points[0]:
    print("Isosceles")
else:
    print("Scalene")
