import math
def solution(progresses, speeds):
    days = []

    for progress, speed in zip(progresses, speeds):
        day = math.ceil((100 - progress) / speed)
        days.append(day)

    max_day = 0
    answer = []

    for day in days:
        if not answer or max_day < day:
            answer.append(1)
            max_day = day
        else:
            answer[-1] += 1

    return answer