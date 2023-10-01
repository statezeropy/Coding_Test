def solution(want, number, discount):
    answer, wants = 0, []

    for v, n in zip(want, number):
        wants += [v]*n

    wants = sorted(wants)
    wants_len = len(wants)
    for i in range(len(discount[:(-wants_len)+1])):
        answer += int(wants == sorted(discount[i:wants_len+i]))

    return answer