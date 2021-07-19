def solution(n):
    answer = 0
    temp=''
    m=1
    if n<3:
        return n
    else:
        while True:
            temp=str(n%3)+temp
            n=n//3   
            if n<3:
                temp=str(n%3)+temp
                break
        for i in temp:
            answer+=int(i)*m
            m=m*3

        return answer