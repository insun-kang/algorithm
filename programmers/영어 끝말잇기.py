def solution(n, words):
    stack=[]
    
    person=0
    order=1
    
    for i in range(len(words)):
        
        person=i%n+1
        
        if i%n==0 and i!=0:
            order+=1
        if len(stack)==0:
            stack.append(words[i])
        else:
            if words[i] not in stack and words[i][0] == stack[-1][-1]:
                stack.append(words[i])
            else:
                return [person, order]
    return [0,0]