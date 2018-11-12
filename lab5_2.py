"""
챕터: Day 5
주제: 함수
문제:
문자열의 튜플을 매개변수로 받아서, 해당 문자열들을 ','로 한 줄에 연결하여 출력하는 함수 print_string을 정의한다.
소프트웨어공학과, 정보통신공학과, 글로컬IT학과, 컴퓨터공학과를 요소로 가지고 있는 튜플을 매개변수로 해서 print_string을 호출한다,
작성자: 김기범
작성일: 2018.10.02.
"""
tuple1 = ("소프트웨어공학과", "정보통신공학과", "글로컬IT학과", "컴퓨터공학과") # 튜플 정의

# 1
def print_string(t) : # 함수 정의
    list1 = "" # 빈 문자열 list1 정의
    for i in range(0, len(t)) : # t의 길이만큼 반복하기
        list1 += t[i] # list1에 t[i] 더하기
        if i != len(t)-1 : # i 가  len(t)-1이 아니라면
            list1 += "," # list1에 ", " 더하기
    return list1; # list1 반환하기
print(print_string(tuple1)) # 함수를 호출하고 출력하기
# return을 사용하지 않을 경우, print(list1)으로 바꾸고 print_string(tuple1)로 바꾸면 됨


# 2
def print_string(t) : # 함수를 정의
    s = len(t) - 1
    for i in t : # i에다가 t 대입
        if i == t[s] : # i가 t[3] 값이라면
            print(t[s]) # t[3] 출력
            break; # 반복문 강제 종료
        print(i, end = ",") # i + ", " 출력하기
print_string(("소프트웨어공학과", "정보통신공학과", "글로컬IT학과", "컴퓨터공학과")) # 함수 호출하기