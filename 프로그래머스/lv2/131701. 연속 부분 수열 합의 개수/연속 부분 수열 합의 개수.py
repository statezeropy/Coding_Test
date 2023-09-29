def solution(elements):
    sums, n = [], len(elements)
    elements += elements[:-1]
    for i, a in enumerate(elements):
        SUM = a
        sums.append(SUM)
        for b in elements[i + 1:i + n]:
            SUM += b
            sums.append(SUM)

    return len(list(set(sums)))
