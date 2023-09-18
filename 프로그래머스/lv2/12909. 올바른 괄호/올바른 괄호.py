def solution(s):
    s = list(s)
    stack = []
    
    if s[0] == ')':
        return False
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            tmp = stack.pop()
            if tmp == ')':
                return False
    if stack:
        return False
    else :
        return True