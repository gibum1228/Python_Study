"""
챕터: Day 5
주제: 매개변수의 전달 방식 비교
문제:
작성자: 김기범
작성일: 2018.10.04.
"""
"""
매개변수의 수정 여부 확인을 위한 함수 정의
call-by-value 방식으로 매개변수 값을 전달(독립적인 것이 장점)
매개변수 값을 복사(copy)하여 전달
"""
def modify1(s):
    s += " To you" # s 정의
    return s

msg = "Happy Birthday" # msg 정의
print("호출 전 msg =", msg) # msg 출력
re = modify1(msg) # modify 값을 re에 저장
print("호출 후 msg =", msg) # 함수 호출 후 msg 출력
print("re =", re) # re 출력