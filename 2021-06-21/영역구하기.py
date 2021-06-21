from collections import deque


m, n, k = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(k)]
paper = [[0]*n for _ in range(m)]
areas=[]
div=0

for point in points: 
    for x in range(point[0], point[2]):
        for y in range(point[1], point[3]):
            paper[y][x]=1

dx=[1,0,-1,0]
dy=[0,1,0,-1]
q=deque()
for i in range(m):
    for j in range(n):
        if paper[i][j] == 0:
            q.append((i,j))
            paper[i][j]=2
            area=1
            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]

                    if 0<=nx<m and 0<=ny<n and paper[nx][ny]==0:
                        q.append((nx, ny))
                        paper[nx][ny]=1
                        area += 1
            div+=1
            areas.append(area)
areas.sort()
print(div)
for i in areas:
print(i, end=' ')