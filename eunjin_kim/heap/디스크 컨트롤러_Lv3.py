import heapq as hq

def solution(jobs):
    answer = []
    
    time_queue = []
    for i in range(len(jobs)):
        hq.heappush(time_queue, (jobs[i][0], jobs[i][1], i)) #요청시간순
        
    time = 0
    ready_queue = []
    
    while time_queue or ready_queue:
        while time_queue:
            start, end, idx = hq.heappop(time_queue)
            if start <= time:
                hq.heappush(ready_queue, (end, start, idx)) #대기큐에 작업을 넣을 때
            else:
                hq.heappush(time_queue, (start, end, idx))
                break
                
        if ready_queue:
            end, start, idx = hq.heappop(ready_queue)
            time += end
            answer.append(time - start)
        else:
            time += 1

    return sum(answer) // len(answer)


"""
jobs [0, 3]
작업요청시간, 소요시간
우선순위 : [1]번째 > [0]번째 > 순서

종료시간 - [0]번째요청시간 의평균

heap에 넣을 원소 ([1]소요시간, [0]요청시점, 차례)


"""