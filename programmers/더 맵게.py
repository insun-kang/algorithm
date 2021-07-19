import heapq

def solution(scoville, K):
    answer = 0
    temp=0
    heapq.heapify(scoville)
    
    while True:
        minsco=heapq.heappop(scoville)
        if minsco>=K:
            return answer
        else:
            if len(scoville)==0:
                return -1
                
            else:
                temp=minsco
                temp+=heapq.heappop(scoville)*2
                heapq.heappush(scoville, temp)
                answer+=1