from collections import deque

INF = int(1e9)


def bfs():
    visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0, 0, 1))
    visit[0][0][1] = 1
    while q:
        y, x, w = q.popleft()

        if y == N-1 and x == M-1:
            return visit[y][x][w]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 1 and w == 1:
                    visit[ny][nx][0] = visit[y][x][1] + 1
                    q.append((ny, nx, 0))
                elif graph[ny][nx] == 0 and w == 0:
                    visit[ny][nx][w] = visit[y][x][1] + 1
                    q.append((ny, nx, w))

    return -1


N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(bfs())
