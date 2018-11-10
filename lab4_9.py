"""
챕터: Day 4
주제: 반복문(for 문)
문제:
    밑변이 5개의 *로 구성된 직각 삼각형 출력
    거꾸로 된 직각 삼각형 출력
작성자: 김기범
작성일: 2018.09.20.
"""
#1
for i in range(5, 0, -1) :
    print('*' * i)

#2
for i in range(5, 0, -1) :
    for a in range(i, 0, -1) :
        print("*", end = '')
    print('')