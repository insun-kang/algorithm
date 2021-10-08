def check(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    cnt = 0
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            cnt += 1
    if cnt == 1:
        return True


def trans_bin_to_ter(lst):
    n = trans_bin_to_dec(lst)
    result = []
    while n > 0:
        n, mod = divmod(n, 3)
        result.append(str(mod))
    return result[::-1]


def trans_bin_to_dec(lst):
    n = 0
    result = 0
    for i in lst:
        result += int(i)*(2**(len(lst)-n-1))
        n += 1
    return result


T = int(input())

for tc in range(1, T+1):
    binary = list(input())
    ternary = list(input())
    answer = 0
    trans_bin_to_dec(binary)
    trans_bin_to_ter(binary)
    for i in range(1, len(binary)):
        if binary[i] == '1':
            binary[i] = '0'
            if check(trans_bin_to_ter(binary), ternary):
                answer = trans_bin_to_dec(binary)
                break
            else:
                binary[i] = '1'

        elif binary[i] == '0':
            binary[i] = '1'
            if check(trans_bin_to_ter(binary), ternary):
                answer = trans_bin_to_dec(binary)
                break
            else:
                binary[i] = '0'
    print(f'#{tc} {answer}')
