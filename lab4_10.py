"""
챕터: Day 4
주제: 반복문(for 문)
문제:
사용자가 입력한 영문자를 아래와 같이 출력
예)
BINGO
 INGO
  NGO
   GO
    O
작성자: 김기범
작성일: 2018.09.27.
"""
S = input() # 문자열 입력받기

#1
for i in range(0, len(S)) : # 0부터 문자열 끝 앞 번호까지 반복문
    print(" " * i, end = "") # 줄 길이만큼 앞에 여백 늘리기
    print(S[i:]) # i부터 끝까지 출력하기


#2
for i in range(0, len(S)) : # 문자열 길이만큼 반복
    o = '' # o를 초기화
    for j in range(0, i) : # i만큼 공백 붙이기
        o = o + ' '
    for k in range(i, len(S)) : # 공백이 있는 o에 문자 붙이기
        o = o + S[k]
    print(o)