"""
챕터: Day 5
주제: lambda 함수의 리스트
문제:
작성자: 김기범
작성일: 2018.10.11.
"""
l = [lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4] # lambda함수로 l 초기화

for f in l : # f에 l 대입
    print(f(3)) # f에 매개변수 3 대입, x == 3