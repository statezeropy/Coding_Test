def solution(s):
    s = s.split()
    a = []
    for i in s:
        a.append(int(i))
        print(i)
        
    return f'{min(a)} {max(a)}'