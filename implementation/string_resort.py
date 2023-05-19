'''
스트링을 받은 후 앞 문자는 알파벳으로 정렬 후 뒤에는 숫자들의 합을 나타내라
'''
import sys

n = sys.stdin.readline().rstrip()

alphabet = []
number = []

for i in n:
    try :
        number.append(int(i))
    except :
        alphabet.append(i)

alphabet.sort()

sum_number = sum(number)
print(''.join(alphabet)+(str(sum_number)))