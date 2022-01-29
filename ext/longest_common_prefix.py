"""
leet code :  Longest Common Prefix
"""


def longest_common_prefix(strs):
    min_length = int(1e9)

    for i in strs:
        min_length = min(len(i), min_length)

    result = ""

    for i in range(min_length):
        initial = ""
        for item in strs:
            if initial == "":
                initial = item[i]

            if initial != item[i]:
                return result
        else:
            result += initial
    return result


print(longest_common_prefix(["dog", "racecar", "car"]))
