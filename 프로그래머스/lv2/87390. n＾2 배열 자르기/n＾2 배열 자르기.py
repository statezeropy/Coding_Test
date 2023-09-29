def solution(n, left, right):
    answer = []
    # t = 0
    # for row in range(n):
    #     t += 1
    #     for i in range(1, n+1):
    #         if t >= i:
    #             answer.append(t)
    #         else:
    #             answer.append(i)

    left_row = left // n
    left_column = left % n
    right_row = (right+1) // n
    right_column = (right+1) % n
    # print(left_row, left_column)
    # print(right_row, right_column)
    
    for row in range(left_row, right_row+1):
        for i in range(n):
            if row >= i:
                answer.append(row+1)
            else:
                answer.append(i+1)
    # print(answer)
    # print(answer[left_column:(right_row-left_row)*n+right_column])
    # 123 2
    # 223 6
    # 333
    # 1234
    # 2234 7~
    # 3334
    # 4444 ~15
        
    return answer[left_column:(right_row-left_row)*n+right_column]