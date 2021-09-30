from collections import deque


def isolation(y, x):
    visit = [[0]*M for _ in range(N)]
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        if y == 0 or y == N-1 or x == 0 or x == M-1:
            return False
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0 and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                q.append((ny, nx))

    return True


def check(y, x):
    cnt = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
            cnt += 1
    if cnt >= 2:
        return True
    else:
        return False


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
time = 0
isol = []
for y in range(1, N-1):
    for x in range(1, M-1):
        if graph[y][x] == 0 and isolation(y, x):
            graph[y][x] = 2
            isol.append([y, x])
while True:
    cheese_check = 0
    visit = [[0]*M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and check(y, x):
                visit[y][x] = 1
    for y in range(N):
        for x in range(M):
            if visit[y][x] == 1:
                graph[y][x] = 0
                for i in range(4):
                    if graph[y+dy[i]][x+dx[i]] == 2:
                        graph[y+dy[i]][x+dx[i]] = 0
                cheese_check = 1
    print(graph)
    if cheese_check == 0:
        break
    else:
        time += 1
print(time)
