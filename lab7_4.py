"""
챕터: Day 7
주제: file 쓰기
문제:
현재 디렉토리 아래에 fruits.txt 파일을 생성하여, 사용자가 입력하는 과일을 한 줄에 하나씩 3개를 저장하라

작성자: 김기범
작성일: 2018.12.06.
"""

f = open("fruits.txt", "wt") # fruits.txt 파일을 쓰기 위해서 열기, "at"는 append 이므로 뒤에 이어서 텍스트를 추가해준다(이어쓰기)

for i in range(0, 3):
    fname = input("과일이름: ") # 입력받기
    f.write(fname) # 입력 받은 과일을 파일에 쓰기
    f.write(":") # 과일이름과 가격 사이에 :을 저장
    
    price = int(input("가격: ")) # 가격을 정수로 받음
    f.write(str(price)) # 가격 저장, 문자 파일에 저장하기 위해서 정수를 문자열로 바꿔서 저장해줘야된다

    f.write("\n") # 한 줄에 하나씩 저장하기 위해 뉴라인


f.close() # 파일 닫기