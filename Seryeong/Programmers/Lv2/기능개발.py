# 스택/큐
import math


def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]
        day = math.ceil((100 - progress) / speed)
        if not answer:
            answer.append(1)
            days.append(day)
        else:
            if days[-1] >= day:
                releases = answer.pop()
                answer.append(releases + 1)
            else:
                answer.append(1)
                days.append(day)
    return answer
