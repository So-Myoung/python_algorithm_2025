def solution(participant, completion):
    runner = {}

    for p in participant:
        if p in runner:
            runner[p] += 1
        else:
            runner[p] = 1

    for c in completion:
        runner[c] -= 1

    for player, count in runner.items():
        if count != 0:
            return player
