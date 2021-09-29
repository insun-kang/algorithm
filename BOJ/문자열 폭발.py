ss = list(input())
bomb = list(input())
stack = []
for i in ss:
    stack.append(i)
    if len(stack) >= len(bomb):
        check = []
        checkcount = 0
        same = True
        for j in range(-1, (-len(bomb))-1, -1):
            if stack[j] != bomb[j]:
                same = False
                break

        if same == True:
            a = 0
            while a < len(bomb):
                stack.pop()
                a += 1
if stack:
    print(''.join(stack))
else:
    print('FRULA')
