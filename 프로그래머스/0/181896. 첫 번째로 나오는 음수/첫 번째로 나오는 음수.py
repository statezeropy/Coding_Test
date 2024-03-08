def solution(num_list):
    if min(num_list) >= 0:
        return -1
    else:
        for i, n in enumerate(num_list):
            if n < 0: return i