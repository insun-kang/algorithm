import sys

sys.setrecursionlimit(10000)


def dfs1(x):
    visited[x] = 1
    global tall

    for i in height_1[x]:
        if not visited[i]:
            tall += 1
            dfs1(i)
    return tall


def dfs2(x):
    visited[x] = 1
    global short

    for i in height_2[x]:
        if not visited[i]:
            short += 1
            dfs2(i)
    return short


n, m = map(int, sys.stdin.readline().split())
height_1 = [[] for _ in range(n + 1)]
height_2 = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    height_1[a].append(b)
    height_2[b].append(a)

cnt = 0

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    tall = short = 0

    temp1 = dfs1(i)

    visited = [0] * (n + 1)
    temp2 = dfs2(i)

    if temp1 + temp2 == n - 1:
        cnt += 1

print(cnt)