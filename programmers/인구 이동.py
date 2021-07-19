from collections import deque

def bfs(y, x):
    dx=[0, 0, 1, -1]
    dy=[1, -1, 0, 0]

    q= deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n and :
                q.append((ny, nx))

    return None

n, l, r = map(int, input().split())

contry = [list(map(int, input().split())) for _ in range(n)]

