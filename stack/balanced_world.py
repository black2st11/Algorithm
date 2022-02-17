"""
https://www.acmicpc.net/problem/4949

다섯번 틀림 답변을 lowercase로 내야하하는데 uppercase로 내버려서

pop이 안될 경우에는 에러 발생을 시키니까 그대로 예외처리
"""

import sys


while True:
    arr = []
    flag = 0
    compare = ""
    while True:
        compare = compare + sys.stdin.readline().rstrip()
        if compare[-1] == ".":
            break

    if compare[0] == ".":
        break
    try:
        for i in compare:
            if i == "(" or i == "[":
                arr.append(i)
            elif i == ")" or i == "]":
                per = arr.pop()
                if per == "(" and i != ")":
                    flag = 1
                    print("no")
                    break
                elif per == "[" and i != "]":
                    flag = 1
                    print("no")
                    break
        else:
            if arr:
                print("no")
            else:
                print("yes")
    except Exception as e:
        print("no")

