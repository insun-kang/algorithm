n = int(input())

line = []
answer=[]
result=0
for _ in range(n):
    x, y = map(int, input().split())
    line.append([x, y])

line.sort()
answer.append(line[0])
for i in range(1,n):
    if line[i-1][0] <= line[i][0] <= line[i-1][1]:
        if line[i][1] > line[i-1][1]:
            answer[0][1] = line[i][1]
    else:
        answer.append(line[i])
for i in answer:
    result += (i[1]-i[0])
print(result)
