def dfs(n):
    cnt = 0
    stack = [n]
    visit[n] = 1
    while stack:
        v = stack.pop(-1)

        for w in graph[v]:
            if visit[w] == 0:
                visit[w] = 1
                stack.append(w)
                cnt += 1
    return cnt


com = int(input())
nw = int(input())
visit = [0]*(com+1)
graph = [[] for i in range(com+1)]
for i in range(nw):
    n, v = map(int, input().split())
    graph[n].append(v)
    graph[v].append(n)
print(dfs(1))
