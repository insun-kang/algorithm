t = int(input())

for a in range(t):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    num = 0
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    directionIdx = 0
    curX, curY = 0, -1

    while num < n * n:
        tmpX = curX + direction[directionIdx][0]
        tmpY = curY + direction[directionIdx][1]

        # 범위 초과시 방향 바꿔줌
        if tmpX < 0 or tmpY < 0 or tmpX >= n or tmpY >= n or arr[tmpX][tmpY] != 0:
            directionIdx += 1
            if directionIdx == 4:
                directionIdx = 0
        else:
            num += 1
            curX, curY = tmpX, tmpY
            arr[curX][curY] = num

    # 출력
    print("#%d" % (a+1))
    for line in arr:
        print(' '.join(map(str, line)))
