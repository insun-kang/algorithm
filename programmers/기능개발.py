import math
def solution(progresses, speeds):
    max=0
    temp=[]
    answer = []
    for i in range(len(progresses)):
        temp.append(math.ceil((100-progresses[i])/speeds[i]))
    for i in range(len(temp)):
        if temp[i]>max:
            max=temp[i]
            print(max)
            answer.append(1)
            
        else:
            answer[-1]+=1
            print(answer)
    return answer