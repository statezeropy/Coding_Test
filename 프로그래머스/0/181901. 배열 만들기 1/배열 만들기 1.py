def solution(n, k):
    answer = [k * (i+1) for i in range(n // k)]
    return answer