def solution(nums):
    len_arr = len(nums) / 2
    len_set = len(set(nums))
    return min(len_arr, len_set)
