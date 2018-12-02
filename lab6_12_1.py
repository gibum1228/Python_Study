"""
챕터: Day 6
주제: exception
문제: 사용자로부터 숫자를 입력받아, 1부터 해당 숫자까지의 합을 구하라.
만약 숫자가 아닌 값이 입력되면, "숫자를 입력하세요"라는 문장을 출력한 후
다시 입력을 받는다
작성자: 김기범
작성일: 2018.11.27.
"""

# exception을 사용하여 프로그래밍

sum = 0 # 합을 저장할 변수 정의

while True: # 숫자를 입력할 때까지 반복
    try: # 숫자값이 입력되는지 검사를 위해 try 사용
        n = int(input("숫자 입력: ")) # int로 변환되는 과정에서 ValueError 발생시 except로 이동
        for i in range(1, n+1): # 오류 발생되지 않을 경우 합 구하기
            sum += i
        break # 합을 구했으므로 반복문 종료
    except ValueError: # 숫자가 입력되지 않은 Exception 잡기
        print("숫자를 입력하세요")

print(n, "까지의 합: ", sum) # 결과 출력