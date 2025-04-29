def solution(answers):
    answer = []

    # 패턴 찾기
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0] * 3

    for i, a in enumerate(answers):
        for j, p in enumerate(patterns):
            if a == p[i % len(p)]:
                scores[j] += 1

    for i, score in enumerate(scores):
        if max(scores) == score:
            answer.append(i+1)

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
