"""
https://programmers.co.kr/learn/courses/30/lessons/42839

소수 부분을 동적으로 처리 함
안할 시에 빠를 수도 있고 아닐 수도 있음
"""
number_array = set()


def solution(numbers):
    answer = 0
    cache = [0] * 9999999
    cache[1] = 1
    cache[0] = 1
    is_picked = []
    make_number("", numbers, is_picked, len(numbers))

    for i in range(2, 9999999):
        if cache[i] == 0:
            for j in range(2, 9999999):
                if i * j >= 9999999:
                    break
                cache[i * j] = 1
    print(number_array)
    for i in number_array:
        if cache[i] == 0:
            answer += 1

    return answer


def make_number(number, numbers, is_picked, count):
    if count < 0:
        return
    if number:
        number_array.add(int("".join(number)))

    for i in range(len(numbers)):
        if not i in is_picked:
            is_picked.append(i)
            make_number(number + numbers[i], numbers, is_picked, count - 1)
            is_picked.pop()


print(solution("17"))
