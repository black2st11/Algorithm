import sys

n = int(sys.stdin.readline().rstrip())

team_count = 0
max_coward = 0

members = list(map(int, sys.stdin.readline().rstrip().split()))

members.sort(reverse=True)

coward_member = 0

for member in members:
    if member > max_coward :
        max_coward = member
    
    coward_member += 1
    
    if max_coward == coward_member:
        max_coward = 0
        team_count += 1
        coward_member = 0

print(team_count)