def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i,j in zip(A,B):
        answer += i * j
        print(i, j, answer)
    

    return answer