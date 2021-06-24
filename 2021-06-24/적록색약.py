from collections import deque

def bfs(area, a, b, color):
    dx=[0, 0, 1, -1]
    dy=[1, -1, 0 ,0]

    q=deque()
    q.append((a, b))


    while q:
        y, x = q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and area[ny][nx] == color:
                area[ny][nx]=0
                q.append((ny, nx))

n = int(input())

non_color_blindness=[] #정상
color_blindness=[] #색맹

for i in range(n):
    l=input()
    tmp=[]
    tmp2=[]
    for j in l:
        tmp.append(j)
        if j =='G':
            j = 'R'
        tmp2.append(j)
    non_color_blindness.append(tmp)
    color_blindness.append(tmp2)

nbcnt=0
bcnt=0

for i in range(n):
    for j in range(n):
        if non_color_blindness[i][j] != 0:
            nbcnt += 1
            bfs(non_color_blindness, i, j, non_color_blindness[i][j])

        if color_blindness[i][j] != 0:
            bcnt += 1
            bfs(color_blindness, i, j, color_blindness[i][j])

print(nbcnt, bcnt)

