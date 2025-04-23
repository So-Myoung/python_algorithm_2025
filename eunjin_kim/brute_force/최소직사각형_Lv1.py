def solution(sizes):
    max_x = 0
    max_y = 0
    
    for x, y in sizes:
        max_x = max(max_x, x, y)
        max_y = max(max_y, min(x, y))
        
    return max_x * max_y