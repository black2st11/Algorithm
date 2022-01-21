import sys

n = [0] * 1000
n[0] = 1
n[1] = 1

for i in range(2, 1000):
    for j in range(2, 500):
        if i * j >= 1000 :
            break 
        n[i*j] = 1

mul1 = 0
mul2 = 0
result = int(1e9)
t = int(sys.stdin.readline().rstrip())
for i in range(len(n)):
    if n[i] == 0:
        mul1 = i
    for j in range(i+1 , len(n)):
        if n[j] == 0:
            mul2 = j
            break
    if mul1 * mul2 > t:
        result = min(mul1 * mul2, result)
    mul1 = 0
    mul2 = 0
            
print(result)
