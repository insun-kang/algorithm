from collections import deque


def bfs(lst):
    q = deque()
    for y, x in lst:
        q.append((y, x, 0))
    while q:
        y, x, cnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                q.append((ny, nx, cnt+1))
                graph[ny][nx] = 1
    return cnt


N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

lst = []
answer = 0
for y in range(M):
    for x in range(N):
        if graph[y][x] == 1:
            lst.append((y, x))
if lst:
    answer = bfs(lst)
for y in range(M):
    if 0 in graph[y]:
        print(-1)
        break
else:
    print(answer)
