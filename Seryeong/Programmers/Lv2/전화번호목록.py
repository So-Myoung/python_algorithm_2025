# 정확성: 83.3
# 효율성: 8.3
# 합계: 91.7 / 100.0
# def solution(phone_book):
#     length = len(phone_book)
#     for i in range(length):
#         for j in range(length):
#             if i == j: # 같은 단어를 비교하면
#                 continue

#             slice = phone_book[j][0: len(phone_book[i])]
#             if phone_book[i] == slice: # 접두어이면
#                 return False
#     return True

# ===================================================
# 정확성: 83.3
# 효율성: 8.3
# 합계: 91.7 / 100.0
# def solution(phone_book):
#     length = len(phone_book)
#     for i in range(length):
#         for j in range(length):
#             if i == j: # 같은 단어를 비교하면
#                 continue
#             if phone_book[j].startswith(phone_book[i]): # 접두어이면
#                 return False
#     return True
