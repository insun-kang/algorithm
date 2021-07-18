from collections import deque


while True:
    w, h = map(int, input().split())
    map_list=[list(map(int, input().split())) for _ in range(h)]
    
    if w == 0 and h == 0:
        break
    
    dx=[1,1,1,-1,-1,-1,0,0]
    dy=[0,-1,1,0,-1,1,1,-1]

    q=deque()
    cnt=0

    for i in range(h):
        for j in range(w):
            if map_list[i][j] == 1:
                q.append((i, j))
                map_list[i][j] = 2

                while q:
                    x, y = q.popleft()
                    
                    for k in range(8):
                        nx=x+dx[k]
                        ny=y+dy[k]

                        if 0<=nx<h and 0<=ny<w and map_list[nx][ny]==1:
                            q.append((nx, ny))
                            map_list[nx][ny]=2
                cnt+=1
    print(cnt)
                        

