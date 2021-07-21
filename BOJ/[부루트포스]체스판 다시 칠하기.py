n, m = map(int, input().split())

paper = [list(input()) for _ in range(n)]
answer = []


for i in range(0, n-7):
    for j in range(0, m-7):
        tmp1 = 0
        tmp2 = 0
        for y in range(j, j+8):
            for x in range(i, i+8):
                if (x+y) % 2 == 0:
                    if paper[x][y] == 'W':
                        tmp1 += 1 
                    if paper[x][y] == 'B':
                        tmp2 += 1
                else:
                    if paper[x][y] == 'B':
                        tmp1 += 1 
                    if paper[x][y] == 'W':
                        tmp2 += 1 
        answer.append(tmp1)
        answer.append(tmp2)

print(min(answer))