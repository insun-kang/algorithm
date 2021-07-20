def solution(n):
    answer = 1
    
    for i in range(1, n//2+1):
        check = 0
        for j in range(i, n//2+3):
            
            if check>n:
                break
            elif check == n:
                answer+=1
                break
            elif check < n:
                check += j
                
    return answer