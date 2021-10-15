#dp로 풀면 메모리 초과...

# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     graph = [list(map(int, input())) for _ in range(N)]
#     for i in range(1, N):
#         graph[i][0] += graph[i-1][0] 
#         graph[0][i] += graph[0][i-1]
#     for y in range(1, N):
#         for x in range(1, N):
#             graph[y][x] += min(graph[y-1][x], graph[y][x-1])
#     print(f'#{tc} {graph[-1][-1]}')

import heapq
INF = int(1e9)

def dijkstra(sy, sx):
    q = []
    heapq.heappush(q, (sy, sx, 0))
    distance[sy][sx] = 0
    while q:
        y, x, dist = heapq.heappop(q)
        if y == N-1 and x==N-1:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and dist+graph[ny][nx] < distance[ny][nx]:
                distance[ny][nx] = dist+graph[ny][nx]
                heapq.heappush(q, (ny, nx, distance[ny][nx]))
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    distance = [[INF] *(N) for _ in range(N)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    dijkstra(0,0)
    print(f'#{tc} {distance[-1][-1]}')