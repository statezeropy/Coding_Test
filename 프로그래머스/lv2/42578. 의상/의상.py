def solution(clothes):
    c = []
    for cloth in clothes:
        c.append(cloth[1])
    
    c_set = set(c)
    outcomes = 1

    for cloth in c_set:
        outcomes *= c.count(cloth) + 1

    return outcomes - 1