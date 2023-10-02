def solution(citations):
    answer = 0
    citations = sorted(citations)
    n = len(citations)

    for i, c in enumerate(citations):
        h = n - i # n편 중 남아있는 논문 수, 모두 c 이상 인용
        if c >= h: # h번 이상 인용됨
            answer = h
            break
    return answer
