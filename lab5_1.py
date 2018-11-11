"""
챕터: Day 5
주제: 함수
문제:
두 개의 정수를 매개변수로 받아서, 두 수의 차를 반환하는 함수 subtract를 정의한다.
4, 8을 매개변수로 subtract를 호출한 후 결과를 출력한다.
작성자: 김기범
작성일: 2018.10.02.
"""
def subtract(a, b) : # 두 수의 차를 구하는 subtract 함수 정의
    # a는 첫 번째 매개변수, b는 두 번째 매개변수
    return a-b # 리턴 값이 a - b

print(subtract(4, 8)) # 함수를 호출하고 그 값을 출력하기, 위치에 의해 인수(매개변수)가 전달됨
print(subtract(b=4, a=8)) # 키워드 인수(매개변수), 파이썬만의 특징

a = 10 # int
b = True # bool
c = '김치' # string

print(type(a)) # 변수의 타입을 반환하는 함수
print(type(b))
print(type(c))