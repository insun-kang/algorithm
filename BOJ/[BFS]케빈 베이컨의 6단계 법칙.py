from collections import deque


def bfs(v):
    cnt = 0
    q = deque()
    q.append((v, cnt))
    while q:
        v, cnt = q.popleft()
        if not visited[v]:
            visited[v] = True
            cnt += 1
            cntlst[v] += cnt
            for w in graph[v]:
                q.append((w, cnt))


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
cntlst = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    visited = [False] * (N+1)
    bfs(i)
print(cntlst.index(min(cntlst[1:])))
