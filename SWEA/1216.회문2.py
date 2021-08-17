for test_case in range(1, 11):
    t = int(input())
    strs = [input() for _ in range(100)]
    max_len = 1
    # 가로 판단
    for s in strs:
        for start in range(100):
            for end in range(100, -1, -1):
                str1 = s[start:end]
                if str1 == str1[::-1]:
                    if max_len < len(str1):
                        max_len = len(str1)
                    break
    # 세로 판단
    for r in range(100):
        for c in range(100):
            for end in range(100, r-1, -1):
                str1 = ''
                for i in range(end-r):
                    str1 += strs[r+i][c]
                if str1 == str1[:: -1]:
                    if max_len < len(str1):
                        max_len = len(str1)

                    break
    print(f'#{t} {max_len}')
