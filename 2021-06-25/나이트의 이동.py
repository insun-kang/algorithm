from collections import deque

def bfs(a1, b1, a2, b2):
    dx=[2, 1, -2, -1, 1, 2, -1, -2]
    dy=[1, 2, 1, 2, -2, -1, -2, -1]
    
    answer=[]
    cnt = 0

    q=deque()

    q.append((b1, a1, cnt))
    chess_map[b1][a1]=1

    while q:

        y, x, cnt = q.popleft()

        if y == b2 and x == a2:
            return cnt

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<l and 0<=ny<l and chess_map[ny][nx] == 0:
                q.append((ny, nx, cnt+1))
                chess_map[ny][nx] = 1

    # return answer

n = int(input())

for i in range(n):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    chess_map = [[0 for _ in range(l)] for _ in range(l)]


    print(bfs(y1, x1, y2, x2))


