def solution(s):
    a = [int(i) for i in s.split()]
    return f'{min(a)} {max(a)}'