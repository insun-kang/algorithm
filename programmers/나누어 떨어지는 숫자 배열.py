def solution(arr, divisor):
    answer = []
    for i in arr:
        if int(i)%divisor==0:
            answer.append(int(i))
    if len(answer)==0:
        answer.append(-1)
    answer.sort()
    return answer