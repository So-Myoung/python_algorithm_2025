def solution(participant, completion):
    names = {}
    for person in completion:
        if person in names:
            names[person] += 1
        else:
            names[person] = 1

    while participant:
        person = participant.pop()
        if person in names and names[person] > 0:
            names[person] -= 1
        else:
            return person

# ===================================================
# 정확성: 58.3
# 효율성: 0.0
# 합계: 58.3 / 100.0
# def solution(participant, completion):
#     while participant:
#         person = participant.pop()
#         if person in completion:
#             completion.remove(person)
#         else:
#             return person
