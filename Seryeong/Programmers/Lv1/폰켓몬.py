def solution(nums):
    maxNums = len(nums) // 2
    pokemon = len(set(nums))
    if pokemon < maxNums:
        answer = pokemon
    else:
        answer = maxNums
    return answer
