#prime : 9_999_999까지의 소수여부를 저장한 배열. (1은 소수, 0은 소수x) --> 실행속도 1000ms 이상 👎
def get_is_prime():
    is_prime = [0, 1] * ((10_000_000) // 2)
    is_prime[1], is_prime[2] = 0, 1

    for i in range(3, int(10_000_000 ** 0.5) + 1, 2):
        if is_prime[i] == 0:
            continue
        for j in range(i+i, 10_000_000, i): #배수는 소수x
            is_prime[j] = 0
            
    return is_prime


def permutation(string, numbers, visited, set_num):
    set_num.add(int(string))
    
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = 1
            permutation(string + numbers[i], numbers, visited, set_num) 
            visited[i] = 0


def solution(numbers):  
    visited = [0] * len(numbers)
    set_num = set()
    permutation('0', numbers, visited, set_num)
    
    cnt = 0
    is_prime = get_is_prime()
    for num in set_num:
        cnt += is_prime[num]
        
    return cnt



'''
#prime 배열없이 + set --> 최대 14ms 👍

def isPrime(num):
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            return False
    return True


def solution(numbers):
    length = len(numbers)
    visited = [0]*length
    seT = set()

    def dfs(v, number):
        if number:  # 0, 1은 소수가 아니므로 제외
            seT.add(int(''.join(number)))

        for i in range(length):
            if visited[i] == 0:
                visited[i] = 1
                number.append(numbers[i])
                dfs(v+1, number)
                visited[i] = 0
                number.pop()

    dfs(0, [])

    cnt = 0
    print(seT)
    for l in seT:
        if l > 1:
            if isPrime(l):
                cnt += 1

    return cnt
'''