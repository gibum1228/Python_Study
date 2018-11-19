"""
챕터: Day 5
주제: 재귀함수(recursion)
자기 자신을 호출하는 함수
문제:
A. 팩토리얼 계산 함수 fact를 재귀함수로 정의하여, fact(5)를 호출한 결과를 출력하라.
작성자: 김기범
작성일: 2018.10.11.
"""
def fact(a) : # 재귀함수 fact 정의
    if a == 1 : # a가 1이면
        return 1 # 1 반환
    else :
        return a * fact(a-1) # 재귀함수

print(fact(5)) # 매개변수 5로 호출