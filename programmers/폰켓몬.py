def solution(nums):
    answer = 0
    pick = len(nums) // 2
    if len(set(nums))<pick:
        answer=len(set(nums))
    else:
        answer=pick
    return answer