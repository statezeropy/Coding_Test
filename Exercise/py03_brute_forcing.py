def solution1(n=3):
    # 0 <= N <= 23
    # 00시 00분 00초 ~ N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력
    count = 0
    h = 0
    m = 0
    s = 0

    while h <= n:
        if '3' in f'{h}{m}{s}': # '3'이 포함된 경우
            count += 1
        
        s += 1 # 1초 추가
        if s >= 60: # 1분
            m += 1
            s = 0
        if m >= 60: # 1시간
            h += 1
            m = 0
    print(count)

def solution2(h=3):
    # 0 <= N <= 23
    # 00시 00분 00초 ~ N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력
    count = 0
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                if '3' in f'{i}{j}{k}':
                    count += 1
    print(count)
    
# 왕실의 나이트 움직임 경우의 수. simulations, brute-force search
def solution3(coordinate='a1'):
    # 나이트 이동 방향 정의
    steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    # 나이트 이동 횟수 초기값
    result = 0

    # 입력된 나이트 위치를 가로/세로 분리 및 1~8로 변환
    row = int(coordinate[1])
    column = int(ord(coordinate[0])) - int(ord('a')) + 1

    # 이동 방향별 가능 여부 확인
    for step in steps:
        if 1 <= row + step[0] <= 8 and 1 <= column + step[1] <= 8:
            result += 1
    print(result)
    return result

# 문자열 재정렬
import re
def solution4(s='K1KA5CB7'):
    text = re.sub(r'\d', '', s)
    numbers = re.sub(r'[^0-9]', '', s)

    results = ''.join(sorted(text)) + ''.join(sorted(numbers))
    print(results)

solution4()

def solution5(s='K1KA5CB7'):
    result = []
    value = 0

    # 문자열 하나씩 확인하며
    for x in s:
        if x.isalpha(): # 알파벳인 경우
            result.append(x)
        else: # 알파벳이 아닌경우 (숫자일 경우)
            value += int(x)

    result.sort() # 문자열 정렬

    if value != 0: # 정렬된 문자열 뒤에 정렬된 숫자 추가
        result.append(str(value))

    print(''.join(result)) # 리스트를 하나의 문자열로 출력