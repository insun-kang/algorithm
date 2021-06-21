from collections import deque

n, m = map(int, input().split())
miro = []
for i in range(n):
    l=input()
    tmp=[]
    for j in l:
        tmp.append(int(j))
    miro.append(tmp)
    
dx=[1,0,-1,0]
dy=[0,1,0,-1]

cnt=1

q=deque()

q.append((0,0,cnt))
miro[0][0]=0
while q:
    x, y, cnt = q.popleft()
    if x==n-1 and y ==m-1:
        print(cnt)
        break

    cnt += 1
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<m and miro[nx][ny]==1:
            q.append((nx, ny, cnt))
            miro[nx][ny]=0