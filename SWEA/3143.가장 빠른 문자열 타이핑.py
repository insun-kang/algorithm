T = int(input())

for test_case in range(1, T + 1):
    A, B = input().split()
    len_a = len(A)
    len_b = len(B)
    cnt = 0
    idx = 0
    answer = 0

    while True:
        if idx >= len_a - len_b+1:
            break
        if B == A[idx:idx+len_b]:
            idx += len_b
            cnt += 1
        else:
            idx += 1

    answer = len_a - (cnt*len_b) + cnt
    print(f'#{test_case} {answer}')
