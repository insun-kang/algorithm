for test_case in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))
    answer = 0
    for i in range(2, len(building)-2):
        tall = 0
        check = 0
        for j in range(i-2, i+3):
            if i == j:
                continue
            if building[i] <= building[j]:
                tall = 0
                check = 0
                break
            else:
                if building[j] >= tall:
                    check = 1
                    tall = building[j]

        if check == 1:
            answer += building[i] - tall

    print(f'#{test_case} {answer}')
