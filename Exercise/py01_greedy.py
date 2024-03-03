def solution1():
    N, K = 29, 5
    result = 0

    while True:
        # 1 빼기 횟수: N - target
        target = (N // K) * K
        result += N - target
        N = target

        # N이 K보다 작은 경우 나눌수 없다.
        if N < K:
            break
        
        # 나누기 과정 진행
        result += 1
        N //= K

    # N이 1이 될 때 까지 횟수
    result += N - 1
    print(result)

# solution1()


def solution2(s):
    result = int(s[0]) # 첫 번째 문자를 result 변수에 할당
    for num in s[1:]: # 두 번째 문자부터 호출
        num = int(num) # 자료형 변환
        if result <= 1 or num <= 1: # result, num 둘 중 하나라도 1 이하인 경우
            result += num # 덧샘 연산
        else:
            result *= num # 곱셈 연산
    print(result)
# s = '567' # 입력 예시
# solution2(s)


def solution3(fear_score):
    fear_score = sorted(fear_score) # 오름차순 정렬
    result = 0 # 총 그룹의 수
    member = 0 # 그룹의 인원
    for fear in fear_score: # 공포도 호출
        member += 1 # 그룹의 인원 추가
        if member >= fear: # 인원 >= 공포도인 경우
            result += 1 # 완성된 그룹 추가
            member = 0 # 인원 초기화
    print(result)
fear_score = [2, 3, 1, 2, 2] # 입력
solution3(fear_score=fear_score)
