def solution(lists):
    ans = []

    ans.append(lists[0])

    for i in range(1, len(lists)):
        if lists[i-1] != lists[i]:
            ans.append(lists[i])

    # if lists[-1] != lists[-2]:
    #     ans.append(lists[-1])

    return ans


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
