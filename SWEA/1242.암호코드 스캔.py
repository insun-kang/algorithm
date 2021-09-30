code_rate = [
    (3, 2, 1, 1),
    (2, 2, 2, 1),
    (2, 1, 2, 2),
    (1, 4, 1, 1),
    (1, 1, 3, 2),
    (1, 2, 3, 1),
    (1, 1, 1, 4),
    (1, 3, 1, 2),
    (1, 2, 1, 3),
    (3, 1, 1, 2)
]

change = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def decode(in_str):
    code = list()
    idx = len(in_str) - 1
    while idx >= 0:
        if in_str[idx] == '1':
            n1 = n2 = n3 = n4 = 0
            while in_str[idx] == '1':
                n4 += 1
                idx -= 1
            while in_str[idx] == '0':
                n3 += 1
                idx -= 1
            while in_str[idx] == '1':
                n2 += 1
                idx -= 1
            multiple = min(n2, n3, n4)
            n1 = (7 * multiple) - (n2 + n3 + n4)
            idx -= n1
            n1 //= multiple
            n2 //= multiple
            n3 //= multiple
            n4 //= multiple
            decimal_num = code_rate.index((n1, n2, n3, n4))
            code.insert(0, decimal_num)
            if len(code) == 8:
                if ((code[0] + code[2] + code[4] + code[6]) * 3 + code[1] + code[3] + code[5] + code[7]) % 10 == 0:
                    if code not in codes:
                        codes.append(code)
                code = list()
        else:
            idx -= 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    in_arr = [input() for _ in range(N)]
    in_arr = list(set(in_arr))

    codes = list()
    for i in range(len(in_arr)):
        arr = in_arr[i]
        for j in range(M):
            if arr[j] != '0' or arr[len(arr) - i - 1] != '0':
                code = ''
                for k in range(M):
                    code += change[arr[k]]
                code = code.rstrip('0')
                decode(code)
                break
    result = 0
    code_length = len(codes)
    for i in range(code_length):
        result += sum(codes[i])

    print('#{} {}'.format(tc, result))
