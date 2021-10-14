import heapq
INF = int(1e9)

def dijkstra(start, graph):
    distance = [INF]*(N+1)
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

    return distance
T = int(input())

for tc in range(1, T+1):
    N,M,X = map(int, input().split())
    leave = [[] for _ in range(N+1)]
    arrival = [[] for _ in range(N+1)]
    MAX = 0
    for _ in range(M):
        x, y, c = map(int, input().split())
        leave[x].append((y, c))
        arrival[y].append((x, c))

    d1 = dijkstra(X, leave)
    d2 = dijkstra(X, arrival)
    for i in range(1, N+1):
        if MAX < d1[i]+d2[i]:
            MAX = d1[i]+d2[i]
    print(f'#{tc} {MAX}')