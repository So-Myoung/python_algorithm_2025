import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) >= 2:
                
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        if a == 0 and b == 0:
            return -1
        
        heapq.heappush(scoville, a+(b*2))
        answer += 1
    
    if scoville[0] < K:
        return -1
            
    return answer
