import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, end):
    distance = [INF] * (n+1)
    if start == end:
        return '-'

    q=[]
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[1]))
    
    return distance[end]

n, m = map(int, input().split())

graph = [[] for _ in range(m)]


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, n+1):
    answer=[0]*(n+1)
    for j in range(1, n+1):
        answer[j] = dijkstra(i, j)
    print(answer[1:])