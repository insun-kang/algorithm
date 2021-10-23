left = ['[','{','(']
right = [']','}',')']
def check(lst):
    stack = []
    for i in lst:
        if stack:
            if i ==']' and stack[-1] == '[':
                stack.pop()
            elif i =='}' and stack[-1] == '{':
                stack.pop()
            elif i ==')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if stack:
        return False
    else:
        return True
def solution(s):
    answer = 0
    lst = list(s)
    for _ in range(len(s)-1):
        if check(lst):
            answer += 1
        lst.append(lst.pop(0))
        
    return answer