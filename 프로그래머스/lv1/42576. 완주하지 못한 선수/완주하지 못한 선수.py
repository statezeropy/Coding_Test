from collections import Counter
def solution(participant, completion):
    participant_dict = dict(Counter(participant))
    completion_dict = dict(Counter(completion))
    for name,count in participant_dict.items():
        if name in completion_dict:
            if count != completion_dict[name]:
                print(completion_dict[name])
                return name
        else:
            return name
