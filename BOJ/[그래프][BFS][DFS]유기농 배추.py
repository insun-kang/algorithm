from collections import deque


def bfs(r, c):
    q = deque()
    q.append((r, c))
    cabbage[r][c] = 0

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and cabbage[nr][nc] == 1:
                q.append((nr, nc))
                cabbage[nr][nc] = 0


t = int(input())
for test_case in range(t):
    m, n, k = map(int, input().split())
    cabbage = [[0]*m for _ in range(n)]
    cnt = 0

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    for i in range(k):
        c, r = map(int, input().split())
        cabbage[r][c] = 1

    for r in range(n):
        for c in range(m):
            if cabbage[r][c] == 1:
                bfs(r, c)
                cnt += 1
    print(cnt)
