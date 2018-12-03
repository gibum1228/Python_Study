"""
챕터: Day 6
주제: exception
문제: 사용자로부터 두 수를 입력받아, 첫번째 수를 두번째 수로 나눈 값을 출력한다.
두번째 수가 0이 입력되는 경우(ZeroDivisionError), '0으로 나눌 수 없습니다'라는 문장을 출력한 후
다시 두 수를 입력받아 계산한다
작성자: 김기범
작성일: 2018.11.27.
"""

while True:
    try:
        a, b = map(int, input("두 수를 입력(띄어쓰기로 구분): ").split()) # 두 수를 동시에 입력받기

        if a == 0: # a가 0일 경우
            t = a
            a = b
            b = t
        print("%d를 %d로 나눈 값: %d" % (a, b, a/b)) # 결과 출력

        break
    except ZeroDivisionError: # 두 번째 수가 0인 경우
        print('0으로 나눌 수 없습니다.')
    except ValueError: # 숫자를 입력받지 못 했을 때
        print("숫자를 입력하세요.")
