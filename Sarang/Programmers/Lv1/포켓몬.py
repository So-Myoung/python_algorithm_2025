def solution(nums):
    answer = 0
    n_choice = len(nums)//2
    if n_choice < len(set(nums)):
        return n_choice
    answer = len(set(nums))
    return answer
