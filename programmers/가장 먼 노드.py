from collections import deque


def solution(n, edge):
    def bfs():
        q = deque()
        q.append((1, 0))
        visit[1] = 0
        while q:
            v, cnt = q.popleft()

            for i in graph[v]:
                if visit[i] == -1:
                    visit[i] = cnt
                    q.append((i, cnt+1))

    graph = [[] for _ in range(n+1)]
    visit = [-1] * (n+1)
    answer = 0
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    bfs()
    check = max(visit)
    for i in visit:
        if i == check:
            answer += 1
    return answer
