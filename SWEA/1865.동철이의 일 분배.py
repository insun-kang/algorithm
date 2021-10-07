def work(depth, p):
    global MAX
    result = []
    if depth == N:
        if MAX < p:
            MAX = p
        return
    if p <= MAX:
        return
    for i in range(N):
        if visit[i] == 1:
            continue
        visit[i] = 1
        np = p*lst[depth][i]/100
        work(depth+1, np)
        visit[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*N
    p = 1
    MAX = 0
    work(0, p)
    print('#{} {}'.format(tc, format(MAX*100, '.6f')))
