

N = int(input())
cnt = 1
book = [list(map(int, input().split())) for _ in range(N)]

answer = sorted(book, key = lambda x:(x[1],x[0]))
check = answer[0][1]
for i in range(1, N):
    if answer[i][0] >= check:
        check = answer[i][1]
        cnt += 1
print(cnt)