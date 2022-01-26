"""
https://www.acmicpc.net/problem/10825
"""

import sys

t = int(sys.stdin.readline().rstrip())

students = []

for _ in range(t):
    name, korean, english, math = sys.stdin.readline().rstrip().split()
    students.append([name, int(korean), int(english), int(math)])

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])
