# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses
# 어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능
# FIFO -> queue 이용 / 시간 복잡도 줄이기 위해 deque 사용
# 각 배포마다 몇 개의 기능이 배포되는지 리스트에 담아 return

from collections import deque


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    res = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        temp = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            temp += 1

        if temp > 0:
            res.append(temp)

    return res
