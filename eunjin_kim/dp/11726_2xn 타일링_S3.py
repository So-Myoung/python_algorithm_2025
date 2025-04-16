import sys
n = int(sys.stdin.readline())


def tiling():
    if n == 1: return 1

    seq = [0] * (n+1)
    seq[0], seq[1], seq[2] = 0, 1, 2

    for i in range(3, n+1):
        seq[i] = (seq[i-1] + seq[i-2]) % 10007
    
    return seq[n]


print(tiling())

