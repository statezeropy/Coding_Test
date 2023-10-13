def solution(priorities, location):
    answer = 0
    loc = []

    for i in range(len(priorities)):               # priorities와 길이가 같아질때까지 반복하기 위한 장치
                                                   # 인덱스가 끝나도 처음 인덱스로 돌아가기 위함
        for i in range(len(priorities)):
            if max(priorities) == priorities[i]:   # priority가 가장 높으면(max) 그 인덱스를 loc에 저장
                loc.append(i)                      # 다음 최댓값을 위해 해당 인덱스의 밸류를 0으로
                priorities[i] = 0                  # 그 다음 인덱스의 밸류가 최댓값이여도 바로 반영 가능

            if len(loc) == len(priorities):        
                break

        if len(loc) == len(priorities):            
                break    

    answer = loc.index(location) + 1

    return answer