import heapq
INF = int(1e9)

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]
 
def unoion_parent(a, b):
    x = find_parent(a)
    y = find_parent(b)
    if x > y: parents[x] = y
    else: parents[y] = x
 
def find(a, b):
    x = find_parent(a)
    y = find_parent(b)
    return x != y
 

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    points = []
    for i in range(N):
        points.append([x[i],y[i]])
    q = []
    for i in range(N):
        for j in range(i+1, N):
            L = ((points[i][0]-points[j][0])**2)+((points[i][1]-points[j][1])**2)
            price = E*L
            heapq.heappush(q, (price, i, j))
    parents = [i for i in range(N)]

    answer = 0
    cnt = 0

    while q and cnt != N-1:
        price, a, b = heapq.heappop(q)

        if find(a, b):
            answer += price
            cnt += 1
            unoion_parent(a, b)
    answer = int(answer+0.5)

    print(f'#{tc} {answer}')