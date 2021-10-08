from collections import deque


def bfs(y, x, n):
    q = deque()
    q.append((y, x, n))
    while q:
        y, x, n = q.popleft()
        if len(n) == 7:
            answer.add(n)
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < 4 and 0 <= ny < 4:
                q.append((ny, nx, n+board[ny][nx]))


T = int(input())

for tc in range(1, T+1):
    board = [list(input().split()) for _ in range(4)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    answer = set()
    for y in range(4):
        for x in range(4):
            bfs(y, x, board[y][x])
    print(f'#{tc} {len(answer)}')
