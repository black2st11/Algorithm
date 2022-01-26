"""
https://www.acmicpc.net/problem/11655
"""

import sys

sentence = sys.stdin.readline().rstrip()
rot13 = ""

for alpha in sentence:
    if "0" <= alpha and alpha <= "9":
        rot13 += alpha
    elif " " == alpha:
        rot13 += " "
    elif "A" <= alpha and alpha <= "Z":
        text = ord(alpha) + 13
        if text > ord("Z"):
            text = text - (ord("Z") - ord("A") + 1)
        rot13 += chr(text)
    elif "a" <= alpha and alpha <= "z":
        text = ord(alpha) + 13
        if text > ord("z"):
            text = text - (ord("z") - ord("a") + 1)
        rot13 += chr(text)

print(rot13)
