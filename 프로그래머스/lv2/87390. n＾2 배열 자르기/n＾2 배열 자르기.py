def solution(n, left, right):
    answer = []

    left_row = left // n
    left_column = left % n
    right_row = (right+1) // n
    right_column = (right+1) % n

    for row in range(left_row, right_row+1):
        for i in range(n):
            if row >= i:
                answer.append(row+1)
            else:
                answer.append(i+1)

        
    return answer[left_column:(right_row-left_row)*n + right_column]