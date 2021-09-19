def bf(start):
    visit[start] = 0
    for i in range(n):
        for v in range(1, n+1):
            for nv, nw in graph[v]:
                if visit[nv] > visit[v] + nw:
                    visit[nv] = visit[v] + nw
                    if i == n-1:
                        return 'YES'

    return 'NO'


tc = int(input())
INF = int(1e9)

for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visit = [INF] * (n+1)
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))
    print(bf(1))
