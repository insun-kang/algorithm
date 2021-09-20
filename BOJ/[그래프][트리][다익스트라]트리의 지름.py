import heapq
INF = int(1e9)


def dijkstra(start):
    MAX = 0
    idx = 0
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        v, d = heapq.heappop(q)
        if distance[v] < d:
            continue
        for w in graph[v]:
            if distance[w[0]] == INF:
                if distance[w[0]] > d + w[1]:
                    distance[w[0]] = d + w[1]
                    heapq.heappush(q, (w[0], d + w[1]))
                    if MAX < distance[w[0]]:
                        MAX = distance[w[0]]
                        idx = w[0]
    return MAX, idx


n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
print(dijkstra(dijkstra(1)[1])[0])
