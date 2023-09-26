from collections import deque
def solution(people, limit):
    answer = 0
    dq = deque()
    people.sort()
    
    for idx in range(len(people)):
        dq.append(people[idx])

    front = 0

    while(len(dq) > 1):
        if(dq[front] + dq[-1] > limit):
            answer += 1
            dq.pop()

        else:
            dq.pop()
            dq.popleft()
            answer += 1

    if(len(dq) == 1):       
        dq.popleft()
        answer += 1


    return answer