def solution(arr):
    stack = [arr[0]]

    for n in arr[1:]:
        if n != stack[-1]:
            stack.append(n)

    return stack
