def solution(s):
    stack = []

    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                return False

    return False if stack else True
