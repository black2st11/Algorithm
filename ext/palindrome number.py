"""
leet code : palindrome number
"""

import sys


def palindrom(num):
    string = str(num)
    if string == string[::-1]:
        return True
    return False


print(palindrom())
