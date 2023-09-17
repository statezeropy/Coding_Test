def solution(targets):
    targets.sort()
    answer = 0
    x = 0
    for s, e in targets:
        if x > s:
            x = min(x, e)
        else:
            x = e
            answer += 1

    return answer