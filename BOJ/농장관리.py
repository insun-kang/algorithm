from collections import deque

def bfs(y, x):
    print(visit)
    q = deque()
    q.append((y, x))
    visit[y][x] = 1
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny < N and 0<= nx < M:
                if graph[ny][nx] > graph[y][x]:
                    return 0
                elif graph[ny][nx] == graph[y][x]:
                    if visit[ny][nx] == 0:
                        visit[ny][nx] = 1
                        q.append((ny, nx))
                else:
                    visit[ny][nx] = 1
    return 1


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

dy = [0,0,1,1,1,-1,-1,-1]
dx = [1,-1,0,1,-1,0,1,-1]

for y in range(N):
    for x in range(M):
        if visit[y][x] == 0:
            print(bfs(y, x))