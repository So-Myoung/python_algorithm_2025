from math import ceil


def solution(progresses, speeds):
    ans = []
    lists = []
    count = 0

    for a, b in zip(progresses, speeds):
        lists.append(ceil((100 - a) / b))

    max_num = 0
    # print(lists)

    for i in lists:

        if i <= max_num:
            count += 1

        else:
            ans.append(count)
            count = 1
            max_num = i

    ans.append(count)



        # print(ans)
        # print(count)

    del ans[0]
    return ans


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))