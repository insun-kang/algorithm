def solution(n):
    answer = n+1
    bin_n=bin(n)[2:]
    n1=bin_n.count('1')
    while True:
        if bin(answer)[2:].count('1')==n1:
            return answer
        else:
            answer+=1