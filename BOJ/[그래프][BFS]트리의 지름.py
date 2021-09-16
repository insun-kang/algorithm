def bfs(start):
    MAX = -1
    idx = -1
    cost = [-1] * (V+1)
    q = []
    cost[start] = 0
    q.append(start)

    while q:
        v = q.pop(0)
        for w in graph[v]:
            if cost[w[0]] == -1:
                cost[w[0]] = cost[v] + w[1]
                q.append(w[0])
                if MAX < cost[w[0]]:
                    MAX = cost[w[0]]
                    idx = w[0]
    return MAX, idx


V = int(input())
new_idx = -1
graph = [[] for _ in range(V+1)]

for _ in range(V):
    tmp = list(map(int, input().split()))[:-1]
    for i in range(1, len(tmp), 2):
        graph[tmp[0]].append((tmp[i], tmp[i+1]))

new_idx = bfs(1)[1]

print(bfs(new_idx)[0])
