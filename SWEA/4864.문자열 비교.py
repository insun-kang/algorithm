T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        result = 1
    else:
        result = 0
    print(f'#{test_case} {result}')
