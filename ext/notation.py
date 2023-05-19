"""
https://www.acmicpc.net/problem/11005

"""
# import sys

# notation = []

# for i in range(10):
#     notation.append(f"{i}")

# for i in range(ord("A"), ord("Z") + 1):
#     notation.append(chr(i))

# n, m = map(int, sys.stdin.readline().rstrip().split())

# result = ""
# while n:
#     if n % m == 0:
#         result = notation[0] + result
#     else:
#         result = notation[n % m] + result
#         n -= n % m
#     n = n // m

# print(result)

"""
https://www.acmicpc.net/problem/2745
int (n , m) 하면 진법 변환이 되네??/ .....
괜히 만듬 ㅋㅋ
"""
# import sys

# notation = []

# for i in range(10):
#     notation.append(f"{i}")

# for i in range(ord("A"), ord("Z") + 1):
#     notation.append(chr(i))

# n, m = sys.stdin.readline().rstrip().split()

# result = 0
# n = n[::-1]

# for i in range(len(n)):
#     result += notation.index(n[i]) * int(m) ** i
#     print(result)

# print(result)

"""
https://www.acmicpc.net/problem/1212

"""

# import sys


# n = sys.stdin.readline().rstrip()

# ten = int(n, 8)

# print(oct(ten):[2:])
