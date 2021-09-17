import heapq

INF = int(1e9)


def dijkstra(start):
    distance = [INF]*(N+1)

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = i[1] + dist

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
answer = []
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, N+1):
    if i != X:
        answer.append(dijkstra(i)[X]+dijkstra(X)[i])

print(max(answer))
