def solution(seq, k):

    start, end, total = 0, 0, seq[0]
    seq += [0]
    first, second = 1000000, 2000000

    while end < len(seq) - 1:
        if total <= k:
            if total == k and end - start < second - first:
                first, second = start, end
            end += 1
            total += seq[end]
        else:
            start += 1
            total -= seq[start - 1]

    return [first, second]