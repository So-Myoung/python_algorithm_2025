def solution(s):
    stack = []
    
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        elif len(stack):
            stack.pop()
        else:
            return False

    if stack:
        return False
    
    return True