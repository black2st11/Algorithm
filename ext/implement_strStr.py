"""
leet code : Implement strStr()
"""


def strStr(haystack, needle):
    try:
        return haystack.index(needle)
    except:
        return 0
