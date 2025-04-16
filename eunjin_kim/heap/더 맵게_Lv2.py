#38

import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    
    for _ in range(len(scoville)):
        food1 = hq.heappop(scoville)
        
        if food1 >= K:
            return answer
        
        if len(scoville) == 0:
            return -1
        
        food2 = hq.heappop(scoville)
        
        mix = food1 + food2 * 2
        hq.heappush(scoville, mix)
        answer += 1
    
    return answer