def solution(s):

# answer = ''

# # 문자열을 모두 소문자로 변환
# #s = s.lower()

# # 공백을 기준으로 단어를 나누고, 각 단어의 첫 글자만 대문자로 변환
# words = s.split(" ")
# jaden_words = [word.capitalize() for word in words]

# # 다시 공백을 사용하여 단어를 결합
# answer = " ".join(jaden_words)



    # s = ' '.join([i.lower().capitalize() for i in s.split(' ')])
    # print(s)
#     t = ['3']
    
# #     a = []
# #     b = ''
#     for i in s:
#         if len(i) == 1:
#             a.append(i[0].upper())
#             b += i[0].upper()
#         # elif str(a) == ' ':
#         #     continue
#         else:
#             # print(i[0].upper()+i[1:].lower())
#             # print(''.join(i[0].upper()+i[1:].lower()))
        
#             a.append(i[0].upper()+i[1:].lower())
#             b += i[0].upper()+i[1:].lower()
#     # s = [i[0] = i[0].upper() for i in s]
#     # a = [(i[:1].upper()+i.lower()[1:]) for i in s]
#     # ' '.join([(i[:1].upper()+i.lower()[1:]) for i in s.split()])
#     # print(' '.join(a))
#     #' '.join(a)
    
    #a = [i.capitalize() for i in s]

    return ' '.join([i.lower().capitalize() for i in s.split(' ')])