from collections import deque

def solution(maps):
    def bfs(y, x):
        q=deque()
        q.append((y, x, 0))
        maps[y][x] = 0
        while q:
            y, x, cnt = q.popleft()
            if y ==M-1 and x==N-1:
                return cnt+1
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if 0<=ny<M and 0<=nx<N and maps[ny][nx] == 1:
                    maps[ny][nx] = 0
                    q.append((ny, nx, cnt+1))
        return -1
    answer = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    N = len(maps[0])
    M = len(maps)
    
    return bfs(0,0)