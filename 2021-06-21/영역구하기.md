# 문제

```
문제
눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면, 그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.



<그림 2>와 같이 분리된 세 영역의 넓이는 각각 1, 7, 13이 된다.

M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

출력
첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.
```

# 풀이 방법
먼저 종이에 영역표시가 된 부분을 모두 1로 바꾸어 주었고 이 종이를 활용해서 탐색을 진행하였다.
원하는 값은 영역의 개수와 각 영역의 크기이기 때문에 각각의 값을 맞는 위치에서 +1씩 시켜주는 방법으로 해결했고
출력시킬 때 end를 이용해서 리스트를 풀어주었다. 만약 값이 str이었다면 join을 활용하는 것도 방법인 듯하다.

    

# 코드
```
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

```

# 출처
    https://www.acmicpc.net/problem/2583
