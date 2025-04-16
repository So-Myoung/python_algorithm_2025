# 스택/큐
def solution(s):
    s = list(s)
    temp = []
    for i in s:
        if i == "(":
            temp.append(i)
        else:
            if temp and temp[-1] == "(":  # 괄호일 경우
                temp.pop()
            else:
                temp.append(i)
    if temp:
        return False
    else:
        return True

# 정확성: 69.5
# 효율성: 0.0
# 합계: 69.5 / 100.0
# def solution(s):
#     s = list(s)
#     temp = []
#     while s:
#         popped = s.pop(0)
#         if popped == "(":
#             temp.append(popped)
#         else:
#             if temp and temp[-1] == "(": # 괄호일 경우
#                 temp.pop()
#             else:
#                 temp.append(popped)
#     if temp:
#         return False
#     else:
#         return True
