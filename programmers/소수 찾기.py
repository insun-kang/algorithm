from itertools import permutations

def find(lst):
    
    ans=0
    for i in lst:
        cnt=0
        for j in range(2, i):
            if i%j ==0:
                cnt+=1
                break
        if cnt==0:
            ans+=1
    return ans
    
    

def make(numbers):
    num_lst=[]
    for i in range(1, len(numbers)+1):
        temp=list(permutations(numbers, i))
        for j in temp:
            temp2=''.join(j)
            if int(temp2) not in num_lst and int(temp2) >1:
                num_lst.append(int(temp2))
    return num_lst
    
def solution(numbers):
    answer = 0
    
    
    return find(make(numbers))