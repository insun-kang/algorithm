from itertools import combinations

def solution(numbers):
    lsts=list(combinations(numbers, 2))
    answer = []
    for lst in lsts:
        if sum(lst) not in answer:
            answer.append(sum(lst))
    answer.sort()
    return answer