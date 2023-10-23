def solution(N):
    zeros = bin(N).split('1')[1:]
    if len(zeros) <= 1:
        return 0
    else:
        return len(max(zeros[:-1]))
