def solution(string):
    ans = True

    lists = list(string)
    signal = []

    for i in lists:
        if i == "(":
            signal.append(i)
        elif i == ")":
            if len(signal) == 0:
                ans = False
                return ans
            else:
                signal.pop()

    if len(signal) != 0: ans = False

    return ans


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
