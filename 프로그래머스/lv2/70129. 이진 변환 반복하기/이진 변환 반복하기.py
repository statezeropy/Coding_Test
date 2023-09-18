def solution(s):
    zero = 0
    count = 0
    
    while True:
        if s == '1':
            break
        size = len(s)
        zero += s.count('0')
        s = bin(s.count('1')).replace('0b', '')
        count += 1

    return [count, zero]