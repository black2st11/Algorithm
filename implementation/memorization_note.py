import sys
from collections import Counter


n, m = map(int, sys.stdin.readline().rstrip().split())
note = Counter()
ordered_note = []
index = -1
prev_times = -1

for _ in range(n):
    word = sys.stdin.readline().rstrip()

    if len(word) < m:
        continue

    note[word] += 1

for item in sorted(note.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
    print(item[0])
