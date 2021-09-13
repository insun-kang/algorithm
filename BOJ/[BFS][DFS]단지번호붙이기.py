from collections import deque


def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 0
    result = 1
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] != 0:
                result += 1
                q.append((ny, nx))

                graph[ny][nx] = 0

    return result


N = int(input())

graph = [list(map(int, input())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = []
cnt = 0

for y in range(N):
    for x in range(N):
        if graph[y][x] != 0:
            answer.append(bfs(y, x))
            cnt += 1
answer.sort()
print(cnt)
for i in answer:
    print(i)
