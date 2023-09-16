def solution(s):
    answer = 0
    for t in range(len(s)):
        tmp = list(s)
        for i in list(s):
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")

        if s == "":
            answer += 1
        
        
        tmp.append(tmp.pop(0))
        s = ''.join(tmp)
    return answer