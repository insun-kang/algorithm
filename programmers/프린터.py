def solution(priorities, location):
    ord=[i for i in range(len(priorities))]
    res=[]
    
    while len(priorities) !=0 :
        if priorities[0]==max(priorities):
            res.append(ord.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            ord.append(ord.pop(0))
            
    return res.index(location)+1