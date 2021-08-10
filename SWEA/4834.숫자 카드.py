T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    check = [0] * 10

    for i in input():  # 0~9까지 역순으로 저장
        num = int(i)
        check[9 - num] += 1

    max_num = max(check)
    right_num = 9 - check.index(max_num)  # 원래 순서로 변환

    print(f'#{test_case} {right_num} {max_num}')
