import sys

while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == 0 and b == 0 and c == 0:
        break

    if len(set([a, b, c])) == 1:
        print("Equilateral")
    elif max([a, b, c]) >= (a + b + c) - max([a, b, c]):
        print("Invalid")
    elif len(set([a, b, c])) == 2:
        print("Isosceles")
    else:
        print("Scalene")
