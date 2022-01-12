'''
정수 n이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 
모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하여라
'''

n = int(input())

count = 0
for i in range(n + 1):
    for minute in range(60):
        for second in range(60):
            if ('%02d%02d%02d' % (i,minute,second)).find('3') >= 1:
                count += 1
print(count)