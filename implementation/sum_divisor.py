import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break
    divisors = []

    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    if sum(divisors) == n:
        print(f"{n} = ", end="")
        print(*divisors, sep=" + ")
    else:
        print(f"{n} is NOT perfect.")
