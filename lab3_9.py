"""
챕터: day 3
주제: boolean
작성자: 김기범
작성일: 2018.09.13.
"""
# bool 타입 변수 정의
a = True
b = False
c = 100
f = bool(c) # int인 c를 bool 타입으로 변환
print(f)
print(bool(0))

# [3, 4, 5]를 bool로 형변환하여 출력
print(bool([3, 4, 5]))
# []는?
print(bool([]))