def dfs(depth, cnt):
    global answer

    if answer < cnt:
        answer = cnt

    for nd in graph[depth]:
        if not visit[nd]:
            visit[nd] = 1
            dfs(nd, cnt + 1)
            visit[nd] = 0

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visit = [0]*(N+1)
    answer = 0

    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(N):
        visit[i] = 1
        dfs(i,1)
        visit[i] = 0
    print(f'#{tc} {answer}')