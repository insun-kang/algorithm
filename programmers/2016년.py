def solution(a, b):
    answer = ''
    week=['SUN','MON','TUE','WED','THU','FRI','SAT']
    days=[31,29,31,30,31,30,31,31,30,31,30,31]
    sum_days=sum(days[:a-1])+b
    answer=week[sum_days%7-3]
    return answer