T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    dict_str = {}
    max_v = 0

    for s in str1:
        if s not in dict_str:
            dict_str[s] = 0
    for s in str2:
        if s in dict_str:
            dict_str[s] += 1

    for key, value in dict_str.items():
        if value >= max_v:
            max_v = value
    print(f'#{test_case} {max_v}')
