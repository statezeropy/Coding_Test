# 재귀함수 recursive function
## 이론적으로 반복문과 동일한 기능을 구현할 수 있다. 재귀함수와 반복문은 어느한쪽이 항상 유리하지 않다.
## 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓입니다.
## 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많습니다.


# 팩토리얼 함수 구현 예시
## 반복문 사용 예시
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

## 재귀함수 사용 예시
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1 반환
        return 1
    # n * (n - 1)!
    return n * factorial_recursive(n-1)
print(f'반복문  예시: {factorial_iterative(5)}')
print(f'재귀함수 예시: {factorial_recursive(5)}')


# 최대공약수 계산 (유클리드 호제법) 예제
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
print(f'최대공약수: {gcd(192, 168)}')

