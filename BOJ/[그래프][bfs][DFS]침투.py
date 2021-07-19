from collections import deque
m, n = map(int, input().split())

fiber = []
answer=''

for i in range(m):
    l=input()
    tmp=[]
    for j in l:
        tmp.append(int(j))
    fiber.append(tmp)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

q=deque()

for i in range(n):
    if fiber[0][i] == 0:
        q.append((0,i))
        fiber[0][i]=1
        while q:
            y, x = q.popleft()

            if y == m-1:
                answer='YES'
                break
            
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<n and 0<=ny<m and fiber[ny][nx]==0:
                    q.append((ny, nx))
                    fiber[ny][nx] = 1
            
if answer != 'YES':
    answer='NO'
print(answer)