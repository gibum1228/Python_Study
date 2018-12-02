"""
챕터: Day 6
주제: exception
문제: 사용자로부터 숫자를 입력받아, 1부터 해당 숫자까지의 합을 구하라.
만약 숫자가 아닌 값이 입력되면, "숫자를 입력하세요"라는 문장을 출력한 후
다시 입력을 받는다
작성자: 김기범
작성일: 2018.11.27.
"""

# exception을 사용하지 않고 프로그랭
import re # regular expression 모듈을 수입

sum = 0 # 합을 저장하는 변수 정의
while True: # 숫자가 입력될 때까지 반복
    n = input("숫자 입력: ") # 입력받기
    r = re.compile("^[0-9]+$") # 숫자인지 확인하기 위해 숫자 패턴 정의

    if (r.search(n) == None): # 숫자가 아니라면
        print("숫자를 입력하세요")
        continue # 다시 입력받기

    for i in range(1, int(n)+1): # 숫자인 경우 합 구하기
        sum += i
    break # 합을 구했으니 반복문 벗어나기

print(n, "까지의 합: ", sum) # 출력