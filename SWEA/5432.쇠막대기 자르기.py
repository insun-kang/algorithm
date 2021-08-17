T = int(input())

for test_case in range(1, T + 1):
    stick = input()
    stack = []
    answer = 0

    for i in range(len(stick)):
        if stick[i] == '(':
            stack.append('(')
        else:
            stack.pop()

            if stick[i-1] == '(':
                answer += len(stack)
            else:
                answer += 1
    print(f'#{test_case} {answer}')
