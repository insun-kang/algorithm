T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    strs = [input() for _ in range(N)]
    answer = ''
    # 가로 판단
    for s in strs:
        for start in range(N-M+1):
            str1 = s[start:start+M]
            if str1 == str1[::-1]:
                answer = str1
    # 세로 판단
    for r in range(N - M + 1):
        for c in range(N):
            str1 = ''
            for i in range(M):
                str1 += strs[r+i][c]
            if str1 == str1[:: -1]:
                answer = str1

    print(f'#{test_case} {answer}')
