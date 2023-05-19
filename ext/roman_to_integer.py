"""
leet code : roman to integer
"""

"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


def roman_to_int(s):
    symbol = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    result = 0
    temp = ""
    temp_num = 0
    for i in s:
        if temp == "":
            temp = i
            temp_num += symbol[i]
        else:
            if temp_num < symbol[i]:
                result += symbol[i] - temp_num
                temp = ""
                temp_num = 0
            elif temp_num > symbol[i]:
                result += temp_num
                temp = i
                temp_num = symbol[i]
            else:
                temp_num += symbol[i]
                temp = temp + i

    else:
        result += temp_num
    return result


print(roman_to_int("MCMXCIV"))
