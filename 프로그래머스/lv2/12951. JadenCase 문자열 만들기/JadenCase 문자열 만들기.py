def solution(s):
    return ' '.join([i.lower().capitalize() for i in s.split(' ')])

# def trySolution(s):
#     s = [i.lower() for i in s.split(' ')]
#     a = []
#     for i in s:
#         a.append(i[0].upper()+i[1:].lower()) 
#     return ' '.join(a)
