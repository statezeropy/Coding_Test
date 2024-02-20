def solution(k, score):
    result = []
    k_scores = []
    
    for i in score:
        k_scores.append(i)
        k_scores.sort(reverse=True)
        if len(k_scores) > k:
            k_scores.pop()
        result.append(k_scores[-1])
    return result