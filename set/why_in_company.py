import sys

n = int(sys.stdin.readline().rstrip())

company = {}

for _ in range(n):
    name, category = sys.stdin.readline().rstrip().split()
    company.update({name: category})

hard_worker = []

for k, v in company.items():
    if v == "enter":
        hard_worker.append(k)

hard_worker.sort(reverse=True)

for worker in hard_worker:
    print(worker)
