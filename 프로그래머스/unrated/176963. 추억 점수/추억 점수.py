def solution(name, yearning, photo):
    answer = []
    name_dict = dict(zip(name, yearning))
    # photo_dict = dict(zip(photo, 0))
    for people in photo:
        result = 0
        for person in people:
            if person in name_dict:
                result += name_dict[person]
        answer.append(result)
            
    
    return answer