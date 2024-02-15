def solution(food):
    eat_food = ''
    for idx, i in enumerate(food[1:]):
        eat_food += str(idx+1) * (i//2)

    result = f'{eat_food}0{eat_food[::-1]}'
    return result