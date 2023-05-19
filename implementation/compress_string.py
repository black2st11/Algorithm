"""
완전 탐색 이용 - 생각 필요
"""
import sys

sentences = sys.stdin.readline().rstrip()

result = len(sentences)

for step in range(1, len(sentences) // 2 + 1):
    compressed = ""
    prev = sentences[0:step]
    count = 1

    for j in range(step, len(sentences), step):
        if prev == sentences[j : j + step]:
            count += 1
        else:
            compressed += str(count) + prev if count >= 2 else prev
            prev = sentences[j : j + step]
            count = 1

    compressed += str(count) + prev if count >= 2 else prev
    result = min(result, len(compressed))

print(result)
