from collections import deque

def bfs(sy, sx):
    global answer
    visit = [[0]*N for _ in range(N)]
    value = []
    q = deque()
    q.append((sy, sx, 1))
    visit[sy][sx] = 1
    value.append(cafe[sy][sx])
    while q:
        print(q)
        print(visit)
        y, x, cnt = q.pop()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny == sy and nx == sx:
                answer.append(cnt)
                break
            if 0<=nx<N and 0<=ny<N and visit[ny][nx] == 0  and cafe[ny][nx] not in value:
                    visit[ny][nx] = 1
                    value.append(cafe[ny][nx])
                    q.append((ny, nx, cnt+1))

    

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    dx = [1,1,-1,-1]
    dy = [1,-1,1,-1]

    answer = []
    # for y in range(N):
    #     for x in range(N):
    bfs(0,1)
    print(answer)
