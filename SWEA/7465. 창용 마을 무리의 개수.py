def bfs(start, cnt):
    q = []
    q.append(start)
    visit[start] = cnt
    while q:
        n = q.pop(0)
        for i in graph[n]:
            if visit[i] == 0:
                visit[i] = cnt
                q.append(i)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph=[[] for _ in range(N+1)]
    visit = [0]*(N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    cnt = 1
    for i in range(1,N+1):
        if visit[i] == 0:
            bfs(i, cnt)
            cnt+=1
    print(f'#{tc} {max(visit)}')