import math

def solution(brown, yellow):
    # a*x**2 + b*x + c = 0
    a = 1
    b = - (brown / 2 + 2)
    c = brown + yellow

    D = b**2 - 4*a*c

    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)

    answer = []
    answer.append(x1)
    answer.append(x2)


    return answer
