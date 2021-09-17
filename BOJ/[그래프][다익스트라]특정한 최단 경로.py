import heapq
INF = int(1e9)


def dijkstra(start):
    distance = [INF]*(N+1)
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)

        if dist > distance[now]:
            continue
        for e, d in graph[now]:
            cost = dist + d
            if cost < distance[e]:
                distance[e] = cost
                heapq.heappush(q, (e, cost))
    return distance


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]


for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

tmp1 = dijkstra(1)
tmp2 = dijkstra(v1)
tmp3 = dijkstra(v2)

path1 = tmp1[v1] + tmp2[v2] + tmp3[N]
path2 = tmp1[v2] + tmp3[v1] + tmp2[N]

answer = 0
if path1 < path2:
    answer = path1
else:
    answer = path2

if answer >= INF:
    print(-1)
else:
    print(answer)
