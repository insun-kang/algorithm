import heapq
import sys
input = sys.stdin.readline
INF=int(1e9)

v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v+1)]

distance = [INF] * (v+1)

for i in range(e):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))

def dijkstra(start):
    q=[]

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
# 모든 노드로 가기 위한 최단 거리를 출력

for i in range(1, v+1):

    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INF")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

