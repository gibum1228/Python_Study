"""
챕터: Day 6
주제: raise exception
문제: 사용자로부터 숫자를 입력받아 0 이하 또는 100 초과의 점수가 입력되면, ValueError 발생(raise)시키고,
"1과 100사이의 수를 입력해주세요" 출력
작성자: 김기범
작성일: 2018.11.29.
"""


n = int(input("숫자 입력: "))

if (n <= 0) or (n > 100):
    raise ValueError ("1과 100 사이의 수를 입력해주세요.")