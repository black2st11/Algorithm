"""
생각 필요, 고칠 필요
"""

import sys


def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]

    return result


def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


lock = []

lock_time = int(sys.stdin.readline().rstrip())

for _ in range(lock_time):
    lock.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(lock)
key_time = int(sys.stdin.readline().rstrip())

key = []
for _ in range(key_time):
    key.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = False

n = len(lock)
m = len(key)

print(key)
new_lock = [[0] * (n * 3) for _ in range(n * 3)]

for i in range(n):
    for j in range(n):
        new_lock[i + n][j + n] = lock[i][j]

for rotation in range(4):
    key = rotate_a_matrix_by_90_degree(key)
    for x in range(n * 2):
        for y in range(n * 2):
            for i in range(m):
                for j in range(m):
                    new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) == True:
                    result = True
                    print("True")
                    break
            for i in range(m):
                for j in range(m):
                    new_lock[x + i][y + i] -= key[i][j]
print(result)
