import math

def solution(progresses, speeds):
    answer = []
    
    leng = len(progresses)
    if leng == 0:
        return answer
    
    answer = [1]
    update = math.ceil((100 - progresses[0]) / speeds[0])
    
    for i in range(1, leng):
        x = math.ceil((100 - progresses[i]) / speeds[i])
        
        if x <= update:
            answer[-1] += 1
        else:
            answer.append(1)
            update = x

    return answer