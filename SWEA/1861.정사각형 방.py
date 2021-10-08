from collections import deque


def bfs(y, x):
    visit = [[0]*N for _ in range(N)]
    q = deque()
    q.append((y, x, 1))
    visit[y][x] = 1
    while q:
        y, x, cnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and rooms[ny][nx] == rooms[y][x] + 1 and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                q.append((ny, nx, cnt+1))

    return cnt


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    answer = []
    for y in range(N):
        for x in range(N):
            answer.append((rooms[y][x], bfs(y, x)))
    answer = sorted(answer, key=lambda x: (-x[1], x[0]))
    print(f'#{tc}', *answer[0])
