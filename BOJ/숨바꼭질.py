from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001
cnt = 0

q = deque()
q.append((N, cnt))
visited[N] = True
while q:
    N, cnt = q.popleft()

    if N == K:
        break

    if 0 <= N+1 < 100001 and visited[N + 1] is False:
        q.append((N+1, cnt+1))
        visited[N+1] = True
    if 0 <= N - 1 < 100001 and visited[N - 1] is False:
        q.append((N-1, cnt+1))
        visited[N-1] = True
    if 0 <= N * 2 < 100001 and visited[N * 2] is False:
        q.append((N*2, cnt+1))
        visited[N*2] = True

print(cnt)
