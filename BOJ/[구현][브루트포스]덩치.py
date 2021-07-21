n = int(input())
answer = []

people = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    tmp = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            tmp += 1
    print(tmp, end = ' ')
