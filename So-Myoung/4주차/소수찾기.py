from itertools import permutations
import math


# 소수 = 약수가 1과 자기 자신
def isPrime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    per_list = []
    num_list = []

    for i in range(1, len(numbers) + 1):
        per_list.extend(set(permutations(numbers, i)))

    for per in per_list:
        if per[0] != '0':
            num_list.append(int(''.join(per)))

    for num in num_list:
        if isPrime(num):
            answer += 1

    return answer


print(solution("17"))
print(solution("011"))