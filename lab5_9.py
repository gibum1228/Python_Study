"""
챕터: Day 5
주제: 매개변수의 전달 방식 비교(call-by-reference), 전역변수
문제:
A. list를 받아서, 마지막 리스트의 요소의 개수를 요소로 추가하는 함수 addNum을 정의한다. 반환되는 값은 없다.
B. [5, 9, 14, 3]을 저장하는 list를 변수 l를 정의한다.
C. l을 인수로 addNum함수를 호출한 후 l을 출력한다.
작성자: 김기범
작성일: 2018.10.11.
"""
# 매개변수의 수정 여부 확인을 위한 함수 정의
# call by reference 방식으로 매개변수 값을 전달

global_v = 100 # 전역변수

def addNum(a) : # a와 l가 똑같은 리스트를 가리킴
    global global_v # 전역변수로 정의, 정의 안 하면 global_v 값은 100
    global_v = 200 # 값을 변경
    a.append(len(l)) # a[마지막]에 길이 추가

l = [5, 9, 14, 3] # l을 초기화
print(l) # 호출 전 출력
addNum(l) # 함수 호출
print(l) # 호출 후 출력
print(global_v)
