"""
챕터: Day 4
주제: 조건문(elif 이용)
문제: 사용자로부터 점수를 입력받는다.
      0보다 크면 '양수', 0이면 '0', 0보다 작으면 '음수'를 출력한다.
작성자: 김기범
작성일: 2018.09.18.
"""

# 정수 입력받기
# 정수가 0보다 크면 양수 출력
# 그렇지 않고, 0이면 0 출력
# 그렇지 않으면 음수 출력

num = int(input("숫자 입력: "))

if(num > 0) :
    print("양수")
elif(num == 0) :
    print("0")
else :
    print("음수")