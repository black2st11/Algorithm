import sys

t = int(sys.stdin.readline().rstrip())

Chong = "ChongChong"
dancer = set()
dancer.add(Chong)

for _ in range(t):
    n, m = sys.stdin.readline().rstrip().split()

    if n == Chong or m == Chong:
        dancer.add(n)
        dancer.add(m)
    elif n in dancer or m in dancer:
        dancer.add(n)
        dancer.add(m)

print(len(dancer))
