def solution(n):
    a = 0
    b = 1
    answer = 0
    
    for i in range(n-1):
        answer = a + b
        a = b
        b = answer
    
    return answer%1234567