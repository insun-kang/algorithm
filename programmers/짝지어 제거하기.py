def solution(s):
    answer = 0
    stack=[]
    
    for i in s:
        if len(stack)>=1 and stack[-1]==i:
            stack.pop(-1)
        else:
            stack.append(i)
    if len(stack)==0:
        return 1
    else:
        return 0