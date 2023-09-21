def solution(n):
    answer = n
    cnt = bin(n).count('1')
    while True:
        answer += 1
        if bin(answer).count('1') == cnt:
            return answer