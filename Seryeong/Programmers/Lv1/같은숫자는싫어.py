# 스택/큐
# pop(0)의 시간복잡도는 O(n)
def solution(arr):
    answer = []
    while arr:
        popped = arr.pop()
        if arr:
            if popped != arr[-1]:
                answer.append(popped)
        else:
            answer.append(popped)
    answer.reverse()
    return answer


# 정확성: 71.9
# 효율성: 0.0
# 합계: 71.9 / 100.0
# def solution(arr):
#     answer = []
#     while arr:
#         popped = arr.pop(0)
#         if answer:
#             if popped != answer[-1]:
#                 answer.append(popped)
#         else:
#             answer.append(popped)
#     return answer
