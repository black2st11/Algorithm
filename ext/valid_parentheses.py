"""
leet code : valid parentheses
"""


def is_valid(s):
    open_brackets = ["(", "[", "{"]
    storage = []
    for item in s:
        if item in open_brackets:
            storage.append(item)
        else:
            if len(storage) == 0:
                return False
            comp = storage.pop()
            if comp == "(" and item == ")":
                continue
            elif comp == "[" and item == "]":
                continue
            elif comp == "{" and item == "}":
                continue
            else:
                return False
    if len(storage) == 0:
        return True

    return False


print(is_valid("(]"))
