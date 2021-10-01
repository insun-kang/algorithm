T = int(input())

for i in range(T):
    n = int(input())
    score1 = list(map(int, input().split()))
    score2 = list(map(int, input().split()))

    score1[1] = score2[0]+score1[1]
    score2[1] = score1[0]+score2[1]
    for i in range(2, n):
        score1[i] = score1[i] + max(score2[i-2], score2[i-1])
        score2[i] = score2[i] + max(score1[i-2], score1[i-1])
    print(max(score1[-1], score2[-1]))
