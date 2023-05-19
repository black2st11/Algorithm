'''
숫자가 주어질 때 그 숫자를 123456 => [1+2+3], [4+5+6]으로 
자릿수 반 기준으로 나눈후 왼쪽 편의 합과 오른쪽 편의 합이 같으면 럭키 아니면 레디
'''
import sys

n = int(sys.stdin.readline().rstrip())

array = []
index = 1

while n >= 1:
    remain = n % 10 ** index
    array.append(remain // 10 ** (index -1))
    index += 1
    n -= remain 

if sum(array[:len(array)//2]) == sum(array[len(array)//2:]):
    print("LUCKY")
else :
    print('READY')