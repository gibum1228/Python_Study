"""
챕터: Day 6
주제: raise exception
문제: 사용자로부터 2 개의 정수를 입력받은 후 아래와 같은 메뉴를 선택하게 하여 그 결과를 출력하라
1. 덧셈
2. 뺄셈
3. 나눗셈
4. 곱셈

만약 2개의 정수를 입력받을 때, 정수가 아닌 수를 입력하면 "정수를 입력하세요"를 출력한 후 다시 입력받는다.
만약 메뉴 입력시 사용자가 1~4 사이의 수가 아니면, "메뉴를 다시 선택해 주세요"를 출력한 후 다시 입력받는다.
나눗셈의 경우, 두번째 수가 0이면 "0으로 나눌 수 없습니다."를 출력한다.

위의 세가지 경우를 exception을 이용하여 처리하라

작성자: 김기범
작성일: 2018.11.29.
"""
while True:
    try:
        a = int(input("첫 번쨰 숫자 입력: ")) # 2 개의 정수 입력받기
        b = int(input("두 번째 숫자 입력: "))

        while True:
            try:
                print("1.덧셈\n" # 메뉴 선택
                      "2.뺄셈\n"
                      "3.나눗셈\n"
                      "4.곱셈")
                menu = int(input("선택한 메뉴: ")) # menu 변수에 값 저장

                if (menu > 4) or (menu < 1): # 메뉴 값이 1~4 사이가 아니라면
                    raise ValueError # 에러

                break # 메뉴 선택 반복문 종료

            except ValueError: # 메뉴가 정수가 아니거나 조건(1~4)에 맞지 않을 경우
                print("메뉴를 다시 선택해주세요.")

        if menu == 1: # 메뉴 값의 따른 사칙연산 값 출력
            print("덧셈 값:", a+b)
        elif menu == 2:
            print("뺄셈 값:", a-b)
        elif menu == 3:
            print("나눗셈 값:", a/b)
        else:
            print("곱셈 값:", a*b)

        break # 프로그램 종료

    except ValueError: # 정수를 입력받지 못 했을 때
        print("정수를 입력하세요.")

    except ZeroDivisionError: # 두 번째 수가 0으로 나누어졌을 때
        print("0으로 나눌 수 없습니다.")
        break # 프로그램 종료