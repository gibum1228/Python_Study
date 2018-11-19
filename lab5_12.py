"""
챕터: Day 5
주제: 재귀함수(recursion)
- 자기 자신을 호출하는 함수
문제:
A. 곱하기를 더하기 반복문으로 구현한 함수 prod를 정의하여 prod(3, 6)을 계산하여 출력
작성자: 김기범
작성일: 2018.10.11.
"""
def prod(a, n) : # 함수 정의
    sum = 0 # 총합 초기화
    for i in range(0, n) :
        sum += a # 0~n-1만큼 a를 sum에 더하기
    print(sum) # 총합 출력

#재귀 함수를 이용하여 구현한 함수 r_prod
def r_prod(a, n) : # 재귀함수 정의
    if n == 1: # n이 1이라면
        return a # a를 출력하고
    else : # 아니면
        return a + r_prod(a, n-1) # n == 1 일 때까지 자신(함수)를 불러 3씩 더하기

prod(3, 6) # 시작 부분
print(r_prod(3, 6)) # r_rod() 반환값을 출력