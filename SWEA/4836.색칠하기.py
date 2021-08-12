T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    colors = [list(map(int, input().split())) for _ in range(n)]
    paper = [[0]*10 for _ in range(10)]
    cnt = 0

    for i in colors:
        r1 = i[0]
        c1 = i[1]
        r2 = i[2]
        c2 = i[3]
        color = i[4]
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if paper[r][c] != color:
                    paper[r][c] += color
    for r in range(10):
        for c in range(10):
            if paper[r][c] == 3:
                cnt += 1
    print(f'#{test_case} {cnt}')
